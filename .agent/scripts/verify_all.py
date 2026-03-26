#!/usr/bin/env python3
"""
Full Verification Suite - Locole Kit
====================================

Runs release-style validation across the shipped checks.
Use this before deployment or major releases.

Usage:
    python .agent/scripts/verify_all.py .
    python .agent/scripts/verify_all.py . --url <URL>

Includes:
    - Security Scan (OWASP, secrets)
    - Lint & Type Coverage
    - Schema Validation
    - Test Suite (unit + integration)
    - UX Audit (psychology, accessibility)
    - SEO Check
    - Lighthouse (Core Web Vitals, when URL is provided)
    - Playwright E2E (when URL is provided)
    - Mobile Audit (if applicable)
"""

import argparse
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import List, Optional


class Colors:
    HEADER = "\033[95m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"


def print_header(text: str) -> None:
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'=' * 70}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.CYAN}{text.center(70)}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'=' * 70}{Colors.ENDC}\n")


def print_step(text: str) -> None:
    print(f"{Colors.BOLD}{Colors.BLUE}[RUN] {text}{Colors.ENDC}")


def print_success(text: str) -> None:
    print(f"{Colors.GREEN}[PASS] {text}{Colors.ENDC}")


def print_warning(text: str) -> None:
    print(f"{Colors.YELLOW}[WARN] {text}{Colors.ENDC}")


def print_error(text: str) -> None:
    print(f"{Colors.RED}[FAIL] {text}{Colors.ENDC}")


VERIFICATION_SUITE = [
    {
        "category": "Security",
        "checks": [
            ("Security Scan", ".agent/skills/vulnerability-scanner/scripts/security_scan.py", True),
        ],
    },
    {
        "category": "Code Quality",
        "checks": [
            ("Lint Check", ".agent/skills/lint-and-validate/scripts/lint_runner.py", True),
            ("Type Coverage", ".agent/skills/lint-and-validate/scripts/type_coverage.py", False),
        ],
    },
    {
        "category": "Data Layer",
        "checks": [
            ("Schema Validation", ".agent/skills/database-design/scripts/schema_validator.py", False),
        ],
    },
    {
        "category": "Testing",
        "checks": [
            ("Test Suite", ".agent/skills/testing-patterns/scripts/test_runner.py", False),
        ],
    },
    {
        "category": "UX & Accessibility",
        "checks": [
            ("UX Audit", ".agent/skills/frontend-design/scripts/ux_audit.py", False),
            ("Accessibility Check", ".agent/skills/frontend-design/scripts/accessibility_checker.py", False),
        ],
    },
    {
        "category": "SEO & Content",
        "checks": [
            ("SEO Check", ".agent/skills/seo-fundamentals/scripts/seo_checker.py", False),
            ("GEO Check", ".agent/skills/geo-fundamentals/scripts/geo_checker.py", False),
        ],
    },
    {
        "category": "Performance",
        "requires_url": True,
        "checks": [
            ("Lighthouse Audit", ".agent/skills/performance-profiling/scripts/lighthouse_audit.py", True),
        ],
    },
    {
        "category": "E2E Testing",
        "requires_url": True,
        "checks": [
            ("Playwright E2E", ".agent/skills/webapp-testing/scripts/playwright_runner.py", False),
        ],
    },
    {
        "category": "Mobile",
        "checks": [
            ("Mobile Audit", ".agent/skills/mobile-design/scripts/mobile_audit.py", False),
        ],
    },
    {
        "category": "Internationalization",
        "checks": [
            ("i18n Check", ".agent/skills/i18n-localization/scripts/i18n_checker.py", False),
        ],
    },
]


def run_script(name: str, script_path: Path, project_path: str, url: Optional[str] = None) -> dict:
    if not script_path.exists():
        print_error(f"{name}: Script not found")
        return {
            "name": name,
            "passed": False,
            "skipped": False,
            "duration": 0,
            "error": f"Script not found: {script_path}",
            "missing": True,
        }

    print_step(f"Running: {name}")
    start_time = datetime.now()

    cmd = [sys.executable, str(script_path), project_path]
    if url and ("lighthouse" in script_path.name.lower() or "playwright" in script_path.name.lower()):
        cmd.append(url)

    env = os.environ.copy()
    env.setdefault("PYTHONIOENCODING", "utf-8")

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            env=env,
            timeout=600,
        )

        duration = (datetime.now() - start_time).total_seconds()
        passed = result.returncode == 0

        if passed:
            print_success(f"{name}: PASSED ({duration:.1f}s)")
        else:
            print_error(f"{name}: FAILED ({duration:.1f}s)")
            if result.stderr:
                print(f"  {result.stderr[:300]}")

        return {
            "name": name,
            "passed": passed,
            "output": result.stdout,
            "error": result.stderr,
            "skipped": False,
            "duration": duration,
            "missing": False,
        }

    except subprocess.TimeoutExpired:
        duration = (datetime.now() - start_time).total_seconds()
        print_error(f"{name}: TIMEOUT (>{duration:.0f}s)")
        return {
            "name": name,
            "passed": False,
            "skipped": False,
            "duration": duration,
            "error": "Timeout",
            "missing": False,
        }

    except Exception as exc:
        duration = (datetime.now() - start_time).total_seconds()
        print_error(f"{name}: ERROR - {exc}")
        return {
            "name": name,
            "passed": False,
            "skipped": False,
            "duration": duration,
            "error": str(exc),
            "missing": False,
        }


