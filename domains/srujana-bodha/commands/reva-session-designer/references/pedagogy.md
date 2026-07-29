# Pedagogical & Neuro-Cognitive Principles Reference

This file guides activity selection and session design decisions in the REVA Session Designer skill.

---

## 1. Cognitive Load Theory (Sweller)

**Core rule:** Working memory handles ~4 items at once. Overloading it blocks learning.

**Application in session design:**
- Never introduce more than **3 new concepts per slide**
- Use **worked examples first**, then practice problems (not the reverse)
- Provide **partially completed examples** for complex procedures (completion problems)
- Avoid split-attention: keep labels adjacent to diagrams, not in a separate legend
- Use **segmenting**: break long animations or code walkthroughs into user-paced steps

**When to apply:** Every concept-build segment. Especially critical for algorithms, data structures, mathematical proofs, and multi-step procedures.

---

## 2. Dual Coding (Paivio)

**Core rule:** Verbal + visual encoding together are retained better than either alone.

**Application:**
- Every concept slide must have a **corresponding visual** — diagram, analogy illustration, timeline, flowchart, or metaphor image
- For abstract concepts: use **concrete analogies with visual representation** (e.g., "a stack is like a stack of plates")
- For process/algorithm content: use **step-by-step animated diagrams** in HTML companion
- Avoid decorative images (clip art); all visuals must encode meaning

**When to apply:** All concept-build slides. Especially powerful for data structures, OS concepts, network architecture, compiler phases.

---

## 3. Retrieval Practice (Roediger & Karpicke)

**Core rule:** Recalling information strengthens memory more than re-reading it.

**Application:**
- Embed a **surprise retrieval check** (2 MCQs, no stakes) before the main activity — students don't know it's coming
- Start session with a **"What do you remember from last session?"** prompt (1 slide, 2 minutes)
- End session with **exit ticket**: "State one thing you learned and one question you still have"
- Concept check quiz is mandatory every session

**When to apply:** Pre-reading recap slide, mid-session retrieval check, debrief segment.

---

## 4. Spaced Practice

**Core rule:** Distributing practice over time beats massed practice.

**Application:**
- Assignment should reference a concept from a **prior module** alongside the current one (interleaving)
- Pre-reading brief should connect to **previously covered COs**
- Assignment brief note: "This also revisits CO[X] from Module [Y]"

---

## 5. Socratic Questioning

**Core rule:** Questions that require students to construct answers build deeper understanding than explanations alone.

**When to use Socratic approach:**
- Topics at **Analyse, Evaluate, or Create** Bloom's level
- When the concept has a non-obvious "why" (e.g., why does quicksort have O(n²) worst case?)
- When students hold a common misconception that can be surfaced through questioning

**Socratic question chain structure (3–5 escalating questions):**

```
Level 1 — Recall/surface:      "What does [term] mean?"
Level 2 — Probe assumption:    "Why do we assume [X]?"
Level 3 — Evidence/reasoning:  "How would you know if [X] were false?"
Level 4 — Alternative view:    "Could [Y] achieve the same result? Why or why not?"
Level 5 — Implication:         "If [X] is true, what follows for [Z]?"
```

**Slide design for Socratic sequence:**
- One question per slide, full-screen dark background, white text, large font (40pt+)
- "Pause and discuss" icon at bottom
- Reveal next question only after discussion cue
- Faculty notes: suggested answer + common wrong answer for each question

**Do NOT use Socratic approach for:** Remember/Understand level topics, first-time exposure to completely new vocabulary, procedural "how to" steps.

---

## 6. Activity Selection Guide

Use this table to select the right activity type based on Bloom's level and topic type:

