# GitHub Copilot Instructions

Use `AGENTS.md` as the primary project instruction file.

For routine faculty/admin work:

1. Stay in Usage Mode unless the user explicitly asks to change SrujanaSangama
   itself.
2. Classify the request into one `domains/<domain>/` folder.
3. Read `domains/<domain>/AGENTS.md` first.
4. Read only the named command, directly referenced rule files, and directly
   referenced shared skills.
5. Do not preload all domains, all commands, all skills,
   `specification/architecture.md`, or `specification/design.md` for a narrow
   task.

For platform changes:

1. Confirm Development Mode as described in `CONSTITUTION.md` section 2.
2. Follow the Agentic Scrum lifecycle in root `AGENTS.md`.
3. Do not edit platform files without a proposal and task trail in
   `specification/`.
