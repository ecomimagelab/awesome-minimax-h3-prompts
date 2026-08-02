#!/usr/bin/env python3
"""Give MiniMax attribution precedence for known fal/official overlaps.

The allowlist is intentionally explicit. fal-only examples are not changed.
Media files are renamed as well so generated GitHub and Pages links do not
present the republisher as the source of an official example.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROMPT_DIR = ROOT / "data" / "prompts"
MEDIA_DIR = ROOT / "media"
OFFICIAL_URL = "https://www.minimax.io/blog/minimax-h3"
OFFICIAL_IDS = {"h3-0017"} | {f"h3-{number:04d}" for number in range(22, 56)}


def main() -> int:
    renamed: dict[str, str] = {}
    changed = 0

    for path in sorted(PROMPT_DIR.glob("h3-*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        if record.get("id") not in OFFICIAL_IDS:
            continue

        tags = [tag for tag in record.get("tags", []) if tag not in {"fal-guide", "community-tested"}]
        if "official" not in tags:
            tags.append("official")
        record["tags"] = tags

        for media in record.get("media", []):
            old_rel = media.get("path", "")
            old_name = Path(old_rel).name
            if old_name.startswith("fal-"):
                new_name = "minimax-official-" + old_name.removeprefix("fal-")
                media["path"] = f"media/{new_name}"
                renamed[old_name] = new_name
            media["source_url"] = OFFICIAL_URL

        record["source"] = {
            "type": "official",
            "author": "MiniMax",
            "url": OFFICIAL_URL,
            "source_location": "page",
            "published_at": "2026-07-31",
            "retrieved_at": record.get("source", {}).get("retrieved_at", "2026-08-01"),
        }
        record.setdefault("verification", {})["notes"] = (
            "Matched to the same prompt and result video in MiniMax's official H3 materials."
        )
        path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        changed += 1

    for old_name, new_name in sorted(renamed.items()):
        old_path = MEDIA_DIR / old_name
        new_path = MEDIA_DIR / new_name
        if new_path.exists():
            if old_path.exists() and old_path.resolve() != new_path.resolve():
                raise FileExistsError(f"Refusing to overwrite {new_path}")
            continue
        if not old_path.exists():
            raise FileNotFoundError(old_path)
        old_path.rename(new_path)

    print(f"Reattributed {changed} records and renamed {len(renamed)} media files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
