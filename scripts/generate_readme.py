from __future__ import annotations

from collections import Counter
from library import ROOT, load_categories, load_prompts

LANG_CONFIG = {
    "en": {
        "file": "README.md",
        "title": "Awesome MiniMax H3 Prompts",
        "tagline": "A curated bilingual library of public prompts, examples, and prompting patterns for MiniMax H3.",
        "switch": "[简体中文](README_zh.md) · **English**",
        "about": "About MiniMax H3",
        "about_text": "MiniMax H3 is a multimodal video generation model that accepts text, images, video, and audio as context. This repository separates official examples, community-tested prompts, and unverified guide templates so readers can judge the evidence behind every entry.",
        "notice": "Copyright and verification notice",
        "notice_text": "Public availability does not remove an author's rights. Publicly accessible media may be mirrored for research, discovery, and click-to-play viewing; every entry preserves attribution, the original URL, and retrieval metadata. Mirrored third-party material is excluded from this repository's CC BY 4.0 license and can be removed through the rights-holder request form. `H3 confirmed: No` means the source did not show a verifiable H3 result.",
        "stats": "Library statistics",
        "browse": "Browse by mode",
        "featured": "Featured prompts",
        "all": "All prompts",
        "prompt": "Prompt",
        "translation": "Chinese translation",
        "description": "Description",
        "details": "Details",
        "source": "Source",
        "source_type": "Source type",
        "published": "Published",
        "retrieved": "Retrieved",
        "thread": "Parent thread",
        "source_location": "Source location",
        "parameters": "Parameters",
        "verification": "Verification",
        "video": "Video",
        "play_video": "Play the original video",
        "yes": "Yes",
        "no": "No",
        "prompt_visible": "Prompt visible",
        "h3_confirmed": "H3 confirmed",
        "output_visible": "Output visible",
        "contribute": "Contributing",
        "contribute_text": "Submit a prompt through the issue form or a pull request. Include the original author, direct source URL, exact prompt, generation mode, and whether a visible output confirms MiniMax H3. See [CONTRIBUTING.md](docs/CONTRIBUTING.md).",
        "license": "License and removals",
        "license_text": "Original repository content is available under [CC BY 4.0](LICENSE). Third-party prompts and media retain their original rights; see [NOTICE.md](NOTICE.md). Rights holders may open a removal request.",
    },
    "zh": {
        "file": "README_zh.md",
        "title": "Awesome MiniMax H3 提示词",
        "tagline": "收录 MiniMax H3 公开提示词、生成案例和提示词方法的中英双语资源库。",
        "switch": "**简体中文** · [English](README.md)",
        "about": "关于 MiniMax H3",
        "about_text": "MiniMax H3 是可将文本、图片、视频和音频作为统一上下文的视频生成模型。本仓库严格区分官方示例、社区实测 Prompt 和尚未展示 H3 结果的公开教程模板，方便读者判断每条内容的证据强度。",
        "notice": "版权与核验说明",
        "notice_text": "内容公开可见不代表作者放弃权利。公开可访问的媒体可能会为研究、发现与点击播放而镜像保存；每条内容均保留作者署名、原始链接和抓取信息。镜像的第三方内容不适用本仓库的 CC BY 4.0，权利人可通过删除申请表要求下架。`H3 已确认：否` 表示来源没有展示可核验的 H3 结果。",
        "stats": "收录统计",
        "browse": "按生成模式浏览",
        "featured": "精选提示词",
        "all": "全部提示词",
        "prompt": "原始 Prompt",
        "translation": "中文翻译",
        "description": "内容说明",
        "details": "详细信息",
        "source": "来源",
        "source_type": "来源类型",
        "published": "发布时间",
        "retrieved": "收录时间",
        "thread": "所属主帖",
        "source_location": "来源位置",
        "parameters": "生成参数",
        "verification": "核验状态",
        "video": "案例视频",
        "play_video": "点击播放原视频",
        "yes": "是",
        "no": "否",
        "prompt_visible": "Prompt 可见",
        "h3_confirmed": "H3 已确认",
        "output_visible": "结果可见",
        "contribute": "参与贡献",
        "contribute_text": "可通过 Issue 表单或 Pull Request 投稿。请提供原作者、直接来源链接、完整 Prompt、生成模式，以及是否存在可确认由 MiniMax H3 生成的公开结果。详情见 [CONTRIBUTING.md](docs/CONTRIBUTING.md)。",
        "license": "许可证与删除请求",
        "license_text": "仓库原创内容采用 [CC BY 4.0](LICENSE)；第三方 Prompt 与媒体仍归原权利人所有，详见 [NOTICE.md](NOTICE.md)。权利人可提交删除请求。",
    },
}


