# IMPLEMENTATION-STATUS.md — SrujanaSangama Build Status

> This is the single source of truth for **what currently exists on disk** versus what `specification/architecture.md` and `specification/design.md` describe as the eventual full system. `README.md` and `AGENTS.md` deliberately describe only what is marked **Implemented** below, plus a one-line mention that the rest is planned and tracked here. This file is updated as part of the Definition of Done for every task (`AGENTS.md` §6) — a task is not Done until this file reflects it.
>
> Status values: **Not started** · **In progress** · **Implemented**
>
> Last updated: 2026-06 | Maintainer: Sanjay Chitnis (@sanchitnis)

---

## How to Read This File

- A domain is **Implemented** only once it has a `README.md`, at least one working command in `commands/`, and has passed a Verifier check against its proposal.
- A domain with a `README.md` but no working commands yet is **In progress**.
- Everything else described in `specification/architecture.md`/`specification/design.md` that has no folder on disk yet is **Not started** — this is the default state for a freshly-specified platform and is not a problem to be alarmed by, just a status to track honestly.
- `README.md` and `AGENTS.md` should never claim a domain, command, or skill works unless it is marked **Implemented** here.

---

## Domain Status

| Domain | Status | Notes |
|---|---|---|
| `onboarding` | Implemented | Initial workspace and profiles configuration, with enhanced profile collection (GitHub, Scopus, Shodhganga, etc.), memory updates, and Vidwan thesis import CSV template |
| `personal-productivity` | Implemented | Cross-domain layer; includes file-based Kanban task boards (tabular format), CLI task manager, automated task backlog processing, flattened rules/workflows, and 12 promoted global specialist skills |
| `srujana-bodha` | In progress | Contains commands for curriculum strategy review, active learning activity design, curriculum concept mapping, course design, and paper review, including `/curriculum-strategy-check`, `/activity-design-ai-ready`, `/concept-map-network`, `/course-design-brainstormer`, `reva-course-reviewer`, `reva-question-paper-reviewer`, and `reva-session-designer` |
| `srujana-shodha` | In progress | Contains commands for PhD research lifecycle guidance, publication pipeline tracking, thesis sprints, research proposal drafting, and research critique, including `/research-lifecycle`, `/manuscript-check`, `/funding-hunt`, `/proposal-check`, and `/research-critique` |
| `admissions-branding` | Not started | |
| `placement-tpc` | Not started | |
| `academic-admin` | In progress | Contains commands for outcome attainment checking, including `/attainment-check` |
| `innovator` | In progress | Contains commands for patentability analysis and patent drafting, including `/patent-draft` |
| `kaizen-excellence` | In progress | Contains commands for professional development planning, including `/gps-plan` |
| `strategic-planning` | Not started | |

## Shared Infrastructure Status

| Item | Status | Notes |
|---|---|---|
| `specification/architecture.md` | Implemented | Vision document — complete and current |
| `specification/design.md` | Implemented | Technical design document — complete and current |
| `CONSTITUTION.md` | Implemented | Governance conventions — complete and current |
| `AGENTS.md` | Implemented | Governance roles and process — complete and current |
| `README.md` | Implemented | Orientation document — complete and current |
| `CONTRIBUTING.md` | Implemented | Contributor mechanics — complete and current |
| `specification/` folder itself | Implemented | Exists; holds this file, `BACKLOG.md`, and per-change proposals |
| Token routing layer | Implemented | Root `AGENTS.md`, domain routers, Copilot instructions, and Gemini shim minimise context loading across IDEs |
| `.agents/skills/` (shared reference material) | Implemented | Workspace customizations folder containing shared reference and tool configurations |
| `validators/` | Not started | No validator scripts exist on disk yet |
| `srujana-memory/` template set | Not started | Depends on `onboarding` and `personal-productivity` domains existing |
| `reva-information/` seed content | Not started | Owned by REVA IT, not by this repository's build cycle |
| `skills/spec-sync/` audit tool | Implemented | Automated synchronization check script |
| `scripts/local/` helper scripts | Implemented | CLI scripts for path resolution, onboarding setup, log pruning, and health diagnostics |

---

## Suggested Build Order

This is a recommendation, not a constraint — the Product Owner may resequence at any time. It exists so a new contributor has a sensible default starting point.

1. **`onboarding`** — nothing else is usable until a faculty member can get a workspace set up
2. **`personal-productivity`** — the layer every other domain assumes exists
3. **`srujana-bodha`** — highest faculty demand, per `specification/architecture.md` Domain 1
4. **`srujana-shodha`**, **`academic-admin`** — next-highest demand
5. The remaining six domains, in whatever order matches institutional priority at the time

---

## Updating This File

Whenever a task in `specification/<topic>-tasks.md` completes Verifier review with a PASS and is merged, update the relevant row above in the same PR. This is checked as part of the PR checklist in `CONTRIBUTING.md`.
