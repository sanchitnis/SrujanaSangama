#!/usr/bin/env python3
"""
NotebookLM Connector — async wrapper around notebooklm-py
Constraint: C2 (Google NotebookLM free tier; no paid API key required)
Requirement: notebooklm-py[browser]>=0.4.0  (pip install "notebooklm-py[browser]")
Auth setup:  notebooklm login   (one-time browser login; stores cookie session locally)

Returns a structured dict consumed by wiki_generator, workbook_generator, skill_generator.
"""
from __future__ import annotations

import asyncio
import json
import re
import sys
import tempfile
from pathlib import Path
from typing import Any


class NotebookLMConnector:
    """
    Orchestrates a NotebookLM notebook lifecycle for one course:
      1. Create (or reuse) a notebook named after the course.
      2. Add all sources from the course descriptor.
      3. Generate: study guide (Markdown), quiz (JSON), flashcards (Markdown),
                   mind map (JSON), audio overview (MP3).
      4. Download all artefacts to a temp directory.
      5. Return a structured dict for downstream generators.
    """

    NB_NAME_PREFIX = "SrujanaBuddy-"

    def __init__(self, course_code: str, course_name: str) -> None:
        self.course_code = course_code
        self.course_name = course_name
        self.nb_name = f"{self.NB_NAME_PREFIX}{course_code}"

    async def run(
        self,
        sources: dict[str, Any],
        units: list[dict],
        gap_topics: list[str] | None = None,
        refresh: bool = False,
    ) -> dict[str, Any]:
        """
        Execute the full NotebookLM pipeline and return artefact data.

        Returns a dict with keys:
          study_guide_md  : str   — full study guide Markdown text
          quiz_items      : list  — list of {question, options, answer, explanation} dicts
          flashcards_md   : str   — Markdown flashcard list
          mind_map_json   : dict  — NLM mind map hierarchy JSON
          audio_path      : str | None — local path to downloaded MP3 (may be None)
          concept_deps    : list  — flat list of concept names extracted from mind map
        """
        try:
            from notebooklm import NotebookLMClient  # type: ignore
        except ImportError:
            print(
                "[ERROR] notebooklm-py is not installed. Run: pip install 'notebooklm-py[browser]'",
                file=sys.stderr,
            )
            raise

        async with await NotebookLMClient.from_storage() as client:
            nb_id = await self._get_or_create_notebook(client, refresh)
            await self._add_sources(client, nb_id, sources)

            # Generate all artefact types (fire in sequence; NLM queue is serial per notebook)
            study_guide_md = await self._generate_study_guide(client, nb_id)
            quiz_items = await self._generate_quiz(client, nb_id)
            flashcards_md = await self._generate_flashcards(client, nb_id)
            mind_map_json = await self._generate_mind_map(client, nb_id)
            audio_path = await self._generate_audio(client, nb_id)

            # If gap topics are provided, ask NLM focused questions and append to study guide
            if gap_topics:
                gap_text = await self._query_gaps(client, nb_id, gap_topics)
                study_guide_md += f"\n\n---\n## Gap Topic Supplement\n\n{gap_text}"

        concept_deps = self._extract_concepts_from_mind_map(mind_map_json)

        return {
            "study_guide_md": study_guide_md,
            "quiz_items": quiz_items,
            "flashcards_md": flashcards_md,
            "mind_map_json": mind_map_json,
            "audio_path": audio_path,
            "concept_deps": concept_deps,
        }

    # ── Private helpers ──────────────────────────────────────────────────────

    async def _get_or_create_notebook(self, client: Any, refresh: bool) -> str:
        """Return the notebook ID, creating if it doesn't exist. In refresh mode reuse."""
        notebooks = await client.notebooks.list()
        for nb in notebooks:
            if nb.title == self.nb_name:
                if refresh:
                    print(f"[NLM] Reusing existing notebook: {self.nb_name} (id={nb.id})")
                    return nb.id
                else:
                    # Delete and recreate for a clean build
                    print(f"[NLM] Deleting stale notebook: {self.nb_name}")
                    await client.notebooks.delete(nb.id)
                    break

        nb = await client.notebooks.create(self.nb_name)
        print(f"[NLM] Created notebook: {self.nb_name} (id={nb.id})")
        return nb.id

    async def _add_sources(self, client: Any, nb_id: str, sources: dict[str, Any]) -> None:
        urls: list[str] = sources.get("urls") or []
        files: list[str] = sources.get("files") or []
        youtube: list[str] = sources.get("youtube") or []

        all_urls = urls + youtube  # NLM handles YouTube URLs the same as web URLs
        for url in all_urls:
            if url:
                print(f"[NLM] Adding source URL: {url}")
                await client.sources.add_url(nb_id, url, wait=True)

        for file_path in files:
            if file_path:
                resolved = Path(file_path).resolve()
                if resolved.exists():
                    print(f"[NLM] Adding source file: {resolved.name}")
                    await client.sources.add_file(nb_id, str(resolved), wait=True)
                else:
                    print(f"[WARN] Source file not found, skipping: {file_path}", file=sys.stderr)

    async def _generate_study_guide(self, client: Any, nb_id: str) -> str:
        print("[NLM] Generating study guide...")
        status = await client.artifacts.generate_report(
            nb_id,
            report_type="study_guide",
        )
        await client.artifacts.wait_for_completion(nb_id, status.task_id)

        with tempfile.NamedTemporaryFile(suffix=".md", delete=False) as tmp:
            tmp_path = tmp.name
        await client.artifacts.download_report(nb_id, tmp_path)
        text = Path(tmp_path).read_text(encoding="utf-8")
        Path(tmp_path).unlink(missing_ok=True)
        print("[NLM] Study guide received.")
        return text

    async def _generate_quiz(self, client: Any, nb_id: str) -> list[dict]:
        print("[NLM] Generating quiz...")
        status = await client.artifacts.generate_quiz(nb_id, difficulty="medium")
        await client.artifacts.wait_for_completion(nb_id, status.task_id)

        with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as tmp:
            tmp_path = tmp.name
        await client.artifacts.download_quiz(nb_id, tmp_path, output_format="json")
        raw = Path(tmp_path).read_text(encoding="utf-8")
        Path(tmp_path).unlink(missing_ok=True)

        try:
            items = json.loads(raw)
        except json.JSONDecodeError:
            print("[WARN] Quiz JSON could not be parsed; returning empty list.", file=sys.stderr)
            items = []
        print(f"[NLM] Quiz received ({len(items)} items).")
        return items

    async def _generate_flashcards(self, client: Any, nb_id: str) -> str:
        print("[NLM] Generating flashcards...")
        status = await client.artifacts.generate_flashcards(nb_id)
        await client.artifacts.wait_for_completion(nb_id, status.task_id)

        with tempfile.NamedTemporaryFile(suffix=".md", delete=False) as tmp:
            tmp_path = tmp.name
        await client.artifacts.download_flashcards(nb_id, tmp_path, output_format="markdown")
        text = Path(tmp_path).read_text(encoding="utf-8")
        Path(tmp_path).unlink(missing_ok=True)
        print("[NLM] Flashcards received.")
        return text

    async def _generate_mind_map(self, client: Any, nb_id: str) -> dict:
        print("[NLM] Generating mind map...")
        result = await client.artifacts.generate_mind_map(nb_id)
        await client.artifacts.wait_for_completion(nb_id, result.task_id)

        with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as tmp:
            tmp_path = tmp.name
        await client.artifacts.download_mind_map(nb_id, tmp_path)
        raw = Path(tmp_path).read_text(encoding="utf-8")
        Path(tmp_path).unlink(missing_ok=True)

        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            print("[WARN] Mind map JSON could not be parsed; returning empty dict.", file=sys.stderr)
            data = {}
        print("[NLM] Mind map received.")
        return data

    async def _generate_audio(self, client: Any, nb_id: str) -> str | None:
        print("[NLM] Generating audio overview (this may take several minutes)...")
        try:
            status = await client.artifacts.generate_audio(
                nb_id,
                audio_type="deep-dive",
                instructions=f"Create a clear, engaging overview of {self.course_name} suitable for undergraduate students.",
            )
            await client.artifacts.wait_for_completion(nb_id, status.task_id)

            with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp:
                tmp_path = tmp.name
            await client.artifacts.download_audio(nb_id, tmp_path)
            print("[NLM] Audio overview downloaded.")
            return tmp_path
        except Exception as exc:  # noqa: BLE001
            print(f"[WARN] Audio generation failed (non-fatal): {exc}", file=sys.stderr)
            return None

    async def _query_gaps(self, client: Any, nb_id: str, gap_topics: list[str]) -> str:
        """Ask NLM targeted questions for each gap topic and return combined Markdown."""
        parts: list[str] = []
        for topic in gap_topics:
            print(f"[NLM] Querying gap topic: {topic}")
            result = await client.chat.ask(
                nb_id,
                f"Explain '{topic}' clearly for undergraduate students. Include a concrete example.",
            )
            parts.append(f"### {topic}\n\n{result.answer}")
        return "\n\n".join(parts)

    @staticmethod
    def _extract_concepts_from_mind_map(mind_map: dict) -> list[str]:
        """Flatten the mind map JSON into a list of concept names."""
        concepts: list[str] = []

        def _walk(node: Any) -> None:
            if isinstance(node, dict):
                label = node.get("label") or node.get("name") or node.get("title") or ""
                if label:
                    concepts.append(label)
                for child in node.get("children", []):
                    _walk(child)
            elif isinstance(node, list):
                for item in node:
                    _walk(item)

        _walk(mind_map)
        return concepts
