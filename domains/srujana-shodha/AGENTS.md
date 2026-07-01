# Srujana Shodha Domain Router

Use this router only after the root `AGENTS.md` Usage Mode router selects
`srujana-shodha`.

## Load Order

1. Identify whether the request concerns research onboarding, grants,
   publications, PhD supervision, patents, funding, SDG impact, or wellness.
2. If a slash command is named, read only the matching file in `commands/`.
3. Read rules only when the command or request names them directly.
4. Read shared skills only when the command or request names them directly.
5. Read nested `rules/agents/` only when the selected workflow names a specific
   agent.

## Local Commands

- `00_onboarding`
- `01_entrance-prep`
- `02_coursework`
- `03_synopsis`
- `04_research-cycle`
- `05_publication-pipeline`
- `06_thesis-sprint`
- `07_patent-workflow`
- `08_grant-proposal`
- `09_book-proposal`
- `10_guide-dashboard`
- `11_session-closer`
- `12_daily-standup`
- `13_stuck-triage`
- `14_wellness-checkin`
- `15_ikigai-audit`
- `brand-sprint`
- `funding-hunt`
- `grant-check`
- `manuscript-check`
- `onboarding`
- `opportunity-mapping`
- `proposal-check`
- `research-lifecycle`
- `sdg-impact-audit`
- `session-closer`

## Local Rules

- `ADVISOR_IDENTITY.md`
- `GRANT_PROPOSAL_STANDARD.md`
- `GUIDE_IDENTITY.md`
- `IKIGAI_ALIGNMENT.md`
- `INDIA_RESEARCH_CONTEXT.md`
- `PERSONAL_BRAND_STANDARD.md`
- `PUBLICATION_STANDARDS.md`
- `RESEARCH_ETHICS.md`
- `REVA_PHD_REGULATIONS.md`
- `SCHOLARLY_WRITING_STANDARD.md`
- `SCHOLAR_IDENTITY.md`
- `SCHOOL_ROUTING.md`
- `SDG_MAPPING_STANDARD.md`
- `WELLBEING_STANDARD.md`

## Output Boundary

Draft outputs for researcher, guide, or institutional review. Write persistent
task outputs to the user's `srujana-memory/` or collaboration space, not to this
shared domain folder.
