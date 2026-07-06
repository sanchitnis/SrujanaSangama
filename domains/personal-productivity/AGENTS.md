# Personal Productivity Domain Router

Use this router only after the root `AGENTS.md` Usage Mode router selects
`personal-productivity`.

## Load Order

1. Identify whether the request is planning, weekly review, project kickoff,
   deep research, skill generation, or session closure.
2. If a slash command is named, read only the matching file in `commands/`.
3. Read rules only when the command or request names them directly.
4. Read shared skills only when the command or request names them directly.
5. Read the smallest relevant part of `srujana-memory/`: current context before
   archives, selected project before all projects, selected task list before all
   memory.

## Core Agents

All core agent system prompts are consolidated under `agents/`:
- `orchestrator.md`
- `memory-steward.md`
- `cee-briefing-agent.md`
- `cee-triage-agent.md`

## Local Workflows

- `workflows/deep-research.md`
- `workflows/project-kickoff.md`
- `workflows/weekly-review.md`

## Local Rules

- `rules/CEE_ENGINE.md`
- `rules/PERMISSION_GUARDIAN.md`
- `rules/PERSONA_ENGINE.md`

## Global Specialist Skills

Generalist specialist agents are promoted to global workspace skills under `.agents/skills/` so they can be reused across all domains:
- `.agents/skills/writing-partner/`
- `.agents/skills/research-analyst/`
- `.agents/skills/web-agent/`
- `.agents/skills/code-architect/`
- `.agents/skills/computer-agent/`
- `.agents/skills/data-interpreter/`
- `.agents/skills/learning-coach/`
- `.agents/skills/reflection-facilitator/`
- `.agents/skills/habit-tracker/`
- `.agents/skills/idea-incubator/`
- `.agents/skills/academic-leadership-advisor/`
- `.agents/skills/skill-generator/`

## Output Boundary

Write personal planning, task, wiki, and reflection outputs to the user's relative path `../srujana-memory/`, not to this shared domain folder.

