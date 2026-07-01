# Module Cleanup Proposal

## Problem

Some active operational files still describe SrujanaSangama as a packaged extension and registry-based system even though the current Constitution and design intent define it as a plain-markdown module repository opened directly by Codex, GitHub Copilot, Claude Code, and Google Antigravity.

The Constitution also points agents to root `architecture.md` and `design.md`, but the current authoritative files live at `specification/architecture.md` and `specification/design.md`. This causes agents to look in the wrong place and wastes context.

## Proposed Change

1. Replace active packaged-extension and registry language with module/domain language.
2. Remove registry artifacts that only supported the retired packaged-extension model.
3. Update `CONSTITUTION.md`, `AGENTS.md`, `CONTRIBUTING.md`, and `IMPLEMENTATION-STATUS.md` references from root `architecture.md` / `design.md` to `specification/architecture.md` / `specification/design.md`.
4. Remove the obsolete local `context/` mode folder so `CONSTITUTION.md` remains the single source for Usage Mode / Development Mode.

## Scope Boundaries

### In Scope

- `CONSTITUTION.md`
- `AGENTS.md`
- `CONTRIBUTING.md`
- `IMPLEMENTATION-STATUS.md`
- `README.md`
- `GEMINI.md`
- `context/`
- `.github/copilot-marketplace.json`
- `.antigravity-marketplace/marketplace.json`
- this proposal and its task file

### Out of Scope

- Deprecated packaged-extension archives under `deprecated/`
- Historical eval reports and logs under `eval/`
- Old proposal archives that explicitly describe retired packaged-extension work
- Moving `specification/architecture.md` or `specification/design.md`
- Renaming domain command files

## Verification

The change is accepted when:

1. Active entry-point files no longer present SrujanaSangama as a packaged extension registry.
2. Registry JSON files are removed.
3. Active governance files point to `specification/architecture.md` and `specification/design.md`.
4. No active local mode file remains to compete with the Constitution's Usage Mode / Development Mode rules.
5. Deprecated and historical files are not rewritten as if they are current operational guidance.

## Product Owner Approval

Approved by the current Development Mode instruction: "fix all plugin to module change issues. Remove the marketplace concept if it is only for plugins. fix constitution for correct address for architecture and design."
