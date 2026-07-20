# Proposal: Faculty Onboarding Process Enhancement

## Problem
The current faculty onboarding workflow (`domains/srujana-shodha/commands/onboarding.md`) does not specify collecting a full set of academic/social profiles (LinkedIn, GitHub, ORCID, Google Scholar, Vidwan, IRINS, Scopus, Shodhganga) or saving them to local memory. It also lacks a standardized template for doctoral theses that can be imported directly into the Vidwan portal.

## Proposed Change
1. **Enhance Phase 1 & Phase 2 of Onboarding**: Add option to upload existing CV/documents or share online links. Instruct the agent to extract information automatically and only prompt manually for missing/unclear details.
2. **Enhance Phase 6 (Memory Initialisation & Review)**: Direct the agent to update `my-memory/faculty-profile.md` and `public-memory/profile.md` and present them to the user for final review and refinement.
3. **Add Vidwan Thesis Import Template**: Add a `doctoral_theses.csv` section with a table:
   `researcher_name, theses_title, theses_awarded_institute, theses_awarded_year`
   noting it can be imported into Vidwan.

## Scope Boundaries

### In Scope
- Modifying `domains/srujana-shodha/commands/onboarding.md`.
- Updating `IMPLEMENTATION-STATUS.md` to log changes.

### Out of Scope
- Modifying PhD Scholar onboarding or other domains.
- Adding code implementation (only markdown workflow description).

## Verification
- File `onboarding.md` has the new phase instructions, relative memory path updates, and the `doctoral_theses.csv` template.