def bool_text(value: bool, text: dict[str, str]) -> str:
    return f"✅ {text['yes']}" if value else f"⚪ {text['no']}"


def anchor(value: str) -> str:
    return value.lower().replace(" / ", "-").replace(" ", "-")


def render_video(media: dict, text: dict[str, str]) -> list[str]:
    playback_url = media.get("playback_url")
    if playback_url:
        return ["", f"#### {text['video']}", "", playback_url, "", f"[↗ {text['play_video']}]({playback_url})"]
    return ["", f"#### {text['video']}", "", f"[▶ {text['play_video']}]({media['path']})"]


def render_card(
    item: dict,
    lang: str,
    categories: dict,
    text: dict[str, str],
    *,
    include_media: bool = True,
) -> str:
    title = item["title"][lang]
    description = item["description"][lang]
    prompt = item["prompt"]
    source = item["source"]
    verification = item["verification"]
    mode = categories["modes"][item["mode"]][lang]
    source_type = categories["source_types"][source["type"]][lang]
    params = " · ".join(f"`{key}: {value}`" for key, value in item["parameters"].items())
    tags = " ".join(f"`{tag}`" for tag in item["tags"])

    lines = [
        f'<a id="{item["id"]}"></a>',
        "",
        f"### {item['id'].upper()} · {title}",
        "",
        f"**{mode}** · **{source_type}**{' · ⭐ Featured' if item['featured'] else ''}",
        "",
        f"#### {text['description']}",
        "",
        description,
        "",
        f"#### {text['prompt']}",
        "",
        "```text",
        prompt["original"],
        "```",
    ]
    if lang == "zh" and prompt["zh"].strip() != prompt["original"].strip():
        lines.extend(["", f"#### {text['translation']}", "", "```text", prompt["zh"], "```"])

    if include_media:
        for media in item.get("media", []):
            if media.get("type") == "video" and media.get("path"):
                lines.extend(render_video(media, text))

    lines.extend(
        [
            "",
            f"#### {text['details']}",
            "",
            f"- **{text['parameters']}：** {params}",
            f"- **Tags：** {tags}",
            f"- **{text['source_type']}：** {source_type}",
            f"- **{text['source']}：** [{source['author']}]({source['url']})",
            *([f"- **{text['thread']}：** [X thread]({source['thread_url']})"] if source.get("thread_url") else []),
            *([f"- **{text['source_location']}：** `{source['source_location']}`"] if source.get("source_location") else []),
            f"- **{text['published']}：** {source['published_at']}",
            f"- **{text['retrieved']}：** {source['retrieved_at']}",
            f"- **{text['verification']}：** {text['prompt_visible']} {bool_text(verification['prompt_visible'], text)} · {text['h3_confirmed']} {bool_text(verification['h3_confirmed'], text)} · {text['output_visible']} {bool_text(verification['output_visible'], text)}",
            f"- **Note：** {verification['notes']}",
            "",
            "---",
        ]
    )
    return "\n".join(lines)


def shared_video_groups(prompts: list[dict]) -> list[list[dict]]:
    by_path: dict[str, list[dict]] = {}
    for item in prompts:
        for media in item.get("media", []):
            if media.get("type") == "video" and media.get("path"):
                by_path.setdefault(media["path"], []).append(item)
                break
    return [items for items in by_path.values() if len(items) > 1]


def render_video_collection(
    items: list[dict], lang: str, categories: dict, text: dict[str, str]
) -> str:
    first = items[0]
    last = items[-1]
    video = next(media for media in first["media"] if media.get("type") == "video")
    id_range = f"{first['id'].upper()}–{last['id'].upper()}"
    if lang == "zh":
        title = f"{id_range} · 一个原视频中的 {len(items)} 段提示词"
        note = "来源将这些案例发布在同一个合集视频中。视频只展示一次，对应的完整提示词依次列在下方。"
    else:
        title = f"{id_range} · {len(items)} prompts in one source video"
        note = "The source presents these examples in a single compilation video. The video is shown once, followed by the complete prompt blocks below."

    lines = [f"### {title}", "", note]
    lines.extend(render_video(video, text))
    lines.extend(["", "---", ""])
    for item in items:
        lines.extend([render_card(item, lang, categories, text, include_media=False), ""])
    return "\n".join(lines)


