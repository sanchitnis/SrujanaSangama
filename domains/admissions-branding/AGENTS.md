# Admissions Branding Domain Router

Use this router only after the root `AGENTS.md` Usage Mode router selects
`admissions-branding`.

## Load Order

1. Identify the admissions, branding, campaign, or enrolment workflow requested.
2. If a slash command is named, read only the matching file in `commands/`.
3. Read local rules only when the command or request names them directly.
4. Read shared skills only when the command or request names them directly.
5. Use `reva-information/` only for the specific policy, programme, or
   admissions reference needed by the task.

## Local Commands

No implemented commands are currently listed in this router.

## Local Rules

No implemented rules are currently listed in this router.

## Output Boundary

Draft outputs for human review. Write persistent task outputs to the user's
`srujana-memory/` or collaboration space, not to this shared domain folder.
