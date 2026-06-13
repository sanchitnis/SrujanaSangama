#!/usr/bin/env python3
"""
spec_sync.py — SrujanaSangama Specification Sync Audit Script
=============================================================

Mechanical file-presence audit: checks that every plugin's spec, tasks,
plugin directory, eval script, and eval dataset are all in place.

Outputs a Markdown drift report to eval/logs/spec_sync_YYYY-MM-DD.md

Usage:
    python skills/spec-sync/scripts/spec_sync.py
    python skills/spec-sync/scripts/spec_sync.py --output-dir eval/logs

Author: SrujanaSangama spec-sync skill
CONSTITUTION: §4 — scripts handle only mechanical work (file I/O, path checks).
              All semantic review is left to human or AI agent.
"""

import argparse
import json
import os
import re
import sys
from datetime import date
from pathlib import Path

# Force UTF-8 output so emoji in reports don't crash Windows cp1252 consoles
if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")


# ---------------------------------------------------------------------------
# Configuration — paths are relative to the repository root
# ---------------------------------------------------------------------------

SPEC_DIR = Path("specification")
PLUGINS_DIR = Path("plugins")
EVAL_DIR = Path("eval")
EVAL_DATA_DIR = EVAL_DIR / "data"
EVAL_LOGS_DIR = EVAL_DIR / "logs"

# Spec files that are platform-wide (not tied to a single plugin)
PLATFORM_SPECS = {
    "architecture.prompt.md",
    "plan.prompt.md",
    "spec.prompt.md",
    "tasks.md",
    "ADDIE.md",
    "BACKLOG.md",
    "iqac-plan-evaluator.md",
    "thirty_startup_assignments.md",
}

