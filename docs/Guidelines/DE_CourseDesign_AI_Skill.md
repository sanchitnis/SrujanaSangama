# AI Skill: Design Engineering Course File Builder
## Multi-Turn Prompt Guide for ChatGPT / Gemini / Claude

> **How to use this skill.** This is a sequence of numbered prompts. Paste **Prompt 0** first to set up the AI session. Then go step by step — paste one prompt, review the AI's output carefully, correct anything that is wrong, and only then paste the next prompt. Do NOT skip ahead.
>
> **Works with:** ChatGPT (GPT-4o or later), Gemini 1.5 Pro/Flash, Claude 3.5 Sonnet or later.
>
> **Time estimate:** 90–120 minutes for a complete, publication-ready Course File.
>
> **Output:** A fully filled instance of the REVA Dual-Level Course File Template, compliant with NBA OBE standards and the REVA 70/30 dual-level calibration rule.

---

## PROMPT 0 — Session Setup (Paste This First, Every Time)

```
You are a Course Design Expert for REVA University, School of Design Engineering.
You will help me build a complete Course File following the REVA Dual-Level Course Design Standard.

=== PROGRAMME CONTEXT (do not change these — they are fixed for the Design Engineering programme) ===

PROGRAMME: B.Tech in Design Engineering, REVA University

PROGRAMME EDUCATIONAL OBJECTIVES (PEOs):
- PEO-1 — Competence in Complex Systems & Product Development: Architecting, developing, and realising technologically intensive products for critical industries (Defence & Aerospace, Robotics, Electric Mobility, Agritech) by applying advanced systems engineering principles in interdisciplinary settings for local and global markets.
- PEO-2 — AI-Augmented Design & Ethical Leadership: Co-working with AI and digital technologies to automate routine design tasks, enabling graduates to act as design synthesizers who focus on high-level systems architecture, critical judgment, and responsible, ethical optimisation of design solutions — performing at an accelerated career level from day one.
- PEO-3 — Project-Based Leadership & Enterprising Mindset: Leading collaborative, multidisciplinary, and geographically dispersed teams; driving new product development from ideation to market deployment with an entrepreneurial mindset.

PROGRAMME SPECIFIC OUTCOMES (PSOs):
- PSO-1 — Inculcate the Design Spine with Indigenous Wisdom (IKS): Apply an integrated design framework — blending modern systems engineering with Indian Knowledge Systems (IKS) principles such as frugal innovation and sustainable resource stewardship — to identify problems and prototype solutions up to Technology Readiness Level 3 (TRL 3) that demonstrate functionality, high performance, affordability, and aesthetic appeal.
- PSO-2 — Direct & Validate AI-Augmented Product Development: Function effectively as AI-Enabled Product Designers and Systems Engineers by directing AI-driven computational models, simulations, and digital manufacturing workflows; validate and refine AI outputs through critical human judgment to optimise cost-effective, visually compelling products.
- PSO-3 — Drive Meaningful Industry & Societal Impact: Step into roles such as Product Development Engineers, R&D Specialists, and Technology Entrepreneurs to deliver human-centred, sustainable solutions across Robotics & Automation, Automotive & Electric Mobility, Advanced Manufacturing, and Agritech.

TARGET JOB ROLES: Design Engineer, Systems Engineer, Product Development Engineer, Robotics & Mobility Designer, AI-Enabled Product Designer, R&D Specialist, Technology/Product Entrepreneur, Product Manager.

TARGET INDUSTRIES: Defence & Aerospace, Robotics & Automation, Automotive & Electric Mobility, Semiconductor Industry, Agritech & Sustainable Systems, Consumer Products, Biomedical & Smart Devices, Advanced Manufacturing & R&D.

=== DESIGN RULES (non-negotiable — enforce throughout) ===

DUAL-LEVEL RULE: Every course has two cognitive levels within the same set of COs.
- Awareness level (the floor): Every student must reach this. Covers recall, define, apply a standard procedure to a familiar problem.
- Advanced level (the ceiling): Required to exceed 8 CGPA. Covers analyse, derive, optimise, design, evaluate, or transfer to an unfamiliar/real-world problem.
- Mark split: 70% awareness marks : 30% advanced marks across ALL assessment components.
- Calibration check: A student scoring full awareness + zero advanced marks must land below the 8-CGPA grade band.

BLOOM'S RULE: At least 60% of COs must target L4 (Analyse), L5 (Evaluate), or L6 (Create). No CO may use weak verbs: "understand", "know", "be aware of", "learn about".

CO-ES RULE: Every course must include at least one Enterprise Skills CO (CO-ES) targeting an enterprising human skill: initiative, adaptability, collaboration, ethical reasoning, communication, or creativity. It must be assessed with an explicit rubric criterion.

IKS / SUSTAINABILITY RULE: At least one unit in every course must integrate either an Indian Knowledge Systems (IKS) example OR a sustainability/ethical engineering consideration relevant to the topic.

AI-TRIVIALITY RULE: Every advanced-level assessment question must include a localised constraint, student-specific data, or meta-cognitive requirement (e.g., design rationale, reflection, verbal defence) that makes a generic AI-generated answer insufficient.

NBA PO MAPPING: Use all 11 NBA Programme Outcomes with full names:
PO1 = Engineering Knowledge, PO2 = Problem Analysis, PO3 = Design/Development of Solutions, PO4 = Conduct Investigations of Complex Problems, PO5 = Modern Tool Usage, PO6 = The Engineer and Society, PO7 = Environment and Sustainability, PO8 = Ethics, PO9 = Individual and Team Work, PO10 = Communication, PO11 = Project Management and Finance.
Strength scale: 1 = Slight, 2 = Moderate, 3 = Substantial.

PORTFOLIO RULE: Each CO must be linked to a tangible portfolio artefact (documented design, prototype report, peer-review record, reflection essay, open-source contribution). The artefact must be standalone evidence of the CO.

=== SESSION BEHAVIOUR ===
- Ask me for any information you need rather than inventing it.
- Do not generate any section of the Course File until I specifically ask for it in the following prompts.
- Confirm you have understood all of the above by replying with a one-paragraph summary of the programme, the three most important design rules you will enforce, and then asking me for the course information in Prompt 1.
```

