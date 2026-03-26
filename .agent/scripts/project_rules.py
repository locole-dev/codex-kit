#!/usr/bin/env python3
"""
Project Rules Sync - Locole Kit
===============================

Analyze a project and generate a stable project-specific rule file that agents
can read before implementation work.

Usage:
    python .agent/scripts/project_rules.py sync [path]
    python .agent/scripts/project_rules.py print [path]
    python .agent/scripts/project_rules.py info [path]
"""

from __future__ import annotations

import argparse
import json
import os
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

GENERATED_START = "<!-- locole:project-rules:start -->"
GENERATED_END = "<!-- locole:project-rules:end -->"
OUTPUT_RELATIVE_PATH = Path(".agent") / "PROJECT_RULES.md"
MANUAL_HEADER = "## Manual Overrides"
IGNORED_DIRS = {
    ".agent",
    ".codex",
    ".git",
    ".next",
    ".nuxt",
    ".svelte-kit",
    ".turbo",
    "build",
    "coverage",
    "dist",
    "node_modules",
    "out",
    "vendor",
    "__pycache__",
}

LANGUAGE_MAP = {
    ".ts": "TypeScript",
    ".tsx": "TypeScript",
    ".js": "JavaScript",
    ".jsx": "JavaScript",
    ".py": "Python",
    ".rs": "Rust",
    ".go": "Go",
    ".java": "Java",
    ".kt": "Kotlin",
    ".swift": "Swift",
    ".vue": "Vue SFC",
    ".svelte": "Svelte",
}


def read_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8-sig"))
    except Exception:
        return {}


def detect_package_manager(root: Path) -> Optional[str]:
    if (root / "pnpm-lock.yaml").exists():
        return "pnpm"
    if (root / "yarn.lock").exists():
        return "yarn"
    if (root / "bun.lockb").exists() or (root / "bun.lock").exists():
        return "bun"
    if (root / "package-lock.json").exists():
        return "npm"
    return None


def detect_monorepo(root: Path, package_data: Dict[str, Any]) -> bool:
    return bool(
        package_data.get("workspaces")
        or (root / "pnpm-workspace.yaml").exists()
        or (root / "turbo.json").exists()
        or (root / "nx.json").exists()
    )


def iter_project_files(root: Path) -> Iterable[Path]:
    for current_root, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in IGNORED_DIRS]
        base = Path(current_root)
        for filename in files:
            yield base / filename


def detect_languages(root: Path) -> List[str]:
    counts: Counter[str] = Counter()
    for file_path in iter_project_files(root):
        language = LANGUAGE_MAP.get(file_path.suffix.lower())
        if language:
            counts[language] += 1
    return [name for name, _ in counts.most_common(4)]


def detect_frameworks(root: Path, package_data: Dict[str, Any]) -> List[str]:
    deps = {
        **package_data.get("dependencies", {}),
        **package_data.get("devDependencies", {}),
    }
    frameworks: List[str] = []

    def add(value: str) -> None:
        if value not in frameworks:
            frameworks.append(value)

    if "next" in deps:
        add("Next.js")
    if "react" in deps:
        add("React")
    if "vue" in deps:
        add("Vue")
    if "nuxt" in deps:
        add("Nuxt")
    if "svelte" in deps or "@sveltejs/kit" in deps:
        add("Svelte")
    if "express" in deps:
        add("Express")
    if "@nestjs/core" in deps or "nestjs" in deps:
        add("NestJS")
    if "fastify" in deps:
        add("Fastify")
    if "react-native" in deps:
        add("React Native")
    if "expo" in deps:
        add("Expo")
    if (root / "pyproject.toml").exists():
        pyproject = (root / "pyproject.toml").read_text(encoding="utf-8", errors="ignore").lower()
        if "fastapi" in pyproject:
            add("FastAPI")
        if "django" in pyproject:
            add("Django")
        if "flask" in pyproject:
            add("Flask")
    if (root / "requirements.txt").exists():
        requirements = (root / "requirements.txt").read_text(encoding="utf-8", errors="ignore").lower()
        if "fastapi" in requirements:
            add("FastAPI")
        if "django" in requirements:
            add("Django")
        if "flask" in requirements:
            add("Flask")
    if (root / "pubspec.yaml").exists():
        pubspec = (root / "pubspec.yaml").read_text(encoding="utf-8", errors="ignore").lower()
        if "flutter" in pubspec:
            add("Flutter")

    return frameworks


