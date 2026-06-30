<!-- Paste this workflow into a PhD Scholar session to identify a relevant funding scheme, prepare a grant application, or plan a conference travel grant. -->

# Session Type: Grant Proposal & Funding Strategy

**Purpose:** Help the scholar identify the right funding scheme from the India landscape, assess grant readiness, and prepare or review a grant proposal.

**Estimated total time:** 45–60 minutes

**Reference files:** `references/india-funding-landscape.md` (v2.0), `plugins/research-reva/workflows/funding-hunt.md` (attribution §10)

Attribution: Adapted from `plugins/research-reva/` (CONSTITUTION §10).

---

## Phase 1 — Grant Readiness Assessment (10 min)

Activate `grant-agent.md` → grant readiness check.

Ask the 4 readiness questions:
1. Societal / industrial / national security application? (2–3 sentences)
2. Guide's active grant or relationship with funding bodies?
3. Preliminary results available?
4. Specific funding need identified?

Score: 3–4 yes → proceed to Phase 2
Score: 1–2 yes → surface readiness gaps first; recommend what to do before applying

---

## Phase 2 — Funding Scheme Identification (10 min)

Read `references/india-funding-landscape.md` sections:
- Section 1 — National Government Agencies
- Section 2 — Corporate & Foundation Fellowships
- Section 3 — International & Bilateral Fellowships
- Section 4 — Domain-Specific Portals

Match the scholar's research domain and career stage to the most relevant schemes.

Present a shortlist of 2–3 schemes:
```
| Scheme | Body | Amount | Domain Match | REVA Eligibility | Deadline |
|---|---|---|---|---|---|
| [scheme] | [body] | [range] | [high/medium] | [yes/caveat] | [date] |
```

---

## Phase 3 — Proposal Drafting (30 min)

For the selected scheme, work through the 8-section proposal structure (from `grant-agent.md`):

1. Title and abstract (150 words — contribution + societal impact)
2. Background and motivation (from lit review)
3. Research objectives and expected outcomes
4. Methodology
5. Work plan / Gantt chart (month-by-month)
6. Budget table (itemised — no lump sums)
7. PI/Co-PI credentials and publications
8. Institutional support statement

**Budget table assistance:**
Build the itemised budget using the template from `grant-agent.md`. Remind: contingency maximum is 10%.

**REVA compliance checklist reminder:**
- DSIR-SIRO recognition required for equipment exemptions (ANRF/DST)
- NITI Aayog Darpan Portal ID required for civic-focused grants
- Registrar/Director of Research endorsement letter required

---

## Phase 4 — Conference Travel Grant (for paper presentations) (10 min)

If the scholar has an accepted paper and needs travel funding:

Requirements:
- Acceptance letter from Scopus-indexed conference (mandatory)
- Apply before travel; original receipts needed for reimbursement

Sources (from `references/india-funding-landscape.md`):
- IEEE India / ACM India / CSI chapters — typically ₹25,000–₹50,000
- DST SERB travel support — up to ₹1,00,000 for international
- IEI — engineering-focused conferences

Help the scholar prepare the travel grant application:
- Cover letter with conference details and paper title
- Acceptance letter attachment
- Cost estimate table (registration + travel + accommodation)

---

## Phase 5 — Grant Tracker Update (3 min)

Update `context/research-tracker.md` → grant tracker:

```
## Grant Tracker
| Scheme | Submission Date | Status | Amount Applied | Decision Date |
|---|---|---|---|---|
| [scheme] | [date] | submitted/under-review/approved/rejected | ₹N | [date] |
```

---

## Output Template

```
## Grant Proposal Session — [Name] — [Date]

**Grant readiness score:** [N/4]
**Scheme selected:** [scheme name] — [body]
**Amount:** [range]

**Proposal sections completed this session:**
- [list completed sections]

**Gaps remaining:**
- [list sections still needed]

**REVA compliance items:**
- DSIR-SIRO: [confirmed / pending]
- Darpan ID: [confirmed / pending]
- Endorsement letter: [confirmed / pending]

**Conference travel grant:** [applicable / not applicable]
**Travel grant application:** [drafted / not started]

**Next action:**
1. [specific task]
2. [specific task]

---
*Grant tracker updated: `context/research-tracker.md`*
```
