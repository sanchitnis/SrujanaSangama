# IMPLEMENTATION-STATUS.md — SrujanaSangama Build Status

> This is the single source of truth for **what currently exists on disk** versus what `architecture.md` and `design.md` describe as the eventual full system. `README.md` and `AGENTS.md` deliberately describe only what is marked **Implemented** below, plus a one-line mention that the rest is planned and tracked here. This file is updated as part of the Definition of Done for every task (`AGENTS.md` §6) — a task is not Done until this file reflects it.
>
> Status values: **Not started** · **In progress** · **Implemented**
>
> Last updated: 2026-06 | Maintainer: Sanjay Chitnis (@sanchitnis)

---

## How to Read This File

- A domain is **Implemented** only once it has a `README.md`, at least one working command in `commands/`, and has passed a Verifier check against its proposal.
- A domain with a `README.md` but no working commands yet is **In progress**.
- Everything else described in `architecture.md`/`design.md` that has no folder on disk yet is **Not started** — this is the default state for a freshly-specified platform and is not a problem to be alarmed by, just a status to track honestly.
- `README.md` and `AGENTS.md` should never claim a domain, command, or skill works unless it is marked **Implemented** here.

---

## Domain Status

| Domain | Status | Notes |
|---|---|---|
| `onboarding` | Not started | First domain to build — nothing else can be used without it |
| `personal-productivity` | Not started | Cross-domain layer; depends on `onboarding` existing first |
| `teaching-learning` | Not started | |
| `srujana-shodha` | Not started | |
| `admissions-branding` | Not started | |
| `placement-tpc` | Not started | |
| `academic-admin` | Not started | |
| `innovator` | Not started | |
| `kaizen-excellence` | Not started | |
| `strategic-planning` | Not started | |

## Shared Infrastructure Status

| Item | Status | Notes |
|---|---|---|
| `architecture.md` | Implemented | Vision document — complete and current |
| `design.md` | Implemented | Technical design document — complete and current |
| `CONSTITUTION.md` | Implemented | Governance conventions — complete and current |
| `AGENTS.md` | Implemented | Governance roles and process — complete and current |
| `README.md` | Implemented | Orientation document — complete and current |
| `CONTRIBUTING.md` | Implemented | Contributor mechanics — complete and current |
| `specification/` folder itself | Implemented | Exists; holds this file, `BACKLOG.md`, and per-change proposals |
| `skills/` (shared reference material) | Not started | No skill folders exist on disk yet |
| `validators/` | Not started | No validator scripts exist on disk yet |
| `srujana-memory/` template set | Not started | Depends on `onboarding` and `personal-productivity` domains existing |
| `reva-information/` seed content | Not started | Owned by REVA IT, not by this repository's build cycle |
| `skills/spec-sync/` audit tool | Not started | Referenced in `CONTRIBUTING.md` but not yet built |

---

## Structural Design Changes (Target Shape, Not Build Status)

Some entries in `specification/` change the *shape* `design.md` describes — what a domain should look like once built — without anything moving from Not started to Implemented. These are logged here for traceability, separately from the domain/infrastructure build status above.

| Change | Proposal | Effect |
|---|---|---|
| Domain-owned skills | `specification/skills-restructure-proposal.md` (2026-06) | Every domain's canonical folder template now includes its own `skills/` subfolder; the repo-root `skills/` folder is narrowed to only the 6 skills genuinely shared by 3+ domains plus `reva-branding`. No domain's status changes as a result — this only affects where a skill will be placed once that domain is actually built. |
| Seven-loop product engineering structure | `LOOPS.md` + `loops/*.md` (2026-06) | Introduces Research, Business & Institutional Analysis, Product, Architecture & Design, Implementation, Deployment & Adoption, and Telemetry & Feedback as explicit top-level loops with their own charters, hand-off points, and working-output folders (`research/`, `business-analysis/`, `deployment/`, `telemetry/`). `CONSTITUTION.md` and `AGENTS.md` updated with corresponding ownership and cross-reference entries. This is process scaffolding around the existing build cycle, not a change to any domain's build status. |

---

## Suggested Build Order

This is a recommendation, not a constraint — the Product Owner may resequence at any time. It exists so a new contributor has a sensible default starting point.

1. **`onboarding`** — nothing else is usable until a faculty member can get a workspace set up
2. **`personal-productivity`** — the layer every other domain assumes exists
3. **`teaching-learning`** — highest faculty demand, per `architecture.md` Domain 1
4. **`srujana-shodha`**, **`academic-admin`** — next-highest demand
5. The remaining six domains, in whatever order matches institutional priority at the time

---

## Updating This File

Whenever a task in `specification/<topic>-tasks.md` completes Verifier review with a PASS and is merged, update the relevant row above in the same PR. This is checked as part of the PR checklist in `CONTRIBUTING.md`.