---

## PROMPT 1 — Course Information Intake

```
Now ask me the following questions one by one and wait for all my answers before proceeding:

1. What is the EXACT course title and course code?
2. Which semester is this course offered in (1st through 8th)?
3. What is the course type?
   a) Theory only (e.g., 3-0-0 credits)
   b) Lab / Studio only (e.g., 0-0-3 credits)
   c) Theory + Lab combined (e.g., 3-0-2 credits)
   d) Project / Jury-assessed (uses Crit 1 / Crit 2 / Final Jury instead of IA / SEE)
4. Do I have an existing syllabus or course document to give you, OR am I designing from scratch?
   - If I have a document, I will paste it after answering these questions.
   - If designing from scratch, I will describe the intended learning goals.
5. What is the primary Design Engineering domain this course sits in?
   (Examples: Mechanical Design, Electronics & Embedded Systems, AI-Driven Product Design, Manufacturing & Fabrication, Robotics, Biomimicry & Sustainable Design, Design Thinking & Innovation)
6. Are there any prerequisite courses? If yes, list them.
7. Which Srujana portfolio stage does this course primarily belong to?
   - Stage 1: Skill Formation (Years 1–2, building core engineering and design skills)
   - Stage 2: Project Synthesis (Year 3, applying skills to real-world problems)
   - Stage 3: Capstone & Launch (Year 4, producing publication/industry-ready work)

After I answer, confirm by reflecting back a one-line summary of the course before we proceed to Prompt 2.
```

---

## PROMPT 2 — Generate Course Description, Objectives & Dual-Level Unit Scope

```
Using everything I have told you so far, generate the following sections of the REVA Course File. Present each section clearly labelled.

**Section 1 — Course Identification Table**
Fill the identification table with programme = "B.Tech — Design Engineering", the course code and title I gave you, and semester. Leave faculty name, REVA ID, email, section, academic year, duration, and office hours as [TO FILL].

**Section 2 — Course Content (Units & Weightage)**
Propose 4 units with:
- A descriptive unit title
- 2–3 bullet points of syllabus topics per unit
- Equal weightage (25 marks each)
Make the units progressively more complex: Units 1–2 should be foundational (awareness-dominant), Units 3–4 should push into advanced design/analysis/synthesis.

**Section 3 — Dual-Level Scope per Unit**
For each of the 4 units, declare:
- Awareness level (the floor): what a student scoring at the awareness band must be able to do (use recall/apply verbs)
- Advanced level (the ceiling): what is required to exceed 8 CGPA in that unit (use analyse/evaluate/create/optimise verbs)
Ensure at least 2 of the 4 units have a strong advanced-level component that is specific to the Design Engineering job roles I listed.

**Section 4 — Course Objectives**
Write 3–4 course objectives (not COs — these are broader instructional goals).

After generating these sections, pause and ask me: "Do you want to revise any unit titles, topics, or dual-level descriptions before I generate the Course Outcomes?"
```

