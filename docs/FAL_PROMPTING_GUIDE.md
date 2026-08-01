# fal.ai MiniMax H3 Prompting Guide / fal.ai 提示词指南摘要

Source / 来源: [MiniMax H3 Prompting Guide + 44 Video Examples](https://fal.ai/learn/devs/minimax-h3-prompting-guide), edited by Bennett Heyn, updated 2026-07-30.

This is a bilingual, independently written summary for the library. The source page contains 44 public H3 result videos and the prompts or prompt excerpts used for them. Five representative entries are currently structured in this repository as H3-0017 through H3-0021; the remaining examples are queued for review and translation.

这是本仓库独立整理的双语摘要。来源页面提供了 44 个公开 H3 结果视频，以及对应的完整 Prompt 或 Prompt 摘录。目前已将其中 5 个代表性案例结构化为 H3-0017 至 H3-0021，其余案例等待逐条核验与翻译。

## Endpoint selection / 模式选择

| Input / 输入 | Endpoint / 模式 | Best use / 适用场景 |
| --- | --- | --- |
| Prompt only / 只有文本 | Text to Video / 文生视频 | Inventing a complete look from text / 由文字自由创造完整视觉 |
| Opening frame, or opening + closing frame / 首帧或首尾帧 | First & Last Frame / 首尾帧 | Controlled motion between known compositions / 在确定构图间生成运动 |
| Any identity, style, motion, video or audio reference / 人物、风格、动作、视频或音频参考 | Reference to Video / 多模态参考生成 | Identity locking, motion transfer, voice, editing / 身份锁定、动作迁移、声音和视频编辑 |

The guide reports 5–15 second output, 24 FPS, 2K video, native stereo audio, prompts up to 7,000 characters, and up to 12 reference files: 9 images, 3 videos, and 3 audio clips within the overall limit.

该指南给出的能力范围为：5–15 秒、24 FPS、2K、原生立体声；Prompt 最长 7,000 字符；最多 12 个参考文件，其中可包含最多 9 张图片、3 段视频和 3 段音频。

## Eight high-leverage techniques / 八条高价值技巧

1. **Assign every reference a job.** State which asset controls identity, mood, product, camera, motion, audio, or ending.  
   **为每个参考素材分配职责。** 明确哪项素材负责身份、氛围、产品、摄影、动作、声音或结尾。
2. **Use a timed shot list.** Divide multi-beat clips into explicit second ranges.  
   **使用时间轴分镜。** 多节拍视频按秒拆分，避免节奏漂移或退化成幻灯片。
3. **Direct audio as carefully as picture.** Specify dialogue, ambience, instruments, rhythm, and cue timing.  
   **像导演画面一样导演声音。** 写清对白、环境声、乐器、节奏和声音落点。
4. **Write concrete negative constraints.** Name unwanted transitions, text errors, genre drift, or visual artifacts.  
   **写具体负面约束。** 明确禁止的转场、乱码、类型偏移和视觉瑕疵。
5. **Lock identity with observable details.** List the face, hair, wardrobe, materials, product features, or typography that must persist.  
   **用可观察细节锁定身份。** 列出必须保持的人脸、发型、服装、材质、产品特征或字体。
6. **Pair each edit with a preservation rule.** Say what changes and what must remain untouched.  
   **把每项修改与保持规则配对。** 同时说明改什么、哪些部分绝不能变化。
7. **Use real camera and film language.** Describe focal behavior, camera movement, exposure, grain, halation, and color response.  
   **使用真实摄影与胶片语言。** 描述焦点、运动、曝光、颗粒、光晕和色彩响应。
8. **Describe transitions as physical events.** Explain the movement, blur, exposure change, cut point, and settling behavior.  
   **把转场写成物理事件。** 说明运动、模糊、曝光变化、切点和稳定方式。

## Curation rule / 收录规则

- Preserve the source prompt and direct page URL.
- Mirror public result media for reliable playback and keep its original media URL.
- Mark whether the page provides the full prompt or only an excerpt.
- Add a Chinese translation without altering the English source text.
- Keep third-party media outside the repository's CC BY 4.0 license and honor removal requests.

- 保留原始 Prompt 和直接页面链接。
- 镜像公开结果视频以保证播放，同时保存原始媒体地址。
- 标明页面提供的是完整 Prompt 还是摘录。
- 添加中文翻译，但不改动英文来源文本。
- 第三方媒体不适用仓库 CC BY 4.0，并接受权利人删除申请。
