---
name: docling-converter
description: Convert PDFs, DOCX, XLSX, PPTX, and images to Markdown for LLM processing or RAG workflows using the Docling SDK. Use whenever the user needs to parse documents.
---

# Docling Document Conversion Skill

This skill provides instructions on how to use `docling` to extract structured data from complex files and convert them into clean Markdown.

## 1. Prerequisites
Ensure you have the `docling` library installed in your environment:
```bash
pip install docling
```

## 2. Supported Formats
The agent should be capable of converting the following formats:
- PDF (Native and Scanned/OCR)
- Word (DOCX)
- PowerPoint (PPTX)
- Excel (XLSX, XLS)
- Images and HTML

## 3. Workflow & Usage Instructions
When a user asks to convert a file or folder, use the following Python script to perform the conversion:

```python
from docling.document_converter import DocumentConverter
from pathlib import Path

def convert_to_md(file_path: str, output_dir: str = "output_docs"):
    converter = DocumentConverter()
    
    # Perform conversion
    result = converter.convert(file_path)
    
    # Export to Markdown
    markdown_output = result.document.export_to_markdown()
    
    # Save output
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    target_file = output_path / f"{Path(file_path).stem}.md"
    with open(target_file, "w", encoding="utf-8") as f:
        f.write(markdown_output)
        
    print(f"Successfully saved to {target_file}")
```

## 4. Context Extraction Guidelines
- **Tables:** Docling is highly accurate with tabular data. Ensure the output preserves table structures using native Markdown tables rather than text alignment.
- **Images/Visuals:** If extracting an image-heavy PDF, you can use Docling's advanced options (VLM) to ensure images are appropriately annotated.
- **Error Handling:** If a file fails to parse natively, gracefully fall back to full-page OCR options.