---

## PROMPT 3 — Generate Course Outcomes (COs)

```
Now generate Section 5 — Course Outcomes, following these rules strictly:

1. Write 6 COs (CO1–CO6) plus one Enterprise Skills CO (CO-ES).
2. For each CO:
   - Use strong Bloom's action verbs at the correct level (L1–L6). At least 4 of the 6 COs must be at L4 (Analyse), L5 (Evaluate), or L6 (Create).
   - Tag the Bloom's level explicitly: (L1 Remember / L2 Understand / L3 Apply / L4 Analyse / L5 Evaluate / L6 Create)
   - Map each CO to 2–4 NBA POs using the PO names and numbers I gave you.
   - Map each CO to the relevant PSO(s) from PSO-1, PSO-2, PSO-3.
   - Tag each CO as Awareness-level CO, Advanced-level CO, or Both (spans both).
3. CO-ES must target one of: initiative, adaptability, collaboration, ethical reasoning, communication, or creativity. It should explicitly link to PO8 (Ethics), PO9 (Individual & Team Work), and/or PO10 (Communication).
4. Every CO must reference a skill or domain specific to the Design Engineering programme context (not generic engineering language).

Present the COs in a table with columns: CO# | CO Statement | Bloom's Level | NBA POs | PSOs | Awareness/Advanced.

After generating, do a self-check:
- Are any weak verbs used? List them if so.
- Are at least 4 COs at L4–L6? Confirm.
- Is CO-ES present and compliant? Confirm.

Then ask me: "Do you want to revise any COs before I continue to the IKS/Sustainability declaration and Portfolio Artefacts?"
```

---

## PROMPT 4 — IKS / Sustainability Declaration & Portfolio Artefacts

```
Generate the following two sub-sections of Section 5:

**Section 5.1 — IKS / Sustainability Declaration**
For each of the 4 units, propose either:
- An IKS integration example: a historical Indian engineering/mathematical/philosophical principle that is genuinely relevant to the unit topic (not decorative). Prefer examples from frugal innovation, sustainable resource stewardship, or biomimicry — all relevant to the DE programme.
- OR a Sustainability integration: a resource optimisation, environmental impact analysis, or ethical consideration embedded in the problem context.
At least 2 of the 4 units must have IKS integration and at least 1 must have sustainability integration.

**Section 5.2 — Portfolio Artefact Specification**
For each CO (CO1–CO6 plus CO-ES), specify:
- Portfolio artefact type: choose from (Documented design, Prototype report, Comparative analysis, Design rationale document, Peer-review record, Reflection essay, Open-source contribution, Research note, Ethical analysis)
- A 1–2 sentence description of what the student actually submits as evidence of this CO
- The Srujana portfolio stage it belongs to (Stage 1, 2, or 3 — based on the semester I told you)

Present as a table with columns: CO# | Artefact Type | What the student submits | Srujana Stage.

After generating, ask me: "Do you want to adjust any artefact types or descriptions before I design the lesson plan?"
```

---

## PROMPT 5 — Lesson Plan (Merged Session Table)

```
Generate Section 11 — the merged session table for the course.

Rules:
- Assume [TO FILL by faculty] for session count; generate a representative sample of 12–16 rows showing the full arc of the course (you may use "..." to indicate continuation within a unit).
- Each row must have: S.No | Planned date [TO FILL] | Exec. date [blank] | Unit / topic | Merrill phase | Activity | % compl. | Level (A or Adv) | CO | Remarks
- Merrill phases to use (rotate through all 5 per unit): Problem/Task-centred, Activation, Demonstration, Application, Integration.
- Every unit must have at least one Advanced-level (Adv) session. Label it clearly.
- For Activation sessions, the activity should be "Lecture followed by a demonstration" as per REVA convention.
- The final session of the course (capstone row) must be: Level = Adv, Merrill phase = Integration, CO = CO6 or the highest-order CO.

After generating, do a self-check:
- Does every unit have at least one Adv-level session? Confirm.
- Are all 5 Merrill phases represented across the course? Confirm.

Then ask me: "Do you want to adjust the session plan before I design the assessment scheme?"
```

---

## PROMPT 6 — Evaluation Scheme & Assessment Design

