# course-buddy-builder

A build tool that takes a structured course descriptor, feeds course materials into Google NotebookLM, and generates three student-ready knowledge artefacts per course:

1. **Knowledge wiki** — Obsidian-format Markdown pages (concept-by-concept, multi-level, wikilinked)
2. **Workbook** — Jupyter notebook with exercises pulled from NotebookLM quiz output
3. **Course Buddy skill** — A Socratic tutor skill file ready to drop into `agents/course-buddyes/instances/`

Anchored by: [references/ai-tutor-philosophy.md](../../references/ai-tutor-philosophy.md)

---

## Constraint

**C2 — Free-tier compatible.** This tool calls the Google NotebookLM API via `notebooklm-py` (unofficial Python client). NotebookLM is available on Google's free tier. Heavy batched usage may be throttled. Use `--skip-notebooklm` for template-only output with no API calls (C1-compatible).

---

## Requirements

- Python 3.10+
- `pip install -r requirements.txt`
- First-time NotebookLM auth: `notebooklm login` (opens browser; saves cookie session)

### Optional
- Jupyter (`pip install notebook`) — to open and run generated workbooks
- Obsidian (free desktop app) — to browse generated wiki with wikilink graph

---

## How to run

### Full pipeline (requires NotebookLM auth)
```bash
python3 build.py --course-file templates/course-descriptor.md --output-dir ../../knowledge/
```

### Dry run (no files written, no API calls)
```bash
python3 build.py --course-file templates/course-descriptor.md --output-dir ../../knowledge/ --dry-run
```

### Template-only (generates artefacts from descriptor alone, no NotebookLM calls)
```bash
python3 build.py --course-file templates/course-descriptor.md --output-dir ../../knowledge/ --skip-notebooklm
```

### Refresh existing course (re-query NotebookLM with updated sources or gap topics)
```bash
python3 build.py --course-file templates/course-descriptor.md --output-dir ../../knowledge/ --refresh
```

### Refresh with eval gap topics (from eval backlog)
```bash
python3 build.py --course-file templates/course-descriptor.md --output-dir ../../knowledge/ --refresh --gap-topics "dynamic programming intuition, heap vs BST tradeoffs"
```

---

## Output structure (per course)

```
knowledge/
  [CourseCode]-[ShortName]/          e.g. CSE301-DSA/
    wiki/
      index.md                       Course overview, unit links, NLM audio embed
      [concept-slug].md              One page per key concept (multi-level: beginner/intermediate/advanced)
      glossary.md                    All key terms, auto-generated from NLM study guide
      concept-map.md                 Mermaid diagram from NLM mind map JSON
      .obsidian/
        app.json                     Minimal Obsidian vault config (turnkey)
    workbook.ipynb                   Jupyter notebook (one section per unit)
    flashcards.md                    Markdown flashcards from NLM
    audio-overview.mp3               NLM audio overview (if generated)
    faculty-notes/
      README.md                      How to add faculty notes
    student-contributions/
      README.md                      How to submit student contributions
    CONTRIBUTING.md                  Contribution guide for this course
  instances/
    [CourseCode]-[ShortName]/
      skill.md                       Course Buddy skill (Socratic tutor, drop into agents/course-buddyes/instances/)
```

---

## Example output (dry run, condensed)
```
[DRY RUN] Course: CSE301 — Data Structures and Algorithms
[DRY RUN] Would create: knowledge/CSE301-DSA/wiki/index.md
[DRY RUN] Would create: knowledge/CSE301-DSA/wiki/big-o-notation.md (3 levels)
[DRY RUN] Would create: knowledge/CSE301-DSA/wiki/binary-search-tree.md (3 levels)
... (22 concept pages)
[DRY RUN] Would create: knowledge/CSE301-DSA/wiki/glossary.md
[DRY RUN] Would create: knowledge/CSE301-DSA/wiki/concept-map.md
[DRY RUN] Would create: knowledge/CSE301-DSA/workbook.ipynb (6 units, 48 cells)
[DRY RUN] Would create: knowledge/CSE301-DSA/flashcards.md
[DRY RUN] Would create: instances/CSE301-DSA/skill.md
[DRY RUN] Skipped: NotebookLM API calls (dry-run mode)
```

---

## Module overview

| File | Purpose |
|------|---------|
| `build.py` | CLI entry point; orchestrates the full pipeline |
| `notebooklm_connector.py` | Async `notebooklm-py` wrapper; produces structured dict of NLM outputs |
| `wiki_generator.py` | Converts NLM study guide + mind map into Obsidian wiki pages |
| `workbook_generator.py` | Generates Jupyter `.ipynb` from quiz JSON + unit structure |
| `skill_generator.py` | Generates Course Buddy skill.md from instance template + NLM data |
| `eval_bridge.py` | (Optional) Scans eval backlog for F-9 gap topics by course code; feeds `--refresh` |
| `templates/course-descriptor.md` | Input template — fill one per course |

---

## NotebookLM auth notes

`notebooklm-py` uses Google cookie authentication (no official API key needed). First-time setup:

```bash
notebooklm login          # Opens browser; log in with your Google account
```

Subsequent runs reuse the saved session. If running in a team, each faculty member authenticates with their own Google account. The tool does not store or transmit credentials beyond the local cookie file managed by `notebooklm-py`.

See [notebooklm-py troubleshooting](https://github.com/teng-lin/notebooklm-py/blob/main/docs/troubleshooting.md) if auth fails.

---

## Related files

| File | Role |
|------|------|
| [references/ai-tutor-philosophy.md](../../references/ai-tutor-philosophy.md) | Governing philosophy for wiki/workbook design |
| [agents/course-buddy-builder.md](../../agents/course-buddy-builder.md) | Agent spec for AI-assisted build/refresh/audit |
| [agents/course-buddyes/_course-buddy-instance-template.md](../../agents/course-buddyes/_course-buddy-instance-template.md) | Template used by skill_generator.py |
| [knowledge/README.md](../../knowledge/README.md) | Output folder conventions and contribution model |
| [eval/data/IMPROVEMENT-BACKLOG.md](../../eval/data/IMPROVEMENT-BACKLOG.md) | F-9 domain gap source for eval_bridge.py |
