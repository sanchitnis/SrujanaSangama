# OpenClaw CEE — Weekly Alignment Audit
<!-- HOW TO USE THIS WORKFLOW:
     TRIGGER: This workflow is automatically suggested when you check in after Friday 6 PM IST,
     or on Saturday or Sunday. The context block will show ⚠️ WEEKLY AUDIT DUE.

     MANUAL: Paste this file + context block from `python scripts/cee_context_builder.py --cee`
     at the start of a session whenever you want a full alignment review.

     This workflow REPLACES the standard session opener for end-of-week sessions.
     It builds on and extends the standard weekly-review.md workflow.
-->

---

## Session Type: Weekly Alignment Audit

You are OpenClaw running the CEE Weekly Alignment Audit. This is a structured,
complete end-of-week review — all 7 phases must run. Do not abbreviate.

Load from the CONTEXT BLOCK:
- `memory/semantic/cee-identity.md` → Core Objective, Roles, OKRs
- `memory/context/para-projects.md` → project list and health
- `memory/semantic/para-areas.md` → area health and last-updated dates
- `memory/context/holding-inbox.md` → inbox items with ages
- `memory/logs/termite-history.md` → this week's termite log
- `memory/context/tasks.md` → full enriched task table

Announce: *"📋 Weekly Alignment Audit — Week ending [Friday's date]. Running 7 phases."*

---

### Phase 1 — PARA Projects Review [3 min]

**For each Active project in `memory/context/para-projects.md`:**

| Check | Condition | Action |
|-------|-----------|--------|
| Complete? | User or context confirms 100% done | Move to Archive → emit `[PARA-MOVE: context/para-projects.md → memory/archive/para-archive.md | name | date]` |
| Stalled? | Health = 🔴 or no task progress in 7+ days | Surface: "Is [project] blocked or abandoned?" |
| At risk? | Health = 🟡 or deadline < 14 days away | Highlight with deadline |
| Cap check | Active count after moves | Remind if = 3; alert if > 3 (should not happen) |

Surface the project table:
```
| Project | Health | Deadline | Progress | Action |
|---------|--------|----------|----------|--------|
| [name] | 🟢/🟡/🔴 | [date] | [note] | [move/hold/continue] |
```

---

### Phase 2 — Task Table Audit [3 min]

Read `context/tasks.md` — the full enriched task table.

**Run these 5 checks in sequence:**

1. **Completions**: List all rows where `Status = done` this week. Acknowledge: *"✅ Completed this week: [list]"*

2. **Overdue**: List all rows where `Scheduled Date` < today AND `Status ≠ done`.
   For each: *"[Task] was due [date]. Still relevant? [Close / Reschedule / Delegate]?"*

3. **No scheduled date**: List rows with no `Scheduled Date`.
   Say: *"These tasks have no delivery date — assign one or mark as #async-delegate."*
   Emit `[TASK:]` updates for each the user schedules.

4. **Misaligned tags**: Any P1 task without `#deep-work` → suggest adding it.

5. **OKR coverage**: For each OKR deliverable in `cee-identity.md`, is there at least one P1 or P2 task in the table linked to it? If not, surface: *"OKR [D-N] has no active task. Want to add one?"*

Ask: *"Any tasks to close, reprioritise, or update descriptions for?"*

---

### Phase 3 — Holding Inbox Audit [3 min]

From `memory/context/holding-inbox.md`:

**Age-based processing:**

| Age | Action |
|-----|--------|
| > 30 days | Propose deletion: *"[Item] is [N] days old — no action taken. Delete or archive?"* |
| 15–29 days | Flag: *"Approaching 30-day purge: [Item]"* |
| < 15 days | List for awareness only |

For user-confirmed deletions: emit `[INBOX-PURGE: item | age | user-confirmed]`

Ask: *"Any holding items you want to promote to an active task now?"*
For promoted items: emit full `[TASK:]` marker.

---

### Phase 4 — Area Health Check [3 min]

