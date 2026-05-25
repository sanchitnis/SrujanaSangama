# TRACK Platform: Private AI Agent & Skill Plugin Marketplace Scope

## 1. Purpose
To provide a modular, extensible, private marketplace platform supporting all aspects of TRACK (Teaching/Learning, Research, Academic Administration, Consulting & Product Development, Kaizen) at individual, department, school, and university levels. Aligned with REVA University’s long-term vision, REVA Summit targets, and national/international benchmarks, the marketplace enables dual-engine deployment of campus-customized AI agents and skills.

## 2. Core Principles
- **Private Marketplace Gating**: Secure, role-based distribution of agents and skills to allowed teams (faculty, department staff, specific student bodies).
- **Dual-Engine Standard**: Write core prompt logic, system guidelines, and MCP tools once; run natively in both Google Antigravity and GitHub Copilot.
- **Empower Faculty and Students**: Facilitate self-reflection, Goal-Plan-Systems (GPS) planning, academic integrity monitoring, and continuous improvement (Kaizen).
- **Evidence-driven & Compliant**: Generate structural evidence for accreditations (NIRF, NAAC, NBA) and continuous feedback without bypass shortcuts.

## 3. Marketplace Capabilities
- **Unified Registry Indexing**: Central indexing (`.antigravity-marketplace/marketplace.json` and `.github/copilot-marketplace.json`) for seamless campus workstation configuration.
- **Dual Host Integration**: Automatic resolution of system prompt boundaries (`rules/`) and custom workflows/commands (`workflows/`) within both GEMINI-run environments and Node.js-based IDE extensions.
- **Model Context Protocol (MCP) Bridge**: Secure, standard-based remote tool integration to query student rosters, curriculum DBs, and placement tracking systems.
- **Accreditation and Quality Validation**: Local Python-based validator hooks checking OBE compliance, BLOOM taxonomy levels, and assignment enjoyability before plugins are baselined.

## 4. Example Marketplace Plugins & Skills

### Teaching/Learning (`plugins/teaching-learning-reva/`)
- **Syllabus & Lesson Planner**: Generates interactive SCORM/OER syllabus structures.
- **Academic Assistant**: Enforces REVA academic integrity guidelines, preventing direct copy-paste code generation.
- **Outcome Mapping & Attainment Tracker**: Direct/indirect CO attainment computation.

### Research (`plugins/research-reva/`)
- **Publication & Citation Tracker**: Fetches publication data for NIRF/NAAC pipelines.
- **Grant Assistant**: Scans funding bodies and drafts matching proposals.

### Academic Administration (`plugins/academic-admin-reva/`)
- **Accreditation Evidence Generator**: Prepares structured reports for NBA SAR/NAAC DVV metrics.
- **MOU and Regulatory Reviewer**: Verifies compliance with UGC, AICTE, and NEP 2020 frameworks.

### Consulting & Product Development (`plugins/consulting-product-reva/`)
- **Srujana Pathway Scaffold**: Guides students from skills to internships, product development, and REVA NEST incubation.
- **IP & Patent Architect**: Drafts patent claims and structures design briefs from project outputs.

### Kaizen / Personal Wellbeing (`plugins/kaizen-wellbeing-reva/`)
- **Faculty Kaizen Coach**: Personal development coaching based on SrujanaBuddy GPS planning.
- **Wellbeing Navigator**: Confidential self-reflection and mental wellbeing support utilizing Hitaishin logic.

## 5. Next Steps
- Finalize registry permissions map for CSE and school-wide testing.
- Launch central marketplace registry on campus workstation instances.
- Onboard core department plugins into the private registry index.
