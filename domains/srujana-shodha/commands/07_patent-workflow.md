<!-- Paste this workflow into a PhD Scholar session when the scholar wants to identify a patentable invention and begin the patent filing process. This workflow invokes the patent-generator plugin chain. -->

# Session Type: Patent Identification & Filing Workflow

**Purpose:** Identify a patentable research output, assess eligibility under §14.1 Option B, and invoke the `patent-generator` plugin chain to begin the patent disclosure draft.

**Estimated total time:** 30–45 minutes for identification and handoff; additional sessions in patent-generator for full drafting

**Reference:** `plugins/patent-generator/workflow.md`

---

## Phase 1 — §14.1 Option B Check (5 min)

Activate `patent-agent.md` → §14.1 Option B eligibility check.

Confirm with the scholar:
1. Is the invention derived from the PhD research?
2. Has the invention been publicly disclosed anywhere? (public disclosure = 12-month India grace period for provisional filing under Patents Act §12)
3. Who are the inventors? (Typically: scholar + guide + REVA as assignee)

If any disclosure concern exists: flag urgency — *"File a provisional application before the 12-month window closes."*

---

## Phase 2 — Patentability Assessment (15 min)

Work through the 4 criteria:

| Criterion | Discussion |
|---|---|
| Novelty | Prior art search results? Databases: USPTO, Espacenet, IndiaIP |
| Inventive Step | Would a CS expert find this obvious? |
| Industrial Application | Practical deployment scenario |
| Not §3(k) excluded | Technical effect beyond algorithm per se? |

Produce a patentability assessment:
- Green (all 4 criteria met) → proceed to Phase 3
- Amber (1–2 concerns) → address concerns before filing
- Red (§3(k) excluded, no technical effect) → recommend publication route instead; inform scholar that Option B requires a *granted* patent

---

## Phase 3 — Filing Type Decision (5 min)

| Scenario | Recommendation |
|---|---|
| Idea formed, full claims not ready | Provisional application (secures priority date) |
| Research complete, claims defined | Complete specification |
| Need granted patent before submission deadline | Begin NOW — India grant takes 2–5 years |

Remind: §14.1 Option B requires a **granted** patent. A provisional filing does not satisfy Option B.

---

## Phase 4 — Patent Generator Handoff (5 min)

*"Your invention looks patentable. I'm handing you to the Patent Generator workflow now. It will walk you through: invention disclosure form → prior art review → claim drafting → abstract → specification sections."*

Reference: `plugins/patent-generator/workflows/01_input.md` → `08_export.md`

Pass to the patent-generator plugin with this context:
- Scholar name, REVA University as assignee
- Guide name as co-inventor
- Invention: [brief description from Phase 2]
- Status: provisional / complete
- PhD research area: [from `context/scholar-profile.md`]

---

## Phase 5 — Patent Tracker Update (3 min)

After handoff (or when returning from patent-generator), update `context/research-tracker.md` → patent tracker:

```
## Patent Tracker
| # | Title (short) | Filing Type | Filing Date | Status | §14.1 Option B Eligible? |
|---|---|---|---|---|---|
| 1 | [title] | Provisional/Complete | [date] | Filed/Published/Granted | No (pending) / Yes (granted) |
```

---

## Output Template

```
## Patent Workflow Session — [Name] — [Date]

**Invention:** [brief description]
**Patentability assessment:** [Green / Amber / Red]
**Concerns flagged:** [list or "none"]
**Filing type recommended:** [Provisional / Complete]
**Prior art search done:** [yes / no]
**§3(k) technical effect confirmed:** [yes / no]

**Patent generator handoff:** [initiated / not yet — reason]

**§14.1 Option B status:**
- Provisional filed: [date or not yet]
- Complete specification: [date or not yet]
- Grant status: [not yet / published / granted]
- Option B satisfied: [no — pending grant / yes — granted on date]

---
*Patent tracker updated: `context/research-tracker.md`*
```
