# Course Designer Guidelines — University Edition (2026 Scheme)

> **Who this is for.** Faculty and School design teams designing or revising any course across all REVA University programmes — B.Tech, B.Sc, B.Des, BBA, MBA, M.Tech, and allied programmes.
>
> **What it does.** It translates the REVA Curriculum Design Framework v2.0 into concrete design rules, organized by **course category** and **L-T-P pattern** — because a 3-0-0 theory foundation course and a 0-0-2 studio/workshop need very different designs. Use the decision table in §2 to find your course type, then follow the rules for that type **plus** the universal rules in §1.
>
> **Programme-specific extensions.** Certain programmes have sufficiently distinct pedagogical models that additional rules apply on top of these universal guidelines. Refer to your programme extension document:
> - B.Tech CSE / ISE / IT / AIML / AIDS / IoT / Cyber Security → `ext_CSE_ISE_IT.md`
> - B.Tech Design Engineering → `ext_Design_Engineering.md`
> - B.Sc / Engineering Sciences → `ext_Sciences.md`
> - Management Programmes → `ext_Management.md`
>
> **Companion document.** Every course produces a Course File using the *Course File Template — Dual-Level (Universal)*. These guidelines tell you how to **design** the course; the template tells you how to **document** it.

---

## 0. Two decisions that must already be fixed before you start

These are **programme-level** decisions, made once centrally per school — not by individual designers. Confirm they exist before designing assessment:

1. **The official awareness/advanced mark ratio.** Each school computes, against REVA's marks-to-grade-point conversion, the split that makes an awareness-only student land **below the 8-CGPA band**. Every theory/integrated course in that school uses this single fixed ratio (illustratively ~70/30). Do **not** invent your own.
2. **A filled reference exemplar.** Each school circulates one fully designed course (scope table + assessment split) as the calibration standard for that programme domain, so "advanced level" means the same thing across courses. *Note: one exemplar per school, not one institution-wide — a Design Engineering ceiling differs from a CSE ceiling.*

If either is missing, flag it — designing assessment without them will break the cross-course consistency the CGPA signal depends on.

---

## 1. Universal rules (every course, every programme, every school)

1. **Outcome-first.** Write Course Outcomes (COs) before content. Each CO maps to PO/PSO (NBA 11 POs, updated framework) and is tagged with a **Bloom taxonomy level** (Remember / Understand / Apply / Analyse / Evaluate / Create). Remember–Apply = awareness floor; Analyse–Create = advanced ceiling.

2. **Two levels in one course.** Never stream students into sections. Design one course delivered at an **awareness floor** (every student must clear it) and an **advanced ceiling** (depth for the strong), separated by **assessment**, anchored to Bloom verbs (floor = Remember/Understand/Apply; ceiling = Analyze/Evaluate/Create).

3. **The floor protects professional readiness.** Awareness-level content must map to the **Programme Core competencies** the course is responsible for (defined per school in the programme extension document). State that mapping explicitly.

4. **Currency.** Content reflects industry-, profession-, and future-role-aligned needs and is reviewed every cycle. Perishable tool/tech specifics belong in workshops, labs, and studios — not frozen into theory syllabi.

5. **Continuous assessment.** Favor frequent low-stakes assessment over a single high-stakes exam, especially for the at-risk majority.

6. **Honest contact-hour budgeting.** Design to the real contact hours implied by L-T-P (see §3), not to an idealized self-study assumption — most of the cohort will not self-study.

7. **Differentiated support is mandatory, not optional.** Every course design names both a **remediation path** (reach the floor) and an **enrichment path** (reach the ceiling).

8. **Academic integrity & accessibility.** Design assessments resistant to trivial AI-completion where the CO is about the student's own competence; design for the diversity of the REVA intake by never assuming unstated prior exposure.

