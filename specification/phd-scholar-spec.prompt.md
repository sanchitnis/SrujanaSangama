# Plan: `reva.phd-scholar` Plugin

**TL;DR:** A new standalone Markdown-native Copilot plugin guiding REVA PhD scholars and supervisors through all 9 lifecycle stages — entrance prep through thesis, patent, grant, and book. Phase 1 is CSE/CSA-first; other branches use placeholders. Dual-persona via `/guide` trigger.

---

## Phase 0 — Input Material Authoring *(prerequisite; blocks later phases)*

Collect/author these before plugin files can be finalized:

1. **REVA PhD Regulations — Sections 14+** (publication requirements, thesis submission rules, examination — current doc cuts off mid-Section 14; **blocks** `thesis-writer` and `publication-coach`)
2. **CSE publication venues list** — IEEE Transactions, ACM, Springer conferences tagged by tier (Q1/Q2/Q3)
3. **India funding landscape digest** — DST-SERB, DBT, CSIR JRF/SRF, UGC fellowships, ICMR, industry grants
4. **REVA thesis format template** — user will add Word/LaTeX template; embed in `references/thesis-format-guide.md`
5. **UGC CARE list + Scopus/WoS guidance** — journal selection heuristics, anti-predatory red flags
6. **Branch placeholder files** — ECE, Management, Life Sciences, etc. (empty structures; user populates later)

---

## Phase 1 — Plugin Scaffolding

- `plugins/phd-scholar/plugin.json` — id: `reva.phd-scholar`, version 1.0.0; lists rules + workflows; registers `/guide` slash command
- `plugins/phd-scholar/package.json` — exposes `phd-scholar` agent with slash commands: `/guide`
- `plugins/phd-scholar/mcp.json` — deferred (no API integration in Phase 1)
- `plugins/phd-scholar/README.md`

---

## Phase 2 — Rules Layer *(6 files)*

| File | Purpose |
|---|---|
| `rules/SCHOLAR_IDENTITY.md` | Default persona — empathetic coach; stage-aware, regulation-enforcing |
| `rules/GUIDE_IDENTITY.md` | Activated by `/guide` — strategic supervisor advisor |
| `rules/REVA_PHD_REGULATIONS.md` | Distilled hard rules: deadlines, credit floors, publication minimums, cancellation triggers (2-year annulment, 10-year hard limit) |
| `rules/RESEARCH_ETHICS.md` | Plagiarism thresholds, authorship norms, RPE course content, SIGSOFT standards from CSE Handbook |
| `rules/SCHOOL_ROUTING.md` | Branch detection → loads CSE materials; graceful placeholder message for other branches |
| `rules/PUBLICATION_STANDARDS.md` | Journal tier guidance, predatory red flags, UGC CARE list, conference tiers |
| `rules/WELLBEING_STANDARD.md` | When to suggest a break vs. escalate; PhD-specific mental health red flags; self-care protocol; signposting to REVA counselling and REVA's `kaizen-wellbeing-reva` plugin |
| `rules/IKIGAI_ALIGNMENT.md` | Defines ikigai check triggers (onboarding, stage transitions, signs of disengagement); ensures research topic and career goals remain coherently connected throughout the programme |

---

## Phase 3 — Agents Layer *(12 files)*

**Core (2):**
- `agents/core/orchestrator.md` — Routes Scholar vs. `/guide` mode; activates correct stage agent
- `agents/core/stage-tracker.md` — Auto-computes milestone dates from provisional registration date + supervisor-confirmed progress inputs; re-computes at each biannual review

**Scholar agents (9):**

