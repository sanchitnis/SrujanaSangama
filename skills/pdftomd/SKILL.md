---
name: pdftomd
description: Convert PDF and office documents (DOCX, PPTX, XLSX, HTML) to Markdown by automatically choosing the best tool among Pandoc, Marker, and MarkItDown based on layout complexity, math/equations, and file format strengths.
version: 1.0.0
tags: [pdf, markdown, converter, pandoc, marker, markitdown]
---

# Document-to-Markdown (pdftomd) Conversion Skill

This skill provides decision logic, installation details, code snippets, and a helper script to convert PDF and various document formats into clean Markdown for LLM parsing, RAG pipelines, or document editing. It leverages the relative strengths of three primary tools: **Pandoc**, **Marker**, and **MarkItDown**.

---

## 1. Relative Strength Matrix

Choose the best tool for conversion by analyzing the input document structure, layout, and complexity:

| Feature / Format | Pandoc | Marker (`marker-pdf`) | MarkItDown | Recommended Choice |
|---|---|---|---|---|
| **Text-Based (Single Column) PDFs** | Fair (requires pdftotext first) | Excellent (high accuracy) | Excellent (very fast & clean) | **MarkItDown** (lightweight/fast) |
| **Complex PDFs (Multi-column/Layouts)** | Poor | Excellent (restructures columns) | Fair (may merge columns incorrectly) | **Marker** |
| **Math & Equations (PDF)** | Poor | Excellent (converts to LaTeX math) | Poor (extracts text chunks) | **Marker** |
| **Scanned PDFs / OCR** | Poor | Excellent (native Tesseract/EasyOCR) | Poor (no native image OCR) | **Marker** |
| **Word Documents (`.docx`)** | Excellent (very clean headers/tables) | N/A (PDF only) | Excellent (easy API) | **Pandoc** (cleaner nested structures) |
| **Excel Spreadsheets (`.xlsx`)** | Fair (converts to basic tables) | N/A (PDF only) | Excellent (cleans cells to MD tables) | **MarkItDown** |
| **PowerPoint Slides (`.pptx`)** | Fair | N/A (PDF only) | Excellent (slides-to-text sections) | **MarkItDown** |
| **HTML / E-books (`.epub`)** | Excellent (highly customizable) | N/A | Fair | **Pandoc** |

---

## 2. Decision Flow

```plaintext
                    [Input File Type?]
                     /              \
                 [PDF]             [Office / Text Docs]
                /     \                  /      |       \
      [Math/Scanned]  [Standard text] [DOCX]  [XLSX]  [Other]
           /               \            /       |        \
       (Marker)       (MarkItDown)  (Pandoc) (MarkItDown) (Pandoc)
```

---

## 3. Tool Installation

### 3.1 Pandoc
Pandoc is a compiled binary.
* **Windows (via winget):**
  ```powershell
  winget install JohnMacFarlane.Pandoc
  ```
* **macOS (via Homebrew):**
  ```bash
  brew install pandoc
  ```
* **Linux (Debian/Ubuntu):**
  ```bash
  sudo apt-get install pandoc
  ```

### 3.2 Marker
Marker relies on PyTorch and layout models. It requires Python 3.9+ and PyTorch.
```bash
pip install marker-pdf
```
*Note: Depending on system configurations, you may also need to install system dependencies such as Tesseract-OCR and ghostscript for scanned PDF support.*

### 3.3 MarkItDown
Microsoft's lightweight converter can be installed directly from PyPI.
```bash
pip install markitdown
```

---

## 4. Usage Recipes & CLI Examples

### 4.1 Using the Helper Script (Automatic Selection)
A helper script is provided at `skills/pdftomd/scripts/convert.py` to automate the selection of the best available tool based on the criteria above:

```bash
# Auto-select the best tool and convert:
python skills/pdftomd/scripts/convert.py input.pdf -o output.md

# Guide selection for specialized PDFs (e.g. math paper):
python skills/pdftomd/scripts/convert.py paper.pdf -o output.md --pdf-type math

# Force a specific tool:
python skills/pdftomd/scripts/convert.py document.docx -o output.md --tool pandoc
```

### 4.2 Raw Tool Command Snippets

#### Pandoc (for clean DOCX/HTML structure)
```bash
# Convert Word DOCX to GitHub Flavored Markdown (preserves tables and checklists)
pandoc -f docx -t gfm input.docx -o output.md
```

#### Marker (for complex/scanned PDFs)
```bash
# Runs the Marker command line tool on a single PDF
marker_single input.pdf --output_dir output_folder/
```

#### MarkItDown (via Python API)
```python
from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("input.xlsx")  # works on pptx, docx, html, simple pdf, etc.

with open("output.md", "w", encoding="utf-8") as f:
    f.write(result.text_content)
```

---

## 5. Developer & Integration Guidelines

* **Metadata Preservation:** Always extract and append document metadata (author, title, creation date) at the top of the converted Markdown file as a frontmatter block where possible.
* **Layout and Spacing:** After conversion, inspect for artifacts such as hyphenation split across lines (e.g., `docu-\nment`) and remove them.
* **Spreadsheets:** Excel tables converted to Markdown can be extremely wide. Recommend utilizing MarkItDown for spreadsheet extractions, and consider transposing tables if the column count exceeds 8 columns to ensure model readability.
