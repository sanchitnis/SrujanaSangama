---
name: skill-generator
description: >
  Extends the OpenClaw agent ecosystem by writing new SKILL.md files on demand.
  Triggered by the Orchestrator when routing confidence is below 0.5 AND the user
  intent is clear enough to define a specialist. Also triggered by explicit user
  requests: "create an agent for X", "add a skill to handle Y", "build me a
  specialist that does Z". Generated skills are saved, registered, and immediately
  available for routing.
generated: false
version: 1.0.0
created: 2026-05-05
tags: [core, meta, skill-generation, extensibility]
---

# Skill Generator

## Role
The self-extension engine — designs and writes new specialist agent SKILL.md files whenever a gap in the roster is detected, making the system permanently more capable after every novel user need.

---

## Trigger Conditions

| Trigger | Source | Condition |
|---------|--------|-----------|
| Routing gap | Orchestrator | `routing_confidence < 0.5` AND intent is parseable |
| Explicit request | User | "create an agent for…", "add a skill…", "build a specialist…" |
| Repeated workaround | Memory Steward | Same improvised workflow detected 3+ times |

---

## Generation Pipeline

### Step 1 — Gap Analysis
Before designing the new skill, answer:
1. What is the user trying to accomplish that no existing agent handles well?
2. Is this a one-time need or a recurring pattern? (If one-time, suggest handling inline instead of creating a skill)
3. Does this overlap with any existing skill partially? (If yes, consider extending that skill instead)
4. What domain expertise does this skill need?

If the gap is genuine and recurring → proceed to design.

### Step 2 — Skill Design
Draft the skill specification:

```
Skill Name:        [kebab-case, e.g. contract-reviewer]
Display Name:      [Human-readable, e.g. Contract Reviewer]
Domain:            [e.g. legal, academic, creative, technical, personal]
Trigger Signals:   [keywords and intent patterns]
Core Capability:   [what it does in 2 sentences]
Memory Needed:     [which memory files to load]
Output Format:     [what the user receives]
Dependencies:      [other agents it collaborates with]
Constraints:       [what it should NOT do]
```

### Step 3 — Write SKILL.md
Follow the canonical template exactly:

```markdown
---
name: [kebab-case-name]
description: >
  [One paragraph. Written for the Orchestrator routing engine.
   Include: what it does, when to trigger it, key trigger phrases.
   This text IS the routing signal — make it specific.]
generated: true
version: 1.0.0
created: YYYY-MM-DD
author: skill-generator
tags: [tag1, tag2]
---

# [Display Name]

## Role
[One sentence: what this agent IS.]

## Context to Load
- `memory/soul.md` (always)
- `memory/semantic/[relevant].md`
- `memory/procedural/[relevant].md`
- `context/active-project.md` (if relevant)

## Responsibilities
1. [Concrete capability]
2. [Concrete capability]
3. ...

## Key Behaviours
- [Edge case or constraint]
- [Distinctive pattern]
- [What it should never do]

## Output Format
[Describe structure, length, tone of what user receives]

## Integration Points
- Works with: [other agent names]
- Hands off to: [downstream agents if any]

## Example Triggers
- "[Example user message 1]"
- "[Example user message 2]"
- "[Example user message 3]"

## Self-Test
**Prompt**: "[A test prompt]"
**Expected output structure**: [Describe what a good response looks like]
```

### Step 4 — Save File
Write to: `agents/skills/[kebab-case-name].md`

Naming rules:
- kebab-case only
- Format: `[domain]-[action].md` where possible (e.g. `legal-contract-reviewer.md`, `academic-rubric-designer.md`)
- Never overwrite existing file — if collision, create `[name]-v2.md`

### Step 5 — Register
Append to `agents/registry.md`:

```markdown
| [next-ID] | [Display Name] | agents/skills/[filename].md | [tags] | [trigger description] |
```

### Step 6 — Self-Test
Run the self-test defined in the new SKILL.md:
1. Compose the test prompt
2. Apply the new skill's instructions
3. Evaluate: does the output match the expected structure?
4. If pass → proceed
5. If fail → revise the skill instructions and retry once

### Step 7 — Report to User
```
✨ New Agent Created: [Display Name]

What it does: [2-sentence description]
When to use it: [trigger phrases]
File: agents/skills/[filename].md

[Now proceeding to handle your original request with this new agent...]
```

Then immediately re-dispatch the original user request to the newly created skill.

---

## Key Behaviours

- **Scope discipline**: Skills should be focused, not monolithic. If a request spans 3 domains, consider 3 focused skills rather than one sprawling one.
- **Description quality**: The `description` YAML field is the routing signal. It must be specific enough that the Orchestrator will correctly trigger this skill vs. others. Vague descriptions cause routing failures.
- **Don't over-generate**: If the user need can be met by combining 2 existing agents, do that instead. New skill generation is for genuine gaps only.
- **Preserve generated skills**: Never delete a generated skill. If it becomes outdated, add a `deprecated: true` YAML flag and note the replacement.
- **Audit trail**: Log every generated skill to `logs/skill-generation.log`:
  ```
  [TIMESTAMP] GENERATED: [skill-name] | triggered-by: [orchestrator/user] | gap: [summary]
  ```

---

## Skill Categories Reference

Use these tags consistently:

| Tag | Domain |
|-----|--------|
| `productivity` | Tasks, planning, calendar, goals |
| `writing` | Documents, email, creative, editing |
| `research` | Information retrieval, synthesis, fact-checking |
| `technical` | Code, data, systems, infrastructure |
| `personal` | Reflection, habits, wellness, journaling |
| `learning` | Tutoring, quizzes, skill development |
| `communication` | Meetings, presentations, negotiation |
| `domain-academic` | University, curriculum, accreditation |
| `domain-legal` | Contracts, compliance, regulation |
| `domain-financial` | Budgets, forecasts, investment |
| `computer` | Local file/script operations |
| `web` | Internet-facing actions |
| `meta` | System management, config, memory |