| Agent | Stage | Key Responsibilities |
|---|---|---|
| `agents/scholar/topic-scout.md` | 0 | Research area mapping, guide eligibility check (7.2 caps), topic feasibility |
| `agents/scholar/coursework-navigator.md` | 1 | Credit pathway routing (18/30/46/50 credits per candidate type), ARM/RPE coaching, IA prep |
| `agents/scholar/synopsis-builder.md` | 2 | Pre-registration colloquium prep; synopsis structure (background, objectives, hypotheses, methodology) |
| `agents/scholar/research-coach.md` | 3 | Lit review (PRISMA-lite), methodology selection, experiment design per CSE Handbook + SIGSOFT standards; biannual progress report scaffolding |
| `agents/scholar/publication-coach.md` | 4 | Paper targeting, drafting, reviewer response coaching; publication minimum tracker (Section 14) |
| `agents/scholar/thesis-writer.md` | 5 | Chapter-by-chapter guidance, REVA thesis template compliance, pre-submission colloquium prep, anti-plagiarism checklist |
| `agents/scholar/patent-agent.md` | 6 | Invokes `patent-generator` workflows — no duplication; adapts for scholar context |
| `agents/scholar/grant-agent.md` | 7 | India grant calendar, SERB/DST/DBT/ICMR proposal structures; adapts `research-reva` funding workflows |
| `agents/scholar/book-agent.md` | 8 | Research monograph / book proposal, publisher targeting, chapter outline |
| `agents/scholar/daily-planner.md` | All | Breaks current milestone into weekly/daily micro-tasks (2–4 hrs each); anti-procrastination nudges; tracks completion; surfaces next doable step on every session open |
| `agents/scholar/blocker-breaker.md` | All | "I'm stuck" triage: classifies blocker as conceptual / methodological / motivational / regulatory / interpersonal → routes to targeted help, worked examples, or escalation path |
| `agents/scholar/wellness-companion.md` | All | Immediate wellbeing check-ins; PhD-specific stress/anxiety patterns; actionable self-care nudges; escalation path to REVA counselling; references `kaizen-wellbeing-reva` plugin for deeper support |
| `agents/scholar/ikigai-compass.md` | All | Research–ikigai alignment checks: connects topic, domain expertise, passion, and societal impact; revisited at onboarding and each major stage transition |

**Guide agent (1):**
- `agents/guide/guide-advisor.md` — Activated by `/guide`; scholar roster view, progress alerts, feedback protocol templates, co-guide coordination

---

## Phase 4 — Workflows Layer *(12 files)*

| File | Covers |
|---|---|
| `workflows/00_onboarding.md` | Profile setup: school, batch, provisional registration date, candidate type (sets credit pathway), guide name, current stage |
| `workflows/01_entrance-prep.md` | Topic ideation, guide identification, entrance test prep (RM + subject-specific split); **interview coaching: mock Q&A, research interest articulation, 10-minute presentation dry-run** |
| `workflows/02_coursework.md` | Course schedule per pathway, credit tracking, IA-I/IA-II/CWEE preparation |
| `workflows/03_synopsis.md` | Synopsis template walkthrough, colloquium presentation coaching |
| `workflows/04_research-cycle.md` | Biannual review cycles, experiment logging, lit review protocol |
| `workflows/05_publication-pipeline.md` | Paper ideation → drafting → submission → revision loop; publication minimum tracking |
| `workflows/06_thesis-sprint.md` | Pre-submission checklist, chapter plan, format compliance, plagiarism self-check |
| `workflows/07_patent-workflow.md` | IP identification → patentability → prior art → draft (chains into `patent-generator`) |
| `workflows/08_grant-proposal.md` | Grant calendar, SERB/DST/DBT templates, budget planning |
| `workflows/09_book-proposal.md` | Publisher targeting, chapter outline, audience scoping |
| `workflows/10_guide-dashboard.md` | `/guide` mode: scholar roster, milestone status, feedback templates, co-guide notes |
| `workflows/11_session-closer.md` | End-of-session memory capture, next action items, milestone date refresh |
| `workflows/12_daily-standup.md` | Quick daily/weekly micro-planning: yesterday / today / blockers; outputs 3 small doable tasks; feeds `daily-planner.md` agent |
| `workflows/13_stuck-triage.md` | "Help, I'm stuck" protocol: blocker classification → targeted intervention (concept explainer, methodology coach, motivational reframe, regulation lookup, or guide escalation) |
| `workflows/14_wellness-checkin.md` | Periodic wellbeing pulse (PhD stress indicators, isolation, imposter syndrome, burnout signals); actionable nudges; escalation path to REVA support services |
| `workflows/15_ikigai-audit.md` | Research–purpose alignment review: passion × strength × world-need × career goal; conducted at onboarding and annually at each biannual review |

---

## Phase 5 — Context & Memory Templates

**`context/` (4 example files — committed):**
- `scholar-profile.md.example` — school, batch, provisional registration date, candidate type, guide, stage; ikigai fields: passion areas, domain strengths, societal need, career goal
- `research-tracker.md.example` — milestone log, biannual review dates, computed deadline table, pending actions
- `publication-pipeline.md.example` — paper title, target venue, submission status, deadline
- `daily-log.md.example` — current micro-task list, blocker notes, daily standup history (last 7 days)

**`memory/` — gitignored, structured like `research-reva`; all files below have a committed `.example` counterpart:**