def detect_style_tools(root: Path, package_data: Dict[str, Any]) -> List[str]:
    deps = {
        **package_data.get("dependencies", {}),
        **package_data.get("devDependencies", {}),
    }
    tools: List[str] = []

    def add(value: str) -> None:
        if value not in tools:
            tools.append(value)

    if "tailwindcss" in deps:
        add("Tailwind CSS")
    if "sass" in deps or "node-sass" in deps:
        add("Sass")
    if "styled-components" in deps:
        add("styled-components")
    if "@emotion/react" in deps:
        add("Emotion")
    if "@mui/material" in deps:
        add("MUI")
    if (root / "components.json").exists():
        add("shadcn/ui")

    if not tools:
        if any(path.name.endswith(".module.css") for path in iter_project_files(root)):
            add("CSS Modules")
        elif any(path.suffix.lower() == ".css" for path in iter_project_files(root)):
            add("CSS")

    return tools


def detect_testing_tools(package_data: Dict[str, Any]) -> List[str]:
    deps = {
        **package_data.get("dependencies", {}),
        **package_data.get("devDependencies", {}),
    }
    tools: List[str] = []

    def add(value: str) -> None:
        if value not in tools:
            tools.append(value)

    if "vitest" in deps:
        add("Vitest")
    if "jest" in deps:
        add("Jest")
    if "@playwright/test" in deps or "playwright" in deps:
        add("Playwright")
    if "cypress" in deps:
        add("Cypress")
    if "pytest" in deps:
        add("Pytest")

    return tools


def detect_quality_tools(root: Path, package_data: Dict[str, Any]) -> List[str]:
    deps = {
        **package_data.get("dependencies", {}),
        **package_data.get("devDependencies", {}),
    }
    tools: List[str] = []

    def add(value: str) -> None:
        if value not in tools:
            tools.append(value)

    if "eslint" in deps or (root / ".eslintrc").exists() or (root / "eslint.config.js").exists():
        add("ESLint")
    if "prettier" in deps or (root / ".prettierrc").exists():
        add("Prettier")
    if "@biomejs/biome" in deps or (root / "biome.json").exists():
        add("Biome")
    if (root / "tsconfig.json").exists():
        tsconfig = read_json(root / "tsconfig.json")
        compiler_options = tsconfig.get("compilerOptions", {})
        if isinstance(compiler_options, dict) and compiler_options.get("strict") is True:
            add("TypeScript strict mode")

    return tools


def detect_layout(root: Path) -> List[str]:
    candidates = {
        "app": [root / "app", root / "src" / "app"],
        "src": [root / "src"],
        "pages": [root / "pages", root / "src" / "pages"],
        "components": [root / "components", root / "src" / "components"],
        "features": [root / "features", root / "src" / "features"],
        "modules": [root / "modules", root / "src" / "modules"],
        "api": [root / "api", root / "src" / "api"],
        "server": [root / "server", root / "src" / "server"],
        "prisma": [root / "prisma"],
        "tests": [root / "tests", root / "src" / "tests"],
        "e2e": [root / "e2e"],
    }
    detected: List[str] = []
    for label, paths in candidates.items():
        if any(path.exists() for path in paths):
            detected.append(label)
    return detected


def command_map(package_data: Dict[str, Any]) -> Dict[str, str]:
    scripts = package_data.get("scripts", {})
    if not isinstance(scripts, dict):
        return {}
    ordered_keys = ["dev", "build", "lint", "test", "typecheck", "format"]
    result: Dict[str, str] = {}
    for key in ordered_keys:
        if key in scripts:
            result[key] = str(scripts[key])
    return result


