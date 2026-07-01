#!/usr/bin/env python3
"""
Eval Bridge — scans the eval improvement backlog for F-9 domain gap items
and extracts gap topics by course code to feed into the Course Buddy Builder refresh pipeline.
Constraint: C1 (stdlib only; no API calls)

Usage:
    python3 eval_bridge.py --course-code CSE301
    python3 eval_bridge.py --course-code CSE301 --backlog ../../eval/data/IMPROVEMENT-BACKLOG.md

Output:
    Prints a comma-separated list of gap topics for use with:
    python3 build.py --course-file ... --refresh --gap-topics "<output>"
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

DEFAULT_BACKLOG = Path(__file__).resolve().parent.parent.parent / "eval" / "data" / "IMPROVEMENT-BACKLOG.md"

# Regex to detect F-9 failure type in a task block
F9_PATTERN = re.compile(r"Failure type:\s*F-9", re.IGNORECASE)
COURSE_PATTERN = re.compile(r"Track affected:\s*(.+)")
DESCRIPTION_PATTERN = re.compile(r"Description:\s*(.+)")


def _parse_backlog(backlog_path: Path) -> list[dict]:
    """
    Parse IMPROVEMENT-BACKLOG.md and return a list of task dicts.
    Each task dict has: task_id, failure_type, track, description, status.
    """
    if not backlog_path.exists():
        print(f"[ERROR] Backlog file not found: {backlog_path}", file=sys.stderr)
        sys.exit(1)

    text = backlog_path.read_text(encoding="utf-8")
    tasks: list[dict] = []
    current: dict | None = None

    for line in text.splitlines():
        line = line.strip()

        # New task block: starts with a bold task ID
        id_match = re.match(r"\*\*Task ID\*\*:\s*(IMP-\S+)", line)
        if id_match:
            if current:
                tasks.append(current)
            current = {"task_id": id_match.group(1), "failure_type": "", "track": "", "description": "", "status": ""}
            continue

        if current is None:
            continue

        if re.match(r"\*\*Failure type\*\*:", line):
            current["failure_type"] = re.sub(r"\*\*Failure type\*\*:\s*", "", line)
        elif re.match(r"\*\*Track affected\*\*:", line):
            current["track"] = re.sub(r"\*\*Track affected\*\*:\s*", "", line)
        elif re.match(r"\*\*Description\*\*:", line):
            current["description"] = re.sub(r"\*\*Description\*\*:\s*", "", line)
        elif re.match(r"\*\*Status\*\*:", line):
            current["status"] = re.sub(r"\*\*Status\*\*:\s*", "", line)

    if current:
        tasks.append(current)

    return tasks


def _extract_gap_topics(tasks: list[dict], course_code: str) -> list[str]:
    """
    Filter for F-9 tasks matching the given course code.
    Extract the concept/topic name from the description.
    """
    topics: list[str] = []
    for task in tasks:
        if "F-9" not in task.get("failure_type", ""):
            continue
        # Check if this task is about the given course code
        track = task.get("track", "")
        description = task.get("description", "")
        if course_code.lower() not in track.lower() and course_code.lower() not in description.lower():
            continue
        # Extract topic: assume the description names the concept
        # Try to find quoted concept or just use the description
        quoted = re.findall(r"['\"]([^'\"]+)['\"]", description)
        if quoted:
            topics.extend(quoted)
        elif description:
            # Use first 60 chars of description as the gap topic
            topics.append(description[:60].rstrip(",. "))

    return topics


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract F-9 domain gap topics for a course from the eval improvement backlog.",
    )
    parser.add_argument("--course-code", required=True, help="Course code to filter for (e.g. CSE301)")
    parser.add_argument(
        "--backlog",
        default=str(DEFAULT_BACKLOG),
        help=f"Path to IMPROVEMENT-BACKLOG.md (default: {DEFAULT_BACKLOG})",
    )
    args = parser.parse_args()

    backlog_path = Path(args.backlog).resolve()
    tasks = _parse_backlog(backlog_path)
    topics = _extract_gap_topics(tasks, args.course_code)

    if not topics:
        print(f"[INFO] No F-9 gap topics found for course code '{args.course_code}' in backlog.")
        sys.exit(0)

    print(",".join(topics))
    print(
        f"\n# Found {len(topics)} gap topic(s). Use with:\n"
        f"# python3 build.py --course-file templates/[descriptor].md "
        f"--refresh --gap-topics \"{','.join(topics)}\"",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
