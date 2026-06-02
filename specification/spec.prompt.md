# TRACK Platform: Private AI Agent & Skill Plugin Marketplace Scope

## 1. Purpose
Grounded in REVA University's Vision — to become a technologically advanced, sustainable global university dedicated to the wellbeing of all — this platform provides a modular, extensible, private marketplace supporting all aspects of TRACK (Teaching/Learning, Research, Academic Administration, Consulting & Product Development, Kaizen) at individual, department, school, and university levels. Aligned with REVA Summit targets and national/international benchmarks, the marketplace enables dual-engine deployment of campus-customized AI agents and skills.

> Full capability detail, agent catalogue, skill registry, and workflow specifications are maintained in `specification/architecture.prompt.md`. This document is the executive scope summary from which development, release, and deployment plans are derived.

## 2. Core Principles
- **Private Marketplace Gating**: Secure, role-based distribution of agents and skills to allowed teams (faculty, department staff, specific student bodies).
- **Dual-Engine Standard**: Write core prompt logic, system guidelines, and MCP tools once; run natively in both Google Antigravity and GitHub Copilot.
- **Empower Faculty and Students**: Facilitate self-reflection, Goal-Plan-Systems (GPS) planning, academic integrity monitoring, and continuous improvement (Kaizen).
- **Evidence-driven & Compliant**: Generate structural evidence for accreditations (NIRF, NAAC, NBA) and continuous feedback without bypass shortcuts.
- **Human-AI Collaboration First**: AI drafts, analyses, and synthesises; humans review, contextualise, and hold final decision authority at every governance gate. No curriculum decision, course approval, or assessment goes forward on AI output alone.
- **Enterprising Student as the North Star**: Every course, assessment, and pathway is designed to produce a graduate who creates value — through technology, service, research, or leadership. Broader than entrepreneurship; fundamental to every professional and citizen.

## 3. Marketplace Capabilities
- **Unified Registry Indexing**: Central indexing (`.antigravity-marketplace/marketplace.json` and `.github/copilot-marketplace.json`) for seamless campus workstation configuration.
- **Dual Host Integration**: Automatic resolution of system prompt boundaries (`rules/`) and custom workflows/commands (`workflows/`) within both GEMINI-run environments and Node.js-based IDE extensions.
- **Model Context Protocol (MCP) Bridge**: Secure, standard-based remote tool integration to query student rosters, curriculum DBs, and placement tracking systems.
- **Accreditation and Quality Validation**: Local validator hooks (Python-first, technology-agnostic) checking OBE compliance, Bloom's taxonomy levels, and assignment enjoyability before plugins are baselined.
- **AI Personalisation & Adaptive Learning**: Diagnostic-driven personalised pathways, AI tutoring, at-risk detection, and remediation — with human advisor oversight at every stage.
- **Srujana Pathway Engine**: Four-stage student progression from Skill Formation (S1) through Real-World Immersion (S2), Create & Contribute (S3), to Enterprise (S4) via REVA NEST.
- **Learning Analytics & Institutional Intelligence**: CO attainment dashboards, NIRF data pipelines, placement readiness tracking, and programme review reporting.
- **EdTech Platform Integration**: Moodle, H5P, QuizBlast, Docusaurus, and OCI deployment orchestrated under faculty and IT direction.
- **Internationalisation Support**: Twinning, dual-degree, credit alignment, and student/faculty mobility planning with international partner universities.
- **Faculty Development Support**: FDP design, pedagogical coaching, AI-era course redesign guidance, and research-teaching nexus advisory.

## 4. Example Marketplace Plugins & Skills

### Teaching/Learning (`plugins/teaching-learning-reva/`)
- **Syllabus & Lesson Planner**: Generates interactive SCORM/OER syllabus structures.
- **Academic Assistant**: Enforces REVA academic integrity guidelines; audits all assessments for AI-triviality and verifies genuine student competency across all submission types.
- **Outcome Mapping & Attainment Tracker**: Direct/indirect CO attainment computation.
- **AI-Ready Assessment & Portfolio Engine**: Links every course outcome to a tangible portfolio artefact; flags AI-trivial tasks for faculty redesign.
- **Personalised Learning Pathway**: Configures AI tutoring, fast-track honours, and remedial support; faculty advisors monitor and intervene.
- **Session & Content Developer**: Generates active-learning session plans, Bloom's-aligned materials, and first-draft content for faculty review and contextualisation.

### Research (`plugins/research-reva/`)
- **Publication & Citation Tracker**: Fetches publication data for NIRF/NAAC pipelines.
- **Grant Assistant**: Scans funding bodies and drafts matching proposals.
- **Scholar Writing Assistant**: Scaffolds manuscript structure, citation networks, and publication submission pipelines.

### Academic Administration (`plugins/academic-admin-reva/`)
- **Accreditation Evidence Generator**: Prepares structured reports for NBA SAR/NAAC DVV metrics.
- **MOU and Regulatory Reviewer**: Verifies compliance with UGC, AICTE, and NEP 2020 frameworks.
- **BOS Governance Officer**: Prepares Board of Studies proposals, compliance checks, agendas, and draft minutes for human deliberation and approval.
- **NIRF & Rankings Accelerator**: Analyses NIRF parameter gaps, builds action plans, and feeds continuous data pipelines for institutional positioning.
- **REVA Summit & Faculty KRA Tracker**: Tracks progress against REVA Summit institutional targets and aligns individual faculty KRA/KPA delivery to institutional commitments.

### Consulting & Product Development (`plugins/consulting-product-reva/`)
- **Srujana Pathway Scaffold**: Guides students from skills to internships, product development, and REVA NEST incubation.
- **IP & Patent Architect**: Drafts patent claims and structures design briefs from project outputs.
- **Portfolio-First Architect**: Redesigns courses to produce publications, products, open source contributions, or documented solutions as verifiable outcomes.
- **Consulting Engagement Advisor**: Coordinates corporate connect MOUs, guest practitioner schedules, and live industry project briefs.

### Kaizen / Personal Wellbeing (`plugins/kaizen-wellbeing-reva/`)
- **Faculty Kaizen Coach**: Personal development coaching based on SrujanaBuddy GPS planning.
- **Wellbeing Navigator**: Confidential self-reflection and mental wellbeing support utilizing Hitaishin logic.
- **Student Srujana Counsellor**: Guides students and faculty advisors in identifying Srujana stage readiness and choosing electives, certifications, and internship tracks.

## 5. Next Steps
- Finalize registry permissions map for CSE and school-wide testing.
- Launch central marketplace registry on campus workstation instances.
- Onboard core department plugins into the private registry index.
