# Teaching & Learning Plugin (REVA Educator Pack)

> **Plugin ID:** `reva.teaching-learning-reva` | **Agent Handle:** `@reva-educator` | **Version:** 1.0.0

A prompt-native campus assistant designed for REVA University faculty to accelerate course design, session planning, content generation, and assessment audits while ensuring continuous alignment to NBA-OBE, NEP 2020, and university academic standards.

---

## 🎓 Core Capabilities

### 1. Curriculum & Course Design
* **Outcome Mapping**: Formulates AI-augmented Course Outcomes (COs) and maps them to Program Outcomes (POs) and Program Specific Outcomes (PSOs).
* **Bloom's Taxonomy Verifier**: Ensures HOTS (Higher Order Thinking Skills) dominance in advanced outcomes.
* **Portfolio Linkage**: Helps faculty connect every CO to a tangible student portfolio output (papers, products, or code).

### 2. Session Planning & active learning
* **Active Learning Strategy Selector**: Matches flipped classroom, jigsaw, or Socratic seminar structures to specific outcomes.
* **Active Session Planner**: Generates session plans, lecture notes drafts, proctored laboratory procedural manuals, and slide visual cues.

### 3. Assessment & Integrity Audits
* **AI-Triviality Auditing**: Audits assignments to flag tasks easily bypassed by consumer AI, helping design durable HOTS assessments.
* **Rubric Builder**: Designs precise holistic and analytic rubrics for project evaluations.

### 4. Course Buddy Integration
* **Course Buddy Builder**: Orchestrates generating complete Obsidian wikis, Jupyter study workbooks, and QuizBlast study guides directly from standard course descriptors.

---

## 🛠️ Slash Commands

* **`/course-check`**: Audits a course outline or syllabus for credit mapping, OBE integrity, and portfolio linkage.
* **`/session-check`**: Generates a complete active-learning session plan, lecture notes, and proctored active task briefs.
* **`/assessment-check`**: Audits an assignment brief, exam pattern, or question bank for AI-triviality risks and HOTS alignment.
* **`/build-course-buddy`**: Builds digital learning course companions (Jupyter workbooks, Obsidian wikis, flashcards).
* **`/audit`**: Full quality audit against accreditation ready benchmarks.

---

## 📂 Directory Layout

```plaintext
plugins/teaching-learning-reva/
├── plugin.json         # Google Antigravity Manifest
├── package.json        # GitHub Copilot VS Code Manifest
├── README.md           # This file
├── rules/              # ACADEMIC_INTEGRITY.md, COURSE_DESIGN_STANDARD.md, ASSESSMENT_QUALITY_STANDARD.md
└── workflows/          # session-check.md, course-check.md, assessment-check.md
```
