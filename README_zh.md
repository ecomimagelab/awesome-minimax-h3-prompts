<p align="center"><img src="public/cover.svg" alt="Awesome MiniMax H3 Prompts" width="100%"></p>

# Awesome MiniMax H3 提示词

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](LICENSE)
[![Validate data](https://github.com/ecomimagelab/awesome-minimax-h3-prompts/actions/workflows/validate.yml/badge.svg)](https://github.com/ecomimagelab/awesome-minimax-h3-prompts/actions/workflows/validate.yml)

> 收录 MiniMax H3 公开提示词、生成案例和提示词方法的中英双语资源库。

**简体中文** · [English](README.md)

[▶ **Open the playable video library / 打开可直接播放的视频页面**](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/)

## 关于 MiniMax H3

MiniMax H3 是可将文本、图片、视频和音频作为统一上下文的视频生成模型。本仓库严格区分官方示例、社区实测 Prompt 和尚未展示 H3 结果的公开教程模板，方便读者判断每条内容的证据强度。

- Official model: `MiniMax-H3`
- Output: up to 2K, 4–15 seconds
- Inputs: text, image, video, and audio references
- Official guide: [MiniMax H3 Video Generation](https://platform.minimax.io/docs/guides/video-generation)
- Community prompting guide: [fal.ai H3 guide — bilingual notes](docs/FAL_PROMPTING_GUIDE.md)
- Curation rules: [Deduplication and source precedence](docs/CURATION_POLICY.md)

> [!IMPORTANT]
> **版权与核验说明：** 没有视频就不收录：每条 Prompt 都必须有可公开下载的结果视频，并镜像保存到 `media/`；不能只保留外部播放链接。相同成片只发布一次，多段有效提示词归到同一视频下。二级指南转载 MiniMax 官方案例时，来源归属 MiniMax，不把转载页面标成原始来源。如果来源只发布视频，可以根据视频反推 Prompt，但必须明确标记为编辑重构，不能冒充创作者原始 Prompt。内容公开可见不代表作者放弃权利。镜像的第三方内容不适用本仓库的 CC BY 4.0，权利人可通过删除申请表要求下架。

## 收录统计

| Metric | Count |
| --- | ---: |
| Total prompts | **50** |
| Official examples | **39** |
| Community tested | **11** |
| Community guide templates | **0** |
| Last curated | **2026-08-01** |

## 按生成模式浏览

- [文生视频 (9)](#文生视频)
- [图生视频 (1)](#图生视频)
- [首尾帧生视频 (9)](#首尾帧生视频)
- [多模态参考生成 (31)](#多模态参考生成)

## 精选提示词

- [无人机上的 TikTok 舞者](#h3-0001) — 官方示例
- [小女孩成长转场](#h3-0003) — 官方示例
- [复古贝雷帽时尚漫步](#h3-0004) — 官方示例
- [希区柯克运镜与参考歌声](#h3-0005) — 官方示例
- [Frutiger Aero 商场第一人称漫步](#h3-0007) — 社区实测
- [别再叫我的名字](#h3-0012) — 社区实测
- [不会得到回复的信](#h3-0013) — 社区实测
- [我看得见尘土](#h3-0014) — 社区实测
- [复古望远镜品牌短片](#h3-0017) — 官方示例
- [厨房里的手绘发光生物](#h3-0018) — 社区实测
- [交互式游戏装备界面](#h3-0019) — 社区实测
- [咖啡微距到沙漠的无缝转场](#h3-0020) — 社区实测

## 合集视频与多段提示词

### H3-0006–H3-0007 · 一个原视频中的 2 段提示词

来源将这些案例发布在同一个合集视频中。视频只展示一次，对应的完整提示词依次列在下方。

#### 案例视频

[▶ 在视频页面播放](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-reddit-neggy5-minimax-h3-tests) · [↗ 查看仓库中的 MP4 文件](media/reddit-neggy5-minimax-h3-tests.mp4)

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


### H3-0012–H3-0016 · 一个原视频中的 5 段提示词

来源将这些案例发布在同一个合集视频中。视频只展示一次，对应的完整提示词依次列在下方。

#### 案例视频

[▶ 在视频页面播放](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-alex-patrascu-minimax-h3-scenes) · [↗ 查看仓库中的 MP4 文件](media/alex-patrascu-minimax-h3-scenes.mp4)

---

<a id="h3-0012"></a>

### H3-0012 · 别再叫我的名字

**文生视频** · **社区实测** · ⭐ Featured

#### 内容说明

一段 15 秒荒漠对峙，以单一手持镜头呈现，第二位说话者始终位于摄影机后。

#### 原始 Prompt

```text
PROMPT 1:

SCENE CONTEXT A middle-aged man stands in the middle of a dirt road in open desert and holds a pistol level at the person filming him. He gives an instruction, is answered by name, and warns them not to say it again. Nothing is fired.

TIMELINE 0.0–3.0s — he is already aimed and steady; his first line lands. 3.0–6.0s — the off-frame reply uses his name; his jaw sets and the muzzle does not drop. 6.0–9.0s — his second line; he takes half a step forward and re-sights. 9.0–11.0s — the off-frame voice starts his name again and stops. 11.0–15.0s — his last line; wind lifts dust across the road behind him; he holds the aim. Hold to black-free end.

ACTIVE REFERENCES No image or video references are active in this shot. Build the man from description only. Man, fifties, white, average build, standing, thinning brown hair, a brown moustache, thin-rimmed prescription glasses; light green long-sleeved button-down shirt with the sleeves buttoned at the wrist, dark work trousers; stern, brow furrowed, sweat starting at the hairline; frightened underneath and controlling it; speaking voice flat, plain, mid-western American, no theatricality. Second speaker: the unseen person the pistol is aimed at, occupying the camera position, never entering frame and never seen. Voice only — male, forties, close to the lens, low and careful.

LOCATION MAP Camera on the dirt road 3.5 m from him at his chest height, facing him square-on so the muzzle is aligned with the lens axis. FG: rutted dirt and loose gravel across the lower frame. MG: the man alone, centre frame. BG: the dirt road receding to a vanishing point at x 50%, y 44%, low scrub and dry brush from x 0% to x 30% and x 70% to x 100%, a distant fence line at x 62%, y 48%, flat desert horizon at y 46%, overcast sky filling the upper half with one pale blue break low at x 24%, y 36%. He occupies x 50%, y 50%, body frontal, both feet planted, right arm extended toward camera with the silver pistol at x 50%, y 56%, held at the very front of the depth plane. His eyeline is straight down the lens. The first visible frame already has him aimed and in position — no empty establishing frame, no walk-in, no delayed reveal, and he remains the only figure in frame for the entire take.

FORMAT MODE Single continuous take, no internal cuts, no transitions, no fades. Real-time motion. His lines are on camera; the second voice is an intentional off-frame speaker at the camera position. No other voices, no narration, no subtitles, no score.

CAMERA 47° diagonal field of view, camera 3.5 m from him at chest height, natural human-eye perspective, no distortion, natural face and body proportions, the road and horizon readable behind him, comfortable depth of field with the pistol slightly forward of his focal plane. Handheld, shoulder-mounted mass, operator breath and small involuntary settling — the camera is being held by the person he is aiming at, so it flinches minutely rather than gliding. Total travel under 20 cm, no push-in, no zoom, no focus rack. Focus holds his eyes behind the glasses; the pistol stays just soft.

ACTION TIMING He is already sighted along the barrel as the shot opens and speaks without lowering it. The off-frame voice answers with his name; his jaw sets and the muzzle does not waver. He speaks his second line and takes half a step forward on the dirt, re-sighting as his weight lands. The off-frame voice begins his name again and stops. He delivers his last line, and wind lifts a curtain of dust across the road behind him. He holds the aim to the end without firing and without lowering the weapon.

PHYSICS The pistol carries real weight — his wrist and forearm show the load and micro-correct continuously; the muzzle drifts a few millimetres and is pulled back on line. His half step lands heel-first in soft dirt with visible weight transfer and a small dust puff that drifts and thins. Shirt fabric pulls across the extended shoulder and creases at the elbow. Wind moves the loose dust and the dry scrub in the same direction and at the same time. Thinning hair lifts and settles with the gust. Sweat beads at his temple and does not run.

LIGHTING Primary source is the full overcast sky acting as one enormous soft toplight, giving even illumination with minimal harsh shadow — a soft shadow under the brow and the nose only, no hard edges anywhere. Secondary is dry ground bounce filling under the chin and lifting the shadow side of the pistol. Both lenses of his glasses carry a broad soft reflection of the sky, and his eyes stay readable behind them. Exposure is set for his face; the sky sits bright but not clipped. No sun shaft, no lens flare, no added key, no light change during the take.

AUDIO Dry wind across open ground, loose grit moving on the road, dry brush ticking, one distant bird, his own breathing close and unsteady. Ambient ducks under the voices. Exactly this exchange, flat and plain, no shouting — 25 words total: HIM: "Put it on the ground. Slowly." OFF-FRAME: "You're not going to shoot me, Ray." HIM: "I've been wrong about myself before." OFF-FRAME: "Ray—" HIM: "Don't say my name again." His first line opens the shot. The off-frame reply lands as his jaw sets. His second line comes as he takes the half step. The off-frame "Ray—" is cut off by his last line, which is quieter than everything before it. His lips move only for his own lines; there is no dialogue in the pauses and no muttering between beats.

POSITIVE LOCKS Exactly one visible person is in frame for the whole take — nobody enters at any edge, no second figure appears on the road, at the fence line or in the reflections on his glasses, and the off-frame speaker is never seen. The pistol stays in his right hand, stays aimed at the lens, and is never fired, never lowered and never re-holstered; no muzzle flash, no recoil, no gunshot. He stays on the road and never turns away from camera. Naturalistic muted palette of dry greens and browns against pale overcast grey. Live-action photoreal footage shot on ARRI Alexa 35, tense neutral mood, natural film grain.
```

#### 中文翻译

```text
提示词 1：

场景背景 开阔荒漠的一条土路中央，一名中年男人用手枪平指正在拍摄他的人。他发出指令，对方叫出他的名字，他警告对方不要再说。全程不开枪。

时间线 0.0–3.0 秒——他已稳定瞄准，说出第一句。3.0–6.0 秒——画外回应叫出他的名字；他咬紧下颌，枪口不落。6.0–9.0 秒——说第二句；向前半步并重新瞄准。9.0–11.0 秒——画外声音再次开口叫名字又停下。11.0–15.0 秒——他说最后一句；风卷起他身后路上的尘土，他保持瞄准。结尾不要淡黑。

启用参考 本镜头不使用图片或视频参考，只按描述构建男人。五十多岁白人，普通体型，棕发稀疏、棕色小胡子、细框近视眼镜；浅绿色长袖扣领衬衫，袖口扣紧，深色工作裤；神情严厉、眉头紧皱，发际线开始出汗；内心恐惧但强行控制；声音平直朴素、美国中西部口音、不戏剧化。第二位说话者是被枪指着、位于摄影机位置且永不入镜的人。只有声音：四十多岁男性，靠近镜头，低声而谨慎。

位置图 摄影机位于土路上，距他 3.5 米、胸口高度，正对他，使枪口与镜头轴线重合。前景：画面下方车辙与松散碎石。中景：男人独自在正中央。背景：土路向 x 50%、y 44% 消失点延伸；低矮灌木和枯枝位于 x 0%–30% 与 x 70%–100%；远处栅栏线在 x 62%、y 48%；平坦荒漠地平线在 y 46%；阴天占据上半画面，x 24%、y 36% 低处有一小块浅蓝天空。他位于 x 50%、y 50%，正面站立，双脚着地，右臂伸向摄影机，银色手枪位于 x 50%、y 56%，处在景深最前端。视线沿镜头直视。第一可见帧中他已就位瞄准；不要空镜、走入或延迟揭示，整段始终只有他一人入镜。

格式模式 单一连续镜头，无内部切镜、转场或淡化；实时运动。他的台词在镜头内说出，第二个声音刻意设置在摄影机位置的画外。无其他声音、旁白、字幕或配乐。

摄影 47° 对角视场，摄影机距 3.5 米、胸口高度；自然人眼透视、无畸变、脸与身体比例自然，后方道路和地平线清晰，舒适景深，手枪略微位于脸部焦平面之前。肩扛式手持重量感，保留摄影者呼吸与轻微不自主沉降；由于持机者正被瞄准，摄影机产生细小畏缩而非滑行。总位移小于 20 厘米，不推进、不变焦、不拉焦。焦点锁在眼镜后的双眼，手枪保持略虚。

动作时序 镜头开始时他已沿枪管瞄准，不放下枪便开口。画外声音以名字回应；他咬紧下颌，枪口不晃。他说第二句并在土路上向前半步，重量落下时重新瞄准。画外声音再次开始叫名字又停下。他说最后一句，风在身后道路上卷起一幕尘土。他保持瞄准至结尾，不开枪也不放下武器。

物理 手枪具有真实重量，手腕和前臂承受负荷并持续微调；枪口漂移几毫米后被拉回轴线。半步以脚跟先落在松软土中，可见重量转移与一小团逐渐飘散变薄的尘土。衬衫布料在伸出的肩膀上被拉紧，肘部形成褶皱。风同时、同向推动松尘和枯灌木；稀疏头发随阵风抬起后落下；太阳穴汗珠凝结但不流淌。

灯光 主光为整片阴天形成的巨大柔和顶光，照明均匀，几乎无硬影；仅眉骨与鼻下有柔影，任何位置都无硬边。辅光为干燥地面反射，填充下巴下方并抬亮手枪阴影侧。两片镜片都有宽阔柔和的天空反光，眼睛仍清晰可读。曝光以脸为准，天空明亮但不剪裁。无阳光束、镜头光斑、额外主光，镜头中光线不变化。

声音 开阔地面的干风、道路上移动的松砂、枯灌木轻响、一只远鸟，以及他近距离不稳定的呼吸。对白时环境声压低。严格按以下 25 个英文词的对白节奏，平直朴素、不喊叫：他："把它放在地上。慢慢来。" 画外："你不会开枪打我，雷。" 他："我以前也看错过自己。" 画外："雷——" 他："别再叫我的名字。" 第一行开启镜头；画外回应时他咬紧下颌；向前半步时说第二句；画外的“雷——”被他最后一句打断，最后一句比之前所有话都轻。他只在自己的台词中动嘴；停顿间没有对白或喃喃自语。

正向锁定 全程恰好只有一个可见人物；任何边缘都不进入他人，道路、栅栏线或眼镜反射中都不出现第二个人，画外说话者绝不被看见。手枪始终在右手、始终指向镜头，绝不开火、放下或重新入套；无枪口火焰、后坐或枪声。他留在路上，从不背对摄影机。干燥绿与棕配浅阴天灰的自然低饱和色板。ARRI Alexa 35 拍摄的真人电影级写实影像，紧张而中性的情绪，自然胶片颗粒。
```

#### 详细信息

- **生成参数：** `duration: 15s` · `resolution: 2560x1440` · `ratio: 16:9`
- **Tags：** `desert` `single-take` `handheld` `dialogue` `community-tested`
- **来源类型：** 社区实测
- **来源：** [Alex Patrascu (@maxescu)](https://x.com/maxescu/status/2082563245504856385)
- **所属主帖：** [X thread](https://x.com/maxescu/status/2082563241062875568)
- **来源位置：** `reply`
- **发布时间：** 2026-07-29
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** The complete prompt appears in an author reply; the parent post says the displayed scenes were tried with MiniMax H3.

---

<a id="h3-0013"></a>

### H3-0013 · 不会得到回复的信

**文生视频** · **社区实测** · ⭐ Featured

#### 内容说明

一段发生在结霜温室中的克制年代戏，通过信纸特写表现人物情绪。

#### 原始 Prompt

```text
PROMPT 2:

SCENE CONTEXT In a frosted country-house conservatory on a grey morning, an older woman tells a younger one that the letter will not be answered. The younger woman holds her composure and loses it only in her hands.

FORMAT MODE Controlled three-segment sequence, one HARD CUT and one INSERT CUT. Real-time motion.

LOCATION MAP Camera inside a glazed conservatory, 3 m from the two women, facing them with the steamed glass wall behind them. FG: potted fern fronds at the frame edge. MG: older woman screen-left, younger woman screen-right, 80 cm apart. BG: glass panes, frost-white winter garden, a cast-iron bench, one low oil lamp. Soft light comes from the whole glass wall behind and above them.

FIRST FRAME AND SPATIAL BLOCKING Both women are in frame from the first visible frame. Older woman at x 32%, y 46%, three-quarter profile facing screen-right, gloved hands folded at her waist. Younger woman at x 68%, y 44%, torso squared to her, gaze locked on her face, a folded letter held in both hands at x 62%, y 76%. No empty establishing frame.

OPTICS LENS LOCK SEGMENT 1 = 47°, camera 3 m out, natural proportions, both faces and the conservatory geography readable. LENS LOCK SEGMENT 2 = 18°, camera 6.5 m back down the conservatory aisle, strong compression, glass panes and ferns stacking behind the younger woman, razor-thin focus on her eyes. LENS LOCK SEGMENT 3 = 29°, camera 4 m out and lower, close on her hands by lens reach, the room dissolving to creamy bokeh behind.

CAMERA Segment 1 locked-off at eye height. Segment 2 long lens with the faintest human drift. Segment 3 handheld, settling downward toward the letter.

ACTION TIMING BEAT 1 — The older woman speaks her line, chin level, hands unmoving. The younger woman does not react in her face. HARD CUT BEAT 2 — Long-lens hold on the younger woman. A long beat. Her eyelids redden; she blinks once and keeps her eyes forward, refusing to look down. INSERT CUT BEAT 3 — Tight on her hands. Her thumbs press and slowly crush the folded letter's edge until the paper buckles, then stop. Hold on the buckled paper.

PHYSICS Paper buckles progressively under thumb pressure and holds its new shape. Glove leather stretches over her knuckles. Condensation runs down glass panes in slow irregular tracks. Silk and wool hold real weight; her skirts do not float. Breath fogs faintly in the cold air.

LIGHTING Primary source is vast soft north daylight through the steamed glass wall behind and above them, motivated, wrapping both faces. Secondary: cold blue bounce off the frost outside, and one warm low oil lamp deep in frame. Soft shadow rolloff with clearly readable eyes and catchlights — restrained low contrast, not silhouette.

AUDIO Rain ticking on glass, a distant door, the faint hiss of the oil lamp, a bird outside. Ambient ducks under the voice. The older woman speaks exactly this line as the shot opens: "There will be no reply, and you will not ask again." No other dialogue, no score. The younger woman's lips stay still.

POSITIVE LOCKS Exactly two women appear and no servant or third figure enters. Both hold their positions across all segments. Costume, gloves, the folded letter and the frost state remain identical across the cuts. Cinematic photorealistic footage shot on ARRI Alexa 35, pearl-grey and soft-green grade, low contrast, natural film grain.
```

#### 中文翻译

```text
提示词 2：

场景背景 灰暗的清晨，一座结霜的乡间宅邸玻璃温室里，一位年长女人告诉年轻女人，那封信不会得到回复。年轻女人保持着镇定，只有双手泄露了情绪。

格式模式 受控的三段式序列，一次硬切和一次插入特写切镜；实时运动。

位置图 摄影机位于玻璃温室内，距两位女人 3 米，面向她们，后方是蒙着水汽的玻璃墙。前景：画面边缘的盆栽蕨叶。中景：年长女人在画面左侧，年轻女人在右侧，相距 80 厘米。背景：玻璃窗格、霜白的冬季花园、一张铸铁长椅和一盏低矮油灯。柔光从她们身后及上方的整面玻璃墙照入。

首帧与空间调度 第一可见帧中两人都已入镜。年长女人位于 x 32%、y 46%，三分之二侧面朝画面右侧，戴手套的双手叠在腰前。年轻女人位于 x 68%、y 44%，躯干正对她，目光锁住她的脸，双手在 x 62%、y 76% 处拿着一封折好的信。不要空镜建立镜头。

光学与镜头锁定 第 1 段为 47°，摄影机距 3 米，自然比例，两张脸和温室空间均清晰可读。第 2 段为 18°，摄影机沿温室过道后退至 6.5 米，产生强烈压缩感，玻璃窗格与蕨类层叠在年轻女人身后，极浅焦点锁在她的眼睛。第 3 段为 29°，摄影机距 4 米且机位更低，以镜头焦段贴近她的双手，房间在后方化成奶油般散景。

摄影 第 1 段眼平固定机位；第 2 段长焦，只有极轻微的人体漂移；第 3 段手持，向下沉落到信件。

动作时序 节拍 1——年长女人抬平下巴说出台词，双手不动。年轻女人脸上毫无反应。硬切至节拍 2——长焦停留在年轻女人身上，长时间停顿。她的眼睑泛红，只眨一次眼，仍直视前方，拒绝低头。插入特写切至节拍 3——紧拍她的双手。拇指按压并缓慢碾皱折叠信纸的边缘，直到纸张屈曲后停下；停留在变形的纸上。

物理 信纸在拇指压力下逐渐屈曲并保持新形状；手套皮革在指关节上绷紧；冷凝水沿玻璃窗格以缓慢而不规则的轨迹流下；丝绸与羊毛具有真实重量，裙摆不漂浮；寒冷空气中呼吸产生淡淡白雾。

灯光 主光为从她们身后与上方蒙雾玻璃墙透入的大片柔和北向日光，动机明确并包裹两张脸。辅光来自室外霜面的冷蓝反射，画面深处另有一盏温暖低位油灯。阴影柔和过渡，双眼和眼神光清晰可见；克制的低反差，不要剪影。

声音 雨点敲击玻璃、远处一扇门、油灯轻微嘶声和室外鸟鸣。说话时环境声压低。镜头开始时，年长女人准确说："不会有回信，你也不准再问。" 没有其他对白，没有配乐；年轻女人的嘴唇始终不动。

正向锁定 画面中恰好只有两位女人，不出现仆人或第三个人。三段中两人位置保持不变；服装、手套、折叠信件和结霜状态在切镜间完全一致。ARRI Alexa 35 拍摄的电影级写实影像，珍珠灰与柔绿调色，低反差，自然胶片颗粒。
```

#### 详细信息

- **生成参数：** `duration: 15s` · `resolution: 2560x1440` · `ratio: 16:9`
- **Tags：** `period-drama` `dialogue` `three-segment` `insert-shot` `community-tested`
- **来源类型：** 社区实测
- **来源：** [Alex Patrascu (@maxescu)](https://x.com/maxescu/status/2082563249095020865)
- **所属主帖：** [X thread](https://x.com/maxescu/status/2082563241062875568)
- **来源位置：** `reply`
- **发布时间：** 2026-07-29
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** The complete prompt appears in an author reply; the parent post says the displayed scenes were tried with MiniMax H3.

---

<a id="h3-0014"></a>

### H3-0014 · 我看得见尘土

**图生视频** · **社区实测** · ⭐ Featured

#### 内容说明

一段以参考图锁定人物和光线、带热浪效果的 15 秒西部片单镜头。

#### 原始 Prompt

```text
PROMPT 3:

SCENE CONTEXT A weathered man rests against a timber rail in blistering noon heat while something is brought up the street toward him. A voice across the street offers him a way out and he declines it.

TIMELINE 0.0–3.0s — the off-frame line; a gust lifts dust across frame. 3.0–6.0s — his answer; he turns his face out of the dust and works his jaw once. 6.0–9.5s — the second off-frame line; his eyes track slowly screen-left to screen-right. 9.5–12.5s — his last line, flat and final. 12.5–15.0s — he pushes off the rail with one shoulder and straightens out of the top of frame; dust closes behind him.

ACTIVE REFERENCES 📷Image1 is the reference and the exact first visible frame — source of truth for his face, hat, wardrobe and the light. Man, fifties, leaning against a timber rail, pale wide-brim hat pushed back with a visible pale forehead line, dust-caked collarless shirt torn at one shoulder, deep sun creases, broken capillaries, grit in the stubble; long past being surprised; speaking voice dry, laconic, low volume. 100% matches the reference. Second speaker: an unseen man across the street, off-frame screen-left at the same level, never entering frame. Voice only — male, middle-aged, flat, carrying across distance.

LOCATION MAP Camera on the street 4.5 m from him at his eye height. FG: nothing between camera and subject except airborne dust. MG: the man against grey weathered timber spanning x 0% to x 55%. BG: a blurred wagon at x 76%, y 30% and two standing figures at x 84%, y 34% and x 92%, y 36%, dissolved in heat shimmer, pale sky at the top edge. He occupies x 34%, y 50%, chest-up, torso angled to screen-right, eyes to screen-left. The first visible frame already contains him in exactly this position. He is the only sharp figure and remains so.

FORMAT MODE Single continuous take, no internal cuts, no transitions. Real-time motion. His lines are on camera; the second voice is an intentional off-frame reply. No other voices, no narration, no subtitles, no music.
CAMERA 29° diagonal field of view, camera 4.5 m out at his eye height, close framing achieved through lens reach, his face razor-sharp, the wagon and the two figures compressed flat behind him and melting into bokeh, visible heat shimmer between camera and background. Locked off with the faintest human drift; no push-in, no focus rack.

ACTION TIMING He squints harder as a gust lifts dust across the frame, and turns his face a few degrees out of it as he answers. He works his jaw once. His eyes track slowly from screen-left to screen-right, following something crossing behind camera. A long beat. He delivers his last line, then pushes off the rail with one shoulder and straightens, rising out of the top edge of frame as the dust closes behind him.

PHYSICS Airborne dust crosses in real gusts, catches the light and settles on his shoulders. The torn shirt fabric lifts at the shoulder and falls. The timber rail does not move when he pushes off it, and his weight transfers audibly into his boots. Sweat and grit sit on the skin without running.

LIGHTING Inherit 📷Image1 exactly and do not relight. Primary: hard vertical noon sun. Secondary: brilliant bounce off pale caliche dust filling the shadows from below. Deep shadow under the hat brim across the bridge of his nose. Highlights on the timber and sky sit near clipping. No fill added, no light change during the take.

AUDIO Dry wind against timber, distant wagon wheels and harness, a fly, boot grit. Ambient ducks under the voices. Exactly this exchange, laconic and flat, spoken across distance without echo effects — 22 words total: OFF-FRAME MAN: "They're bringing him up now." HIM: "I can see the dust." OFF-FRAME MAN: "You want to be somewhere else?" HIM: "I've been somewhere else. Didn't help." The off-frame line opens the shot. He answers into the gust. The second off-frame line comes while his eyes track across. His last line lands as he pushes off the rail. His lips move only for his own lines.

POSITIVE LOCKS Exactly one sharp figure is in frame; the two background figures stay unresolved in the heat haze and never become characters or come into focus, and no one crosses between camera and subject. Hat, torn shirt, dust layer and the timber rail stay exactly as in 📷Image1. Cinematic photorealistic footage shot on ARRI Alexa 35, natural film grain.
```

#### 中文翻译

```text
提示词 3：

场景背景 炙热正午，一名饱经风霜的男人靠在木栏上，街道远处有人正把某个对象带向他。街对面一个声音给他逃脱的机会，他拒绝了。

时间线 0.0–3.0 秒——画外台词响起，一阵风把尘土卷过画面。3.0–6.0 秒——他回答，稍微转脸避开尘土，下颌动一次。6.0–9.5 秒——第二句画外台词，他的目光缓慢从画面左侧移至右侧。9.5–12.5 秒——他说出最后一句，平淡而决绝。12.5–15.0 秒——他用一侧肩膀推离栏杆，站直并从画面上缘离开，尘土在身后合拢。

启用参考 📷Image1 是参考图，也是精确的第一可见帧，是其脸、帽子、服装和光线的唯一依据。男人五十多岁，靠着木栏；浅色宽檐帽向后推，额头留有清晰浅色晒痕；无领衬衫覆满尘土，一侧肩头撕裂；深重日晒纹、破裂毛细血管、胡茬里夹着砂砾；早已不会感到意外；声音干涩、简短、低声。与参考图 100% 一致。第二位说话者是街对面看不见的男人，位于画外左侧同一高度，始终不入镜；只有声音，中年男性，平直，能跨越距离传来。

位置图 摄影机在街上，距他 4.5 米，与眼睛同高。前景除悬浮尘土外没有遮挡。中景是男人靠在从 x 0% 延伸至 x 55% 的灰色风化木栏。背景：x 76%、y 30% 处一辆模糊马车，x 84%、y 34% 与 x 92%、y 36% 处两名站立人物，均消融在热浪中；画面顶部为浅色天空。他位于 x 34%、y 50%，胸部以上入镜，身体朝画面右侧，眼睛看向左侧。第一帧已精确处于此位置；他始终是唯一清晰人物。

格式模式 单一连续镜头，无内部切镜、无转场；实时运动。他的台词在镜头内说出，第二个声音为刻意设置的画外回应。无其他声音、旁白、字幕或音乐。

摄影 29° 对角视场，摄影机距 4.5 米、与他眼睛同高，通过焦段获得近景。他的脸锐利清晰，马车和两个人物被压扁在后方并融为散景，镜头与背景之间可见热浪。固定机位，仅有极轻微人体漂移；不推进，不拉焦。

动作时序 阵风卷起尘土时他眯紧眼睛，回答时将脸转开几度避尘，下颌动一次。目光缓慢从左移到右，跟随摄影机后方横穿的东西。长停顿后说最后一句，再以肩膀推离栏杆站直，从画面上缘离开，尘土在身后合拢。

物理 悬浮尘土以真实阵风横穿画面，捕捉光线并落在肩上；撕裂衬衫在肩头被吹起后落下；他推离时木栏不动，重量转移到靴子上且有可听见的声音；汗水与砂砾停留在皮肤上而不流淌。

灯光 完全继承 📷Image1，不重新布光。主光为垂直的强烈正午阳光；辅光是浅色钙质尘土从下方产生的明亮反射，填充阴影。帽檐下方横跨鼻梁形成深影。木材与天空高光接近过曝；不加补光，镜头中光线不变化。

声音 干风吹过木材、远处马车轮与挽具声、苍蝇和靴底砂砾声。对白时环境声压低。严格说出这组简短平淡、跨距离但不加回声效果的 22 词对白：画外男人："他们正把他带上来。" 他："我看得见尘土。" 画外男人："你想去别处吗？" 他："我去过别处。没用。" 画外台词开启镜头；他迎着阵风回答；目光横移时第二句画外台词响起；推离栏杆时最后一句落下。他只在自己的台词中动嘴。

正向锁定 画面中恰好只有一个清晰人物；背景两人始终无法在热浪中辨认，绝不成为角色或进入焦点，也没有人从摄影机与主体之间穿过。帽子、破衬衫、尘土层与木栏必须与 📷Image1 完全一致。ARRI Alexa 35 拍摄的电影级写实影像，自然胶片颗粒。
```

#### 详细信息

- **生成参数：** `duration: 15s` · `resolution: 2560x1440` · `ratio: 16:9`
- **Tags：** `western` `image-reference` `single-take` `dialogue` `community-tested`
- **来源类型：** 社区实测
- **来源：** [Alex Patrascu (@maxescu)](https://x.com/maxescu/status/2082563252471357498)
- **所属主帖：** [X thread](https://x.com/maxescu/status/2082563241062875568)
- **来源位置：** `reply`
- **发布时间：** 2026-07-29
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** The complete prompt appears in an author reply; the parent post says the displayed scenes were tried with MiniMax H3. Image1 is required but is not redistributed here.

---

<a id="h3-0015"></a>

### H3-0015 · 我星期二签了

**文生视频** · **社区实测**

#### 内容说明

以三个克制机位讲述的那不勒斯蓝调时刻阳台戏。

#### 原始 Prompt

```text
PROMPT 4:

SCENE CONTEXT On a narrow Naples balcony at blue hour, a woman tells a man she has already taken the job. He does not argue, which is worse.

FORMAT MODE Controlled three-segment sequence, two HARD CUTs. Real-time motion. Restrained camera throughout.

LOCATION MAP Camera on the balcony, 2 m from the couple, facing them with the lit kitchen doorway behind them screen-centre-left. FG: iron rail and two espresso cups. MG: woman and man standing 60 cm apart. BG: alley canyon, drying laundry, a lit window opposite, string lights. Warm light comes from behind them through the doorway; cool dusk fills from camera side.

FIRST FRAME AND SPATIAL BLOCKING Both are in frame from the first visible frame. Woman at x 34%, y 46%, torso facing screen-right, one hand on the iron rail. Man at x 68%, y 44%, three-quarter profile facing her, hands at his sides. Their eyelines meet at x 50%. The two espresso cups sit on the rail at x 52%, y 74%.

OPTICS LENS LOCK SEGMENT 1 = 47°, camera 2.2 m out, natural proportions, both faces and the alley depth readable. LENS LOCK SEGMENT 2 = 29°, camera 4.5 m back along the balcony, close on the woman by lens reach, alley lights compressing into soft round bokeh behind her. LENS LOCK SEGMENT 3 = 84°, camera 1 m from the man, foreground rail presence, the whole balcony and doorway visible to the edges.

CAMERA Segment 1 handheld with almost no travel, operator breath only. Segment 2 locked-off. Segment 3 handheld, a slow 20 cm settle downward as he lowers his head. Camera stays on the dusk side of both faces.

ACTION TIMING BEAT 1 — She speaks her line, then looks at her own hand on the rail rather than at him. He does not move. HARD CUT BEAT 2 — Held on her. A long beat. Her mouth begins a word and abandons it; she swallows and lifts her eyes back to him. HARD CUT BEAT 3 — On him. He nods once, small, and picks up one of the espresso cups without drinking from it. The shot holds on his hand around the cup as the string lights flicker once.

PHYSICS Cool air moves the drying laundry in the background on real cloth delay. Her knit sleeve compresses where her forearm presses the rail. The cup has weight; the saucer chatters faintly when lifted. Loose hair moves independently of her head turn.

LIGHTING Primary source is the warm kitchen bulb behind them through the doorway, motivated, giving both a warm hair and shoulder rim. Fill is cool ambient dusk from camera side. Soft shadow rolloff, not crushed silhouettes — eyes stay readable with visible catchlights. Practical string lights and one lit window across the alley sit in the background.

AUDIO Distant scooter, a television two floors down, pigeons, faint street voices. Ambient ducks under the voice. She speaks exactly this line as the shot opens: "I signed it on Tuesday." No other dialogue, no score. His lips stay still.

POSITIVE LOCKS Exactly two people are on the balcony and no one appears in the doorway behind them. Their positions, wardrobe, the two cups and the laundry arrangement remain identical across the cuts. Cinematic photorealistic footage shot on ARRI Alexa 35, warm-amber against slate-blue grade, low contrast, natural film grain.
```

#### 中文翻译

```text
提示词 4：

场景背景 蓝调时刻，那不勒斯一处狭窄阳台上，女人告诉男人她已经接受那份工作。他没有争辩，这反而更糟。

格式模式 受控三段式序列，两次硬切；实时运动，全程采用克制摄影。

位置图 摄影机位于阳台，距两人 2 米，面向他们，后方画面中左位置是亮着灯的厨房门。前景：铁栏杆与两杯意式浓缩咖啡。中景：女人和男人相距 60 厘米站立。背景：狭长巷道、晾晒衣物、对面一扇亮窗与串灯。暖光从他们后方门内照出，摄影机方向以冷色暮光补光。

首帧与空间调度 第一可见帧中两人都已入镜。女人位于 x 34%、y 46%，躯干朝画面右侧，一只手放在铁栏杆上。男人位于 x 68%、y 44%，三分之二侧面朝向她，双手垂在身侧。二人视线在 x 50% 相交。两杯咖啡位于栏杆 x 52%、y 74%。

光学与镜头锁定 第 1 段 47°，摄影机距 2.2 米，自然比例，两张脸和巷道纵深清晰可读。第 2 段 29°，摄影机沿阳台后退至 4.5 米，以焦段贴近女人，巷灯在她身后压缩成柔和圆形散景。第 3 段 84°，距男人 1 米，前景保留栏杆存在感，完整阳台和门口一直可见到画面边缘。

摄影 第 1 段手持、几乎无位移，只有摄影者呼吸；第 2 段固定机位；第 3 段手持，男人低头时缓慢向下沉 20 厘米。摄影机始终位于两张脸的暮光侧。

动作时序 节拍 1——她说出台词，然后看向自己放在栏杆上的手而不是男人；男人不动。硬切至节拍 2——停留在她身上，长时间停顿；她刚想开口便放弃，吞咽一下，再抬眼看他。硬切至节拍 3——拍男人；他轻轻点头一次，拿起其中一只咖啡杯但不喝。镜头停在他握杯的手上，串灯闪烁一次。

物理 冷空气吹动背景晾晒衣物，布料反应具有真实延迟；她前臂压栏杆处的针织袖子被挤压；杯子有重量，端起时杯碟轻响；散发的运动独立于她的转头。

灯光 主光来自身后门内暖色厨房灯泡，为头发与肩膀形成暖边光；补光为摄影机侧的冷色暮光。阴影柔和过渡，不要死黑剪影，眼睛与眼神光可读；背景保留真实串灯和对面一扇亮窗。

声音 远处踏板车、楼下两层的电视、鸽子与微弱街谈声。对白时环境声压低。镜头开始时她准确说："我星期二签了。" 没有其他对白或配乐；男人嘴唇始终不动。

正向锁定 阳台上恰好两个人，后方门口不出现任何人。切镜间二人位置、服装、两只杯子与晾衣布局保持完全一致。ARRI Alexa 35 拍摄的电影级写实影像，暖琥珀与石板蓝调色，低反差，自然胶片颗粒。
```

#### 详细信息

- **生成参数：** `duration: 15s` · `resolution: 2560x1440` · `ratio: 16:9`
- **Tags：** `relationship-drama` `blue-hour` `three-segment` `dialogue` `community-tested`
- **来源类型：** 社区实测
- **来源：** [Alex Patrascu (@maxescu)](https://x.com/maxescu/status/2082563256028139736)
- **所属主帖：** [X thread](https://x.com/maxescu/status/2082563241062875568)
- **来源位置：** `reply`
- **发布时间：** 2026-07-29
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** The complete prompt appears in an author reply; the parent post says the displayed scenes were tried with MiniMax H3.

---

<a id="h3-0016"></a>

### H3-0016 · 天亮时拿下那条路

**文生视频** · **社区实测**

#### 内容说明

由煤油灯、月光和炮火闪光推动的三段式战时命令场景。

#### 原始 Prompt

```text
PROMPT 5:

SCENE CONTEXT In a shelled Normandy farmhouse at night, a colonel orders a captain to take the lane at first light. The captain accepts the order knowing what it costs.

FORMAT MODE Controlled three-segment sequence, one HARD CUT and one REVERSE CUT. Real-time motion.

LOCATION MAP Camera inside a roofless farmhouse room, 2.5 m from a map table. FG: table edge, tin mug, field telephone. MG: colonel standing screen-left of the table, captain standing screen-right. BG: pinned maps on plaster, splintered beams, a hole in the roof. Primary light is a hurricane lamp on the table between them.

FIRST FRAME AND SPATIAL BLOCKING Both officers are already at the table in the first visible frame. Colonel at x 30%, y 44%, three-quarter profile facing screen-right, index finger planted on the map at x 46%, y 76%. Captain at x 70%, y 42%, torso squared to the colonel, gaze down on the finger, not the face. Lamp at x 50%, y 66%. No empty establishing frame.

OPTICS LENS LOCK SEGMENT 1 = 47°, camera 2.5 m from the table, natural proportions, both officers and the map geography readable. LENS LOCK SEGMENT 2 = 29°, camera 4 m back, close on the captain by lens reach, the pinned map wall compressed soft behind him. LENS LOCK SEGMENT 3 = 84°, camera 1.1 m above the map surface angled up past the lamp, foreground lamp glass looming, both men and the broken roof visible to the edges.

CAMERA Segment 1 locked-off at chest height. Segment 2 handheld with operator breath, camera on the lamp's shadow side. Segment 3 handheld low, slow rise past the lamp flame.

ACTION TIMING BEAT 1 — The colonel speaks his line, finger pressing hard enough to crease the map. Plaster dust drifts through the lamp beam. REVERSE CUT BEAT 2 — On the captain. A distant artillery flash strobes blue across his face. A muscle jumps in his cheek; he nods once and looks up. HARD CUT BEAT 3 — Low wide past the lamp. The captain squares his cap, turns and walks out of frame screen-right. The colonel stays, hand flattening the creased map, and the lamp flame leans in the draught of the door.

PHYSICS Paper creases and holds the crease under finger pressure. The lamp flame bends and recovers when air moves; its light level dips accordingly. Plaster dust falls with real settling drift. Boots find rubble with uneven weight transfer and grit sound. Wool uniform holds damp weight and does not billow.

LIGHTING Primary source is the hurricane lamp on the table, motivated, hard and warm, underlighting both faces and leaving eye sockets in shadow. Secondary: cold moonlight through the roof hole rimming shoulders, plus intermittent distant artillery flash on the back wall. Exposure is set for the lamp; shadows are allowed to crush. No added frontal fill.

AUDIO Distant shellfire, a field telephone hum, wind through the broken roof, drip of water. Ambient ducks under the voice. The colonel speaks exactly this line as the shot opens: "You take the lane at first light, with what you have." No other dialogue, no score. The captain's lips stay still.

POSITIVE LOCKS Exactly two officers are in the room and no other figures enter. Both stay on their own side of the table until the captain exits in the final beat. Uniform state, mud, plaster dust and the lamp position remain identical across the cuts. Cinematic photorealistic footage shot on ARRI Alexa 35, desaturated olive-and-amber grade, natural film grain.
```

#### 中文翻译

```text
提示词 5：

场景背景 夜晚，一座遭炮击的诺曼底农舍里，上校命令一名上尉在天亮时夺取那条小路。上尉明知代价仍接受命令。

格式模式 受控三段式序列，一次硬切和一次反打切镜；实时运动。

位置图 摄影机位于没有屋顶的农舍房间内，距地图桌 2.5 米。前景：桌沿、锡杯和野战电话。中景：上校站在桌子左侧，上尉站在右侧。背景：钉在灰泥墙上的地图、断裂木梁和屋顶破洞。主光为两人之间桌上的一盏煤油灯。

首帧与空间调度 第一可见帧中两位军官已经在桌旁。上校位于 x 30%、y 44%，三分之二侧面朝画面右侧，食指压在地图 x 46%、y 76% 处。上尉位于 x 70%、y 42%，躯干正对上校，目光落在手指而不是脸上。灯位于 x 50%、y 66%。不要空镜建立镜头。

光学与镜头锁定 第 1 段 47°，摄影机距桌 2.5 米，自然比例，两位军官和地图空间都清晰可读。第 2 段 29°，摄影机后退到 4 米，以焦段贴近上尉，钉满地图的墙在他身后被柔和压缩。第 3 段 84°，摄影机位于地图表面上方 1.1 米，越过灯向上拍，前景灯罩具有压迫感，两人和破损屋顶一直可见到画面边缘。

摄影 第 1 段胸口高度固定机位；第 2 段手持并保留摄影者呼吸，摄影机位于灯的阴影侧；第 3 段低位手持，缓慢上升越过灯焰。

动作时序 节拍 1——上校说出台词，手指用力到让地图产生折痕；灰泥粉尘穿过灯光漂浮。反打切至节拍 2——拍上尉；远处炮火闪光以蓝光扫过他的脸，脸颊肌肉抽动一下，他点一次头并抬眼。硬切至节拍 3——越过灯的低位广角；上尉扶正军帽、转身并从画面右侧走出。上校留下，用手压平有折痕的地图，门口穿堂风令灯焰倾斜。

物理 纸张在手指压力下形成并保持折痕；空气流动时灯焰弯曲后恢复，亮度随之下降；灰泥粉尘以真实沉降漂移落下；靴子踩过碎石时重量转移不均并发出砂砾声；羊毛军服带有潮湿重量且不鼓胀飘动。

灯光 主光为桌上动机明确、坚硬温暖的煤油灯，从下方照亮两张脸并使眼窝留在阴影中。辅光为穿过屋顶破洞、勾勒肩部的冷月光，以及间歇照亮后墙的远处炮火闪光。曝光以灯为准，允许阴影压黑；不加正面补光。

声音 远处炮击、野战电话嗡鸣、风穿过破损屋顶和滴水声。对白时环境声压低。镜头开始时上校准确说："天亮时，你带着现有的人和装备拿下那条路。" 没有其他对白或配乐；上尉嘴唇始终不动。

正向锁定 房间内恰好只有两名军官，不出现其他人。直到最后节拍上尉离开前，两人始终各自在桌子一侧。切镜间制服状态、泥污、灰泥粉尘和灯的位置完全一致。ARRI Alexa 35 拍摄的电影级写实影像，低饱和橄榄绿与琥珀色调，自然胶片颗粒。
```

#### 详细信息

- **生成参数：** `duration: 15s` · `resolution: 2560x1440` · `ratio: 16:9`
- **Tags：** `war-drama` `night` `three-segment` `dialogue` `community-tested`
- **来源类型：** 社区实测
- **来源：** [Alex Patrascu (@maxescu)](https://x.com/maxescu/status/2082563259782287522)
- **所属主帖：** [X thread](https://x.com/maxescu/status/2082563241062875568)
- **来源位置：** `reply`
- **发布时间：** 2026-07-29
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** The complete prompt appears in an author reply; the parent post says the displayed scenes were tried with MiniMax H3.

---


### H3-0027–H3-0048 · 一个原视频中的 2 段提示词

来源将这些案例发布在同一个合集视频中。视频只展示一次，对应的完整提示词依次列在下方。

#### 案例视频

[▶ 在视频页面播放](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-green-screen-to-fairytale-composite) · [↗ 查看仓库中的 MP4 文件](media/minimax-official-green-screen-to-fairytale-composite.mp4)

---

<a id="h3-0027"></a>

### H3-0027 · 绿幕转童话场景合成

**多模态参考生成** · **官方示例**

#### 内容说明

公开的 MiniMax H3“绿幕转童话场景合成”案例，包含原始提示词与对应成片。

#### 原始 Prompt

```text
Remove the green screen background of Video 1 and turn it into a fairy tale-like background similar to Video 2. The background elements need to completely match the actions of the characters in Video 1. Modify the lighting of the characters in Video 1 so that it completely matches the background.
```

#### 中文翻译

```text
移除视频 1 的绿幕背景，替换为与视频 2 相似的童话式背景。背景元素必须与视频 1 中人物的动作完全匹配。调整视频 1 中人物的光照，使其与新背景完全一致。
```

#### 详细信息

- **生成参数：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **来源类型：** 官方示例
- **来源：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **来源位置：** `page`
- **发布时间：** 2026-07-31
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0048"></a>

### H3-0048 · 绿幕环境替换

**多模态参考生成** · **官方示例**

#### 内容说明

公开的 MiniMax H3“绿幕环境替换”案例，包含原始提示词与对应成片。

#### 原始 Prompt

```text
Remove the green-screen background from Video 1 and replace it with a fairy-tale environment similar to Video 2. Make every background element respond correctly to the subject’s movement, and relight the subject so they blend naturally into the new scene.
```

#### 中文翻译

```text
移除视频 1 的绿幕背景，替换为与视频 2 相似的童话环境。让所有背景元素正确响应主体的动作，并重新调整主体光照，使其自然融入新场景。
```

#### 详细信息

- **生成参数：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **来源类型：** 官方示例
- **来源：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **来源位置：** `page`
- **发布时间：** 2026-07-31
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---



## 全部提示词

## 文生视频

*上方合集中的相关提示词:* [H3-0006](#h3-0006) · [H3-0007](#h3-0007) · [H3-0012](#h3-0012) · [H3-0013](#h3-0013) · [H3-0015](#h3-0015) · [H3-0016](#h3-0016)

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

#### 案例视频

[▶ 在视频页面播放](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-text-to-video) · [↗ 查看仓库中的 MP4 文件](media/minimax-official-text-to-video.mp4)

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

<a id="h3-0018"></a>

### H3-0018 · 厨房里的手绘发光生物

**文生视频** · **社区实测** · ⭐ Featured

#### 内容说明

将真人手机影像与手绘发光动画融合的纯文本生成案例。

#### 原始 Prompt

```text
15 seconds, 16:9 landscape. Blend live-action footage of a small kitchen at dusk with hand-drawn luminous animation. The last sunset light lingers at the window. The lived-in kitchen contains an old wooden table, a half-washed mug, a lightly fogged glass bottle, and a hanging dish towel.

Shoot as if someone is filming one-handed on a phone: subtle hand tremor, hesitant close-focus pulls, backlit exposure breathing, and slightly coarse noise in the shadows. It should feel like an astonishing event captured in a rush at home, not a carefully dressed commercial.

Do not show giant eyes, split mouths, fangs, threatening behavior, lunges, sudden black frames, or jump scares. Use only room tone, cloth friction, a soft mug clink, faucet drips, the camera operator’s footsteps and quiet breathing, plus gentle electronic tones and tiny vocalizations from the drawn creatures.
```

#### 中文翻译

```text
15 秒，16:9 横屏。把黄昏小厨房的真人影像与手绘发光动画融合。最后一缕夕阳停留在窗边；有人生活痕迹的厨房里有旧木桌、洗到一半的杯子、轻微起雾的玻璃瓶和悬挂的抹布。

像有人单手用手机拍摄：轻微手抖、犹豫的近距离拉焦、逆光下的曝光呼吸，以及阴影中略粗糙的噪点。画面应像在家匆忙捕捉到不可思议的事件，而不是精心布置的广告。

不要出现巨眼、裂口、尖牙、威胁行为、猛扑、突然黑帧或惊吓镜头。声音仅包括室内底噪、布料摩擦、杯子轻响、水龙头滴水、拍摄者脚步和轻微呼吸，以及温柔电子音与手绘生物细小的叫声。
```

#### 案例视频

[▶ 在视频页面播放](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-fal-hand-drawn-kitchen-creature) · [↗ 查看仓库中的 MP4 文件](media/fal-hand-drawn-kitchen-creature.mp4)

#### 详细信息

- **生成参数：** `duration: 15s` · `resolution: 2K` · `ratio: 16:9`
- **Tags：** `hand-drawn` `live-action` `phone-camera` `native-audio` `community-tested`
- **来源类型：** 社区实测
- **来源：** [Bennett Heyn / fal](https://fal.ai/learn/devs/minimax-h3-prompting-guide)
- **来源位置：** `page`
- **发布时间：** 2026-07-30
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** Published by fal as a text-to-video MiniMax H3 example with the result visible.

---

<a id="h3-0025"></a>

### H3-0025 · 霓虹洗衣店邂逅

**文生视频** · **官方示例**

#### 内容说明

公开的 MiniMax H3“霓虹洗衣店邂逅”案例，包含原始提示词与对应成片。

#### 原始 Prompt

```text
15 seconds, 16:9 landscape. Combine a live-action late-night laundromat with hand-drawn luminous animation. The small self-service laundromat has gently flickering fluorescent lights, running washers, plastic baskets, a worn bench, and one sock on the floor. Keep the space quiet and faintly nostalgic.

Use a one-handed phone-camera feel with visible shake, exposure fluctuation under white fluorescent light, environmental reflections in glass, and delayed autofocus at close range. Avoid polished commercial composition; it should feel like an authentic late-night encounter, filmed while following a strange apparition.
```

#### 中文翻译

```text
15 秒，16:9 横屏。将深夜自助洗衣店的真人实拍与手绘发光动画结合。小型自助洗衣店内，荧光灯轻微闪烁，洗衣机正在运转，散落着塑料筐、旧长凳，地上还有一只袜子。空间保持安静，略带怀旧感。

采用单手持手机拍摄的感觉，保留明显抖动、白色荧光灯下的曝光波动、玻璃上的环境反射，以及近距离拍摄时稍显迟缓的自动对焦。避免精致的商业构图；画面应像在跟随一个奇异幻影时偶然拍到的真实深夜邂逅。
```

#### 案例视频

[▶ 在视频页面播放](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-neon-laundromat-encounter) · [↗ 查看仓库中的 MP4 文件](media/minimax-official-neon-laundromat-encounter.mp4)

#### 详细信息

- **生成参数：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `text-to-video` `official`
- **来源类型：** 官方示例
- **来源：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **来源位置：** `page`
- **发布时间：** 2026-07-31
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

## 图生视频

*上方合集中的相关提示词:* [H3-0014](#h3-0014)

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

#### 案例视频

[▶ 在视频页面播放](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-first-last-frame) · [↗ 查看仓库中的 MP4 文件](media/minimax-official-first-last-frame.mp4)

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

<a id="h3-0022"></a>

### H3-0022 · 史诗太空歌剧预告片

**首尾帧生视频** · **官方示例**

#### 内容说明

公开的 MiniMax H3“史诗太空歌剧预告片”案例，包含原始提示词与对应成片。

#### 原始 Prompt

```text
Epic theatrical space-opera teaser

Keep the pace fast and the scale enormous without letting the edit drag. Use sharp hard cuts, a shaking command deck, white-hot flashes, split-second black frames, and a violent jump-to-warp impact. Title cards should use wide-tracked cinematic typography—not pure white—with restrained material texture, subtle illumination, and a faint edge glow. Animate the titles by emerging from deep-space shadow, catching a sweep of starlight, opening their letter spacing, leaving a slight afterimage, and flashing briefly against black.
```

#### 中文翻译

```text
史诗级院线太空歌剧预告片

保持快速节奏和宏大尺度，不要让剪辑拖沓。使用凌厉的硬切、剧烈震动的指挥舱、炽白闪光、转瞬即逝的黑场，以及猛烈跃迁至曲速的冲击。标题卡使用宽字距的电影字体——不要用纯白色——配合克制的材质纹理、轻微照明和淡淡的边缘辉光。标题动画从深空阴影中浮现，掠过一束星光，逐渐拉开字距，留下轻微残影，并在黑场上短暂闪现。
```

#### 案例视频

[▶ 在视频页面播放](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-epic-space-opera-teaser) · [↗ 查看仓库中的 MP4 文件](media/minimax-official-epic-space-opera-teaser.mp4)

#### 详细信息

- **生成参数：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `first-last-frame` `official`
- **来源类型：** 官方示例
- **来源：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **来源位置：** `page`
- **发布时间：** 2026-07-31
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0028"></a>

### H3-0028 · 动态画廊海报

**首尾帧生视频** · **官方示例**

#### 内容说明

公开的 MiniMax H3“动态画廊海报”案例，包含原始提示词与对应成片。

#### 原始 Prompt

```text
Animate the source artwork as a motion poster while preserving its white gallery border, inner frame, red/white/black palette, 3D collectible-figure look, and original layout. Add a light, playful type-on sound whenever text appears.
```

#### 中文翻译

```text
将源艺术作品制作成动态海报，同时保留白色画廊边框、内框、红白黑配色、3D 收藏级人偶质感和原始版式。每当文字出现时，加入轻快俏皮的打字音效。
```

#### 案例视频

[▶ 在视频页面播放](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-animated-gallery-poster) · [↗ 查看仓库中的 MP4 文件](media/minimax-official-animated-gallery-poster.mp4)

#### 详细信息

- **生成参数：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `first-last-frame` `official`
- **来源类型：** 官方示例
- **来源：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **来源位置：** `page`
- **发布时间：** 2026-07-31
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0033"></a>

### H3-0033 · 汽车网站 UI 动效

**首尾帧生视频** · **官方示例**

#### 内容说明

公开的 MiniMax H3“汽车网站 UI 动效”案例，包含原始提示词与对应成片。

#### 原始 Prompt

```text
Animate the website UI: the top headline slides down into place, the copy panel below slides up, and the car’s lights shift from dark to red.
```

#### 中文翻译

```text
为网站 UI 制作动画：顶部标题向下滑入定位，下方文案面板向上滑入，汽车灯光从暗色变为红色。
```

#### 案例视频

[▶ 在视频页面播放](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-automotive-website-ui-animation) · [↗ 查看仓库中的 MP4 文件](media/minimax-official-automotive-website-ui-animation.mp4)

#### 详细信息

- **生成参数：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `first-last-frame` `official`
- **来源类型：** 官方示例
- **来源：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **来源位置：** `page`
- **发布时间：** 2026-07-31
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0034"></a>

### H3-0034 · 旋转产品页面揭幕

**首尾帧生视频** · **官方示例**

#### 内容说明

公开的 MiniMax H3“旋转产品页面揭幕”案例，包含原始提示词与对应成片。

#### 原始 Prompt

```text
Reveal the layout from top to bottom. Upper and center typography slides down; lower typography slides up. Once the central product appears, let it rotate subtly.
```

#### 中文翻译

```text
从上到下揭示页面布局。上方和中部文字向下滑入，下方文字向上滑入。中央产品出现后，让它轻微旋转。
```

#### 案例视频

[▶ 在视频页面播放](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-rotating-product-page-reveal) · [↗ 查看仓库中的 MP4 文件](media/minimax-official-rotating-product-page-reveal.mp4)

#### 详细信息

- **生成参数：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `first-last-frame` `official`
- **来源类型：** 官方示例
- **来源：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **来源位置：** `page`
- **发布时间：** 2026-07-31
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0035"></a>

### H3-0035 · 黏土动画熔岩峡谷飞跃

**首尾帧生视频** · **官方示例**

#### 内容说明

公开的 MiniMax H3“黏土动画熔岩峡谷飞跃”案例，包含原始提示词与对应成片。

#### 原始 Prompt

```text
Claymation. A fox sprints to the edge of a cliff and launches without hesitation, making a dramatic heroic leap in slow motion over an immense lava canyon. Midair, the camera races beneath the fox’s belly in a bold dynamic move, revealing the terrifying depth of the chasm and the fully extended motion of its clay body.
```

#### 中文翻译

```text
黏土动画。一只狐狸冲向悬崖边缘，毫不犹豫地起跳，以戏剧化的英雄式慢动作飞越巨大的熔岩峡谷。腾空时，摄影机以大胆的动态运动从狐狸腹部下方高速掠过，展现深不见底的峡谷和黏土身体完全舒展的动作。
```

#### 案例视频

[▶ 在视频页面播放](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-claymation-lava-canyon-leap) · [↗ 查看仓库中的 MP4 文件](media/minimax-official-claymation-lava-canyon-leap.mp4)

#### 详细信息

- **生成参数：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `first-last-frame` `official`
- **来源类型：** 官方示例
- **来源：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **来源位置：** `page`
- **发布时间：** 2026-07-31
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0038"></a>

### H3-0038 · 第一人称战术游戏画面

**首尾帧生视频** · **官方示例**

#### 内容说明

公开的 MiniMax H3“第一人称战术游戏画面”案例，包含原始提示词与对应成片。

#### 原始 Prompt

```text
Camera: first-person, eye level, handheld gameplay. Simulate a player operating a modern-warfare FPS, holding an assault rifle and advancing slowly around the perimeter of a military base. Move forward along a road beside cover, sweep the reticle across the passage ahead, pause to fire several rounds at a distant target, then continue pushing forward like authentic player-controlled footage.

Lighting: cool natural light across a modern military base, mixed with smoke and firelight. Keep the image photoreal and crisp, with AAA-quality weapons, materials, dust, and battlefield haze.

Camera movement: subtle player-driven sway while moving; begin with a slow advance, make small checks left and right, add light recoil when firing, then continue forward steadily.
```

#### 中文翻译

```text
摄影机：第一人称、眼平视角、手持式游戏画面。模拟玩家操作现代战争 FPS，手持突击步枪，在军事基地外围缓慢推进。沿掩体旁的道路前进，让准星扫过前方通道，停下向远处目标射击数发，然后像真实玩家操控画面一样继续向前推进。

光照：现代军事基地中的冷色自然光，与烟雾和火光混合。画面保持照片级真实和清晰，武器、材质、尘土与战场薄雾达到 AAA 游戏品质。

摄影机运动：移动时带轻微的玩家操控摇摆；开场缓慢前进，小幅左右查看，射击时加入轻微后坐力，随后稳定继续向前。
```

#### 案例视频

[▶ 在视频页面播放](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-first-person-tactical-gameplay) · [↗ 查看仓库中的 MP4 文件](media/minimax-official-first-person-tactical-gameplay.mp4)

#### 详细信息

- **生成参数：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `first-last-frame` `official`
- **来源类型：** 官方示例
- **来源：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **来源位置：** `page`
- **发布时间：** 2026-07-31
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0039"></a>

### H3-0039 · 互动乙游转场

**首尾帧生视频** · **官方示例**

#### 内容说明

公开的 MiniMax H3“互动乙游转场”案例，包含原始提示词与对应成片。

#### 原始 Prompt

```text
Interactive Otome Game

Use the first image as the exact opening frame and the second as the exact ending frame. Create a transition within a premium Chinese otome visual-novel interface, capturing an intimate backstage moment before and after a performance. Move naturally from “Choose to watch his performance” to “Han Xu reacts with intrigued interest after hearing the heroine.” Reveal UI copy, choices, and dialogue boxes with refined otome-game motion design. Keep transitions fluid and the romantic tension suggestive but restrained.
```

#### 中文翻译

```text
互动乙女游戏

将第一张图片作为精确起始帧，第二张图片作为精确结束帧。在高级中式乙女视觉小说界面中制作转场，呈现演出前后亲密的后台时刻。从“选择观看他的表演”自然过渡到“韩旭听到女主角的话后露出饶有兴趣的反应”。以精致的乙游动效呈现 UI 文案、选项和对话框。转场保持流畅，浪漫张力含蓄而克制。
```

#### 案例视频

[▶ 在视频页面播放](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-interactive-otome-game-transition) · [↗ 查看仓库中的 MP4 文件](media/minimax-official-interactive-otome-game-transition.mp4)

#### 详细信息

- **生成参数：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `first-last-frame` `official`
- **来源类型：** 官方示例
- **来源：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **来源位置：** `page`
- **发布时间：** 2026-07-31
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0054"></a>

### H3-0054 · 精准服装互换

**首尾帧生视频** · **官方示例**

#### 内容说明

公开的 MiniMax H3“精准服装互换”案例，包含原始提示词与对应成片。

#### 原始 Prompt

```text
Two magicians stand onstage facing the audience and perform a “swap” illusion. They wave their wands simultaneously and smoke rises. When it clears, their suit colors have exchanged: the magician on the left now wears white, and the one on the right now wears black. Their glove colors do not change. They bow; the red curtain closes behind them and gradually shifts from deep red to dark blue.
```

#### 中文翻译

```text
两名魔术师站在舞台上面向观众，表演“互换”魔术。他们同时挥动魔杖，烟雾升起。烟雾散去后，两人的西装颜色已经互换：左侧魔术师现在穿白色，右侧魔术师现在穿黑色。手套颜色不变。两人鞠躬；身后的红色幕布合拢，并逐渐从深红变为深蓝。
```

#### 案例视频

[▶ 在视频页面播放](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-precision-costume-swap) · [↗ 查看仓库中的 MP4 文件](media/minimax-official-precision-costume-swap.mp4)

#### 详细信息

- **生成参数：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `first-last-frame` `official`
- **来源类型：** 官方示例
- **来源：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **来源位置：** `page`
- **发布时间：** 2026-07-31
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

## 多模态参考生成

*上方合集中的相关提示词:* [H3-0027](#h3-0027) · [H3-0048](#h3-0048)

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

#### 案例视频

[▶ 在视频页面播放](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-reference) · [↗ 查看仓库中的 MP4 文件](media/minimax-official-reference.mp4)

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

#### 案例视频

[▶ 在视频页面播放](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-hitchcock-reference) · [↗ 查看仓库中的 MP4 文件](media/minimax-official-hitchcock-reference.mp4)

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

<a id="h3-0017"></a>

### H3-0017 · 复古望远镜品牌短片

**多模态参考生成** · **官方示例** · ⭐ Featured

#### 内容说明

使用四张参考图、固定双筒望远镜遮罩、焦点驱动文字和快速扫描转场的品牌短片。

#### 原始 Prompt

```text
Use Images 1–4 as sequential keyframes, seen through a vintage binocular viewfinder searching for the MINIMAX installation. Open out of focus with subtle handheld shake, then push in quickly and rack focus onto Image 1. Between keyframes, use fast binocular-scan transitions with whip movement, motion blur, optical smearing, and brief exposure flicker. Cut at peak blur, then settle and snap back into focus.

Keep the twin circular lens mask absolutely fixed throughout: identical position, scale, feathered black vignette, and edge softness, with no warping or drift. Only the image inside the mask may move.

In Image 2, let the fabric move gently in the wind while the MINIMAX lettering follows the folds and remains legible. In Image 3, the subject should feel like a stylish passerby caught by chance, walking, turning, and swinging their arms naturally. In Image 4, the subject adjusts their glasses or lifts their chin slightly with a cool, effortless fashion-campaign attitude.

Red typography should resolve with the focus: begin slightly blurred and at low opacity, then fade into clarity over 0.3–0.5 seconds. A subtle vertical slide or slight tracking expansion is allowed. Fade it out before the next transition or let motion blur carry it away. No spins, bounces, or large fly-ins/outs.

Visual language: a voyeuristic, Wes Anderson-inspired 35 mm film look with fine grain, soft highlight halation, restrained color, and red typographic accents. Minimal, premium, lightly playful. Do not add people, vehicles, buildings, or logos. Preserve the core composition and the MINIMAX installation exactly.
```

#### 中文翻译

```text
将图片 1–4 作为连续关键帧，通过复古双筒望远镜取景器寻找 MINIMAX 装置。开场失焦并带轻微手持抖动，随后快速推进并拉焦到图片 1。关键帧之间使用快速望远镜扫描转场：甩动、运动模糊、光学拖影与短暂曝光闪烁；在模糊峰值切镜，再稳定下来并迅速恢复清晰。

双圆镜片遮罩全程绝对固定：位置、比例、羽化黑色暗角和边缘柔度完全一致，不变形、不漂移；只有遮罩内部画面可以移动。

图片 2 中布料随风轻动，MINIMAX 字样跟随褶皱但保持可读。图片 3 中人物像偶然被捕捉的时髦路人，自然行走、转身和摆臂。图片 4 中人物调整眼镜或轻抬下巴，呈现冷静、不费力的时尚广告姿态。

红色文字随焦点显现：初始略虚且低透明度，在 0.3–0.5 秒内淡入清晰；可轻微垂直滑动或扩展字距。下次转场前淡出，或由运动模糊带走。不要旋转、弹跳或大幅飞入飞出。

视觉语言：带窥视感、受韦斯·安德森启发的 35mm 胶片质感，细颗粒、柔和高光晕染、克制色彩和红色文字点缀；极简、高级、略带俏皮。不要新增人物、车辆、建筑或标志；严格保留核心构图与 MINIMAX 装置。
```

#### 案例视频

[▶ 在视频页面播放](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-vintage-binocular-brand-film) · [↗ 查看仓库中的 MP4 文件](media/minimax-official-vintage-binocular-brand-film.mp4)

#### 详细信息

- **生成参数：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `brand-film` `multi-image` `typography` `transition` `official`
- **来源类型：** 官方示例
- **来源：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **来源位置：** `page`
- **发布时间：** 2026-07-31
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0019"></a>

### H3-0019 · 交互式游戏装备界面

**多模态参考生成** · **社区实测** · ⭐ Featured

#### 内容说明

一段详细的 15 秒时间轴 UI 序列，完成角色装备改造并加载赛博朋克世界。

#### 原始 Prompt

```text
Use Image 1 for the character and Image 2 for the UI style.

[0–2 seconds] High-angle overhead shot. The character sits on a vivid, highly saturated purple floor, looks up at camera, and matches Image 1. A game menu appears on the right: START NEW GAME, CONTINUE (highlighted), SETTINGS, EXIT GAME. Player profile MINIMAX appears top left. The cursor selects CONTINUE.

[2–4 seconds] Smoothly push in to her right arm. A RIGHT ARM EQUIPMENT panel slides in from the right. PHANTOM GRIP is selected, then the selection moves to CHRONOS CLAW. Her mechanical hand reconfigures: fingers separate, new claw-like joints lock into place, and cyan LEDs flare brighter.

[4–7 seconds] Arc smoothly to her left. An ARMAMENT CUSTOMIZATION grid slides in, showing hand, forearm, elbow, and upper-arm components. The selector cycles rapidly. Her left arm disassembles section by section: the forearm plate releases, new armor slides in, the elbow joint swaps, and the hand reconfigures, with exposed wiring and pistons visible during the change.

[7–8.5 seconds] Pull back to a medium shot. CONFIRM CONFIG flashes; click it. All UI panels collapse inward and vanish. She uncrosses her legs and settles into a relaxed seated pose with one knee raised, lifting the prosthetic hand for a subtle post-configuration movement.

[8.5–10 seconds] A LOADING bar appears along the bottom and races from 0% to 100%. The saturated purple environment darkens as shadows creep inward and warm golden light begins to bleed through.

[10–15 seconds] As she stands, the full world loads around her: a dense cyberpunk slum with flickering neon, rain-wet streets, moving crowds, passing motorcycles, tangled overhead cables, and stacked buildings stretching toward futuristic towers. Settle into a third-person camera behind her. HUD elements fade in: minimap top right, health and ammo bottom left, then a mission marker. She steps into the street.
```

#### 中文翻译

```text
图片 1 用于角色，图片 2 用于 UI 风格。

[0–2 秒] 高角度俯拍。角色坐在鲜艳高饱和紫色地面上，抬头看向摄影机并匹配图片 1。右侧出现菜单：START NEW GAME、CONTINUE（高亮）、SETTINGS、EXIT GAME；左上显示玩家档案 MINIMAX；光标选择 CONTINUE。

[2–4 秒] 平滑推进到她的右臂。RIGHT ARM EQUIPMENT 面板从右侧滑入，先选中 PHANTOM GRIP，再移动到 CHRONOS CLAW。机械手重构：手指分开，新的爪状关节锁定，青色 LED 变亮。

[4–7 秒] 平滑绕到她左侧。ARMAMENT CUSTOMIZATION 网格滑入，展示手、前臂、肘部和上臂组件，选择器快速循环。左臂逐段拆解：前臂装甲释放，新装甲滑入，肘关节替换，手部重构；变化过程中可见线路与活塞。

[7–8.5 秒] 拉回中景。CONFIRM CONFIG 闪烁并被点击；全部 UI 面板向内收拢消失。她解开盘腿，以单膝抬起的放松坐姿稳定下来，抬起义肢做轻微配置后动作。

[8.5–10 秒] 底部出现 LOADING 条，从 0% 快速到 100%。高饱和紫色环境逐渐变暗，阴影向内蔓延，暖金色光开始渗入。

[10–15 秒] 她站起时完整世界在周围加载：密集赛博朋克贫民区、闪烁霓虹、雨湿街道、移动人群、驶过的摩托车、纠缠电缆与层叠建筑，并延伸到未来高塔。摄影机稳定在她身后的第三人称视角。HUD 依次淡入：右上小地图、左下生命与弹药、任务标记。她迈步走入街道。
```

#### 案例视频

[▶ 在视频页面播放](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-fal-interactive-game-equipment-ui) · [↗ 查看仓库中的 MP4 文件](media/fal-interactive-game-equipment-ui.mp4)

#### 详细信息

- **生成参数：** `duration: 15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `game-ui` `timecoded` `typography` `cyberpunk` `community-tested`
- **来源类型：** 社区实测
- **来源：** [Bennett Heyn / fal](https://fal.ai/learn/devs/minimax-h3-prompting-guide)
- **来源位置：** `page`
- **发布时间：** 2026-07-30
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** Published by fal as a MiniMax H3 reference-to-video example with two reference images and the result visible.

---

<a id="h3-0020"></a>

### H3-0020 · 咖啡微距到沙漠的无缝转场

**多模态参考生成** · **社区实测** · ⭐ Featured

#### 内容说明

使用两张参考图，从咖啡微观材质连续匹配到沙漠景观。

#### 原始 Prompt

```text
@Image 1: Push in rapidly toward the milk foam, cocoa particles, and dark liquid texture on the coffee until particles, bubbles, and ripples fill the frame. Keep the macro photography realistic, with extremely shallow depth of field and fine powder drifting through backlight. Let the surface feel suspended between granular sand and fluid.

At the exact moment when the cocoa particles, foam contours, and coffee swirl closely resemble the dune ridges, wind-carved textures, and airborne sand in @Image 2, transition seamlessly into the desert landscape. Continue pushing forward until the full dunes from @Image 2 are revealed.

No tearing, black frames, hard cuts, obvious VFX, or compositing seams. Keep it photoreal, quiet, and restrained—as though one granular material naturally expands from the microscopic coffee surface into a vast desert. One continuous shot with no visible edit.
```

#### 中文翻译

```text
@图片 1：快速推进咖啡表面的奶泡、可可颗粒和深色液体纹理，直到颗粒、气泡和涟漪充满画面。保持真实微距摄影，极浅景深，细粉在逆光中漂浮；表面质感介于颗粒沙土与流体之间。

当可可颗粒、泡沫轮廓和咖啡旋涡与 @图片 2 的沙丘脊线、风蚀纹理和飞沙高度相似的精确时刻，无缝转入沙漠景观。继续向前推进，直到完整展现图片 2 的沙丘。

不要撕裂、黑帧、硬切、明显特效或合成接缝。保持写实、安静和克制，仿佛同一种颗粒材料从微观咖啡表面自然扩展成辽阔沙漠。单一连续镜头，不出现可见剪辑。
```

#### 案例视频

[▶ 在视频页面播放](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-fal-macro-coffee-desert-transition) · [↗ 查看仓库中的 MP4 文件](media/fal-macro-coffee-desert-transition.mp4)

#### 详细信息

- **生成参数：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `macro` `seamless-transition` `material-match` `multi-image` `community-tested`
- **来源类型：** 社区实测
- **来源：** [Bennett Heyn / fal](https://fal.ai/learn/devs/minimax-h3-prompting-guide)
- **来源位置：** `page`
- **发布时间：** 2026-07-30
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** Published by fal as a MiniMax H3 reference-to-video example with two reference images and the result visible.

---

<a id="h3-0021"></a>

### H3-0021 · 视频中猫替换为狗

**多模态参考生成** · **社区实测**

#### 内容说明

只改变一个主体、其余源视频保持稳定的极简局部编辑指令。

#### 原始 Prompt

```text
Replace the cat in the video with a dog.
```

#### 中文翻译

```text
将视频中的猫替换成狗。
```

#### 案例视频

[▶ 在视频页面播放](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-fal-cat-to-dog-replacement) · [↗ 查看仓库中的 MP4 文件](media/fal-cat-to-dog-replacement.mp4)

#### 详细信息

- **生成参数：** `duration: source dependent` · `resolution: 2K` · `ratio: adaptive`
- **Tags：** `video-editing` `subject-replacement` `localized-edit` `community-tested`
- **来源类型：** 社区实测
- **来源：** [Bennett Heyn / fal](https://fal.ai/learn/devs/minimax-h3-prompting-guide)
- **来源位置：** `page`
- **发布时间：** 2026-07-30
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** Published by fal as a precise MiniMax H3 video-editing example with the source and result visible.

---

<a id="h3-0023"></a>

### H3-0023 · 沙漠时尚广告片

**多模态参考生成** · **官方示例**

#### 内容说明

公开的 MiniMax H3“沙漠时尚广告片”案例，包含原始提示词与对应成片。

#### 原始 Prompt

```text
Create a premium 16:9 landscape fashion film. Use Image 1 for the overall mood, location, and film texture; Image 2 for the talent; Image 3 for the bag; and Image 4 for the closing brand mark. This is a fashion campaign for the clothing and bag. The tone is elevated, cool, and restrained, but the edit should still feel lively and fashion-forward—not like a conventional narrative film or an e-commerce ad.

Keep the story simple: beside a vintage car on a desert highway, a woman walks to the rear of the car, opens the trunk, takes out a black bag, shares a quiet beat with the man standing nearby, then leaves carrying the bag. Integrate the clothing and bag naturally into the performance so they feel like part of the characters’ identity.
```

#### 中文翻译

```text
制作一支高级的 16:9 横屏时尚短片。图片 1 用于整体情绪、地点和胶片质感；图片 2 用于人物；图片 3 用于包袋；图片 4 用于片尾品牌标识。这是一支服装与包袋的时尚广告。基调高级、冷静、克制，但剪辑仍应活跃且具时尚前瞻性——不要拍成传统叙事电影或电商广告。

故事保持简单：在沙漠公路的一辆老爷车旁，一位女子走到车尾，打开后备厢，取出一个黑色包袋，与站在旁边的男子安静对视片刻，随后提包离开。让服装和包袋自然融入表演，使其成为角色身份的一部分。
```

#### 案例视频

[▶ 在视频页面播放](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-desert-fashion-campaign) · [↗ 查看仓库中的 MP4 文件](media/minimax-official-desert-fashion-campaign.mp4)

#### 详细信息

- **生成参数：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **来源类型：** 官方示例
- **来源：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **来源位置：** `page`
- **发布时间：** 2026-07-31
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0024"></a>

### H3-0024 · 赛博垃圾摇滚时尚短片

**多模态参考生成** · **官方示例**

#### 内容说明

公开的 MiniMax H3“赛博垃圾摇滚时尚短片”案例，包含原始提示词与对应成片。

#### 原始 Prompt

```text
Use Image 1 as the reference for texture and mood, and Image 2 for the subject’s appearance. Generate a 15-second, 16:9 fashion short. Preserve the subject’s identity: long platinum-blonde hair, narrow black vintage sunglasses, a glossy black patent-leather trench coat, a cool, self-assured expression, and orange firelight reflected across the coat.

Style: fast-cut fashion film on analog stock, set against a nighttime blaze with black smoke and orange-red flames. Layer in VHS glitches, CCTV signal interruptions, 1990s film grain, scanlines, chromatic aberration, light leaks, flash-to-white transitions, and subtle frame jitter.
```

#### 中文翻译

```text
图片 1 作为质感与情绪参考，图片 2 作为人物外观参考。生成一支 15 秒、16:9 的时尚短片。保持人物身份一致：铂金色长发、窄框黑色复古太阳镜、亮面黑色漆皮风衣、冷酷自信的表情，以及映在风衣上的橙色火光。

风格：使用模拟胶片质感的快速剪辑时尚片，背景是夜间大火、黑烟和橙红色火焰。叠加 VHS 故障、监控信号中断、20 世纪 90 年代胶片颗粒、扫描线、色差、漏光、闪白转场和轻微画面抖动。
```

#### 案例视频

[▶ 在视频页面播放](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-cyber-grunge-fashion-film) · [↗ 查看仓库中的 MP4 文件](media/minimax-official-cyber-grunge-fashion-film.mp4)

#### 详细信息

- **生成参数：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **来源类型：** 官方示例
- **来源：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **来源位置：** `page`
- **发布时间：** 2026-07-31
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0026"></a>

### H3-0026 · 赛博垃圾摇滚说唱 MV

**多模态参考生成** · **官方示例**

#### 内容说明

公开的 MiniMax H3“赛博垃圾摇滚说唱 MV”案例，包含原始提示词与对应成片。

#### 原始 Prompt

```text
Style: dark-pop / cyber-grunge / rap music video with photoreal high-fashion polish and the texture of a scanned film magazine—high contrast without looking cheap. Reference late-1990s to early-2000s indie magazines, photocopies, film scans, underground-music posters, and zine collage. Add coarse grain, subtle gate weave, halftone dots, rough print edges, and slight scan misregistration. Keep the edit fast and use hard cuts only—no fades or soft transitions. Match the typographic treatment and surface texture of the reference images.
```

#### 中文翻译

```text
风格：暗黑流行／赛博垃圾摇滚／说唱音乐录像，兼具照片级高定时尚质感和扫描电影杂志的纹理——高对比但不廉价。参考 20 世纪 90 年代末至 21 世纪初的独立杂志、复印件、胶片扫描、地下音乐海报和 zine 拼贴。加入粗颗粒、轻微片门晃动、半色调网点、粗糙印刷边缘和轻微扫描套印偏移。保持快速剪辑，只使用硬切——不要淡入淡出或柔和转场。文字处理和表面质感要与参考图片一致。
```

#### 案例视频

[▶ 在视频页面播放](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-cyber-grunge-rap-music-video) · [↗ 查看仓库中的 MP4 文件](media/minimax-official-cyber-grunge-rap-music-video.mp4)

#### 详细信息

- **生成参数：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **来源类型：** 官方示例
- **来源：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **来源位置：** `page`
- **发布时间：** 2026-07-31
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0029"></a>

### H3-0029 · 竖屏家庭冲突短剧

**多模态参考生成** · **官方示例**

#### 内容说明

公开的 MiniMax H3“竖屏家庭冲突短剧”案例，包含原始提示词与对应成片。

#### 原始 Prompt

```text
A 9:16 vertical family-confrontation scene with grounded live-action performances, set in a Chinese family home or small restaurant. Use warm interior light, red decorations and calligraphy in the background, shallow depth of field, intense emotion, and tight pacing.

Performance: natural short-form drama, never theatrical. Qin Haoxuan argues back with anger, hurt, and urgency. The older woman questions him in a sharp, forceful, relentless tone. Build the confrontation steadily.

Shoot mainly in medium-close shots with frequent shot/reverse-shot cutting. Keep the setting lived-in and realistic. No sci-fi, period costume, or animation styling. Do not show subtitles, added text, platform watermarks, or stickers.
```

#### 中文翻译

```text
一段 9:16 竖屏家庭冲突场景，采用真实自然的真人表演，发生在中国家庭住宅或小餐馆中。使用温暖室内光，背景带红色装饰和书法，浅景深、强烈情绪与紧凑节奏。

表演：自然的短剧风格，绝不舞台化。秦昊轩带着愤怒、受伤和急迫进行反驳。年长女性以尖锐、强势、步步紧逼的语气质问他，冲突逐步升级。

主要使用中近景，并频繁进行正反打剪辑。环境要有真实生活气息。不要科幻、古装或动画风格。不要出现字幕、额外文字、平台水印或贴纸。
```

#### 案例视频

[▶ 在视频页面播放](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-vertical-family-confrontation) · [↗ 查看仓库中的 MP4 文件](media/minimax-official-vertical-family-confrontation.mp4)

#### 详细信息

- **生成参数：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **来源类型：** 官方示例
- **来源：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **来源位置：** `page`
- **发布时间：** 2026-07-31
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0030"></a>

### H3-0030 · 未来感眼镜广告

**多模态参考生成** · **官方示例**

#### 内容说明

公开的 MiniMax H3“未来感眼镜广告”案例，包含原始提示词与对应成片。

#### 原始 Prompt

```text
Create a premium 9:16 fashion-eyewear commercial. Match the reference video’s shot rhythm, edit speed, white-cyclorama look, and severe fashion attitude. Use a seamless minimal white studio with clean, bold, avant-garde art direction worthy of a global luxury campaign.

Use Image 1 for the key visual: two full-body female models, one Black and one white, preserving their elevated wardrobe, body language, studio lighting, runway presence, and cool attitude. Use Image 2 for facial details. Both models wear futuristic luxury eyewear based on Image 3: wraparound curved lenses, a sharp cat-eye/goggle hybrid silhouette, mirrored reflections, streamlined temples, and the finish of a premium fashion accessory.
```

#### 中文翻译

```text
制作一支高级 9:16 时尚眼镜广告。匹配参考视频的镜头节奏、剪辑速度、白色无缝背景效果和凌厉时尚态度。使用极简无缝白棚，并配以干净、大胆、前卫、足以匹配全球奢侈品牌广告的艺术指导。

图片 1 作为主视觉：两位全身女性模特，一位黑人、一位白人，保留她们的高级服装、肢体语言、影棚灯光、T 台气场和冷峻态度。图片 2 用于面部细节。两位模特都佩戴基于图片 3 的未来奢华眼镜：环绕式弧形镜片、锐利的猫眼与护目镜混合轮廓、镜面反射、流线型镜腿，以及高级时尚配饰的精致表面。
```

#### 案例视频

[▶ 在视频页面播放](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-futuristic-eyewear-campaign) · [↗ 查看仓库中的 MP4 文件](media/minimax-official-futuristic-eyewear-campaign.mp4)

#### 详细信息

- **生成参数：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **来源类型：** 官方示例
- **来源：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **来源位置：** `page`
- **发布时间：** 2026-07-31
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0031"></a>

### H3-0031 · 人体工学椅产品短片

**多模态参考生成** · **官方示例**

#### 内容说明

公开的 MiniMax H3“人体工学椅产品短片”案例，包含原始提示词与对应成片。

#### 原始 Prompt

```text
Product Feature Visualization

Present a black Herman Miller ergonomic chair in a premium office with a full 360-degree product reveal. Cut to macro views of the breathable mesh back with airflow visualization, an engineering animation of the lumbar support and ergonomic curve, and demonstrations of multidirectional armrest and seat-height adjustment. Show designers, developers, and creative professionals working comfortably over long sessions. Include a 3D skeletal-support visualization that communicates all-day comfort, plus refined interior styling. End with the line: “WHERE INSPIRATION MEETS COMFORT.” Keep the direction minimal, cool-toned, professional, futuristic, and slow-paced. Use Image 1 for feature details and Image 2 for the product.
```

#### 中文翻译

```text
产品功能可视化

在高级办公空间中展示一把黑色 Herman Miller 人体工学椅，并完成 360 度产品展示。切至透气网布椅背的微距镜头并可视化气流；展示腰部支撑和人体工学曲线的工程动画；演示多方向扶手和座椅高度调节。呈现设计师、开发者和创意专业人士长时间舒适工作的状态。加入 3D 骨骼支撑可视化，传达全天候舒适性，并搭配精致的室内设计。片尾显示：“WHERE INSPIRATION MEETS COMFORT.” 整体方向极简、冷色、专业、未来感且节奏舒缓。图片 1 用于功能细节，图片 2 用于产品。
```

#### 案例视频

[▶ 在视频页面播放](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-ergonomic-chair-product-film) · [↗ 查看仓库中的 MP4 文件](media/minimax-official-ergonomic-chair-product-film.mp4)

#### 详细信息

- **生成参数：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **来源类型：** 官方示例
- **来源：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **来源位置：** `page`
- **发布时间：** 2026-07-31
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0032"></a>

### H3-0032 · Nike 风格产品落地页

**多模态参考生成** · **官方示例**

#### 内容说明

公开的 MiniMax H3“Nike 风格产品落地页”案例，包含原始提示词与对应成片。

#### 原始 Prompt

```text
Create a dynamic product-landing-page UI/UX demo inspired by Nike’s digital language, built around the product in Image 1. Use oversized, bold, italicized sans-serif typography and backgrounds that combine speed-driven light streaks with dark carbon fiber or breathable performance-mesh textures. Show a smooth, fast, powerful scroll through the page, plus high-impact hover interactions with scale-ups and color inversion.
```

#### 中文翻译

```text
围绕图片 1 中的产品，制作一个受 Nike 数字视觉语言启发的动态产品落地页 UI/UX 演示。使用超大、粗体、斜体无衬线字体，背景结合强调速度的光轨与深色碳纤维或透气运动网布纹理。展示流畅、快速、有力量的页面滚动，并加入高冲击力的悬停交互，如放大和颜色反转。
```

#### 案例视频

[▶ 在视频页面播放](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-nike-style-product-landing-page) · [↗ 查看仓库中的 MP4 文件](media/minimax-official-nike-style-product-landing-page.mp4)

#### 详细信息

- **生成参数：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **来源类型：** 官方示例
- **来源：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **来源位置：** `page`
- **发布时间：** 2026-07-31
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0036"></a>

### H3-0036 · 仙侠角色短片

**多模态参考生成** · **官方示例**

#### 内容说明

公开的 MiniMax H3“仙侠角色短片”案例，包含原始提示词与对应成片。

#### 原始 Prompt

```text
Use Image 2 as the locked character reference. Preserve the half-up long black hair, openwork silver crown, indigo ribbon, layered pale hanfu, translucent blue outer robe, deep-blue sash, silver floral fastener, and long tassels. Use Image 1 for storyboard order and pacing.

Render in high-quality 4K, 16:9 Chinese-inspired 3D with cinematic xianxia production value: intense, solemn, and shaped by destiny. Follow the storyboard beat by beat, with natural camera movement and seamless transitions—never a slideshow. Show the face only in close-up or extreme close-up. In wide shots, use back view, rear three-quarter view, or empty environment shots; never show a distant frontal face.
```

#### 中文翻译

```text
将图片 2 作为锁定的角色参考。保留半束的黑色长发、镂空银冠、靛蓝发带、层叠浅色汉服、半透明蓝色外袍、深蓝腰带、银色花形扣件和长流苏。图片 1 用于分镜顺序和节奏。

以高质量 4K、16:9 的中式 3D 风格呈现，具备电影级仙侠制作水准：强烈、庄重，并带有宿命感。逐拍遵循分镜，摄影机运动自然、转场无缝——绝不能像幻灯片。仅在近景或特写中展示面部。远景使用背面、后侧三分之四视角或空镜；不要在远处展示正脸。
```

#### 案例视频

[▶ 在视频页面播放](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-fantasy-wuxia-character-film) · [↗ 查看仓库中的 MP4 文件](media/minimax-official-fantasy-wuxia-character-film.mp4)

#### 详细信息

- **生成参数：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **来源类型：** 官方示例
- **来源：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **来源位置：** `page`
- **发布时间：** 2026-07-31
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0037"></a>

### H3-0037 · 乙游男主角色宣传片

**多模态参考生成** · **官方示例**

#### 内容说明

公开的 MiniMax H3“乙游男主角色宣传片”案例，包含原始提示词与对应成片。

#### 原始 Prompt

```text
Create a character promo for a male lead in an otome game. Use Image 2 as a strict identity reference. Preserve the same face, hairstyle, body proportions, costume design, material detail, and polished otome-CG aesthetic throughout.
```

#### 中文翻译

```text
为乙女游戏中的男性主角制作角色宣传片。将图片 2 作为严格的身份参考。全程保持相同的面容、发型、身体比例、服装设计、材质细节和精致的乙游 CG 美学。
```

#### 案例视频

[▶ 在视频页面播放](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-otome-male-lead-character-promo) · [↗ 查看仓库中的 MP4 文件](media/minimax-official-otome-male-lead-character-promo.mp4)

#### 详细信息

- **生成参数：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **来源类型：** 官方示例
- **来源：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **来源位置：** `page`
- **发布时间：** 2026-07-31
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0040"></a>

### H3-0040 · 多素材电影感重混

**多模态参考生成** · **官方示例**

#### 内容说明

公开的 MiniMax H3“多素材电影感重混”案例，包含原始提示词与对应成片。

#### 原始 Prompt

```text
Use Images 1–6 as assets. Match Reference Video 1 closely for shot rhythm, transition language, and music.
```

#### 中文翻译

```text
使用图片 1–6 作为素材。紧密匹配参考视频 1 的镜头节奏、转场语言和音乐。
```

#### 案例视频

[▶ 在视频页面播放](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-multi-asset-cinematic-remix) · [↗ 查看仓库中的 MP4 文件](media/minimax-official-multi-asset-cinematic-remix.mp4)

#### 详细信息

- **生成参数：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **来源类型：** 官方示例
- **来源：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **来源位置：** `page`
- **发布时间：** 2026-07-31
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0041"></a>

### H3-0041 · 真人场景体素化变换

**多模态参考生成** · **官方示例**

#### 内容说明

公开的 MiniMax H3“真人场景体素化变换”案例，包含原始提示词与对应成片。

#### 原始 Prompt

```text
Preserve the buildings, pedestrians, and overall environment in Video 1 as photoreal live action. Transform only the trees and cars into 3D pixel-art or voxel-block objects in the style of Minecraft, using Image 1 as the visual reference. Keep their motion physically correct, and preserve the real environment’s shadows and transmitted light. Use Video 2 as the overall target.
```

#### 中文翻译

```text
保留视频 1 中的建筑、行人和整体环境为照片级真人实拍。仅将树木和汽车转换为《我的世界》风格的 3D 像素艺术或体素方块物体，并使用图片 1 作为视觉参考。保持它们的运动符合物理规律，同时保留真实环境中的阴影和透射光。视频 2 作为整体目标参考。
```

#### 案例视频

[▶ 在视频页面播放](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-live-action-voxel-transformation) · [↗ 查看仓库中的 MP4 文件](media/minimax-official-live-action-voxel-transformation.mp4)

#### 详细信息

- **生成参数：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **来源类型：** 官方示例
- **来源：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **来源位置：** `page`
- **发布时间：** 2026-07-31
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0042"></a>

### H3-0042 · 角色替换与表演参考

**多模态参考生成** · **官方示例**

#### 内容说明

公开的 MiniMax H3“角色替换与表演参考”案例，包含原始提示词与对应成片。

#### 原始 Prompt

```text
Match the character motion, expressions, and performance timing in Image 1 closely to Input Video 1.

At the sink on the right side of frame, the man hands a washed plate to the woman on the left. He turns, then suddenly flicks dish-soap foam at her with his right hand. Startled, she immediately retaliates. They laugh, dodge, and playfully throw foam back and forth.
```

#### 中文翻译

```text
让图片 1 中角色的动作、表情和表演节奏紧密匹配输入视频 1。

画面右侧水槽旁，男子把洗好的盘子递给左侧女子。他转身后突然用右手把洗洁精泡沫弹向她。她被吓到后立即反击。两人一边大笑、一边躲闪，玩闹着互相抛洒泡沫。
```

#### 案例视频

[▶ 在视频页面播放](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-character-swap-with-performance-reference) · [↗ 查看仓库中的 MP4 文件](media/minimax-official-character-swap-with-performance-reference.mp4)

#### 详细信息

- **生成参数：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **来源类型：** 官方示例
- **来源：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **来源位置：** `page`
- **发布时间：** 2026-07-31
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0043"></a>

### H3-0043 · 街舞动作迁移

**多模态参考生成** · **官方示例**

#### 内容说明

公开的 MiniMax H3“街舞动作迁移”案例，包含原始提示词与对应成片。

#### 原始 Prompt

```text
Use Video 1 as the motion reference for a street-dance performance. Use Images 1 and 2 as the character references.
```

#### 中文翻译

```text
使用视频 1 作为街舞表演的动作参考。使用图片 1 和图片 2 作为角色参考。
```

#### 案例视频

[▶ 在视频页面播放](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-street-dance-motion-transfer) · [↗ 查看仓库中的 MP4 文件](media/minimax-official-street-dance-motion-transfer.mp4)

#### 详细信息

- **生成参数：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **来源类型：** 官方示例
- **来源：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **来源位置：** `page`
- **发布时间：** 2026-07-31
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0044"></a>

### H3-0044 · 水豚动作复现

**多模态参考生成** · **官方示例**

#### 内容说明

公开的 MiniMax H3“水豚动作复现”案例，包含原始提示词与对应成片。

#### 原始 Prompt

```text
Motion reference for a DIY reaction clip

Match the action in Video 1 from a locked-off wide camera. Replace the three suited men with three highly photoreal capybaras. Preserve the original movement path exactly: all three drop quickly to the floor; the left capybara jumps to center; the center capybara rolls to the far left; the new center capybara rolls to the far right; the right capybara jumps to center; finally, the center capybara jumps onto the other two, forming a pyramid. Keep the camera fixed and integrate fur, lighting, and shadows realistically into the scene.
```

#### 中文翻译

```text
DIY 反应短片的动作参考

使用固定广角机位匹配视频 1 中的动作。将三名穿西装的男子替换为三只高度照片级真实的水豚。精确保留原始运动路径：三只水豚同时快速趴到地面；左侧水豚跳到中央；中央水豚滚到最左侧；新的中央水豚滚到最右侧；右侧水豚跳到中央；最后中央水豚跳到另外两只上方，叠成金字塔。保持摄影机固定，并让毛发、光照和阴影真实融入场景。
```

#### 案例视频

[▶ 在视频页面播放](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-capybara-motion-recreation) · [↗ 查看仓库中的 MP4 文件](media/minimax-official-capybara-motion-recreation.mp4)

#### 详细信息

- **生成参数：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **来源类型：** 官方示例
- **来源：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **来源位置：** `page`
- **发布时间：** 2026-07-31
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0045"></a>

### H3-0045 · 声音克隆对白迁移

**多模态参考生成** · **官方示例**

#### 内容说明

公开的 MiniMax H3“声音克隆对白迁移”案例，包含原始提示词与对应成片。

#### 原始 Prompt

```text
The character says: “Follow the wind, live free. Leave worries behind, enjoy the moment.” Match the voice in Audio 1.
```

#### 中文翻译

```text
角色说道：“逐风而行，自在而活。抛开烦恼，享受当下。”声音匹配音频 1。
```

#### 案例视频

[▶ 在视频页面播放](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-voice-clone-dialogue-transfer) · [↗ 查看仓库中的 MP4 文件](media/minimax-official-voice-clone-dialogue-transfer.mp4)

#### 详细信息

- **生成参数：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **来源类型：** 官方示例
- **来源：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **来源位置：** `page`
- **发布时间：** 2026-07-31
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0046"></a>

### H3-0046 · 添加与群体同步的角色

**多模态参考生成** · **官方示例**

#### 内容说明

公开的 MiniMax H3“添加与群体同步的角色”案例，包含原始提示词与对应成片。

#### 原始 Prompt

```text
Add one person on the left side of frame wearing the same team uniform and moving in sync with the others.
```

#### 中文翻译

```text
在画面左侧添加一个人，穿着与其他人相同的队服，并与其他人同步运动。
```

#### 案例视频

[▶ 在视频页面播放](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-add-a-character-in-sync-with-the-others) · [↗ 查看仓库中的 MP4 文件](media/minimax-official-add-a-character-in-sync-with-the-others.mp4)

#### 详细信息

- **生成参数：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **来源类型：** 官方示例
- **来源：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **来源位置：** `page`
- **发布时间：** 2026-07-31
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0047"></a>

### H3-0047 · 主体与服装精准替换

**多模态参考生成** · **官方示例**

#### 内容说明

公开的 MiniMax H3“主体与服装精准替换”案例，包含原始提示词与对应成片。

#### 原始 Prompt

```text
Precise Subject and Wardrobe Replacement

Replace the child at the back of Video 1 with the golden retriever from Image 1. Replace the khaki jacket worn by the child on the far left with the denim jacket from Image 2.
```

#### 中文翻译

```text
精准主体与服装替换

将视频 1 后方的儿童替换为图片 1 中的金毛犬。将最左侧儿童穿的卡其色夹克替换为图片 2 中的牛仔夹克。
```

#### 案例视频

[▶ 在视频页面播放](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-subject-wardrobe-replacement) · [↗ 查看仓库中的 MP4 文件](media/minimax-official-subject-wardrobe-replacement.mp4)

#### 详细信息

- **生成参数：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **来源类型：** 官方示例
- **来源：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **来源位置：** `page`
- **发布时间：** 2026-07-31
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0049"></a>

### H3-0049 · 日转夜重打光

**多模态参考生成** · **官方示例**

#### 内容说明

公开的 MiniMax H3“日转夜重打光”案例，包含原始提示词与对应成片。

#### 原始 Prompt

```text
Relighting

Change the lighting in the reference video from daytime to night.
```

#### 中文翻译

```text
重新打光

将参考视频中的光照从白天改为夜晚。
```

#### 案例视频

[▶ 在视频页面播放](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-day-to-night-relighting) · [↗ 查看仓库中的 MP4 文件](media/minimax-official-day-to-night-relighting.mp4)

#### 详细信息

- **生成参数：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **来源类型：** 官方示例
- **来源：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **来源位置：** `page`
- **发布时间：** 2026-07-31
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0050"></a>

### H3-0050 · 窗外景观替换

**多模态参考生成** · **官方示例**

#### 内容说明

公开的 MiniMax H3“窗外景观替换”案例，包含原始提示词与对应成片。

#### 原始 Prompt

```text
Live-action environment replacement

Replace the view outside the window in Video 1 with Image 1.
```

#### 中文翻译

```text
真人实拍环境替换

将视频 1 中窗外的景色替换为图片 1。
```

#### 案例视频

[▶ 在视频页面播放](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-window-view-replacement) · [↗ 查看仓库中的 MP4 文件](media/minimax-official-window-view-replacement.mp4)

#### 详细信息

- **生成参数：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **来源类型：** 官方示例
- **来源：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **来源位置：** `page`
- **发布时间：** 2026-07-31
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0051"></a>

### H3-0051 · 对白与表演替换

**多模态参考生成** · **官方示例**

#### 内容说明

公开的 MiniMax H3“对白与表演替换”案例，包含原始提示词与对应成片。

#### 原始 Prompt

```text
In Video 1, replace the woman’s line—“There’s no way we can be together. It’s not that I don’t love you; we simply can’t make it to the end.”—with the line from Audio 1: “Please don’t go. This time, let’s not let each other go.” Adjust the performance subtly to match the new dialogue.
```

#### 中文翻译

```text
在视频 1 中，将女子的台词——“我们不可能在一起。不是我不爱你；只是我们根本走不到最后。”——替换为音频 1 中的台词：“请不要走。这一次，我们不要再放开彼此。”细微调整表演，使其匹配新的对白。
```

#### 案例视频

[▶ 在视频页面播放](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-dialogue-performance-replacement) · [↗ 查看仓库中的 MP4 文件](media/minimax-official-dialogue-performance-replacement.mp4)

#### 详细信息

- **生成参数：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **来源类型：** 官方示例
- **来源：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **来源位置：** `page`
- **发布时间：** 2026-07-31
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0052"></a>

### H3-0052 · 多元素场景编辑

**多模态参考生成** · **官方示例**

#### 内容说明

公开的 MiniMax H3“多元素场景编辑”案例，包含原始提示词与对应成片。

#### 原始 Prompt

```text
In the reference video: replace the newspaper with a green hardcover book; replace the chair with a red sofa; remove the subject’s sunglasses and reveal a clear face; remove the burning-car effect and restore the vehicle to normal; replace the photograph taken from the coat with a small black notebook; and add a tree on the left side of frame.
```

#### 中文翻译

```text
在参考视频中：将报纸替换为绿色精装书；将椅子替换为红色沙发；移除主体的太阳镜并露出清晰面容；移除汽车燃烧效果并恢复车辆正常状态；将从外套中取出的照片替换为黑色小笔记本；在画面左侧添加一棵树。
```

#### 案例视频

[▶ 在视频页面播放](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-multi-element-scene-editing) · [↗ 查看仓库中的 MP4 文件](media/minimax-official-multi-element-scene-editing.mp4)

#### 详细信息

- **生成参数：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **来源类型：** 官方示例
- **来源：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **来源位置：** `page`
- **发布时间：** 2026-07-31
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0053"></a>

### H3-0053 · 产品、招牌与对白替换

**多模态参考生成** · **官方示例**

#### 内容说明

公开的 MiniMax H3“产品、招牌与对白替换”案例，包含原始提示词与对应成片。

#### 原始 Prompt

```text
In the reference video, replace the canned drink shown at the beginning with Coca-Cola. Change the illuminated “FamilyMart” convenience-store sign in the background to “HUHUI.” At the end, replace every snack in the plastic bag with cans of Coca-Cola, and change the final line from “I bought a few snacks” to “I bought a whole bunch of Coke.”
```

#### 中文翻译

```text
在参考视频中，将开头出现的罐装饮料替换为可口可乐。把背景中发光的“FamilyMart”便利店招牌改为“HUHUI”。结尾时，将塑料袋中的所有零食替换为罐装可口可乐，并把最后一句“我买了几样零食”改为“我买了一大堆可乐”。
```

#### 案例视频

[▶ 在视频页面播放](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-product-sign-dialogue-replacement) · [↗ 查看仓库中的 MP4 文件](media/minimax-official-product-sign-dialogue-replacement.mp4)

#### 详细信息

- **生成参数：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **来源类型：** 官方示例
- **来源：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **来源位置：** `page`
- **发布时间：** 2026-07-31
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0055"></a>

### H3-0055 · 手绘浪漫特效

**多模态参考生成** · **官方示例**

#### 内容说明

公开的 MiniMax H3“手绘浪漫特效”案例，包含原始提示词与对应成片。

#### 原始 Prompt

```text
Creative interpretation + animated graphic effects

Add orange-yellow hand-drawn marks like Image 1 around the two people in Video 1. As they move closer, the marks multiply and build from tiny sparks into bright radiance. When they kiss, introduce pink brushstrokes.
```

#### 中文翻译

```text
创意诠释＋动态手绘特效

在视频 1 中两人周围加入类似图片 1 的橙黄色手绘标记。随着两人靠近，标记不断增多，从微小火花逐渐积累为明亮光芒。两人接吻时，加入粉色笔触。
```

#### 案例视频

[▶ 在视频页面播放](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-hand-drawn-romance-vfx) · [↗ 查看仓库中的 MP4 文件](media/minimax-official-hand-drawn-romance-vfx.mp4)

#### 详细信息

- **生成参数：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **来源类型：** 官方示例
- **来源：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **来源位置：** `page`
- **发布时间：** 2026-07-31
- **收录时间：** 2026-08-01
- **核验状态：** Prompt 可见 ✅ 是 · H3 已确认 ✅ 是 · 结果可见 ✅ 是
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

## 参与贡献

可通过 Issue 表单或 Pull Request 投稿。请提供原作者、直接来源链接、完整 Prompt、生成模式，以及是否存在可确认由 MiniMax H3 生成的公开结果。详情见 [CONTRIBUTING.md](docs/CONTRIBUTING.md)。

## 许可证与删除请求

仓库原创内容采用 [CC BY 4.0](LICENSE)；第三方 Prompt 与媒体仍归原权利人所有，详见 [NOTICE.md](NOTICE.md)。权利人可提交删除请求。

---

MiniMax and Hailuo are trademarks of their respective owners. This community project is not affiliated with or endorsed by MiniMax.

Generated from structured data curated through 2026-08-01.
