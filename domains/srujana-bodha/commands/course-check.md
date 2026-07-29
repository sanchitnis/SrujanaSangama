# /course-check
## Course Design Quality Audit (Enhanced OBE & AI-Ready Edition)

> Paste this command: `/course-check <path-to-course-design-document>`
>
> **Purpose**: Conduct a comprehensive, professional audit of a course syllabus, outcomes, and programme mapping against REVA's Course Design Quality Standard, OBE rigor, AI-readiness, and institutional alignment standards.
>
> **Session Type**: Structured course audit review | **Duration**: 45–60 minutes
>
> **Human Role**: You provide the course design document. AI audits comprehensively. Faculty reviews findings and acts on recommendations.

---

## Input Requirements

Provide a **Course Design Document** (can be a draft) containing:

1. **Course Metadata**: Code, title, credits, semester, prerequisites
2. **Course Outcomes (COs)**: 4–6 outcomes with target Bloom's levels
3. **CO-PO/PSO Mapping**: How each CO contributes to programme outcomes (optional draft; audit will enhance)
4. **Unit Structure**: 4–5 units with topics and expected Bloom's levels
5. **Assessment Strategy**: CIA methods, end-sem exam, projects, labs (draft or final)
6. **Resources & Activities**: Learning methods, tools, pedagogical approach (draft or final)

---

## Comprehensive Audit Steps (7 Dimensions)

### Dimension 1: Course Outcomes Quality & Bloom's Verification ✓

**Audit Task**: Verify each CO is measurable, uses strong action verbs, and targets appropriate cognitive levels for AI-era learning.

**Checks**:

| Criterion | Flag if... |
|---|---|
| Weak Verb | CO uses "understand", "know", "study", "learn", "be familiar with" |
| Unmeasurable | CO uses vague terms like "appreciate", "explore", "gain insight" without success criteria |
| Below L3 | All COs are <L3; no synthesis, application, or analysis present |
| Bloom's L1-L3 Heavy | >50% of COs target only L1–L3 (knowledge, comprehension, application) |
| No L4-L6 Thread | Fewer than 2 COs target L4–L6 (analyze, evaluate, create) |
| Enterprise Skills Missing | No CO explicitly targets initiative, adaptability, collaboration, ethical reasoning, communication, or creativity |

**Findings Table**:

| CO ID | Statement | Bloom's L | Strong Verb? | Measurable? | Flags |
|---|---|---|---|---|---|
| CO1 | ... | L# | Y/N | Y/N | [Any of above] |

**Summary Metrics**:
- Total COs: `[#]`
- HOTS COs (L4-L6): `[#]` / **HOTS Percentage: $\ge 60\%$?** → **[PASS / FAIL]**
- Enterprise Skills COs: `[#]` (Target: ≥1 explicit)
- Weak Verbs: `[#]` → **[PASS / ACTION NEEDED]**

**Output**: PASS / CONDITIONAL / FAIL with specific CO rewrites recommended

---

### Dimension 2: CO-PO/PSO Mapping Rigor & Strength Levels ✓

**Audit Task**: Verify that each CO is explicitly mapped to Programme Outcomes (POs) and Programme Specific Outcomes (PSOs) with justified strength levels.

**Standard**: 
- Strength 1 (Slight/Low): Indirect or minor reinforcement
- Strength 2 (Moderate/Medium): Explicitly assessed in projects, homework, or labs
- Strength 3 (Substantial/High): Direct, central focus of course; measured as core outcome

**Checks**:

| Criterion | Flag if... |
|---|---|
| Unmapped CO | Any CO not mapped to ≥1 PO/PSO (orphaned outcome) |
| No Strength Levels | Mapping exists but strength (1/2/3) not specified |
| Strength 3 - No Justification | High mapping strength asserted but no assessment strategy described |
| No PO Coverage | Some POs receive no CO mapping (coverage gap) |
| Generic Mapping | All COs mapped identically to same POs (unrealistic) |
| Enterprise Skills PO Missing | Enterprising human skills CO not linked to any PSO/PO on ethics, collaboration, or leadership |

**Findings Table**:

