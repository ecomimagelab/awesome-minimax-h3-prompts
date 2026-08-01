from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
PROMPTS_DIR = ROOT / "data" / "prompts"
CATEGORIES_FILE = ROOT / "data" / "categories.json"

REQUIRED_TOP_LEVEL = {
    "id",
    "title",
    "description",
    "mode",
    "featured",
    "prompt",
    "parameters",
    "tags",
    "source",
    "verification",
}


def read_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def load_categories() -> dict[str, Any]:
    return read_json(CATEGORIES_FILE)


def load_prompts() -> list[dict[str, Any]]:
    prompts = [read_json(path) for path in sorted(PROMPTS_DIR.glob("*.json"))]
    return sorted(prompts, key=lambda item: item["id"])


def validate_prompt(item: dict[str, Any], allowed_modes: set[str]) -> list[str]:
    errors: list[str] = []
    item_id = item.get("id", "<missing-id>")

    missing = REQUIRED_TOP_LEVEL - item.keys()
    if missing:
        errors.append(f"{item_id}: missing fields: {', '.join(sorted(missing))}")

    if item.get("mode") not in allowed_modes:
        errors.append(f"{item_id}: unsupported mode: {item.get('mode')!r}")

    for field in ("title", "description"):
        value = item.get(field, {})
        if not isinstance(value, dict) or not value.get("en") or not value.get("zh"):
            errors.append(f"{item_id}: {field} must contain non-empty en and zh values")

    prompt = item.get("prompt", {})
    for field in ("original", "zh", "original_language"):
        if not isinstance(prompt, dict) or not prompt.get(field):
            errors.append(f"{item_id}: prompt.{field} is required")
    if isinstance(prompt, dict) and prompt.get("original_language") != "en" and not prompt.get("en"):
        errors.append(f"{item_id}: prompt.en is required when the original language is not English")

    source = item.get("source", {})
    source_url = source.get("url", "") if isinstance(source, dict) else ""
    if not source_url.startswith(("https://", "http://")):
        errors.append(f"{item_id}: source.url must be an HTTP(S) URL")
    for field in ("type", "author", "published_at", "retrieved_at"):
        if not isinstance(source, dict) or not source.get(field):
            errors.append(f"{item_id}: source.{field} is required")

    source_location = source.get("source_location") if isinstance(source, dict) else None
    if source_location is not None and source_location not in {"post", "reply", "comment", "page"}:
        errors.append(f"{item_id}: unsupported source.source_location: {source_location!r}")
    thread_url = source.get("thread_url", "") if isinstance(source, dict) else ""
    if thread_url and not thread_url.startswith(("https://", "http://")):
        errors.append(f"{item_id}: source.thread_url must be an HTTP(S) URL")

    verification = item.get("verification", {})
    for field in ("prompt_visible", "h3_confirmed", "output_visible", "notes"):
        if not isinstance(verification, dict) or field not in verification:
            errors.append(f"{item_id}: verification.{field} is required")

    if not isinstance(item.get("tags"), list) or not item.get("tags"):
        errors.append(f"{item_id}: tags must be a non-empty list")

    for index, media in enumerate(item.get("media", [])):
        if media.get("type") not in {"video", "image", "audio"}:
            errors.append(f"{item_id}: media[{index}].type is unsupported")
        if not media.get("path"):
            errors.append(f"{item_id}: media[{index}].path is required")
        elif media["path"].startswith(("http://", "https://")):
            errors.append(f"{item_id}: media[{index}].path must be a repository-relative path")
        if not media.get("source_url", "").startswith(("https://", "http://")):
            errors.append(f"{item_id}: media[{index}].source_url must be an HTTP(S) URL")
        if media.get("playback_url") and not media["playback_url"].startswith(("https://", "http://")):
            errors.append(f"{item_id}: media[{index}].playback_url must be an HTTP(S) URL")

    return errors
