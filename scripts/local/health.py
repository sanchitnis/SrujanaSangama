#!/usr/bin/env python3
"""
SrujanaSangama: Workspace Integrity Check
Description: Verifies that all required local memory folders, templates,
             and configurations exist and are healthy. Zero LLM calls.
"""

import sys
import datetime
from pathlib import Path

# Ensure UTF-8 output on Windows
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")

import path_resolver
from path_resolver import get_srujana_memory_dir, get_reva_info_dir, resolve_path

class C:
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    ORANGE = "\033[38;5;208m"
    DIM = "\033[2m"
    BOLD = "\033[1m"
    END = "\033[0m"

ok   = lambda m: print(f"  {C.GREEN}✓{C.END}  {m}")
fail = lambda m: print(f"  {C.RED}✗{C.END}  {C.RED}{m}{C.END}")
warn = lambda m: print(f"  {C.YELLOW}⚠{C.END}  {C.YELLOW}{m}{C.END}")
info = lambda m: print(f"  {C.DIM}{m}{C.END}")
hr   = lambda: print(f"  {C.DIM}{'─'*55}{C.END}")
sec  = lambda t: print(f"\n  {C.ORANGE}{C.BOLD}{t}{C.END}") or hr()

# Srujana-Memory files that must exist for a healthy onboarding state
REQUIRED_MEMORY_FILES = [
    "my-memory/soul.md",
    "my-memory/semantic/profile.md",
    "my-memory/semantic/teaching.md",
    "my-memory/semantic/research.md",
    "my-memory/semantic/professional.md",
    "my-memory/context/this-semester.md",
    "my-memory/context/tasks.md",
    "my-memory/context/active-projects.md",
    "my-memory/gps/sankalpa-current.md",
    "my-memory/gps/goals-current.md",
    "my-memory/gps/habit-log.md",
    "my-memory/episodic/recent.md",
    "public-memory/profile.md",
    "srujana.code-workspace"
]

# SrujanaSangama repository files that must exist
REQUIRED_REPO_FILES = [
    "README.md",
    "CONSTITUTION.md",
    "AGENTS.md",
    "CONTRIBUTING.md",
    "IMPLEMENTATION-STATUS.md",
    "scripts/local/path_resolver.py",
    "scripts/local/init.py",
    "scripts/local/prune_episodic.py",
    "scripts/local/health.py"
]

errors = warnings = 0

def check(cond, ok_msg, fail_msg, w=False):
    global errors, warnings
    if cond:
        ok(ok_msg)
    else:
        if w:
            warn(fail_msg)
            warnings += 1
        else:
            fail(fail_msg)
            errors += 1

def main():
    global errors, warnings
    print(f"\n  {C.ORANGE}{C.BOLD}🦅 SrujanaSangama Workspace Health Check — {datetime.date.today()}{C.END}\n")

    # 1. Check Repository Files
    sec("1. Repository Integrity")
    for rel in REQUIRED_REPO_FILES:
        p = resolve_path(rel) # resolves to repo root since it doesn't match memory prefixes
        size_str = f"  {C.DIM}({p.stat().st_size:,}b){C.END}" if p.exists() else ""
        check(p.exists(), f"{rel}{size_str}", f"MISSING REPO FILE: {rel}", w=False)

    # 2. Check Srujana Memory Workspace
    sec("2. Local Memory Workspace (srujana-memory)")
    try:
        mem_dir = get_srujana_memory_dir()
        ok(f"Memory directory found: {mem_dir}")
        
        for rel in REQUIRED_MEMORY_FILES:
            # Resolved relative to srujana-memory/
            p = mem_dir / rel
            size_str = f"  {C.DIM}({p.stat().st_size:,}b){C.END}" if p.exists() else ""
            check(p.exists(), f"{rel}{size_str}", f"MISSING MEMORY FILE: {rel} (Run onboarding script to resolve)", w=False)
            
    except SystemExit:
        fail("Srujana memory folder ('srujana-memory') not found on system. Please run python scripts/local/init.py first.")
        errors += 1

    # 3. Check REVA Information Directory
    sec("3. Reference Directory (reva-information)")
    try:
        info_dir = get_reva_info_dir()
        ok(f"Reference directory found: {info_dir}")
        check((info_dir / "regulations").exists(), "regulations/ folder present", "regulations/ folder missing in reference directory")
        check((info_dir / "quality").exists(), "quality/ folder present", "quality/ folder missing in reference directory")
    except SystemExit:
        fail("Reference folder ('reva-information') not found on system.")
        errors += 1

    # 4. Check Profile Settings
    sec("4. Profile Integrity")
    try:
        soul_path = get_srujana_memory_dir() / "my-memory/soul.md"
        if soul_path.exists():
            soul = soul_path.read_text(encoding="utf-8")
            check("Name" in soul and "[To be filled]" not in soul[:250],
                  "soul.md appears populated",
                  "soul.md identity fields are still blank or default", w=True)
            
            ep = get_srujana_memory_dir() / "my-memory/episodic/recent.md"
            if ep.exists():
                lines = ep.read_text(encoding="utf-8").split("\n")
                entries = sum(1 for l in lines if l.startswith("## ["))
                info(f"episodic/recent.md: {entries} entries logged ({len(lines)} lines total)")
                if len(lines) > 450:
                    warn("Episodic log approaching prune limit — Run: python scripts/local/prune_episodic.py")
        else:
            warn("soul.md missing — Profile cannot be audited.")
    except Exception as e:
        warn(f"Could not audit soul.md: {e}")

    # 5. Check Log Files
    sec("5. Memory Logs")
    try:
        log_dir = get_srujana_memory_dir() / "my-memory/logs"
        for log in ["sessions.log", "memory-changes.log"]:
            p = log_dir / log
            if p.exists():
                n = len([l for l in p.read_text(encoding="utf-8").split("\n") if l.strip()])
                ok(f"{log}  {C.DIM}({n} entries){C.END}")
            else:
                warn(f"{log} not yet populated (will write on active use)")
    except Exception as e:
        warn(f"Could not audit memory logs: {e}")

    print()
    hr()
    if errors == 0 and warnings == 0:
        print(f"  {C.GREEN}{C.BOLD}✓ All workspace checks passed.{C.END}")
    elif errors == 0:
        print(f"  {C.YELLOW}{C.BOLD}⚠ {warnings} warning(s) — workspace fully functional.{C.END}")
    else:
        print(f"  {C.RED}{C.BOLD}✗ {errors} error(s), {warnings} warning(s) detected.{C.END}")
        print(f"\n  {C.DIM}Run: python scripts/local/init.py to rebuild setup files.{C.END}")
    print()
    return 0 if errors == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