| CO ID | Mapped PO/PSO | Strength | Assessment Evidence | Justification Quality | Gaps |
|---|---|---|---|---|---|
| CO1 | PO1, PO3, PSO2 | 2, 2, 3 | CIA quiz, project rubric, viva | Clear; rubric explicit | None |
| CO2 | [Unmapped] | — | — | — | **ORPHANED** |

**Summary Metrics**:
- Total CO-PO pairs: `[#]`
- Mapped pairs with strength levels: `[#]` → **[PASS if 100% / CONDITIONAL if 70–99% / FAIL if <70%]**
- Strength 3 mappings with clear assessment strategy: `[#]` / `[Total Strength 3]`
- Enterprise skills CO linked: **[YES / NO]** → **[PASS if YES / FAIL if NO]**

**Output**: PASS / CONDITIONAL / FAIL with specific mapping strength recommendations
1.  **Analyze Course Outcomes (COs)**:
    *   List all COs.
    *   Identify the Bloom's Cognitive Level (L1 to L6) of the primary verb in each CO.
    *   Flag any COs using weak, non-measureable verbs (e.g., "understand", "study", "know").
2.  **Evaluate HOTS Dominance**:
    *   Calculate the percentage of COs that map to Levels 4 (Analyze), 5 (Evaluate), or 6 (Create).
    *   Standard check: **Is the HOTS percentage $\ge 60\%$?**
3.  **Assess CO-PO & PSO Mapping Rigor**:
    *   Audit the mapping strength levels (1, 2, 3) for each CO-PO pair.
    *   Identify any "high" mapping strengths (Level 3) that lack clear learning activity justifications.
    *   Confirm if the enterprising human skills PO/PSO thread is linked.
4.  **Verify Portfolio Linkage**:
    *   Identify the designated portfolio output (e.g., product, paper, open-source repository) associated with the course.
    *   Check if the portfolio milestones are mapped directly to corresponding COs.
5.  **Examine Institutional Alignment**:
    *   Verify integration of Educate to enterprise philosophy, focus on developing human centered core/life skills, Engineering habits (if applicable), AI-ready activities (where students performace higher level activities with augmentation by AI), Learning by doing, PBL, liberal studies, sustainability indicators, REVA vision, mission and values and finally NEP perspectives, Indian Knowledge Systems (IKS) etc. in course units.

---

### Dimension 3: Enterprise Human Skills Thread ✓

**Audit Task**: Verify that at least one CO explicitly targets enterprising human skills and that assessment and rubrics are in place.

**Enterprising Skills Taxonomy**:
- **Initiative**: Identifies problems proactively; takes action without waiting for permission
- **Adaptability**: Learns quickly; pivots strategy when conditions change; embraces uncertainty
- **Collaboration**: Works across boundaries; listens actively; negotiates win-win
- **Ethical Reasoning**: Considers stakeholder impact; navigates dilemmas with integrity
- **Communication**: Articulates ideas clearly; tailors message to audience; listens
- **Creativity & Value Creation**: Generates novel solutions; creates value for users/organization

**Checks**:

| Criterion | Flag if... |
|---|---|
| No Enterprise CO | Zero COs target enterprising skills |
| Generic Language | CO says "develop leadership" without specific skill name |
| No Assessment | Enterprise CO exists but no rubric or assessment method specified |
| No Visibility | Enterprise component exists but is hidden in activities (not explicit in CO) |
| Low Assessment Weight | Enterprise CO assessed <10% of course grade |
| No Rubric | Rubric for enterprise CO lacks observable, measurable criteria |

**Findings Table**:

| Enterprise Skill | CO # | Assessment Method | Rubric Present? | Weight in Grade | Observable Criteria | Quality Rating |
|---|---|---|---|---|---|---|
| Initiative | CO#3 | Project with reflective component | Yes | 15% | 5 criteria explicit | Strong |
| Collaboration | [Missing] | — | — | — | — | **GAP** |

**Summary Metrics**:
- Enterprise skills COs: `[#]` (Target: ≥1)
- Skills explicitly named in CO: `[List]`
- Skills with visible assessment/rubric: `[#]` → **[PASS if all named / CONDITIONAL if partial / FAIL if none]**
- Average assessment weight per enterprise skill: `[#]%` (Target: 10–15%)