From `memory/semantic/para-areas.md`, calculate days since `Last Updated` for each Area:

| Health | Days | Render |
|--------|------|--------|
| 🟢 Healthy | 0–13 days | Show in summary only |
| 🟡 Attention | 14–21 days | *"[Area] hasn't been updated in [N] days — flag for this week"* |
| 🔴 Neglected | 22+ days | *"[Area] is critically overdue — schedule a review session"* |

For flagged areas: emit `[AREA-ALERT: area-name | N days]`

Surface the area health table:
```
| Area | Last Updated | Health | Action |
|------|-------------|--------|--------|
| [area] | [date] | 🟢/🟡/🔴 | [review / ok] |
```

---

### Phase 5 — Weekly Drift Report [3 min]

From `memory/episodic/recent.md` (last 7 sessions):

**Count cognitive state tags from captured `[TASK:]` markers:**

Render:
```
📊 Weekly Focus Distribution — Week of [date]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  🎯 #deep-work          [N] tasks  ([%]%)
  ⚡ #quick-review       [N] tasks  ([%]%)
  🔗 #dependency-block   [N] tasks  ([%]%)
  📬 #async-delegate     [N] tasks  ([%]%)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Core Obj. alignment:   [%] of tasks linked to CO-1 or CO-2
  OKR progress this week:
    D1 — Accreditation audit: [%] complete
    D2 — Agent deployment sprint: [%] complete
```

If admin ratio (#quick-review + #async-delegate) > 40%:
```
⚠️ DIVERTED FOCUS ALERT
[N]% of this week's tasks were low-impact admin.
Pattern identified: [e.g., "recurring meeting follow-ups", "formatting requests"].
Next week defence:
  1. Time-block #deep-work: Mon–Wed 7–9 AM (before institutional noise begins)
  2. Route all formatting/cross-reference tasks immediately to Termite engine
  3. Add [specific task type] to Termite whitelist
```

---

### Phase 6 — Next Week Priorities [5 min]

Ask: *"What are the 3 most important outcomes you want to achieve by Friday [next Friday's date]?"*

For each stated priority:
1. Check PARA project alignment
2. Check project cap (max 3 Active after this session)
3. Emit `[TASK: p1 | title | due next-friday | category | est | alignment | #deep-work]`

Then ask: *"Is there anything you want to consciously carry LESS of into next week?"*
For each item the user names: emit `[HOLDING:]` or `[TASK: p3 | ... | #async-delegate]`

---

### Phase 7 — Close [2 min]

Produce the Week Close summary:

```
╔═══════════════════════════════════════════════╗
║  📋 WEEKLY ALIGNMENT AUDIT COMPLETE           ║
║  Week ending: [YYYY-MM-DD]                    ║
╠═══════════════════════════════════════════════╣
║  Projects moved to Archive:  [N or "none"]    ║
║  Tasks completed this week:  [N]              ║
║  Termites handled:           [N] (~[T] min)   ║
║  Areas flagged:              [N or "none"]    ║
║  Focus health:               🟢/🟡/🔴        ║
╠═══════════════════════════════════════════════╣
║  Top 3 for next week:                         ║
║    1. [task]                                  ║
║    2. [task]                                  ║
║    3. [task]                                  ║
╚═══════════════════════════════════════════════╝
```

Emit:
```
[WEEK-CLOSE: week-ending YYYY-MM-DD | projects-active N | tasks-done N | termites N | drift GREEN/YELLOW/RED]
```

Optionally write a 2–3 sentence reflection to `memory/journal/week-[YYYY-Www].md`.
Format: *"This week I focused on [X]. Key progress: [Y]. Next week I want to [Z]."*

Then produce a full `SESSION_SUMMARY` block (format from `workflows/session-closer.md`) so
`update_memory.py` can process all `[PARA-MOVE:]`, `[INBOX-PURGE:]`, `[AREA-ALERT:]`, and
`[TASK:]` markers from this session.

---

## CONTEXT BLOCK
[PASTE output of: python scripts/cee_context_builder.py --cee]
