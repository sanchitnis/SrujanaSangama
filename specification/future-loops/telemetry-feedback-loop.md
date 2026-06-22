# Telemetry & Feedback Loop

> **Intent:** Know whether what's deployed is actually working, for whom, and what to fix next.
> **Owner:** Sanjay Chitnis.
> **Cadence:** Continuous opt-in collection; periodic review.
> See [`LOOPS.md`](../LOOPS.md) for how this loop relates to the other six.

---

## The Constraint This Loop Has to Work Within

SrujanaSangama has no central server by design — `design.md`'s Overview states this explicitly: a shared read-only folder, opened directly in each faculty member's own Claude Code, Copilot, or Antigravity. There is no backend that automatically observes usage the way a SaaS product would. Every mechanism in this loop has to respect that constraint rather than quietly reintroducing a server through the back door.

---

## What Gets Measured

### Usage signal (opt-in, faculty-controlled)

A lightweight personal usage log, written inside the faculty member's own `srujana-memory/` — not transmitted anywhere automatically. Concretely:

- A new file, `my-memory/context/usage-log.md`, which the agent appends a one-line entry to after completing a command: domain, command, date. This is local-only and under the faculty member's full control, consistent with `CONSTITUTION.md`'s privacy stance on `srujana-memory/` contents.
- **Sharing this log back is a separate, explicit, opt-in action** — for example, during a `/weekly-review` or `/monthly-report` (per `design.md`'s `personal-productivity` domain), the agent can offer: *"Would you like to include a summary of which commands you used this month in your shareable report, to help us improve the platform?"* If yes, that summary — not the raw log — is what gets shared, and only because the faculty member said yes that specific time.
- This loop never assumes consent persists from one sharing instance to the next; it asks again each time, since the underlying memory file is private by default per `CONSTITUTION.md`.

### Faculty feedback (direct and continuous)

- An open channel for faculty to report friction or request a feature — feeding directly into `specification/BACKLOG.md` (per `CONTRIBUTING.md` §2's format) as `Source: user-report`.
- Specifically prompted feedback after a new domain's first month live, coordinated with the Deployment & Adoption Loop's adoption-support work.

### System performance parameters

Since there's no server, "system performance" here means something different from a typical product:

- **Spec clarity** — how often does a command file leave an agent uncertain (measured indirectly via Implementation Loop query rates, and directly via faculty reporting an agent "got confused").
- **Cross-IDE consistency** — whether a command behaves the same way in Claude Code, Copilot, and Antigravity, spot-checked periodically rather than continuously monitored.
- **Token/context cost** — whether a domain's `rules/` and `skills/` have grown large enough to slow down or degrade a session; this is the practical proxy for "performance" in a markdown-and-agent system.

---

## What a Periodic Review Produces

- A short **evidence brief** — patterns from the usage log summaries and direct feedback received since the last review, written for the Product Loop's next triage pass. Lives at `telemetry/reviews/YYYY-MM.md`.
- Flags anything that looks like an institutional-level concern (a whole school not adopting something) up to the Business & Institutional Analysis Loop, rather than treating it purely as a product prioritization question.
- Flags anything that looks like a deeper pattern about the building method itself (not just this platform) over to the Research Loop.

---

## How This Loop Connects to the Others

- Receives live usage starting from Loop 6's rollout.
- Hands an evidence brief to Loop 3 for the next prioritization pass — this is the primary feedback path that makes the whole seven-loop system actually a loop rather than a one-way pipeline.
- Occasionally flags institutional concerns to Loop 2, or building-method patterns to Loop 1.
- Never collects anything from `srujana-memory/` without the explicit, per-instance opt-in described above — this is a hard constraint, not a preference, consistent with `CONSTITUTION.md`'s treatment of personal memory as private by default.
