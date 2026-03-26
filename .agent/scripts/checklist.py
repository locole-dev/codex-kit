#!/usr/bin/env python3
"""
Master Checklist Runner - Locole Kit
====================================

Orchestrates validation scripts in priority order.
Use this for incremental validation during development.

Usage:
    python .agent/scripts/checklist.py .                    # Run core checks
    python .agent/scripts/checklist.py . --url <URL>        # Include performance checks

Priority Order:
    P0: Security Scan (vulnerabilities, secrets)
    P1: Lint & Type Check (code quality)
    P2: Schema Validation (if database exists)
    P3: Test Runner (unit/integration tests)
    P4: UX Audit (psychology laws, accessibility)
    P5: SEO Check (meta tags, structure)
    P6: Performance (lighthouse - requires URL)
"""

import argparse
import os
import subprocess
import sys
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
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'=' * 60}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.CYAN}{text.center(60)}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'=' * 60}{Colors.ENDC}\n")


def print_step(text: str) -> None:
    print(f"{Colors.BOLD}{Colors.BLUE}[RUN] {text}{Colors.ENDC}")


def print_success(text: str) -> None:
    print(f"{Colors.GREEN}[PASS] {text}{Colors.ENDC}")


def print_warning(text: str) -> None:
    print(f"{Colors.YELLOW}[WARN] {text}{Colors.ENDC}")


def print_error(text: str) -> None:
    print(f"{Colors.RED}[FAIL] {text}{Colors.ENDC}")


CORE_CHECKS = [
    ("Security Scan", ".agent/skills/vulnerability-scanner/scripts/security_scan.py", True),
    ("Lint Check", ".agent/skills/lint-and-validate/scripts/lint_runner.py", True),
    ("Schema Validation", ".agent/skills/database-design/scripts/schema_validator.py", False),
    ("Test Runner", ".agent/skills/testing-patterns/scripts/test_runner.py", False),
    ("UX Audit", ".agent/skills/frontend-design/scripts/ux_audit.py", False),
    ("SEO Check", ".agent/skills/seo-fundamentals/scripts/seo_checker.py", False),
]

PERFORMANCE_CHECKS = [
    ("Lighthouse Audit", ".agent/skills/performance-profiling/scripts/lighthouse_audit.py", True),
    ("Playwright E2E", ".agent/skills/webapp-testing/scripts/playwright_runner.py", False),
]


def check_script_exists(script_path: Path) -> bool:
    return script_path.exists() and script_path.is_file()


def run_script(name: str, script_path: Path, project_path: str, url: Optional[str] = None) -> dict:
    if not check_script_exists(script_path):
        print_warning(f"{name}: Script not found, skipping")
        return {"name": name, "passed": True, "output": "", "skipped": True}

    print_step(f"Running: {name}")

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
            timeout=300,
        )

        passed = result.returncode == 0

        if passed:
            print_success(f"{name}: PASSED")
        else:
            print_error(f"{name}: FAILED")
            if result.stderr:
                print(f"  Error: {result.stderr[:200]}")

        return {
            "name": name,
            "passed": passed,
            "output": result.stdout,
            "error": result.stderr,
            "skipped": False,
        }

    except subprocess.TimeoutExpired:
        print_error(f"{name}: TIMEOUT (>5 minutes)")
        return {"name": name, "passed": False, "output": "", "error": "Timeout", "skipped": False}

    except Exception as exc:
        print_error(f"{name}: ERROR - {exc}")
        return {"name": name, "passed": False, "output": "", "error": str(exc), "skipped": False}


def print_summary(results: List[dict]) -> bool:
    print_header("CHECKLIST SUMMARY")

    passed_count = sum(1 for result in results if result["passed"] and not result.get("skipped"))
    failed_count = sum(1 for result in results if not result["passed"] and not result.get("skipped"))
    skipped_count = sum(1 for result in results if result.get("skipped"))

    print(f"Total Checks: {len(results)}")
    print(f"{Colors.GREEN}[PASS] Passed: {passed_count}{Colors.ENDC}")
    print(f"{Colors.RED}[FAIL] Failed: {failed_count}{Colors.ENDC}")
    print(f"{Colors.YELLOW}[SKIP] Skipped: {skipped_count}{Colors.ENDC}")
    print()

    for result in results:
        if result.get("skipped"):
            status = f"{Colors.YELLOW}[SKIP]{Colors.ENDC}"
        elif result["passed"]:
            status = f"{Colors.GREEN}[PASS]{Colors.ENDC}"
        else:
            status = f"{Colors.RED}[FAIL]{Colors.ENDC}"
        print(f"{status} {result['name']}")

    print()

    if failed_count > 0:
        print_error(f"{failed_count} check(s) FAILED - Please fix before proceeding")
        return False

    print_success("All checks passed.")
    return True


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run the Locole Kit validation checklist",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python .agent/scripts/checklist.py .                      # Core checks only
  python .agent/scripts/checklist.py . --url http://localhost:3000  # Include performance
        """,
    )
    parser.add_argument("project", help="Project path to validate")
    parser.add_argument("--url", help="URL for performance checks (lighthouse, playwright)")
    parser.add_argument("--skip-performance", action="store_true", help="Skip performance checks even if URL provided")

    args = parser.parse_args()

    project_path = Path(args.project).resolve()

    if not project_path.exists():
        print_error(f"Project path does not exist: {project_path}")
        sys.exit(1)

    print_header("LOCOLE KIT - MASTER CHECKLIST")
    print(f"Project: {project_path}")
    print(f"URL: {args.url if args.url else 'Not provided (performance checks skipped)'}")

    results = []

    print_header("CORE CHECKS")
    for name, script_path, required in CORE_CHECKS:
        script = project_path / script_path
        result = run_script(name, script, str(project_path))
        results.append(result)

        if required and not result["passed"] and not result.get("skipped"):
            print_error(f"CRITICAL: {name} failed. Stopping checklist.")
            print_summary(results)
            sys.exit(1)

    if args.url and not args.skip_performance:
        print_header("PERFORMANCE CHECKS")
        for name, script_path, required in PERFORMANCE_CHECKS:
            script = project_path / script_path
            result = run_script(name, script, str(project_path), args.url)
            results.append(result)

    all_passed = print_summary(results)
    sys.exit(0 if all_passed else 1)


if __name__ == "__main__":
    main()
