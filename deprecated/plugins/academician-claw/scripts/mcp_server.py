#!/usr/bin/env python3
"""
AcademicianClaw MCP Server
--------------------------
Implements MCP protocol (JSON-RPC 2.0, Content-Length framing over stdio) to
expose OpenClaw scripts as agent-callable tools. Zero external dependencies —
pure Python stdlib + subprocess.

Tools exposed:
  build_context   — Assemble the context block from memory files (start of session)
  new_session     — Reset session state, show overdue tasks and carry-overs
  check_tasks     — List overdue / due-today / due-this-week tasks
  health_check    — Verify all required files exist and no LLM calls in scripts
  prune_episodic  — Archive old episodic entries when recent.md gets large

Usage (called automatically by Antigravity via mcp.json):
  python scripts/mcp_server.py
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

PLUGIN_ROOT = Path(__file__).parent.parent  # plugins/academician-claw/
SERVER_NAME = "academician-claw"
SERVER_VERSION = "2.0.0"
PROTOCOL_VERSION = "2024-11-05"

# ── ANSI colour stripper ──────────────────────────────────────────────────────

def strip_ansi(text: str) -> str:
    """Remove terminal colour/style escape sequences for clean MCP text output."""
    return re.sub(r"\x1B\[[0-9;]*[mKJH]|\x1B\[[0-9]*[A-D]", "", text)


# ── Script runner ─────────────────────────────────────────────────────────────

def run_script(script_filename: str) -> str:
    """Run a scripts/ file as a subprocess and return its cleaned stdout."""
    script_path = PLUGIN_ROOT / "scripts" / script_filename
    if not script_path.exists():
        return f"[ERROR] Script not found: {script_path}"

    result = subprocess.run(
        [sys.executable, str(script_path)],
        capture_output=True,
        text=True,
        cwd=str(PLUGIN_ROOT),
        encoding="utf-8",
        errors="replace",
        env={**__import__("os").environ, "PYTHONIOENCODING": "utf-8"},
    )
    output = result.stdout
    if result.returncode != 0 and result.stderr:
        output += f"\n[stderr] {result.stderr}"
    return strip_ansi(output).strip()


# ── Tool definitions (MCP schema) ─────────────────────────────────────────────

TOOLS: list[dict] = [
    {
        "name": "build_context",
        "description": (
            "Build the OpenClaw context block from Sanjay's memory files "
            "(soul, semantic, episodic, tasks, habits, active project). "
            "Call this at the START of every AcademicianClaw session to load "
            "full personal context into the conversation."
        ),
        "inputSchema": {"type": "object", "properties": {}, "required": []},
    },
    {
        "name": "new_session",
        "description": (
            "Start a new OpenClaw session: resets context/current-session.md, "
            "clears the scratchpad, surfaces overdue tasks and carry-overs from "
            "the last session, and logs the session start timestamp."
        ),
        "inputSchema": {"type": "object", "properties": {}, "required": []},
    },
    {
        "name": "check_tasks",
        "description": (
            "Show tasks from context/tasks.md grouped by urgency: "
            "OVERDUE, DUE TODAY, DUE THIS WEEK. Use at session start or when "
            "the user asks what's pending / what's next / what's overdue."
        ),
        "inputSchema": {"type": "object", "properties": {}, "required": []},
    },
    {
        "name": "health_check",
        "description": (
            "Run a full system integrity check on AcademicianClaw: "
            "verifies required files exist, memory is populated, "
            "and no LLM API calls are present in any script."
        ),
        "inputSchema": {"type": "object", "properties": {}, "required": []},
    },
    {
        "name": "prune_episodic",
        "description": (
            "Archive old episodic memory entries from memory/episodic/recent.md "
            "when it exceeds ~400 lines. Run when health_check warns about "
            "episodic size. Safe to call — does not delete, only archives."
        ),
        "inputSchema": {"type": "object", "properties": {}, "required": []},
    },
]

# Maps tool name → script filename
TOOL_SCRIPT_MAP: dict[str, str] = {
    "build_context": "context_builder.py",
    "new_session": "new_session.py",
    "check_tasks": "task_check.py",
    "health_check": "health.py",
    "prune_episodic": "prune_episodic.py",
}


# ── MCP JSON-RPC transport (Content-Length framing over stdio) ────────────────

def write_response(obj: dict) -> None:
    """Write a JSON-RPC response using binary stdout to avoid CRLF translation."""
    body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
    header = f"Content-Length: {len(body)}\r\n\r\n".encode("utf-8")
    sys.stdout.buffer.write(header + body)
    sys.stdout.buffer.flush()


def success(id, result: dict) -> None:
    write_response({"jsonrpc": "2.0", "id": id, "result": result})


def error_response(id, code: int, message: str) -> None:
    write_response({"jsonrpc": "2.0", "id": id,
                    "error": {"code": code, "message": message}})


# ── Request dispatcher ────────────────────────────────────────────────────────

def dispatch(request: dict) -> None:
    method: str = request.get("method", "")
    req_id = request.get("id")          # None for notifications

    # ── initialize ──────────────────────────────────────────────────────
    if method == "initialize":
        success(req_id, {
            "protocolVersion": PROTOCOL_VERSION,
            "capabilities": {"tools": {}},
            "serverInfo": {"name": SERVER_NAME, "version": SERVER_VERSION},
        })

    # ── notifications/initialized (no response) ──────────────────────────
    elif method == "notifications/initialized":
        pass

    # ── tools/list ──────────────────────────────────────────────────────
    elif method == "tools/list":
        success(req_id, {"tools": TOOLS})

    # ── tools/call ──────────────────────────────────────────────────────
    elif method == "tools/call":
        params = request.get("params", {})
        tool_name: str = params.get("name", "")

        if tool_name not in TOOL_SCRIPT_MAP:
            error_response(req_id, -32602,
                           f"Unknown tool '{tool_name}'. "
                           f"Available: {list(TOOL_SCRIPT_MAP)}")
            return

        output = run_script(TOOL_SCRIPT_MAP[tool_name])
        success(req_id, {
            "content": [{"type": "text", "text": output or "(no output)"}]
        })

    # ── ping ─────────────────────────────────────────────────────────────
    elif method == "ping":
        success(req_id, {})

    # ── unknown method ───────────────────────────────────────────────────
    else:
        if req_id is not None:  # only respond to requests, not notifications
            error_response(req_id, -32601, f"Method not found: {method}")


# ── Main loop (Content-Length framed stdio reader) ────────────────────────────

def main() -> None:
    """Main loop using binary stdin/stdout for byte-accurate Content-Length framing."""
    stdin  = sys.stdin.buffer
    # stdout.buffer is used in write_response already

    while True:
        # 1. Read headers (binary lines) until blank line
        headers: dict[str, str] = {}
        while True:
            raw = stdin.readline()
            if not raw:                      # EOF
                return
            line = raw.rstrip(b"\r\n").decode("utf-8", errors="replace")
            if not line:                     # blank line = end of headers
                break
            if ":" in line:
                key, _, val = line.partition(":")
                headers[key.strip().lower()] = val.strip()

        # 2. Read exactly Content-Length bytes
        length = int(headers.get("content-length", 0))
        if length == 0:
            continue
        body_bytes = stdin.read(length)
        if not body_bytes:
            return

        # 3. Parse and dispatch
        try:
            request = json.loads(body_bytes.decode("utf-8"))
        except json.JSONDecodeError as exc:
            error_response(None, -32700, f"Parse error: {exc}")
            continue

        try:
            dispatch(request)
        except Exception as exc:  # noqa: BLE001
            req_id = request.get("id")
            error_response(req_id, -32603, f"Internal error: {exc}")


if __name__ == "__main__":
    main()
