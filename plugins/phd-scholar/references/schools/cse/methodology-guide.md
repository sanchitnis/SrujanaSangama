---
name: CSE Methodology Guide
description: Distilled methodology guidance for PhD scholars in CSE — method selection, experiment design, validity threats, and statistical analysis guidance.
version: "1.0"
tags: [cse, methodology, experiment-design, statistics, validity, phd]
attribution: Synthesised from researcher-handbook.md and ACM SIGSOFT Empirical Standards.
---

# CSE Methodology Guide
## Research Methods for REVA CSE PhD Scholars

---

## 1. Methodology Selection Matrix

Answer these three questions to identify your primary methodology:

1. **Is your contribution primarily a new artefact** (algorithm, system, tool, model, framework)?
2. **Is your contribution primarily understanding** (how practitioners work, how a system behaves, what factors drive an outcome)?
3. **Is your contribution primarily a synthesis** (what is known across the literature)?

| Your Answer | Primary Methodology | SIGSOFT Standard to Follow |
|---|---|---|
| Artefact — and you evaluate it empirically | Experiment / Engineering Research | Experiments Standard |
| Artefact — in a real-world deployment context | Case Study + Experiment | Case Study + Experiments Standards |
| Understanding — from practitioners | Survey or Interview Study | Survey / Questionnaire Study Standard |
| Understanding — from a system/organisation | Case Study | Case Study Standard |
| Synthesis — across published literature | Systematic Literature Review | SLR Standard |
| Mixed (understanding + artefact) | Mixed Methods | Mixed Methods Standard |

---

## 2. Experiment Design: Step-by-Step

### Step 1 — Define Hypotheses

Every experiment must have a null hypothesis (H0) and alternative hypothesis (H1).

Format:
> H0: [Your system / method] does NOT [achieve property X] compared to [baseline]
> H1: [Your system / method] DOES [achieve property X] compared to [baseline]

Never state the hypothesis after seeing the results.

### Step 2 — Define Variables

| Variable Type | Definition | Example |
|---|---|---|
| Independent | What you change | Algorithm version (proposed vs baseline) |
| Dependent | What you measure | Prediction accuracy (F1), Runtime (ms) |
| Control | What you hold fixed | Dataset, hardware, random seed |

### Step 3 — Define Baseline

Your baseline must be:
- A published state-of-the-art method (cite the paper)
- OR a classical approach (e.g., Random Forest, SVM, Linear Regression)
- OR a null/random baseline that establishes a floor

Do not compare against something you built yourself — that proves nothing to reviewers.

### Step 4 — Define Metrics

Define metrics BEFORE running experiments:
- Classification: Precision, Recall, F1, AUC-ROC, MCC (for imbalanced data)
- Regression: MAE, RMSE, R²
- System performance: Throughput (req/s), Latency (ms p95), Memory (MB), Energy (J)
- User study: Task completion rate, SUS score, Time-on-task

### Step 5 — Run Statistical Tests

| Condition | Test | When to Use |
|---|---|---|
| Normal, 2 groups, independent | Independent samples t-test | A/B comparison |
| Normal, 2 groups, paired | Paired t-test | Before/after on same subjects |
| Non-normal or ordinal, 2 groups | Mann-Whitney U | Most ML comparison scenarios |
| Non-normal, paired | Wilcoxon signed-rank | Before/after, non-normal |
| Multiple groups | ANOVA (normal) or Kruskal-Wallis (non-normal) | 3+ algorithm versions |
| Correlation | Pearson (normal) or Spearman (non-normal) | Feature relationship |

Always state: test name, test statistic, p-value, effect size.
Threshold: p < 0.05 is conventional. State it; do not assume it is known.

### Step 6 — Report Effect Size

Statistical significance tells you the effect is unlikely to be chance. Effect size tells you whether it matters in practice.

| Statistic | Use With | Interpretation |
|---|---|---|
| Cohen's d | t-tests | Small 0.2, Medium 0.5, Large 0.8 |
| r | Mann-Whitney, Wilcoxon | Small 0.1, Medium 0.3, Large 0.5 |
| η² | ANOVA | Small 0.01, Medium 0.06, Large 0.14 |

---

## 3. Validity Threats — What Reviewers Will Ask

Addressing validity threats is NOT optional. Every methodology chapter must have a "Threats to Validity" section.

| Threat Type | Reviewer Question | Mitigation Strategy |
|---|---|---|
| Internal validity | Did confounders cause the observed effect? | Control variables; randomisation; ablation study |
| External validity | Do results generalise? | Multiple datasets; multiple domains; diversity of subjects |
| Construct validity | Are the metrics measuring what matters? | Multiple metrics; user study; qualitative validation |
| Conclusion validity | Are statistical conclusions reliable? | Power analysis; correct test for distribution; report effect size |

Power analysis tip: Run a power analysis BEFORE collecting data to ensure your sample size can detect an effect of the expected magnitude. Tools: G*Power, pwr (R package), statsmodels (Python).

---

## 4. Survey and Interview Study Design

When research is about understanding human behaviour, practices, or perceptions:

1. **Sampling strategy:** Purposive (targeted expertise) or snowball. State why the sample is appropriate.
2. **Sample size guidance:** Surveys: aim for n ≥ 30 for quantitative analysis. Interviews: saturation typically at 12–20.
3. **Survey instrument:** Pilot with 3–5 respondents before deployment. Measure reliability (Cronbach's α ≥ 0.7 for Likert scales).
4. **Interview protocol:** Semi-structured. Write a guide, not a rigid script. Record with consent.
5. **Qualitative coding:** Open coding → axial coding → selective coding (grounded theory lite). Use ATLAS.ti, NVivo, or manual.
6. **Bias disclosure:** Non-response bias, social desirability bias, researcher bias — state these explicitly.

---

## 5. Case Study Design

A case study investigates a phenomenon in its real-world context. It is appropriate when the boundary between phenomenon and context is unclear.

Minimum structure (Yin 2014):
1. **Unit of analysis:** What/who is the case? (a project, a team, an organisation, a system deployment)
2. **Case selection rationale:** Why this case? (typical case / extreme case / revelatory case)
3. **Data collection:** Multiple sources (interviews + documents + observation = triangulation)
4. **Analysis protocol:** How will you code / categorise / interpret data?
5. **Validity:** Construct validity (use multiple sources), internal validity (pattern matching), external validity (what the case generalises to), reliability (case study protocol documented)

---

## 6. Statistical Significance vs. Practical Significance

A statistically significant result is NOT necessarily important. Always interpret both:

- **Statistical significance:** p < 0.05 means the result is unlikely (< 5%) to have occurred by chance
- **Practical significance:** Effect size, absolute difference, business/engineering impact

Example of correct reporting:
> "The proposed method achieved an F1 of 0.87 vs the baseline's 0.79 (Δ = 0.08), a difference that is statistically significant (Mann-Whitney U, p = 0.012) with medium effect size (r = 0.31). This improvement corresponds to N fewer false negatives in a corpus of M instances."

---

## 7. Replication Package Checklist

Before submitting any paper:
- [ ] Code pushed to public repository (GitHub / Zenodo)
- [ ] Dataset uploaded or access instructions provided
- [ ] `README.md` with environment setup, run commands, expected outputs
- [ ] Random seeds documented
- [ ] Hardware/software configuration documented (CPU, GPU, OS, library versions)
- [ ] Results tables in machine-readable format (CSV, not only PDF tables)