# Files in specification/ that are not spec/tasks pairs
NON_PLUGIN_FILES = PLATFORM_SPECS | {
    "Future AI_Learning_App_Skills_Plan.md",
    "Future with Skills_Audit_Executive_Summary.md",
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def repo_root() -> Path:
    """Walk up from this script's location to find the repo root (contains CONSTITUTION.md)."""
    p = Path(__file__).resolve().parent
    for _ in range(6):
        if (p / "CONSTITUTION.md").exists():
            return p
        p = p.parent
    # Fallback: assume CWD is repo root
    return Path.cwd()


def plugin_name_from_spec(spec_file: str) -> str:
    """Extract plugin name from a *-spec.prompt.md filename."""
    return re.sub(r"-spec\.prompt\.md$", "", spec_file)


def plugin_name_from_tasks(tasks_file: str) -> str:
    """Extract plugin name from a *-tasks.md filename."""
    return re.sub(r"-tasks\.md$", "", tasks_file)


def to_snake(name: str) -> str:
    """Convert kebab-case plugin name to snake_case for eval file matching."""
    return name.replace("-", "_")


def symbol(ok: bool | None) -> str:
    if ok is True:
        return "✅"
    if ok is False:
        return "❌"
    return "⚠️"


def symbol_ascii(ok: bool | None) -> str:
    """ASCII-safe version for console output on Windows."""
    if ok is True:
        return "[OK]"
    if ok is False:
        return "[!!]"
    return "[??]"


# ---------------------------------------------------------------------------
# Audit logic
# ---------------------------------------------------------------------------

def collect_plugin_names(root: Path) -> dict:
    """
    Discover all plugin-level items from spec files, tasks files, and plugin dirs.
    Returns a unified dict: {plugin_name: {spec, tasks, plugin_dir, eval_script, eval_dataset, eval_report}}
    """
    plugins: dict[str, dict] = {}

    def ensure(name: str) -> dict:
        if name not in plugins:
            plugins[name] = {
                "spec": False,
                "tasks": False,
                "plugin_dir": False,
                "eval_script": False,
                "eval_dataset": False,
                "eval_report": False,
            }
        return plugins[name]

    # Scan specification/ for *-spec.prompt.md files
    if (root / SPEC_DIR).exists():
        for f in (root / SPEC_DIR).iterdir():
            if f.is_file() and f.name.endswith("-spec.prompt.md") and f.name not in NON_PLUGIN_FILES:
                name = plugin_name_from_spec(f.name)
                ensure(name)["spec"] = True

        # Scan specification/ for *-tasks.md files (excluding tasks.md itself)
        for f in (root / SPEC_DIR).iterdir():
            if f.is_file() and f.name.endswith("-tasks.md") and f.name != "tasks.md" and f.name not in NON_PLUGIN_FILES:
                name = plugin_name_from_tasks(f.name)
                ensure(name)["tasks"] = True

    # Scan plugins/ directories
    if (root / PLUGINS_DIR).exists():
        for d in (root / PLUGINS_DIR).iterdir():
            if d.is_dir() and not d.name.startswith("."):
                ensure(d.name)["plugin_dir"] = True

    # Scan eval/ for eval scripts and datasets
    if (root / EVAL_DIR).exists():
        for f in (root / EVAL_DIR).iterdir():
            if f.is_file() and f.name.startswith("eval_") and f.name.endswith(".py"):
                snake = f.name[len("eval_"):-len(".py")]
                # Try to match to a known plugin
                for name in list(plugins.keys()):
                    if to_snake(name) == snake:
                        plugins[name]["eval_script"] = True
                        break
                else:
                    # Orphan eval script — add with what we know
                    kebab = snake.replace("_", "-")
                    ensure(kebab)["eval_script"] = True

        for f in (root / EVAL_DIR).iterdir():
            if f.is_file() and f.name.endswith("_eval_report.md"):
                snake = f.name[:-len("_eval_report.md")]
                for name in list(plugins.keys()):
                    if to_snake(name) == snake:
                        plugins[name]["eval_report"] = True
                        break

    if (root / EVAL_DATA_DIR).exists():
        for f in (root / EVAL_DATA_DIR).iterdir():
            if f.is_file() and f.name.endswith("_eval_dataset.json"):
                snake = f.name[:-len("_eval_dataset.json")]
                for name in list(plugins.keys()):
                    if to_snake(name) == snake:
                        plugins[name]["eval_dataset"] = True
                        break

    return plugins


def compute_drift(entry: dict) -> str:
    """Return drift severity: PASS, WARN, or FAIL."""
    if entry["spec"] and entry["tasks"] and entry["plugin_dir"] and entry["eval_script"] and entry["eval_dataset"]:
        return "PASS"
    if not entry["spec"] and not entry["tasks"] and entry["plugin_dir"]:
        return "FAIL"  # Plugin exists with no spec at all
    if entry["spec"] and not entry["tasks"]:
        return "FAIL"  # Spec without tasks
    if (entry["spec"] or entry["plugin_dir"]) and not (entry["eval_script"] and entry["eval_dataset"]):
        return "WARN"  # Missing eval coverage
    return "WARN"


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------

def build_report(plugins: dict, run_date: date) -> str:
    lines = [
        f"# Spec-Sync Audit Report — {run_date.isoformat()}",
        "",
        "> Generated by `skills/spec-sync/scripts/spec_sync.py`",
        "> This report is mechanical (file-presence only). Semantic review requires human or AI agent assessment.",
        "",
        "---",
        "",
        "## Summary",
        "",
    ]

    pass_count = sum(1 for v in plugins.values() if compute_drift(v) == "PASS")
    warn_count = sum(1 for v in plugins.values() if compute_drift(v) == "WARN")
    fail_count = sum(1 for v in plugins.values() if compute_drift(v) == "FAIL")

    lines += [
        f"- ✅ **PASS**: {pass_count} plugins — all files present",
        f"- ⚠️ **WARN**: {warn_count} plugins — missing eval coverage",
        f"- ❌ **FAIL**: {fail_count} plugins — critical files missing",
        "",
        "---",
        "",
        "## Detail Table",
        "",
        "| Plugin | Spec | Tasks | Plugin Dir | Eval Script | Eval Dataset | Eval Report | Status |",
        "|---|---|---|---|---|---|---|---|",
    ]

    for name in sorted(plugins.keys()):
        e = plugins[name]
        drift = compute_drift(e)
        status_icon = {"PASS": "✅ PASS", "WARN": "⚠️ WARN", "FAIL": "❌ FAIL"}[drift]
        lines.append(
            f"| `{name}` "
            f"| {symbol(e['spec'])} "
            f"| {symbol(e['tasks'])} "
            f"| {symbol(e['plugin_dir'])} "
            f"| {symbol(e['eval_script'])} "
            f"| {symbol(e['eval_dataset'])} "
            f"| {symbol(e['eval_report'])} "
            f"| {status_icon} |"
        )

    lines += [
        "",
        "---",
        "",
        "## Action Items",
        "",
    ]

    fail_items = [(n, e) for n, e in plugins.items() if compute_drift(e) == "FAIL"]
    warn_items = [(n, e) for n, e in plugins.items() if compute_drift(e) == "WARN"]

    if fail_items:
        lines.append("### ❌ Critical — Must Fix Before Next Sprint")
        lines.append("")
        for name, e in sorted(fail_items):
            actions = []
            if not e["spec"]:
                actions.append(f"Create `specification/{name}-spec.prompt.md`")
            if not e["tasks"]:
                actions.append(f"Create `specification/{name}-tasks.md`")
            if not e["plugin_dir"]:
                actions.append(f"Create `plugins/{name}/` directory structure")
            for a in actions:
                lines.append(f"- **`{name}`**: {a}")
        lines.append("")

    if warn_items:
        lines.append("### ⚠️ Warnings — Missing Eval Coverage")
        lines.append("")
        for name, e in sorted(warn_items):
            actions = []
            if not e["eval_script"]:
                actions.append(f"Create `eval/eval_{to_snake(name)}.py`")
            if not e["eval_dataset"]:
                actions.append(f"Create `eval/data/{to_snake(name)}_eval_dataset.json`")
            if not e["eval_report"]:
                actions.append(f"Run eval and create `eval/{to_snake(name)}_eval_report.md`")
            for a in actions:
                lines.append(f"- **`{name}`**: {a}")
        lines.append("")

    if not fail_items and not warn_items:
        lines.append("No drift detected. All plugins are fully specced and evaluated. ✅")
        lines.append("")

    lines += [
        "---",
        "",
        "*Add unspecced ideas to `specification/BACKLOG.md`. Promote to a spec sprint via `AGENTS.md` Coordinator flow.*",
    ]

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="SrujanaSangama Spec-Sync Audit — checks spec/tasks/plugin/eval alignment."
    )
    parser.add_argument(
        "--output-dir",
        default=str(EVAL_LOGS_DIR),
        help=f"Directory to write the Markdown report (default: {EVAL_LOGS_DIR})",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print report to stdout only; do not write to disk.",
    )
    args = parser.parse_args()

    root = repo_root()
    print(f"[spec_sync] Repository root: {root}")

    plugins = collect_plugin_names(root)
    print(f"[spec_sync] Discovered {len(plugins)} plugin entries.")

    run_date = date.today()
    report = build_report(plugins, run_date)

    if args.dry_run:
        print(report)
    else:
        out_dir = root / args.output_dir
        out_dir.mkdir(parents=True, exist_ok=True)
        out_file = out_dir / f"spec_sync_{run_date.isoformat()}.md"
        out_file.write_text(report, encoding="utf-8")
        print(f"[spec_sync] Report written to: {out_file}")

    # Exit non-zero if any FAIL entries
    fail_count = sum(1 for v in plugins.values() if compute_drift(v) == "FAIL")
    if fail_count:
        print(f"[spec_sync] ❌ {fail_count} FAIL(s) detected. See report for details.")
        sys.exit(1)

    warn_count = sum(1 for v in plugins.values() if compute_drift(v) == "WARN")
    if warn_count:
        print(f"[spec_sync] ⚠️  {warn_count} WARN(s) detected. See report for details.")
        sys.exit(0)  # Warnings are not blocking

    print("[spec_sync] ✅ All checks passed.")


if __name__ == "__main__":
    main()
