# Module Cleanup Tasks

Parent proposal: `specification/module-cleanup-proposal.md`

## Task 1 - Correct Governance Document Paths

- Files: `CONSTITUTION.md`, `AGENTS.md`, `IMPLEMENTATION-STATUS.md`
- Type: edit
- Proposal clauses satisfied: Proposed Change 3; Verification 3
- Status: Complete

### Verifier Report

- PASS - Active governance references now point to `specification/architecture.md` and `specification/design.md`.
- PASS - Scope stayed inside the task boundary.

## Task 2 - Remove Registry Artifacts

- Files: `.github/copilot-marketplace.json`, `.antigravity-marketplace/marketplace.json`, `GEMINI.md`
- Type: delete/delete/edit
- Proposal clauses satisfied: Proposed Change 2; Verification 1, 2
- Status: Complete

### Verifier Report

- PASS - Registry JSON files were removed.
- PASS - `GEMINI.md` continues to forbid manifest, registry, and install-script patterns without duplicating domain content.

## Task 3 - Refresh Active User-Facing Module Language

- Files: `README.md`, `CONTRIBUTING.md`
- Type: edit
- Proposal clauses satisfied: Proposed Change 1; Verification 1
- Status: Complete

### Verifier Report

- PASS - Active docs now describe modules/domains rather than packaged extensions or registry installation.
- PASS - Active user-facing docs describe direct folder use and module/domain routing.

## Task 4 - Remove Obsolete Local Mode Folder

- Files: `context/`
- Type: delete
- Proposal clauses satisfied: Proposed Change 4; Verification 4
- Status: Complete

### Verifier Report

- PASS - `context/` was removed after the mode authority moved fully to `CONSTITUTION.md`.
- PASS - No active local mode file remains to compete with the Constitution.
