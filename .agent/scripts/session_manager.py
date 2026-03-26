#!/usr/bin/env python3
"""
Session Manager - Locole Kit
============================

Analyzes project state, detects tech stack, tracks file statistics, and
provides a summary of the current session.

Usage:
    python .agent/scripts/session_manager.py status [path]
    python .agent/scripts/session_manager.py info [path]
"""

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, List


def get_project_root(path: str) -> Path:
    return Path(path).resolve()


def read_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def analyze_package_json(root: Path) -> Dict[str, Any]:
    pkg_file = root / "package.json"
    if not pkg_file.exists():
        return {
            "name": root.name,
            "version": "0.0.0",
            "type": "unknown",
            "dependencies": {},
            "stack": [],
            "scripts": [],
        }

    try:
        data = read_json(pkg_file)
        deps = data.get("dependencies", {})
        dev_deps = data.get("devDependencies", {})
        all_deps = {**deps, **dev_deps}

        stack = []
        if "next" in all_deps:
            stack.append("Next.js")
        elif "react" in all_deps:
            stack.append("React")
        elif "vue" in all_deps:
            stack.append("Vue")
        elif "svelte" in all_deps:
            stack.append("Svelte")
        elif "express" in all_deps:
            stack.append("Express")
        elif "nestjs" in all_deps or "@nestjs/core" in all_deps:
            stack.append("NestJS")

        if "tailwindcss" in all_deps:
            stack.append("Tailwind CSS")
        if "prisma" in all_deps:
            stack.append("Prisma")
        if "typescript" in all_deps:
            stack.append("TypeScript")

        return {
            "name": data.get("name", "unnamed"),
            "version": data.get("version", "0.0.0"),
            "stack": stack,
            "scripts": list(data.get("scripts", {}).keys()),
        }
    except Exception as exc:
        return {
            "name": root.name,
            "version": "0.0.0",
            "stack": [],
            "scripts": [],
            "error": str(exc),
        }


def count_files(root: Path) -> Dict[str, int]:
    stats = {"created": 0, "modified": 0, "total": 0}
    exclude = {".git", "node_modules", ".next", "dist", "build", ".agent", ".codex", "__pycache__"}

    for root_dir, dirs, files in os.walk(root):
        dirs[:] = [directory for directory in dirs if directory not in exclude]
        stats["total"] += len(files)

    return stats


def detect_features(root: Path) -> List[str]:
    features = []
    src = root / "src"
    if src.exists():
        possible_dirs = ["components", "modules", "features", "app", "pages", "services"]
        for directory in possible_dirs:
            path = src / directory
            if path.exists() and path.is_dir():
                for child in path.iterdir():
                    if child.is_dir():
                        features.append(child.name)
    return features[:10]


def print_status(root: Path) -> bool:
    info = analyze_package_json(root)
    stats = count_files(root)
    features = detect_features(root)

    print("\n=== Project Status ===")
    print(f"\nProject: {info.get('name', root.name)}")
    print(f"Path: {root}")
    print(f"Type: {', '.join(info.get('stack', ['Generic']))}")
    print("Status: Active")

    print("\nTech Stack:")
    if info.get("stack"):
        for tech in info["stack"]:
            print(f"  - {tech}")
    else:
        print("  (No framework-specific stack detected)")

    print(f"\nDetected Modules/Features ({len(features)}):")
    if features:
        for feature in features:
            print(f"  - {feature}")
    else:
        print("  (No distinct feature modules detected)")

    print(f"\nFiles: {stats['total']} total files tracked")
    if info.get("error"):
        print(f"Warning: package.json could not be parsed: {info['error']}")
    print("\n====================\n")
    return "error" not in info


def main() -> None:
    parser = argparse.ArgumentParser(description="Session Manager")
    parser.add_argument("command", choices=["status", "info"], help="Command to run")
    parser.add_argument("path", nargs="?", default=".", help="Project path")

    args = parser.parse_args()
    root = get_project_root(args.path)
    info = analyze_package_json(root)

    if args.command == "status":
        ok = print_status(root)
        sys.exit(0 if ok else 1)

    print(json.dumps(info, indent=2))
    sys.exit(1 if "error" in info else 0)


if __name__ == "__main__":
    main()
