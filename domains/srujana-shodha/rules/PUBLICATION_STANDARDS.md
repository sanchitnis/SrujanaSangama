---
name: publication-standards
description: >
  Publication quality and venue selection standards for REVA PhD scholars.
  Forked from plugins/research-reva/rules/GRANT_PROPOSAL_STANDARD.md
  (publication section). Adds §14.1 publication minimums, UGC CARE context,
  predatory journal red flags, and conference tier tags.
version: 1.0.0
created: 2026-06-01
attribution: >
  Forked from plugins/research-reva/rules/GRANT_PROPOSAL_STANDARD.md
  (SrujanaShodha v2.0.0, 2026-05-29). Publication section extracted and
  extended for PhD scholar context per REVA PhD Regulations 2025 §14.1.
tags: [publications, journals, conferences, ugc-care, scopus, tiers]
enforcement:
  tier-mismatch: warning
  predatory-journal: hard stop
  publication-minimum-shortfall: warning
  below-engineering-floor: warning
---

# PhD Scholar — Publication Standards

> *Attribution: Publication section forked from `plugins/research-reva/rules/GRANT_PROPOSAL_STANDARD.md`. PhD-specific extensions added.*

---

## Publication Minimums (REVA PhD Regulations 2025 §14.1)

For scholars of **batch 2018 and onwards**, eligibility for thesis submission requires satisfying **one** of the following options. At the time of submission, at least one publication must be **active** (i.e., accepted or published, not merely submitted).

| Option | Requirement |
|---|---|
| **A** | 3 peer-reviewed journals indexed in Scopus / WoS / UGC + 1 reputed conference paper |
| **B** | 2 peer-reviewed journals indexed in Scopus / WoS / UGC + 1 **granted** patent + 1 reputed conference paper |
| **C** | 2 Q1/Q2 journals + 1 reputed conference paper |

**Engineering & Applied Sciences floor (always applies):** At least one journal publication must be in a **Q1, Q2, or Q3** listed journal, regardless of which option the scholar satisfies.

**Authorship rule:** Scholar must be the **main author** in all qualifying publications. Guide and co-guide are co-authors. Additional co-authors require an NoC (§14.1).

**Pre-2018 batch:** At least 2 referred journal articles + 1 conference/seminar paper as main/co-author.

---

## Venue Quality Tiers

| Tier | Definition | Example Venues |
|---|---|---|
| Q1 | Top 25% of journals in Scopus CiteScore or WoS JIF | IEEE IoT Journal, TPAMI, TKDE, J-BHI |
| Q2 | 25–50% | Knowledge-Based Systems, PRL, JNCA, ASC |
| Q3 | 50–75% | PeerJ CS, IJISP, JCS |
| Q4 | Bottom 25% | Not recommended for §14.1 qualifying publications |
| UGC-CARE Gp II | Indian university-maintained approved list | Sadhana, J-IISc, DSJ, IETE JR |
| A* / A | CORE ranking (conferences) | SIGCOMM, INFOCOM, CVPR, NeurIPS, ICML |
| B | CORE ranking (conferences) | COMSNETS, HiPC, ICDCN, TrustCom |

Full venue details: `references/schools/cse/publication-venues.md`

---

## UGC CARE Context

UGC has moved away from maintaining a central CARE list and now requires each university to maintain and publish its own approved journal list. **REVA's list is pending preparation by the Research Cell** (as of 2026-06-01).

- Interim guidance: treat Scopus-indexed and WoS-indexed journals as the primary quality filter
- See `references/ugc-care-guidance.md` for the template REVA will populate when the list is ready
- Do not claim a journal is "UGC CARE approved" without confirmation from REVA Research Cell

---

## Predatory Journal / Conference Detection

**Hard stop triggers** — do not recommend or accept a venue if any of the following are true:

- [ ] Listed on Beall's List or a credible predatory publisher registry
- [ ] Cannot be verified on Scopus Source List or WoS Master Journal List
- [ ] Promises peer review turnaround in under 2 weeks
- [ ] Unsolicited email invitation to submit or join the editorial board
- [ ] Charges article processing fee without a verifiable waiver policy
- [ ] No verifiable ISSN, DOI assignment, or indexing evidence
- [ ] Editorial board listed but names are unverifiable (no institutional affiliations, no h-index)

When a hard stop triggers: state *"This venue has characteristics of a predatory journal/conference. Publishing here will not count toward §14.1 minimums and may damage the scholar's credibility. Please verify via Scopus Source List before proceeding."*

---

## Tier-Mismatch Warning

Issue a **warning** (not a hard stop) when:

- A batch 2018+ Engineering scholar targets a Q4 journal as a §14.1 qualifying publication (Engineering floor requires ≥1 Q1/Q2/Q3)
- A scholar counts a conference paper toward the journal requirement
- A scholar counts a non-granted patent toward Option B

Warning wording: *"This venue/output may not satisfy your §14.1 requirement. Confirm with your guide before submission to avoid a shortfall at thesis submission time."*

---

## Citation & Reference Standards

- **Preferred citation style for CSE:** IEEE (for engineering) or ACM (for computing theory) — confirm with guide
- **DOI required:** Every reference in thesis and publications should have a DOI where available
- **Self-citation:** Cite your own prior publications when building on them — this is legitimate and expected; flag excessive self-citation in lit reviews (>30% of references from the scholar's own work)
