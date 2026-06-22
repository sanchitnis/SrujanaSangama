# Business & Institutional Analysis Loop

> **Intent:** Confirm the platform still serves REVA's actual priorities, and secure the decisions only REVA leadership can make.
> **Owner:** Sanjay Chitnis.
> **Cadence:** Aligned to REVA's own planning calendar — REVA Summit (annual) and REVA Manthan (periodic operational review), per `architecture.md` Domain 5.
> See [`LOOPS.md`](../LOOPS.md) for how this loop relates to the other six.

---

## Why This Loop Exists

Every other loop assumes that what's being built is worth building. This loop is where that assumption gets checked against REVA's actual institutional reality — Vision and Mission alignment (`architecture.md`'s opening sections), NIRF/NAAC priorities, budget and staffing capacity, data governance and IT policy, and plain institutional risk. It is also the loop responsible for **decisions only REVA leadership can make** — things no amount of good engineering can substitute for, such as whether a new domain touching student data requires a policy review, or whether REVA IT can actually commit to maintaining a new shared OneDrive folder.

This loop does not design or specify anything. It produces **institutional permission and priority**, which the Product Loop then translates into a backlog.

---

## What This Loop Produces

- **An institutional alignment note per major proposal direction** — a short statement of how a candidate direction connects to REVA's Vision/Mission, NIRF/NAAC strategy, or a specific REVA Summit/Manthan outcome. Lives at `business-analysis/alignment-notes/<topic>.md`.
- **Go/no-go and sequencing decisions** — when two candidate directions compete for attention, this is where institutional priority (not engineering convenience) breaks the tie. Logged as a short decision record at `business-analysis/decisions/YYYY-MM-<topic>.md`.
- **Risk and policy flags** — anything requiring REVA IT, legal, or data governance sign-off before the Product Loop should even consider it. Logged the same way.

---

## What Feeds Into This Loop

- Outcomes from REVA Summit (annual strategic meeting — Chancellor's vision, school-level goal setting, peer benchmarking) and REVA Manthan (periodic operational review), per `architecture.md` Domain 5.
- The Institutional Development Plan (IDP), also per `architecture.md` Domain 5 — any platform direction should be checkable against the IDP's current priorities.
- Findings surfaced by the Telemetry & Feedback Loop, when adoption or satisfaction data suggests an institutional-level concern (e.g., a whole school isn't adopting a domain — is that a product problem or an institutional one?).

---

## What This Loop Hands to the Product Loop

A short mandate, not a specification: *what* matters institutionally and *why*, with enough context for the Product Loop to translate it into specific backlog items. For example: "REVA Summit flagged IQAC documentation burden as a top-3 institutional pain point this year" is a Business & Institutional Analysis Loop output. "Build `/aqar-generate` before `/atr-track`, because IQAC documentation burden is this year's top-3 pain point" is the Product Loop's job, not this one's.

---

## How This Loop Connects to the Others

- It gates entry into the main operating loop (Product → Architecture & Design → Implementation → Deployment → Telemetry) — nothing reaches Loop 4 (Architecture & Design) without having passed through here first, at least implicitly for routine work and explicitly for anything touching policy, data governance, or budget.
- It does not interact directly with Implementation, Deployment, or Telemetry — those only ever hear from this loop indirectly, via the Product Loop's backlog.
- See `LOOPS.md` for the full hand-off diagram.
