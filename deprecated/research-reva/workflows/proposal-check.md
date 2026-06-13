# /proposal-check

Perform a rigorous, professional quality and compliance audit of the provided research grant proposal draft. You must evaluate the draft against the **REVA Grant Proposal Standard** (`rules/GRANT_PROPOSAL_STANDARD.md`).

---

## Audit Steps

1.  **Evaluate Thematic Alignment**:
    *   Identify the target funding agency (DST, DBT, UGC, CSIR, AICTE, MEITY) and specific call brief, if provided.
    *   Analyze the proposal objectives for direct alignment with the agency's active priorities and thematic focus.
2.  **Verify Template & Section Compliance**:
    *   Audit the proposal draft for the required standard sections (Project Title, Executive Summary, Problem Statement, Work Plan, Risk Analysis).
    *   Flag any missing or underdeveloped sections.
3.  **Critique Novelty & Feasibility**:
    *   Examine the statement of novelty. Is it explicit, clear, and distinct from previous works?
    *   Check for documented evidence of feasibility (preliminary results, existing lab infrastructure, pilot work).
4.  **Audit Budget Logical Rationale**:
    *   Analyze budget allocations (Capital Equipment, Consumables, Manpower).
    *   Verify that capital equipment maps directly to methodology work packages.
    *   Check if manpower emoluments adhere to official DST/national standards.

---

## Output Format

Your response must be formatted as a structured, professional grant reviewer report:

### 🏛️ Grant Proposal Quality & Compliance Report

#### 1. Funding Agency Thematic Alignment
*   **Target Agency & Call**: `[Identify agency, e.g., DST - Deep Tech Call]`
*   **Thematic Alignment Status**: `[HIGH / MEDIUM / POOR]`
*   **Alignment Feedback**: `[Traceable analysis of how well objectives map to agency priorities]`

#### 2. Section Compliance Dashboard
| Required Section | Completion Status | Detailed Review Findings |
| :--- | :---: | :--- |
| Project Title | `[PASS / REDESIGN]` | ... |
| Executive Summary | `[PASS / INCOMPLETE]` | ... |
| Problem Statement | `[PASS / WEAK]` | ... |
| Work Plan / Gantt | `[PASS / MISSING]` | ... |
| Risk & Mitigation | `[PASS / WEAK]` | ... |

#### 3. Novelty & Feasibility Index
*   **Novelty Statement Quality**: `[Strong / Generic / Ambiguous]`
*   **Feasibility Index**: `[High / Medium / Low] (Based on documented preliminary work & infrastructure)`
*   **Critical Gap**: `[Identify the single biggest gap that could lead to rejection]`

#### 4. Budget & Manpower Compliance
*   **Capital Equipment Rationale**: `[Justified / Over-budgeted / Weakly mapped]`
*   **DST Manpower Standard Check**: `[COMPLIANT / OUT OF COMPLIANCE - e.g., JRF scales]`

#### 5. Prioritized Action Items for Success
Provide a numbered list of immediate revisions needed to increase the funding probability.