def generate(lang: str, prompts: list[dict], categories: dict) -> str:
    text = LANG_CONFIG[lang]
    source_counts = Counter(item["source"]["type"] for item in prompts)
    mode_counts = Counter(item["mode"] for item in prompts)
    latest = max(item["source"]["retrieved_at"] for item in prompts)
    video_groups = shared_video_groups(prompts)
    grouped_ids = {item["id"] for group in video_groups for item in group}

    lines = [
        '<p align="center"><img src="public/cover.svg" alt="Awesome MiniMax H3 Prompts" width="100%"></p>',
        "",
        f"# {text['title']}",
        "",
        "[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)",
        "[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](LICENSE)",
        "[![Validate data](https://github.com/ecomimagelab/awesome-minimax-h3-prompts/actions/workflows/validate.yml/badge.svg)](https://github.com/ecomimagelab/awesome-minimax-h3-prompts/actions/workflows/validate.yml)",
        "",
        f"> {text['tagline']}",
        "",
        f"{text['switch']}",
        "",
        f"## {text['about']}",
        "",
        text["about_text"],
        "",
        "- Official model: `MiniMax-H3`",
        "- Output: up to 2K, 4–15 seconds",
        "- Inputs: text, image, video, and audio references",
        "- Official guide: [MiniMax H3 Video Generation](https://platform.minimax.io/docs/guides/video-generation)",
        "- Community prompting guide: [fal.ai H3 guide — bilingual notes](docs/FAL_PROMPTING_GUIDE.md)",
        "",
        f"> [!IMPORTANT]\n> **{text['notice']}：** {text['notice_text']}",
        "",
        f"## {text['stats']}",
        "",
        "| Metric | Count |",
        "| --- | ---: |",
        f"| Total prompts | **{len(prompts)}** |",
        f"| Official examples | **{source_counts['official']}** |",
        f"| Community tested | **{source_counts['community-tested']}** |",
        f"| Community guide templates | **{source_counts['community-guide']}** |",
        f"| Last curated | **{latest}** |",
        "",
        f"## {text['browse']}",
        "",
    ]

    for mode_key, label in categories["modes"].items():
        mode_label = label[lang]
        lines.append(f"- [{mode_label} ({mode_counts[mode_key]})](#{anchor(mode_label)})")

    featured = [item for item in prompts if item["featured"]]
    lines.extend(["", f"## {text['featured']}", ""])
    for item in featured:
        source_type = categories["source_types"][item["source"]["type"]][lang]
        lines.append(f"- [{item['title'][lang]}](#{item['id']}) — {source_type}")

    if video_groups:
        collection_heading = "合集视频与多段提示词" if lang == "zh" else "Compilation videos with multiple prompts"
        lines.extend(["", f"## {collection_heading}", ""])
        for group in video_groups:
            lines.extend([render_video_collection(group, lang, categories, text), ""])

    lines.extend(["", f"## {text['all']}", ""])
    for mode_key, mode_label in categories["modes"].items():
        lines.extend([f"## {mode_label[lang]}", ""])
        grouped_entries = [item for item in prompts if item["mode"] == mode_key and item["id"] in grouped_ids]
        entries = [item for item in prompts if item["mode"] == mode_key and item["id"] not in grouped_ids]
        if grouped_entries:
            label = "上方合集中的相关提示词" if lang == "zh" else "Related prompts in the compilation above"
            links = " · ".join(f"[{item['id'].upper()}](#{item['id']})" for item in grouped_entries)
            lines.extend([f"*{label}:* {links}", ""])
        if not entries and not grouped_entries:
            lines.extend(["_Coming soon._", ""])
            continue
        for item in entries:
            lines.extend([render_card(item, lang, categories, text), ""])

    lines.extend(
        [
            f"## {text['contribute']}",
            "",
            text["contribute_text"],
            "",
            f"## {text['license']}",
            "",
            text["license_text"],
            "",
            "---",
            "",
            "MiniMax and Hailuo are trademarks of their respective owners. This community project is not affiliated with or endorsed by MiniMax.",
            "",
            f"Generated from structured data curated through {latest}.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    prompts = load_prompts()
    categories = load_categories()
    for lang, config in LANG_CONFIG.items():
        output = ROOT / config["file"]
        output.write_text(generate(lang, prompts, categories), encoding="utf-8", newline="\n")
        print(f"Wrote {output.relative_to(ROOT)} with {len(prompts)} prompts")


if __name__ == "__main__":
    main()
