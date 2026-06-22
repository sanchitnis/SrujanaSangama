# Implementation Loop

> **Intent:** Turn an approved proposal into working domain content, regardless of which contributor or IDE does it.
> **Owner:** Any contributor, via the Coordinator/Implementor/Verifier roles defined in `AGENTS.md` §3.
> **Cadence:** Per task, continuous once contributors are active.
> See [`LOOPS.md`](../LOOPS.md) for how this loop relates to the other six.

---

## Why This Charter Exists Alongside `AGENTS.md`

`AGENTS.md` §3–§4 already defines the Coordinator, Implementor, and Verifier roles and the sprint lifecycle in full — this charter does not repeat that. What `AGENTS.md` doesn't yet address is the case this platform is explicitly designed for: **multiple people, each on a different IDE (Claude Code, GitHub Copilot in VS Code, Google Antigravity), working against the same git repository at the same time.** That's this charter's entire job.

---

## The Core Problem This Loop Solves

Two contributors, on two different machines and two different IDEs, could both pick up a task from the same `specification/<topic>-tasks.md` file without knowing the other has started. Or one contributor's agent could interpret an ambiguous `CONSTITUTION.md` rule slightly differently from another's. Neither failure mode needs new tooling to solve — both are solved by making existing git discipline (already in `CONTRIBUTING.md`) and existing markdown files (already in `specification/`) do double duty as coordination signals.

---

## The Claiming Protocol

Before starting a task from an approved `specification/<topic>-tasks.md`:

1. **Check the file first.** If a task already has a contributor's name next to it and is not yet marked complete, do not start it — pick a different task or check with that contributor.
2. **Claim it by adding your name and today's date** next to the task, in the same commit or PR that begins your work on it: `- [ ] T-003: ... — @yourname, 2026-06-19`.
3. **Commit the claim early**, even before the task is finished — this is what makes the claim visible to someone else who checks the file five minutes later from a different IDE.
4. **Release a claim** (remove your name) if you stop working on a task before finishing it, so someone else can pick it up.

This is intentionally lightweight — a comment in a markdown file, not a locking system — because the expected scale of concurrent contribution is small (a handful of people, not a large engineering team), and git's own merge conflict on the `-tasks.md` file itself is a natural, sufficient backstop if two people claim the same task within seconds of each other.

---

## Consistency Across IDEs and Agents

Since `CONSTITUTION.md`, `AGENTS.md`, and the relevant `specification/<topic>-proposal.md` are the same plain-text files regardless of which IDE reads them, the main risk is not the files themselves but **how literally an agent follows the Escalation & Ambiguity Protocol already defined in `AGENTS.md` §5**. This loop adds one operating norm on top of that protocol: when a contributor's agent raises an `<!-- AGENT QUERY: -->` comment, the contributor should resolve it with the Product Owner *before* continuing, even if their particular IDE would technically let them proceed — the protocol's value depends on this being honored consistently across every IDE, not just the one it happened to be raised in.

---

## Definition of Done, Restated for the Multi-Contributor Case

`AGENTS.md` §6 already defines Definition of Done for a single task. For this loop specifically: a task is not actually finished until the claim next to it in `-tasks.md` is updated to reflect completion (not just removed), so the file remains an accurate record of who built what — this matters for the Research Loop's later observation of how implementation actually unfolded across contributors (see `loops/research-loop.md`).

---

## How This Loop Connects to the Others

- Receives an approved proposal and task list from Loop 4.
- Hands a merged, Verifier-passed PR to Loop 6 for rollout.
- A task's progress (claimed, in progress, Verifier-passed) is exactly the kind of raw material the Research Loop reads to observe spec-to-behavior fidelity and multi-agent consistency — see `loops/research-loop.md`.
