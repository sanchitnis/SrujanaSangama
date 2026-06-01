---
name: UGC Journal Approval Guidance
description: Template and guidance for REVA University's own UGC-approved journal list — context on the UGC policy change, required schema, interim fallback guidance, and a callout for the Research Cell.
version: "1.0"
tags: [ugc, journals, approval, reva, research-cell]
status: PENDING REVA RESEARCH CELL
---

# UGC Journal Approval Guidance

---

## Context: UGC Policy Change

The University Grants Commission (UGC) previously maintained a centralised **CARE (Consortium for Academic and Research Ethics) List** of approved journals. That central list has been discontinued.

Under the revised UGC policy, **each university is now responsible for preparing and maintaining its own list of approved journals** for the purposes of PhD publication requirements and faculty promotion criteria.

REVA PhD scholars should no longer rely on a third-party "UGC-CARE list" as a guarantee of institutional acceptance. The applicable standard is whether a journal appears on **REVA University's own approved journal list**, prepared and maintained by the REVA Research Cell.

---

> ⚠️ **PENDING REVA RESEARCH CELL**
>
> As of 2026-06-01, REVA University's own UGC-approved journal list has **not yet been prepared** by the Research Cell.
>
> Until this list is published:
> - Scholars should use Scopus and WoS (SCIE / ESCI) indexing as the primary quality indicator
> - Scholars should discuss specific journal choices with their guide before submitting
> - The REVA Research Cell should be contacted directly for the most current guidance
>
> This file will be updated when the REVA Research Cell publishes the approved list.

---

## Schema for REVA's Approved Journal List

When the Research Cell prepares the list, it should follow this schema (one row per journal):

| Column | Description |
|---|---|
| `journal_title` | Full journal title as registered with the publisher |
| `issn_print` | Print ISSN |
| `issn_online` | Online/E-ISSN |
| `publisher` | Publisher name |
| `domain_tags` | Subject area tags (e.g., Computer Science, Electrical Engineering, Management) |
| `scopus_indexed` | Yes / No |
| `wos_scie_indexed` | Yes / No |
| `wos_esci_indexed` | Yes / No |
| `quartile` | Q1 / Q2 / Q3 / Q4 / Unranked |
| `approval_date` | Date REVA Research Cell approved this journal (YYYY-MM-DD) |
| `review_cycle` | How often this entry is reviewed (e.g., Annual) |
| `notes` | Any restrictions or conditions (e.g., "eligible for PhD count from 2024 only") |

---

## Interim Fallback Guidance (Until REVA List Is Published)

In the absence of REVA's own list, scholars and guides should use the following resources to evaluate journal quality:

1. **Scopus Source List**
   URL: https://www.scopus.com/sources.uri
   Filter by: subject area, title keyword, ISSN
   Status: free to search; updated regularly

2. **Clarivate Web of Science Master Journal List**
   URL: https://mjl.clarivate.com/
   Filter by: title, ISSN, subject category
   Status: free to search; updated regularly

3. **Beall's List (updated community version)**
   URL: https://beallslist.net/
   Use: identify potential predatory journals to **avoid**
   Note: Beall's List is community-maintained; cross-check against Scopus/WoS before acting on it alone

4. **SCImago Journal Rankings (SJR)**
   URL: https://www.scimagojr.com/
   Use: verify quartile and h-index of any Scopus-indexed journal

5. **Guide consultation:** For any journal not clearly indexed in Scopus or WoS, the scholar must obtain written confirmation from their guide before submitting. This protects the scholar in the event of regulatory scrutiny.

---

## What Counts for PhD Publication Requirements

Until REVA publishes its own list, the following interpretation is recommended based on the REVA PhD Regulations 2025 (§14.1):

| Publication Type | Counts For §14.1? | Guidance |
|---|---|---|
| Scopus-indexed journal (not predatory) | Yes | Verify via Scopus Source List |
| WoS-SCIE journal | Yes | Verify via WoS Master Journal List |
| WoS-ESCI journal | Case-by-case | Discuss with guide; ESCI is indexed but not assigned impact factor |
| UGC-approved journal (once REVA list is published) | Yes (per REVA Research Cell confirmation) | Await REVA list |
| Conference proceedings (IEEE/ACM sponsored, with ISBN) | Counts as the required conference paper | Verify sponsorship |
| Open-access journal (Scopus-indexed, DOAJ gold) | Yes, if Scopus-indexed | Not all open-access journals are indexed |
| Predatory journal (on Beall's List, no Scopus/WoS) | No | Hard stop — do not submit |
