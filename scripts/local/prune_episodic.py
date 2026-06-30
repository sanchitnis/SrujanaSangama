#!/usr/bin/env python3
"""
SrujanaSangama: Episodic Memory Manager
Description: Archives old entries in my-memory/episodic/recent.md when it exceeds the limit.
             Zero LLM API calls.
"""

import re
import datetime
import sys
from pathlib import Path

# Ensure UTF-8 output on Windows
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")

import path_resolver
from path_resolver import resolve_path

PRUNE_THRESHOLD = 500   # lines
ARCHIVE_LINES   = 200   # lines to move to archive
KEEP_LINES      = 300   # lines to keep in recent.md

class C:
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    ORANGE = "\033[38;5;208m"
    DIM = "\033[2m"
    BOLD = "\033[1m"
    END = "\033[0m"

def read(rel, default=""):
    p = resolve_path(rel)
    return p.read_text(encoding="utf-8") if p.exists() else default

def write(rel, content):
    p = resolve_path(rel)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")

def append_to(rel, text):
    p = resolve_path(rel)
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "a", encoding="utf-8") as f:
        f.write(text)

def main():
    recent_path = resolve_path("my-memory/episodic/recent.md")
    
    # Fallback to legacy path for safety
    if not recent_path.exists():
        recent_path = resolve_path("memory/episodic/recent.md")

    if not recent_path.exists():
        print("  [ERROR] No episodic recent log found. Please run onboarding first.")
        return

    content = recent_path.read_text(encoding="utf-8")
    lines   = content.split("\n")
    total   = len(lines)

    print(f"\n  {C.ORANGE}{C.BOLD}🗂  Episodic Memory Manager{C.END}")
    print(f"  {C.DIM}recent.md: {total} lines (threshold: {PRUNE_THRESHOLD}){C.END}\n")

    if total < PRUNE_THRESHOLD:
        print(f"  {C.GREEN}✓ No pruning needed.{C.END} ({PRUNE_THRESHOLD - total} lines before threshold)\n")
        return

    # Split entries by heading ## [YYYY-MM-DD
    header_lines = []
    entries = []
    in_header = True
    current_entry = []

    for line in lines:
        if re.match(r"^## \[", line):
            in_header = False
            if current_entry:
                entries.append("\n".join(current_entry))
            current_entry = [line]
        elif in_header:
            header_lines.append(line)
        else:
            current_entry.append(line)

    if current_entry:
        entries.append("\n".join(current_entry))

    total_entries = len(entries)
    archive_count = max(1, total_entries // 3)  # archive oldest third
    to_archive = entries[:archive_count]
    to_keep    = entries[archive_count:]

    # Determine archive file name
    archive_month = datetime.date.today().strftime("%Y-%m")
    archive_path  = f"my-memory/episodic/gps-archive/{archive_month}.md"

    # Check if archive already exists (append) or create new
    existing_archive = read(archive_path, "")
    if not existing_archive:
        archive_header = f"# Episodic Archive — {archive_month}\n_Archived from recent.md_\n\n"
    else:
        archive_header = existing_archive

    archive_content = archive_header + "\n\n".join(to_archive) + "\n"
    write(archive_path, archive_content)

    # Rebuild recent.md
    header_text  = "\n".join(header_lines)
    recent_new   = header_text + "\n\n" + "\n\n".join(to_keep) + "\n"
    
    # Write back to the same file path that we read from
    if "my-memory" in str(recent_path):
        write("my-memory/episodic/recent.md", recent_new)
    else:
        write("memory/episodic/recent.md", recent_new)

    new_line_count = len(recent_new.split("\n"))

    # Log
    ts = datetime.datetime.now().isoformat(timespec="seconds")
    append_to("my-memory/logs/memory-changes.log",
              f"[{ts}] PRUNE: moved {archive_count} entries to {archive_path} | recent.md now {new_line_count} lines\n")

    print(f"  {C.GREEN}✓ Archived{C.END} {archive_count} entries → {archive_path}")
    print(f"  {C.GREEN}✓ recent.md{C.END} reduced to {new_line_count} lines")
    print(f"  {C.DIM}Log updated: srujana-memory/my-memory/logs/memory-changes.log{C.END}\n")

if __name__ == "__main__":
    main()