**Output**: PASS / CONDITIONAL / FAIL with specific enterprise skills integration recommendations

---

### Dimension 4: Portfolio Linkage & Artefact Mapping ✓

**Audit Task**: Verify that course design specifies a clear portfolio output and that each unit or the course culmination produces a tangible artefact linked to COs.

**Portfolio Output Types**:
- Research paper, literature review, case analysis
- Design prototype, system architecture, feasibility study
- Computational analysis, dataset, model, or simulation output
- Documented solution, algorithm implementation, open-source contribution
- Reflective narrative, career portfolio piece, professional communication sample

**Checks**:

| Criterion | Flag if... |
|---|---|
| No Portfolio Output | Course design silent on what portfolio artefact students produce |
| Vague Output | Output described as "project" or "assignment" without tangible product definition |
| No CO Linkage | Portfolio output exists but which CO(s) it measures is not specified |
| Unit Level Unclear | No clear mapping of unit outputs to cumulative course portfolio |
| No Assessment Rubric | Portfolio output has no rubric or success criteria |
| Weight <15% | Portfolio represents <15% of course grade (insufficient emphasis) |
| No Guidance | No template, exemplar, or rubric provided to students |

**Findings Table**:

| Portfolio Component | Unit / Timing | COs Addressed | Rubric Link | Weight | Exemplar Provided | Cumulative Integration |
|---|---|---|---|---|---|---|
| Unit 1: Literature Analysis | Week 3 | CO1, CO2 | Yes (analytic) | 5% | Yes | Feeds final synthesis |
| Unit 2: Design Brief | Week 6 | CO3, CO4 | Yes (holistic) | 5% | Yes | Feeds capstone project |
| Capstone: System Design Doc | Week 15 | CO3-CO6, PSO1 | Yes | 20% | Yes | Standalone + portfolio entry |

**Summary Metrics**:
- Total portfolio outputs: `[#]` (Target: ≥3 for 4-unit course)
- Outputs with explicit CO mapping: `[#]` → **[PASS if 100% / CONDITIONAL if 70–99% / FAIL if <70%]**
- Outputs with rubrics: `[#]`
- Average weight of portfolio in course grade: `[#]%` (Target: 15–25%)
- Student guidance (templates/exemplars) provided: `[YES / NO]`

**Output**: PASS / CONDITIONAL / FAIL with specific portfolio design recommendations

---

### Dimension 5: Assessment Strategy & HOTS Dominance ✓

**Audit Task**: Verify that the course assessment plan covers all COs, emphasizes HOTS (L4–L6), and includes both formative and summative methods.

**Standard**: 60%+ of assessment weight must target Bloom's L4–L6 (Analyze, Evaluate, Create).

**Checks**:

| Criterion | Flag if... |
|---|---|
| HOTS Weight <60% | Marks distribution: L1–L3 receive >40% of weight |
| Limited Methods | Assessment uses only exams or only projects (not diverse) |
| No Formative | No low-stakes quizzes, reflections, or checkpoints; only summative |
| CO Gaps | Some COs have no assessment method specified |
| No Rubrics | HOTS tasks lack analytic rubrics; grading criteria vague |
| AI-Trivial Tasks | Assignment briefs solvable by generic AI prompts; no contextual constraints |
| No Proctoring | Strength 3 CO-PO mappings have no proctored or viva-voce validation |

**Assessment Weight Distribution Table**:

| Assessment Type | Bloom's Levels Targeted | Weight | Formative/Summative | CO Coverage |
|---|---|---|---|---|
| Weekly Quiz | L1-L2 | 10% | Formative | CO1, CO2 |
| Midterm Exam | L2-L4 | 25% | Summative | CO1-CO3 |
| Group Project + Viva | L4-L6 | 20% | Summative | CO3-CO6 + Enterprise |
| Peer Review Reflections | L5-L6 | 15% | Formative | CO4, CO5, Enterprise |
| End-Sem Exam | L3-L4 | 30% | Summative | All COs |