9. **Enterprise Human Skills — embedded, not a separate CO.** Enterprise human skills (Initiative, Adaptability, Collaboration, Ethical Reasoning, Communication, Creativity & Value Creation) are addressed through **CO-PO mapping** — they do not require a dedicated standalone CO. However, their presence must be made **explicit** in two places:
    - **Course Overview**: state which enterprise skills the course develops and through which topics or activities.
    - **Assignment & Activity Design**: at least one assignment or activity per course must be explicitly designed to surface and assess an enterprise skill, with an observable rubric criterion. Generic activity briefs that happen to involve teamwork but do not name or assess the skill do not satisfy this requirement.

10. **IKS / Sustainability / Liberal Studies — encouraged integration.** Course designers are strongly encouraged to connect their course to at least one of the following where it fits naturally:
    - **Indian Knowledge Systems (IKS)**: historical Indian achievements, local case studies, Indian philosophical perspectives relevant to the domain.
    - **Sustainability**: resource optimization, environmental responsibility, community wellbeing, circular economy thinking.
    - **Liberal Studies connection**: ethics, design thinking, communication, creative disciplines, interdisciplinary perspectives.
    Where integrated, it should be visible in the lesson plan and, where possible, rubric-assessed. *This is a quality nudge, not a gate — forced or tokenistic integration is worse than none.*

11. **Portfolio Artefact (mandatory).** Every course must produce at least one tangible, CO-linked **portfolio artefact** — a deliverable that serves as evidence of competence beyond an exam score. This artefact must be: named and described in the Course File; linked to specific COs; rubric-graded; integrated into the CIA cycle (minimum 15% of course marks). *Acceptable types: documented solution, design prototype, research analysis, computational model, reflective narrative, open-source contribution, exhibition piece — domain-appropriate.*

---

## 2. Find your course type

| Category code | Meaning | Typical L-T-P | Go to |
|---|---|---|---|
| FC | Foundation Course (math, science, humanities, management) | 3-0-0, 2-1-0, 1-0-0 | §4.1 |
| HC (theory) | Hard Core programme theory | 3-0-0, 2-1-0 | §4.2 |
| HC (integrated) | Hard Core theory + embedded lab/studio | 1-1-1, 2-0-1 | §4.3 |
| HC / standalone lab | Practical-only lab | 0-0-1 | §4.4 |
| W1–W8 | Workshop / Studio Workshop (just-in-time, SIG/Studio-designed) | 0-0-2 | §4.5 |
| SC / PEC | Soft Core / Professional Elective (specialisation track) | 3-0-0 | §4.6 |
| OE | Open Elective (cross-discipline) | 3-0-0 | §4.7 |
| ETC | Emerging Technology Course | 1-0-0 | §4.8 |
| MC | Mandatory Course (non-credit / 0-credit) | 0-0-0, 1-0-0 | §4.9 |
| AEC | Ability Enhancement (professional readiness) | 0-0-1 | §4.10 |
| Proj | Mini / Capstone Project | 0-0-2 to 0-0-8 | §4.11 |
| Intern | Internship / Field Placement | 0-0-4 | §4.12 |

> **Programme-specific additions.** Some programmes define additional category codes not in this table (e.g., SC-Studio, SC-Fablab for Design Engineering). These are defined in the relevant programme extension document.

---

## 3. How to read L-T-P (and what each implies)

**L = Lecture, T = Tutorial, P = Practical/Studio.** 1 credit ≈ 1 lecture hour, 1 tutorial hour, or 2 practical hours per week.

| Pattern | Reads as | Design implication |
|---|---|---|
| 3-0-0 | Pure theory | Conceptual mastery; advanced level lives in analysis/derivation questions, not lab or studio work. |
| 2-1-0 | Theory + tutorial | Use the tutorial hour for guided problem-solving — your best lever for carrying the floor cohort. |
| 1-1-1 | Integrated theory-lab | Theory and practice interleave; the lab/studio component is where advanced students build real artefacts. |
| 2-0-1 / 0-0-1 | Theory-light + lab / pure lab | Assessment is demonstration-based; rubric, not written exam, carries the level distinction. |
| 0-0-2 | Workshop / studio / heavy practical | No formal lecture; entirely doing. Currency and just-in-time design dominate. |
| 0-0-4 … 0-0-8 | Project / internship / field placement | Deliverable-graded; the level distinction is contributor-grade vs owner-grade work. |

