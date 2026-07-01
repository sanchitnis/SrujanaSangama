# Onboarding Domain Router

Use this router only after the root `AGENTS.md` Usage Mode router selects
`onboarding`.

## Load Order

1. Identify whether the user needs first-time setup, profile creation, or a
   resume/profile audit.
2. If a slash command is named, read only the matching file in `commands/`.
3. Read rules only when the command or request names them directly.
4. Read shared skills only when the command or request names them directly.
5. Read or create `srujana-memory/` files only as required by the selected
   onboarding command and only in the user's personal workspace.

## Local Commands

- `00_onboarding`
- `resume-audit`

## Local Rules

No implemented rules are currently listed in this router.

## Output Boundary

Create or update user-owned memory/workspace files as directed by the selected
command. Do not write personal data into the shared SrujanaSangama folder.
