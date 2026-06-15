<!-- Paste this workflow at the end of any PhD Scholar session to capture what was done, update memory, and set the next actions. -->

# Session Type: Session Closer — Memory Capture & Next Actions

**Purpose:** Capture the session's work, update all relevant memory and context files, and set the scholar's next 1–3 specific tasks before closing.

**Estimated total time:** 5–10 minutes

---

## Phase 1 — Session Summary (2 min)

Ask: *"Before we close — shall I capture what we did today and update your task list?"*

If yes: proceed to Phase 2.
If no: offer a 2–3 sentence verbal summary and close.

---

## Phase 2 — Work Capture (3 min)

Ask the scholar to confirm:
1. *"What was the main thing we worked on today?"*
2. *"Did you complete what you planned? Or is something still in progress?"*
3. *"Did any new information come up that should be saved — a paper, a decision, a date?"*

---

## Phase 3 — Memory Update (3–5 min)

Based on the session content, update the relevant files:

| If session was about... | Update file |
|---|---|
| Coursework / credits | `context/scholar-profile.md` → `credits_completed` |
| Research progress | `context/research-tracker.md` → milestone log + experiment log |
| Publications | `memory/semantic/publication-log.md` + `context/publication-pipeline.md` |
| Thesis chapters | `context/research-tracker.md` → `thesis_chapters_complete` |
| Patent | `context/research-tracker.md` → patent tracker |
| Grant | `context/research-tracker.md` → grant tracker |
| Wellbeing | `memory/wellbeing-log.md` (with scholar consent) |
| Ikigai | `memory/ikigai.md` |
| General tasks | `memory/tasks.md` |
| Biannual review | `memory/semantic/progress-reports.md` |

For each update: offer to write the specific entry rather than asking the scholar to do it manually.

After updating memory files:
- Rebuild the local HTML dashboards: Execute the builder scripts `python tools/build_scholar_dashboard.py` and `python tools/build_faculty_dashboard.py` to refresh the profile completeness, KPIs, and collaborative status on the local HTML portals.

---

## Phase 4 — Episodic Memory Append (1 min)

Append a brief episodic record to `memory/semantic/episodic/`:

```
## Session — [YYYY-MM-DD]
Focus: [main topic]
Work done: [2–3 bullet points]
Decisions made: [any important decision]
Next session: [agreed next focus]
```

---

## Phase 5 — Next Actions (2 min)

Set 1–3 specific, achievable next actions:

```
## Next Actions — [Date]
1. [specific task] — est. [N hours] — by [date]
2. [specific task] — est. [N hours] — by [date]
3. [specific task if any] — est. [N hours] — by [date]
```

These are written to `memory/tasks.md` → active task list.

---

## Phase 6 — Closing (1 min)

Close warmly and with purpose:

*"Great session today. Your next step is: [task 1]. See you [next session / whenever you're ready]."*

If the scholar showed any stress signals during the session: add a gentle wellbeing note — *"Take care of yourself between sessions. The research will be there when you're ready."*

---

## Output Template

```
## Session Closed — [Name] — [Date]

**Session focus:** [main topic]
**Work completed:** [bullet list]
**In progress (carrying over):** [list or "none"]

**Files updated:**
- [file name] — [what was updated]
- [file name] — [what was updated]

**Next actions:**
1. [task] — [N hrs] — by [date]
2. [task] — [N hrs] — by [date]

**Next milestone:** [milestone + N days remaining]
**Wellbeing note:** [none / gentle note if needed]
```
