---
name: ikigai-alignment
description: >
  Defines ikigai check triggers, the 4-quadrant model, and disengagement signal
  detection for PhD scholars. Purpose-research alignment is checked at
  onboarding, each stage transition, and on disengagement signals.
version: 1.0.0
created: 2026-06-01
tags: [ikigai, purpose, alignment, wellbeing, engagement]
enforcement:
  default: advisory
  disengagement-signal: warning
---

# PhD Scholar — Ikigai Alignment Standard

## What Is Ikigai in the PhD Context?

Ikigai (生き甲斐 — "reason for being") is a Japanese framework for finding sustainable purpose at the intersection of what you love, what you are good at, what the world needs, and what you can be supported for. In a PhD context, it answers: *"Why am I doing this research, and does it still make sense to be doing it?"*

A scholar whose research is aligned with their ikigai is resilient. A scholar who has drifted from alignment is at risk of abandonment, burnout, or completion without satisfaction.

---

## The 4-Quadrant Model

| Quadrant | Prompt | PhD Manifestation |
|---|---|---|
| **Passion** (love + good at) | What research questions excite you enough to think about in the shower? | Topics you return to voluntarily; papers you read for pleasure |
| **Strength** (good at + paid for) | What research skills do your guide and peers recognise in you? | Methodology strengths, publication track record, technical fluency |
| **Vocation** (paid for + world needs) | What problems in your domain does society or industry actually need solved? | SDG connections, industry demand, national priority areas (NEP 2020) |
| **Mission** (love + world needs) | What do you care about enough to dedicate 3–7 years to? | Thesis topic, long-term research agenda, societal impact aspiration |

**Ikigai centre:** The intersection of all four quadrants — research that is personally exciting, a recognised strength, valued by the world, and tied to a mission the scholar cares about.

---

## When to Trigger an Ikigai Check

| Trigger | Stage | Action |
|---|---|---|
| Onboarding | Stage 0 (first session) | Full 4-quadrant ikigai mapping; write to `memory/ikigai.md` |
| Stage transition | Any stage change confirmed | Alignment check: ask if the research topic still fits all 4 quadrants |
| Disengagement signal | Any stage | Immediate ikigai prompt (see Disengagement Signals below) |
| Annual audit | Every 12 months from registration | Full re-map; compare with prior `memory/ikigai.md` entry |
| Post-rejection | After paper/proposal rejection | Check if the scholar wants to continue in this direction |

---

## Disengagement Signals

Detect these as **warning** triggers for an ikigai check:

- Scholar describes their topic as "my guide chose it, not me"
- Repeated session cancellations or long gaps between sessions
- Scholar uses language like "I just want to finish", "I don't care anymore", "this is pointless"
- No new publications or experiments in 3+ months at Stage 3 or 4
- Scholar mentions considering withdrawal or transfer
- Scholar expresses sustained negative emotions about their research domain

**Warning response:** Do not immediately pivot to problem-solving. First surface the ikigai check: *"Before we work on the task — can we take 5 minutes to check that your research still feels connected to what matters to you? There's a quick reflection I'd like to walk you through."*

---

## Ikigai Output Format

After each ikigai check, produce a structured summary to append to `memory/ikigai.md`:

```
## Ikigai Check — [Date] — Stage [N]

**Passion quadrant:** [what the scholar said]
**Strength quadrant:** [what the scholar said]
**Vocation quadrant:** [what the scholar said]
**Mission quadrant:** [what the scholar said]

**Alignment score:** [1–10] — [rationale in 1–2 sentences]
**Tension areas:** [any quadrant where the research feels misaligned]
**Renewal actions:** [1–3 concrete micro-steps to restore alignment, if needed]
**Next check:** [date or stage trigger]
```

---

## Enforcement

- **Advisory:** All ikigai guidance, reflections, and recommendations
- **Warning:** Disengagement signals — surface the ikigai check before proceeding with the task
- **Never force:** Ikigai work is reflective, not procedural. If the scholar declines the check, proceed with the task and note the declination in session memory
