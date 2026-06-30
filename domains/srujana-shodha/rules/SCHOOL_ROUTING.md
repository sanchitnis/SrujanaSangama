---
name: school-routing
description: >
  Detects the scholar's school/department and routes to the correct materials.
  CSE/CSA scholars get full support. All other schools receive a graceful
  placeholder message until their materials are prepared. Hard stop prevents
  CSE content from being served to non-CSE scholars.
version: 1.0.0
created: 2026-06-01
tags: [routing, school, cse, placeholder]
enforcement:
  cse-routing: advisory
  non-cse-content-leak: hard stop
---

# PhD Scholar — School Routing

## Purpose

This rule governs how the plugin routes scholars based on their school/department. Routing happens at onboarding and is stored in `context/scholar-profile.md`. The current stage is confirmed at each session open.

---

## Supported Schools

| School | Status | Materials |
|---|---|---|
| Computer Science & Applications (CSE / CSA) | ✅ Fully supported | `references/schools/cse/` |
| Electronics & Communication Engineering (ECE) | ⏳ Placeholder | `references/schools/ece/researcher-handbook.md.placeholder` |
| Management Studies | ⏳ Placeholder | `references/schools/management/researcher-handbook.md.placeholder` |
| Life Sciences | ⏳ Placeholder | *(to be added)* |
| All other schools | ⏳ Placeholder | Generic placeholder response |

---

## Detection Logic

1. At onboarding, ask: *"What is your school / department at REVA University?"*
2. Match the response against CSE/CSA keywords: `computer science`, `CSE`, `CSA`, `computer applications`, `MCA`, `M.Tech CSE`, `information technology`, `IT`, `artificial intelligence`, `data science`, `cybersecurity`.
3. Store the detected school in `context/scholar-profile.md` under the `school` field.
4. On every subsequent session, read `school` from `context/scholar-profile.md` and apply the routing rule below.

---

## Routing Rules

### Rule R-1: CSE/CSA Scholar — Full Support (advisory)
**Trigger:** School field matches CSE/CSA keywords.
**Action:** Load full CSE materials — `references/schools/cse/`, `references/reva-phd-regulations-digest.md`, `references/india-funding-landscape.md`, etc.
**Enforcement:** `advisory`

### Rule R-2: Non-CSE Scholar — Graceful Placeholder (hard stop)
**Trigger:** School field does NOT match CSE/CSA keywords.
**Action:** Display the placeholder message below. Do NOT load or reference any CSE-specific content (publication venues, CSE handbook, CSE methodology guide). Do NOT attempt to adapt CSE content to another domain.
**Enforcement:** `hard stop` — zero CSE content must reach a non-CSE scholar.

**Placeholder message (exact wording per CONSTITUTION §11):**

---

> *Support for your school is being prepared. The PhD Scholar plugin currently provides full guidance for the School of Computer Science and Applications (CSE/CSA). Materials for your school will be added in a future release. In the meantime, please contact REVA's Research and Development Cell for school-specific PhD guidance. General workflows (daily planning, wellbeing check-ins, ikigai audits, blocker triage) are available to you now.*

---

### Rule R-3: Ambiguous School — Clarify Before Routing (advisory)
**Trigger:** School field is blank or cannot be matched.
**Action:** Ask the scholar to clarify their school before loading any school-specific materials. Do not default to CSE.
**Enforcement:** `advisory`

---

## General Workflows Available to All Schools

The following workflows do not depend on school-specific materials and are available to all scholars regardless of school:

- `workflows/12_daily-standup.md`
- `workflows/13_stuck-triage.md`
- `workflows/14_wellness-checkin.md`
- `workflows/15_ikigai-audit.md`
- `workflows/00_onboarding.md` (profile setup only — no CSE content loaded for non-CSE)
