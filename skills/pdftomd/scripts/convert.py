import os
import sys
import subprocess
import argparse
import shutil
from pathlib import Path

def is_tool_installed(name):
    """Check whether name is on PATH and marked as executable."""
    return shutil.which(name) is not None

def run_pandoc(input_path, output_path):
    """Convert input document to Markdown using Pandoc."""
    input_path = Path(input_path)
    ext = input_path.suffix.lower()
    
    # Map extensions to pandoc format names
    fmt_map = {
        '.docx': 'docx',
        '.html': 'html',
        '.htm': 'html',
        '.epub': 'epub',
        '.odt': 'odt',
        '.rst': 'rst',
        '.latex': 'latex',
        '.tex': 'latex'
    }
    
    from_fmt = fmt_map.get(ext, 'auto')
    
    # We use gfm (GitHub Flavored Markdown) for cleaner tables and layouts
    cmd = ["pandoc", "-f", from_fmt, "-t", "gfm", str(input_path), "-o", str(output_path)]
    print(f"Running command: {' '.join(cmd)}")
    
    try:
        result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("Pandoc conversion completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error during Pandoc execution: {e.stderr}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"Failed to run Pandoc: {e}", file=sys.stderr)
        return False

def run_marker(input_path, output_dir, output_file_name=None):
    """Convert PDF to Markdown using Marker CLI."""
    if not is_tool_installed("marker_single"):
        print("Error: 'marker_single' CLI tool is not installed on PATH.", file=sys.stderr)
        print("Please install it via: pip install marker-pdf", file=sys.stderr)
        return False
    
    input_path = Path(input_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    cmd = ["marker_single", str(input_path), "--output_dir", str(output_dir)]
    print(f"Running command: {' '.join(cmd)}")
    
    try:
        result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("Marker conversion completed successfully!")
        
        # Marker generates output in output_dir / <stem> / <stem>.md
        # Let's move/copy it to the expected output_file_name if provided
        generated_folder = output_dir / input_path.stem
        generated_file = generated_folder / f"{input_path.stem}.md"
        
        if generated_file.exists() and output_file_name:
            target_file = output_dir / output_file_name
            shutil.copy2(generated_file, target_file)
            print(f"Copied Marker output to {target_file}")
            
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error during Marker execution: {e.stderr}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"Failed to run Marker: {e}", file=sys.stderr)
        return False

def run_markitdown(input_path, output_path):
    """Convert input document to Markdown using Microsoft MarkItDown."""
    try:
        from markitdown import MarkItDown
    except ImportError:
        print("Error: 'markitdown' Python package is not installed.", file=sys.stderr)
        print("Please install it via: pip install markitdown", file=sys.stderr)
        return False

    print(f"Running MarkItDown on {input_path}...")
    try:
        md = MarkItDown()
        result = md.convert(str(input_path))
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(result.text_content)
        
        print(f"MarkItDown conversion completed successfully! Output saved to {output_path}")
        return True
    except Exception as e:
        print(f"Error during MarkItDown execution: {e}", file=sys.stderr)
        return False

def main():
    parser = argparse.ArgumentParser(description="Multi-tool Document-to-Markdown Converter (Pandoc, Marker, MarkItDown)")
    parser.add_argument("input", help="Path to the input document (PDF, DOCX, PPTX, XLSX, HTML, etc.)")
    parser.add_argument("-o", "--output", help="Path to the output Markdown file")
    parser.add_argument("-d", "--output-dir", help="Directory to store outputs (defaults to input file directory)")
    parser.add_argument("-t", "--tool", choices=["auto", "pandoc", "marker", "markitdown"], default="auto",
                        help="Specify the tool to use (default: auto)")
    parser.add_argument("--pdf-type", choices=["auto", "text", "scanned", "math", "layout"], default="auto",
                        help="Guide the tool selection for PDF files (default: auto)")
    
    args = parser.parse_args()
    
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: Input file does not exist: {input_path}", file=sys.stderr)
        sys.exit(1)
        
    ext = input_path.suffix.lower()
    
    # Establish output directory
    if args.output_dir:
        output_dir = Path(args.output_dir)
    else:
        output_dir = input_path.parent
        
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Establish output file path
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = output_dir / f"{input_path.stem}.md"
        
    tool = args.tool
    
    # Decision Logic (Auto-Selection)
    if tool == "auto":
        if ext == ".pdf":
            # PDF selection logic
            if args.pdf_type in ["math", "layout", "scanned"]:
                if is_tool_installed("marker_single"):
                    tool = "marker"
                    print(f"Selected 'marker' for PDF type '{args.pdf_type}' because 'marker_single' is available.")
                else:
                    tool = "markitdown"
                    print(f"Selected 'markitdown' for PDF type '{args.pdf_type}' because 'marker_single' is not installed (fallback).")
            else:
                # Default for simple PDF or text-based PDF
                tool = "markitdown"
                print("Selected 'markitdown' as the default lightweight PDF text extractor.")
        elif ext in [".docx", ".html", ".htm", ".epub", ".odt"]:
            # Word & textual documents
            if is_tool_installed("pandoc"):
                tool = "pandoc"
                print(f"Selected 'pandoc' for {ext} because 'pandoc' is installed on PATH (superior text/table structure).")
            else:
                tool = "markitdown"
                print(f"Selected 'markitdown' for {ext} because 'pandoc' is not installed on PATH.")
        elif ext in [".pptx", ".xlsx", ".xls", ".zip"]:
            # Slides, spreadsheets, archives
            tool = "markitdown"
            print(f"Selected 'markitdown' for {ext} (native support for slides, spreadsheets, and zip archives).")
        else:
            # Fallback
            if is_tool_installed("pandoc"):
                tool = "pandoc"
            else:
                tool = "markitdown"
            print(f"Selected '{tool}' as fallback for unknown extension {ext}.")
            
    # Execute the selected tool
    success = False
    if tool == "pandoc":
        if not is_tool_installed("pandoc"):
            print("Error: Pandoc is selected but not installed on PATH. Falling back to MarkItDown...", file=sys.stderr)
            success = run_markitdown(input_path, output_path)
        else:
            success = run_pandoc(input_path, output_path)
            
    elif tool == "marker":
        if not is_tool_installed("marker_single"):
            print("Error: Marker is selected but 'marker_single' is not installed. Falling back to MarkItDown...", file=sys.stderr)
            success = run_markitdown(input_path, output_path)
        else:
            success = run_marker(input_path, output_dir, output_path.name)
            
    elif tool == "markitdown":
        success = run_markitdown(input_path, output_path)
        
    if success:
        print(f"Conversion succeeded! Output stored at: {output_path}")
        sys.exit(0)
    else:
        print("Conversion failed.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