```
memory/
  .gitignore
  soul.md                        ← Scholar identity: name, school, batch, registration date,
                                    research domain, career aspiration, learning style,
                                    communication preferences, strengths, fears, motivators
  soul.md.example                ← Template with annotated empty fields

  ikigai.md                      ← 4-quadrant ikigai map: passion × strength × world-need × career goal;
                                    current alignment score; last reviewed date
  ikigai.md.example

  tasks.md                       ← Active task list: milestone → weekly → daily micro-tasks;
                                    status (todo/in-progress/done/blocked); due dates; blocker notes
  tasks.md.example

  wellbeing-log.md               ← Periodic check-in snapshots: date, mood, stress level,
                                    workload rating, blockers, self-care actions taken
  wellbeing-log.md.example

  semantic/
    research-pipeline.md         ← Active research threads, parked ideas, experiment log,
                                    stage lifecycle per thread (ideation→published)
    research-pipeline.md.example

    publication-log.md           ← Paper title, venue, tier, submission date, status,
                                    reviewer responses, acceptance/rejection notes
    publication-log.md.example

    progress-reports.md          ← Biannual progress report history: dates, guide remarks,
                                    committee feedback, corrective actions
    progress-reports.md.example

    episodic/                    ← Session-by-session notes (auto-appended by session-closer workflow)
```

---

## Phase 6 — References Folder

```
plugins/phd-scholar/references/
  schools/
    cse/
      researcher-handbook.md        ← copy from references/The CSE Researcher's Handbook.md
      publication-venues.md         ← Phase 0 item (user provides)
      methodology-guide.md          ← distilled from CSE Handbook + SIGSOFT standards
    ece/
      researcher-handbook.md.placeholder
    management/
      researcher-handbook.md.placeholder
    [other schools]/
  reva-phd-regulations-digest.md    ← compact quick-reference card from full regulations
  ugc-care-guidance.md              ← Phase 0 item (user provides)
  india-funding-landscape.md        ← Phase 0 item (user provides)
  thesis-format-guide.md            ← Phase 0 item (user provides template)
  phd-milestone-calculator.md       ← auto-compute logic spec for stage-tracker agent
```

---

**Total file count:** ~75 files

**Cross-plugin reuse (no duplication):**
- `plugins/patent-generator/workflows/` + `lib/` → Stage 6 invoked by `patent-agent.md`
- `plugins/research-reva/workflows/funding-hunt.md` + `manuscript-check.md` → adapt for Stages 4 & 7
- `plugins/research-reva/rules/RESEARCH_ETHICS.md` + `GRANT_PROPOSAL_STANDARD.md` → adapt into rules layer
- `plugins/kaizen-wellbeing-reva/` → referenced by `WELLBEING_STANDARD.md` and `wellness-companion.md` for deeper support escalation

---

## Verification

1. Onboarding with mock CSE scholar → school routing loads CSE materials, not placeholders
2. Thesis submission attempt at <3 years → `REVA_PHD_REGULATIONS.md` blocks with correct regulation citation
3. All 4 credit pathways (18/30/46/50) → correct course list and schedule generated
4. Stage 0→5 walkthrough with mock scholar → correct agent activates at each stage
5. Stage 6 → `patent-generator` workflows surface correctly via `patent-agent.md`
6. `/guide` trigger → `GUIDE_IDENTITY.md` + `guide-dashboard` workflow activates; scholar persona suppressed
7. ECE school input → graceful placeholder message, no CSE content leaks
8. `stage-tracker.md` with a registration date + 2 progress updates → correct milestone dates auto-computed
9. `daily-planner.md` with a 3-month milestone → outputs ≥3 specific micro-tasks for the current week
10. `blocker-breaker.md` with a conceptual blocker → routes to concept explainer; with a motivational blocker → routes to wellness-companion
11. `wellness-companion.md` with burnout signals → outputs actionable nudges + escalation path to REVA counselling
12. `ikigai-compass.md` at onboarding → generates a 4-quadrant ikigai map tied to research topic; at Stage 3 → confirms alignment still holds

---

## Decisions (Confirmed)

1. **Guide mode**: `/guide` slash-command trigger — switches persona to `GUIDE_IDENTITY.md` + `guide-advisor.md` + `guide-dashboard` workflow
2. **Thesis template**: REVA-specific template exists; user will add it → embed in `references/thesis-format-guide.md`, referenced by `thesis-writer.md`
3. **Timeline calculator**: Auto-compute — `stage-tracker.md` derives milestone dates from provisional registration date + supervisor-confirmed progress inputs; refreshed each biannual review

## Scope Boundaries

- **In scope**: All 9 stages, CSE Phase 1, dual persona (Scholar + `/guide`)
- **Out of scope (Phase 1)**: ECE/Management/Life Sciences content; MCP API integration; automated push notifications
- **Blocked until input**: `thesis-writer.md` and `publication-coach.md` finalization requires REVA PhD Regulations Sections 14+
