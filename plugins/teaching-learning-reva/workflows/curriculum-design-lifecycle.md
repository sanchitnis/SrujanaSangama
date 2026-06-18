# Curriculum Design Lifecycle Workflow
## Complete Human-AI Collaborative Pipeline for REVA University

> **Usage**: This document defines the end-to-end curriculum design process at REVA University. Faculty curriculum committees, programme leaders, department heads, and AI collaborators use this workflow to move from institutional strategy through course design, activity design, and concept mapping. **Every decision gate remains with humans.**

---

## Overview: Five-Phase Model

The curriculum design lifecycle is structured in **5 integrated phases**, each with explicit human deliberation gates:

```
PHASE 1: STRATEGY          PHASE 2: ARCHITECTURE      PHASE 3: COURSE DESIGN    PHASE 4: ACTIVITY DESIGN   PHASE 5: CONCEPT MAPPING
School Vision              Programme Structure         Individual Courses        Learning Activities        Concept Network
↓                         ↓                           ↓                         ↓                          ↓
Market Analysis           PO/PSO Definition          CO Definition             AI-Ready Activities        Prerequisites & Usage
Job Role Profiles         Prerequisite Mapping       CO-PO/PSO Mapping        Bloom's Alignment         Attainment Evidence
↓                         ↓                           ↓                         ↓                          ↓
📋 HUMAN DELIBERATION      📋 HUMAN DELIBERATION      📋 HUMAN DELIBERATION    📋 HUMAN DELIBERATION    📋 HUMAN DELIBERATION
Faculty Committee         Faculty + Industry         Faculty + Subject Expert  Faculty + Pedagogy Expert  Curriculum Committee
Program Leader Review     Validation Panel           Peer Review               Industry Input             Global Benchmarking
```

---

## Phase 1: Curriculum Strategy (Human-Created Inputs)

### Duration
**4–6 weeks** | Led by: School Director, Department Heads, Faculty Committee | AI Role: Structure, template support

### Inputs Required (Humans Provide)
1. **School Vision & Mission Document**
   - Alignment to REVA's global, sustainable, technologically advanced, wellbeing vision
   - Core values and student formation goals

2. **Programme Learning Objectives (PEOs)** — 3 to 5 per programme
   - Raised to AI-era ambition (students perform at 5–6 year experience levels via AI co-working)
   - Differentiators from peer institutions
   - Career progression aspirations

3. **Industry Job Role Analysis**
   - Identify 6–10 critical job roles for graduates
   - Skills, tools, and responsibilities for each role
   - Emerging vs. declining roles (5-year horizon)
   - Internship and placement success criteria

4. **Market & Futures Intelligence**
   - WEF Future of Jobs relevant insights
   - NASSCOM FutureSkills gaps
   - LinkedIn Economic Graph trends in your domain
   - Global benchmarking (QS, THE, NIRF gaps)

### Phase 1 Deliverables (AI Supports Structuring)

| Artifact | Format | Content |
|---|---|---|
| **Strategy Brief** | Markdown | Vision, mission alignment, market positioning, key differentiators |
| **Job Role Profiles** | Table | Role title, responsibilities, skills, tools, expected salary range, career ladder |
| **Futures Dashboard** | Markdown + Table | WEF, NASSCOM, industry trends mapped to curriculum implications |
| **PEO Document** | Markdown | Each PEO with rationale, CO coverage, assessment strategy |

### Phase 1 Gate: Faculty Committee Approval
- [ ] Strategy brief reviewed and approved by faculty curriculum committee
- [ ] Job role profiles validated by industry advisory board
- [ ] PEOs endorsed by school leadership and aligned to REVA mission
- [ ] **Decision**: Proceed to Phase 2 or iterate strategy

---

## Phase 2: Curriculum Architecture (Programme-Level Design)

### Duration
**3–4 weeks** | Led by: Faculty Curriculum Committee + Industry Panel | AI Role: CO-PO mapping, prerequisite analysis, gap detection

