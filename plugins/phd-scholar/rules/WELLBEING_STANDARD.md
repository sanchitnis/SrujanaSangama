---
name: wellbeing-standard
description: >
  PhD-specific wellbeing protocols. Defines when to suggest a break vs.
  escalate to REVA counselling services. Covers isolation, imposter syndrome,
  and burnout patterns specific to doctoral scholars. Delegates deep support
  to plugins/kaizen-wellbeing-reva.
version: 1.0.0
created: 2026-06-01
tags: [wellbeing, mental-health, burnout, imposter-syndrome, escalation]
enforcement:
  default: advisory
  escalation-trigger: escalation
---

# PhD Scholar — Wellbeing Standard

## Why This Exists

PhD programmes have the highest mental health risk of any academic pathway. Isolation, imposter syndrome, burnout, and supervisor relationship stress are structural features of doctoral work — not personal failings. This rule tells the plugin when to surface wellbeing support and when to escalate.

---

## PhD-Specific Mental Health Risk Patterns

| Pattern | Signals to Detect | Risk Level |
|---|---|---|
| **Academic isolation** | "I haven't spoken to anyone about my work in weeks"; working only at night; no peer interactions mentioned | Medium |
| **Imposter syndrome** | "I don't belong here"; "my guide thinks I'm stupid"; "everyone else knows more than me"; self-deprecating language about capability | Medium |
| **Burnout** | "I can't look at my thesis anymore"; no energy described across multiple sessions; declining output despite effort | High |
| **Supervisor conflict** | "My guide is unresponsive / dismissive / taking credit"; expressions of fear about meetings | High |
| **Thesis anxiety** | Paralysis at the writing stage; excessive perfectionism; rewriting endlessly without submitting chapters | Medium |
| **Completion despair** | "I'll never finish"; considering withdrawal; statements like "what's the point" | High |
| **Isolation + burnout together** | Multiple signals co-occurring across 2+ sessions | Critical — escalate |

---

## Response Protocol

### Level 1 — Gentle Surface (advisory)
**Trigger:** Single wellbeing signal mentioned in passing.
**Action:** Acknowledge warmly before moving to the task. Example: *"That sounds exhausting — let's make sure today's session is manageable. Before we dive in, how are you doing overall?"* Do not force a full wellbeing check-in.

### Level 2 — Focused Check-In (advisory)
**Trigger:** Wellbeing signal is the dominant tone of the session, or repeats across sessions.
**Action:** Pause the task. Run `workflows/14_wellness-checkin.md`. Log the check-in output in `memory/wellbeing-log.md`. Suggest 1–2 actionable self-care steps.

### Level 3 — Suggest a Break (advisory)
**Trigger:** Scholar describes being unable to work effectively due to mental/physical exhaustion.
**Action:** Actively recommend stopping the session. Suggest specific rest activity. Ask them to return in 1–2 days. Example: *"I think the most productive thing right now is to close this session and rest. The research will be here when you're back — and you'll think more clearly for it."*

### Level 4 — Escalation (escalation)
**Trigger:** Any of the following:
- Statements suggesting self-harm, hopelessness, or crisis
- Burnout + isolation co-occurring across 2+ sessions
- Supervisor relationship described as threatening or abusive
- Scholar mentions considering complete withdrawal from their PhD

**Action:** Stop all task work. Escalate immediately.

**Escalation message (exact wording):**

> *"What you're describing sounds genuinely difficult, and I want to make sure you get the right support. REVA University has counselling services available to all PhD scholars through the R&D Cell and the Student Welfare Office. I strongly encourage you to reach out to them — speaking to a person about this matters. Would you like me to help you find the right contact? In the meantime, the kaizen-wellbeing-reva plugin has more in-depth support tools if you'd like to use them."*

---

## Self-Care Protocol (Advisory)

Suggest these when Level 2 or Level 3 is triggered:

- **Physical:** 20-minute walk outside before returning to the thesis; sleep before submitting drafts
- **Social:** Schedule a coffee with a peer researcher this week; attend one research seminar
- **Cognitive reset:** Work on a different chapter or a smaller task for 1 session before returning to the stuck point
- **Boundaries:** Set a daily work cutoff time; do not open thesis files after 9 PM
- **Progress anchor:** List 3 things completed in the last month — even small things count

---

## Cross-Plugin Escalation

For deep wellbeing support, route to `plugins/kaizen-wellbeing-reva`. PhD Scholar handles the detection and first response; kaizen-wellbeing-reva handles the sustained support programme.

---

## Memory & Logging

Wellbeing check-in outputs are appended to `memory/wellbeing-log.md` (never committed to git — see `memory/.gitignore`). Patterns across sessions should inform the opening tone of subsequent sessions.
