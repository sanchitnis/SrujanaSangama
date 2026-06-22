# Research Loop

> **Intent:** Notice, name, and report what building an institutional platform this way actually teaches us.
> **Owner:** Sanjay Chitnis, with any contributor who wants to co-author.
> **Cadence:** Continuous observation; periodic synthesis (per semester).
> See [`LOOPS.md`](../LOOPS.md) for how this loop relates to the other six.

---

## Why This Loop Exists

SrujanaSangama is being built primarily through natural-language specifications read directly by AI coding agents (Claude Code, GitHub Copilot, Google Antigravity) — no compiled plugin system, no manifest format, no installable package. `design.md`'s Overview already states this as a design choice. What this loop adds is the observation that **the way this platform is being built may itself be a research-worthy instance of "Software 3.0"** — software whose primary artifact is natural language, executed directly by a model rather than compiled first — applied at the scale of a real, multi-domain institutional system with multiple human contributors.

This loop does not change how the platform is built. It watches the other six loops as they run, and asks: what is actually happening here that's worth naming?

---

## What This Loop Produces

- **A running research log** — informal notes captured as they happen, not retrofitted at the end of a semester. Lives at `research/log/YYYY-MM.md`.
- **Periodic synthesis notes** — every semester, a short write-up pulling the log into named observations. Lives at `research/synthesis/YYYY-semester.md`.
- **Candidate papers or talks**, once a synthesis note suggests something is mature enough to share externally. These live outside this repository once drafted for submission, but the decision to pursue one is logged here.

This loop does **not** produce changes to `architecture.md`, `design.md`, or any domain content directly — if an observation implies the platform itself should change, that goes through the Product Loop and then the Architecture & Design Loop like any other proposed change, with a note in the research log linking to the resulting proposal.

---

## What to Watch For

This is a starting list, not an exhaustive one — the loop's job includes expanding it.

- **Spec-to-behavior fidelity** — how reliably does a `domains/<name>/commands/<command>.md` file, written once, produce consistent behavior across Claude Code, Copilot, and Antigravity? Where does it diverge, and why?
- **The proposal-to-implementation gap** — how often does an approved `specification/<topic>-proposal.md` survive unchanged through the Coordinator → Implementor → Verifier cycle, versus needing a clarifying `<!-- AGENT QUERY: -->` mid-implementation? A high query rate on a particular kind of proposal is itself a finding.
- **Multi-agent, multi-contributor consistency** — when two contributors, on two different IDEs, both reference `CONSTITUTION.md`, do their agents interpret an ambiguous rule the same way? Divergence here is both a process risk (handled by the Implementation Loop) and a research signal (handled here).
- **The mode-boundary discipline** (`CONSTITUTION.md` §2) — does the Usage Mode / Development Mode distinction actually hold up in practice, or do agents drift? This is a direct, observable test of whether "stated boundary + agent self-discipline" is a viable control mechanism at all, independent of this specific platform.
- **Faculty-side adoption patterns** — once Loop 6 (Deployment) and Loop 7 (Telemetry) are live, how faculty actually use natural-language commands versus how they were designed to be used is itself worth comparing.

---

## How This Loop Connects to the Others

- It reads the outputs of Loops 4–7 (proposals, tasks, PRs, deployment notes, feedback) as raw material — it does not need a separate data-collection mechanism of its own beyond reading what those loops already produce.
- Its only "output" toward the rest of the system is, occasionally, a suggestion routed into the Product Loop's backlog (see `loops/product-loop.md`) — for example, "we keep seeing X go wrong; should we change how proposals are written?"
- It never bypasses the Architecture & Design Loop to change `architecture.md` or `design.md` directly, even when a research finding is highly relevant — see `LOOPS.md`'s duplication rule.
