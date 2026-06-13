# OpenClaw — Session Closer
<!-- Paste this at the END of your Claude session to generate the SESSION_SUMMARY block -->
<!-- The update_memory.py script will parse this output and update your memory files -->

---

Please produce a **SESSION_SUMMARY** block for this conversation. This block will be parsed by a script to update my memory files. Follow the format exactly — field names and delimiters must match precisely.

```
===SESSION_SUMMARY_START===

DATE: [today's date in YYYY-MM-DD]

ACCOMPLISHED:
- [one-line description of each thing completed or produced]
- [...]

MEMORY_UPDATES:
- [fact | tier: soul/semantic/procedural/episodic | file: filename.md]
- [fact | tier: semantic | file: work.md]
- [...]

TASKS_CAPTURED:
- [priority: p1/p2/p3 | text: task description | due: YYYY-MM-DD or none]
- [...]

TASKS_COMPLETED:
- [task text that was completed this session]
- [...]

HABITS_LOGGED:
- [habit name | status: done/missed | date: YYYY-MM-DD]
- [...]

DEPRECATED_FACTS:
- [old fact that is no longer true]
- [...]

SKILL_GAPS:
- [skill name | description of what it would do]
- [...]

AGENTS_USED:
- [list of agent names used this session]

OPEN_THREADS:
- [anything left unfinished that should be picked up next session]
- [...]

EPISODIC_ENTRY:
[Write a 3–5 sentence narrative summary of this session for the episodic memory log.
Include: what was worked on, key decisions made, what was learned, mood/energy if apparent.]

===SESSION_SUMMARY_END===
```

Produce nothing outside the delimiters. Fill every field. Use `[none]` for empty fields rather than leaving them blank.
