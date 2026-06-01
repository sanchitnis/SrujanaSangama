# REVA University — Agentic Academic Platform Architecture

> A Human-AI Collaborative System for AI-Era Curriculum Development, Portfolio-First Learning,
> Enterprising Student Formation, Srujana Pathway, Personalised Tutoring, Stakeholder Governance,
> and Institutional Excellence — aligned to ADDIE, NBA-OBE, NEP 2020, and REVA's Vision and Mission

\---

## REVA Vision and Mission

**Vision:** To become a technologically advanced, sustainable global university dedicated to the wellbeing of all.

**Mission:**

* Provide learner-centric education leveraged with cutting-edge technologies
* Foster stewardship by nurturing talent, leadership qualities, and entrepreneurial thinking in a safe and secure environment
* Promote liberal studies and foster the pursuit of performing arts, literature, sports, and other creative and intellectual disciplines
* Promote a culture of collaboration and cooperation
* Serve humanity and promote sustainability through higher education based on universal values

**Platform Promise:** Every course, every semester, every student emerges with a richer portfolio, a sharper enterprising mindset, a verified skill credential, and a clear personal trajectory — while REVA advances to Top 100 NIRF, deepens global partnerships, and lives its vision of wellbeing for all.

\---

## Foundational Design Philosophy

### Human-AI Collaboration as the Operating Principle

This platform is not an AI system that generates academic content autonomously. It is a **collaborative intelligence environment** where human judgment, institutional wisdom, faculty expertise, industry insight, and student agency are the primary authors — and AI is the accelerator, the quality mirror, and the tireless first-draft partner.

Every step — analysis, curriculum design, industry validation, BOS deliberation, content creation, assessment design, student mentoring — is a **human-AI dialogue**: AI contributes speed, breadth, pattern recognition, and structured outputs; humans contribute values, contextual judgment, relationships, creativity, and final authority.

No curriculum decision, no course approval, no assessment goes forward on AI output alone. The platform is a scaffold for better human decisions, not a replacement for them.

### The Enterprising Student as the North Star

The central output of this platform is a graduate who is **enterprising** — someone who:

* Sees problems as opportunities
* Initiates action rather than waiting for permission
* Collaborates across boundaries and disciplines
* Communicates with clarity and conviction
* Reasons ethically under uncertainty
* Adapts and learns continuously in the face of change
* Creates value for others — through technology, service, art, research, or leadership

This is broader than entrepreneurship. An enterprising nurse, civil servant, researcher, and founder all share these qualities. Every course, every assessment, and every Srujana stage is designed with this graduate in mind.

### PEO Ambition in the AI Era

Program Educational Objectives are **raised** in this platform. AI augmentation means REVA graduates are expected to perform tasks and take on responsibilities that previously required 5–6 years of industry experience. PEOs reflect this raised ambition. COs embed the assumption that students work alongside AI tools — assessed on judgment, synthesis, creative application, and ethical reasoning, not on tasks that AI can do faster.

\---

## Overview

The REVA Academic Agent Platform is a modular, multi-agent collaborative system built around the **complete professional life of a REVA faculty member**. Faculty operate simultaneously across five interconnected work domains — Teaching & Learning, Research, Academic Administration, Consulting & Product Development, and Kaizen & Wellbeing — and this platform provides dedicated agentic intelligence for every domain. Capabilities span the entire academic lifecycle: future-of-jobs intelligence gathering, programme and course design, stakeholder validation, Board of Studies governance, content delivery, portfolio-building assessments, CO attainment and accreditation, grant writing and patent drafting, industry consulting and IP commercialisation, and continuous personal and professional improvement. The platform operates across online, face-to-face, and hybrid modes and integrates NBA accreditation, NIRF ranking strategy, the Srujana entrepreneurial pathway, and internationalisation by design.

**Five faculty work domains, one coherent platform:**

| Domain | What Faculty Do | Primary Plugin | Agent Handle |
|---|---|---|---|
| **1. Teaching & Learning** | Course design, session delivery, assessment, mentoring, portfolio-first pedagogy | `reva.teaching-learning-reva` | `@reva-educator` |
| **2. Research** | Grants, publications, patents, PhD supervision, research brand | `reva.srujana-shodha` + `patent-generator` | `@reva-scholar` |
| **3. Academic Administration** | OBE/NBA, BOS governance, accreditation, NIRF, regulatory compliance | `reva.academic-admin-reva` | `@reva-admin` |
| **4. Consulting & Product Development** | Industry engagement, IP, MOUs, funded projects, startup mentoring | `reva.consulting-product-reva` + `patent-generator` | `@reva-innovator` |
| **5. Kaizen & Wellbeing** | Reflection, GPS goals, habit tracking, FDP, work-life integration | `reva.kaizen-wellbeing-reva` | `@reva-kaizen` |

`reva.academician-claw` (`@claw`) is the **personal intelligence layer** spanning all five domains — carrying memory, coordinated task management, writing support, and academic leadership across the full professional life.

The platform consists of:

* **Specialist Agents** — Role-based AI collaboration partners (not autonomous actors)
* **Skills** — Domain-specific knowledge and process modules loadable on demand
* **Workflows** — Human-AI collaborative procedures for end-to-end academic operations
* **Validators** — Quality-gate scripts for OBE compliance, portfolio integrity, AI-readiness, and accreditation

\---

## Faculty Role Architecture

Faculty at REVA University are knowledge professionals who operate simultaneously across five interconnected work domains. This platform provides dedicated agentic intelligence for each domain. `reva.academician-claw` (`@claw`) serves as the **personal intelligence layer** that coordinates across all five — carrying context, memory, and cross-domain coherence for each individual faculty member.

### Domain Overview

| # | Domain | What Faculty Do | Primary Plugin | Agent Handle |
|---|---|---|---|---|
| 1 | **Teaching & Learning** | Course design and delivery, assessment, mentoring, lab supervision, portfolio-first pedagogy, FDP | `reva.teaching-learning-reva` | `@reva-educator` |
| 2 | **Research** | Grant writing, publication, patents, PhD supervision, funding, collaboration, personal brand | `reva.srujana-shodha` + `patent-generator` | `@reva-scholar` |
| 3 | **Academic Administration** | OBE/NBA compliance, BOS governance, accreditation, regulatory reporting, CO attainment, NIRF data | `reva.academic-admin-reva` | `@reva-admin` |
| 4 | **Consulting & Product Development** | Industry engagement, IP commercialisation, MOUs, startup mentoring, funded projects, technology transfer | `reva.consulting-product-reva` + `patent-generator` | `@reva-innovator` |
| 5 | **Kaizen & Wellbeing** | Reflection, GPS goal planning, habit tracking, FDP planning, professional growth, work-life integration | `reva.kaizen-wellbeing-reva` | `@reva-kaizen` |

The personal intelligence layer `@claw` spans all five — managing weekly reviews, deep work, project management, writing, skill development, and academic leadership across every domain.

---

### Domain 1 — Teaching & Learning

Faculty are the primary architects of the student learning experience. Every task in this domain is a human-AI collaboration: AI drafts, structures, and audits; faculty decide, contextualise, and deliver.

#### Task Taxonomy

| Task Group | Tasks |
|---|---|
| **Curriculum & Course Design** | Programme PEO/PO/PSO design; course CO formulation (AI-augmented); CO-PO mapping; module sequencing; syllabus writing; prerequisite mapping; elective design; minor programme design |
| **Session Planning & Delivery** | Lesson plan preparation; session material design; active learning activity selection; Bloom's-level alignment; tutorial and practical planning; flipped classroom design |
| **Content Development** | Lecture notes; slide decks; case studies; problem sets; video scripts; reading lists; annotation guides; OER packaging |
| **Lab & Project Supervision** | Lab manual authoring; virtual lab design; PBL project design; capstone supervision; mini-project and final-year project guidance; industry project integration |
| **Assessment & Evaluation** | HOTS assignment design; question bank creation; rubric design; CIA planning; end-semester exam pattern; AI-readiness audit of assessments; viva voce design; peer assessment |
| **CO Attainment & Analytics** | Direct and indirect CO attainment computation; at-risk student identification; remediation planning; programme committee reporting |
| **Student Mentoring & Advising** | Srujana stage counselling; personalised pathway co-design; portfolio milestone review; placement readiness tracking; honours/remedial pathway assignment |
| **Faculty Development** | FDP participation; micro-teaching reflection; peer observation; pedagogical coaching; AI-era course redesign; learning from course review feedback |
| **Portfolio-First Pedagogy** | CO-to-artefact linkage; portfolio milestone planning; publication scaffolding; open-source contribution design; product brief generation |
| **EdTech & Platform** | LMS course setup; H5P/QuizBlast configuration; AI tutor calibration; accessibility compliance; digital syllabus publication |

#### Plugins, Agents, Workflows & Skills

| Task Group | Plugin | Key Agents | Workflows / Commands | Key Skills |
|---|---|---|---|---|
| Course Design | `reva.teaching-learning-reva` | `course-designer`, `curriculum-architect` | `/course-check`, `/design-course` | `co-ai-augmented-designer`, `co-po-mapping`, `blooms-aligner` |
| Session Planning | `reva.teaching-learning-reva` | `session-planner`, `content-developer` | `/session-check`, `/develop-session` | `unit-plan-designer`, `active-learning-strategies`, `scaffolding-designer` |
| Assessment | `reva.teaching-learning-reva` | `assessment-engineer` | `/assessment-check`, `/build-assessment` | `hots-assignment-designer`, `ai-ready-assessment-auditor`, `rubric-designer` |
| CO Attainment | `reva.academic-admin-reva` | `evaluation-analyst` | `/attainment`, `/evaluate-co` | `co-attainment-calculator`, `at-risk-detector`, `remediation-planner` |
| Portfolio-First | `reva.teaching-learning-reva` | `portfolio-architect` | `/portfolio-design` | `portfolio-co-linker`, `publication-scaffolder`, `portfolio-review-rubric-builder` |
| Lab & Projects | `reva.teaching-learning-reva` | `lab-designer`, `project-architect` | `/create-lab`, `/design-project` | `lab-manual-writer`, `pbl-project-designer`, `capstone-framework` |
| Student Mentoring | `reva.teaching-learning-reva` | `student-advisor`, `learning-pathway-designer` | `/personalize`, `/srujana-track` | `srujana-counsellor`, `personalised-pathway-engine`, `placement-readiness-tracker` |
| Faculty Development | `reva.academician-claw` | `learning-coach`, `reflection-facilitator` | `/weekly-review`, `/new-skill` | `pedagogical-coaching`, `ai-pedagogy-coach`, `fdp-programme-designer` |
| Personal Coordination | `reva.academician-claw` | `orchestrator`, `task-manager` | `/project-kickoff`, `/session-close` | `human-ai-handoff-protocol` |

---

### Domain 2 — Research

Faculty researchers carry a full research lifecycle — from idea through funding, execution, dissemination, and impact. AI accelerates and structures each stage; the faculty member retains intellectual ownership and institutional accountability.

#### Task Taxonomy

| Task Group | Tasks |
|---|---|
| **Research Identity & Competency** | Research profile building; ORCID/Scopus/Google Scholar management; competency gap identification; research interest sharpening; SDG alignment mapping |
| **Opportunity & Collaboration** | Research opportunity scanning (DST, SERB, ICSSR, UGC, Fulbright, industry); interdisciplinary collaboration mapping; co-investigator identification; international partner research |
| **Grant & Funding** | Grant proposal writing (SERB, DST, DBT, ICMR, industry); funding agency profiling; budget and timeline drafting; proposal review and scoring; revision cycles |
| **Research Execution** | Research methodology design; experiment or study design; data collection and analysis; research diary and log management; milestone tracking |
| **Publication Pipeline** | Literature review; manuscript writing; journal targeting and submission; revision and rebuttal; conference paper preparation; preprint management |
| **Patent & IP** | Invention disclosure; patentability assessment; prior art simulation; Indian patent application drafting (Form 1, 2, 3); patent prosecution support |
| **PhD Supervision** | Scholar onboarding; topic selection guidance; coursework advising; synopsis and research plan review; milestone monitoring; thesis review; publication coaching; viva preparation |
| **Research Leadership & Brand** | Research group formation; lab/centre establishment; personal brand building; media and science communication; mentoring junior faculty |
| **Book & Monograph Writing** | Book proposal; chapter outline; academic writing workflow; publisher targeting; peer review management |

#### Plugins, Agents, Workflows & Skills

