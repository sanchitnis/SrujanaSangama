#!/usr/bin/env python3
"""health.py — OpenClaw system integrity check. Zero LLM calls."""
import datetime, sys
from pathlib import Path
BASE = Path(__file__).parent.parent.parent

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
    "README.md",
    "prompts/session/ORCHESTRATOR.md",
    "prompts/session/SESSION_CLOSER.md",
    "prompts/agents/WRITING_PARTNER.md",
    "prompts/agents/RESEARCH_ANALYST.md",
    "prompts/agents/TASK_MANAGER.md",
    "prompts/agents/CODE_ARCHITECT.md",
    "prompts/agents/LEARNING_COACH.md",
    "prompts/agents/REFLECTION_FACILITATOR.md",
    "prompts/agents/HABIT_TRACKER.md",
    "prompts/agents/IDEA_INCUBATOR.md",
    "prompts/agents/DATA_INTERPRETER.md",
    "prompts/agents/MEMORY_STEWARD.md",
    "prompts/agents/ACADEMIC_ADVISOR.md",
    "prompts/workflows/SKILL_GENERATOR.md",
    "prompts/workflows/WEEKLY_REVIEW.md",
    "agents/core/orchestrator.md",
    "agents/core/memory-steward.md",
    "agents/core/skill-generator.md",
    "agents/registry.md",
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
    "context/tasks.md",
    "context/active-project.md",
    "context/current-session.md",
    "scripts/local/context_builder.py",
    "scripts/local/update_memory.py",
    "scripts/local/init.py",
    "scripts/local/health.py",
    "scripts/local/task_check.py",
    "scripts/local/habit_checkin.py",
    "scripts/local/new_session.py",
    "scripts/local/prune_episodic.py",
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
        p = BASE / rel
        check(p.exists(), f"{rel}  {C.D}({p.stat().st_size:,}b){C.END}", f"MISSING: {rel}", w=False)

    sec("Memory Population")
    soul = (BASE / "memory/soul.md").read_text() if (BASE/"memory/soul.md").exists() else ""
    check("Name" in soul and "[to be filled]" not in soul[:150],
          "soul.md appears populated",
          "soul.md not populated — run: python3 scripts/local/init.py", w=True)

    ep = BASE / "memory/episodic/recent.md"
    if ep.exists():
        lines = ep.read_text().split("\n")
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
            content = p.read_text()
            hits = [pat for pat in api_patterns if re.search(pat, content)]
            if hits:
                fail(f"{rel} — contains LLM API call pattern: {hits}")
            else:
                ok(f"{rel} — no LLM calls detected")

    sec("Logs")
    for log in ["logs/sessions.log", "logs/memory-changes.log"]:
        p = BASE / log
        if p.exists():
            n = len([l for l in p.read_text().split("\n") if l.strip()])
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
