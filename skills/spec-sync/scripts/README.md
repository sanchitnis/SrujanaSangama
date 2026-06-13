# spec_sync.py — Usage Guide

## Overview

`spec_sync.py` is a mechanical file-presence audit script for the SrujanaSangama repository.
It checks that every plugin's spec, tasks, plugin directory, eval script, and eval dataset are all in place.

## Requirements

- Python 3.8 or higher
- Run from the **repository root** (the directory containing `CONSTITUTION.md`)

## Usage

```powershell
# Standard run (writes report to eval/logs/)
python skills/spec-sync/scripts/spec_sync.py

# Custom output directory
python skills/spec-sync/scripts/spec_sync.py --output-dir eval/logs

# Dry run — print to stdout only, no file written
python skills/spec-sync/scripts/spec_sync.py --dry-run
```

## Output

- **Console**: Summary table with PASS / WARN / FAIL counts.
- **File**: `eval/logs/spec_sync_YYYY-MM-DD.md` — full Markdown drift report.

## Exit Codes

| Code | Meaning |
|---|---|
| `0` | All checks pass or only warnings (non-blocking) |
| `1` | One or more FAIL entries detected (missing critical files) |

## What It Checks

| Check | Pass Condition |
|---|---|
| Spec ↔ Tasks | Every `*-spec.prompt.md` has a matching `*-tasks.md` |
| Spec ↔ Plugin dir | Every spec has a matching `plugins/<name>/` directory |
| Plugin ↔ Eval script | Every plugin has `eval/eval_<name>.py` |
| Plugin ↔ Eval dataset | Every plugin has `eval/data/<name>_eval_dataset.json` |
| Orphan plugins | Every `plugins/<name>/` has a spec |
| Tasks ↔ Eval report | Every tasks file has `eval/<name>_eval_report.md` |

## What It Does NOT Check

- File content or semantic correctness (that's for AI agents)
- Whether tasks in `*-tasks.md` are reflected in actual plugin files
- Whether eval datasets have sufficient diversity or quality

## Adding a New Plugin

When you add a new plugin, the script will detect and report:
- ❌ If you create a `plugins/<name>/` directory without a spec or tasks file
- ⚠️ If you have a spec and plugin directory but no eval coverage

Resolve FAIL items before starting a new sprint. Add eval coverage as part of the plugin's verification phase.
