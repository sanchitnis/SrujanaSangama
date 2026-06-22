# Product Loop

> **Intent:** Decide what faculty should be able to do next, and justify it with evidence.
> **Owner:** Sanjay Chitnis, acting in the Product Owner role defined in `AGENTS.md` §2.
> **Cadence:** Weekly or biweekly backlog triage.
> See [`LOOPS.md`](../LOOPS.md) for how this loop relates to the other six.

---

## Why This Loop Exists

`AGENTS.md` already defines the Product Owner role and the rule that "no implementation begins without explicit Product Owner approval on the corresponding `specification/<topic>-proposal.md`." This loop is the *process* by which that approval decision actually gets made well — combining institutional mandate (Loop 2), evidence from real usage (Loop 7), and unscheduled ideas (`specification/BACKLOG.md`, per `CONTRIBUTING.md`) into a prioritized, justified sequence of what gets specified next.

This loop decides **what's next and why**. It does not write the specification itself — that's the Architecture & Design Loop's job, once this loop hands over a mandate.

---

## Inputs to Every Triage Pass

1. **Institutional mandates** from the Business & Institutional Analysis Loop (`loops/business-analysis-loop.md`).
2. **Usage and feedback evidence** from the Telemetry & Feedback Loop (`loops/telemetry-feedback-loop.md`) — what's actually being used, what's stalling, what faculty are explicitly asking for.
3. **The unscheduled ideas register**, `specification/BACKLOG.md` (format defined in `CONTRIBUTING.md` §2).
4. **Current build status**, `specification/IMPLEMENTATION-STATUS.md` — so prioritization accounts for what's already in flight versus untouched.
5. **Research findings**, when the Research Loop routes a suggestion this way.

---

## What a Triage Pass Produces

- An updated **priority order** for `specification/BACKLOG.md` items — promoting an idea from `Idea` to `Ready-to-propose`, or explicitly deferring one with a stated reason.
- For anything promoted to `Ready-to-propose`, a **one-paragraph mandate** — the problem, who it serves, and why it's the right next thing — handed to the Architecture & Design Loop as the seed of a `specification/<topic>-proposal.md`. The Product Loop writes the mandate; the Architecture & Design Loop writes the proposal.
- A short **rationale note** when priority order changes meaningfully, especially when usage evidence overrides an earlier assumption (e.g., "we assumed `teaching-learning` would be used most; Telemetry shows `srujana-shodha` commands run 3x more often — resequencing").

---

## Success Metrics This Loop Is Accountable For

These are the metrics the Product Loop itself is judged against — distinct from the system-level metrics owned by the Telemetry & Feedback Loop (see `loops/telemetry-feedback-loop.md` for the full metric catalogue):

| Metric | What it tells us |
|---|---|
| Time from BACKLOG idea → approved proposal | Is the prioritization process itself a bottleneck? |
| % of shipped domains/commands that get real usage within 30 days | Is this loop picking the right things, not just defensible things? |
| % of backlog promoted on evidence vs. on assumption | Is prioritization actually evidence-led, per the loop's stated intent? |

---

## How This Loop Connects to the Others

- Receives mandates from Loop 2, evidence from Loop 7, ideas from anyone via `BACKLOG.md`.
- Hands a one-paragraph mandate to Loop 4, which is responsible for turning it into a properly scoped proposal per `CONSTITUTION.md` §6.
- Never writes `domains/` content, `architecture.md`, or `design.md` directly — see `LOOPS.md`'s duplication rule.
