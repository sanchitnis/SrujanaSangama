# SrujanaSangama Domains and Commands

This file lists all the available agent domains in SrujanaSangama, along with their primary slash commands and typical use cases.

---

## Available Domains

* **onboarding**
  - `/onboard`: Sets up user profile, creates local `srujana-memory` structures, and performs a resume audit.
* **personal-productivity** (Execution Engine & Operating System)
  - `/morning-briefing`: Daily agenda and task alignment.
  - `/weekly-review` / `/weekly-alignment-audit`: End-of-week task auditing.
  - `/deep-research`: Conducts structured literature and web searches.
  - `/skill-generator`: Packages a workflow into a reusable skill.
  - `/project-kickoff`: Sets up metadata for a new project.
* **teaching-learning**
  - `/curriculum-strategy-check`: Audits school curriculum strategy (vision, mission, PEOs, POs, roles, market trends).
  - `/activity-design-ai-ready`: Designs AI-resistant, HOTS-aligned authentic learning activities.
  - `/concept-map-network`: Generates curriculum concept networks and prerequisite maps.
  - `/curriculum-design-lifecycle`: End-to-end course/curriculum design.
  - `/lesson-plan`: Drafts modular lesson plans.
  - `/question-paper-reviewer`: Checks question papers against Blooms Taxonomy and REVA standards.
  - `/assessment-check` / `/course-check` / `/session-check`: Formative review of educational materials.
* **srujana-shodha**
  - `/research-lifecycle`: Guides through academic research phases from coursework to thesis defense.
  - `/manuscript-check`: Audits drafts before journal submission.
  - `/funding-hunt` / `/opportunity-mapping`: Locates suitable grants and projects.
  - `/grant-check` / `/proposal-check`: Reviews grant proposals.
  - `/sdg-impact-audit`: Maps research contribution to Sustainable Development Goals.
  - `/brand-sprint`: Builds researcher brand and online profiles.
* **academic-admin**
  - `/attainment-check`: Evaluates course/program outcome attainment.
* **innovator**
  - `/patent-draft`: Full multi-step workflow for patentability analysis and patent application drafting.
* **kaizen-excellence** (Reflective Growth & Process Improvement)
  - `/gps-plan`: Drafts strategic improvement goals for personal growth and process optimization.
* **admissions-branding**
  - Assists with institutional branding and marketing materials.
* **placement-tpc**
  - Connects students with placement preparation and career development tools.
* **strategic-planning**
  - Formulates institutional growth strategies and developmental goals.

---

## How to Invoke Commands

Once onboarded, start any session by asking the AI agent to assist you within a specific domain. The AI agent will read the instructions in the repository to guide you.

For example, simply ask the AI agent:
* *"Under the `teaching-learning` domain, run `/question-paper-reviewer` on my draft paper"*
* *"Use the `srujana-shodha` domain and run `/funding-hunt` for a green energy project"*

For details on the workspace memory structure, refer to [srujana-memory README](../../srujana-memory/README.md).
For instructions on contributing and development rules, refer to [specification README](../specification/README.md).
