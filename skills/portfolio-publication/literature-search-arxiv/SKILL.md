---
name: literature-search-arxiv
description: >
  Search for scientific papers, preprints, and publications on arXiv. Extract
  metadata, abstracts, and download full-text PDFs or HTML versions of papers.
  Use when the user asks to find research papers, literature, or specific arXiv
  IDs.
---

# arXiv Search and Retrieval

## Prerequisites

1. **`uv`**: Ensure `uv` Python package manager is installed on the system.
2. **User Notification**: Check that the user is aware of arXiv's Terms of Use (https://info.arxiv.org/help/api/index.html) and paper licenses before downloading.

## Core Rules

- **Terms of Use**: Respect arXiv's rate limit: maximum 1 request every 3 seconds. The helper client automatically manages this rate limit.
- Document and list the URLs of all papers that were used to produce the output.

## Utility Scripts

All commands below should be run from the repository root directory.

### 1. Search and Extract Metadata

Search arXiv and return a clean JSON array of matching papers.

```powershell
uv run plugins/srujana-shodha/skills/literature-search-arxiv/scripts/search_arxiv.py --query "au:einstein AND ti:relativity" --max_results 5 2>$null > arxiv_search_results.json
```

> **Important**: The tool outputs a large JSON result. Limit `--max_results` (e.g. 5–10) or paginate using `--start`. Always redirect output to a file and parse it separately to avoid terminal truncation or context overflow.

*Returned Metadata:* JSON results include `id`, `title`, `summary`, `published`, `authors`, `pdf_url`, `primary_category`, `doi`, `journal_ref`, and `comment`.

*Options:*
- `--query`: Search string (e.g., `au:einstein AND ti:relativity`). See [query_syntax.md](references/query_syntax.md) for details.
- `--id_list`: Comma-separated list of arXiv IDs to fetch directly (e.g. `1706.03762v5`).
- `--start`: Pagination offset (default 0).
- `--max_results`: Number of results to return (default 10).
- `--sort_by`: `relevance`, `lastUpdatedDate`, or `submittedDate`.
- `--sort_order`: `ascending` or `descending`.

### 2. Download Paper (PDF or HTML)

Download the full text of a paper to a file in the workspace.

```powershell
uv run plugins/srujana-shodha/skills/literature-search-arxiv/scripts/download_paper.py --id 1706.03762 --format pdf --output paper.pdf
```

*Options:*
- `--id`: The arXiv ID (e.g., `1706.03762` or `1706.03762v5`).
- `--format`: `pdf` or `html`. Note: HTML is only available for newer papers.
- `--output`: Filepath to save the downloaded document.

### 3. Download Paper Source (tar.gz)

Download the LaTeX source files of a paper.

```powershell
uv run plugins/srujana-shodha/skills/literature-search-arxiv/scripts/download_paper_source.py --id 2010.11645 --output source.tar.gz
```

*Safe Extraction Requirements*: Always extract into a dedicated subdirectory to avoid cluttering your workspace:
```powershell
mkdir paper_source; tar -xzf source.tar.gz -C paper_source
```

## Reference

- **Advanced Query Syntax**: See [query_syntax.md](references/query_syntax.md) for prefixes (`au`, `ti`, `abs`), booleans, and date filtering.

## Workflow

1. Search for papers using `search_arxiv.py`. Review the JSON summaries.
2. If full text is needed, use `download_paper.py` to fetch the PDF or HTML.
3. Read the downloaded file using standard file viewing tools.
