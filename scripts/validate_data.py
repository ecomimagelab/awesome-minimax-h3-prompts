from __future__ import annotations

import hashlib
import sys
from pathlib import Path

from library import ROOT, load_categories, load_prompts, validate_prompt


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    categories = load_categories()
    prompts = load_prompts()
    allowed_modes = set(categories["modes"])

    errors: list[str] = []
    seen_ids: set[str] = set()
    seen_originals: dict[str, str] = {}
    media_paths: set[str] = set()

    for item in prompts:
        errors.extend(validate_prompt(item, allowed_modes))
        item_id = item.get("id", "<missing-id>")

        if item_id in seen_ids:
            errors.append(f"{item_id}: duplicate id")
        seen_ids.add(item_id)

        original = item.get("prompt", {}).get("original", "").strip().casefold()
        if original in seen_originals:
            errors.append(f"{item_id}: duplicate prompt text (also in {seen_originals[original]})")
        elif original:
            seen_originals[original] = item_id

        for media in item.get("media", []):
            if media.get("type") == "video" and media.get("path"):
                media_paths.add(media["path"])

    seen_media_hashes: dict[str, str] = {}
    for relative_path in sorted(media_paths):
        local_path = ROOT / relative_path
        if not local_path.is_file():
            continue
        digest = sha256(local_path)
        if digest in seen_media_hashes:
            errors.append(
                f"duplicate video bytes: {relative_path} is identical to {seen_media_hashes[digest]}; "
                "reuse one media path and group the prompts beneath it"
            )
        else:
            seen_media_hashes[digest] = relative_path

    if errors:
        print("Data validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validated {len(prompts)} prompts across {len(allowed_modes)} modes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