| Bloom's Level | Topic Type | Recommended Activity |
|--------------|-----------|---------------------|
| Remember | Vocabulary, facts, syntax | Concept check MCQ, Kahoot-style quiz |
| Understand | Concepts, mechanisms | Think-Pair-Share, analogy mapping |
| Apply | Procedures, algorithms | Coding challenge, worked example completion |
| Analyse | Trade-offs, comparisons | Case study, Socratic chain, pros/cons table |
| Evaluate | Design decisions, justification | Scenario choice with reasoning, peer review |
| Create | System design, new solutions | Mini-project brief, design challenge |

**Kahoot-style quiz:** Use when topic has **≥5 discrete facts** (e.g., OS scheduling algorithm names and properties, SQL clause types, sorting algorithm complexities). Do NOT use for Analyse/Evaluate/Create levels — competitive speed undermines reflective thinking.

**Think-Pair-Share:** Use for conceptual "why" questions at Understand/Apply level. Allow 60 seconds individual think time, 60 seconds pair, then share with class.

**Simulation / animation:** Use for dynamic processes — sorting algorithms, memory allocation, TCP handshake, CPU scheduling, compilation phases. Embed in HTML companion.

**Mini case study:** Use for Analyse/Evaluate. Present a 3–5 sentence scenario with a decision point. Students choose + justify. Best for 10-minute slots.

---

## 7. The Hook Principle

**Core rule:** The brain prioritises novel, surprising, or emotionally relevant information. The first 5 minutes of a session determine attention for the next 55.

**Hook types by topic:**

| Hook Type | Example Application |
|-----------|-------------------|
| Surprising fact or statistic | "Google's search index is ~100 petabytes. How does it return results in 0.3 seconds?" |
| Provocative question | "Is an O(n²) algorithm ever better than O(n log n)?" |
| Real failure story | "The Therac-25 radiation machine killed patients due to a race condition. Let's see how." |
| Live demo | Run a short code snippet that produces a counterintuitive result |
| Analogy reveal | "Today's topic works exactly like a restaurant kitchen. Here's why." |

**Hook slide design:** Dark background, single bold statement or question, no bullet points, relevant image (full bleed preferred).

---

## 8. Assignment Design Principles (Bloom's-aligned)

| Bloom's Level | Assignment Verb | Example |
|--------------|----------------|---------|
| Remember | List, define, label | List all TCP/IP layers and their functions |
| Understand | Explain, summarise, classify | Explain why a hash collision occurs with an example |
| Apply | Implement, solve, use | Implement a linked list with insert and delete operations |
| Analyse | Compare, differentiate, examine | Compare BFS and DFS for a given graph problem; justify your choice |
| Evaluate | Justify, critique, assess | Critique the use of bubble sort in a production system; propose an alternative |
| Create | Design, construct, develop | Design a cache replacement policy for a given workload; implement and test it |

**Rubric template (4 criteria):**

| Criterion | Excellent (4) | Satisfactory (2) | Needs Work (1) |
|-----------|--------------|-----------------|----------------|
| Correctness | Fully correct, edge cases handled | Mostly correct, minor errors | Significant errors |
| Understanding | Demonstrates deep understanding | Basic understanding evident | Misses key concepts |
| Communication | Clear, well-structured, precise | Readable but disorganised | Hard to follow |
| [Topic-specific] | [Define per assignment] | | |

Scale marks to assignment weight. Always state: submission format, file naming convention, LMS deadline.

---

## 9. Neuro-Cognitive Quick Reference

| Principle | 1-line rule | Slide/Activity implication |
|-----------|------------|--------------------------|
| Primacy-Recency | Students best remember first and last 5 minutes | Strong hook; clear debrief |
| Interleaving | Mix topics across practice | Assignment references prior CO |
| Elaborative interrogation | "Why is this true?" > "What is this?" | Prefer Socratic to declarative slides |
| Desirable difficulty | Moderate challenge > too easy or too hard | Target Bloom's level +1 above prior session |
| Emotional salience | Relevant + surprising = memorable | Real-world failure stories in hooks |
| Sleep consolidation | Learning consolidates during sleep | Assign pre-reading day before, not hours before |