> **Golden rule:** the higher the P, the more the level distinction must live in a **rubric** rather than a **question paper**.

---

## 4. Rules by course type

### 4.1 Foundation Course (FC) — e.g. Calculus, Probability, Physics, Communicative English, Design Thinking

- These carry the heaviest **intake-diversity** risk: students often arrive with the widest prior-knowledge gaps here.
- **Awareness floor:** the foundational fluency every downstream course assumes. Make it genuinely reachable from a no-prior-exposure start — include a week-0 / bridge ramp where the gap is real.
- **Advanced ceiling:** application to programme-relevant problems, not just textbook computation or generic exercises.
- Use the **tutorial hour** (if T≥1) for remediation and worked examples; do not lecture into it.
- Continuous assessment essential — Foundation Courses are where at-risk students disengage earliest.
- IKS integration is especially natural here: foundational knowledge in most domains has Indian heritage worth surfacing.

### 4.2 Hard Core theory (HC, 3-0-0 / 2-1-0) — e.g. DBMS, Thermodynamics, Structural Analysis, Marketing Management

- The backbone of programme professional readiness. Awareness floor **must** map to the Programme Core competencies defined by the school.
- **Awareness floor:** define, explain, apply standard procedures to familiar problems.
- **Advanced ceiling:** compare/justify design or analytical choices, analyze complexity/trade-offs, solve novel problems.
- Apply the **fixed awareness/advanced mark ratio** (§0.1). Verify in the Course File that awareness-only < 8 CGPA.
- Blueprint every IA and the SEE so advanced questions are present and identifiable.

### 4.3 Hard Core integrated (HC, 1-1-1 / 2-0-1) — e.g. DSA, Design & Analysis of Algorithms, Materials & Manufacturing

- The **lab/studio/practical credit is not decoration** — it is where advanced students demonstrate the ceiling.
- Split assessment across both modes: written (concept floor + analysis ceiling) **and** practical/studio (implement floor + optimize/design/create ceiling).
- Map practical tasks to real, current tooling or methods; refresh each cycle without changing the conceptual CO.
- Rubric for the practical component must distinguish *works / meets brief* (floor) from *efficient / scalable / well-reasoned / innovative* (ceiling).

### 4.4 Standalone lab (HC, 0-0-1)

- Pure demonstration of skill. No written-exam ceiling — the **rubric is the entire level mechanism**.
- Define observable floor criteria (task completes correctly / meets brief) and ceiling criteria (handles edge cases, optimizes, explains choices, shows judgment).
- Keep lab sheets or studio briefs current; this is a low-cost place to inject recent tools or methods.

### 4.5 Workshop (W1–W8, 0-0-2) — School/SIG/Studio-owned, just-in-time

- **Titles in the scheme are indicative placeholders.** School/SIG/Studio teams design the actual content just-in-time so it reflects the technology, industry, or design landscape at the moment students take it.
- Design for **doing**, not lecturing: a workshop with a lecture component is mis-designed.
- Currency is the whole point — tie each offering to live professional needs (job postings, industry briefs, design competitions, field challenges) and re-author each cycle.
- Assessment is artefact + demonstration. Floor = a working deliverable; ceiling = a deliverable that shows judgment, extension, or production/exhibition readiness.
- Document the just-in-time rationale so the School/SIG can show why this offering, this cycle.

### 4.6 Soft Core / Professional Elective (SC/PEC, 3-0-0) — School Specialisation Track courses

- These are the **specialisation tracks** of each school and programme. They are owned end-to-end by a School Specialisation Group (SIG, Studio, or equivalent community of practice) as a community of practice.
- Design the elective as one coherent sequence with the school's workshops, projects, and internship/field placement — not a standalone course.
- Aligned to professional/recruiter/industry needs; expect to revise content faster than HC theory.
- Advanced ceiling here is closer to **professional contributor competence** than to exam performance — assess accordingly.
- *For programme-specific specialisation track definitions, refer to your programme extension document.*

