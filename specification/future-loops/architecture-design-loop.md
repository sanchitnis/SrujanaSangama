# Architecture & Design Loop

> **Intent:** Keep `architecture.md` (what) and `design.md` (how) correct and internally consistent as the system grows.
> **Owner:** Sanjay Chitnis, via the `specification/` proposal mechanism.
> **Cadence:** Per proposal.
> See [`LOOPS.md`](../LOOPS.md) for how this loop relates to the other six.

---

## Why This Loop Exists

This loop already has its full process defined elsewhere — `CONSTITUTION.md` §6 (the `specification/` folder), §2 (the mode boundary that gates when this work can even happen), and `AGENTS.md` §3–§5 (the Coordinator role specifically, plus the escalation protocol). This charter does not repeat any of that. Its only job is to state where this loop sits relative to the other six, and what it receives and produces at its boundary.

---

## What Triggers This Loop

A one-paragraph mandate from the Product Loop (`loops/product-loop.md`) — *what* should be built next and *why*, but not *how*. Turning that mandate into a properly scoped `specification/<topic>-proposal.md`, with explicit Scope Boundaries and Verification criteria, is this loop's entire job.

## What This Loop Produces

A proposal approved by the Product Owner, per the existing process in `CONSTITUTION.md` §6 — nothing more is defined here, since that document already owns the detail.

## What Happens Next

Once approved, the proposal hands directly to the Implementation Loop (`loops/implementation-loop.md`), which runs the Coordinator → Implementor → Verifier cycle already defined in `AGENTS.md` §3–§4.

---

## The One Thing Worth Adding Here That Isn't Already Stated Elsewhere

Because multiple contributors on different IDEs may all be capable of drafting a proposal, this loop's single coordination rule is: **only the Product Owner approves a proposal**, regardless of who drafted it or which IDE they used. A contributor can draft `specification/<topic>-proposal.md` directly if they have a mandate from the Product Loop (or a clear enough idea logged in `BACKLOG.md`), but it does not move to the Implementation Loop until Sanjay has approved it — exactly as `AGENTS.md` §2 already states for the Product Owner role generally.

---

## How This Loop Connects to the Others

- Receives a mandate from Loop 3.
- Hands an approved proposal to Loop 5.
- Is gated by the mode boundary in `CONSTITUTION.md` §2 — this loop's work only happens in Development Mode.
- See `LOOPS.md` for the full hand-off diagram, and `CONSTITUTION.md` / `AGENTS.md` for the actual mechanics of this loop's process.
