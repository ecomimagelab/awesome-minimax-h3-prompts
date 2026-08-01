from __future__ import annotations

import sys

from library import load_categories, load_prompts, validate_prompt


def main() -> int:
    categories = load_categories()
    prompts = load_prompts()
    allowed_modes = set(categories["modes"])

    errors: list[str] = []
    seen_ids: set[str] = set()
    seen_originals: dict[str, str] = {}

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

    if errors:
        print("Data validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validated {len(prompts)} prompts across {len(allowed_modes)} modes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