### 4.7 Open Elective (OE, 3-0-0)

- Taken by students **from other programmes** — do **not** assume the home programme's prerequisites.
- Awareness floor must be reachable by a non-specialist; ceiling can reward those who connect it to their home discipline.
- Self-contained; no dependency on this programme's HC chain.
- Especially valuable for IKS and liberal studies integration — cross-disciplinary perspective is the point.

### 4.8 Emerging Technology / Domain Course (ETC, 1-0-0)

- Light-credit, awareness-raising by nature. The goal is **literacy and motivation**, not mastery.
- Strategic role: early exposure that converts passive learners by showing where the progression path leads.
- Keep it current and inspiring; assess by engagement/short artefact, not heavy exams.
- Do not over-engineer a dual-level split into a 1-credit literacy course — floor-only is acceptable here, stated explicitly.

### 4.9 Mandatory Course (MC, 0-credit) — Constitution & Cyber Law, Environmental Science, IKS, etc.

- Non-CGPA but required. Design for **completion and awareness**, not differentiation.
- No awareness/advanced split needed; a single competency floor with pass/complete grading.
- Keep assessment light and integrity-focused.

### 4.10 Ability Enhancement (AEC, 0-0-1) — Professional Readiness, every semester

- The **Programme Core professional readiness** made explicit — steady practice across semesters, not a final-year crash.
- Align tightly and continuously to current professional entry requirements for the programme's graduate roles (which shift as industry and AI change hiring and practice).
- Floor = clears the professional readiness bar; track readiness per student and feed weak signals to academic mentors.
- Continuous, low-stakes, frequent.
- *For domain-specific professional readiness definitions, refer to your programme extension document.*

### 4.11 Project (Proj, 0-0-2 → 0-0-8) — Mini Project, Capstone Phase I/II

- The progression ladder: Mini 1 → Mini 2 → Capstone I → Capstone II, with credits rising to make room for doing.
- **Level distinction = deliverable grade, not exam.** Define two rubric heights on the same brief:
  - **Contributor-grade** (team-based, employment/practice-oriented) — clears the floor.
  - **Owner-grade** (product-shipping / design-ready / publication-ready / venture-launching) — reaches the ceiling.
- Same rubric, different ceilings — never different briefs that pre-label students.
- Capstone may **be** a venture, exhibition, publication, or commissioned work for students on an entrepreneurship or professional exit track.
- Briefs owned by the School/SIG and kept aligned to professional/industry/design community needs.
- Portfolio artefact from each project phase must be explicitly defined and rubric-graded.

### 4.12 Internship / Field Placement (Intern, 0-0-4)

- School-brokered where possible; quality of placement is the primary design variable.
- Assess by supervisor evaluation + reflective artefact mapped to COs.
- Floor = credible contribution and professional conduct; ceiling = ownership of a real deliverable or design outcome.
- Feed internship performance back to the School Specialisation Group and to academic mentors.

---

## 5. Design checklist (run before submitting any course)

