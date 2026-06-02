# Plan: `format-convertor` Skill

**TL;DR:** Create a robust, generalized `format-convertor` skill and associated Python wrapper tool in SrujanaSangama to handle document conversions (Markdown, DOCX, HTML, PDF) using Pandoc.

---

## Proposed Changes

### 1. [NEW] [SKILL.md](file:///d:/Github/SrujanaSangama/skills/format-convertor/SKILL.md)
The main skill definition file.
- Outlines supported formats: Markdown (`.md`), Word Document (`.docx`), HTML (`.html`), PDF (`.pdf`), RTF (`.rtf`), EPUB (`.epub`).
- Describes usage triggers and operating modes (Direct CLI vs Python Wrapper).
- Includes error troubleshooting guidelines for Pandoc dependencies (e.g., LaTeX/Typst/wkhtmltopdf for PDF generation).

### 2. [NEW] [convert.py](file:///d:/Github/SrujanaSangama/tools/format-convertor/convert.py)
A Python wrapper script to safely execute Pandoc conversion tasks.
- Checks if Pandoc is installed on system PATH.
- Validates input files, output file paths, and format compatibilities.
- Gracefully handles PDF conversions by trying Typst or wkhtmltopdf/weasyprint if standard PDF engines are missing, and providing informative help messages on failure.

---

## Verification

1. **Direct Markdown to DOCX**: Converting a Markdown file to `.docx` succeeds and preserves basic headers, tables, lists, and formatting.
2. **Direct Markdown to HTML**: Converting a Markdown file to `.html` succeeds.
3. **DOCX to Markdown**: Converting a Word document back to Markdown succeeds.
4. **Environment Check**: Running the wrapper without pandoc installed or with invalid formats triggers a clear, helpful error message.
5. **PDF Fallbacks**: Graceful degradation or instruction set when PDF compilation engines (like Typst or LaTeX) are not configured.

---

## Decisions (Confirmed)

1. **Skill Name**: `format-convertor`
2. **Implementation Strategy**: Markdown-native skill instruction (`skills/format-convertor/SKILL.md`) paired with a robust python helper (`tools/format-convertor/convert.py`) following CONSTITUTION.md guidelines.
3. **Pandoc dependency**: Relies on Pandoc being installed on the user's system PATH.

---

## Scope Boundaries

- **In scope**: General document format conversion (Markdown, DOCX, HTML, PDF, RTF, EPUB) using Pandoc and the Python wrapper.
- **Out of scope**: Non-pandoc proprietary file conversions (e.g., XLS, PPTX, CAD files).
