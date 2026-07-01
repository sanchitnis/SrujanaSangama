#!/usr/bin/env python3
"""health.py — OpenClaw system integrity check. Zero LLM calls."""
import datetime, sys
from pathlib import Path

# Ensure UTF-8 output on Windows
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")
import path_resolver
from path_resolver import BASE, WORKSPACE_ROOT, resolve_path


class C:
    G="\033[92m"; R="\033[91m"; Y="\033[93m"; O="\033[38;5;208m"
    D="\033[2m"; B="\033[1m"; END="\033[0m"

ok   = lambda m: print(f"  {C.G}✓{C.END}  {m}")
fail = lambda m: print(f"  {C.R}✗{C.END}  {C.R}{m}{C.END}")
warn = lambda m: print(f"  {C.Y}⚠{C.END}  {C.Y}{m}{C.END}")
info = lambda m: print(f"  {C.D}{m}{C.END}")
hr   = lambda: print(f"  {C.D}{'─'*55}{C.END}")
sec  = lambda t: print(f"\n  {C.O}{C.B}{t}{C.END}") or hr()

REQUIRED = [
    # Core docs
    "README.md",
    # Rules (session prompt + system agents)
    "rules/ORCHESTRATOR.md",
    "rules/PERSONA_ENGINE.md",
    "rules/PERMISSION_GUARDIAN.md",
    # Workflows
    "workflows/session-closer.md",
    "workflows/weekly-review.md",
    "workflows/skill-generator.md",
    "workflows/deep-research.md",
    "workflows/project-kickoff.md",
    # Agent skills
    "agents/skills/writing-partner.md",
    "agents/skills/research-analyst.md",
    "agents/skills/task-manager.md",
    "agents/skills/code-architect.md",
    "agents/skills/learning-coach.md",
    "agents/skills/reflection-facilitator.md",
    "agents/skills/habit-tracker.md",
    "agents/skills/idea-incubator.md",
    "agents/skills/data-interpreter.md",
    "agents/skills/academic-leadership-advisor.md",
    # Agent core
    "agents/core/orchestrator.md",
    "agents/core/memory-steward.md",
    "agents/core/skill-generator.md",
    "agents/registry.md",
    # Memory
    "memory/soul.md",
    "memory/episodic/recent.md",
    "memory/semantic/work.md",
    "memory/semantic/preferences.md",
    "memory/semantic/vocabulary.md",
    "memory/semantic/relationships.md",
    "memory/semantic/ideas.md",
    "memory/semantic/learning.md",
    "memory/procedural/writing-style.md",
    "memory/procedural/code-style.md",
    "memory/procedural/decision-patterns.md",
    "memory/procedural/relationship.md",
    "memory/habits/habits.md",
    # Context
    "context/tasks.md",
    "context/active-project.md",
    "context/current-session.md",
    # Scripts
    "scripts/context_builder.py",
    "scripts/update_memory.py",
    "scripts/init.py",
    "scripts/health.py",
    "scripts/task_check.py",
    "scripts/habit_checkin.py",
    "scripts/new_session.py",
    "scripts/prune_episodic.py",
    "scripts/mcp_server.py",
]


errors = warnings = 0

def check(cond, ok_msg, fail_msg, w=False):
    global errors, warnings
    if cond: ok(ok_msg)
    else:
        if w: warn(fail_msg); warnings += 1
        else: fail(fail_msg); errors += 1

def main():
    print(f"\n  {C.O}{C.B}🦅 OpenClaw Health Check — {datetime.date.today()}{C.END}\n")

    sec("Required Files")
    for rel in REQUIRED:
        p = resolve_path(rel)
        is_optional_pre_onboard = rel.startswith("memory/") or rel.startswith("context/")
        if not p.exists() and is_optional_pre_onboard:
            warn(f"MISSING (Will be created during onboarding): {rel}")
            continue
        size_str = f"  {C.D}({p.stat().st_size:,}b){C.END}" if p.exists() else ""
        check(p.exists(), f"{rel}{size_str}", f"MISSING: {rel}", w=False)

    sec("Memory Population")
    soul_path = resolve_path("memory/soul.md")
    soul = soul_path.read_text(encoding="utf-8") if soul_path.exists() else ""
    check("Name" in soul and "[to be filled]" not in soul[:150],
          "soul.md appears populated",
          "soul.md not populated — run: python3 scripts/local/init.py", w=True)

    ep = resolve_path("memory/episodic/recent.md")
    if ep.exists():
        lines = ep.read_text(encoding="utf-8").split("\n")
        entries = sum(1 for l in lines if l.startswith("## ["))
        info(f"episodic/recent.md: {entries} entries, {len(lines)} lines total")
        if len(lines) > 450:
            warn("Episodic approaching prune threshold — run: python3 scripts/local/prune_episodic.py")

    sec("Scripts — No LLM Check")
    import re
    api_patterns = [r"anthropic\.Anthropic\(", r"openai\.OpenAI\(", r"requests\.post.*api", r"httpx\.post.*api"]
    for rel in [r for r in REQUIRED if r.endswith(".py")]:
        p = BASE / rel
        if p.exists():
            content = p.read_text(encoding="utf-8")
            hits = [pat for pat in api_patterns if re.search(pat, content)]
            if hits:
                fail(f"{rel} — contains LLM API call pattern: {hits}")
            else:
                ok(f"{rel} — no LLM calls detected")

    sec("Logs")
    for log in ["logs/sessions.log", "logs/memory-changes.log"]:
        p = BASE / log
        if p.exists():
            n = len([l for l in p.read_text(encoding="utf-8").split("\n") if l.strip()])
            ok(f"{log}  {C.D}({n} entries){C.END}")
        else:
            warn(f"{log} not yet created (will be created on first session)")

    print()
    hr()
    if errors == 0 and warnings == 0:
        print(f"  {C.G}{C.B}✓ All checks passed.{C.END}")
    elif errors == 0:
        print(f"  {C.Y}{C.B}⚠ {warnings} warning(s) — system functional.{C.END}")
    else:
        print(f"  {C.R}{C.B}✗ {errors} error(s), {warnings} warning(s).{C.END}")
        print(f"\n  {C.D}Run: python3 scripts/local/init.py to fix setup issues.{C.END}")
    print()
    return 0 if errors == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