| Task Group | Plugin | Key Agents | Workflows / Commands | Key Skills |
|---|---|---|---|---|
| Research Identity | `reva.srujana-shodha` | `competency-profiler`, `personal-brand-builder` | `/onboarding`, `/brand-sprint` | `PERSONAL_BRAND_STANDARD.md`, `SDG_MAPPING_STANDARD.md` |
| Opportunity Scouting | `reva.srujana-shodha` | `opportunity-scout`, `collaboration-architect` | `/opportunity-mapping` | `INDIA_RESEARCH_CONTEXT.md` |
| Grant Writing | `reva.srujana-shodha` | `funding-navigator`, `work-product-reviewer` | `/funding-hunt`, `/grant`, `/grant-check` | `GRANT_PROPOSAL_STANDARD.md` |
| Research Execution | `reva.srujana-shodha` | `research-pipeline-coach` | `/research-lifecycle` | `SCHOLARLY_WRITING_STANDARD.md` |
| Publication | `reva.srujana-shodha` | `journal-targeter`, `work-product-reviewer` | `/manuscript-check`, `/proposal-check` | `SCHOLARLY_WRITING_STANDARD.md`, `RESEARCH_ETHICS.md` |
| Patent & IP | `patent-generator` | *(workflow-driven)* | `01_input` → `08_export` | `patentWorkflow.js`, prior-art simulation |
| PhD Supervision | `reva.phd-scholar` *(planned)* | `guide-advisor`, `research-coach` | `/guide` | `REVA_PHD_REGULATIONS.md`, `PUBLICATION_STANDARDS.md` |
| SDG Impact Audit | `reva.srujana-shodha` | `competency-profiler` | `/sdg-impact-audit` | `SDG_MAPPING_STANDARD.md` |
| Personal Coordination | `reva.academician-claw` | `research-analyst`, `writing-partner` | `/deep-research`, `/project-kickoff` | `deep-research.md`, `skill-generator.md` |

---

### Domain 3 — Academic Administration

Administrative work is the institutional backbone of academic quality. Faculty carry governance, compliance, reporting, and committee responsibilities that keep the institution accredited, ranked, and operationally sound.

#### Task Taxonomy

| Task Group | Tasks |
|---|---|
| **OBE & CO Attainment** | CO-PO matrix maintenance; CIA and end-sem score entry and computation; direct and indirect attainment calculation; threshold review; remediation planning; course-end reports |
| **BOS & Curriculum Governance** | Curriculum change proposals; BOS agenda and documentation preparation; BOS minutes drafting; regulatory compliance checks (UGC, AICTE, NEP 2020); approval tracking |
| **NBA / NAAC Accreditation** | SAR criterion-wise documentation; OBE evidence packaging; NAAC DVV preparation; peer committee review; pre-visit compliance audit |
| **NIRF Reporting** | NIRF parameter data collection; annual data submission; parameter gap analysis; NIRF action plan contribution |
| **Regulatory Compliance** | UGC, AICTE, NEP 2020 compliance checks; academic programme approval documentation; fee regulation compliance; autonomy and affiliation governance |
| **Faculty Workload & Load Management** | Teaching load calculation and distribution; timetable inputs; workload reporting per REVA policy |
| **Academic Calendar & Lesson Planning** | Lesson plan generation and submission; teaching calendar management; session log maintenance; co-coverage documentation |
| **Examination Duties** | Question paper submission; CIA mark entry; end-semester invigilation coordination; result declaration documentation |
| **Programme Review & Committee Work** | Annual programme review preparation; PAC (Programme Advisory Committee) inputs; programme outcomes attainment reporting; departmental committee participation |
| **Student Records & Mentoring Records** | Mentor-mentee record maintenance; at-risk student tracking; remediation action records; attendance and performance documentation |

#### Plugins, Agents, Workflows & Skills

| Task Group | Plugin | Key Agents | Workflows / Commands | Key Skills |
|---|---|---|---|---|
| CO Attainment | `reva.academic-admin-reva` | `evaluation-analyst` | `/attainment` | `co-attainment-calculator`, `co-attainment-threshold-setter`, `attainment-heatmap-generator` |
| BOS Governance | `reva.academic-admin-reva` | `bos-governance-officer` | `/bos-approve` | `bos-proposal-formatter`, `bos-minutes-generator`, `regulatory-compliance-checker`, `curriculum-change-tracker` |
| NBA / NAAC | `reva.academic-admin-reva` | `accreditation-officer` | `/accredit` | `nba-sar-generator`, `naac-dvv-preparer`, `co-attainment-auditor` |
| NIRF | `reva.academic-admin-reva` | `nirf-accelerator` | `/nirf-accelerate` | `nirf-parameter-analyzer`, `nirf-data-pipeline`, `nirf-action-plan-generator` |
| Lesson Plan & Calendar | `reva.academic-admin-reva` | `evaluation-analyst` | `/attainment` | `academic-calendar-generator`, `programme-review-documenter` |
| Course Review Audit | `reva.teaching-learning-reva` | `pedagogy-advisor` | `/review-course` | `ai-ready-course-auditor`, `obe-compliance-checker`, `bloom-level-verifier` |
| Analytics & Reporting | `reva.academic-admin-reva` | `analytics-reporter` | `/analytics` | `learning-analytics-dashboard`, `co-attainment-report-generator`, `programme-review-reporter` |
| Personal Coordination | `reva.academician-claw` | `task-manager`, `academic-leadership-advisor` | `/weekly-review`, `/session-close` | `weekly-review.md` |

**Validator Support:** `obe-check.py`, `attainment-audit.py`, `accreditation-ready.py`, `nirf-data-validator.py`

---

### Domain 4 — Consulting & Product Development

Faculty who engage industry, build products, commercialise IP, or run funded consultancies are the bridge between REVA's academic excellence and real-world impact. This domain also covers faculty mentoring students through REVA NEST and Srujana Stage 4.

#### Task Taxonomy

| Task Group | Tasks |
|---|---|
| **Industry Consulting** | Engagement scoping and brief; client need analysis; proposal and deliverable structure; billing and MOU framework; progress reporting; deliverable review and sign-off |
| **IP & Patent Development** | Invention identification and disclosure; patentability assessment; prior art search; Indian patent application drafting; patent prosecution; commercialisation strategy |
| **MOU & Partnership Management** | MOU drafting (academic, research, industry); scope and milestone definition; review against REVA policy; renewal and amendment cycles; partner relationship tracking |
| **Industry-Funded Projects** | Project scoping and proposal; team assembly; milestone planning; financial tracking; progress reporting to sponsor; final deliverable and IP assignment |
| **Technology Transfer** | Technology readiness level (TRL) assessment; licensing frameworks; spin-off feasibility; REVA NEST linkage; investor readiness brief |
| **Startup & NEST Mentoring** | Mentoring student startups (Srujana Stage 4); business model review; pitch coaching; legal and IP setup guidance; investor introduction |
| **Product Development** | Product requirement specification; prototype planning; user testing design; product brief generation; market validation framework |
| **Experiential Learning Management** | Live industry problem integration into courses; industry mentor mapping; capstone industry linkage; advisory panel coordination; placement pipeline building |
| **Revenue & Commercialisation Strategy** | Consulting revenue tracking; IP royalty framework; grant-to-product pipeline; academic entrepreneurship policy navigation |

#### Plugins, Agents, Workflows & Skills

| Task Group | Plugin | Key Agents | Workflows / Commands | Key Skills |
|---|---|---|---|---|
| IP & Patent | `reva.consulting-product-reva` + `patent-generator` | *(workflow-driven)* | `/patent`, `01_input` → `08_export` | `PRODUCT_IP_GUIDELINES.md`, `patentWorkflow.js` |
| MOU & Partnership | `reva.consulting-product-reva` | *(workflow-driven)* | `/patent` (draft mode) | `PRODUCT_IP_GUIDELINES.md`, `industry-partner-mou-designer` |
| Industry Consulting | `reva.consulting-product-reva` | `stakeholder-validator` | *(consulting brief workflow)* | `industry-review-facilitator`, `feedback-synthesis-engine` |
| Experiential Learning | `reva.teaching-learning-reva` | `experiential-designer` | `/design-project` | `industry-project-integrator`, `srujana-industry-connect-builder` |
| Startup Mentoring | `reva.teaching-learning-reva` | `srujana-pathway-designer` | `/srujana-track` | `venture-launch-designer`, `product-research-scaffolder`, `entrepreneurship-studio-designer` |
| Research-to-Product Bridge | `reva.srujana-shodha` + `patent-generator` | `funding-navigator`, `work-product-reviewer` | `/research-lifecycle`, `/grant` | `GRANT_PROPOSAL_STANDARD.md`, `product-brief-generator` |
| Personal Coordination | `reva.academician-claw` | `idea-incubator`, `task-manager` | `/project-kickoff`, `/deep-research` | `project-kickoff.md` |

---

### Domain 5 — Kaizen & Wellbeing

Kaizen (改善 — continuous improvement) applied to academic professional life. Faculty are knowledge workers whose sustained effectiveness depends on intentional habits, regular reflection, purposeful goal-setting, and genuine wellbeing. This domain treats faculty development as a continuous personal improvement practice — not a one-off FDP event.

#### Task Taxonomy