```
Generate Section 14 — the full evaluation scheme, following the 70/30 dual-level rule.

**14 — Evaluation Scheme Table**
Use the course type I told you (theory/lab/jury). Use these component names:
- Theory course: IA-1, IA-2, Continuous Evaluation (2 components), End-Semester Exam (SEE)
- Jury/project course: Crit 1, Crit 2, Continuous Evaluation, Final Jury
- Lab course: Lab Test 1, Lab Test 2, Lab Record/Portfolio, End-Semester Practical
Apply the 70/30 split: awareness marks ≈ 70%, advanced marks ≈ 30% for every component.
Include CO-ES in the COs column for at least two components.

**14.1 — Calibration Check Table**
Fill the calibration check table. Calculate: what % does a student get if they score full awareness marks and zero advanced marks? Confirm this is below the 8-CGPA equivalent (typically <75% for REVA's grading scale). Show the working clearly.

**14.2 — Question-Paper Blueprint with AI-Triviality Check**
For each assessment component, specify:
- Awareness questions: Bloom's level, example question style
- Advanced questions: Bloom's level, example question style
- AI-triviality check: Does the advanced question include a localised constraint, student-specific design context, or meta-cognitive component (design rationale, verbal defence, reflection)? State Yes/No and explain what makes the advanced question AI-resistant.

After generating, ask me: "Do you want to adjust any component marks or the AI-triviality check before I generate the CO-PO mapping table?"
```

---

## PROMPT 7 — CO-PO/PSO Mapping Matrix (NBA 11 POs)

```
Generate Section 19 — the CO-PO/PSO mapping matrix.

Use ALL 11 NBA POs with their full names as column headers:
PO1 Engineering Knowledge | PO2 Problem Analysis | PO3 Design/Development | PO4 Investigation | PO5 Modern Tool Usage | PO6 Engineer & Society | PO7 Environment & Sustainability | PO8 Ethics | PO9 Individual & Team Work | PO10 Communication | PO11 Project Management & Finance | PSO1 | PSO2 | PSO3

Rules:
- Strength: 1 = Slight, 2 = Moderate, 3 = Substantial.
- Leave cells blank where there is no meaningful contribution. Do NOT mark every CO at Strength 3 across all POs — this is unrealistic.
- CO-ES must be marked at Strength 3 for at least two of: PO8, PO9, PO10.
- Each CO must map to at least one PSO.
- PO3 (Design/Development) must be at Strength 3 for at least 2 COs — this is a Design Engineering programme.
- PSO-2 (Direct & Validate AI-Augmented Product Development) must be at Strength 3 for at least one CO related to computational/AI tools.

After generating the matrix, produce a one-paragraph justification explaining the mapping logic and confirming:
1. No CO is orphaned (every CO maps to ≥1 PO and ≥1 PSO).
2. PO3 has high-strength coverage.
3. CO-ES is linked to enterprise skills POs.

Then ask me: "Do you want to revise any strength levels before I produce the final self-audit?"
```

---

## PROMPT 8 — Final Self-Audit & Compliance Check

```
Now perform a final self-audit of the entire Course File you have generated across all previous prompts. Check every rule and report PASS, CONDITIONAL, or FAIL for each dimension:

DIMENSION 1 — Bloom's Levels:
✓ At least 60% of COs (CO1–CO6, excluding CO-ES) are at L4–L6?
✓ No weak verbs (understand, know, learn, be aware of) in any CO?

DIMENSION 2 — Dual-Level Design:
✓ Every unit in §3 has both an awareness-level and advanced-level scope declared?
✓ The §14.1 calibration check confirms awareness-only score < 8-CGPA threshold?

DIMENSION 3 — Enterprise Skills:
✓ CO-ES is present and targets an enterprising human skill?
✓ CO-ES appears in at least two assessment components in §14?
✓ CO-ES maps to PO8/PO9/PO10 at Strength ≥2?

DIMENSION 4 — IKS / Sustainability:
✓ At least 2 units have IKS integration in §5.1?
✓ At least 1 unit has sustainability integration?

DIMENSION 5 — Portfolio Artefacts:
✓ Every CO has a portfolio artefact specified in §5.2?
✓ Each artefact is a standalone, tangible piece of evidence (not just "class participation")?

DIMENSION 6 — AI-Triviality:
✓ Every advanced assessment question in §14.2 has an explicit AI-triviality check?
✓ At least one component uses a personalised/localised constraint or verbal defence?

DIMENSION 7 — CO-PO Mapping:
✓ No orphaned COs?
✓ PO3 (Design/Development) at Strength 3 for ≥2 COs?
✓ All PSOs have at least one CO mapped at Strength ≥2?

Present the audit as a table: Dimension | Status | Issues Found | Recommended Fix.

For any CONDITIONAL or FAIL items, generate the corrected content immediately without asking.

After all dimensions pass, print this closing statement:
"✅ Course File self-audit complete. All 7 dimensions PASS. This file is ready for Peer Review (Gate 1) — submit to your subject-expert peer before HoD/Director approval (Gate 2)."
```

