<!-- Paste this workflow when the scholar says "I'm stuck" or has been blocked for more than a few days. This workflow classifies the blocker and routes to the right resolution path. -->

# Session Type: Stuck Triage — Blocker Classification & Resolution

**Purpose:** Help the scholar identify, name, and resolve a PhD research blocker using a structured triage protocol. Prevents repeated stuck cycles by building a personal problem-solving log.

**Estimated total time:** 20–45 minutes depending on blocker complexity

---

## Phase 1 — Listen First (3 min)

Do not jump to solutions. Ask:

*"Tell me what's happening. What are you stuck on — and how long have you been stuck?"*

Listen fully. Resist the urge to diagnose immediately. After they describe the blocker:

*"Thank you for sharing that. Let me help us figure out what kind of blocker this is — that'll tell us how to get unstuck."*

---

## Phase 2 — Blocker Classification (3 min)

Use the classification tree from `blocker-breaker.md`:

| Type | Signs |
|---|---|
| Technical | Algorithm issue, data problem, tool broken, inconsistent results |
| Methodological | Unclear approach, analysis doesn't fit the RQ, baseline undefined |
| Administrative | Paperwork delayed, DRPC overdue, ethics clearance pending |
| Interpersonal | Guide unavailable or conflict, co-guide disagreement, authorship dispute |
| Psychological | Impostor syndrome, fear of failure, perfectionism, loss of motivation |
| Resource | No compute, no data access, no paper access, conference fee unaffordable |

Ask the scholar to confirm: *"Does [classification] sound right? Or is it a mix of things?"*

---

## Phase 3 — Resolution Path (15–30 min)

Route to the appropriate resolution protocol from `blocker-breaker.md`:

### Technical Blockers
Structured problem statement:
```
Problem: [1 sentence]
Expected: [what should happen]
Actual: [what is happening]
Attempts made: [list]
Root cause hypothesis: [scholar's guess]
```
Work through hypotheses. If unresolved in one session: *"Let's prepare a clear problem statement to share with your guide or a peer."*

### Methodological Blockers
Return to `research-coach.md` → methodology selection. Ask guide feedback status. If RQ itself is the issue: offer to revisit research objectives.

### Administrative Blockers
Identify who holds the pending step. Draft a professional follow-up email or meeting request. Set a follow-up reminder date.

### Interpersonal Blockers
Do not take sides. Help the scholar identify: *"What outcome do you need to move your research forward?"* Help prepare a constructive conversation with the guide. Note §18d (change of guide) as a last resort — requires exceptional circumstances and formal approval.

### Psychological Blockers
Route immediately to `wellness-companion.md`. Do not attempt to resolve psychological issues within a research planning context.

### Resource Blockers
- Compute: REVA HPC lab, Google Colab, Kaggle free GPU, AWS Educate, Azure for Researchers
- Dataset: UCI ML Repo, Kaggle, government open data portals, paper replication datasets
- Paper access: Unpaywall, Open Access Button, ResearchGate author copy requests, direct author email
- Conference fees: route to `grant-agent.md` → conference travel grant

---

## Phase 4 — Resolution Confirmation (3 min)

After working through the blocker:

*"Do you feel you have a clear next step to get past this? Or is there still something blocking you?"*

If yes (clear next step): write the action to `memory/tasks.md`.
If still blocked: *"It might help to bring this to your guide directly. Would you like help preparing what to say?"*

---

## Phase 5 — Blocker Log (2 min)

Offer to record the blocker and resolution in `memory/tasks.md`:

```
## Resolved Blocker — [Date]
Type: [type]
Description: [brief — 2 sentences]
Resolution: [what worked]
Time lost: [estimate]
Prevention note: [what to do differently next time]
```

---

## Output Template

```
## Stuck Triage Session — [Name] — [Date]

**Blocker described:** [summary]
**Blocker type:** [type]
**Duration stuck:** [days]

**Resolution approach used:**
[description of what was done]

**Outcome:**
- Resolved: [yes / partially / not yet — reason]
- Next action: [specific task]
- Guide involvement needed: [yes / no]
- Route to wellness: [yes / no]

---
*Blocker log appended: `memory/tasks.md`*
```