| Task Group | Tasks |
|---|---|
| **GPS Goal Planning** | Annual and semester goal setting (Goals-Plans-Systems); priority identification; milestone definition; goal alignment with REVA Mission and personal Ikigai |
| **Weekly Review & Reflection** | Weekly review cycle (what went well, what didn't, what to carry forward); teaching reflection; research reflection; professional development review |
| **Habit Design & Tracking** | Habit identification and stacking; daily and weekly commitment tracking; habit streaks and recovery; energy management planning |
| **FDP Planning & Participation** | FDP needs identification; FDP selection and scheduling; post-FDP reflection and practice integration; STTP and workshop coordination |
| **Skill Development** | Identifying skill gaps (teaching, research, admin, tech); personal learning roadmap; certification planning; learning log maintenance |
| **Work-Life Integration** | Workload calibration; boundary-setting and recovery practices; seasonal planning (exam periods, conference seasons); sabbatical and leave planning |
| **Mental & Physical Wellbeing** | Stress signal recognition; wellbeing check-ins; physical health practices; mindfulness and focus practices; support resource navigation |
| **Professional Identity & Brand** | Academic profile maintenance; conference participation planning; professional community engagement; mentoring and being mentored |
| **Ikigai Alignment** | Mapping work to purpose (Ikigai — what I love, what I'm good at, what the world needs, what I can be paid for); career direction reviews; meaning-making practices |
| **Community & Peer Support** | Faculty learning circle participation; CoP engagement; peer support and accountability partnerships; alumni and industry network cultivation |

#### Plugins, Agents, Workflows & Skills

| Task Group | Plugin | Key Agents | Workflows / Commands | Key Skills |
|---|---|---|---|---|
| GPS Goal Planning | `reva.kaizen-wellbeing-reva` | *(workflow-driven)* | `/gps` | `gps-plan.md`, `PERSONAL_REFLECTION_RULES.md` |
| Weekly Review | `reva.academician-claw` | `reflection-facilitator`, `task-manager` | `/weekly-review` | `weekly-review.md` |
| Habit Tracking | `reva.kaizen-wellbeing-reva` | `habit-tracker` | `/gps` | `PERSONAL_REFLECTION_RULES.md` |
| Skill Development | `reva.academician-claw` | `learning-coach` | `/new-skill` | `skill-generator.md` |
| FDP Planning | `reva.kaizen-wellbeing-reva` | *(workflow-driven)* | `/gps` | `fdp-programme-designer` |
| Wellbeing | `reva.kaizen-wellbeing-reva` | *(workflow-driven)* | `/gps` | `PERSONAL_REFLECTION_RULES.md`, `wellbeing-curriculum-designer` |
| Research Ikigai | `reva.srujana-shodha` | `competency-profiler` | `/onboarding` | `IKIGAI_ALIGNMENT.md` *(planned in phd-scholar)* |
| Session Closure | `reva.academician-claw` | `memory-steward` | `/session-close` | `session-closer.md` |
| Personal Coordination | `reva.academician-claw` | `orchestrator`, `reflection-facilitator` | `/weekly-review`, `/session-close` | All claw workflows |

---

### Cross-Domain Personal Intelligence Layer

`reva.academician-claw` (`@claw`) is not domain-specific — it is the faculty member's **personal agentic workspace** that carries memory, context, and coherence across all five domains.

| Capability | How It Supports the 5 Domains |
|---|---|
| **Memory layer** (`soul.md`, `tasks.md`) | Remembers ongoing commitments across teaching, research, admin, consulting, and wellbeing — no re-briefing needed per session |
| **Weekly review workflow** | Surfaces cross-domain wins, blocks, and forward plans in one integrated review |
| **Writing partner agent** | Drafts and refines outputs across all five domains: teaching materials, grant proposals, admin reports, consulting briefs, reflection entries |
| **Task manager agent** | Holds the complete cross-domain task list with priorities, deadlines, and next actions |
| **Research analyst agent** | Supports deep dives for any domain: course design research, funding intelligence, industry trends, wellbeing literature |
| **Academic leadership advisor** | Supports committee roles, HOD/Dean functions, and institutional leadership responsibilities |
| **Idea incubator agent** | Captures and develops ideas from any domain: new courses, research questions, product concepts, consulting opportunities |
| **Learning coach agent** | Identifies and plans skill development across all five domains; tracks progress |
| **Reflection facilitator agent** | Structures reflective practice from teaching reviews, research setbacks, consulting outcomes, or personal growth |

---

### Plugin-to-Domain Responsibility Matrix

| Plugin | Domain 1 Teaching | Domain 2 Research | Domain 3 Admin | Domain 4 Consulting | Domain 5 Kaizen |
|---|---|---|---|---|---|
| `reva.teaching-learning-reva` | **Primary** | — | Supporting | Supporting | — |
| `reva.srujana-shodha` | — | **Primary** | — | Supporting | Supporting |
| `patent-generator` | — | Supporting | — | **Primary** | — |
| `reva.academic-admin-reva` | Supporting | — | **Primary** | — | — |
| `reva.consulting-product-reva` | — | — | — | **Primary** | — |
| `reva.kaizen-wellbeing-reva` | — | — | — | — | **Primary** |
| `reva.academician-claw` | Supporting | Supporting | Supporting | Supporting | Supporting |
| `reva.phd-scholar` *(planned)* | — | **Primary** (PhD) | — | — | Supporting |

\---

## Repository Structure

The SrujanaSangama repository is the private plugin marketplace for REVA University. It uses a **dual-engine architecture**: a single codebase deploys to both GitHub Copilot (via `package.json`) and Google Antigravity (via `plugin.json`). All agent intelligence lives in Markdown files; scripts handle only mechanical work.

```plaintext
SrujanaSangama/
├── AGENTS.md                        # AI team roles and Agentic Scrum sprint protocol
├── CONSTITUTION.md                  # Immutable project constitution — conventions, anti-patterns, gates
├── README.md                        # Platform overview and dual-engine architecture
├── CONTRIBUTING.md                  # Contributor guide
│
├── plan/                            # Spec contracts (primary build artifact)
│   ├── plan-*.prompt.md             # Feature spec files — approved before implementation begins
│   └── tasks-*.md                   # Atomic task lists — generated by Coordinator Agent
│
├── plugins/                         # Plugin implementations (compilation output of specs)
│   ├── phd-scholar/                 # [IN DEVELOPMENT] reva.phd-scholar — PhD scholar + guide advisor
│   ├── academician-claw/            # reva.academician-claw — Faculty personal agentic intelligence (OpenClaw v2)
│   ├── research-reva/               # reva.srujana-shodha — Faculty research advisor (SrujanaShodha)
│   ├── patent-generator/            # patent-generator — Indian patent extraction and drafting tool
│   ├── teaching-learning-reva/      # reva.teaching-learning-reva — Course design and audit agent pack
│   ├── academic-admin-reva/         # reva.academic-admin-reva — Admin, attainment, and compliance pack
│   ├── consulting-product-reva/     # reva.consulting-product-reva — IP, MOU, and consulting pack
│   └── kaizen-wellbeing-reva/       # reva.kaizen-wellbeing-reva — Kaizen and wellbeing coach
│
├── agents/                          # Root-level agent definitions (non-plugin, cross-cutting)
│   ├── course-buddy-builder.md      # Builds Course Buddy artefacts from course descriptors
│   └── course-buddies/              # Generated per-course buddy instances
│
├── skills/                          # Root-level skills loadable by any plugin
│   └── course-buddy-builder/        # SKILL.md + tools + references
│
├── specification/                   # Platform-level architecture and abstractions
│   ├── architecture.md              # Platform dual-engine architecture
│   ├── track_scope.md               # Scope and platform capabilities
│   ├── ADDIE.md                     # ADDIE instructional design flow
│   └── REVAskills/                  # Skill specifications (annual activities, NIRF, course design)
│
├── references/                      # Source of truth documents
│   ├── reva-PhD-regulations.md      # REVA University PhD Regulations 2025
│   └── The CSE Researcher's Handbook.md  # Empirical standards for CSE researchers
│
├── docs/                            # Guidelines and reference documentation
│   ├── architecture.md              # This file
│   ├── AISkills and Technologies.md # AI domain skills and tools map
│   └── Guidelines/                  # Course, mini-project, and final-year project guidelines
│
├── eval/                            # Evaluation data and CO attainment improvement backlog
├── knowledge/                       # Generated course knowledge bases (course-buddy-builder output)
└── Templates/                       # Schema and template files
```

### Plugin Anatomy

Every plugin under `plugins/` follows this canonical layout (enforced by CONSTITUTION.md):

```plaintext
plugins/<plugin-name>/
├── plugin.json          # Google Antigravity manifest (id, rules, workflows, mcpConfig)
├── package.json         # GitHub Copilot manifest (agent handle, slash commands)
├── mcp.json             # MCP server config (omit if no external tools needed)
├── README.md            # Plugin overview
├── rules/               # Identity, standards, and enforcement policies (Markdown)
├── workflows/           # Multi-phase prompt protocols (Markdown)
├── agents/
│   ├── core/            # Orchestrator + memory steward
│   └── <domain>/        # Specialist agents grouped by role
├── context/             # Committed .example template files (never real user data)
├── memory/              # Gitignored live memory (soul.md, tasks.md, etc.)
│   └── semantic/        # Project-level trackers and episodic logs
└── references/          # Plugin-local reference materials and school overlays
```

\---

## Plugin Registry

Current state of all plugins in the `plugins/` directory as of June 2026. Built under Agentic Scrum (see AGENTS.md and CONSTITUTION.md).

### Plugin Maturity Tiers

| Tier | Description | Examples |
|---|---|---|
| **Full Agentic System** | Orchestrator + Memory Steward + specialist agents + full memory layer. Personal intelligence for a specific role. | `academician-claw`, `research-reva` |
| **TRACK Agent Pack** | Single slash command, minimal rules layer. Focused on one workflow or audit task. | `teaching-learning-reva`, `academic-admin-reva`, `consulting-product-reva`, `kaizen-wellbeing-reva` |
| **Standalone Workflow Tool** | Sequential command pipeline with paired workflow+instructions files. No memory layer. | `patent-generator` |
| **In Development** | Spec approved; implementation sprint planned. | `phd-scholar` |

---

### `reva.academician-claw` — OpenClaw v2 — Faculty Personal Intelligence

**Tier:** Full Agentic System | **Agent handle:** `@claw` | **Version:** 2.0.0

**Purpose:** Personal agentic intelligence for REVA faculty — writing, research, task management, reflection, habits, learning coaching, and academic leadership. Prompt-native; no LLM API calls in scripts. Each faculty member maintains their own local `memory/` (gitignored).

| Layer | Files |
|---|---|
| **Rules** | `ORCHESTRATOR.md`, `PERSONA_ENGINE.md`, `PERMISSION_GUARDIAN.md` |
| **Workflows** | `weekly-review`, `project-kickoff`, `deep-research`, `skill-generator`, `session-closer` |
| **Core agents** | `orchestrator.md`, `memory-steward.md`, `skill-generator.md` |
| **Specialist agents** | `writing-partner`, `research-analyst`, `task-manager`, `learning-coach`, `reflection-facilitator`, `habit-tracker`, `idea-incubator`, `data-interpreter`, `code-architect`, `web-agent`, `computer-agent`, `academic-leadership-advisor` |
| **Slash commands** | `/weekly-review`, `/project-kickoff`, `/deep-research`, `/session-close`, `/new-skill` |
| **MCP** | Python server (`scripts/mcp_server.py`) |

---

### `reva.srujana-shodha` — SrujanaShodha — Faculty Research Advisor

**Tier:** Full Agentic System | **Agent handle:** `@reva-scholar` | **Version:** 2.0.0

**Purpose:** Personal research advisory intelligence for REVA faculty — competency profiling, opportunity identification, interdisciplinary collaboration, funding navigation, full research lifecycle coaching, work product review, and personal brand building.

| Layer | Files |
|---|---|
| **Rules** | `ADVISOR_IDENTITY.md`, `RESEARCH_ETHICS.md`, `INDIA_RESEARCH_CONTEXT.md`, `SDG_MAPPING_STANDARD.md`, `PERSONAL_BRAND_STANDARD.md`, `GRANT_PROPOSAL_STANDARD.md`, `SCHOLARLY_WRITING_STANDARD.md` |
| **Workflows** | `onboarding`, `opportunity-mapping`, `funding-hunt`, `research-lifecycle`, `brand-sprint`, `sdg-impact-audit`, `grant-check`, `manuscript-check`, `proposal-check`, `session-closer` |
| **Core agents** | `orchestrator.md`, `memory-steward.md` |
| **Specialist agents** | `competency-profiler`, `opportunity-scout`, `collaboration-architect`, `funding-navigator`, `research-pipeline-coach`, `journal-targeter`, `work-product-reviewer`, `personal-brand-builder` |
| **Slash commands** | `/grant`, `/manuscript-check`, `/proposal-check` |
| **MCP** | Node.js server (`dist/mcp-server.js`) connecting to REVA Scholar API |
| **Memory** | `soul.md`, `collaborators_plan.md`, `proposal_draft.md`; `semantic/funding-log.md`, `semantic/research-pipeline.md` |

---

### `patent-generator` — Indian Patent Extraction and Drafting Tool

**Tier:** Standalone Workflow Tool | **Version:** 0.1.0

**Purpose:** Guides users through extracting invention details, checking patentability, simulating prior art search, scoring, and generating a draft Indian patent application (Form 1, 2, 3). Agent-driven; no external API or JS execution.

| Layer | Files |
|---|---|
| **Workflows** | 8 paired workflow+instructions files: `01_input` → `02_extract` → `03_patentability` → `04_prior_art` → `05_scoring` → `06_draft_template` → `07_application` → `08_export` |
| **SKILL.md** | Root-level skill entry point |
| **lib/** | `patentWorkflow.js` (mechanical pipeline only) |
| **No rules or agents layer** | — |

---

### `reva.teaching-learning-reva` — Teaching & Learning Agent Pack

**Tier:** TRACK Agent Pack | **Agent handle:** `@reva-educator` | **Version:** 1.0.0

**Purpose:** Course design, session planning, content generation, and integrity audits. Integrates the `course-buddy-builder` skill for generating Obsidian wikis and Jupyter workbooks from course descriptors.

| Layer | Files |
|---|---|
| **Rules** | `ACADEMIC_INTEGRITY.md`, `COURSE_DESIGN_STANDARD.md`, `ASSESSMENT_QUALITY_STANDARD.md` |
| **Workflows** | `session-check`, `course-check`, `assessment-check` |
| **Slash commands** | `/audit`, `/course-check`, `/assessment-check`, `/build-course-buddy` |

---

### `reva.academic-admin-reva` — Academic Administration Agent Pack

**Tier:** TRACK Agent Pack | **Agent handle:** `@reva-admin` | **Version:** 1.0.0

**Purpose:** CO-PO attainment tracking, curriculum revision governance, accreditation metrics, and regulatory compliance audits (UGC, AICTE, NEP 2020).

| Layer | Files |
|---|---|
| **Rules** | `REGULATORY_COMPLIANCE.md` |
| **Workflows** | `attainment-check` |
| **Slash commands** | `/attainment` |

---

### `reva.consulting-product-reva` — Consulting & Product Development Agent Pack

**Tier:** TRACK Agent Pack | **Agent handle:** `@reva-innovator` | **Version:** 1.0.0

**Purpose:** IP claim drafting, MOU reviews, consulting engagement briefs, and experiential learning management.

| Layer | Files |
|---|---|
| **Rules** | `PRODUCT_IP_GUIDELINES.md` |
| **Workflows** | `patent-draft` |
| **Slash commands** | `/patent` |

---

### `reva.kaizen-wellbeing-reva` — Kaizen & Wellbeing Agent Pack

**Tier:** TRACK Agent Pack | **Agent handle:** `@reva-kaizen` | **Version:** 1.0.0

**Purpose:** Self-reflection coaching, habit and commitment trackers, FDP integrations, GPS goal planning, and wellbeing navigation for faculty.

| Layer | Files |
|---|---|
| **Rules** | `PERSONAL_REFLECTION_RULES.md` |
| **Workflows** | `gps-plan` |
| **Slash commands** | `/gps` |

---

### `reva.phd-scholar` — PhD Scholar & Guide Advisor *(IN DEVELOPMENT)*

**Tier:** Full Agentic System | **Agent handles:** `@phd-scholar` (default), `/guide` (supervisor mode) | **Target version:** 1.0.0

**Spec:** `plan/plan-revaPhDScholar.prompt.md`

**Purpose:** Guides REVA PhD scholars (and their supervisors) through all 9 lifecycle stages — from entrance prep and topic selection through coursework, active research, publication, thesis, patent, grant, and book writing. Phase 1 covers CSE/CSA; other schools use placeholders until branch-specific handbooks are provided. Dual-persona: default Scholar mode + `/guide` trigger activates supervisor view.

| Layer | Planned Files |
|---|---|
| **Rules** (8) | `SCHOLAR_IDENTITY.md`, `GUIDE_IDENTITY.md`, `REVA_PHD_REGULATIONS.md`, `RESEARCH_ETHICS.md`, `SCHOOL_ROUTING.md`, `PUBLICATION_STANDARDS.md`, `WELLBEING_STANDARD.md`, `IKIGAI_ALIGNMENT.md` |
| **Workflows** (16) | `00_onboarding` → `01_entrance-prep` → `02_coursework` → `03_synopsis` → `04_research-cycle` → `05_publication-pipeline` → `06_thesis-sprint` → `07_patent-workflow` → `08_grant-proposal` → `09_book-proposal` → `10_guide-dashboard` → `11_session-closer` → `12_daily-standup` → `13_stuck-triage` → `14_wellness-checkin` → `15_ikigai-audit` |
| **Core agents** | `orchestrator.md`, `stage-tracker.md` (auto-computes milestone dates from registration date + progress inputs) |
| **Scholar agents** (9) | `topic-scout`, `coursework-navigator`, `synopsis-builder`, `research-coach`, `publication-coach`, `thesis-writer`, `patent-agent`, `grant-agent`, `book-agent` |
| **Support agents** (4) | `daily-planner`, `blocker-breaker`, `wellness-companion`, `ikigai-compass` |
| **Guide agent** (1) | `guide-advisor` (activated by `/guide`) |
| **Memory** | `soul.md`, `ikigai.md`, `tasks.md`, `wellbeing-log.md`; `semantic/research-pipeline.md`, `publication-log.md`, `progress-reports.md`, `episodic/` |
| **Slash commands** | `/guide` (supervisor mode) |
| **Cross-plugin reuse** | `patent-generator` workflows (Stage 6), `research-reva` funding/manuscript workflows (Stages 4 & 7), `kaizen-wellbeing-reva` (wellbeing escalation) |
| **Phase 1 school** | CSE/CSA (references: `The CSE Researcher's Handbook`, SIGSOFT empirical standards) |
| **Regulation source** | `references/reva-PhD-regulations.md` — REVA University PhD Regulations 2025 |

---

## Agents

Specialist AI collaboration partners. Each agent works alongside humans — generating drafts, analyses, and structured options that humans review, adapt, and approve. Human decision authority is non-negotiable at every stage.

### Core Academic Lifecycle Agents

|Agent|Role in Human-AI Collaboration|Key Skills Used|
|-|-|-|
|`orchestrator`|Coordinates multi-agent workflows; surfaces the right agent at the right moment; routes human decisions to the correct governance step|parallel-agents, addie-phase-router, human-ai-handoff-protocol|
|`curriculum-architect`|Co-designs programmes with faculty curriculum committees; drafts PEOs at raised AI-era ambition; maps POs, PSOs, course structures, and minor frameworks for human review|peo-ai-era-designer, po-design, pso-design, programme-structure-designer, minor-framework-designer|
|`course-designer`|Partners with faculty to draft AI-augmented COs, CO-PO maps, module sequences, and portfolio linkage for faculty validation and approval|co-ai-augmented-designer, co-po-mapping, blooms-aligner, course-outline-writer, portfolio-co-linker|
|`session-planner`|Works with faculty to suggest active learning strategies, Bloom's-aligned activities, and proctored skill tasks for faculty selection and adaptation|unit-plan-designer, active-learning-strategies, scaffolding-designer, proctored-activity-designer|
|`content-developer`|Generates first-draft learning objects — notes, slides, case studies — for faculty review, editing, and contextualisation|lecture-notes-generator, slide-designer, case-study-developer, ai-ready-content-designer, oer-packager|
|`assessment-engineer`|Drafts HOTS assignments, proctored activities, rubrics, and question banks; flags AI-trivial tasks for human redesign|hots-assignment-designer, proctored-assessment-designer, ai-ready-assessment-auditor, rubric-designer|
|`lab-designer`|Designs lab manuals and virtual labs with lab faculty; every lab produces a portfolio artefact|lab-manual-writer, virtual-lab-designer, h5p-content-creator, portfolio-artefact-designer|
|`project-architect`|Co-designs PBL, capstone, and interdisciplinary projects with faculty; links every project to a portfolio output|pbl-project-designer, capstone-framework, interdisciplinary-project-connector, publication-scaffolder|
|`syllabus-publisher`|Generates course syllabus pages with CO-PO tables, certification map, portfolio milestones; faculty approves before publication|docusaurus-syllabus-publisher, syllabus-page-renderer, certification-credit-mapper|
|`evaluation-analyst`|Computes CO attainment, identifies gaps, and proposes remediation actions for faculty and HOD review|co-attainment-calculator, at-risk-detector, remediation-planner, co-attainment-report-generator|
|`pedagogy-advisor`|Reviews courses for pedagogical quality alongside faculty mentors; advises on Bloom's alignment, UDL, IKS, and enterprising-skills embedding|learning-design-principles, instructional-strategy-selector, universal-design-learning, iks-integration|
|`learning-pathway-designer`|Generates personalised pathways; faculty advisor and student co-decide the chosen path|learning-pathway-engine, honours-fast-track-designer, ai-tutor-configurator, diagnostic-assessment-designer|
|`community-facilitator`|Scaffolds peer learning groups, CoPs, and alumni connections; facilitation decisions rest with faculty and student leaders|collaborative-learning-designer, peer-mentoring-system, alumni-connect-integrator, community-of-practice-builder|
|`experiential-designer`|Designs field immersion, service learning, and design thinking experiences in co-creation with faculty and industry partners|experiential-learning-cycle, service-learning-designer, srujana-phase-router, design-thinking-workshop|
|`faculty-developer`|Generates feedback, coaching plans, and FDP recommendations for faculty reflection and action; the coaching relationship remains human|pedagogical-coaching, ai-pedagogy-coach, course-review-feedback, fdp-programme-designer|
|`student-advisor`|Provides faculty advisors with data-driven insights on at-risk students, Srujana readiness, and placement gaps; humans act on insights|at-risk-detector, placement-readiness-tracker, srujana-counsellor, remediation-planner|
|`analytics-reporter`|Builds dashboards and reports for programme committees, HODs, and VC office; humans interpret and decide|learning-analytics-dashboard, nirf-data-feed, co-attainment-report-generator, programme-review-reporter|
|`technology-integrator`|Configures and integrates EdTech platforms under IT and faculty direction; ensures accessibility and pedagogical fit|lms-course-builder, quizblast-setup, ai-personalization-stack, oci-infrastructure|

### Strategic, Governance, and Positioning Agents

|Agent|Role in Human-AI Collaboration|Key Skills Used|
|-|-|-|
|`futures-intelligence-scout`|AI and faculty teams jointly research WEF, NASSCOM, LinkedIn, and global education trends; AI synthesises, humans deliberate and decide on curriculum implications|wef-jobs-scanner, ai-era-role-mapper, nasscom-skills-mapper, linkedin-trends-analyzer, curriculum-currency-checker|
|`stakeholder-validator`|AI prepares validation instruments and synthesises feedback; industry experts and faculty conduct the conversations and take the decisions|industry-review-facilitator, advisory-panel-coordinator, feedback-synthesis-engine, validation-gap-reporter|
|`bos-governance-officer`|Prepares BOS proposals, compliance checks, agendas, and draft minutes; Board deliberates and decides — AI ensures nothing is missed|bos-proposal-formatter, regulatory-compliance-checker, bos-minutes-generator, curriculum-change-tracker|
|`enterprising-skills-designer`|Co-designs enterprising human skills curriculum with faculty; embeds initiative, adaptability, collaboration, ethics, communication, and creativity across all programmes|enterprising-co-designer, human-skills-rubric-builder, liberal-arts-integration-designer, wellbeing-curriculum-designer|
|`srujana-pathway-designer`|Architects Srujana pathway in collaboration with placement, industry relations, and REVA NEST teams; students navigate it with faculty mentors|srujana-stage-designer, internship-framework-builder, product-research-scaffolder, venture-launch-designer|
|`portfolio-architect`|Redesigns courses to be portfolio-first in partnership with faculty; every course produces a publication, product, open source contribution, or documented solution|portfolio-co-linker, publication-scaffolder, open-source-project-designer, product-brief-generator|
|`ai-personalization-engine`|Configures AI tutoring and personalised pathways; human advisors and faculty monitor and intervene|ai-tutor-configurator, personalised-pathway-engine, honours-fast-track-designer, remedial-ai-tutor-designer|
|`certification-integrator`|Maps NPTEL, SWAYAM, and professional certifications to programme credits; faculty and BOS validate equivalences|nptel-credit-mapper, swayam-integration-designer, professional-cert-aligner, mooc-portfolio-recognizer|
|`internationalization-agent`|AI and international relations office jointly research partners and co-draft frameworks; academic leadership and partner institutions negotiate and decide|twinning-programme-designer, dual-degree-framework, international-credit-aligner, global-minor-designer|
|`nirf-accelerator`|Analyses NIRF gaps and builds action plans for leadership review and prioritisation|nirf-parameter-analyzer, nirf-data-pipeline, admissions-excellence-tracker, placement-intelligence-reporter|
|`accreditation-officer`|Prepares NBA SAR, NAAC DVV, and institutional documentation; peer committees and leadership review and certify|nba-sar-generator, naac-dvv-preparer, co-attainment-auditor, programme-review-documenter|
|`interdisciplinary-connector`|Maps minor opportunities across all four models; faculty and programme committees decide which minors to activate|minor-framework-designer, intra-reva-minor-designer, nptel-swayam-minor-designer, international-minor-designer|

\---

## Skills

Modular knowledge domains loaded on demand. Each skill supports human-AI collaboration — generating structured drafts, frameworks, and analyses that humans review, adapt, and approve.

\---

### ADDIE Process Skills

|Skill|Description|
|-|-|
|`addie-phase-router`|Determines active ADDIE phase; routes to appropriate agents; surfaces human decision gates at each phase transition|
|`needs-analysis`|Supports stakeholder interviews and learner needs synthesis; task analysis; performance gap identification; futures intelligence integration|
|`context-analysis`|Environmental, institutional, stakeholder, and technology context analysis including AI-era readiness and REVA mission alignment|
|`learner-profile-builder`|Entry behaviour mapping, prior knowledge, Srujana stage, AI tool proficiency, and liberal arts interests|
|`learning-design-principles`|Gagne's Nine Events, Merrill's First Principles, Dick and Carey model; holistic and wellbeing-aligned design|
|`instructional-strategy-selector`|Matches teaching strategies to outcomes, Bloom's levels, and enterprising human-skills threads|
|`formative-evaluation`|Mid-process evaluation checkpoints and human-reviewed iteration triggers|
|`summative-evaluation`|End-of-cycle evaluation, revision planning, and improvement loop documentation|
|`addie-documentation-packager`|Compiles full ADDIE artefact set for any course or programme for BOS submission|
|`human-ai-handoff-protocol`|Defines at each workflow step what AI drafts, what humans decide, and what requires formal governance approval|

\---

### OBE and NBA Compliance Skills

|Skill|Description|
|-|-|
|`peo-ai-era-designer`|PEO formulation raised to AI-augmented ambition: graduates expected to perform at 5–6 year experience levels through AI co-working; aligned to REVA Vision of global, sustainable, technologically advanced graduates|
|`po-design`|NBA 12 Program Outcomes alignment including AI literacy, ethical AI use, sustainability, and global competency|
|`pso-design`|Program Specific Outcomes reflecting AI-era specialisations, industry-defined competencies, and REVA mission|
|`co-ai-augmented-designer`|CO writing embedding AI-augmentation assumptions: tasks achievable with AI raise the cognitive floor; assessment focuses on judgment, synthesis, creation, and ethics|
|`co-po-mapping`|CO-PO and CO-PSO mapping matrix with strength levels (1/2/3); includes enterprising skills PO linkage|
|`co-attainment-calculator`|Direct (CIA, end-sem) and indirect (surveys, portfolio review) attainment computation|
|`co-attainment-threshold-setter`|Target setting and threshold definition for CO attainment decisions|
|`obe-compliance-checker`|Gap analysis against NBA OBE requirements; flags missing portfolio CO linkages and human-skills COs|
|`bloom-level-verifier`|Verifies CO verb alignment with Bloom's taxonomy; ensures HOTS dominance in AI-era courses|
|`nba-documentation`|SAR criterion-wise documentation and self-assessment scoring|
|`attainment-heatmap-generator`|CO-PO coverage heatmap for programme review committees|
|`portfolio-co-linker`|Links every CO to a tangible portfolio artefact: paper, product, open source contribution, or documented solution|

\---

### Future Intelligence Skills

*AI and faculty curriculum committees jointly research and deliberate: AI scans and synthesises; humans validate, contextualise, and decide on curriculum implications.*

|Skill|Description|
|-|-|
|`wef-jobs-scanner`|Scans WEF Future of Jobs Reports for emerging roles, declining roles, and reskilling priorities; generates structured briefing for committee review|
|`ai-era-role-mapper`|Maps AI-era job roles (Prompt Engineer, AI Product Manager, MLOps, Responsible AI Specialist, etc.) to curriculum competency threads; presented as discussion input for faculty and industry panels|
|`nasscom-skills-mapper`|Integrates NASSCOM FutureSkills Prime and sector skill reports into curriculum gap analysis for human validation|
|`linkedin-trends-analyzer`|LinkedIn Economic Graph insights: in-demand skills, role evolution, hiring trends — compiled as faculty briefing inputs|
|`industry-skills-taxonomy-builder`|Builds and maintains a living REVA skills taxonomy; faculty and industry advisors review and update each cycle|
|`curriculum-currency-checker`|Flags outdated topics, tools, and skills against current industry practice; presents flagged list for faculty action|
|`ai-job-role-profile-generator`|Generates detailed AI-era job role profiles (responsibilities, skills, tools, CO linkage) as starting input for curriculum committee discussions|
|`international-education-trends-scanner`|Scans QS, THE, and global curriculum benchmarks; supports academic leadership in programme positioning discussions|
|`futures-briefing-packager`|Compiles all intelligence into a structured futures briefing document for the annual human-led curriculum review workshop|

\---

### Stakeholder Governance Skills

*Industry validation and BOS approval are fundamentally human deliberative processes. AI prepares, structures, and documents — humans conduct the conversations, exercise judgment, and record the decisions.*

|Skill|Description|
|-|-|
|`industry-review-facilitator`|Designs structured industry expert review sessions: agenda, review instruments, discussion prompts — humans conduct the conversations|
|`advisory-panel-coordinator`|Manages industry advisory board composition, meeting cadence, agenda, and recommendation documentation|
|`feedback-synthesis-engine`|Synthesises multi-stakeholder feedback into structured curriculum change proposals for faculty committee consideration|
|`validation-gap-reporter`|Documents validation-identified gaps with priority classification and proposed curriculum response for faculty action|
|`bos-proposal-formatter`|Formats curriculum change proposals for BOS review to UGC/AICTE regulatory standards|
|`bos-agenda-generator`|Generates Board of Studies meeting agendas with supporting documents and member briefing materials|
|`bos-minutes-generator`|Drafts structured BOS minutes with decisions, action items, and approval records for secretary review and sign-off|
|`curriculum-change-tracker`|Tracks all changes through proposal → industry validation → BOS deliberation → approval → implementation → evaluation|
|`external-examiner-briefing`|Prepares external examiner briefing documents, question paper review forms, and structured feedback formats|
|`regulatory-compliance-checker`|UGC, AICTE, NEP 2020, and REVA internal policy compliance checks on every curriculum proposal before BOS submission|
|`industry-partner-mou-designer`|Designs structured industry partnership MOUs with curriculum, placement, and research commitments for leadership negotiation|

\---

### Curriculum Design Skills

|Skill|Description|
|-|-|
|`programme-structure-designer`|Credit distribution, semester layout, theory-lab-project balance, Srujana stage integration, and REVA mission alignment|
|`prerequisite-mapper`|Course dependency and knowledge pre-requisite mapping with visual dependency graph|
|`curriculum-gap-analyzer`|Industry relevance, technology currency, and skills gap analysis using futures intelligence feeds and advisory inputs|
|`curriculum-revision-tracker`|Version control and change management through BOS approval cycle|
|`honours-curriculum-designer`|Honours with Research and Honours with Technology Commercialisation tracks for fast learners with early Srujana Stage 3 access|
|`elective-pool-designer`|Open, professional, and discipline elective baskets incorporating NPTEL, SWAYAM, certifications, and liberal arts options|
|`minor-framework-designer`|Overarching minor programme architecture supporting all four minor models|
|`intra-reva-minor-designer`|Intra-REVA interdisciplinary minors: CS taking Design/Management, Engineering taking Life Sciences/Arts|
|`nptel-swayam-minor-designer`|NPTEL and SWAYAM credit-bearing minor tracks with CO-PO mapping and BOS-approved equivalences|
|`industry-micro-credential-minor`|Industry-defined micro-credential minors: AWS Cloud, Google AI, NASSCOM Data, Cisco Networking|
|`international-minor-designer`|Joint minors co-designed and co-delivered with international partner universities|
|`interdisciplinary-thread-mapper`|Cross-programme shared modules, joint project threads, and minor bridges|
|`liberal-studies-integrator`|Embeds performing arts, literature, sports, sustainability, and creative disciplines into programme structure per REVA Mission|
|`ug-pg-pathway-designer`|3+1+1 and 4+1 integrated pathway design under UGC 2022 regulations|
|`nep-credit-framework`|NEP 2020 credit framework, multiple entry-exit, Academic Bank of Credits integration|

\---

### Course Design Skills

|Skill|Description|
|-|-|
|`course-outline-writer`|Full course outline with AI-augmented COs, units, certification links, portfolio expectations, and Srujana stage indicator|
|`module-sequencer`|Module and unit ordering with progressive learning scaffolding toward a portfolio artefact|
|`unit-plan-designer`|Unit-level instructional plan with session breakdown, Bloom's level, active learning strategy, and human-skills thread|
|`blooms-aligner`|Bloom's taxonomy alignment review; ensures HOTS dominance across AI-era course design|
|`contact-hour-planner`|Teaching hour distribution across theory, tutorial, practicum, portfolio work, and proctored skill sessions|
|`co-coverage-checker`|Ensures every CO is covered across modules, sessions, assessments, and portfolio tasks|
|`ai-ready-course-auditor`|Audits for AI-readiness: AI-trivial tasks flagged for redesign; proctored activities balance AI-assisted work|
|`industry-input-integrator`|Advisory panel and futures intelligence inputs embedded into course design with documented traceability|

\---

### Content Development Skills

|Skill|Description|
|-|-|
|`lecture-notes-generator`|Structured lecture notes with concepts, worked examples, self-check questions, and reflection prompts|
|`slide-designer`|Pedagogically rich, REVA-branded slide decks (PPTX and HTML) with active learning cues|
|`case-study-developer`|Real-world case studies; preference for Indian industry, social enterprise, and sustainability contexts aligned to REVA Mission|
|`problem-set-creator`|Graded problem sets across Bloom's levels; higher-order problems require judgment, synthesis, and creative application|
|`ai-ready-content-designer`|Content designed for AI-era engagement: problems requiring creativity, ethical reasoning, stakeholder empathy, and societal judgment|
|`reading-list-curator`|Primary readings, OERs, NPTEL modules, SWAYAM courses, arXiv papers, and textbooks curated by faculty with AI support|
|`video-script-writer`|Educational video scripts with learning objectives, narration, and visual storyboards|
|`oer-packager`|Open Educational Resource packaging in SCORM and xAPI formats|
|`microlearning-packager`|Bite-sized learning objects for spaced delivery and mobile access|
|`annotation-guide-creator`|Guided annotation layers for papers, industry reports, and primary sources|
|`wellbeing-content-integrator`|Embeds mental health, physical wellbeing, and values-based reflection into course content per REVA Vision|

\---

### Assessment and Evaluation Skills

|Skill|Description|
|-|-|
|`hots-assignment-designer`|Designs Higher Order Thinking assignments that are enjoyable, complex, AI-era relevant, and produce portfolio artefacts|
|`proctored-assessment-designer`|Designs in-person supervised assessments that verify genuine student brain and hand competency|
|`ai-ready-assessment-auditor`|Audits every assignment: AI-trivial tasks flagged; HOTS dominance verified; proctored components balanced; portfolio artefact authenticity checked|
|`assignment-enjoyability-auditor`|Reviews assignments for student motivation, creative latitude, real-world relevance, and authentic sense of accomplishment|
|`portfolio-assessment-builder`|Portfolio-based assessment linking tasks to publications, products, open source, or documented solutions|
|`question-bank-generator`|Multi-level Bloom's question banks tagged by CO, unit, difficulty, and AI-augmentation assumption|
|`rubric-designer`|Analytic and holistic rubrics for assignments, projects, presentations, portfolio review, and enterprising-skills assessment|
|`quiz-designer`|Formative quiz design for QuizBlast and H5P platforms|
|`exam-pattern-designer`|CIA and end-sem exam patterns with CO coverage matrix; separates AI-assisted from proctored components|
|`peer-assessment-designer`|Structured peer review instruments and calibration protocols|
|`viva-voce-designer`|Oral examination question sets and rubrics — essential for verifying genuine student understanding in AI era|
|`continuous-assessment-planner`|CIA calendar with component weights, CO mapping, and portfolio milestone alignment|
|`remediation-planner`|Structured below-threshold intervention, re-assessment, and AI tutor support|
|`survey-instrument-designer`|Course-end and programme-level indirect attainment surveys|

\---

### Lab, Project, and Experiential Learning Skills

|Skill|Description|
|-|-|
|`lab-manual-writer`|Lab manuals with aim, theory, procedure, observation, inference, and portfolio output brief|
|`virtual-lab-designer`|Simulation-based virtual labs using PhET, LabXchange, or custom builds|
|`pbl-project-designer`|Problem and project-based learning scenarios with milestones and portfolio deliverables|
|`capstone-framework`|Capstone phases, milestones, rubrics, and public exhibition; every capstone produces a public-facing artefact|
|`interdisciplinary-project-connector`|Multi-department, cross-domain project design with minor credit linkage and shared rubrics|
|`industry-project-integrator`|Live industry problem statements, mentor mapping, and delivery protocols|
|`hackathon-designer`|Hackathon challenge design, judging rubrics, and sprint scaffolding|
|`design-thinking-workshop`|Human-centred design studio facilitation for wicked problems and social innovation|
|`service-learning-designer`|Community-linked service learning with reflection frameworks and social impact portfolio — directly expressing REVA's mission of sustainability and universal values|
|`field-immersion-planner`|Industry visit, field study, and immersive experience planning|
|`research-project-scaffolder`|Undergraduate research from hypothesis to paper, patent, or conference presentation|
|`open-source-contribution-designer`|GitHub issues, PRs, documentation, and community engagement as assessed, portfolio-generating activities|
|`publication-scaffolder`|Course project → literature context → writing → conference or journal submission pipeline|
|`product-brief-generator`|Product requirement briefs from course COs linking learning to deliverable products and solutions|
|`entrepreneurship-studio-designer`|Ideation-to-venture studio curriculum with REVA NEST integration and Srujana Stage 4 linkage|
|`liberal-arts-experiential-designer`|Performing arts, literature, and sports-integrated learning experiences per REVA Mission|

\---

### Pedagogy and Instructional Design Skills

|Skill|Description|
|-|-|
|`active-learning-strategies`|Flipped classroom, think-pair-share, jigsaw, gallery walk, muddiest point, Socratic seminar|
|`experiential-learning-cycle`|Kolb's experiential cycle embedded into course and session design|
|`scaffolding-designer`|Cognitive and procedural scaffolding for complex learning tasks|
|`differentiated-instruction`|Multi-level content and assessment supporting fast-track honours and slow-learner remedial paths|
|`universal-design-learning`|UDL: multiple means of representation, engagement, and expression|
|`metacognitive-prompts`|Self-reflection, think-alouds, and metacognitive strategy prompts — critical in AI era to prevent cognitive offloading|
|`iks-integration`|Indian Knowledge Systems: Panchakosha, Guru-Shishya, Vivekananda's man-making education, contextual wisdom, sustainability ethics|
|`holistic-learning-designer`|Cognitive, affective, psychomotor, social, and spiritual dimensions of learning aligned to REVA Vision of wellbeing for all|
|`inquiry-based-learning`|Guided and open inquiry sequence design|
|`proctored-activity-designer`|Supervised in-person activities ensuring genuine brain and hand competency|
|`flipped-classroom-designer`|Pre-class, in-class, and post-class activity sequencing|
|`collaborative-pedagogy-designer`|Course structures making collaboration, co-creation, and peer accountability pedagogically central|

\---

### Enterprising Human Skills

*The durable human advantage in the AI era — qualities that AI cannot replicate and that give REVA graduates their distinctive edge across every career path. Broader than entrepreneurship; fundamental to every professional and citizen.*

|Skill|Description|
|-|-|
|`enterprising-co-designer`|Writes Enterprising Human Skills COs for every course: initiative, adaptability, collaborative agency, and value creation|
|`critical-thinking-embedder`|Designs tasks requiring analysis of ambiguous problems, evaluation of competing arguments, and synthesis of novel solutions|
|`communication-skill-designer`|Oral, written, visual, and cross-cultural communication tasks embedded as portfolio deliverables across all semesters|
|`ethical-reasoning-designer`|Ethical case scenarios, responsible AI use, societal impact analysis, and value-based decision tasks aligned to REVA universal values mission|
|`leadership-collaboration-designer`|Team dynamics, constructive conflict, peer leadership, and accountable collaboration structures in projects and labs|
|`adaptability-resilience-designer`|Growth mindset tasks, iterative redesign challenges, failure reflection protocols, and adaptive learning experiences|
|`creativity-and-initiative-designer`|Open-ended tasks rewarding original approaches, divergent thinking, and self-initiated exploration|
|`financial-legal-literacy-designer`|Personal finance, IP basics, contracts, and startup compliance embedded as practical course threads|
|`global-and-cultural-competence-designer`|Cross-cultural collaboration, global professional norms, and international perspectives in course projects|
|`sustainability-values-designer`|Sustainability thinking, social responsibility, and universal values embedded into projects per REVA Mission|
|`wellbeing-curriculum-designer`|Physical, mental, and social wellbeing integrated into design: study skills, stress resilience, community care|
|`human-skills-rubric-builder`|Observable, assessable rubrics for enterprising human skills across academic, project, and portfolio contexts|
|`human-advantage-portfolio-designer`|Designs the human skills portfolio: communication artefacts, ethical analyses, leadership reflections, social impact evidence|
|`ai-human-collaboration-designer`|Teaches students to use AI as a tool while retaining ownership of judgment, creativity, ethics, and human relationships|
|`liberal-arts-integration-designer`|Integrates performing arts, literature, creative writing, sports, and humanities into degree programmes per REVA Mission|

\---

### Srujana Pathway Skills

*Srujana (Sanskrit: सृजन — to create, to bring into being) is REVA's structured entrepreneurial progression pathway. Designed fresh in this architecture through collaboration among faculty, placement, industry relations, REVA NEST, and students.*

|Skill|Description|
|-|-|
|`srujana-phase-router`|Routes students to the appropriate Srujana stage based on academic year, portfolio readiness, and faculty mentor assessment|
|`srujana-s1-skill-builder`|Stage 1 — Skill Formation: structured skill development through courses, labs, certifications, and foundational portfolio artefacts (Semesters 1–4)|
|`srujana-s2-internship-designer`|Stage 2 — Real World Immersion: structured industry or research internship with COs, mentor mapping, and reflective portfolio (Semesters 3–6)|
|`srujana-s3-product-research-designer`|Stage 3 — Create and Contribute: product development, research project, patent filing, open source contribution, or published paper (Semesters 5–7)|
|`srujana-s4-venture-designer`|Stage 4 — Enterprise: venture design through REVA NEST; pitch preparation, business model, legal setup, investor readiness (Semester 7–8 and beyond)|
|`srujana-portfolio-integrator`|Integrates all four Srujana stage artefacts into a unified enterprising portfolio — the student's journey from learner to creator|
|`srujana-milestone-tracker`|Tracks student progress through stages with milestone gates, faculty mentor check-ins, and advisory reviews|
|`srujana-counsellor`|Guides students and advisors in identifying Srujana stage, choosing electives, certifications, and internship tracks|
|`internship-framework-builder`|Institutional internship credit framework: guidelines, mentor mapping, assessment rubrics, credit recognition|
|`product-research-scaffolder`|Stage 3 scaffold: problem identification, ideation, prototype, IP check, paper writing, or open source pipeline|
|`venture-launch-designer`|REVA NEST integration, pitch scaffolding, team formation, financial modelling, and founder mindset development|
|`srujana-industry-connect-builder`|Builds the industry and alumni mentor network supporting Srujana Stages 2, 3, and 4|

\---

### Portfolio and Publication Skills

|Skill|Description|
|-|-|
|`portfolio-architecture-designer`|Designs the student's cumulative 4-year portfolio with semester-by-semester artefact milestones across all courses|
|`portfolio-co-linker`|Links every CO to a tangible output: paper, product, open source contribution, or documented solution|
|`publication-scaffolder`|Course project → literature context → drafting → review → conference or journal submission pipeline|
|`open-source-contribution-designer`|GitHub issues, PRs, documentation, and community engagement as assessed portfolio-generating activities|
|`product-artefact-designer`|Product spec documents, prototypes, technical demos, and solution briefs as course outputs|
|`portfolio-review-rubric-builder`|Analytic rubrics for portfolio artefact quality, originality, and public impact|
|`digital-portfolio-publisher`|Guides students in publishing portfolios on GitHub Pages, personal sites, or REVA's showcase platform|
|`placement-portfolio-connector`|Links portfolio artefacts directly to placement readiness and recruiter-facing profiles|
|`portfolio-integrity-auditor`|Verifies portfolio artefacts represent genuine student work; distinguishes AI-assisted from student-authored elements|

\---

### AI Personalisation Skills

*AI personalises the learning journey; human advisors and faculty monitor, guide, and intervene.*

|Skill|Description|
|-|-|
|`ai-tutor-configurator`|Configures AI tutoring for slow learners: adaptive pacing, Socratic prompts, concept reinforcement, progress reports to faculty|
|`personalised-pathway-engine`|Generates individualised pathways based on diagnostics and CO performance; faculty advisor co-signs the plan with student|
|`intelligent-intervention-designer`|AI-triggered interventions: at-risk alerts, content recommendations, peer group suggestions — humans act on signals|
|`ai-study-companion-builder`|Student-facing AI study companion: question answering, practice generation, reflection prompting, wellbeing check-ins|
|`honours-fast-track-designer`|Fast-track pathways for high performers: advanced electives, research immersion, early Srujana Stage 3 access|
|`remedial-ai-tutor-designer`|Dedicated AI tutor for slow learners with extra tutorial credits, paced re-learning, and faculty check-in rubrics|
|`ai-personalization-stack`|Technical architecture for AI personalisation: LLM APIs, learner data models, adaptive content delivery|
|`learning-velocity-tracker`|Tracks individual learning velocity and surfaces adjustment recommendations for faculty advisor review|
|`peo-readiness-profiler`|AI-assisted profiling of each student's readiness to meet raised AI-era PEOs by graduation; shared with student and advisor|

\---

### Certification and MOOC Integration Skills

|Skill|Description|
|-|-|
|`nptel-credit-mapper`|Maps NPTEL courses to programme electives and minors with CO-PO equivalence documentation for BOS approval|
|`swayam-integration-designer`|SWAYAM course integration: credit transfer, assessment equivalence, and progress tracking|
|`professional-cert-aligner`|Aligns industry certifications (AWS, Google Cloud, Microsoft, NASSCOM, Cisco, PMI) to COs and electives|
|`mooc-portfolio-recognizer`|Recognises MOOC completion artefacts as portfolio evidence within CO attainment computation|
|`certification-track-designer`|Designs structured certification tracks within degree programmes|
|`external-credit-auditor`|Audits externally earned credits for regulatory compliance and CO-PO integrity before BOS ratification|
|`mooc-quality-screener`|Screens MOOCs for academic rigour, currency, and alignment before faculty recommendation|

\---

### Adaptive and Personalised Learning Skills

|Skill|Description|
|-|-|
|`learning-pathway-engine`|Personalised pathway generation based on diagnostic and CO performance data|
|`diagnostic-assessment-designer`|Pre-course and mid-course diagnostic instruments|
|`remedial-content-designer`|Below-threshold support content and guided re-learning sequences|
|`enrichment-content-designer`|Advanced extension content for high performers leading to honours or early Srujana Stage 3|
|`spaced-repetition-planner`|Forgetting curve-based review scheduling and retrieval practice design|
|`mastery-learning-designer`|Mastery-based progression with competency gating|
|`self-paced-module-designer`|Self-paced online modules with checkpoint assessments for flexible learners|

\---

### Social and Community Learning Skills

|Skill|Description|
|-|-|
|`collaborative-learning-designer`|Group work structures, roles, protocols, and interdependence design|
|`peer-mentoring-system`|Peer mentor-mentee matching; Srujana senior-junior pairing; training materials|
|`community-of-practice-builder`|CoP setup for faculty learning circles, student discipline communities, and alumni networks|
|`study-circle-facilitator`|Study group design guides, norms, facilitation prompts, AI tutor integration|
|`social-annotation-setup`|Hypothesis and Perusall social reading layer configuration|
|`alumni-connect-integrator`|Alumni mentorship, guest lecture series, industry immersion, and Srujana Stage 2/3 mentor network|
|`industry-expert-connector`|Industry advisory panel, expert guest series, practitioner-in-residence, and live project partnerships|
|`discourse-forum-designer`|Asynchronous academic discussion forum design and moderation guides|

\---

### EdTech and Platform Integration Skills

|Skill|Description|
|-|-|
|`lms-course-builder`|Moodle and Canvas course structure, activity sequencing, gradebook, and portfolio submission setup|
|`h5p-content-creator`|H5P interactives: branching scenarios, drag-and-drop, video quizzes, timelines|
|`docusaurus-syllabus-publisher`|Docusaurus-based course syllabus pages with OBE metadata, CO-PO tables, portfolio milestones, Srujana stage|
|`quizblast-setup`|QuizBlast platform configuration for large-cohort formative assessment|
|`ai-tool-integration`|AI tool scaffolding for student and faculty use with clear ethical use guidelines|
|`oci-infrastructure`|OCI Free Tier deployment for EdTech tools, AI tutors, and agent services|
|`video-platform-integration`|YouTube, Panopto, and Kaltura video content management|
|`accessibility-checker`|WCAG 2.1 accessibility compliance for all digital educational content|
|`mobile-learning-adapter`|Responsive content adaptation for mobile learner access|
|`scorm-xapi-packager`|SCORM and xAPI packaging for LMS delivery and learning activity tracking|

\---

### Internationalisation Skills

*AI and human international relations teams co-research; partner university relationships are built and sustained through human dialogue and trust.*

|Skill|Description|
|-|-|
|`twinning-programme-designer`|Twinning programme design: credit equivalence, quality assurance protocols, student mobility, and joint delivery|
|`dual-degree-framework`|Dual degree architecture: partner selection criteria, joint COs, shared assessment, mutual credential recognition|
|`international-credit-aligner`|Maps REVA courses to ECTS, US credit hours, and APQF frameworks|
|`mobility-programme-planner`|Inbound and outbound student mobility: summer schools, semester abroad, research exchange, faculty mobility|
|`international-curriculum-benchmarker`|Benchmarks REVA programmes against top 100 global university curricula in the same discipline|
|`joint-research-programme-designer`|Joint research and innovation programmes aligned to REVA's sustainability and technology vision|
|`english-medium-course-designer`|Courses for international student cohorts with language support and cultural contextualisation|
|`global-minor-designer`|Minors co-designed and co-delivered with international partner universities|
|`international-partner-intelligence`|AI-assisted research on potential partner universities by ranking, discipline strength, and REVA Vision alignment; humans negotiate and decide|

\---

### Learning Analytics and Reporting Skills

|Skill|Description|
|-|-|
|`learning-analytics-dashboard`|Student progress, engagement, portfolio health, CO attainment, and Srujana stage analytics|
|`co-attainment-report-generator`|Automated CO attainment reports for programme committees|
|`at-risk-detector`|Early warning indicators; AI-triggered alerts reviewed by faculty advisors before action|
|`engagement-tracker`|LMS engagement: logins, submissions, forum activity, portfolio uploads, AI tutor interaction|
|`placement-readiness-tracker`|CO and portfolio mapping to placement readiness and recruiter benchmarks|
|`faculty-effectiveness-analyzer`|Teaching effectiveness from student feedback and attainment correlation|
|`programme-review-reporter`|Annual programme review data and narrative for programme committees and BOS|
|`cohort-progression-analyzer`|Year-on-year cohort progression and outcome trend analysis|
|`nirf-data-feed`|Continuous NIRF parameter data collection feeding the NIRF Accelerator|
|`srujana-progress-tracker`|Cohort-level Srujana progress across all four stages|
|`portfolio-quality-analyzer`|Portfolio artefact quality distribution across cohorts; gaps flagged for faculty action|
|`wellbeing-indicator-tracker`|Tracks student wellbeing signals from platform engagement, performance, and advisor interactions|

\---

### Institutional Positioning Skills

|Skill|Description|
|-|-|
|`nirf-parameter-analyzer`|Analyses REVA's position on each NIRF parameter; identifies priority gaps with estimated rank impact|
|`nirf-data-pipeline`|Automates NIRF data collection, cleaning, and submission-ready packaging|
|`nirf-action-plan-generator`|NIRF improvement action plans by parameter with owner, timeline, and measurable target|
|`admissions-excellence-tracker`|Student quality metrics, programme appeal signals, and competitive positioning for admissions|
|`placement-intelligence-reporter`|Placement analytics: company quality, role seniority, CTC trends, sector diversity, portfolio-to-placement correlation|
|`programme-reputation-builder`|Programme visibility: accreditations, student success stories, alumni achievements, and research output|
|`research-output-tracker`|Faculty and student publications, patents, and funded projects for ranking inputs and institutional reputation|

\---

### Accreditation and Documentation Skills

|Skill|Description|
|-|-|
|`nba-sar-generator`|NBA SAR generation by criterion with evidence links and self-assessment scoring|
|`naac-dvv-preparer`|NAAC DVV documentation, metric data preparation, and supporting evidence|
|`nirf-data-collector`|NIRF parameter data collection and submission format preparation|
|`co-attainment-auditor`|OBE audit trail documentation for NBA inspection readiness|
|`academic-calendar-generator`|Lesson plan, teaching calendar, and session log generation|
|`programme-review-documenter`|Board of Studies documentation and curriculum revision records|
|`accreditation-gap-analyzer`|Gaps between current programme state and accreditation criteria with remediation plan|
|`regulatory-compliance-checker`|UGC, AICTE, NEP 2020, and REVA policy compliance checks|

\---

### Faculty Development Skills

|Skill|Description|
|-|-|
|`pedagogical-coaching`|Faculty pedagogy improvement plans — AI drafts; faculty mentor reviews and owns the coaching relationship|
|`ai-pedagogy-coach`|Guides faculty in designing AI-era courses: raising ambition, redesigning assessments, embedding AI literacy|
|`course-review-feedback`|Structured feedback on course design, portfolio linkage, AI-readiness, and enterprising-skills presence|
|`micro-teaching-evaluator`|Micro-teaching observation rubrics and structured debrief guides|
|`research-integration-advisor`|Research-teaching nexus: connecting faculty research to course content and student projects|
|`faculty-load-optimizer`|Teaching load calculation, distribution, and optimisation per REVA policy|
|`fdp-programme-designer`|FDP design aligned to OBE, active learning, AI-era pedagogy, and portfolio-first principles|
|`mentorship-programme-designer`|New faculty mentorship programme design and milestone planning|

\---

### Output Format Skills

|Skill|Description|
|-|-|
|`pptx-generator`|REVA-branded PowerPoint for sessions, BOS presentations, and academic events|
|`docx-generator`|REVA-branded Word documents for course materials, proposals, and reports|
|`html-page-builder`|Interactive HTML educational pages with REVA branding|
|`pdf-exporter`|PDF export of syllabi, BOS proposals, and accreditation documents|
|`syllabus-page-renderer`|OBE syllabus page with CO-PO tables, certification linkage, portfolio expectations, and Srujana stage indicator|
|`excel-report-generator`|CO attainment, analytics, NIRF data, and programme review Excel reports|
|`infographic-renderer`|Visual summaries for concepts, pathways, programme structures, Srujana journey, and institutional positioning|

\---

## Workflows

Human-AI collaborative procedures for end-to-end academic operations. Invoke with `/command`. Every workflow identifies **human decision gates** explicitly — points where AI stops and humans deliberate.

### Core Academic Workflows

|Command|Description|
|-|-|
|`/analyze`|Human-AI needs analysis: AI scans futures data and learner profiles; faculty and curriculum committee deliberate and decide|
|`/design-curriculum`|AI-assisted programme design — PEOs (raised) → POs → PSOs → course map → minor basket → MOOC/cert tracks; faculty committee approves each phase; BOS provides formal approval|
|`/design-course`|AI drafts AI-augmented COs, CO-PO map, module sequence, assessment plan, and portfolio linkage; course faculty reviews, refines, and formally approves|
|`/generate-syllabus`|AI generates syllabus page in Docusaurus, HTML, and DOCX; faculty reviews and approves before publication|
|`/develop-session`|AI generates first-draft session materials; faculty edits, contextualises, and approves before delivery|
|`/create-lab`|AI designs lab manual or virtual lab; lab faculty validates procedure, safety, and portfolio output brief|
|`/design-project`|AI drafts PBL or capstone design; project faculty and industry mentors co-refine and approve|
|`/build-assessment`|AI generates HOTS assignments, proctored tasks, rubrics, and question banks; faculty reviews for AI-readiness and enjoyability|
|`/evaluate-co`|Automated CO attainment computation; results reviewed by faculty and programme committee before action|

### Intelligence and Governance Workflows

|Command|Description|
|-|-|
|`/futures-scan`|AI and faculty jointly compile WEF, NASSCOM, LinkedIn, and global trends into a structured briefing; curriculum committee deliberates and decides on implications|
|`/validate-industry`|AI prepares instruments and synthesises feedback; industry experts and faculty conduct dialogue and record decisions; AI documents outcomes|
|`/bos-approve`|AI prepares proposal, compliance check, agenda, and draft minutes; Board of Studies deliberates and records formal decisions|

### Personalisation and Pathway Workflows

|Command|Description|
|-|-|
|`/srujana-track`|AI assesses stage readiness and generates pathway plan; student and faculty advisor co-design the personal Srujana journey|
|`/personalize`|AI diagnostic → pathway → fast-track or remedial assignment → AI tutor setup; faculty advisor monitors and adjusts throughout|
|`/portfolio-design`|AI audits COs, proposes artefact types, and drafts milestone plan; faculty approves and contextualises|

### Certification and Global Workflows

|Command|Description|
|-|-|
|`/certify-map`|AI maps NPTEL/SWAYAM/professional certs to CO-PO equivalences; faculty and BOS validate and formally approve credit allocation|
|`/internationalize`|AI researches partner universities and drafts credit alignment frameworks; international relations office and academic leadership negotiate, decide, and build the relationship|

### Institutional Positioning Workflows

|Command|Description|
|-|-|
|`/nirf-accelerate`|NIRF gap analysis → AI-generated action plan → leadership review and prioritisation → data pipeline activation → progress dashboard|
|`/review-course`|Comprehensive course review: Bloom's audit + CO coverage + assessment AI-readiness + portfolio completeness + human-skills presence + curriculum currency|
|`/faculty-develop`|AI generates pedagogy gap analysis and coaching plan; faculty mentor facilitates the development conversation and relationship|
|`/analytics`|Analytics dashboard: CO attainment, engagement, portfolio health, Srujana progress, at-risk flags, placement readiness — reviewed by programme committee|
|`/community-learn`|Social learning setup: peer groups, CoP scaffolding, alumni/expert connect, study circles|
|`/accredit`|NBA or NAAC documentation generation; peer committee and leadership review before submission|
|`/orchestrate`|Multi-agent coordination for complex operations spanning ADDIE phases, governance cycles, and institutional priorities|

\---

## Skill Loading Protocol

```plaintext
User Request / Academic Trigger / Institutional Signal
                    ↓
         ADDIE Phase Router
                    ↓
     Agent Selection (role-based)
                    ↓
  ┌─────────────────────────────────────┐
  │   Human-AI Handoff Check            │
  │   What does AI draft or analyse?    │
  │   What does the human decide?       │
  │   Is industry validation required?  │
  │   Is BOS governance required?       │
  └─────────────────────────────────────┘
                    ↓
      Skill Description Match
                    ↓
          Load SKILL.md
                    ↓
    Read references/ (templates, rubrics,
    frameworks, WEF/NASSCOM feeds, BOS
    proposal formats, REVA policy docs)
                    ↓
    Read scripts/ (computation, validation,
    generation, portfolio audit, NIRF data)
                    ↓
    Apply REVA branding to all outputs
                    ↓
  ┌─────────────────────────────────────┐
  │   Governance Gate                   │
  │   Industry validation needed?       │
  │   → Route to /validate-industry     │
  │   BOS approval needed?              │
  │   → Route to /bos-approve           │
  └─────────────────────────────────────┘
```

### Skill Structure

```plaintext
skill-name/
├── SKILL.md           # (Required) Metadata, instructions, frameworks,
│                      #   human decision points, governance gates
├── scripts/           # (Optional) Python/Bash computation and generation
├── references/        # (Optional) Templates, rubric banks, framework docs,
│                      #   CO banks, WEF/NASSCOM data, REVA policy documents
└── assets/            # (Optional) REVA logos, brand tokens, illustration sets
```

\---

## Validators

Quality-gate scripts enforcing OBE compliance, portfolio integrity, AI-readiness, pedagogical standards, and accreditation readiness. All outputs are reviewed by humans before any action is taken.

### Validator Scripts

|Script|Purpose|When to Use|
|-|-|-|
|`obe-check.py`|CO-PO mapping completeness, Bloom's level correctness, CO coverage, portfolio linkage, human-skills CO presence|Before course finalisation|
|`attainment-audit.py`|Attainment data integrity, threshold logic, direct + indirect merge, audit trail completeness|Before NBA submission|
|`pedagogy-scan.py`|Bloom's level distribution, active learning frequency, UDL compliance, enterprising-skills CO presence, liberal arts integration|Course design review|
|`ai-readiness-audit.py`|Flags AI-trivial assignments; verifies HOTS dominance; checks proctored activity balance; validates portfolio artefact authenticity|Before each semester launch|
|`portfolio-integrity-check.py`|Every CO linked to artefact type; portfolio milestone plan exists; rubrics present; Srujana stage artefacts tracked; digital publication pathway defined|Course design and semester review|
|`content-qa.py`|Content completeness, session-to-CO linkage, format compliance, and currency vs. futures intelligence flags|Before content deployment|
|`accreditation-ready.py`|Full pre-visit audit: SAR completeness, OBE trail, NIRF data, evidence links, regulatory compliance|Pre-NBA / NAAC visit|
|`nirf-data-validator.py`|NIRF parameter data completeness, format compliance, year-on-year consistency|Quarterly and pre-submission|

### What They Check

**obe-check.py:**

* CO verb alignment with Bloom's taxonomy; HOTS ≥ 60% across course
* CO-PO mapping completeness; all POs addressed at programme level
* AI-augmented COs present where appropriate
* Portfolio CO linkage for every CO
* Enterprising Human Skills CO in every course
* Attainment threshold defined

**ai-readiness-audit.py:**

* Assignment completable by AI without student judgment → flag for redesign
* HOTS (Analyse / Evaluate / Create) ≥ 60% of total marks
* Proctored assessment present to verify genuine student competency
* Portfolio artefact requires authentic student work with verifiable authorship
* AI collaboration is explicit, bounded, and declared — not hidden
* Enjoyability indicators: creative latitude, real-world relevance, student choice present

**portfolio-integrity-check.py:**

* Every CO linked to a portfolio artefact type
* Portfolio milestone plan with semester timing in course outline
* Portfolio rubrics exist for every artefact type
* Cumulative 4-year portfolio architecture visible at programme level
* Srujana stage artefacts mapped across all four stages
* Digital publication pathway defined for at least one course per semester

**accreditation-ready.py** — all above checks plus:

* SAR section completeness by NBA criterion
* Supporting evidence files present and correctly named
* Programme outcome attainment computed at programme level
* Faculty qualification and load data consistent
* Infrastructure data complete
* NIRF parameter data current and validator-cleared

\---

## Quick Reference

### Domain 1 — Teaching & Learning (`@reva-educator`)

|Need|Agent|Workflow / Command|Key Skills|
|-|-|-|-|
|New programme with raised PEOs|`curriculum-architect`|`/design-curriculum`|peo-ai-era-designer, programme-structure-designer, nep-credit-framework|
|Future-of-jobs intelligence for curriculum|`futures-intelligence-scout`|`/futures-scan`|wef-jobs-scanner, nasscom-skills-mapper, futures-briefing-packager|
|Industry validation of curriculum|`stakeholder-validator`|`/validate-industry`|industry-review-facilitator, feedback-synthesis-engine|
|AI-augmented course design|`course-designer`|`/design-course`|co-ai-augmented-designer, co-po-mapping, blooms-aligner|
|Enterprising skills in curriculum|`enterprising-skills-designer`|`/design-course`|enterprising-co-designer, human-skills-rubric-builder, liberal-arts-integration-designer|
|Session material development|`session-planner` + `content-developer`|`/develop-session`|active-learning-strategies, slide-designer, proctored-activity-designer|
|AI-ready assessment design|`assessment-engineer`|`/build-assessment`|ai-ready-assessment-auditor, hots-assignment-designer, proctored-assessment-designer|
|Portfolio-first course redesign|`portfolio-architect`|`/portfolio-design`|portfolio-co-linker, publication-scaffolder, portfolio-review-rubric-builder|
|Srujana pathway for students|`srujana-pathway-designer`|`/srujana-track`|srujana-s1–s4-skills, srujana-portfolio-integrator, internship-framework-builder|
|Minors (all four models)|`interdisciplinary-connector`|`/design-curriculum`|intra-reva-minor-designer, nptel-swayam-minor-designer, industry-micro-credential-minor, international-minor-designer|
|NPTEL / SWAYAM / certifications|`certification-integrator`|`/certify-map`|nptel-credit-mapper, professional-cert-aligner, mooc-portfolio-recognizer|
|Lab or project design|`lab-designer` + `project-architect`|`/create-lab`, `/design-project`|lab-manual-writer, pbl-project-designer, capstone-framework|
|Honours / fast learners|`learning-pathway-designer`|`/personalize`|honours-fast-track-designer, enrichment-content-designer|
|AI tutor / slow learners|`ai-personalization-engine`|`/personalize`|ai-tutor-configurator, remedial-ai-tutor-designer|
|Student Srujana counselling|`student-advisor`|`/srujana-track`|srujana-counsellor, placement-readiness-tracker, at-risk-detector|
|Comprehensive course review|`pedagogy-advisor`|`/review-course`|ai-ready-course-auditor, obe-compliance-checker, bloom-level-verifier|
|Twinning / dual degrees|`internationalization-agent`|`/internationalize`|twinning-programme-designer, dual-degree-framework, international-credit-aligner|
|Learning analytics|`analytics-reporter`|`/analytics`|learning-analytics-dashboard, at-risk-detector, srujana-progress-tracker|

### Domain 2 — Research (`@reva-scholar`)

|Need|Agent|Workflow / Command|Key Skills|
|-|-|-|-|
|Research profile and onboarding|`competency-profiler`|`/onboarding`|PERSONAL_BRAND_STANDARD.md, SDG_MAPPING_STANDARD.md|
|Research opportunity and funding scan|`opportunity-scout` + `funding-navigator`|`/opportunity-mapping`, `/funding-hunt`|INDIA_RESEARCH_CONTEXT.md, GRANT_PROPOSAL_STANDARD.md|
|Grant proposal writing|`funding-navigator` + `work-product-reviewer`|`/grant`, `/grant-check`|GRANT_PROPOSAL_STANDARD.md|
|Manuscript writing and journal targeting|`journal-targeter` + `work-product-reviewer`|`/manuscript-check`|SCHOLARLY_WRITING_STANDARD.md, RESEARCH_ETHICS.md|
|Research proposal review|`work-product-reviewer`|`/proposal-check`|SCHOLARLY_WRITING_STANDARD.md|
|Full research lifecycle coaching|`research-pipeline-coach`|`/research-lifecycle`|SCHOLARLY_WRITING_STANDARD.md|
|Interdisciplinary collaboration mapping|`collaboration-architect`|`/opportunity-mapping`|INDIA_RESEARCH_CONTEXT.md|
|SDG impact audit|`competency-profiler`|`/sdg-impact-audit`|SDG_MAPPING_STANDARD.md|
|Personal research brand sprint|`personal-brand-builder`|`/brand-sprint`|PERSONAL_BRAND_STANDARD.md|
|Indian patent application drafting|*(workflow-driven)*|`01_input` → `08_export`|patentWorkflow.js, prior-art simulation|
|PhD scholar guidance (planned)|`guide-advisor`|`/guide`|REVA_PHD_REGULATIONS.md, PUBLICATION_STANDARDS.md|
|Deep research on any topic|`research-analyst` (`@claw`)|`/deep-research`|deep-research.md|

### Domain 3 — Academic Administration (`@reva-admin`)

|Need|Agent|Workflow / Command|Key Skills|
|-|-|-|-|
|CO attainment computation|`evaluation-analyst`|`/attainment`, `/evaluate-co`|co-attainment-calculator, co-attainment-threshold-setter, attainment-heatmap-generator|
|Board of Studies governance|`bos-governance-officer`|`/bos-approve`|bos-proposal-formatter, bos-minutes-generator, regulatory-compliance-checker|
|NBA / NAAC accreditation documentation|`accreditation-officer`|`/accredit`|nba-sar-generator, naac-dvv-preparer, co-attainment-auditor|
|NIRF ranking improvement|`nirf-accelerator`|`/nirf-accelerate`|nirf-parameter-analyzer, nirf-action-plan-generator, research-output-tracker|
|Regulatory compliance check|`bos-governance-officer`|`/bos-approve`|regulatory-compliance-checker, curriculum-change-tracker|
|Programme review reporting|`analytics-reporter`|`/analytics`|programme-review-reporter, co-attainment-report-generator|
|Admissions and placements intelligence|`nirf-accelerator`|`/analytics`|admissions-excellence-tracker, placement-intelligence-reporter|
|Faculty development planning|`faculty-developer`|`/faculty-develop`|fdp-programme-designer, pedagogical-coaching|
|Complex multi-phase operations|`orchestrator`|`/orchestrate`|addie-phase-router, parallel-agents, human-ai-handoff-protocol|

### Domain 4 — Consulting & Product Development (`@reva-innovator`)

|Need|Agent|Workflow / Command|Key Skills|
|-|-|-|-|
|IP claim drafting and patent application|*(workflow-driven)*|`/patent`, `01_input` → `08_export`|PRODUCT_IP_GUIDELINES.md, patentWorkflow.js|
|MOU and partnership drafting|*(workflow-driven)*|`/patent` (draft mode)|industry-partner-mou-designer, PRODUCT_IP_GUIDELINES.md|
|Industry consulting brief|`stakeholder-validator`|*(consulting brief workflow)*|industry-review-facilitator, feedback-synthesis-engine|
|Experiential learning with industry|`experiential-designer`|`/design-project`|industry-project-integrator, srujana-industry-connect-builder|
|Student startup and NEST mentoring|`srujana-pathway-designer`|`/srujana-track`|venture-launch-designer, product-research-scaffolder|
|Research-to-product pipeline|`funding-navigator` + `work-product-reviewer`|`/research-lifecycle`, `/grant`|product-brief-generator, GRANT_PROPOSAL_STANDARD.md|
|Idea development and incubation|`idea-incubator` (`@claw`)|`/project-kickoff`|project-kickoff.md|

### Domain 5 — Kaizen & Wellbeing (`@reva-kaizen`)

|Need|Agent|Workflow / Command|Key Skills|
|-|-|-|-|
|Annual/semester GPS goal planning|*(workflow-driven)*|`/gps`|gps-plan.md, PERSONAL_REFLECTION_RULES.md|
|Weekly cross-domain review|`reflection-facilitator` + `task-manager` (`@claw`)|`/weekly-review`|weekly-review.md|
|Habit design and tracking|`habit-tracker` (`@claw`)|`/weekly-review`|PERSONAL_REFLECTION_RULES.md|
|Skill gap identification and learning roadmap|`learning-coach` (`@claw`)|`/new-skill`|skill-generator.md|
|FDP planning and post-FDP integration|*(workflow-driven)*|`/gps`|fdp-programme-designer|
|Wellbeing check-in and support navigation|*(workflow-driven)*|`/gps`|PERSONAL_REFLECTION_RULES.md|
|Session closure and memory update|`memory-steward` (`@claw`)|`/session-close`|session-closer.md|
|Ikigai and career direction review|`competency-profiler` (`@reva-scholar`)|`/onboarding`|SDG_MAPPING_STANDARD.md|

\---

## Design Principles

Every agent, skill, workflow, and validator in this platform is grounded in the following non-negotiable principles:

* **Human-AI collaboration at every step** — AI accelerates, drafts, analyses, and surfaces options; humans exercise judgment, build relationships, and take final decisions. No curriculum, assessment, or governance action proceeds on AI output alone.
* **REVA Vision as the compass** — Technologically advanced, sustainable, global, dedicated to the wellbeing of all. Every design choice is tested against this.
* **REVA Mission as the design brief** — Learner-centred, entrepreneurial stewardship, liberal arts and creative disciplines, collaboration, universal values, and sustainability. These are structural requirements, not decorative statements.
* **ADDIE as the operating backbone** — Analysis always precedes Design; Development is validated before Implementation; Evaluation feeds back into every phase.
* **NBA OBE as the quality contract** — Every course artefact is traceable to a CO; every CO is mapped to a PO; attainment is computed, evidenced, and audited.
* **PEOs raised for the AI era** — Graduates are expected to perform at 5–6 year experience levels through AI co-working; COs embed this; assessments test judgment, synthesis, creation, and ethics.
* **Portfolio-first learning** — Every course produces a tangible artefact: a publication, product, open source contribution, or documented solution.
* **Enterprising human skills as the durable advantage** — Critical thinking, communication, ethical reasoning, adaptability, collaboration, initiative, and creativity are non-negotiable across every programme. These are what AI cannot replace.
* **Srujana as the student's personal narrative** — Every student has a visible journey from skill formation to real-world contribution. The platform scaffolds and celebrates this journey.
* **Differentiation by design** — Fast learners are accelerated through honours tracks and early Srujana Stage 3. Slow learners are supported through AI tutors, extra tutorials, and personalised pathways. No student is without a forward path.
* **Bloom's taxonomy as the learning compass** — Outcomes, content, activities, and assessments are coherently aligned; HOTS dominates in AI-era courses.
* **AI-readiness of assessments** — Trivially AI-completable tasks are redesigned. Proctored activities verify genuine competency. AI-assisted work is explicit, bounded, and declared.
* **Futures intelligence as a living input** — Curriculum is updated by WEF, NASSCOM, LinkedIn, and global signals — synthesised by AI, deliberated by humans, approved by BOS.
* **Governance integrity** — Industry validation and BOS approval are human deliberative processes. AI prepares and documents; the Board decides.
* **Internationalisation as a long-term human relationship** — Twinning, dual degrees, and joint programmes are built on trust, sustained dialogue, and mutual academic respect — supported by AI intelligence, driven by human partnership.
* **NIRF Top 100 as the institutional north star** — Every platform capability connects to research output, academic quality, placements, faculty excellence, and global engagement.
* **REVA brand on every output** — All documents, pages, and slides conform to REVA visual identity, typography, and brand voice.

\---

*REVA University — Educate to Enterprise
"To become a technologically advanced, sustainable global university dedicated to the wellbeing of all"
Author: Dr. Sanjay Chitnis (in collaboration with Claude.ai)
Platform Version: 0.2  | Academic Year: 2026–27*