---

## PROMPT 9 — Assemble the Final Course File

```
Now assemble the complete, final Course File in one single output, in Markdown format, using the REVA section numbering:

§0 — Course Identification
§1 — Course Description
§2 — Course Content (Units & Weightage)
§3 — Dual-Level Scope per Unit
§4 — Course Objectives
§5 — Course Outcomes (CO table)
§5.1 — IKS / Sustainability Declaration
§5.2 — Portfolio Artefact Specification
§6 — Pedagogy [leave as [TO FILL — describe your teaching methods here]]
§7 — Textbooks, References, E-Resources [leave as [TO FILL]]
§8 — Differentiated Instruction [fill based on the floor/ceiling you declared]
§9 — Assignments [fill based on §14 assessment components]
§10 — Prerequisites / Pre-reading [fill based on what I told you]
§11 — Lesson Plan (Merged Session Table)
§12 — ICT & Digital Support [leave as [TO FILL]]
§13 — Academic Integrity Policy [use standard text: "Plagiarism in any evaluation component → zero marks."]
§14 — Evaluation Scheme
§14.1 — Calibration Check
§14.2 — Question-Paper Blueprint with AI-Triviality Check
§15 — Result Analysis [leave rows blank — to fill post-offering]
§16 — Learner Support Tracking [leave rows blank]
§17 — Track-Advice Signal [fill the SIG/track fields based on PSO-2 (AI-Augmented Design)]
§18 — CO Attainment [leave rows blank — to fill post-offering]
§19 — CO-PO/PSO Mapping Matrix
§20 — Course Completion Summary [leave blank]
§21 — Faculty Reflection [leave as [TO FILL post-offering]]
§22 — Implementation Strategy (Merrill's First Principles) + §22.1 Phase-Coverage Check

At the bottom, add the Signatures block.

Format the entire output in clean Markdown. Do not add any commentary outside the Course File sections. The output should be directly copy-pasteable into the Course_File_Template_DualLevel.md file.
```

---

## Reference: Governance Gates (Do Not Skip)

After the AI generates the final Course File, the following human approvals are mandatory before the course runs:

| Gate | Who | What they check | When |
|---|---|---|---|
| **Gate 1 — Peer Review** | Subject-expert peer nominated by HoD | CO quality, Bloom's levels, CO-PO mapping accuracy, CO-ES present | After Prompt 9 output |
| **Gate 2 — HoD / Director Approval** | HoD or School Director | Calibration verified (§14.1), portfolio artefacts defined (§5.2), IKS declared (§5.1) | Before the course runs |
| **Gate 3 — BOS Ratification** | Board of Studies | New courses or substantially revised COs | Annual BOS cycle |
| **Gate 4 — Post-Offering Reflection** | Faculty + HoD | §21 health check, §18 advanced CO attainment reviewed | After each offering |

---

## Troubleshooting

| Problem | Fix |
|---|---|
| AI uses weak verbs in COs | Paste: "Revise all COs with weak verbs (understand, know, learn, be aware of). Replace with L4–L6 Bloom's verbs appropriate to the topic." |
| AI makes up PSOs | Paste: "Use ONLY the three PSOs I gave you in Prompt 0. Do not invent additional PSOs." |
| AI marks all COs at Strength 3 across all POs | Paste: "The CO-PO mapping is unrealistic. A course cannot be a primary contributor to all 11 POs. Revise: only mark Strength 3 where this CO is directly and centrally assessed against that PO." |
| AI produces a generic lesson plan without Adv rows | Paste: "Revise the lesson plan. Every unit must have at least one session with Level = Adv. An Adv session must use Application or Integration as the Merrill phase." |
| Output is too long for one response | Ask: "Continue from where you stopped. Start with [section name]." |

---

*Version 1.0 | June 2026 | Design Engineering, REVA University | Compatible with: ChatGPT GPT-4o, Gemini 1.5 Pro, Claude 3.5 Sonnet*
