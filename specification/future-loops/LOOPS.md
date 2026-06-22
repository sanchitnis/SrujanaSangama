# LOOPS.md — SrujanaSangama Top-Level Loop Map

> SrujanaSangama is not built, deployed, and maintained as a single straight-line project. It runs as a set of **loops** — concurrent cycles, each with its own intent, owner, cadence, and re-entry path. This file is the map of how the loops connect. Each loop has its own charter file under `loops/`, which is the single source of truth for that loop's detail. This file does not restate any loop's internals — only how they hand off to one another.
>
> Last updated: 2026-06 | Maintainer: Sanjay Chitnis (@sanchitnis)

---

## Why Loops, Not a Pipeline

A conventional SDLC is usually drawn as a line: research → requirements → design → build → deploy → maintain. SrujanaSangama doesn't work that way, for two reasons specific to how it is being built:

1. **It is built Software-3.0-style** — natural-language specifications read directly by AI agents, with no compiled build step. The cost of revisiting an earlier decision is low, so every loop needs a re-entry path, not just a one-way handoff to the next stage.
2. **Several loops run concurrently, at different speeds, by different people.** Research observation is slow and occasional. Implementation and feedback are continuous. A straight-line pipeline can't represent that; a set of loops that synchronize at defined hand-off points can.

---

## The Seven Loops

| # | Loop | Intent (one sentence) | Owner | Cadence | Charter |
|---|---|---|---|---|---|
| 1 | **Research** | Notice, name, and report what building an institutional platform this way actually teaches us | Sanjay Chitnis, with any contributor who wants to co-author | Continuous observation; periodic synthesis (per semester) | [`loops/research-loop.md`](loops/research-loop.md) |
| 2 | **Business & Institutional Analysis** | Confirm the platform still serves REVA's actual priorities, and secure the decisions only REVA leadership can make | Sanjay Chitnis | Aligned to REVA Summit / REVA Manthan calendar | [`loops/business-analysis-loop.md`](loops/business-analysis-loop.md) |
| 3 | **Product** | Decide what faculty should be able to do next, and justify it with evidence | Sanjay Chitnis (Product Owner role, per `AGENTS.md`) | Weekly/biweekly backlog triage | [`loops/product-loop.md`](loops/product-loop.md) |
| 4 | **Architecture & Design** | Keep `architecture.md` (what) and `design.md` (how) correct and internally consistent as the system grows | Sanjay Chitnis, via the `specification/` proposal mechanism | Per proposal | [`loops/architecture-design-loop.md`](loops/architecture-design-loop.md) |
| 5 | **Implementation** | Turn an approved proposal into working domain content, regardless of which contributor or IDE does it | Any contributor, via Coordinator/Implementor/Verifier roles in `AGENTS.md` | Per task, continuous once contributors are active | [`loops/implementation-loop.md`](loops/implementation-loop.md) |
| 6 | **Deployment & Adoption** | Get a working domain into faculty hands and help them actually start using it | Sanjay Chitnis, with REVA IT for shared-folder distribution | Per domain release | [`loops/deployment-adoption-loop.md`](loops/deployment-adoption-loop.md) |
| 7 | **Telemetry & Feedback** | Know whether what's deployed is actually working, for whom, and what to fix next | Sanjay Chitnis | Continuous opt-in collection; periodic review | [`loops/telemetry-feedback-loop.md`](loops/telemetry-feedback-loop.md) |

---

## How the Loops Hand Off to Each Other

