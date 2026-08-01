# Contributing / 参与贡献

Thank you for helping build a trustworthy MiniMax H3 prompt library.

感谢你帮助我们建立一个可信、可追溯的 MiniMax H3 提示词库。

## Required information / 必填信息

Every submission must include:

- Exact prompt text as published by the author.
- Direct source URL—not a profile page or search result.
- Original author name or handle.
- Generation mode: text-to-video, image-to-video, first/last frame, or reference generation.
- Whether the public source explicitly confirms MiniMax H3.
- Whether a generated result is visible at the source.
- Publication date, if available.

每次投稿必须提供：

- 作者公开发布的完整原始 Prompt。
- 直接来源链接，不能只提供个人主页或搜索结果。
- 原作者名称或账号。
- 生成模式：文生视频、图生视频、首尾帧或多模态参考生成。
- 来源是否明确说明使用 MiniMax H3。
- 来源是否展示生成结果。
- 可获取时提供发布时间。

## Review rules / 审核规则

- Do not submit private, paywalled, leaked, or deleted content.
- Do not claim a result is H3-generated without a public statement or visible model label.
- AI-written translations are allowed, but the original prompt must remain unchanged.
- Do not upload third-party videos or images without permission; link to the original source.
- Maintainers may edit metadata and translations for clarity while preserving the source prompt.

## Local validation / 本地校验

```bash
python scripts/validate_data.py
python scripts/generate_readme.py
```

Commit both the structured data and regenerated README files.

