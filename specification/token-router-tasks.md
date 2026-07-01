# Token Router Tasks

Parent proposal: `specification/token-router-proposal.md`

## Task 1 - Sanction Router Conventions

- Files: `CONSTITUTION.md`, `specification/token-router-proposal.md`, `specification/token-router-tasks.md`
- Type: edit/create
- Proposal clauses satisfied: Proposed Change 4; Verification 3
- Status: Complete

### Verifier Report

- PASS - `CONSTITUTION.md` now permits domain-level `AGENTS.md` files and host shims as routing indexes.
- PASS - No manifest, plugin, install, or marketplace convention was introduced.
- PASS - Scope stayed within the task boundary.

## Task 2 - Root And Host Entry Routers

- Files: `AGENTS.md`, `.github/copilot-instructions.md`, `GEMINI.md`
- Type: edit/create/create
- Proposal clauses satisfied: Proposed Change 1, 2; Verification 1, 2, 5, 6
- Status: Complete

### Verifier Report

- PASS - Root `AGENTS.md` routes first and limits Usage Mode reads.
- PASS - Development Mode gate and Scrum lifecycle are preserved.
- PASS - Copilot and Gemini/Antigravity shims defer to the same router.
- PASS - No domain command or rule content was duplicated.

## Task 3 - Domain Local Routers

- Files: `domains/*/AGENTS.md`
- Type: create
- Proposal clauses satisfied: Proposed Change 3; Verification 4, 6
- Status: Complete

### Verifier Report

- PASS - Every current domain has a compact local `AGENTS.md`.
- PASS - Routers list loading strategy and avoid duplicating command/rule/skill content.
- PASS - Files are inside sanctioned domain folders.

## Task 4 - Implementation Status

- Files: `IMPLEMENTATION-STATUS.md`
- Type: edit
- Proposal clauses satisfied: Verification 7
- Status: Complete

### Verifier Report

- PASS - Shared infrastructure status now records the token routing layer.
- PASS - No domain implementation status was changed.
