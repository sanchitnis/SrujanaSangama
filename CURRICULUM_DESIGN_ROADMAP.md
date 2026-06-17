# 🗺️ Newbie's Roadmap: From School Vision to Course Syllabus
## A Complete Reference Guide for REVA Curriculum Designers

> **Who is this for?** Anyone starting from scratch — a new faculty member, a school director, or a programme lead who wants to design a school, curriculum, or individual course. This document tells you **which files to read, in which order, and why** before you start building anything.

---

## How to Read This Roadmap

Each stage of building a curriculum is a **Phase**. For every Phase:
- 📖 **Read First** — the document(s) you must read before doing anything
- 🤖 **AI Skill to Use** — the command you invoke in the AI to get structured help
- ✅ **Gate** — what must be approved before you move to the next Phase
- 📄 **Output** — the document you produce at the end of this Phase

---

## The Big Picture: 5 Phases of Curriculum Design

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│   PHASE 1        PHASE 2        PHASE 3       PHASE 4    PHASE 5  │
│   SCHOOL         PROGRAMME      COURSE         ACTIVITY   CONCEPT   │
│   STRATEGY  ──►  ARCHITECTURE ──► DESIGN   ──► DESIGN ──► MAPPING  │
│                                                                     │
│   "Why does      "What does      "What is       "How will  "Does     │
│   this school    the programme   each course    students   it all    │
│   exist?"        look like?"     teach?"        learn?"    connect?" │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

**Total estimated time for a new programme:** 4–6 months (teams working in parallel)

---

## 🏛️ Phase 1: School Strategy
### "I want to build a strategy document for my school"

**What this phase produces:** A School Curriculum Strategy Document that defines your school's vision, the job roles your graduates will fill, and the market intelligence that justifies your programme design.

---

### 📖 Step 1 — Read This First (Before Writing Anything)