- [ ] COs written first, each tagged with a **Bloom taxonomy level** (Remember / Understand / Apply / Analyse / Evaluate / Create), mapped to NBA 11 POs/PSOs.
- [ ] Awareness floor explicitly mapped to **Programme Core competencies** (defined in your programme extension).
- [ ] Advanced ceiling defined per unit using Bloom anchor; consistent with the **school reference exemplar**.
- [ ] **Enterprise Skills declared in Course Overview**: which skills the course develops and through which activities — stated explicitly (not implied).
- [ ] **Enterprise Skills visible in at least one assignment/activity**: brief names the skill; rubric includes an observable criterion for it.
- [ ] **IKS / Sustainability / Liberal Studies thread**: at least one unit-level integration point documented in the lesson plan.
- [ ] **Portfolio Artefact defined**: named, CO-linked, rubric-graded, integrated into CIA (≥15% of marks).
- [ ] For theory/integrated: official awareness/advanced **mark ratio applied** and the *awareness-only < 8 CGPA* check passes.
- [ ] For high-P courses: level distinction lives in a **rubric**, not a question paper.
- [ ] Remediation path (to floor) **and** enrichment path (to ceiling) both named.
- [ ] Content currency: perishable tooling/methods in labs/workshops/studios; review cycle noted.
- [ ] Intake-aware: no unstated prior-exposure assumption; bridge ramp where the gap is real.
- [ ] For SC/W/Proj/Intern: ownership sits with a School Specialisation Group and links to its track.
- [ ] **AI-augmented assessment (mandatory — at least 1 per course)**: at least one assignment or activity per course must be explicitly designed as an **AI-assisted task**, where:
  - Students are **required** to use an AI tool as part of completing the task (not optional, not prohibited).
  - The scope is **challenging enough** that AI output alone is insufficient — the task requires the student's own judgment, domain knowledge, contextual reasoning, or critical evaluation to produce a complete and credible response.
  - The submission must include a mandatory **AI Use Declaration** stating: which AI tool(s) were used, what prompts or queries were submitted, how the AI output was used or modified, and what the student contributed beyond the AI's response.
- [ ] Track-advice signal defined for prerequisite courses feeding specialisation selection.

---

## 6. Quick reference — what carries the "level" distinction by L-T-P

| L-T-P shape | Floor shown by | Ceiling shown by | Level mechanism |
|---|---|---|---|
| 3-0-0 | Standard-case written answers | Analysis / novel-problem written answers | Question paper |
| 2-1-0 | Tutorial problem-solving | Harder tutorial / open problems | Question paper + tutorial |
| 1-1-1 / 2-0-1 | Concept recall + working output | Trade-off analysis + optimized / innovative design | Paper **and** rubric |
| 0-0-1 / 0-0-2 | Task completes / brief met | Edge-cases / optimization / judgment / design innovation | Rubric only |
| 0-0-4…0-0-8 | Contributor-grade deliverable | Owner-grade / shipped / exhibited / published | Rubric only |
| 1-0-0 (ETC) | Literacy + engagement | (floor-only acceptable) | Light artefact |
| 0-credit (MC) | Completion | (none) | Pass/complete |

---

## 7. Enterprise Human Skills — Design Guide

Enterprise human skills are skills AI cannot perform autonomously and that every graduate needs regardless of school or programme. They are addressed through **CO-PO mapping** (no separate CO required), but must be **named explicitly** in the course overview and **designed into** at least one assignment or activity with a rubric criterion.

### 7.1 PO-to-Skills Mapping Reference (NBA 11 POs)

Use this table to identify which enterprise skills your course naturally develops, how to design assessments and activities that surface them, and how to calibrate CO-PO mapping strength (1 = Low, 2 = Medium, 3 = High).

---

#### PO1: Engineering Knowledge
**Skills mapped:** Engineering knowledge · Computational thinking · Digital literacy · AI literacy · Data literacy · Curiosity · Scientific mindset

**How to achieve through course design:** Connect mathematics, science, computing and engineering fundamentals to real applications. Use concept application tasks, numerical problems, coding exercises, simulations, AI-assisted learning tasks and tool-based demonstrations. Assess whether students can use core engineering knowledge to explain, calculate, model or solve technical problems.

| Mapping Strength | What it means | Example |
|---|---|---|
| **Low (1)** | CO introduces basic concepts or terminology | Define AI, sensors, algorithms or engineering terms |
| **Medium (2)** | CO requires application of concepts in problems or labs | Solve numerical problems or write simple code using engineering principles |
| **High (3)** | CO requires integration of mathematics, science, computing and engineering knowledge to solve complex problems | Design and justify a working technical solution using calculations, coding, simulation and engineering reasoning |

---