**Summary Metrics**:
- Total assessment weight: `[100%]`
- HOTS weight (L4-L6): `[#]%` → **[PASS if ≥60% / FAIL if <60%]**
- Formative : Summative ratio: `[#]% : [#]%` (Healthy: 30–40% formative)
- Assessment methods: `[#]` types (Target: ≥4 methods)
- COs with rubrics: `[#]` / `[Total COs]`
- AI-trivial flags: `[#]` assessments need redesign

**Output**: PASS / CONDITIONAL / FAIL with specific assessment strategy recommendations

---

### Dimension 6: Institutional Integration (IKS, Sustainability, Liberal Studies) ✓

**Audit Task**: Verify that course design explicitly integrates Indian Knowledge Systems (IKS), sustainability/environmental responsibility, and liberal studies connections.

**Integration Points**:
- **IKS**: Historical Indian achievements, local case studies, Indian philosophical perspectives, mathematical/engineering heritage
- **Sustainability**: Resource optimization, circular economy, climate impact, environmental ethics, community wellbeing
- **Liberal Studies**: Arts, design thinking, literature, ethics, communication, creative expression

**Checks**:

| Criterion | Flag if... |
|---|---|
| No IKS Thread | Zero mention of Indian history, local cases, or IKS perspectives |
| No Sustainability Thread | Course ignores environmental impact or resource considerations |
| No Liberal Studies | No connection to ethics, communication, creative disciplines, or design thinking |
| Generic Examples | Examples mention India/sustainability but lack deep integration |
| Tokenistic | Institutional threads mentioned in one unit only; not woven throughout |
| No Assessment | Institutional threads present but not assessed or rubric-visible |

**Integration Mapping Table**:

| Thread | Unit(s) | Specific Integration | Assessment | Depth |
|---|---|---|---|---|
| IKS | Unit 2, Unit 4 | Vedic mathematics approach to algorithms; ancient Indian water management in System Design | Project rubric includes "IKS perspective" criterion | Substantial |
| Sustainability | Units 2-4 | Energy efficiency in every major design decision; carbon footprint analysis in capstone | Rubric criterion: "Sustainability consideration evident" | Moderate |
| Liberal Studies | Unit 1, Unit 4 | Ethics case study on AI bias (Unit 1); team communication reflection (Unit 4) | Rubric: "Ethical reasoning" and "Communication clarity" | Developing |

**Summary Metrics**:
- IKS integration: **[ABSENT / TOKEN / INTEGRATED / DEEP]** with `[#]` unit touchpoints
- Sustainability integration: **[ABSENT / TOKEN / INTEGRATED / DEEP]** with `[#]` unit touchpoints
- Liberal studies integration: **[ABSENT / TOKEN / INTEGRATED / DEEP]** with `[#]` unit touchpoints
- Institutional threads assessed (rubric visibility): **[YES / NO / PARTIAL]**

**Output**: PASS / CONDITIONAL / FAIL with specific integration enhancement recommendations

---

### Dimension 7: Concept Prerequisites & Future Course Alignment ✓

**Audit Task**: Verify that course design explicitly identifies prerequisite concepts (from prior courses or PUC) and clarifies how course concepts support downstream courses and job roles.

**Checks**:

| Criterion | Flag if... |
|---|---|
| No Prerequisite List | Course design silent on which prior-course concepts are assumed |
| Isolated Concepts | Topics taught with no visible connection to prior or future courses |
| No Job Role Linkage | Concepts not mapped to identified job role requirements |
| No Downstream Usage | Course design doesn't clarify how concepts will be used in future semesters |
| Concept Gaps | Prerequisites not taught in identified prior courses (curriculum hole) |

**Concept-Course Mapping Table**:

| Concept | Prerequisites (Prior Course) | Unit(s) Taught | Bloom's L | Job Roles Using | Downstream Courses | Verified? |
|---|---|---|---|---|---|---|
| Binary Search Tree | Data Structures (SEM 2) | Unit 2 | L3 | Software Engineer, ML Engineer | Database Design (SEM 4), Big Data (SEM 5) | Yes |
| Recursion | Programming Fundamentals | Unit 1-2 | L2→L4 | All roles | All advanced CS courses | Yes |
| API Design | [Missing] | Unit 4 | L4 | All roles | Microservices (SEM 5) | **NO - FLAG** |