### Phase 2 Inputs (from Phase 1)
- Approved PEOs
- Job role profiles
- Market intelligence
- REVA Mission alignment markers

### Phase 2 Process

#### Step 2.1: Translate PEOs to Programme Outcomes (POs & PSOs) — *[5 days]*
- **AI Task**: Generate draft PO set using NBA 11 (updated NBA framework) + REVA mission threads + enterprise skills
- **Human Task**: Faculty committee deliberates, adapts, finalizes POs
  - Ensure PO-PSO set covers: technical competency, AI literacy, ethical reasoning, sustainable thinking, global perspective, enterprising mindset
  - Map each PO to job role expectations
  - Ensure at least 60% of POs target HOTS (Level 4–6)
- **Artifact**: Finalized PO/PSO document with rationale

#### Step 2.2: Build Programme Structure — *[5 days]*
- **AI Task**: Generate alternate programme structures (credit distribution, semester layout, theory-lab-project balance)
- **Human Task**: Faculty committee selects structure
  - Semester-wise course distribution
  - Core vs. elective balance
  - Srujana stage integration (Stage 2 internship, Stage 3 product/research, Stage 4 venture)
  - Lab, project, and portfolio slots reserved
- **Artifact**: Programme curriculum outline with course codes, credits, prerequisites

#### Step 2.3: Map Programme Concept Network — *[7 days]*
- **AI Task**: Extract foundational concepts from programme; map prerequisites (PUC → Year 1 → Year 2 → Year 3 → Year 4)
- **Human Task**: Faculty validates concept prerequisites and sequencing
  - Ensure no concept is isolated (every concept has a prerequisite and future usage)
  - Flag circular dependencies
  - Align pre-requisite courses to match student entry behavior
- **Artifact**: Concept dependency map (Mermaid); prerequisite chain for every course

#### Step 2.4: Define Portfolio & Attainment Strategy — *[5 days]*
- **AI Task**: Suggest portfolio outputs aligned to POs/PSOs and job roles
- **Human Task**: Faculty decides portfolio structure
  - Every course produces a unit portfolio item (publication, case analysis, design)
  - Capstone or Stage 4 integrates all portfolio items into a unified graduate portfolio
  - Portfolio assessment rubric linked to CO and PO attainment
- **Artifact**: Portfolio strategy document; capstone brief; attainment measurement plan

### Phase 2 Gate: Faculty + Industry Validation
- [ ] PO/PSO set approved by faculty committee and industry advisory board
- [ ] Programme structure aligned to job roles and graduation requirements
- [ ] Concept network validated (no isolated concepts; all prerequisites satisfied)
- [ ] Portfolio strategy accepted as mechanism for CO-PO attainment evidence
- [ ] **Decision**: Proceed to Phase 3 (course design) or iterate architecture

---

## Phase 3: Course Design (Individual Course Development)

### Duration
**2–3 weeks per course** | Led by: Course Faculty + Subject Matter Expert | AI Role: CO drafting, mapping, benchmarking

### Phase 3 Inputs
- Approved PO/PSO framework
- Job role profiles
- Concept prerequisite map
- Portfolio strategy

### Phase 3 Process

#### Step 3.1: Review Curriculum Strategy & PO/PSO Mapping — *[1 hour]*
**AI Skill Invoked**: `/curriculum-strategy-check`
- Input: School strategy document
- AI generates: Structured audit against 8 dimensions (IKS integration, sustainability, liberal studies, enterprise skills, industry alignment, job role coverage, attainment strategy, international benchmarking)
- Output: PASS/FAIL verdict per dimension; remediation checklist
- **Human Decision**: Review audit; approve strategy or request revisions

