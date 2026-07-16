---
name: reva-session-designer
description: >
  Design complete, pedagogically rich session materials for one BTech CS session at REVA University.
  Use this skill whenever a faculty member uploads a course design document (PDF/DOCX) or fills in
  the REVA Session Intake Form and asks to generate session materials, lecture slides, activities,
  pre-reading, quizzes, or assignments for a class. Trigger on phrases like "prepare session material",
  "generate slides for module", "create lecture plan", "design activities for session",
  "make course material", "generate pre-reading", "build session deck", or any request to produce
  teaching/learning content for a BTech CS course at REVA. Always use this skill — even if the
  request seems partial (e.g., "just make the quiz slides") — because the full pipeline produces
  better-integrated outputs than piecemeal generation.
compatibility: "Requires bash, web_search, create_file, present_files tools. Uses pptx skill for slide generation."
---

# REVA Session Designer

Produces a full session material package for **one session within a BTech CS module** at REVA University:
- **PPTX slide deck** — REVA-branded, activity-based, ready to present
- **HTML interactive companion** — embedded quizzes, interactive activities, animations

---

## Step 0 — Read the PPTX skill first

Before generating any slides, read `/mnt/skills/public/pptx/SKILL.md` and its `pptxgenjs.md` reference.
The PPTX skill governs all slide creation mechanics, QA, and visual polish standards.

---

## Step 1 — Intake

### If the user uploads a PDF or DOCX course design document:
Extract the following fields (ask the user to confirm or fill gaps):
- Course name, course code, semester, year
- Module number and title
- Session number within module (e.g., Session 2 of 4)
- Session topic / title
- Course Outcomes (COs) addressed — with CO statements
- Bloom's taxonomy levels targeted
- Pre-requisite knowledge students should already have
- Key concepts to be covered (list)
- Suggested activities / lab context (if any)
- Duration (default: 60 minutes)
- Any special notes (guest talk, demo, flipped classroom, etc.)

### If the user does not have a document — use the Intake Form:
Present the **REVA Session Intake Form** (see `references/intake-form.md`) and collect all fields.

### Clarification rule:
Do NOT proceed to Step 2 until you have at minimum:
- Session topic, CO(s) addressed, Bloom's level, key concepts list, duration.

---

## Step 2 — Research Phase (run in parallel)

Once intake is complete, run all three searches simultaneously:

**2a. Curated pre-reading resources**
Search: `"[topic] introduction tutorial BTech CS" site:geeksforgeeks.org OR site:cs.stanford.edu OR site:mit.edu OR nptel`
Aim for 2–3 high-quality links (NPTEL, GeeksForGeeks, MIT OCW, NPTEL, Programiz preferred).
Summarise each in one line.

**2b. Curated video resources**
Search: `"[topic] explained" YouTube OR NPTEL site:youtube.com`
Find 2–3 videos under 15 minutes. Include title, channel, approx duration, URL.
Prefer: NPTEL, CS Dojo, Abdul Bari, MIT OpenCourseWare, 3Blue1Brown (for math-adjacent topics), Fireship (for web/programming topics).

**2c. Activity ideas and analogies**
Search: `"[topic] teaching activity analogy classroom CS"` to find any published active learning ideas, analogies, or demos specific to this topic.

---

## Step 3 — Pedagogical Planning

Before writing any slides, produce an internal **Session Blueprint** (show this to faculty for confirmation before generating slides):

```
SESSION BLUEPRINT
─────────────────────────────────────────────
Course: [name] | Session [X] of [Y] | [duration] min
Topic: [topic]
COs addressed: [CO list]
Bloom's level: [Remember / Understand / Apply / Analyse / Evaluate / Create]

ARC:
1. HOOK (5 min)          → [describe hook: surprising fact, demo, question, story]
2. PRE-READING RECAP (5 min) → [what students should have read; quick recall activity]
3. LEARNING OUTCOMES (2 min) → [3–5 LOs, Bloom's-tagged]
4. CONCEPT BUILD (25 min)    → [chunked into 2–3 sub-topics; note where Socratic Q&A fits]
5. ACTIVITY (10 min)         → [quiz / case / simulation / think-pair-share — specify which]
6. PRACTICE (8 min)          → [problem set / peer exercise / quick coding challenge]
7. DEBRIEF + SYNTHESIS (3 min) → [what did we learn; connect back to CO]
8. ASSIGNMENT BRIEF (2 min)   → [task, rubric, Bloom's tag, submission format]

Activity selection rationale: [why these activities for this Bloom's level + topic]
Neuro-cognitive notes: [spaced retrieval, dual coding, interleaving, worked example — which apply here]
─────────────────────────────────────────────
```

**Pedagogical principles to apply** — see `references/pedagogy.md` for full guidance. Key rules:
- Apply **Cognitive Load Theory**: chunk new content into ≤3 concepts per slide; use worked examples before problems
- Apply **Dual Coding**: pair every concept explanation with a visual (diagram, analogy illustration, timeline)
- Apply **Retrieval Practice**: embed at least one unannounced recall question before the activity segment
- Apply **Socratic Questioning**: for analytical/application topics, use a question-chain sequence of 3–5 escalating questions instead of direct explanation (see `references/pedagogy.md` §Socratic)
- **Concept check quiz** is mandatory every session; Kahoot-style competitive quiz when topic has ≥5 discrete facts to recall
- CO–Bloom's alignment must be visible on the Learning Outcomes slide

