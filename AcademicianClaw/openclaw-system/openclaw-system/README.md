# OpenClaw v2 — Prompt-Native Agentic Intelligence System

> *A Claude-native, markdown-first, self-learning agent ecosystem.*
> *No API calls in code. No SDKs. Every intelligent action is a Markdown file you paste into Claude's chat box.*

---

## Core Philosophy

OpenClaw runs entirely through **conversation with Claude**. Intelligence lives in carefully crafted Markdown prompt files. Scripts do only mechanical work: reading files, assembling context blocks, updating memory from parsed text, managing tasks and habits. They never call any LLM API.

```
┌──────────────────────────────────────────────────────┐
│  scripts/local/context_builder.py                    │
│    reads memory/ files → formats → prints to stdout  │
│                         ↓                            │
│  YOU paste into Claude chat:                         │
│    prompts/session/ORCHESTRATOR.md + context block   │
│                         ↓                            │
│  Claude responds as OpenClaw                         │
│                         ↓                            │
│  At session end: paste SESSION_CLOSER.md             │
│  Claude outputs structured SESSION_SUMMARY           │
│                         ↓                            │
│  scripts/local/update_memory.py                      │
│    parses summary → updates memory/ files            │
└──────────────────────────────────────────────────────┘
```

**Rule**: if a task needs language understanding or text generation → Claude via a prompt file.
**Rule**: if a task is mechanical (file I/O, string formatting, date math) → a script, zero LLM calls.

---

## How a Session Works

```
BEFORE SESSION
  python3 scripts/local/context_builder.py
  → prints a formatted CONTEXT BLOCK (your memory, tasks, project)

IN CLAUDE CHAT
  Paste 1: prompts/session/ORCHESTRATOR.md  +  CONTEXT BLOCK
  → Claude activates as OpenClaw Orchestrator, knows who you are

  Work normally. When Claude says "→ route to Writing Partner":
  Paste 2: prompts/agents/WRITING_PARTNER.md
  → Claude switches to that specialist with full context already loaded

  At end of session:
  Paste: prompts/session/SESSION_CLOSER.md
  → Claude outputs a structured SESSION_SUMMARY block

AFTER SESSION
  python3 scripts/local/update_memory.py
  → paste Claude's SESSION_SUMMARY when prompted
  → script updates memory files — no LLM call
```

---

## Directory Structure

```
openclaw/
├── README.md
├── prompts/                        ← Everything you paste into Claude
│   ├── session/
│   │   ├── ORCHESTRATOR.md         ← Start every session with this
│   │   └── SESSION_CLOSER.md       ← End every session with this
│   ├── agents/                     ← One file per specialist agent
│   │   ├── WRITING_PARTNER.md
│   │   ├── RESEARCH_ANALYST.md
│   │   ├── TASK_MANAGER.md
│   │   ├── CODE_ARCHITECT.md
│   │   ├── LEARNING_COACH.md
│   │   ├── REFLECTION_FACILITATOR.md
│   │   ├── HABIT_TRACKER.md
│   │   ├── IDEA_INCUBATOR.md
│   │   ├── DATA_INTERPRETER.md
│   │   ├── MEMORY_STEWARD.md
│   │   └── ACADEMIC_ADVISOR.md
│   └── workflows/                  ← Multi-step composite prompts
│       ├── SKILL_GENERATOR.md
│       ├── WEEKLY_REVIEW.md
│       ├── PROJECT_KICKOFF.md
│       └── DEEP_RESEARCH.md
├── agents/                         ← Agent SKILL.md definitions
│   ├── core/
│   ├── skills/
│   └── registry.md
├── memory/                         ← All persistent user knowledge
│   ├── soul.md
│   ├── episodic/recent.md
│   ├── semantic/
│   ├── procedural/
│   └── habits/habits.md
├── context/                        ← Active working state
│   ├── tasks.md
│   ├── active-project.md
│   ├── current-session.md
│   └── scratchpad.md
├── scripts/local/                  ← Mechanical utilities, zero LLM calls
│   ├── init.py
│   ├── context_builder.py
│   ├── update_memory.py
│   ├── new_session.py
│   ├── task_check.py
│   ├── habit_checkin.py
│   ├── health.py
│   └── prune_episodic.py
└── logs/
    ├── sessions.log
    └── memory-changes.log
```

---

## Quick Start

```bash
python3 scripts/local/init.py           # first-time setup
python3 scripts/local/health.py         # verify system
python3 scripts/local/context_builder.py  # build today's context block
# paste ORCHESTRATOR.md + context block into Claude
# work...
# paste SESSION_CLOSER.md into Claude, copy output
python3 scripts/local/update_memory.py  # save what was learned
```

---

*OpenClaw v2.0 — prompt-native, no LLM API calls in code.*
