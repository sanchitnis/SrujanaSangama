# /manuscript-check

Perform a rigorous academic quality and compliance audit of the provided research paper, manuscript draft, or project report. You must evaluate the draft against the **REVA Scholarly Writing Standard** (`rules/SCHOLARLY_WRITING_STANDARD.md`).

---

## Audit Steps

1.  **Analyze Manuscript Structure**:
    *   Check for essential scholarly sections: Abstract, Introduction, Literature Review, Methodology, Results/Discussion, Conclusion, and References.
    *   Verify the Abstract context, problem statement, methodology, results, and impact alignment.
2.  **Evaluate Literature Review & Citation Authenticity**:
    *   Assess the depth of the literature mapping (consensus, contradiction, gap).
    *   Audit citations for standard formatting (IEEE, ACM, Harvard, etc.) and check for potential hallucinated references.
3.  **Assess Hypothesis & Methodology Rigor**:
    *   Extract and critique the primary hypothesis or objective statement. Is it testable and specific?
    *   Evaluate the reproducibility of the methodology description.
    *   Confirm if study limitations and research assumptions are explicitly stated.
4.  **Detect AI-Plagiarism & Generic Writing Indicators**:
    *   Scan for common AI boilerplate phrases, generic transitions, and unreferenced assertions.
    *   Check for compliance with ethics declarations (funding source, conflict of interest, author contribution).

---

## Output Format

Your response must be formatted as a structured, professional peer-review report:

### 📄 Scholarly Manuscript Quality Audit Report

#### 1. Structural & Section Completeness
*   **Abstract Evaluation**: `[Actionable feedback on the abstract's logical flow]`
*   **Structure Score**: `[Complete / Minor Gaps / Incomplete - list missing sections]`

#### 2. Literature Review & Citation Audit
*   **Research Gap Clarity**: `[PASS / FAIL / WEAK] - detail if the research gap is explicitly stated.`
*   **Citation Authenticity Check**:
| Reference Entry | Formatting Compliance | Hallucination / Risk Flag |
| :--- | :---: | :--- |
| `[Ref 1]` | ... | `[Low Risk / Needs Verification]` |

#### 3. Hypothesis & Methodology Evaluation
*   **Extracted Hypothesis**: `"... [extracted statement] ..."`
*   **Hypothesis Quality**: `[Strong / Vague / Missing - suggestions to sharpen]`
*   **Reproducibility Analysis**: `[Feedback on whether methodology is detailed enough for replication]`

#### 4. Actionable Revision Advice
Provide a numbered, concise list of peer-review comments and necessary corrections for the author.
