# Plan: `bizcard` Skill

**TL;DR:** Create a robust, Markdown-native `bizcard` skill in SrujanaSangama to scan and extract contact information from business cards in `my-memory/bizcard/` and update `my-memory/semantic/collaborators.md`.

---

## Proposed Changes

### 1. [NEW] [SKILL.md](file:///d:/Github/SrujanaSangama/skills/bizcard/SKILL.md)
The main skill definition file.
- YAML frontmatter defining name `bizcard` and description.
- Trigger conditions: User mentions business cards, contact scanning, uploading a business card, or processing images in `my-memory/bizcard/`.
- Clear multi-card detection instructions: Agent utilizes `view_file` to OCR/process images in `my-memory/bizcard/`.
- Strict details extraction layout.
- Indian context phone number normalization rules.
- User confirmation layout template.
- Duplicate contact detection logic: parsing `my-memory/semantic/collaborators.md` to match name/phone against existing records.
- Google People API Person Resource format generation instructions when "Save" is selected.
- Logic to append new contacts to `my-memory/semantic/collaborators.md` in the established Markdown format.

---

## Verification

1. **Card Parsing**: Verify that the agent can read a business card image from `my-memory/bizcard/` (or via simulation), extract and normalize details.
2. **Indian Phone Normalization**: Verify phone numbers format to `+91-XXXXX-XXXXX`.
3. **Duplicate Check Simulation**: Verify duplicate contact warning triggers if name/phone matches an entry in `collaborators.md`.
4. **Output & Save**: Verify the Google People API JSON output and the markdown insertion into `my-memory/semantic/collaborators.md`.

---

## Decisions (Confirmed)

1. **Skill Name**: `bizcard`
2. **Centralized Memory Location**: Reads from and writes to `D:\Github\srujana-memory\my-memory\`.
3. **Contact File**: Appends new contacts to `my-memory/semantic/collaborators.md` following its existing structure.
4. **Image Location**: Scans for files in the subfolder `my-memory/bizcard/`.

---

## Scope Boundaries

- **In scope**: Scanning card images in `my-memory/bizcard/`, extracting fields, Indian localization, formatting confirmation menu, simulating duplicate checks against `my-memory/semantic/collaborators.md`, formatting output to Google People API JSON, and updating `my-memory/semantic/collaborators.md`.
- **Out of scope**: Direct API integration with Google People API (handled externally via the generated JSON payload).