def infer_rules(data: Dict[str, Any]) -> List[str]:
    rules: List[str] = []
    frameworks = data["frameworks"]
    languages = data["languages"]
    style_tools = data["style_tools"]
    testing_tools = data["testing_tools"]
    quality_tools = data["quality_tools"]
    layout = data["layout"]
    package_manager = data["package_manager"]
    scripts = data["commands"]

    if package_manager:
        rules.append(f"Use `{package_manager}` for install and lifecycle commands when working in this repo.")

    if data["monorepo"]:
        rules.append("Treat this repository as a workspace/monorepo and scope commands to the affected package before editing or testing.")

    if "TypeScript" in languages:
        rules.append("Prefer TypeScript for new code and keep types aligned with the existing type boundaries.")
    elif "JavaScript" in languages and "TypeScript" not in languages:
        rules.append("Stay in JavaScript by default; do not introduce TypeScript unless the user asks for it.")

    if "Next.js" in frameworks:
        if "app" in layout:
            rules.append("Follow the Next.js App Router structure already present under `app/` and keep server/client boundaries explicit.")
        elif "pages" in layout:
            rules.append("Follow the existing Next.js Pages Router conventions and avoid mixing routing styles without a reason.")
    elif "React" in frameworks:
        rules.append("Preserve the existing React component structure and state-management style instead of introducing a new pattern.")
    elif "Vue" in frameworks or "Nuxt" in frameworks:
        rules.append("Keep changes aligned with the existing Vue/Nuxt single-file component structure and conventions.")
    elif "React Native" in frameworks or "Expo" in frameworks:
        rules.append("Stay within the mobile app architecture already present and avoid bringing in web-only patterns.")
    elif "Flutter" in frameworks:
        rules.append("Follow the existing Flutter project structure and keep Dart-specific patterns consistent across features.")

    if "Tailwind CSS" in style_tools:
        rules.append("Prefer Tailwind utilities and existing design tokens; avoid introducing a second styling system.")
    elif "CSS Modules" in style_tools:
        rules.append("Prefer CSS Modules where styling is component-scoped instead of adding a new styling stack.")
    elif style_tools:
        rules.append(f"Match the existing styling stack ({', '.join(style_tools)}) instead of mixing in new styling tools.")

    if "prisma" in data["dependency_names"]:
        rules.append("When data models change, keep Prisma schema, migrations, and generated client usage in sync.")

    if "Vitest" in testing_tools:
        rules.append("Add or update tests with Vitest rather than introducing a new unit-test runner.")
    elif "Jest" in testing_tools:
        rules.append("Add or update tests with Jest rather than introducing a second unit-test runner.")
    elif testing_tools:
        rules.append(f"Use the existing testing stack ({', '.join(testing_tools)}) for verification work.")
    else:
        rules.append("No dedicated test runner was detected; add tests only when they fit the existing repo style or the user asks for them.")

    if "Playwright" in testing_tools:
        rules.append("Use Playwright for end-to-end coverage when UI flows need browser verification.")

    if quality_tools:
        rules.append(f"Respect the repository quality tools: {', '.join(quality_tools)}.")

    if "src" in layout:
        rules.append("Keep new application code inside `src/` unless a nearby pattern shows otherwise.")

    if scripts.get("lint"):
        rules.append("Run the existing lint command after meaningful code changes.")
    if scripts.get("test"):
        rules.append("Use the repo's existing test command before closing work that changes behavior.")

    unique_rules: List[str] = []
    for rule in rules:
        if rule not in unique_rules:
            unique_rules.append(rule)
    return unique_rules[:10]


