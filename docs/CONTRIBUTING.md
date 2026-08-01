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
- A downloadable public result video that can be mirrored into this repository under `media/`.
- Publication date, if available.

If the public source contains a result video but no prompt, maintainers may reconstruct a prompt from observable visual, motion, camera, timing, and audio evidence. A reconstructed prompt must set `prompt.reconstructed_from_video` to `true`, include bilingual `prompt.reconstruction_notes`, and keep `verification.prompt_visible` as `false`. It must never be presented as the creator's original wording.

For X threads, inspect the main post plus consecutive author replies. If the prompt is in a reply or comment, use that reply as `source.url`, add the main post as `source.thread_url`, and set `source.source_location` to `reply` or `comment`.

每次投稿必须提供：

- 作者公开发布的完整原始 Prompt。
- 直接来源链接，不能只提供个人主页或搜索结果。
- 原作者名称或账号。
- 生成模式：文生视频、图生视频、首尾帧或多模态参考生成。
- 来源是否明确说明使用 MiniMax H3。
- 来源是否展示生成结果。
- 可公开下载并镜像保存到本仓库 `media/` 目录的结果视频。
- 可获取时提供发布时间。

如果公开来源只有结果视频、没有 Prompt，维护者可以根据可观察到的画面、动作、镜头、时间和音频信息反推 Prompt。反推内容必须将 `prompt.reconstructed_from_video` 设为 `true`，提供中英文 `prompt.reconstruction_notes`，并将 `verification.prompt_visible` 保持为 `false`；不得将其表述为创作者原文。

对于 X 线程，请同时检查主帖和作者连续回复。如果 Prompt 位于回复或评论中，应将该回复设为 `source.url`，将主帖设为 `source.thread_url`，并把 `source.source_location` 标记为 `reply` 或 `comment`。

## Review rules / 审核规则

- Do not submit private, paywalled, leaked, or deleted content.
- No video, no entry: prompts without a downloadable public result video are not accepted.
- Every accepted video must be downloaded and committed under `media/`; external playback URLs alone are not accepted.
- Reconstructed prompts must stay within observable evidence. Do not invent hidden reference assets, model parameters, exact dialogue, or production details that the video cannot support.
- Do not claim a result is H3-generated without a public statement or visible model label.
- AI-written translations are allowed, but the original prompt must remain unchanged.
- Publicly accessible third-party media may be mirrored for click-to-play viewing only when attribution, the original URL, retrieval metadata, and removal-request path are preserved. Do not collect private, paywalled, leaked, or deleted media.
- Maintainers may edit metadata and translations for clarity while preserving the source prompt.

- 不收录没有公开可下载结果视频的 Prompt。
- 每个保留条目都必须把视频下载并提交到 `media/`；不能只保存外部播放链接。
- 视频反推 Prompt 只能描述可观察证据，不得编造隐藏参考素材、模型参数、精确台词或视频无法证明的制作信息。

## Local validation / 本地校验

```bash
python scripts/validate_data.py
python scripts/generate_readme.py
```

Commit both the structured data and regenerated README files.