#### Step 3.2: Define Course Outcomes (COs) — *[2 days]*
- **AI Task**: Draft COs using AI-augmented design principles (assumes AI co-working; focuses on judgment, synthesis, ethics, creativity)
- **Human Task**: Faculty reviews, refines, and approves CO set
  - Verify Bloom's Levels: **60%+ HOTS (L4–L6)** minimum
  - Embed at least one enterprising human skills CO (initiative, adaptability, collaboration, ethical reasoning, communication, creativity)
  - Ensure CO coverage of prerequisite concepts from prerequisite courses
  - Verify CO will support future courses' prerequisites
  - Link each CO to at least one job role expectation
- **Artifact**: CO document with Bloom's level, enterprise skills thread, job role mapping

#### Step 3.3: Map CO-PO/PSO Strength Levels — *[1 day]*
**AI Skill Invoked**: `/course-check` (updated)
- Input: Course outcomes, PO/PSO framework, job roles
- AI generates: Draft CO-PO/PSO matrix with strength levels (1=Slight, 2=Moderate, 3=Substantial) and justifications
- **Human Review**: Faculty validates mapping strength and identifies assessment strategy
  - For Strength 3 mappings: Specify which CO assessment (CIA, labs, projects) directly measures PO attainment
  - Flag any CO that maps to no PO (orphaned outcome)
  - Verify enterprising skills CO is mapped to appropriate POs
- **Artifact**: Finalized CO-PO/PSO mapping matrix with strength justifications

#### Step 3.4: Design Unit Structure & Activities — *[3 days]*
- **AI Task**: Suggest unit sequence, major topics, prerequisite concept coverage
- **Human Task**: Faculty refines unit breakdown
  - 4–5 units per course (semester span)
  - Each unit linked to 1–3 COs
  - Prerequisite concepts from prior courses explicitly listed
  - Portfolio output per unit or cumulative
- **Artifact**: Unit syllabus structure

#### Step 3.5: Verify Portfolio & Institutional Integration — *[1 day]*
- **AI Task**: Audit course for portfolio linkage, IKS integration, sustainability thread, liberal studies connection
- **Human Task**: Faculty specifies portfolio output and institutional threads
  - Designate portfolio output (research paper, design prototype, computational report, case solution, open source contribution)
  - Add IKS linkage: historical Indian engineering example, Indian mathematical principle, or Indian approach to the topic
  - Add sustainability linkage: optimization, resource management, environmental impact, or ethical consideration
  - Add liberal studies connection: communication, storytelling, ethics, design thinking, or creative expression
- **Artifact**: Course design document (ADDIE-compliant) with CO-PO mapping, unit structure, portfolio linkage, institutional integration

### Phase 3 Gate: Faculty Peer Review + Subject Expert Input
- [ ] COs verified for Bloom's levels and AI-era design
- [ ] CO-PO/PSO mapping reviewed for rigor and justification
- [ ] No orphaned COs; all COs mapped to ≥1 PO
- [ ] Enterprising skills CO present and assessed
- [ ] Portfolio output clearly defined and linked to COs
- [ ] IKS, sustainability, liberal studies integration specified
- [ ] Course aligns to programme concept network (prerequisites satisfied, supports future courses)
- [ ] **Decision**: Proceed to Phase 4 (activity design) or revise course design

---

## Phase 4: Activity Design & AI-Readiness (Learning Experiences)

### Duration
**2–3 weeks per course** | Led by: Course Faculty + Pedagogy Advisor + Industry Partner | AI Role: Activity drafting, AI-triviality auditing, rubric design

### Phase 4 Inputs
- Finalized course design from Phase 3
- CO-PO/PSO mapping with strength levels
- Portfolio strategy
- Job role profiles

### Phase 4 Process

