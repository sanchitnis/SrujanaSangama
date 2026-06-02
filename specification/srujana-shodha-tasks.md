# Tasks — `reva.srujana-shodha` Plugin Backlog

> **Spec contract:** [srujana-shodha-spec.prompt.md](file:///d:/Github/SrujanaSangama/specification/srujana-shodha-spec.prompt.md)
> **Governance:** `CONSTITUTION.md` §13 (≤3 files, ≤1 hr per task).
> **Status:** Approved (Unified Backlog)

---

## Active Sprint Tasks

### Phase 1 — Manifests & Scaffolding
- [ ] **T-001**: Configure manifests `plugins/srujana-shodha/plugin.json` & `plugins/srujana-shodha/package.json` to register `@reva-scholar` agent with triggers `/grant`, `/manuscript-check`, `/proposal-check` and `/guide` (for supervisor mode).
- [ ] **T-002**: Initialize `plugins/srujana-shodha/README.md` summarizing the unified faculty research + PhD scholar capabilities.

### Phase 2 — Rules Layer (14 files)
- [ ] **T-003**: Create core identity rules (`rules/ADVISOR_IDENTITY.md`, `rules/SCHOLAR_IDENTITY.md`, `rules/GUIDE_IDENTITY.md`).
- [ ] **T-004**: Create regulation and ethics rules (`rules/REVA_PHD_REGULATIONS.md`, `rules/RESEARCH_ETHICS.md`, `rules/PUBLICATION_STANDARDS.md`).
- [ ] **T-005**: Create environment and context rules (`rules/SCHOOL_ROUTING.md`, `rules/INDIA_RESEARCH_CONTEXT.md`, `rules/WELLBEING_STANDARD.md`).
- [ ] **T-006**: Create research alignment rules (`rules/IKIGAI_ALIGNMENT.md`, `rules/SDG_MAPPING_STANDARD.md`, `rules/PERSONAL_BRAND_STANDARD.md`, `rules/GRANT_PROPOSAL_STANDARD.md`, `rules/SCHOLARLY_WRITING_STANDARD.md`).

### Phase 3 — Agents Layer (24 files)
- [ ] **T-007**: Implement core routing agents (`agents/core/orchestrator.md`, `agents/core/stage-tracker.md`, `agents/core/memory-steward.md`).
- [ ] **T-008**: Implement faculty research agents (`competency-profiler`, `opportunity-scout`, `collaboration-architect`, `funding-navigator`, `research-pipeline-coach`, `journal-targeter`, `work-product-reviewer`, `personal-brand-builder`).
- [ ] **T-009**: Implement scholar lifecycle agents (`topic-scout`, `coursework-navigator`, `synopsis-builder`, `research-coach`, `publication-coach`, `thesis-writer`, `patent-agent`, `grant-agent`, `book-agent`).
- [ ] **T-010**: Implement support and guide agents (`daily-planner`, `blocker-breaker`, `wellness-companion`, `ikigai-compass`, `guide-advisor`).

### Phase 4 — Workflows Layer (26 files)
- [ ] **T-011**: Implement Faculty-facing workflows (`onboarding`, `opportunity-mapping`, `funding-hunt`, `research-lifecycle`, `brand-sprint`, `sdg-impact-audit`, `grant-check`, `manuscript-check`, `proposal-check`, `session-closer`).
- [ ] **T-012**: Implement Scholar-facing onboarding & early workflows (`00_onboarding`, `01_entrance-prep`, `02_coursework`, `03_synopsis`, `04_research-cycle`).
- [ ] **T-013**: Implement Scholar-facing core pipelines & final workflows (`05_publication-pipeline`, `06_thesis-sprint`, `07_patent-workflow`, `08_grant-proposal`, `09_book-proposal`, `10_guide-dashboard`).
- [ ] **T-014**: Implement Scholar-facing support workflows (`11_session-closer`, `12_daily-standup`, `13_stuck-triage`, `14_wellness-checkin`, `15_ikigai-audit`).

### Phase 5 — Context & Memory Templates
- [ ] **T-015**: Set up example profiles and pipeline templates (`context/scholar-profile.md.example`, `context/research-tracker.md.example`, `context/publication-pipeline.md.example`, `context/daily-log.md.example`).
- [ ] **T-016**: Create local gitignored memory structure layouts (`memory/soul.md.example`, `memory/ikigai.md.example`, `memory/tasks.md.example`, `memory/wellbeing-log.md.example`, `memory/semantic/*`).

### Phase 6 — Reference Materials
- [ ] **T-017**: Author branch handbooks & publications reference (`references/schools/cse/*`, `references/reva-phd-regulations-digest.md`, `references/ugc-care-guidance.md`, `references/india-funding-landscape.md`, `references/thesis-format-guide.md`, `references/phd-milestone-calculator.md`).

---

## Verification Criteria
- [ ] Onboarding with mock CSE scholar/faculty loads proper guidelines and context.
- [ ] Slash commands `/grant`, `/manuscript-check`, `/proposal-check` analyze documents against guidelines correctly.
- [ ] `/guide` successfully loads the guide-advisor persona and suppresses scholar identity.
- [ ] Milestone calculator computes accurate deadlines per registration date and credit pathway (18/30/46/50).