```
                    ┌─────────────────┐
                    │   1. RESEARCH    │  observes all loops,
                    │                  │  periodically publishes findings
                    └────────┬─────────┘
                             │ findings feed back into how loops 2–7 are run
                             ▼
   ┌─────────────────────────────────────────────────────────────┐
   │                                                              │
   │   2. BUSINESS &           3. PRODUCT                        │
   │   INSTITUTIONAL    ─────▶  decides WHAT'S NEXT               │
   │   ANALYSIS                 and WHY, with evidence            │
   │   confirms institutional       │                             │
   │   priority and approval        │ one-line mandate            │
   │                                 ▼                             │
   │                        4. ARCHITECTURE & DESIGN              │
   │                           turns a mandate into an approved   │
   │                           specification/ proposal             │
   │                                 │                             │
   │                                 │ approved proposal + tasks   │
   │                                 ▼                             │
   │                        5. IMPLEMENTATION                      │
   │                           builds the approved domain content  │
   │                                 │                             │
   │                                 │ Verifier PASS + merged PR   │
   │                                 ▼                             │
   │                        6. DEPLOYMENT & ADOPTION                │
   │                           rolls the domain out to faculty      │
   │                                 │                             │
   │                                 │ faculty start using it       │
   │                                 ▼                             │
   │                        7. TELEMETRY & FEEDBACK                 │
   │                           collects usage signal and feedback   │
   │                                 │                             │
   └─────────────────────────────────┼─────────────────────────────┘
                                     │ evidence feeds back into
                                     ▼
                            3. PRODUCT (next prioritization pass)
```

The loop from 3 → 4 → 5 → 6 → 7 → back to 3 is the **main operating loop** — this is what runs continuously once the platform has live faculty users. Loops 1 and 2 sit alongside it: Loop 2 gates entry into the main loop (nothing reaches Loop 4 without institutional sign-off), and Loop 1 observes the whole thing without participating in any single hand-off.

---

## The One Rule That Keeps This From Duplicating the Other Six Documents

Each loop charter states **what that loop decides and how**, never **what the platform does or how it's built** — that remains exclusively the job of `architecture.md` and `design.md`. A loop charter that finds itself describing a domain's capability in detail, rather than referencing it, has drifted out of scope. This mirrors the rule already enforced across `CONSTITUTION.md`, `AGENTS.md`, `README.md`, and `CONTRIBUTING.md`.

| If you're looking for... | Go to... |
|---|---|
| What the platform does | `architecture.md` |
| How the platform is built | `design.md` |
| Conventions and guardrails for changing the platform | `CONSTITUTION.md` |
| Roles and the spec→build cycle for a single change | `AGENTS.md` |
| How to actually contribute a change | `CONTRIBUTING.md` |
| What currently exists vs. what's planned | `specification/IMPLEMENTATION-STATUS.md` |
| Why we're building it this way, and what we're learning | `loops/research-loop.md` |
| Whether REVA leadership has approved a direction | `loops/business-analysis-loop.md` |
| What's being prioritized next, and why | `loops/product-loop.md` |
| The proposal mechanism for an architecture/design change | `loops/architecture-design-loop.md` (which then points to `CONSTITUTION.md` §6) |
| How multiple contributors on different IDEs build the same proposal together | `loops/implementation-loop.md` |
| How a finished domain actually reaches faculty | `loops/deployment-adoption-loop.md` |
| How we know if it's working | `loops/telemetry-feedback-loop.md` |

---

## Multi-Contributor, Multi-IDE Collaboration — the Cross-Cutting Concern

Loops 4 through 7 are designed to be worked by different people, on different IDEs (Claude Code, GitHub Copilot in VS Code, Google Antigravity), against the same shared git repository. This works because:

- Everything is plain markdown — no IDE-specific build artifact, no compiled output that only one tool can produce.
- The `specification/<topic>-proposal.md` → `specification/<topic>-tasks.md` → PR cycle (detailed in `AGENTS.md` and `loops/implementation-loop.md`) is the same regardless of which IDE a contributor used to do the work.
- Git branching and PR review (per `CONTRIBUTING.md`) is the actual collision-prevention mechanism — there is no additional locking system. A task is "claimed" simply by adding the contributor's name next to it in the `-tasks.md` file before starting, which is sufficient given the small scale of expected concurrent contribution.

See `loops/implementation-loop.md` for the full protocol.
