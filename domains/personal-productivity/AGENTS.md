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

## Local Commands

- `07_morning-briefing`
- `08_weekly-alignment-audit`
- `deep-research`
- `project-kickoff`
- `session-closer`
- `skill-generator`
- `weekly-review`

## Local Rules

- `CEE_ENGINE.md`
- `ORCHESTRATOR.md`
- `PERMISSION_GUARDIAN.md`
- `PERSONA_ENGINE.md`

The nested `rules/agents/` and `rules/prompts/` folders should be read only when
the selected command names a specific agent or prompt.

## Output Boundary

Write personal planning, task, wiki, and reflection outputs to the user's
`srujana-memory/`, not to this shared domain folder.