#### Step 4.1: Design Active Learning Activities — *[5 days]*
**AI Skill Invoked**: `/activity-design-ai-ready`
- Input: Course unit, target COs, Bloom's levels, enterprise skills thread
- AI generates: 3–5 unit activities including:
  - In-class active learning (think-pair-share, jigsaw, flipped classroom, Socratic seminar)
  - Out-of-class project or assignment
  - Proctored skill validation activity (to prevent AI triviality bypass)
  - Portfolio contribution (how this unit's work feeds the final course portfolio)
- **Human Review & Adaptation**: Faculty and pedagogy advisor
  - Verify AI-ready design: activities include contextual constraints, meta-cognitive reflection, authentic assessment indicators
  - Ensure HOTS-aligned: 60%+ of assessment weight targets Bloom's L4–L6
  - Map activities to career-readiness and enterprise skills expectations
  - Specify proctoring strategy (in-lab modification, viva-voce, live execution, peer validation)
  - Adapt activities to local context, student population, available resources
- **Artifact**: Unit-wise activity playbook with timelines, instructions, rubrics

#### Step 4.2: AI-Triviality & Assessment Authenticity Audit — *[3 days]*
**Automated Check**: Assignment authenticity verification
- Input: All assignment briefs, exams, project descriptions
- AI flags:
  - Tasks solvable in <5 minutes via generic AI prompt → Redesign required
  - Tasks lacking localized context or student-specific constraints → Add constraint
  - Tasks missing meta-cognitive requirement → Add reflection/explanation component
  - Tasks with weak rubric or unclear success criteria → Strengthen rubric
- **Human Decision**: Faculty reviews flags and either
  - Accepts the activity as AI-resistant after AI review confirms constraints
  - Redesigns activity to add context, constraints, or meta-cognition
- **Artifact**: AI-readiness audit report; redesigned activity briefs (if needed)

#### Step 4.3: Design Rubrics for All HOTS Assessment — *[2 days]*
- **AI Task**: Generate analytic and holistic rubrics for major activities, projects, and portfolio artefacts
- **Human Review & Refinement**: Faculty ensures rubrics are observable, measurable, and linked to COs and POs
  - Holistic rubric: 4–5 levels (Excellent, Good, Satisfactory, Poor); CO and PO indicators at each level
  - Analytic rubric: 4–6 criteria (content, process, presentation, collaboration, ethics, creativity); each criterion scored separately
  - Rubric aligned to enterprise skills where applicable (initiative, communication, ethical reasoning, etc.)
- **Artifact**: Rubric set for all graded activities

#### Step 4.4: Design Proctored Skill Validation Tasks — *[3 days]*
- **Input**: CO-PO mapping; enterprise skills COs; job roles requiring specific skills
- **Process**: Faculty designs 2–3 proctored activities (in-lab, in-class, or supervised)
  - Live coding/problem-solving under time constraint
  - Modification task: student modifies their own code/solution on the spot
  - Viva-voce: oral exam using randomized Socratic question pools to verify understanding
  - Peer-teaching: student explains concept to peer and responds to clarifying questions
- **Purpose**: Direct evidence that CO was achieved by the student, not delegated to AI
- **Artifact**: Proctored activity briefs with question banks and marking scheme

### Phase 4 Gate: Pedagogy + Industry Expert Review
- [ ] Active learning activities designed for each unit
- [ ] All activities mapped to COs and HOTS levels
- [ ] AI-readiness audit passed: no AI-trivial tasks; all assignments include contextual constraints
- [ ] Rubrics are observable, measurable, linked to COs and POs
- [ ] Proctored validation activities designed for all Strength 3 CO-PO mappings
- [ ] Enterprise skills assessed in 2–3 activities with visible rubric criteria
- [ ] Portfolio contribution pathway clear for each activity
- [ ] Career readiness indicators present in 2+ activities
- [ ] **Decision**: Finalize activity playbook or iterate design

---

## Phase 5: Concept Map Network (Curriculum Coherence Verification)

### Duration
**1–2 weeks** | Led by: Curriculum Coordinator + AI | AI Role: Concept extraction, mapping, validation

### Phase 5 Inputs
- All course designs from Phase 3
- All activity designs from Phase 4
- Job role profiles
- GATE/competitive exam syllabus (if applicable)

### Phase 5 Process

#### Step 5.1: Concept Extraction & Network Mapping — *[3 days]*
**AI Skill Invoked**: `/concept-map-network`
- Input: All course syllabi, topic lists, activity descriptions
- AI extracts and maps:
  - **Core Concepts**: Foundational principles (e.g., Binary Search, Finite State Machine, Photosynthesis, Ohm's Law)
  - **Prerequisite Chains**: Concept A (PUC) → Concept B (Sem 1) → Concept C (Sem 3) → Concept D (Job role)
  - **Usage Tracking**: Every concept appears in ≥1 course; advanced Bloom's levels in later courses
  - **Job Role Linkage**: Map concepts to skills in job profiles; flag redundant or missing concepts
  - **GATE Alignment**: For CSE/ECE: flag any GATE exam topics not covered in curriculum
- **Output**: Mermaid network diagram + CSV matrix (concept | prerequisite | courses taught | Bloom's levels | job roles using | GATE relevance)
- **Artifact**: Concept map (Mermaid visualization); concept-course coverage matrix

#### Step 5.2: Curriculum Coherence Audit — *[2 days]*
- **AI Task**: Identify:
  - Isolated concepts (no prerequisite, no future usage) → Flag for removal or repurposing
  - Orphaned prerequisites (concept taught but no course using it) → Identify downstream course or remove
  - Circular dependencies (Concept A → B → A) → Resolve sequencing
  - Concept gaps vs. job roles or GATE exam → Recommend insertion
- **Human Review**: Curriculum committee validates AI findings
  - Approve concept removals
  - Decide on concept additions
  - Validate prerequisite sequence
  - Confirm all job role competencies are covered
- **Artifact**: Curriculum coherence report; approved concept network

#### Step 5.3: Concept-CO Linking & Attainment Mapping — *[3 days]*
- **Process**: Link every concept to the CO(s) that teach it
  - Create matrix: Concept | Course | CO | Bloom's L | Assessment | Portfolio Evidence
  - Verify every CO has 3–8 foundational concepts
  - Identify Bloom's L progression: if Concept X is taught at L2 in Sem 1 and L4 in Sem 3, evidence flow is correct
- **Artifact**: Concept-CO mapping matrix; Bloom's progression tracker

#### Step 5.4: Global Benchmarking & International Alignment — *[2 days]*
- **AI Task**: Compare curriculum against:
  - International best practices (CDIO from Singapore, EU Competency Frameworks, China's engineering holism, Japan's character development, Korea's ICT leadership, India's IKS)
  - Peer institution curricula (QS/THE benchmarks)
  - Industry-defined curricula (Google, Amazon, Microsoft skill tracks; NASSCOM, IEEE guidelines)
- **Human Review**: Curriculum committee identifies best-practice gaps or innovations to adopt
  - Stronger enterprise skills integration?
  - Enhanced sustainability or IKS threads?
  - New technology or methodology adoption?
- **Artifact**: International benchmarking report; curriculum enhancement recommendations

### Phase 5 Gate: Curriculum Committee Final Approval
- [ ] Concept map complete: no isolated concepts; all prerequisites and usage paths clear
- [ ] Concept-CO mapping verified: every CO has core concept support; Bloom's progression validated
- [ ] Job role coverage confirmed: every job role skill is mapped to ≥1 concept-CO-course
- [ ] GATE/competitive exam alignment checked (CSE/ECE); gaps noted or resolved
- [ ] Global benchmarking review complete; no critical best-practice gaps identified
- [ ] Final approval by curriculum committee + programme leader
- [ ] **Decision**: Approve curriculum for BOS submission or iterate

---

## Post-Approval: Implementation & Continuous Evaluation

### Phase 5+ Implementation Workflow

#### Step 5+.1: BOS Submission & Governance Approval — *[2–4 weeks]*
- **AI Task**: Format curriculum documentation for UGC/AICTE compliance and BOS review
- **Human Task**: Board of Studies deliberates and approves
  - BOS votes on curriculum changes
  - Approves or requests modifications
  - Sets effective implementation date

#### Step 5+.2: Faculty Development & Preparation — *[4–6 weeks]*
- **Process**: FDP workshop for all faculty teaching in the programme
  - Hands-on activity design and rubric creation
  - AI-ready assessment strategies
  - Proctored skill validation techniques
  - Portfolio evaluation practices
  - Enterprise skills mentoring approaches

#### Step 5+.3: Course Launch & Mid-Semester Checkpoints — *[Semester-long]*
- **Ongoing**: 
  - Faculty implement course design and activities
  - Mid-semester formative evaluation: check if COs are being attained
  - Adjust activities or rubrics if needed
  - Document portfolio artefacts
  - Collect indirect evidence (surveys, focus groups) on enterprise skills development

#### Step 5+.4: End-of-Semester CO Attainment & Programme Review — *[2 weeks post-semester]*
- **Process**: 
  - AI aggregates CO attainment data (CIA scores, end-sem exams, project rubrics, portfolio artefacts)
  - Faculty reviews attainment against targets (typically 70–80% of students achieve ≥70% in each CO)
  - If attainment <60%, trigger remediation or activity redesign for next iteration
  - Collect feedback on enterprise skills from student reflections and industry internship supervisors

#### Step 5+.5: Annual Curriculum Review Cycle — *[6–8 weeks, end of academic year]*
- **Process**: Annual structured curriculum review facilitated by teaching-learning-reva plugin
  - Aggregate co-attainment across cohorts
  - Job placement feedback: which COs were most valued by employers?
  - Student career survey: are graduates positioned for identified roles?
  - Futures intelligence update: any emerging skills or roles to incorporate?
  - Faculty and industry feedback compilation
  - Propose curriculum enhancements for next BOS cycle

---

## Key Design Principles (Woven Throughout)

### 1. Portfolio-First Learning
Every course, every semester produces a tangible artefact:
- Unit outputs: research summaries, design prototypes, computational analysis, documented solutions
- Course capstone: unified project or paper demonstrating CO mastery
- Graduation portfolio: showcase of best work across all four years, career-ready

### 2. AI-Ready & AI-Proof Assessment
- Activities designed with AI co-working assumption
- Constraints added: context-specific, student-roster-specific, locally-situated
- Meta-cognitive component required: reflection, explanation, reasoning
- Proctored validation for all Strength 3 CO-PO mappings
- Peer and viva-voce components to verify individual contribution

### 3. Enterprising Human Skills as Thread
Every course embeds at least one CO in:
- **Initiative & Adaptability**: Design challenges with open-ended constraints
- **Collaboration & Communication**: Group projects with peer evaluation, presentations with feedback
- **Ethical Reasoning**: Case studies, ethical dilemmas, sustainability impact analysis
- **Value Creation**: How does the student's work solve real problems or create value for users?

### 4. International Best Practices Woven In
- **CDIO (Singapore)**: Conceive → Design → Implement → Operate structure in capstone/Srujana projects
- **China's Engineering Holism**: Dual focus on technical competency + moral character development
- **EU Competency Framework**: Explicit competency descriptions (knowledge, skills, attitudes)
- **Japan's Kaizen & Hitaishin**: Continuous improvement and inner development threads
- **Korea's ICT Leadership**: Emerging technology adoption and digital transformation mindset
- **India's IKS**: Historical achievements, local case studies, ethical principles of stewardship

### 5. Sustainability & Liberal Studies Integration
Every course connects to:
- **Sustainability**: Resource optimization, environmental impact, circular economy, climate considerations
- **Liberal Studies**: Arts, design thinking, literature, performing arts, ethics, philosophy, local culture
- **IKS**: Indian mathematical or engineering history, local Indian case study, ethical principle from Indian philosophy

### 6. OBE Rigor & HOTS Dominance
- 60%+ of COs target Bloom's L4–L6 (Analyze, Evaluate, Create)
- Assessment weight: 60%+ on HOTS tasks
- Clear CO-PO mapping with explicit strength levels and justifications
- Direct attainment evidence (CIA, projects, exams) + Indirect (surveys, portfolio review)
- Annual attainment review and remediation planning

### 7. Human Governance at Every Gate
All critical decisions rest with humans:
- Strategy approval by faculty committee + industry board
- PO/PSO definition by faculty
- CO refinement by subject experts
- Activity design review by pedagogy advisors
- Portfolio strategy by faculty committees
- Concept network validation by curriculum leaders
- Final approval by BOS

AI provides: drafts, suggestions, structured analysis, rubric templates, audit reports. Humans deliberate, decide, and take accountability.

---

## Using This Workflow

### For a New Curriculum Initiative
1. Complete Phase 1 (Strategy) — School Director leads with industry input
2. Run `/curriculum-strategy-check` skill to audit strategy completeness
3. Proceed through Phases 2–5 sequentially
4. At each phase gate, convene human deliberation session
5. Move to implementation

### For Curriculum Revision (Annual Cycle)
1. Start at Phase 5+ (Post-Approval Implementation & Review)
2. Run annual curriculum review with AI support
3. Identify proposed changes
4. For major changes: return to Phase 2 or 3 as needed
5. For minor tweaks: Phase 4 activity design refresh
6. Submit to BOS

### For Adding a New Course (Mid-Curriculum)
1. Verify fit within programme architecture (Phase 2 concept network)
2. Conduct Phase 3 (Course Design) in isolation
3. Ensure course COs map to programme POs/PSOs and concept prerequisites
4. Conduct Phase 4 (Activity Design)
5. Update programme concept map (Phase 5)
6. Submit to BOS as standalone course addition

---

## AI Skills Supporting This Workflow

| Skill Name | Triggered | Input | Output |
|---|---|---|---|
| `/curriculum-strategy-check` | Phase 3.1 | School strategy document | Strategy audit with 8-dimension assessment |
| `/course-check` (updated) | Phase 3.3 | Course design + PO/PSO framework | CO quality audit; mapping strength matrix; improvement checklist |
| `/activity-design-ai-ready` | Phase 4.1 | Unit, COs, Bloom's levels | 3–5 unit activities with AI-ready design indicators |
| `/concept-map-network` | Phase 5.1 | All course syllabi + job profiles | Mermaid network, concept-course-CO matrix, gap analysis |
| `/enterprise-skills-audit` | Phases 3–4 (continuous) | COs, activities, rubrics | Enterprise skills thread coverage; recommendations |
| `/portfolio-audit` | Phases 3–4 (continuous) | Course design, activities | Portfolio output linkage; assessment evidence mapping |
| `/iks-integration-check` | Phases 3–4 (continuous) | Unit topics, activities | IKS thread suggestions; local case study integration |

---

## Success Indicators

A curriculum designed via this workflow should evidence:

- ✅ **60%+ HOTS dominance** across COs, assessment, and activities
- ✅ **No isolated concepts** in the concept map; every concept has a prerequisite and future usage
- ✅ **All job roles addressed** with >1 mapped concept-CO pathway
- ✅ **Portfolio artefacts collected** each semester; capstone integrates all
- ✅ **Enterprise skills embedded** in 4+ unit activities; observable rubric criteria
- ✅ **CO attainment >70%** annually for ≥75% of students
- ✅ **Graduate feedback**: "This curriculum prepared me for my role and emergent challenges"
- ✅ **International benchmarking**: Curriculum aligns or exceeds peer institution quality
- ✅ **IKS, sustainability, liberal studies integrated** visibly in each course
- ✅ **Student engagement & satisfaction >80%** on end-of-semester surveys

---

*Last Updated: June 11, 2026 | Maintained by: REVA Teaching-Learning Innovation Team*
