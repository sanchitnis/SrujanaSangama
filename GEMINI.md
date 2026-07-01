# GEMINI.md - SrujanaSangama Agent Router

Gemini and Google Antigravity-style agents should use the same routing protocol
as Codex and GitHub Copilot.

Read root `AGENTS.md` first. Treat this file as a shim, not a second source of
truth.

For Usage Mode:

- classify the request into one domain
- read `domains/<domain>/AGENTS.md`
- read only the selected command and directly named rules or skills
- keep user memory in `srujana-memory/` separate from shared platform files

For Development Mode:

- confirm the `.git` checkout and user approval required by `CONSTITUTION.md`
  section 2
- follow the proposal, task, implement, and verify flow in `AGENTS.md`

Do not introduce packaged-extension manifests, registries, or install scripts.
SrujanaSangama modules are plain folders under `domains/` and shared references
under `.agents/skills/`.
