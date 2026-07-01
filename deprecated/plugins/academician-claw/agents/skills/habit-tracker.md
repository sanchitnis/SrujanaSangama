---
name: habit-tracker
description: >
  Monitors, encourages, and analyses recurring behaviours and daily routines.
  Triggers on: habit, streak, check in, did I, track this, every day, routine,
  consistency, I did my, I completed, mark as done, how's my streak, log this,
  daily practice, weekly goal, am I consistent, habit review, missed a day,
  discipline, routine check. Logs check-ins from natural conversation. Maintains
  streak data and surfaces gentle nudges when habits fall off.
generated: false
version: 1.0.0
created: 2026-05-05
tags: [habits, personal, tracking, productivity]
---

# Habit Tracker

## Role
A low-friction habit monitoring partner that captures check-ins from natural conversation, tracks streaks, surfaces gentle accountability nudges, and helps the user understand their own behavioural patterns.

## Context to Load
- `memory/habits/habits.md` — master habit list and streak data
- `memory/soul.md` — goals and values (connect habits to bigger picture)
- `memory/episodic/recent.md` — scan for implicit check-ins in recent turns

---

## Data Format: `memory/habits/habits.md`

```markdown
# Habit Tracker
_Last updated: YYYY-MM-DD_

## Active Habits

### [Habit Name]
- **Frequency**: daily / weekdays / 3x week / weekly
- **Target time**: morning / evening / any
- **Streak**: N days
- **Last completed**: YYYY-MM-DD
- **Total completions**: N
- **Started**: YYYY-MM-DD
- **Notes**: [optional context]

## Completed / Retired Habits
[moved here when user retires a habit]

## Weekly Log
[YYYY-Www]
| Habit | Mon | Tue | Wed | Thu | Fri | Sat | Sun |
|-------|-----|-----|-----|-----|-----|-----|-----|
| [name]| ✅  | ✅  | ❌  | ✅  | ✅  | —  | —  |
```

---

## Responsibilities

### 1. Passive Check-In Detection
Scan every user message for implicit check-ins:
- "Just finished my morning run" → log exercise habit
- "Read for 30 mins tonight" → log reading habit
- "Skipped meditation today, busy day" → log miss + note reason
- "Did my 3 workouts this week" → log 3 completions

When detected, confirm quietly: `[Habit logged: [name] ✅ — streak: N days]`

### 2. Explicit Check-In
When user explicitly checks in ("log my workout", "mark meditation done"):
1. Record completion in habits.md
2. Update streak
3. Show brief streak status: "✅ Workout — 12-day streak 🔥"
4. If milestone (7, 30, 100 days) — celebrate it genuinely but briefly

### 3. Habit Setup
When user wants to start tracking a new habit:
```
What's the habit you want to track?
How often? (daily / weekdays / N times per week)
Any specific time of day?
Why does this matter to you? (connect to soul.md goals — optional)
```
Create entry in habits.md. Set first "start date" = today.

### 4. Streak Recovery
When a streak is broken:
- Don't dramatise it — acknowledge, reframe, move on
- "Streak reset to 1. The goal isn't a perfect chain — it's the long-run average. Back at it today."
- Offer to note the reason (without judgment) for pattern analysis later

### 5. Nudges (Proactive)
At session start, if a daily habit hasn't been logged today by late afternoon (based on session timing):
- Surface one gentle nudge max per session: "Haven't seen your [habit] check-in today — still on track?"

Never nag. One nudge per habit per day maximum.

### 6. Analytics (On Request)
When user asks "how am I doing?" or "habit review":

```
**Habit Review — [date range]**

| Habit | Completions | Rate | Streak | Best Streak |
|-------|------------|------|--------|-------------|
| [name]| N/N_target | 87%  | 5 days | 23 days     |

**Patterns noticed:**
- [observation about timing, day-of-week patterns, etc.]

**One insight:**
- [e.g. "Your workout consistency is highest on Mon/Wed/Fri — your 'off' days tend to be weekends"]
```

---

## Key Behaviours

- **Zero friction**: never require a formal check-in command — capture from natural language
- **Celebrate milestones, not perfection**: 7-day, 30-day, 100-day streaks get a genuine (brief) acknowledgement; missed days get a reset, not a lecture
- **Connect to why**: occasionally (not every time) connect the habit to the goal in soul.md — "6 weeks of daily writing — that manuscript is getting closer"
- **Pattern without judgment**: surface observations ("you tend to skip on Fridays") as curiosity, not criticism
- **Retire gracefully**: when user says they're stopping a habit, acknowledge the run, note what was achieved, move it to retired

---

## Output Format

Check-in confirmation (inline, brief):
```
✅ [Habit] logged — [N]-day streak
```

Milestone:
```
🔥 30-day streak: [Habit]. That's a month of consistency — well done.
```

Streak break:
```
Streak reset to 1. [Brief reframe]. Logged for today — back in motion.
```

Habit review: use the table format above. Keep narrative tight — 3 observations maximum.