#### PO2: Problem Analysis
**Skills mapped:** Critical thinking · Complex problem solving · Decision-making · Data-centric thinking · Research literacy · Systems thinking · Information literacy · Ambiguity handling

**How to achieve through course design:** Train students to identify, formulate and analyse problems before solving them. Use problem-tree analysis, root cause analysis, stakeholder mapping, case study analysis, literature review, data interpretation and assumption testing. Assess whether students can define the real problem, analyse causes, use evidence and reach justified conclusions.

| Mapping Strength | What it means | Example |
|---|---|---|
| **Low (1)** | CO asks students to recognise or describe a problem | Identify the problem in a given case |
| **Medium (2)** | CO asks students to analyse causes, data or constraints | Analyse causes of failure using data or a fishbone diagram |
| **High (3)** | CO asks students to formulate a complex problem, review evidence and justify conclusions | Prepare a full problem analysis report with literature review, stakeholder analysis, assumptions, constraints and justified conclusions |

---

#### PO3: Design / Development of Solutions
**Skills mapped:** Creativity · Innovation · Design thinking · User empathy · Product thinking · Sustainability literacy · Entrepreneurial opportunity recognition · Courage to experiment

**How to achieve through course design:** Include open-ended design challenges, user need identification, ideation, prototyping, testing and iteration. Use design thinking workshops, CAD modelling, product sketches, prototype building, sustainability review, whole-life cost analysis and user feedback. Focus assessment on creativity, feasibility, safety, sustainability and improvement through iteration.

| Mapping Strength | What it means | Example |
|---|---|---|
| **Low (1)** | CO exposes students to design principles or examples | Explain the stages of design thinking |
| **Medium (2)** | CO requires students to create a guided design or prototype | Create a prototype based on a given problem statement |
| **High (3)** | CO requires students to design, develop, test and improve a solution for a complex contextual problem | Develop a tested solution considering user needs, safety, cost, sustainability, culture, society and environment |

---

#### PO4: Conduct Investigations of Complex Problems
**Skills mapped:** Scientific mindset · Curiosity · Experimentation · Evidence-based reasoning · Data literacy · Modelling · Statistical thinking · Research discipline · Intellectual honesty

**How to achieve through course design:** Have students conduct experiments, collect data, model systems, analyse results and interpret findings. Use lab investigations, hypothesis testing, simulation studies, field observations, data analysis, validation tasks and research mini-projects. Test the ability to design investigations, handle data responsibly and draw valid conclusions.

| Mapping Strength | What it means | Example |
|---|---|---|
| **Low (1)** | CO introduces experimental or research methods | Describe steps in an experiment |
| **Medium (2)** | CO requires students to conduct guided experiments and interpret results | Conduct a lab experiment and prepare a result table |
| **High (3)** | CO requires independent investigation, modelling, data analysis and evidence-based conclusions | Design an experiment, collect data, analyse errors, interpret results and defend conclusions |

---

#### PO5: Engineering Tool Usage
**Skills mapped:** Modern tool usage · AI tool usage · Digital literacy · Prompt engineering · Simulation skills · Modelling · Automation · Cybersecurity awareness · Tool judgement

**How to achieve through course design:** Expose students to relevant engineering, IT, AI, data, simulation, modelling and documentation tools. Use CAD, programming, simulation, AI-assisted coding, data dashboards, version control, digital fabrication and cybersecurity basics. Assess whether students can choose suitable tools, use them effectively and recognise limitations.

| Mapping Strength | What it means | Example |
|---|---|---|
| **Low (1)** | CO introduces a tool or demonstrates its basic use | Identify uses of CAD, Python, AI tools or simulation software |
| **Medium (2)** | CO requires students to apply tools in guided tasks | Use a tool to complete a lab or assignment |
| **High (3)** | CO requires students to independently select, apply, compare and justify tools for complex engineering work | Select and use multiple tools to model, simulate, build, analyse and document a working solution |

---

