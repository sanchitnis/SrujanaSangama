---
name: CSE Researcher Handbook
description: Guide for PhD scholars in Computer Science and Engineering at REVA University — research process, methodology selection, empirical standards, and writing discipline.
version: "1.0"
tags: [cse, research, methodology, empirical, sigsoft, phd]
attribution: Adapted from references/The CSE Researcher's Handbook.md (CONSTITUTION §10)
---

# CSE Researcher's Handbook
## REVA School of Computer Science and Engineering — PhD Scholar Edition

Attribution: Adapted from `references/The CSE Researcher's Handbook.md` (CONSTITUTION §10). Sections relevant to PhD methodology are included. Faculty-facing administrative sections are omitted.

---

## 1. What Research Is (and Is Not)

Research is a systematic investigation designed to establish facts, solve problems, or develop new knowledge. In Computer Science and Engineering, research:

- **Makes a novel claim** about the world — a claim that was not previously established in the literature
- **Provides evidence** for that claim — evidence that a competent, sceptical peer can evaluate and, in principle, reproduce
- **Situates itself** in the existing literature — demonstrating that the claim is not already established elsewhere

Research is NOT:
- A tutorial or survey of existing techniques (without a novel synthesis or finding)
- A software project without an evaluated research contribution
- A literature review that does not articulate a gap

---

## 2. The Research Process

A typical CS PhD research process proceeds through these phases:

1. **Problem identification** — articulate the specific unsolved problem
2. **Literature review** — understand what has been done and where the gap is (PRISMA-lite — see §4)
3. **Methodology selection** — choose the right research method for the problem (see §3)
4. **Research execution** — experiments, artefact design, data collection
5. **Results analysis** — statistical or qualitative analysis (see §5)
6. **Contribution writing** — paper drafting, peer review, publication
7. **Thesis integration** — bringing contributions together into a coherent thesis narrative

---

## 3. Research Methodology Selection

The right methodology depends on the research question type:

| Research Question Type | Appropriate Methodology | SIGSOFT Standard |
|---|---|---|
| "Does X perform better than Y?" | Experiment / Empirical study | Experiments Standard |
| "How do practitioners use X?" | Survey or Interview study | Survey Standard |
| "Can we build X that achieves Y property?" | Design Science / Constructive | Engineering Research |
| "How does X happen in a real organisation?" | Case Study | Case Study Standard |
| "What is known about X across studies?" | Systematic Literature Review | SLR Standard |
| "X and Y together explain Z better" | Mixed Methods | Mixed Methods Standard |

For all empirical work, consult the **ACM SIGSOFT Empirical Standards** (https://github.com/acmsigsoft/EmpiricalStandards). These define the minimum quality bar for publication in top CS venues.

---

## 4. Systematic Literature Review (PRISMA-lite)

A PhD literature review must be systematic — not a curated list of papers the researcher happened to find.

**Minimum standard:**
1. Define 3–5 search terms
2. State which databases were searched (IEEE Xplore, ACM DL, Scopus, Google Scholar, arXiv)
3. Define inclusion/exclusion criteria (date range, publication type, relevance threshold)
4. Report counts: papers identified → deduplicated → title/abstract screened → full-text reviewed → included
5. Group included papers by theme (not chronology)
6. For each theme: what is agreed, what is contested, what gap remains

**Output:** A 3-sentence gap statement that directly motivates your research objectives.

---

## 5. Experiment Design Principles

When designing an experiment:

1. **Hypothesis formulation:** Convert the research question into a testable H0 (null) and H1 (alternative)
2. **Variables:** Identify independent (manipulated), dependent (measured), and control (held constant) variables
3. **Baseline:** Define what you are comparing against — a state-of-the-art method, a prior system, or a null condition
4. **Metrics:** Define what "better" means before running any experiment (accuracy, F1, latency, throughput, energy, user satisfaction)
5. **Statistical test selection:**
   - Normally distributed data: t-test (two groups), ANOVA (multiple groups)
   - Non-normal / ordinal data: Mann-Whitney U, Wilcoxon signed-rank, Kruskal-Wallis
   - Correlation: Pearson (normal), Spearman (non-normal)
6. **Effect size:** Report Cohen's d or similar — statistical significance does not imply practical significance
7. **Threats to validity:** Address all four types in every methodology chapter

### Four Types of Validity Threats

| Type | Question | Example |
|---|---|---|
| Internal validity | Did our manipulation actually cause the observed effect? | Confounding variables not controlled |
| External validity | Do the results generalise beyond this study? | Only one dataset used; may not generalise |
| Construct validity | Are we measuring what we think we are measuring? | User satisfaction measured by time-on-task alone |
| Conclusion validity | Are our statistical conclusions reliable? | Underpowered study; p-values unreliable |

---

## 6. Language Discipline

### The "Significant" Rule (CONSTITUTION §15)

**"Significant" must be used only in the statistical sense.** Do not use it to mean "large", "important", "notable", or "substantial" unless a statistical significance test has been run and the p-value is stated.

Correct: *"The proposed method achieved 8.3% higher accuracy (p < 0.05, Wilcoxon signed-rank test)"*
Incorrect: *"The proposed method showed a significant improvement in accuracy"*

Alternatives when no statistical test is appropriate:
- "substantial", "notable", "marked", "considerable"
- Or: state the precise number ("15% higher", "2× faster")

### Precision in Claims

- Every empirical claim must cite a source or state the measurement
- "State of the art" must be defined — state-of-the-art as of which year? compared to which specific system?
- "Better" must be defined — better on which metric? under which conditions?

---

## 7. Research Writing Process

The best research writing follows this order:
1. Write the results and figures first (they are the most concrete)
2. Write the methodology next (explains how you got the results)
3. Write the related work (how results relate to prior work)
4. Write the introduction last (you now know what you actually found)
5. Write the abstract very last (it summarises everything)

Do not write a paper by filling in a template top-to-bottom — that produces weak introductions and disconnected sections.

---

## 8. Replication and Reproducibility

For a CS research contribution to be credible:
- Datasets must be available (or a clear reason for unavailability stated)
- Code and scripts must be available (or a clear reason for unavailability stated)
- Experimental configuration must be fully described (hardware, software versions, seeds for random processes)

The standard is: *a competent peer should be able to re-run your experiment and obtain results consistent with those reported.*