---

## Step 4 — Slide Deck Generation (PPTX)

Target: **20–30 slides** for a 60-minute session. Scale proportionally for other durations.

### REVA Brand Standards
- Primary: **REVA Orange `#F7A35B`**
- Dark: **REVA Grey `#4A4C55`**  
- Background: **White `#FFFFFF`** (content slides) / REVA Grey (title, section dividers)
- Accent: **Light orange tint `#FDE8D0`** for highlight boxes
- Font: **Plus Jakarta Sans** — Bold for titles, Regular for body
- Fallback fonts (PPTX): Calibri (title), Calibri Light (body)
- Logo: Place REVA wordmark top-right on title slide and section dividers (use text "REVA University" in REVA Orange if no logo asset available)
- CO badge: Small pill/tag bottom-left of Learning Outcomes slide and Assignment slide

### Mandatory Slide Set (in order):

| # | Slide Type | Notes |
|---|-----------|-------|
| 1 | **Title slide** | Session title, course code, module, session no., faculty name placeholder, date placeholder |
| 2 | **Pre-reading** | 2–3 resources with one-line descriptions + URLs; "Read before this session" header |
| 3 | **Videos to watch** | 2–3 curated videos, title + channel + duration + URL |
| 4 | **Learning Outcomes** | 3–5 LOs with Bloom's verb tags; CO mapping shown as badges |
| 5 | **Hook** | Surprising fact, provocative question, or short scenario — no definitions yet |
| 6–N | **Concept build slides** | Chunked; max 3 concepts per slide; dual-coded (text + visual); Socratic Q slides interspersed |
| N+1 | **Retrieval check** | "Before we go further — what do you recall?" — 2 quick MCQs, answers revealed on click |
| N+2 | **Activity slide** | Full-screen activity prompt (quiz, case study, think-pair-share, or scenario) |
| N+3 | **Practice** | Problem / challenge slide with worked example hint |
| N+4 | **Debrief** | Key takeaways; connect back to LOs and CO |
| N+5 | **Assignment** | Task description, Bloom's level tag, rubric table (criteria / marks), submission format |

### Slide design rules (from PPTX skill):
- Every slide must have a visual element — no text-only slides
- Use icon-in-circle motif for lists; orange accent boxes for key definitions
- Dark (REVA Grey) background for title, section dividers, hook, and debrief slides
- Light background for all content slides
- Socratic question slides: full-screen dark background, single large question in white, pause icon

---

## Step 5 — Interactive HTML Companion

Generate a single self-contained HTML file alongside the PPTX. It must include:

### HTML Required Sections:
1. **Session header** — title, CO, Bloom's level, duration badge (REVA branded)
2. **Pre-reading panel** — clickable resource cards with links
3. **Video panel** — clickable video cards with thumbnails (YouTube embed or link)
4. **Interactive concept check quiz** — MCQ with instant feedback, score tracker, REVA-styled
5. **Kahoot-style rapid quiz** (if topic warrants) — timed questions, points, leaderboard display (single-player simulation)
6. **Activity widget** — appropriate to topic:
   - Matching/drag-and-drop for classification topics
   - Scenario-choice branching for case studies
   - Animated diagram for process/algorithm topics
   - Socratic question reveal sequence for analytical topics
7. **Practice problem** — with "Show hint" and "Show solution" toggles
8. **Assignment card** — task, rubric table, Bloom's tag, submission format

### HTML technical standards:
- Single file, no external dependencies except CDN (use Tailwind CDN, no build step)
- REVA colour variables: `--reva-orange: #F7A35B; --reva-grey: #4A4C55; --reva-light: #FDE8D0`
- Mobile-responsive
- Smooth scroll navigation between sections
- Print-friendly (assignment card should print cleanly)

---

## Step 6 — QA

### PPTX QA:
Follow the full QA loop from the PPTX skill:
1. Extract text with `markitdown` — check for missing content
2. Convert to images — visually inspect for overlap, overflow, contrast issues
3. Fix and re-verify

### HTML QA:
- Open in bash with `python3 -m http.server` or verify file structure
- Check all interactive elements have correct answer keys
- Verify all URLs from web search are live (curl check)

---

## Step 7 — Deliver

Copy final files to `/mnt/user-data/outputs/`:
- `[CourseCode]_[ModuleNo]_Session[N]_Slides.pptx`
- `[CourseCode]_[ModuleNo]_Session[N]_Interactive.html`

Call `present_files` with both files.

Provide a brief summary to faculty:
- Session arc (8-step sequence)
- Activity type used and rationale
- Kahoot quiz: yes/no
- Assignment Bloom's level
- CO(s) addressed

---

## Reference Files

- `references/intake-form.md` — The structured intake form to present when no document is uploaded
- `references/pedagogy.md` — Full pedagogical and neuro-cognitive principles guide
