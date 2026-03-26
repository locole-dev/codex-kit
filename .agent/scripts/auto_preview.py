#!/usr/bin/env python3
"""
Auto Preview - Locole Kit
=========================

Manages the local development server for previewing the application.

Usage:
    python .agent/scripts/auto_preview.py start [port]
    python .agent/scripts/auto_preview.py stop
    python .agent/scripts/auto_preview.py status
"""

import argparse
import json
import os
import signal
import subprocess
import sys
import time
from pathlib import Path


AGENT_DIR = Path(".agent")
PID_FILE = AGENT_DIR / "preview.pid"
LOG_FILE = AGENT_DIR / "preview.log"
STATE_FILE = AGENT_DIR / "preview.json"


def get_project_root() -> Path:
    return Path(".").resolve()


def ensure_agent_dir() -> None:
    AGENT_DIR.mkdir(parents=True, exist_ok=True)


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def load_state() -> dict:
    if not STATE_FILE.exists():
        return {}
    try:
        return read_json(STATE_FILE)
    except Exception:
        return {}


def save_state(pid: int, port: int) -> None:
    ensure_agent_dir()
    STATE_FILE.write_text(
        json.dumps(
            {
                "pid": pid,
                "port": port,
                "url": f"http://localhost:{port}",
            },
            indent=2,
        ),
        encoding="utf-8",
    )


def clear_state() -> None:
    for path in (PID_FILE, STATE_FILE):
        if path.exists():
            path.unlink()


def is_running(pid: int) -> bool:
    if sys.platform == "win32":
        result = subprocess.run(
            ["tasklist", "/FI", f"PID eq {pid}", "/FO", "CSV", "/NH"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        output = (result.stdout or "").strip()
        return bool(output) and "No tasks are running" not in output

    try:
        os.kill(pid, 0)
        return True
    except OSError:
        return False


def get_start_command(root: Path):
    pkg_file = root / "package.json"
    if not pkg_file.exists():
        return None

    try:
        data = read_json(pkg_file)
    except Exception as exc:
        raise RuntimeError(f"Could not read package.json: {exc}") from exc

    scripts = data.get("scripts", {})
    if "dev" in scripts:
        return ["npm", "run", "dev"]
    if "start" in scripts:
        return ["npm", "start"]
    return None


def start_server(port: int = 3000) -> None:
    ensure_agent_dir()

    if PID_FILE.exists():
        try:
            pid = int(PID_FILE.read_text().strip())
            if is_running(pid):
                print(f"[WARN] Preview already running (PID: {pid})")
                return
        except Exception:
            pass

    root = get_project_root()
    try:
        cmd = get_start_command(root)
    except RuntimeError as exc:
        print(f"[FAIL] {exc}")
        sys.exit(1)

    if not cmd:
        print("[FAIL] No 'dev' or 'start' script found in package.json")
        sys.exit(1)

    env = os.environ.copy()
    env["PORT"] = str(port)

    if sys.platform == "win32" and cmd[0] in {"npm", "npx"}:
        cmd[0] = f"{cmd[0]}.cmd"

    print(f"[RUN] Starting preview on port {port}...")

    with open(LOG_FILE, "w", encoding="utf-8") as log:
        process = subprocess.Popen(
            cmd,
            cwd=str(root),
            stdout=log,
            stderr=log,
            env=env,
        )

    time.sleep(2)
    if process.poll() is not None:
        clear_state()
        print("[FAIL] Preview process exited during startup.")
        print(f"Logs: {LOG_FILE}")
        sys.exit(process.returncode or 1)

    PID_FILE.write_text(str(process.pid), encoding="utf-8")
    save_state(process.pid, port)
    print(f"[PASS] Preview started (PID: {process.pid})")
    print(f"Logs: {LOG_FILE}")
    print(f"URL: http://localhost:{port}")


def stop_server() -> None:
    if not PID_FILE.exists():
        print("[INFO] No preview server found.")
        return

    try:
        pid = int(PID_FILE.read_text().strip())
        if is_running(pid):
            if sys.platform != "win32":
                os.kill(pid, signal.SIGTERM)
            else:
                subprocess.call(["taskkill", "/F", "/T", "/PID", str(pid)])
            print(f"[PASS] Preview stopped (PID: {pid})")
        else:
            print("[INFO] Process was not running.")
    except Exception as exc:
        print(f"[FAIL] Error stopping server: {exc}")
    finally:
        clear_state()


def status_server() -> None:
    running = False
    pid = None
    state = load_state()
    port = state.get("port")
    url = state.get("url", "Unknown")

    if PID_FILE.exists():
        try:
            pid = int(PID_FILE.read_text().strip())
            if is_running(pid):
                running = True
                if port:
                    url = f"http://localhost:{port}"
        except Exception:
            pass

    print("\n=== Preview Status ===")
    if running:
        print("Status: Running")
        print(f"PID: {pid}")
        print(f"URL: {url}")
        print(f"Logs: {LOG_FILE}")
    else:
        print("Status: Stopped")
    print("===================\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["start", "stop", "status"])
    parser.add_argument("port", nargs="?", default="3000")

    args = parser.parse_args()

    if args.action == "start":
        start_server(int(args.port))
    elif args.action == "stop":
        stop_server()
    else:
        status_server()


if __name__ == "__main__":
    main()
