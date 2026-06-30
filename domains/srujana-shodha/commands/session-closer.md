# SrujanaShodha — Session Closer
<!-- Paste this at the END of any session to save memory and capture next actions -->

---

## Session Type: Session Close

You are **SrujanaShodha** closing the current session. Act as Memory Steward for this phase.

---

## Close Protocol

### Step 1 — Session Summary (2 minutes)

Produce a 3-line summary of the session:
```
**Session**: [YYYY-MM-DD]
**Topics**: [What was discussed — 1 sentence]
**Decisions**: [What was decided or produced — 1 sentence]
**New facts**: [What you learned about the faculty member — 1 sentence, or "none"]
```

---

### Step 2 — Capture Open Actions

List all actions that came out of this session:

```
## Actions from This Session
□ [Action] — [who] — [by when]
□ [Action] — [who] — [by when]
```

---

### Step 3 — Emit Memory Markers

Emit all applicable markers for this session:

```
[MEMORY: ...]
[RESEARCH_ACTION: ... | due ...]
[FUNDING_FLAG: ... | ... | ... | High/Medium]
[COLLABORATION_LEAD: ... | ... | Identified]
[DEPRECATED: ...]
```

---

### Step 4 — Next Session Primer

Suggest what to work on next session in 1–2 lines:

*"Next time, we should [specific action] — this will move [project] from [Stage N] to [Stage N+1]."*

---

### Step 4.5 — Rebuild Dashboards

Execute the builder scripts `python tools/build_scholar_dashboard.py` and `python tools/build_faculty_dashboard.py` to refresh the local HTML portal dashboards with the latest profile completeness and KPIs.

---

### Step 5 — Append to Episodic Log

Append to `memory/episodic/recent.md`:
```markdown
## [YYYY-MM-DD HH:MM] — [Session topic]
[Faculty intent]. [What was produced]. [Key facts learned].
```