def print_final_report(results: List[dict], start_time: datetime) -> bool:
    total_duration = (datetime.now() - start_time).total_seconds()

    print_header("FULL VERIFICATION REPORT")

    total = len(results)
    passed = sum(1 for result in results if result["passed"] and not result.get("skipped"))
    failed = sum(1 for result in results if not result["passed"] and not result.get("skipped"))
    skipped = sum(1 for result in results if result.get("skipped"))
    missing = sum(1 for result in results if result.get("missing"))

    print(f"Total Duration: {total_duration:.1f}s")
    print(f"Total Checks: {total}")
    print(f"{Colors.GREEN}[PASS] Passed: {passed}{Colors.ENDC}")
    print(f"{Colors.RED}[FAIL] Failed: {failed}{Colors.ENDC}")
    print(f"{Colors.YELLOW}[SKIP] Skipped: {skipped}{Colors.ENDC}")
    if missing:
        print(f"{Colors.RED}[FAIL] Missing checks: {missing}{Colors.ENDC}")
    print()

    print(f"{Colors.BOLD}Results by Category:{Colors.ENDC}")
    current_category = None
    for result in results:
        if result.get("category") and result["category"] != current_category:
            current_category = result["category"]
            print(f"\n{Colors.BOLD}{Colors.CYAN}{current_category}:{Colors.ENDC}")

        if result.get("skipped"):
            status = f"{Colors.YELLOW}[SKIP]{Colors.ENDC}"
        elif result.get("missing"):
            status = f"{Colors.RED}[MISSING]{Colors.ENDC}"
        elif result["passed"]:
            status = f"{Colors.GREEN}[PASS]{Colors.ENDC}"
        else:
            status = f"{Colors.RED}[FAIL]{Colors.ENDC}"

        duration_str = f"({result.get('duration', 0):.1f}s)" if not result.get("skipped") else ""
        print(f"  {status} {result['name']} {duration_str}")

    print()

    if failed > 0:
        print(f"{Colors.BOLD}{Colors.RED}FAILED CHECKS:{Colors.ENDC}")
        for result in results:
            if not result["passed"] and not result.get("skipped"):
                label = "[MISSING]" if result.get("missing") else "[FAIL]"
                print(f"\n{Colors.RED}{label} {result['name']}{Colors.ENDC}")
                if result.get("error"):
                    print(f"  Error: {result['error'][:200]}")
        print()

    if failed > 0:
        print_error(f"VERIFICATION FAILED - {failed} check(s) need attention")
        print(f"\n{Colors.YELLOW}[TIP] Fix critical (security, lint) issues first{Colors.ENDC}")
        return False

    print_success("All checks passed. Ready for deployment.")
    return True


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run the complete Locole Kit verification suite",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python .agent/scripts/verify_all.py .
  python .agent/scripts/verify_all.py . --url http://localhost:3000
  python .agent/scripts/verify_all.py . --url https://staging.example.com --no-e2e
        """,
    )
    parser.add_argument("project", help="Project path to validate")
    parser.add_argument("--url", help="URL for performance & E2E checks")
    parser.add_argument("--no-e2e", action="store_true", help="Skip E2E tests")
    parser.add_argument("--stop-on-fail", action="store_true", help="Stop on first failure")

    args = parser.parse_args()

    project_path = Path(args.project).resolve()

    if not project_path.exists():
        print_error(f"Project path does not exist: {project_path}")
        sys.exit(1)

    print_header("LOCOLE KIT - FULL VERIFICATION SUITE")
    print(f"Project: {project_path}")
    print(f"URL: {args.url if args.url else 'Not provided (web checks skipped)'}")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    start_time = datetime.now()
    results = []

    for suite in VERIFICATION_SUITE:
        category = suite["category"]
        requires_url = suite.get("requires_url", False)

        if requires_url and not args.url:
            print_warning(f"Skipping {category}: no URL provided")
            continue

        if args.no_e2e and category == "E2E Testing":
            continue

        print_header(category.upper())

        for name, script_path, required in suite["checks"]:
            script = project_path / script_path
            result = run_script(name, script, str(project_path), args.url)
            result["category"] = category
            results.append(result)

            if args.stop_on_fail and required and not result["passed"] and not result.get("skipped"):
                print_error(f"CRITICAL: {name} failed. Stopping verification.")
                print_final_report(results, start_time)
                sys.exit(1)

    all_passed = print_final_report(results, start_time)
    sys.exit(0 if all_passed else 1)


if __name__ == "__main__":
    main()
