# Academic Admin Domain Router

Use this router only after the root `AGENTS.md` Usage Mode router selects
`academic-admin`.

## Load Order

1. Identify the exact academic administration workflow.
2. If a slash command is named, read only the matching file in `commands/`.
3. Read rules only when the command or request names them directly.
4. Read shared skills only when the command or request names them directly.
5. Use `reva-information/` only for the specific regulation, policy, syllabus,
   or accreditation reference needed by the task.

## Local Commands

- `attainment-check`

## Local Rules

- `REGULATORY_COMPLIANCE.md`

## Output Boundary

Draft outputs for human review. Write persistent task outputs to the user's
`srujana-memory/` or collaboration space, not to this shared domain folder.