#### PO6: The Engineer and the World
**Skills mapped:** Citizenship · Making a difference · Sustainability literacy · Cultural literacy · Community-based learning · Environmental awareness · Legal awareness · Social responsibility · Systems thinking

**How to achieve through course design:** Connect engineering decisions with society, environment, economy, health, safety, law, culture and sustainability. Use community problem identification, sustainability audits, life-cycle analysis, social impact studies, accessibility reviews and field-based projects. Assess whether students can evaluate the broader consequences of engineering solutions.

| Mapping Strength | What it means | Example |
|---|---|---|
| **Low (1)** | CO mentions social, environmental or legal aspects | List environmental impacts of a technology |
| **Medium (2)** | CO asks students to analyse impact in a structured activity | Analyse the social and environmental impact of a case study |
| **High (3)** | CO requires students to integrate societal, environmental, economic and legal considerations into solution design | Design a solution for a real community problem with sustainability, safety, cost, legal and cultural considerations |

---

#### PO7: Ethics
**Skills mapped:** Character · Universal human values · Professional ethics · Responsible AI · Privacy awareness · Fairness · Inclusion · Academic integrity · Diversity · Legal compliance

**How to achieve through course design:** Embed ethics into assignments, projects, AI usage, teamwork, fieldwork and reporting. Use ethical dilemma discussions, AI-use declarations, plagiarism awareness, data privacy cases, inclusive design reviews and professional conduct reflection. Evaluate judgement, accountability and responsible decision-making.

| Mapping Strength | What it means | Example |
|---|---|---|
| **Low (1)** | CO introduces ethical principles or human values | Define plagiarism, privacy or professional ethics |
| **Medium (2)** | CO requires students to analyse ethical issues in cases | Analyse an ethical dilemma involving AI, safety or data use |
| **High (3)** | CO requires students to apply ethics, inclusion, legal compliance and responsible AI principles in actual project decisions | Submit a project with consent forms, AI-use declaration, bias check, safety review and ethical justification |

---

#### PO8: Individual and Collaborative Teamwork
**Skills mapped:** Collaboration · Teamwork · Leadership · Self-management · Commitment · Conscientiousness · Emotional intelligence · Conflict resolution · Interdisciplinary work

**How to achieve through course design:** Include individual accountability and team-based work. Use team projects, role rotation, peer review, sprint planning, meeting minutes, group presentations, conflict resolution tasks and leadership opportunities. Include both product outcome and team process evidence in assessment.

| Mapping Strength | What it means | Example |
|---|---|---|
| **Low (1)** | CO includes participation in group activities | Participate in a group discussion |
| **Medium (2)** | CO requires students to work in teams with assigned roles | Complete a team assignment with defined roles |
| **High (3)** | CO assesses individual contribution, leadership, collaboration, conflict handling and multidisciplinary team output | Lead or contribute to a multidisciplinary project with peer evaluation, task logs, role rotation and final team deliverable |

---

#### PO9: Communication
**Skills mapped:** Communication · Self-expression · Media literacy · Technical writing · Storytelling · Presentation skills · Documentation · Visual communication · Inclusive communication

**How to achieve through course design:** Have students communicate technical ideas in written, oral, visual and digital formats. Use report writing, presentations, posters, pitch decks, demo videos, technical documentation, user manuals, blogs and peer teaching. Assess clarity, structure, evidence, audience awareness, inclusivity and professional formatting.

| Mapping Strength | What it means | Example |
|---|---|---|
| **Low (1)** | CO requires basic explanation or short written responses | Write short answers or explain a concept orally |
| **Medium (2)** | CO requires structured reports, presentations or documentation | Prepare a lab report or class presentation |
| **High (3)** | CO requires professional communication to technical and non-technical audiences with inclusive and well-supported documentation | Present a project with report, design documentation, poster, demo video and audience-specific explanation |

---

#### PO10: Project Management and Finance
**Skills mapped:** Entrepreneurial courage · Project planning · Budgeting · Financial literacy · Resource management · Risk management · Decision-making · Product ownership · Execution discipline

