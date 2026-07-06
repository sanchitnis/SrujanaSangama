# Kaizen Excellence Domain Router

Use this router only after the root `AGENTS.md` Usage Mode router selects
`kaizen-excellence`.

## Load Order

1. Identify whether the request is personal reflection, FDP planning, team
   improvement, school improvement, or strategic Kaizen.
2. If a slash command is named, read only the matching file in `commands/`.
3. Read rules only when the command or request names them directly.
4. Read shared skills only when the command or request names them directly.
5. Read private wellbeing or reflection memory only when the user explicitly
   wants that context used.

## Local Commands

- `gps-plan`

## Local Rules

- `PERSONAL_REFLECTION_RULES.md`

## Domain Boundary vs Personal Productivity

* **`kaizen-excellence`** governs **reflective growth, retrospectives, and continuous improvement** (personal habits, wellness check-ins, professional development planning, and course/school improvement retrospectives).
* **`personal-productivity`** governs **execution mechanics** (daily task tracking in `tasks.md`, holding inboxes, and automated backlog processing). Use the task manager CLI inside `personal-productivity` for transactional tasks.

## Output Boundary

Draft outputs for human reflection, development, and decisions. Save journaling, habits, and reflective logs to the user's `../srujana-memory/`, not to this shared domain folder.