def collect_data(root: Path) -> Dict[str, Any]:
    package_data = read_json(root / "package.json")
    dependency_names = {
        **package_data.get("dependencies", {}),
        **package_data.get("devDependencies", {}),
    }

    data = {
        "project_name": package_data.get("name") or root.name,
        "root": str(root),
        "package_manager": detect_package_manager(root),
        "monorepo": detect_monorepo(root, package_data),
        "languages": detect_languages(root),
        "frameworks": detect_frameworks(root, package_data),
        "style_tools": detect_style_tools(root, package_data),
        "testing_tools": detect_testing_tools(package_data),
        "quality_tools": detect_quality_tools(root, package_data),
        "layout": detect_layout(root),
        "commands": command_map(package_data),
        "dependency_names": dependency_names,
    }
    data["rules"] = infer_rules(data)
    return data


def format_list(values: List[str], fallback: str = "Not detected") -> str:
    return ", ".join(values) if values else fallback


def generated_section(data: Dict[str, Any]) -> str:
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    command_lines = [f"- `{name}`: `{command}`" for name, command in data["commands"].items()]
    if not command_lines:
        command_lines.append("- No common lifecycle scripts were detected.")

    rule_lines = [f"{index}. {rule}" for index, rule in enumerate(data["rules"], start=1)]
    if not rule_lines:
        rule_lines.append("1. No strong project-specific code rules were detected; follow the closest local patterns in the touched files.")

    return "\n".join(
        [
            GENERATED_START,
            f"_Generated by `python .agent/scripts/project_rules.py sync .` on {timestamp}_",
            "",
            "## Project Snapshot",
            f"- Project: `{data['project_name']}`",
            f"- Root: `{data['root']}`",
            f"- Package manager: `{data['package_manager'] or 'not detected'}`",
            f"- Monorepo: `{'yes' if data['monorepo'] else 'no'}`",
            f"- Primary languages: {format_list(data['languages'])}",
            f"- Frameworks/runtime: {format_list(data['frameworks'])}",
            f"- Styling: {format_list(data['style_tools'])}",
            f"- Testing: {format_list(data['testing_tools'])}",
            f"- Quality tools: {format_list(data['quality_tools'])}",
            f"- Layout hints: {format_list(data['layout'])}",
            "",
            "## Preferred Commands",
            *command_lines,
            "",
            "## Generated Working Rules",
            *rule_lines,
            GENERATED_END,
        ]
    ).strip()


def extract_manual_section(existing_text: str) -> str:
    marker_index = existing_text.find(MANUAL_HEADER)
    if marker_index >= 0:
        return existing_text[marker_index:].strip()
    return "\n".join(
        [
            MANUAL_HEADER,
            "",
            "- Add stable repo-specific decisions here.",
            "- This section is preserved every time the project rule is synced.",
        ]
    )


def build_markdown(data: Dict[str, Any], existing_text: str = "") -> str:
    manual = extract_manual_section(existing_text)
    return "\n\n".join(
        [
            "# Project Rules",
            "Read this file before implementation work when it exists. The generated section can be refreshed at any time, while the manual section is preserved across syncs.",
            generated_section(data),
            manual,
            "",
        ]
    )


def sync_rules(root: Path) -> Path:
    target = root / OUTPUT_RELATIVE_PATH
    target.parent.mkdir(parents=True, exist_ok=True)
    existing_text = target.read_text(encoding="utf-8") if target.exists() else ""
    target.write_text(build_markdown(collect_data(root), existing_text), encoding="utf-8")
    return target


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate or refresh project-specific coding rules")
    parser.add_argument("command", choices=["sync", "print", "info"], help="Action to run")
    parser.add_argument("path", nargs="?", default=".", help="Project path")
    args = parser.parse_args()

    root = Path(args.path).resolve()
    data = collect_data(root)

    if args.command == "info":
        print(json.dumps(data, indent=2))
        return

    if args.command == "print":
        print(build_markdown(data))
        return

    target = sync_rules(root)
    print(f"[OK] Project rules synced: {target}")
    print("Read this file before implementation work:")
    print(f"  {target}")


if __name__ == "__main__":
    main()
