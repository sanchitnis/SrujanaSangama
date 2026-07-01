# Token Router Proposal

## Problem

Agents currently have to infer how much SrujanaSangama context to load from long root-level documentation. This increases token use, slows task startup, and raises the chance that an agent reads unrelated domains or governance documents before doing a narrow faculty task.

The platform also needs clearer cross-IDE routing for Codex, GitHub Copilot, and Google Antigravity-style agents while preserving the plain-markdown, no-manifest architecture required by `CONSTITUTION.md`.

## Proposed Change

1. Convert root `AGENTS.md` into a compact router-first instruction file:
   - start every session in Usage Mode
   - load Development Mode governance only after confirmation
   - classify user intent before reading domain material
   - load only the selected domain, selected command, directly referenced rules, and directly needed skills
2. Add IDE-specific shims:
   - `.github/copilot-instructions.md` mirrors only the routing layer for GitHub Copilot
   - `GEMINI.md` points Gemini/Antigravity-style agents to the same routing protocol
3. Add `domains/<domain>/AGENTS.md` files as domain-local routing indexes. These files are not new domain intelligence; they tell agents which local commands, rules, and shared skills to read lazily.
4. Update `CONSTITUTION.md` to sanction domain-level `AGENTS.md` files and host shims as routing indexes, while keeping all substantive intelligence in `domains/`, `skills/`, and the vision documents.

## Scope Boundaries

### In Scope

- Root `AGENTS.md`
- `CONSTITUTION.md`
- `.github/copilot-instructions.md`
- `GEMINI.md`
- `domains/*/AGENTS.md`
- `specification/token-router-tasks.md`
- `IMPLEMENTATION-STATUS.md` shared infrastructure row updates

### Out of Scope

- Moving `architecture.md` or `design.md`
- Rewriting existing command workflows
- Adding plugin manifests, marketplace registries, or install scripts
- Changing any faculty-facing domain behavior beyond context-loading instructions
- Reading every command or every rule during normal task startup

## Verification

The change is accepted when:

1. Root `AGENTS.md` clearly instructs agents to route first and load only relevant context in Usage Mode.
2. Root `AGENTS.md` still preserves the Development Mode gate and Agentic Scrum lifecycle.
3. `CONSTITUTION.md` explicitly permits `domains/<domain>/AGENTS.md`, `.github/copilot-instructions.md`, and `GEMINI.md` as routing shims without allowing manifests or marketplace packaging.
4. Every current domain folder has a local `AGENTS.md` with a compact context-loading protocol.
5. GitHub Copilot and Gemini/Antigravity-style entry points defer to the same router rather than duplicating domain content.
6. No command, rule, or skill content is duplicated into the router files.
7. `IMPLEMENTATION-STATUS.md` records the routing infrastructure as implemented.

## Product Owner Approval

Approved by the current Development Mode instruction: "implement all the suggestions."
