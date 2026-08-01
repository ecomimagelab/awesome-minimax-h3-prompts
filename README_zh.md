<p align="center"><img src="public/cover.svg" alt="Awesome MiniMax H3 Prompts" width="100%"></p>

# Awesome MiniMax H3 提示词

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](LICENSE)
[![Validate data](https://github.com/ecomimagelab/awesome-minimax-h3-prompts/actions/workflows/validate.yml/badge.svg)](https://github.com/ecomimagelab/awesome-minimax-h3-prompts/actions/workflows/validate.yml)

> 收录 MiniMax H3 公开提示词、生成案例和提示词方法的中英双语资源库。

**简体中文** · [English](README.md)

## 关于 MiniMax H3

MiniMax H3 是可将文本、图片、视频和音频作为统一上下文的视频生成模型。本仓库严格区分官方示例、社区实测 Prompt 和尚未展示 H3 结果的公开教程模板，方便读者判断每条内容的证据强度。

- Official model: `MiniMax-H3`
- Output: up to 2K, 4–15 seconds
- Inputs: text, image, video, and audio references
- Official guide: [MiniMax H3 Video Generation](https://platform.minimax.io/docs/guides/video-generation)

> [!IMPORTANT]
> **版权与核验说明：** 内容公开可见不代表作者放弃权利。每条收录均保留作者署名和直接来源链接。`H3 已确认：否` 表示该 Prompt 虽面向 H3 发布，但来源页面没有展示可核验的 H3 结果。第三方媒体默认仅链接、不搬运。

## 收录统计

| Metric | Count |
| --- | ---: |
| Total prompts | **11** |
| Official examples | **5** |
| Community tested | **2** |
| Community guide templates | **4** |
| Last curated | **2026-08-01** |

## 按生成模式浏览

- [文生视频 (7)](#文生视频)
- [图生视频 (1)](#图生视频)
- [首尾帧生视频 (1)](#首尾帧生视频)
- [多模态参考生成 (2)](#多模态参考生成)

## 精选提示词

- [无人机上的 TikTok 舞者](#h3-0001) — 官方示例
- [从首帧生成现代舞](#h3-0002) — 官方示例
- [小女孩成长转场](#h3-0003) — 官方示例
- [复古贝雷帽时尚漫步](#h3-0004) — 官方示例
- [希区柯克运镜与参考歌声](#h3-0005) — 官方示例
- [Frutiger Aero 商场第一人称漫步](#h3-0007) — 社区实测

## 全部提示词

## 文生视频

<a id="h3-0001"></a>

### H3-0001 · 无人机上的 TikTok 舞者

**文生视频** · **官方示例** · ⭐ Featured

#### 内容说明

MiniMax 官方文生视频 API 示例，重点测试高难度动作表现。

#### 原始 Prompt

```text
A tiktok dancer is dancing on a drone, doing flips and tricks.
```

#### 中文翻译

```text
一名 TikTok 舞者站在无人机上跳舞，完成空翻和各种特技动作。
```

#### 详细信息

- **生成参数：** `duration: 5s` · `resolution: 2K` · `ratio: 16:9`
- **Tags：** `action` `dance` `aerial` `official`
- **来源类型：** 官方示例
- **来源：** [MiniMax](https://platform.minimax.io/docs/guides/video-generation)
- **发布时间：** 2026-07-31
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** Published in the official MiniMax H3 API guide.

---

<a id="h3-0006"></a>

### H3-0006 · 公园里雀跃的松狮犬

**文生视频** · **社区实测**

#### 内容说明

社区 H3 文生视频实测，使用两段连续的动物动作。

#### 原始 Prompt

```text
an adorable adult chow chow dog prancing in a park at daytime, the dog then sits down and yawns cutely, looking around.
```

#### 中文翻译

```text
白天，一只可爱的成年松狮犬在公园里欢快地跳跃。随后它坐下来，可爱地打了个哈欠，并四处张望。
```

#### 详细信息

- **生成参数：** `duration: not stated` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `animal` `park` `action-sequence` `community-tested`
- **来源类型：** 社区实测
- **来源：** [Neggy5](https://www.reddit.com/r/StableDiffusion/comments/1vc8o4u/used_my_last_hour_of_my_veniceai_sub_to_test/)
- **发布时间：** 2026-08-01
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** The author states the shown clips were generated with MiniMax H3.

---

<a id="h3-0007"></a>

### H3-0007 · Frutiger Aero 商场第一人称漫步

**文生视频** · **社区实测** · ⭐ Featured

#### 内容说明

社区 H3 第一人称环境实测，采用 Frutiger Aero 复古未来主义风格。

#### 原始 Prompt

```text
a first-person view walk through a busy ultramodern shopping mall with frutiger aero aesthetic at dusk. lots of pretty trees and foliage, beautiful organic architecture, lighting
```

#### 中文翻译

```text
黄昏时分，以第一人称视角穿行于一座繁忙的超现代购物中心，整体采用 Frutiger Aero 美学。周围有大量漂亮的树木与绿植、优美的有机建筑形态和富有氛围感的灯光。
```

#### 详细信息

- **生成参数：** `duration: not stated` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `first-person` `architecture` `frutiger-aero` `community-tested`
- **来源类型：** 社区实测
- **来源：** [Neggy5](https://www.reddit.com/r/StableDiffusion/comments/1vc8o4u/used_my_last_hour_of_my_veniceai_sub_to_test/)
- **发布时间：** 2026-08-01
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** The author states the shown clips were generated with MiniMax H3.

---

<a id="h3-0008"></a>

### H3-0008 · 穿越沙漠山脊的旅人

**文生视频** · **公开教程模板**

#### 内容说明

公开的 H3 电影感模板，包含主体运动、环境反馈、运镜路径和结束状态。

#### 原始 Prompt

```text
Wide cinematic shot of a lone traveler crossing a windswept desert at sunset. He leans forward against the wind while his coat and scarf stream naturally behind him; fine sand curls around his boots with each step. The camera performs a slow lateral tracking move at waist height, maintaining his profile. Warm backlight, long shadows, restrained teal-and-orange grade. One continuous shot ending as he stops on the ridge and sees a distant city.
```

#### 中文翻译

```text
电影感广角镜头：日落时分，一名孤独的旅人穿越狂风席卷的沙漠。他迎风前倾，外套和围巾自然地向身后飘动；每走一步，细沙都在靴子周围卷起。镜头保持腰部高度，缓慢横向跟拍并维持人物侧面。温暖逆光、长阴影、克制的青橙色调。全程一个连续镜头，以旅人在山脊停下、看见远方城市结束。
```

#### 详细信息

- **生成参数：** `duration: not stated` · `resolution: not stated` · `ratio: landscape`
- **Tags：** `cinematic` `desert` `tracking-shot` `community-guide`
- **来源类型：** 公开教程模板
- **来源：** [VideoToPrompt](https://www.videotoprompt.app/posts/hailuo-h3-prompt-guide)
- **发布时间：** 2026-07-21
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ⚪ 否 · 结果可见 ⚪ 否
- **Note：** Published as an H3 prompt template; no generated H3 output is shown beside the prompt.

---

<a id="h3-0009"></a>

### H3-0009 · 高端柑橘饮料广告

**文生视频** · **公开教程模板**

#### 内容说明

公开产品广告模板，重点控制液体物理、标签稳定性与环绕运镜。

#### 原始 Prompt

```text
Macro product shot of a chilled citrus drink can standing upright on black stone. A thin stream of water strikes the surface beside it, producing a controlled splash that wraps around the base while condensation beads slide down the aluminum. The camera makes a slow 30-degree clockwise orbit, keeping the logo sharp and facing forward. Crisp studio rim lighting, dark premium commercial style. End with the splash settled and the can centered.
```

#### 中文翻译

```text
微距产品镜头：一罐冰镇柑橘饮料直立在黑色石材上。一股细水流击中罐体旁的台面，形成受控水花并环绕罐底，冷凝水珠沿铝罐表面滑落。镜头缓慢顺时针环绕 30 度，保持商标清晰且始终朝向镜头。清晰的棚拍轮廓光，深色高端商业风格。以水花平息、饮料罐居中结束。
```

#### 详细信息

- **生成参数：** `duration: not stated` · `resolution: not stated` · `ratio: landscape`
- **Tags：** `product` `advertising` `water-physics` `orbit` `community-guide`
- **来源类型：** 公开教程模板
- **来源：** [VideoToPrompt](https://www.videotoprompt.app/posts/hailuo-h3-prompt-guide)
- **发布时间：** 2026-07-21
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ⚪ 否 · 结果可见 ⚪ 否
- **Note：** Published as an H3 prompt template; no generated H3 output is shown beside the prompt.

---

<a id="h3-0010"></a>

### H3-0010 · 手持吸尘器博主测评

**文生视频** · **公开教程模板**

#### 内容说明

公开竖屏 UGC 模板，明确规定双手动作、产品交互与自然表情。

#### 原始 Prompt

```text
Vertical smartphone video of a woman in a bright apartment demonstrating a compact handheld vacuum. She looks into the lens, raises the product with her right hand, points to its nozzle with her left index finger, then bends slightly and cleans crumbs from the sofa in one smooth pass. Natural blinking and conversational expression. Light handheld camera movement, soft window light, authentic creator-review style, no cuts.
```

#### 中文翻译

```text
竖屏手机视频：一名女子在明亮的公寓里演示小型手持吸尘器。她看向镜头，用右手举起产品，用左手食指指向吸嘴；随后稍微弯腰，以一次流畅动作吸走沙发上的碎屑。自然眨眼，呈现交谈时的表情。轻微手持运镜、柔和窗光、真实博主测评风格，不剪切。
```

#### 详细信息

- **生成参数：** `duration: not stated` · `resolution: not stated` · `ratio: 9:16`
- **Tags：** `ugc` `product-demo` `vertical-video` `community-guide`
- **来源类型：** 公开教程模板
- **来源：** [VideoToPrompt](https://www.videotoprompt.app/posts/hailuo-h3-prompt-guide)
- **发布时间：** 2026-07-21
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ⚪ 否 · 结果可见 ⚪ 否
- **Note：** Published as an H3 prompt template; no generated H3 output is shown beside the prompt.

---

<a id="h3-0011"></a>

### H3-0011 · 雨夜屋顶女剑士

**文生视频** · **公开教程模板**

#### 内容说明

公开动画动作模板，使用按时间展开的动作链和横向平行跟拍。

#### 原始 Prompt

```text
Anime-style medium-wide shot of a teenage swordswoman sprinting across rain-soaked rooftops at night. Her feet push off each tile in sequence, loose roof fragments slide behind her, and her coat follows the direction of motion. The camera tracks parallel at full-body distance, then gradually moves ahead as she leaps across a narrow alley. Bold linework, dramatic blue moonlight, rain streaks, controlled motion blur. She lands in a balanced crouch.
```

#### 中文翻译

```text
动画风格中广角镜头：夜晚，一名少女剑士在被雨水浸透的屋顶上疾跑。她的双脚依次蹬过每块瓦片，松动的瓦片碎片从身后滑落，外套顺着运动方向飘动。镜头以全身距离平行跟拍，当她跃过狭窄巷道时逐渐移到前方。粗犷有力的线条、戏剧性的蓝色月光、雨丝和受控运动模糊。她最终以平衡的蹲姿落地。
```

#### 详细信息

- **生成参数：** `duration: not stated` · `resolution: not stated` · `ratio: landscape`
- **Tags：** `anime` `action` `rain` `tracking-shot` `community-guide`
- **来源类型：** 公开教程模板
- **来源：** [VideoToPrompt](https://www.videotoprompt.app/posts/hailuo-h3-prompt-guide)
- **发布时间：** 2026-07-21
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ⚪ 否 · 结果可见 ⚪ 否
- **Note：** Published as an H3 prompt template; no generated H3 output is shown beside the prompt.

---

## 图生视频

<a id="h3-0002"></a>

### H3-0002 · 从首帧生成现代舞

**图生视频** · **官方示例** · ⭐ Featured

#### 内容说明

使用首帧图片，让画面中的人物开始跳现代舞的官方图生视频示例。

#### 原始 Prompt

```text
Contemporary dance, the people in the picture are performing contemporary dance.
```

#### 中文翻译

```text
现代舞，图片中的人物正在表演现代舞。
```

#### 详细信息

- **生成参数：** `duration: 5s` · `resolution: 2K` · `ratio: adaptive`
- **Tags：** `dance` `human-motion` `first-frame` `official`
- **来源类型：** 官方示例
- **来源：** [MiniMax](https://platform.minimax.io/docs/guides/video-generation)
- **发布时间：** 2026-07-31
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** Published with a first-frame input in the official API guide.

---

## 首尾帧生视频

<a id="h3-0003"></a>

### H3-0003 · 小女孩成长转场

**首尾帧生视频** · **官方示例** · ⭐ Featured

#### 内容说明

通过首帧和尾帧控制人物从童年到成年的转场。

#### 原始 Prompt

```text
A little girl grows up.
```

#### 中文翻译

```text
一个小女孩逐渐长大。
```

#### 详细信息

- **生成参数：** `duration: 5s` · `resolution: 2K` · `ratio: adaptive`
- **Tags：** `transition` `aging` `first-frame` `last-frame` `official`
- **来源类型：** 官方示例
- **来源：** [MiniMax](https://platform.minimax.io/docs/guides/video-generation)
- **发布时间：** 2026-07-31
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** Published with first- and last-frame inputs in the official API guide.

---

## 多模态参考生成

<a id="h3-0004"></a>

### H3-0004 · 复古贝雷帽时尚漫步

**多模态参考生成** · **官方示例** · ⭐ Featured

#### 内容说明

使用人物参考图保持主体一致性的电影感时尚片段。

#### 原始 Prompt

```text
On an overcast day, in an ancient cobbled alleyway, the model walks and adjusts a vintage beret with a smile; natural lighting and cinematic colors.
```

#### 中文翻译

```text
阴天，在古老的鹅卵石巷道中，模特一边行走，一边微笑着调整复古贝雷帽；自然光线，电影感色彩。
```

#### 详细信息

- **生成参数：** `duration: 5s` · `resolution: 2K` · `ratio: adaptive`
- **Tags：** `fashion` `character-consistency` `cinematic` `official`
- **来源类型：** 官方示例
- **来源：** [MiniMax](https://platform.minimax.io/docs/guides/video-generation)
- **发布时间：** 2026-07-31
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** Published with a reference image in the official API guide.

---

<a id="h3-0005"></a>

### H3-0005 · 希区柯克运镜与参考歌声

**多模态参考生成** · **官方示例** · ⭐ Featured

#### 内容说明

结合参考视频运镜、人物图片与音频演唱的官方全模态示例。

#### 原始 Prompt

```text
Reference the Hitchcock camera movement from Video 1, have the character in Image 2 sing, with the vocals matching Audio 3.
```

#### 中文翻译

```text
参考视频 1 中的希区柯克式运镜，让图片 2 中的角色演唱，并使歌声与音频 3 保持一致。
```

#### 详细信息

- **生成参数：** `duration: not stated` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `multimodal` `camera-reference` `voice-reference` `official`
- **来源类型：** 官方示例
- **来源：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **发布时间：** 2026-07-31
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** Published in the official MiniMax H3 launch article.

---

## 参与贡献

可通过 Issue 表单或 Pull Request 投稿。请提供原作者、直接来源链接、完整 Prompt、生成模式，以及是否存在可确认由 MiniMax H3 生成的公开结果。详情见 [CONTRIBUTING.md](docs/CONTRIBUTING.md)。

## 许可证与删除请求

仓库原创内容采用 [CC BY 4.0](LICENSE)；第三方 Prompt 与媒体仍归原权利人所有，详见 [NOTICE.md](NOTICE.md)。权利人可提交删除请求。

---

MiniMax and Hailuo are trademarks of their respective owners. This community project is not affiliated with or endorsed by MiniMax.

Generated from structured data curated through 2026-08-01.