**How to achieve through course design:** Include planning, scheduling, costing and resource management. Use project charters, Gantt charts, bill of materials, budget sheets, risk registers, cost-benefit analysis, business model canvas, procurement planning and product pitching. Evaluate whether students can manage time, cost, people, resources and risks.

| Mapping Strength | What it means | Example |
|---|---|---|
| **Low (1)** | CO introduces project management or finance concepts | Define Gantt chart, budget or risk |
| **Medium (2)** | CO requires students to prepare plans, budgets or risk analysis for guided tasks | Prepare a project plan and estimated budget |
| **High (3)** | CO requires students to manage a complete project with timeline, budget, risk, resources and economic justification | Execute a project with timeline tracking, cost sheet, procurement decisions, risk mitigation and final financial justification |

---

#### PO11: Life-Long Learning
**Skills mapped:** Lifelong learning · Adaptability · Resilience · Curiosity · Career agility · Self-directed learning · Metacognition · Personal knowledge management · Future readiness

**How to achieve through course design:** Encourage students to learn beyond the syllabus and reflect on their growth. Use learning journals, skill audits, independent mini-projects, certification tasks, technology trend reviews, reflective portfolios and self-learning plans. Evaluate the student's ability to identify learning gaps, learn independently and adapt to emerging technologies.

| Mapping Strength | What it means | Example |
|---|---|---|
| **Low (1)** | CO encourages awareness of new technologies or learning needs | Write a note on emerging technologies |
| **Medium (2)** | CO requires students to explore and report on new tools, trends or skills | Complete a self-learning assignment on a new tool |
| **High (3)** | CO requires independent learning, application of a new tool or technology and reflective evidence of growth | Learn an unfamiliar tool independently, apply it in a project and submit a reflective learning portfolio |

---

### 7.2 How to declare enterprise skills in the Course Overview

Identify which POs your course develops most strongly (Strength 2 or 3 mappings). In the Course Overview section of the Course File, add a brief statement naming the skills and how they appear, for example:

> *"This course develops **Communication (PO9)** and **Ethical Reasoning (PO7)** as enterprise skills. Students practice communication through the Unit 3 design presentation (peer + faculty audience). Ethical reasoning is developed through the Unit 4 case study on [domain-specific ethical dilemma]."*

### 7.3 How to design enterprise skills into assignments

The assignment brief must:
1. **Name** the enterprise skill (and its PO) being targeted.
2. Include a **constraint or context** that forces the skill (e.g., audience specification for communication; a changed constraint for adaptability).
3. Include at least **one observable rubric criterion** that separately scores the skill — not just the technical output.

> **Avoid**: a group project brief that says "work in teams" without assessing collaboration explicitly.  
> **Prefer**: a brief that says "each team member submits a 1-paragraph reflection on their contribution and one thing they adapted based on a teammate's input" — with a rubric row for Collaboration (PO8).
---

## 8. IKS / Sustainability / Liberal Studies — Integration Guide

| Thread | Domain-agnostic integration examples |
|---|---|
| **IKS** | Historical precedents in the discipline from Indian heritage; Indian case studies; ethical principles from Indian philosophical traditions |
| **Sustainability** | Resource optimization in any design/solution; environmental impact of the course's domain; community wellbeing considerations |
| **Liberal Studies** | Ethics case study; interdisciplinary connection; communication / creative expression component; design thinking |

**Minimum requirement**: at least one of the three threads integrated in at least one unit, visible in the lesson plan, and ideally rubric-assessed.

---

*Guideline Version*: 1.0 (University Edition) | *Released*: June 2026  
*Derived from*: `Course_Designer_Guidelines_2026.md` (School of CSE, 2026 Scheme)  
*Maintained by*: REVA Teaching-Learning Innovation Team  
*Lead Architect*: Sanjay Chitnis  
*Companion documents*: `Course_File_Template_Universal.md` | Programme Extension files  
*Next Review*: June 2027
