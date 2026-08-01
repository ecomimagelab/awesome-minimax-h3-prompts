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
        "notice_text": "Public availability does not remove an author's rights. Every entry preserves attribution and a direct source link. `H3 confirmed: No` means the prompt was published for H3 but the source did not show a verifiable H3 result. Third-party media is linked rather than copied.",
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
        "parameters": "Parameters",
        "verification": "Verification",
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
        "notice_text": "内容公开可见不代表作者放弃权利。每条收录均保留作者署名和直接来源链接。`H3 已确认：否` 表示该 Prompt 虽面向 H3 发布，但来源页面没有展示可核验的 H3 结果。第三方媒体默认仅链接、不搬运。",
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
        "parameters": "生成参数",
        "verification": "核验状态",
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


def render_card(item: dict, lang: str, categories: dict, text: dict[str, str]) -> str:
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

    lines.extend(
        [
            "",
            f"#### {text['details']}",
            "",
            f"- **{text['parameters']}：** {params}",
            f"- **Tags：** {tags}",
            f"- **{text['source_type']}：** {source_type}",
            f"- **{text['source']}：** [{source['author']}]({source['url']})",
            f"- **{text['published']}：** {source['published_at']}",
            f"- **{text['retrieved']}：** {source['retrieved_at']}",
            f"- **{text['verification']}：** {text['prompt_visible']} {bool_text(verification['prompt_visible'], text)} · {text['h3_confirmed']} {bool_text(verification['h3_confirmed'], text)} · {text['output_visible']} {bool_text(verification['output_visible'], text)}",
            f"- **Note：** {verification['notes']}",
            "",
            "---",
        ]
    )
    return "\n".join(lines)


def generate(lang: str, prompts: list[dict], categories: dict) -> str:
    text = LANG_CONFIG[lang]
    source_counts = Counter(item["source"]["type"] for item in prompts)
    mode_counts = Counter(item["mode"] for item in prompts)
    latest = max(item["source"]["retrieved_at"] for item in prompts)

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

    lines.extend(["", f"## {text['all']}", ""])
    for mode_key, mode_label in categories["modes"].items():
        lines.extend([f"## {mode_label[lang]}", ""])
        entries = [item for item in prompts if item["mode"] == mode_key]
        if not entries:
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