| Priority | File to Read | Why You Need It | Location |
| :---: | :--- | :--- | :--- |
| ⭐ Must Read | **Curriculum Design Framework v2** | The single master document that explains the entire REVA philosophy: AI-era design, OBE, Portfolio-first, IKS, and international benchmarks. Start here. | [CURRICULUM_DESIGN_FRAMEWORK_v2.md](file:///d:/SrujanaSangama/plugins/teaching-learning-reva/CURRICULUM_DESIGN_FRAMEWORK_v2.md) |
| ⭐ Must Read | **Curriculum Design Lifecycle** | The step-by-step process guide for all 5 Phases. This is your master workflow document — what to do, in what order, and who approves what. | [curriculum-design-lifecycle.md](file:///d:/SrujanaSangama/plugins/teaching-learning-reva/workflows/curriculum-design-lifecycle.md) |

---

### ✍️ Step 2 — What You Must Write (Your Inputs)

Your strategy document must contain these four sections. Write them yourself — AI will help you structure, but the content must come from human deliberation:

1. **School Vision & Mission** — What kind of graduate does your school produce? How does it connect to REVA's values?
2. **Programme Educational Objectives (PEOs)** — 3 to 5 statements describing what your graduates will achieve 3–5 years after graduation. *(Refer to today's conversation for how to frame these correctly.)*
3. **Job Role Analysis** — 6–10 specific roles your graduates will hold. Name them, describe the tools and skills each role requires.
4. **Market & Futures Intelligence** — What do WEF, NASSCOM, and industry trends say about your domain? Who are your peer institutions?

> [!IMPORTANT]
> **Design Engineering Specific:** If you are designing for the B.Tech Design Engineering programme, also read [ext_Design_Engineering.md](file:///d:/SrujanaSangama/docs/Guidelines/ext_Design_Engineering.md). This document overrides certain universal rules for a studio-based programme and explains how Design Engineering assessment (Jury Critique, Process Portfolio) differs from standard engineering programmes.

---

### 🤖 Step 3 — Use the AI to Audit Your Draft

Once you have a draft strategy document, invoke this AI skill to check it:

```
/curriculum-strategy-check <path-to-your-strategy-document>
```

**What it checks (8 Dimensions):**

| Dimension | What It Audits |
| :--- | :--- |
| 1 | Alignment to REVA Mission & Vision |
| 2 | AI-Era Ambition in your PEOs |
| 3 | Job Role Clarity & Industry Grounding |
| 4 | Enterprising Human Skills Thread |
| 5 | Sustainability & IKS Integration |
| 6 | Market Intelligence & Futures Grounding |
| 7 | Competency Framework & PO/PSO Architecture |
| 8 | International Benchmarking |

**Reference:** [10_curriculum-strategy-check.md](file:///d:/SrujanaSangama/plugins/teaching-learning-reva/workflows/10_curriculum-strategy-check.md)

---

### ✅ Phase 1 Gate: Faculty Committee Approval

Before moving to Phase 2, these must be signed off:
- [ ] Strategy brief approved by faculty curriculum committee
- [ ] Job role profiles validated by industry advisory board
- [ ] PEOs endorsed by school leadership
- [ ] Strategy audit passes (all 8 dimensions: PASS or CONDITIONAL with remediation plan)

**Output:** ✅ School Curriculum Strategy Document (approved)

---

## 📐 Phase 2: Programme Architecture
### "I have an approved strategy. Now I need to build the programme structure."

**What this phase produces:** A finalized PO/PSO framework, the semester-wise programme structure, a concept prerequisite map, and a portfolio strategy.

---

### 📖 Step 1 — Read This First

| Priority | File to Read | Why You Need It | Location |
| :---: | :--- | :--- | :--- |
| ⭐ Must Read | **Curriculum Design Lifecycle** — Phase 2 section | Step-by-step instructions for translating PEOs into POs and PSOs, building the programme structure, and designing the portfolio strategy. | [curriculum-design-lifecycle.md](file:///d:/SrujanaSangama/plugins/teaching-learning-reva/workflows/curriculum-design-lifecycle.md) (Lines 70–122) |
| ⭐ Must Read | **Course Design Standard (Rules)** | The non-negotiable quality standards that govern every course in the programme: HOTS dominance (60%+), CO-PO mapping strength levels, Portfolio-first linkage, and IKS integration. Read this before defining POs so your POs are designed to match what courses can realistically attain. | [COURSE_DESIGN_STANDARD.md](file:///d:/SrujanaSangama/plugins/teaching-learning-reva/rules/COURSE_DESIGN_STANDARD.md) |

---

### ✍️ Step 2 — What You Must Build

**Step 2.1: Translate PEOs → Programme Outcomes (POs) & PSOs**
- Use the 11 NBA POs as your base framework
- Adapt them for AI-era context
- Add 2–3 Programme Specific Outcomes (PSOs) that make your programme distinct
- Map every PO/PSO to the job roles you defined in Phase 1
- Ensure the full PO/PSO set covers: technical competency, AI literacy, ethical reasoning, sustainable thinking, global perspective, and enterprising mindset

**Step 2.2: Build Programme Structure**
- Design semester-wise course layout (credits, L-T-P patterns)
- Decide core vs. elective balance
- Plan Srujana Stage integration (Stage 2 internship, Stage 3 product/research, Stage 4 venture)

**Step 2.3: Map the Concept Prerequisite Network**
- Extract all foundational concepts the programme teaches
- Map prerequisites: PUC → Year 1 → Year 2 → Year 3 → Year 4
- Ensure no concept is "floating" (every concept has a prerequisite and a downstream usage)

**Step 2.4: Define Portfolio & Attainment Strategy**
- What does a graduate's portfolio look like at the end of 4 years?
- What type of artefact does each course produce?
- How does the capstone integrate everything?

> [!IMPORTANT]
> **Design Engineering Specific:** Read Section 12 (Portfolio Strategy) of [ext_Design_Engineering.md](file:///d:/SrujanaSangama/docs/Guidelines/ext_Design_Engineering.md). The Design Engineering portfolio model (process documentation, Jury Crits, studio artefacts) differs significantly from a standard engineering programme.

---

### ✅ Phase 2 Gate: Faculty + Industry Validation

- [ ] PO/PSO set approved by faculty committee and industry advisory board
- [ ] Programme structure aligned to job roles and credit regulations
- [ ] Concept network validated (no isolated concepts)
- [ ] Portfolio strategy accepted as the CO-PO attainment evidence mechanism

**Output:** ✅ Programme PO/PSO Document + Programme Curriculum Outline + Concept Prerequisite Map + Portfolio Strategy

---

## 📚 Phase 3: Course Design
### "I need to design an individual course — outcomes, mapping, and structure."

**What this phase produces:** A complete course design document with Course Outcomes (COs), CO-PO/PSO mapping, unit structure, portfolio output, and institutional integration (IKS, sustainability, liberal studies).

---

### 📖 Step 1 — Read This First

| Priority | File to Read | Why You Need It | Location |
| :---: | :--- | :--- | :--- |
| ⭐ Must Read | **Course Designer Guidelines 2026** | The primary practical guide for course design. Tells you how to design any course type (theory, studio, lab, workshop, project, internship). **Start here before writing a single CO.** | [Course_Designer_Guidelines_2026.md](file:///d:/SrujanaSangama/docs/Guidelines/Course_Designer_Guidelines_2026.md) |
| ⭐ Must Read | **Course Designer Guidelines Universal** | The comprehensive universal rulebook for all course types. Contains all L-T-P patterns explained, design rules by course type, and the design checklist. | [Course_Designer_Guidelines_Universal.md](file:///d:/SrujanaSangama/docs/Guidelines/Course_Designer_Guidelines_Universal.md) |
| ⭐ Must Read | **Course Design Standard (Rules)** | The non-negotiable REVA quality rules for every course. Read to understand what the AI audit will check you against. | [COURSE_DESIGN_STANDARD.md](file:///d:/SrujanaSangama/plugins/teaching-learning-reva/rules/COURSE_DESIGN_STANDARD.md) |
| Supplementary | **Assessment Quality Standard** | Deeper guidance on designing assessments that are rigorous, AI-resistant, and HOTS-dominant. | [ASSESSMENT_QUALITY_STANDARD.md](file:///d:/SrujanaSangama/plugins/teaching-learning-reva/rules/ASSESSMENT_QUALITY_STANDARD.md) |
| Supplementary | **Course Design Workflow (Quick Notes)** | A brief internal workflow note about how faculty and AI collaborate to create courses. Good for a quick context overview. | [CourseDesignWorkflow.md](file:///d:/SrujanaSangama/docs/Guidelines/CourseDesignWorkflow.md) |

> [!IMPORTANT]
> **Design Engineering Specific:** The universal guidelines tell you to apply standard engineering course rules. For Design Engineering, you MUST ALSO read [ext_Design_Engineering.md](file:///d:/SrujanaSangama/docs/Guidelines/ext_Design_Engineering.md). This document overrides assessment structure (Jury Critique replaces IA tests), course categories (SC-Studio, SC-Fablab, SC-Field, SC-Digital), and portfolio requirements for all studio courses.

---

### ✍️ Step 2 — What You Must Build

**Step 3.1: Identify Your Course Type**
Use the course type decision table in the Guidelines (§2) to classify your course:
- `FC` Foundation Course | `HC` Hard Core Theory | `HC-Integrated` | `SC` Soft Core | `W` Workshop | `OE` Open Elective | `Proj` Project | `Intern` Internship
- *Design Engineering adds:* `SC-Studio` | `SC-Fablab` | `SC-Field` | `SC-Digital`

**Step 3.2: Write Course Outcomes (COs)**
- 4–6 outcomes per course
- Use strong action verbs (analyze, design, evaluate, create, critique, optimize) — NOT "understand" or "know"
- At least 60% of COs must target Bloom's L4–L6 (Analyze, Evaluate, Create)
- At least 1 CO must explicitly target an enterprising human skill (initiative, adaptability, collaboration, ethical reasoning, communication, creativity)
- Each CO must link to at least one job role from your Phase 1 analysis

**Step 3.3: Map CO-PO/PSO (Strength Levels)**
Each CO maps to 1–3 POs/PSOs with a strength level:
| Level | Meaning |
| :--- | :--- |
| **1 (Slight)** | Indirect/minor reinforcement |
| **2 (Moderate)** | Explicitly assessed in projects or labs |
| **3 (Substantial)** | Direct, central focus; measured as a core outcome. Must have proctored or viva validation. |

**Step 3.4: Design Unit Structure**
- 4–5 units per course (semester span)
- Each unit links to 1–3 COs
- Each unit names the prerequisite concepts from prior courses
- Each unit includes a portfolio output

**Step 3.5: Embed Institutional Threads**
Every course must explicitly address:
- 🇮🇳 **IKS** — Historical Indian engineering/math example, local case study, or Indian philosophical principle
- 🌱 **Sustainability** — Resource optimization, environmental impact, or ethical consideration
- 🎨 **Liberal Studies** — Ethics, communication, design thinking, or creative expression connection

---

### 🤖 Step 3 — Use the AI to Audit Your Draft

Once you have a draft course design, invoke:

```
/course-check <path-to-your-course-design-document>
```

**What it checks (7 Dimensions):**

| Dimension | What It Audits |
| :--- | :--- |
| 1 | Course Outcomes Quality & Bloom's Verification |
| 2 | CO-PO/PSO Mapping Rigor & Strength Levels |
| 3 | Enterprise Human Skills Thread |
| 4 | Portfolio Linkage & Artefact Mapping |
| 5 | Assessment Strategy & HOTS Dominance |
| 6 | Institutional Integration (IKS, Sustainability, Liberal Studies) |
| 7 | Concept Prerequisites & Future Course Alignment |

**Reference:** [course-check.md](file:///d:/SrujanaSangama/plugins/teaching-learning-reva/workflows/course-check.md)

---

### ✅ Phase 3 Gate: Peer Review + Subject Expert Input

- [ ] All COs verified for Bloom's levels and AI-era design
- [ ] CO-PO/PSO mapping reviewed for rigor and justification (no orphaned COs)
- [ ] Enterprise skills CO present and assessed
- [ ] Portfolio output clearly defined and linked to COs
- [ ] IKS, sustainability, liberal studies integration specified

**Output:** ✅ Course Design Document (ADDIE-compliant, with CO-PO mapping, unit structure, portfolio linkage)

---

## 🎯 Phase 4: Activity & Assessment Design
### "My course outcomes are set. Now I need to design how students actually learn and are assessed."

**What this phase produces:** A unit-wise activity playbook with AI-ready learning activities, rubrics, and proctored validation tasks.

---

### 📖 Step 1 — Read This First

| Priority | File to Read | Why You Need It | Location |
| :---: | :--- | :--- | :--- |
| ⭐ Must Read | **Curriculum Design Lifecycle** — Phase 4 section | The detailed process for activity design: what types of activities to design, how to verify AI-readiness, rubric design standards, and proctored validation tasks. | [curriculum-design-lifecycle.md](file:///d:/SrujanaSangama/plugins/teaching-learning-reva/workflows/curriculum-design-lifecycle.md) (Lines 195–265) |
| ⭐ Must Read | **Assessment Quality Standard** | The rules that govern assessment design quality: HOTS dominance in assessment, AI-triviality checks, rubric standards, and formative vs summative balance. | [ASSESSMENT_QUALITY_STANDARD.md](file:///d:/SrujanaSangama/plugins/teaching-learning-reva/rules/ASSESSMENT_QUALITY_STANDARD.md) |

> [!IMPORTANT]
> **Design Engineering Specific:** Read Sections 5 (Assessment Model), 6 (Merrill's First Principles), and 10 (AI-Augmented Assessment) of [ext_Design_Engineering.md](file:///d:/SrujanaSangama/docs/Guidelines/ext_Design_Engineering.md). The assessment model for Design Engineering uses **Jury Critiques** (Crit 1 + Crit 2) instead of standard IA-1/IA-2 tests, and assessment lives entirely in rubrics for studio courses.

---

### ✍️ Step 2 — What You Must Build

**Activity Types (per unit):**
1. **In-class active learning** — Flipped classroom, Think-Pair-Share, Jigsaw, Socratic Seminar, Case Study
2. **Out-of-class guided project** — Design challenge with AI-ready constraints (localized, meta-cognitive, authentic)
3. **Proctored skill validation** — Viva-voce, live coding/modification, peer teaching, in-lab execution (mandatory for all Strength 3 CO-PO mappings)
4. **Portfolio synthesis task** — The cumulative output that feeds the course portfolio

**The AI-Readiness Test for Every Assignment:**
Every major assessment must pass ALL of these:
- ✅ **Localized Constraint** — uses student-specific or context-specific data that can't be generically prompted
- ✅ **Meta-Cognitive Component** — student must explain their reasoning, not just submit a solution
- ✅ **Authentic Indicator** — mirrors real professional practice; produces a tangible artefact
- ✅ **Proctoring Strategy** — how will you verify this is the student's own work? (viva, live demo, peer teaching)

**Rubric Design Standards:**
- Holistic rubric: 4–5 levels (Excellent → Emerging); CO and PO indicators at each level
- Analytic rubric: 4–6 criteria (content, process, presentation, collaboration, ethics, creativity)
- Enterprise skills must have an explicitly scored criterion in the rubric (not just implied)

---

### 🤖 Step 3 — Use the AI to Design Activities

```
/activity-design-ai-ready <unit-description>
```

**What it generates:**
- 3–5 unit activities, including in-class, out-of-class, and proctored validation tasks
- Each activity tagged with Bloom's level, enterprise skill, AI-readiness indicators, and portfolio contribution

**Reference:** [11_activity-design-ai-ready.md](file:///d:/SrujanaSangama/plugins/teaching-learning-reva/workflows/11_activity-design-ai-ready.md)

---

### ✅ Phase 4 Gate: Pedagogy + Industry Expert Review

- [ ] All activities mapped to COs and HOTS levels
- [ ] AI-readiness audit passed: no AI-trivial tasks; all assignments include contextual constraints
- [ ] Rubrics are observable, measurable, and linked to COs and POs
- [ ] Proctored validation activities designed for all Strength 3 CO-PO mappings
- [ ] Enterprise skills assessed in 2–3 activities with visible rubric criteria

**Output:** ✅ Unit-wise Activity Playbook + Full Rubric Set + Proctored Activity Briefs

---

## 🕸️ Phase 5: Concept Map & Curriculum Coherence
### "All courses are designed. Now I need to verify the whole curriculum hangs together."

**What this phase produces:** A visual concept dependency map of the entire programme and a coherence audit confirming no orphaned, isolated, or circular concepts exist.

---

### 📖 Step 1 — Read This First

| Priority | File to Read | Why You Need It | Location |
| :---: | :--- | :--- | :--- |
| ⭐ Must Read | **Curriculum Design Lifecycle** — Phase 5 section | Explains how to extract concepts from all courses, build the network map, identify coherence gaps, and link concepts to job roles. | [curriculum-design-lifecycle.md](file:///d:/SrujanaSangama/plugins/teaching-learning-reva/workflows/curriculum-design-lifecycle.md) (Lines 268–332) |

---

### 🤖 Step 2 — Use the AI to Build the Concept Map

```
/concept-map-network <path-to-all-course-designs>
```

**What it generates:**
- A Mermaid network diagram of all concepts across all courses
- A CSV matrix: Concept | Prerequisite | Courses Taught | Bloom's Levels | Job Roles | GATE Relevance
- A coherence audit report flagging: isolated concepts, orphaned prerequisites, circular dependencies, job-role gaps

**Reference:** [12_concept-map-network.md](file:///d:/SrujanaSangama/plugins/teaching-learning-reva/workflows/12_concept-map-network.md)

---

### ✅ Phase 5 Gate: Curriculum Committee Final Approval

- [ ] Concept map complete: no isolated concepts; all prerequisites and usage paths clear
- [ ] All job role skills mapped to ≥1 concept-CO-course
- [ ] Global benchmarking review complete
- [ ] Final approval by curriculum committee + programme leader

**Output:** ✅ Concept Network Diagram + Coherence Audit Report → Ready for BOS Submission

---

## 📋 Quick Reference: Complete Document Index

### "Which file do I open for what?"

| I want to... | Read this file | Location |
| :--- | :--- | :--- |
| Understand the entire REVA curriculum design philosophy | CURRICULUM_DESIGN_FRAMEWORK_v2.md | [Link](file:///d:/SrujanaSangama/plugins/teaching-learning-reva/CURRICULUM_DESIGN_FRAMEWORK_v2.md) |
| Follow the step-by-step process for all 5 phases | curriculum-design-lifecycle.md | [Link](file:///d:/SrujanaSangama/plugins/teaching-learning-reva/workflows/curriculum-design-lifecycle.md) |
| Know the non-negotiable rules for every course | COURSE_DESIGN_STANDARD.md | [Link](file:///d:/SrujanaSangama/plugins/teaching-learning-reva/rules/COURSE_DESIGN_STANDARD.md) |
| Know the assessment quality rules | ASSESSMENT_QUALITY_STANDARD.md | [Link](file:///d:/SrujanaSangama/plugins/teaching-learning-reva/rules/ASSESSMENT_QUALITY_STANDARD.md) |
| Know the academic integrity rules | ACADEMIC_INTEGRITY.md | [Link](file:///d:/SrujanaSangama/plugins/teaching-learning-reva/rules/ACADEMIC_INTEGRITY.md) |
| Design any course (primary practical guide) | Course_Designer_Guidelines_2026.md | [Link](file:///d:/SrujanaSangama/docs/Guidelines/Course_Designer_Guidelines_2026.md) |
| Understand course types by L-T-P (Universal rulebook) | Course_Designer_Guidelines_Universal.md | [Link](file:///d:/SrujanaSangama/docs/Guidelines/Course_Designer_Guidelines_Universal.md) |
| Design a Design Engineering course specifically | ext_Design_Engineering.md | [Link](file:///d:/SrujanaSangama/docs/Guidelines/ext_Design_Engineering.md) |
| See a real, filled-out course design template | Course_File_Template_DualLevel.md | [Link](file:///d:/SrujanaSangama/docs/Guidelines/Course_File_Template_DualLevel.md) |
| Run the Phase 1 strategy audit | 10_curriculum-strategy-check.md | [Link](file:///d:/SrujanaSangama/plugins/teaching-learning-reva/workflows/10_curriculum-strategy-check.md) |
| Run the Phase 3 course audit | course-check.md | [Link](file:///d:/SrujanaSangama/plugins/teaching-learning-reva/workflows/course-check.md) |
| Design AI-ready activities for a unit | 11_activity-design-ai-ready.md | [Link](file:///d:/SrujanaSangama/plugins/teaching-learning-reva/workflows/11_activity-design-ai-ready.md) |
| Build a concept map across the programme | 12_concept-map-network.md | [Link](file:///d:/SrujanaSangama/plugins/teaching-learning-reva/workflows/12_concept-map-network.md) |
| Quickly understand the course design workflow | CourseDesignWorkflow.md | [Link](file:///d:/SrujanaSangama/docs/Guidelines/CourseDesignWorkflow.md) |
| Find a sample Engineering Mathematics syllabus | engMath.md | [Link](file:///d:/SrujanaSangama/docs/Guidelines/engMath.md) |

---

## 🤖 AI Skills Cheat Sheet

| When you are at... | Use this command | What it does |
| :--- | :--- | :--- |
| Phase 1 — Auditing your strategy document | `/curriculum-strategy-check <file>` | 8-dimension audit of your school strategy |
| Phase 3 — Auditing a course design | `/course-check <file>` | 7-dimension audit of your course design |
| Phase 4 — Designing unit activities | `/activity-design-ai-ready <unit>` | Generates 3–5 AI-ready activities per unit |
| Phase 5 — Building the concept map | `/concept-map-network <all course files>` | Generates a Mermaid concept network and gap analysis |

---

## 🎓 Design Engineering Fast Track

If you are working on the **B.Tech Design Engineering programme**, here is your specific reading order:

```
STEP 1: Read Course_Designer_Guidelines_Universal.md   (universal base rules)
    ↓
STEP 2: Read ext_Design_Engineering.md                 (Design Engineering overrides)
    ↓
STEP 3: Read COURSE_DESIGN_STANDARD.md                 (REVA quality standards)
    ↓
STEP 4: Read ASSESSMENT_QUALITY_STANDARD.md            (assessment rules)
    ↓
STEP 5: Draft your course (using Course_File_Template_DualLevel.md as template)
    ↓
STEP 6: Run /course-check on your draft
    ↓
STEP 7: Run /activity-design-ai-ready for each unit
```

Key differences to remember for Design Engineering:

| Standard Engineering | Design Engineering |
| :--- | :--- |
| IA-1 + IA-2 (written tests) | Crit 1 + Crit 2 (Jury Critique) |
| Question paper is the level mechanism | Rubric is the entire level mechanism |
| Code / report as portfolio artefact | Physical/digital artefact + process portfolio |
| CSCore placement competencies at awareness floor | Design process literacy at awareness floor |
| Studio courses: SC-Studio, SC-Fablab, SC-Digital | New course types specific to Design Engineering |

---

## ⚠️ The Most Common Newbie Mistakes

> [!WARNING]
> Avoid these errors that most first-time curriculum designers make:

1. **Writing COs using "understand" or "know"** — These are immeasurable. Use strong verbs: analyze, design, evaluate, construct, critique.
2. **Mapping every CO to every PO at Strength 3** — Unrealistic. Most COs should map to 2–3 POs at Strength 1 or 2. Strength 3 means it is the central focus of the course.
3. **Designing AI-trivial assessments** — If a student can submit an unmodified ChatGPT output, the assessment needs redesign. Add a localized constraint and a meta-cognitive reflection.
4. **Skipping the institutional threads** — IKS, sustainability, and liberal studies are not optional decorations. They must appear in at least one unit per course and ideally be rubric-visible.
5. **Designing Phase 3 before Phase 2 is approved** — Never design courses before the PO/PSO framework is finalized. Courses without a PO/PSO framework to map to are incomplete.
6. **Treating Design Engineering like a standard engineering programme** — Studio courses need rubrics, jury critiques, and process portfolios — not written exams and question papers.

---

*Roadmap Version: 1.0 | Created: June 17, 2026 | Maintained by: REVA Teaching-Learning Innovation Team*
*Based on: SrujanaSangama Repository — teaching-learning-reva plugin (June 2026)*
