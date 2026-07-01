# Innovator Domain Router

Use this router only after the root `AGENTS.md` Usage Mode router selects
`innovator`.

## Load Order

1. Identify whether the request concerns patents, consulting, MOUs, products, or
   startup mentoring.
2. If a slash command is named, read only the matching file in `commands/`.
3. Read rules only when the command or request names them directly.
4. Read shared skills only when the command or request names them directly.
5. Use `reva-information/` only for the specific legal, institutional, or policy
   reference needed by the task.

## Local Commands

- `01_input`
- `02_extract`
- `03_patentability`
- `04_prior_art`
- `05_scoring`
- `06_draft_template`
- `07_application`
- `08_export`
- `patent-draft`

Instruction companion files with `.instructions.md` may be read only when the
matching workflow step is selected.

## Local Rules

- `PRODUCT_IP_GUIDELINES.md`

## Output Boundary

Draft outputs for human and legal/IP review. Write persistent task outputs to
the user's `srujana-memory/` or collaboration space, not to this shared domain
folder.
