# /assessment-check

Perform a rigorous quality and integrity audit of the provided course assessments, exams, lab manuals, or assignment drafts. You must evaluate the assessments against the **REVA Assessment Quality Standard** (`rules/ASSESSMENT_QUALITY_STANDARD.md`).

---

## Audit Steps

1.  **AI-Triviality & Plagiarism Risk Audit**:
    *   Examine each question or task in the draft.
    *   Flag any tasks that can be completely resolved by copy-pasting directly into an LLM (e.g., standard definitions, boilerplate code).
    *   Identify missing meta-cognitive or constraint layers in off-site assignments.
2.  **Verify HOTS (Bloom's L4-L6) Dominance**:
    *   Map each exam question or assignment task to its corresponding Bloom's level.
    *   Calculate the percentage of total marks/weight assigned to HOTS questions (Levels 4, 5, or 6).
    *   Standard check: **Is the HOTS weight $\ge 60\%$?**
3.  **Audit Enjoyability & Engagement Metrics**:
    *   Evaluate tasks against the enjoyability factors (Autonomy, Impact, Micro-Achievements).
    *   Suggest adjustments to make the assignments more engaging and real-world relevant.
4.  **Confirm Viva-Voce & Proctored Validation Gaps**:
    *   Check if projects or weekly practical tasks include clear, structured in-person viva or live modification verification instructions.

---

## Output Format

Your response must be formatted as a structured, professional audit report:

### 🛡️ Assessment Quality & Integrity Audit Report

#### 1. Question-by-Question Integrity Audit
| Question / Task | Target Bloom's Level | AI-Triviality Risk | Actionable Redesign Recommendation |
| :--- | :---: | :---: | :--- |
| Q1 | ... | `[HIGH / MED / LOW]` | ... |

*   **HOTS (L4-L6) Marks Percentage**: `[Calculate %]`
*   **HOTS Dominance Status**: `[PASS / FAIL (Required >= 60%)]`

#### 2. Student Motivation & Engagement Score
*   **Autonomy Score**: `[1-5] (How much creative choice does the student have?)`
*   **Real-world Impact Score**: `[1-5] (Is there public-facing or community usefulness?)`
*   **Actionable Advice**: `[Concise tip to improve the student motivation index]`

#### 3. Security & Proctored Validation Mapping
*   **Unproctored Components**: `[List unproctored elements]`
*   **In-person Validation Method**: `[e.g., Socratic Viva-Voce / On-the-spot Code Modification]`
*   **Validation Gap Status**: `[SECURED / ACTION REQUIRED - detail what's missing]`

#### 4. Mandatory Faculty Revision Steps
Provide a numbered, concise list of modifications required before this assessment is approved for students.