**Summary Metrics**:
- Total concepts in course: `[#]`
- Concepts with explicit prerequisites verified: `[#]` → **[PASS if 100% / CONDITIONAL if 70–99% / FAIL if <70%]**
- Concepts mapped to future courses: `[#]`
- Concepts mapped to job roles: `[#]`
- Isolated concepts (no prerequisite, no usage): `[#]` → **[FLAG if >0]**

**Output**: PASS / CONDITIONAL / FAIL with curriculum coherence recommendations

---

## Output: Course Design Quality Audit Report

### 📊 REVA Course Design Quality Audit Report

```
COURSE INFORMATION
==================
Course Code: [CODE]
Course Title: [TITLE]
Semester: [SEM] | Credits: [#] | Prerequisite(s): [LIST]
Date Audited: [DATE]
Faculty Lead: [NAME]

EXECUTIVE SUMMARY
=================
Overall Verdict: [APPROVED FOR IMPLEMENTATION / CONDITIONAL APPROVAL — REVISIONS REQUIRED / REQUIRES MAJOR REDESIGN]
Quality Score: [##]/100

DIMENSION AUDIT RESULTS
=======================
✓ Dimension 1 (Outcomes & Bloom's): [PASS / CONDITIONAL / FAIL]
✓ Dimension 2 (CO-PO/PSO Mapping): [PASS / CONDITIONAL / FAIL]
✓ Dimension 3 (Enterprise Skills): [PASS / CONDITIONAL / FAIL]
✓ Dimension 4 (Portfolio Linkage): [PASS / CONDITIONAL / FAIL]
✓ Dimension 5 (Assessment & HOTS): [PASS / CONDITIONAL / FAIL]
✓ Dimension 6 (IKS/Sustainability/Liberal Studies): [PASS / CONDITIONAL / FAIL]
✓ Dimension 7 (Concept Prerequisites): [PASS / CONDITIONAL / FAIL]

DETAILED FINDINGS
=================
[Per-dimension audit summary, findings table, and recommendations]

REMEDIATION CHECKLIST (Priority Order)
=======================================
If CONDITIONAL or FAIL:

[ ] CRITICAL (Must fix before implementation):
    1. [Specific action with estimated effort]
    2. [Specific action with estimated effort]

[ ] HIGH (Must fix before next cycle):
    1. [Specific action]
    2. [Specific action]

[ ] MEDIUM (Good-to-have enhancement):
    1. [Specific action]

NEXT STEPS
==========
→ If APPROVED: Course ready for faculty development, activity design phase, and implementation
→ If CONDITIONAL: Schedule remediation review with faculty; target resolution date [DATE]; re-audit after revisions
→ If FAIL: Course design requires substantial rework; recommend faculty workshop; re-submit for audit

SIGN-OFF
========
Audited By: [AI Agent] | Date: [DATE]
Faculty Review By: [FACULTY NAME] | Date: [DATE]
Department Head Approval: [NAME] | Date: [DATE]

Next Audit: [DATE or "Upon major revision"]
```

---

## How to Use This Audit

### For Faculty Designing a Course
1. Draft your course design (COs, mapping, activities, assessment, portfolio output)
2. Run `/course-check <file>`
3. Receive comprehensive audit report with 7-dimension assessment
4. Review REMEDIATION CHECKLIST
5. Make prioritized revisions (CRITICAL first, then HIGH, then MEDIUM)
6. Submit revised course design for re-audit or faculty review

### For Department Heads / Curriculum Committees
1. Collect course audit reports for entire programme
2. Identify common gaps across courses (e.g., enterprise skills weak in multiple courses)
3. Plan programme-level FDP or curriculum revision sprint
4. Track remediation across courses

### For Annual Curriculum Review
1. Re-run audit on all existing courses
2. Identify drift from REVA standards
3. Prioritize refreshes
4. Plan incremental improvements

---

*Skill Version*: 2.0 (Enhanced OBE & AI-Ready Edition) | *Last Updated*: June 11, 2026 | *Maintained by*: REVA Teaching-Learning Innovation Team
