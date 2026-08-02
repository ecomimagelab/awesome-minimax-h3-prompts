<p align="center"><img src="public/cover.svg" alt="Awesome MiniMax H3 Prompts" width="100%"></p>

# Awesome MiniMax H3 Prompts

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](LICENSE)
[![Validate data](https://github.com/ecomimagelab/awesome-minimax-h3-prompts/actions/workflows/validate.yml/badge.svg)](https://github.com/ecomimagelab/awesome-minimax-h3-prompts/actions/workflows/validate.yml)

> A curated bilingual library of public prompts, examples, and prompting patterns for MiniMax H3.

[简体中文](README_zh.md) · **English**

[▶ **Open the playable video library / 打开可直接播放的视频页面**](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/)

## About MiniMax H3

MiniMax H3 is a multimodal video generation model that accepts text, images, video, and audio as context. This repository separates official examples, community-tested prompts, and unverified guide templates so readers can judge the evidence behind every entry.

- Official model: `MiniMax-H3`
- Output: up to 2K, 4–15 seconds
- Inputs: text, image, video, and audio references
- Official guide: [MiniMax H3 Video Generation](https://platform.minimax.io/docs/guides/video-generation)
- Community prompting guide: [fal.ai H3 guide — bilingual notes](docs/FAL_PROMPTING_GUIDE.md)
- Curation rules: [Deduplication and source precedence](docs/CURATION_POLICY.md)

> [!IMPORTANT]
> **Copyright and verification notice：** No video, no entry: every prompt must have a downloadable public result video mirrored under `media/`; external playback links alone are not accepted. Duplicate outputs are published only once, with multiple useful prompt variants grouped beneath the same video. If a secondary guide republishes an official MiniMax example, attribution follows MiniMax rather than the republisher. If the source publishes only a video, the prompt may be reconstructed, but it must be labeled as an editorial approximation rather than the creator's original prompt. Public availability does not remove an author's rights. Mirrored third-party material is excluded from this repository's CC BY 4.0 license and can be removed through the rights-holder request form.

## Library statistics

| Metric | Count |
| --- | ---: |
| Total prompts | **50** |
| Official examples | **39** |
| Community tested | **11** |
| Community guide templates | **0** |
| Last curated | **2026-08-01** |

## Browse by mode

- [Text to Video (9)](#text-to-video)
- [Image to Video (1)](#image-to-video)
- [First / Last Frame (9)](#first-last-frame)
- [Reference Generation (31)](#reference-generation)

## Featured prompts

- [Drone-riding TikTok dancer](#h3-0001) — Official example
- [A little girl grows up](#h3-0003) — Official example
- [Vintage beret fashion walk](#h3-0004) — Official example
- [Hitchcock move with referenced singer and audio](#h3-0005) — Official example
- [Frutiger Aero shopping mall walk](#h3-0007) — Community tested
- [Don't say my name again](#h3-0012) — Community tested
- [The unanswered letter](#h3-0013) — Community tested
- [I can see the dust](#h3-0014) — Community tested
- [Vintage binocular brand film](#h3-0017) — Official example
- [Hand-drawn kitchen creature](#h3-0018) — Community tested
- [Interactive game equipment UI](#h3-0019) — Community tested
- [Macro coffee-to-desert transition](#h3-0020) — Community tested

## Compilation videos with multiple prompts

### H3-0006–H3-0007 · 2 prompts in one source video

The source presents these examples in a single compilation video. The video is shown once, followed by the complete prompt blocks below.

#### Video

[▶ Play on the video site](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-reddit-neggy5-minimax-h3-tests) · [↗ View the MP4 file in this repository](media/reddit-neggy5-minimax-h3-tests.mp4)

---

<a id="h3-0006"></a>

### H3-0006 · Chow chow prancing in a park

**Text to Video** · **Community tested**

#### Description

A community H3 text-to-video test with a simple two-beat animal action.

#### Prompt

```text
an adorable adult chow chow dog prancing in a park at daytime, the dog then sits down and yawns cutely, looking around.
```

#### Details

- **Parameters：** `duration: not stated` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `animal` `park` `action-sequence` `community-tested`
- **Source type：** Community tested
- **Source：** [Neggy5](https://www.reddit.com/r/StableDiffusion/comments/1vc8o4u/used_my_last_hour_of_my_veniceai_sub_to_test/)
- **Published：** 2026-08-01
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** The author states the shown clips were generated with MiniMax H3.

---

<a id="h3-0007"></a>

### H3-0007 · Frutiger Aero shopping mall walk

**Text to Video** · **Community tested** · ⭐ Featured

#### Description

A community H3 first-person environment test with a retro-futuristic visual direction.

#### Prompt

```text
a first-person view walk through a busy ultramodern shopping mall with frutiger aero aesthetic at dusk. lots of pretty trees and foliage, beautiful organic architecture, lighting
```

#### Details

- **Parameters：** `duration: not stated` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `first-person` `architecture` `frutiger-aero` `community-tested`
- **Source type：** Community tested
- **Source：** [Neggy5](https://www.reddit.com/r/StableDiffusion/comments/1vc8o4u/used_my_last_hour_of_my_veniceai_sub_to_test/)
- **Published：** 2026-08-01
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** The author states the shown clips were generated with MiniMax H3.

---


### H3-0012–H3-0016 · 5 prompts in one source video

The source presents these examples in a single compilation video. The video is shown once, followed by the complete prompt blocks below.

#### Video

[▶ Play on the video site](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-alex-patrascu-minimax-h3-scenes) · [↗ View the MP4 file in this repository](media/alex-patrascu-minimax-h3-scenes.mp4)

---

<a id="h3-0012"></a>

### H3-0012 · Don't say my name again

**Text to Video** · **Community tested** · ⭐ Featured

#### Description

A tense 15-second desert standoff staged as one handheld take with an unseen speaker behind the camera.

#### Prompt

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

#### Details

- **Parameters：** `duration: 15s` · `resolution: 2560x1440` · `ratio: 16:9`
- **Tags：** `desert` `single-take` `handheld` `dialogue` `community-tested`
- **Source type：** Community tested
- **Source：** [Alex Patrascu (@maxescu)](https://x.com/maxescu/status/2082563245504856385)
- **Parent thread：** [X thread](https://x.com/maxescu/status/2082563241062875568)
- **Source location：** `reply`
- **Published：** 2026-07-29
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** The complete prompt appears in an author reply; the parent post says the displayed scenes were tried with MiniMax H3.

---

<a id="h3-0013"></a>

### H3-0013 · The unanswered letter

**Text to Video** · **Community tested** · ⭐ Featured

#### Description

A restrained three-segment period drama in a frosted conservatory, with emotion revealed through a paper insert.

#### Prompt

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

#### Details

- **Parameters：** `duration: 15s` · `resolution: 2560x1440` · `ratio: 16:9`
- **Tags：** `period-drama` `dialogue` `three-segment` `insert-shot` `community-tested`
- **Source type：** Community tested
- **Source：** [Alex Patrascu (@maxescu)](https://x.com/maxescu/status/2082563249095020865)
- **Parent thread：** [X thread](https://x.com/maxescu/status/2082563241062875568)
- **Source location：** `reply`
- **Published：** 2026-07-29
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** The complete prompt appears in an author reply; the parent post says the displayed scenes were tried with MiniMax H3.

---

<a id="h3-0014"></a>

### H3-0014 · I can see the dust

**Image to Video** · **Community tested** · ⭐ Featured

#### Description

A 15-second image-referenced western scene built as a single heat-shimmering take.

#### Prompt

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

#### Details

- **Parameters：** `duration: 15s` · `resolution: 2560x1440` · `ratio: 16:9`
- **Tags：** `western` `image-reference` `single-take` `dialogue` `community-tested`
- **Source type：** Community tested
- **Source：** [Alex Patrascu (@maxescu)](https://x.com/maxescu/status/2082563252471357498)
- **Parent thread：** [X thread](https://x.com/maxescu/status/2082563241062875568)
- **Source location：** `reply`
- **Published：** 2026-07-29
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** The complete prompt appears in an author reply; the parent post says the displayed scenes were tried with MiniMax H3. Image1 is required but is not redistributed here.

---

<a id="h3-0015"></a>

### H3-0015 · I signed it on Tuesday

**Text to Video** · **Community tested**

#### Description

A blue-hour Naples balcony drama told through three restrained camera setups.

#### Prompt

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

#### Details

- **Parameters：** `duration: 15s` · `resolution: 2560x1440` · `ratio: 16:9`
- **Tags：** `relationship-drama` `blue-hour` `three-segment` `dialogue` `community-tested`
- **Source type：** Community tested
- **Source：** [Alex Patrascu (@maxescu)](https://x.com/maxescu/status/2082563256028139736)
- **Parent thread：** [X thread](https://x.com/maxescu/status/2082563241062875568)
- **Source location：** `reply`
- **Published：** 2026-07-29
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** The complete prompt appears in an author reply; the parent post says the displayed scenes were tried with MiniMax H3.

---

<a id="h3-0016"></a>

### H3-0016 · Take the lane at first light

**Text to Video** · **Community tested**

#### Description

A three-segment wartime command scene motivated by a hurricane lamp, moonlight, and artillery flashes.

#### Prompt

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

#### Details

- **Parameters：** `duration: 15s` · `resolution: 2560x1440` · `ratio: 16:9`
- **Tags：** `war-drama` `night` `three-segment` `dialogue` `community-tested`
- **Source type：** Community tested
- **Source：** [Alex Patrascu (@maxescu)](https://x.com/maxescu/status/2082563259782287522)
- **Parent thread：** [X thread](https://x.com/maxescu/status/2082563241062875568)
- **Source location：** `reply`
- **Published：** 2026-07-29
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** The complete prompt appears in an author reply; the parent post says the displayed scenes were tried with MiniMax H3.

---


### H3-0027–H3-0048 · 2 prompts in one source video

The source presents these examples in a single compilation video. The video is shown once, followed by the complete prompt blocks below.

#### Video

[▶ Play on the video site](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-green-screen-to-fairytale-composite) · [↗ View the MP4 file in this repository](media/minimax-official-green-screen-to-fairytale-composite.mp4)

---

<a id="h3-0027"></a>

### H3-0027 · Green-Screen to Fairytale Composite

**Reference Generation** · **Official example**

#### Description

A published MiniMax H3 example demonstrating green-screen to fairytale composite, with its exact source prompt and result video.

#### Prompt

```text
Remove the green screen background of Video 1 and turn it into a fairy tale-like background similar to Video 2. The background elements need to completely match the actions of the characters in Video 1. Modify the lighting of the characters in Video 1 so that it completely matches the background.
```

#### Details

- **Parameters：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **Source type：** Official example
- **Source：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **Source location：** `page`
- **Published：** 2026-07-31
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0048"></a>

### H3-0048 · Green-Screen Environment Replacement

**Reference Generation** · **Official example**

#### Description

A published MiniMax H3 example demonstrating green-screen environment replacement, with its exact source prompt and result video.

#### Prompt

```text
Remove the green-screen background from Video 1 and replace it with a fairy-tale environment similar to Video 2. Make every background element respond correctly to the subject’s movement, and relight the subject so they blend naturally into the new scene.
```

#### Details

- **Parameters：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **Source type：** Official example
- **Source：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **Source location：** `page`
- **Published：** 2026-07-31
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---



## All prompts

## Text to Video

*Related prompts in the compilation above:* [H3-0006](#h3-0006) · [H3-0007](#h3-0007) · [H3-0012](#h3-0012) · [H3-0013](#h3-0013) · [H3-0015](#h3-0015) · [H3-0016](#h3-0016)

<a id="h3-0001"></a>

### H3-0001 · Drone-riding TikTok dancer

**Text to Video** · **Official example** · ⭐ Featured

#### Description

A compact official text-to-video API example focused on acrobatic motion.

#### Prompt

```text
A tiktok dancer is dancing on a drone, doing flips and tricks.
```

#### Video

[▶ Play on the video site](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-text-to-video) · [↗ View the MP4 file in this repository](media/minimax-official-text-to-video.mp4)

#### Details

- **Parameters：** `duration: 5s` · `resolution: 2K` · `ratio: 16:9`
- **Tags：** `action` `dance` `aerial` `official`
- **Source type：** Official example
- **Source：** [MiniMax](https://platform.minimax.io/docs/guides/video-generation)
- **Published：** 2026-07-31
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** Published in the official MiniMax H3 API guide.

---

<a id="h3-0018"></a>

### H3-0018 · Hand-drawn kitchen creature

**Text to Video** · **Community tested** · ⭐ Featured

#### Description

A text-only hybrid of live-action phone footage and luminous hand-drawn animation.

#### Prompt

```text
15 seconds, 16:9 landscape. Blend live-action footage of a small kitchen at dusk with hand-drawn luminous animation. The last sunset light lingers at the window. The lived-in kitchen contains an old wooden table, a half-washed mug, a lightly fogged glass bottle, and a hanging dish towel.

Shoot as if someone is filming one-handed on a phone: subtle hand tremor, hesitant close-focus pulls, backlit exposure breathing, and slightly coarse noise in the shadows. It should feel like an astonishing event captured in a rush at home, not a carefully dressed commercial.

Do not show giant eyes, split mouths, fangs, threatening behavior, lunges, sudden black frames, or jump scares. Use only room tone, cloth friction, a soft mug clink, faucet drips, the camera operator’s footsteps and quiet breathing, plus gentle electronic tones and tiny vocalizations from the drawn creatures.
```

#### Video

[▶ Play on the video site](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-fal-hand-drawn-kitchen-creature) · [↗ View the MP4 file in this repository](media/fal-hand-drawn-kitchen-creature.mp4)

#### Details

- **Parameters：** `duration: 15s` · `resolution: 2K` · `ratio: 16:9`
- **Tags：** `hand-drawn` `live-action` `phone-camera` `native-audio` `community-tested`
- **Source type：** Community tested
- **Source：** [Bennett Heyn / fal](https://fal.ai/learn/devs/minimax-h3-prompting-guide)
- **Source location：** `page`
- **Published：** 2026-07-30
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** Published by fal as a text-to-video MiniMax H3 example with the result visible.

---

<a id="h3-0025"></a>

### H3-0025 · Neon Laundromat Encounter

**Text to Video** · **Official example**

#### Description

A published MiniMax H3 example demonstrating neon laundromat encounter, with its exact source prompt and result video.

#### Prompt

```text
15 seconds, 16:9 landscape. Combine a live-action late-night laundromat with hand-drawn luminous animation. The small self-service laundromat has gently flickering fluorescent lights, running washers, plastic baskets, a worn bench, and one sock on the floor. Keep the space quiet and faintly nostalgic.

Use a one-handed phone-camera feel with visible shake, exposure fluctuation under white fluorescent light, environmental reflections in glass, and delayed autofocus at close range. Avoid polished commercial composition; it should feel like an authentic late-night encounter, filmed while following a strange apparition.
```

#### Video

[▶ Play on the video site](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-neon-laundromat-encounter) · [↗ View the MP4 file in this repository](media/minimax-official-neon-laundromat-encounter.mp4)

#### Details

- **Parameters：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `text-to-video` `official`
- **Source type：** Official example
- **Source：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **Source location：** `page`
- **Published：** 2026-07-31
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

## Image to Video

*Related prompts in the compilation above:* [H3-0014](#h3-0014)

## First / Last Frame

<a id="h3-0003"></a>

### H3-0003 · A little girl grows up

**First / Last Frame** · **Official example** · ⭐ Featured

#### Description

An official first-and-last-frame transition example showing a character growing up.

#### Prompt

```text
A little girl grows up.
```

#### Video

[▶ Play on the video site](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-first-last-frame) · [↗ View the MP4 file in this repository](media/minimax-official-first-last-frame.mp4)

#### Details

- **Parameters：** `duration: 5s` · `resolution: 2K` · `ratio: adaptive`
- **Tags：** `transition` `aging` `first-frame` `last-frame` `official`
- **Source type：** Official example
- **Source：** [MiniMax](https://platform.minimax.io/docs/guides/video-generation)
- **Published：** 2026-07-31
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** Published with first- and last-frame inputs in the official API guide.

---

<a id="h3-0022"></a>

### H3-0022 · Epic Space Opera Teaser

**First / Last Frame** · **Official example**

#### Description

A published MiniMax H3 example demonstrating epic space opera teaser, with its exact source prompt and result video.

#### Prompt

```text
Epic theatrical space-opera teaser

Keep the pace fast and the scale enormous without letting the edit drag. Use sharp hard cuts, a shaking command deck, white-hot flashes, split-second black frames, and a violent jump-to-warp impact. Title cards should use wide-tracked cinematic typography—not pure white—with restrained material texture, subtle illumination, and a faint edge glow. Animate the titles by emerging from deep-space shadow, catching a sweep of starlight, opening their letter spacing, leaving a slight afterimage, and flashing briefly against black.
```

#### Video

[▶ Play on the video site](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-epic-space-opera-teaser) · [↗ View the MP4 file in this repository](media/minimax-official-epic-space-opera-teaser.mp4)

#### Details

- **Parameters：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `first-last-frame` `official`
- **Source type：** Official example
- **Source：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **Source location：** `page`
- **Published：** 2026-07-31
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0028"></a>

### H3-0028 · Animated Gallery Poster

**First / Last Frame** · **Official example**

#### Description

A published MiniMax H3 example demonstrating animated gallery poster, with its exact source prompt and result video.

#### Prompt

```text
Animate the source artwork as a motion poster while preserving its white gallery border, inner frame, red/white/black palette, 3D collectible-figure look, and original layout. Add a light, playful type-on sound whenever text appears.
```

#### Video

[▶ Play on the video site](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-animated-gallery-poster) · [↗ View the MP4 file in this repository](media/minimax-official-animated-gallery-poster.mp4)

#### Details

- **Parameters：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `first-last-frame` `official`
- **Source type：** Official example
- **Source：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **Source location：** `page`
- **Published：** 2026-07-31
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0033"></a>

### H3-0033 · Automotive Website UI Animation

**First / Last Frame** · **Official example**

#### Description

A published MiniMax H3 example demonstrating automotive website ui animation, with its exact source prompt and result video.

#### Prompt

```text
Animate the website UI: the top headline slides down into place, the copy panel below slides up, and the car’s lights shift from dark to red.
```

#### Video

[▶ Play on the video site](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-automotive-website-ui-animation) · [↗ View the MP4 file in this repository](media/minimax-official-automotive-website-ui-animation.mp4)

#### Details

- **Parameters：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `first-last-frame` `official`
- **Source type：** Official example
- **Source：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **Source location：** `page`
- **Published：** 2026-07-31
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0034"></a>

### H3-0034 · Rotating Product Page Reveal

**First / Last Frame** · **Official example**

#### Description

A published MiniMax H3 example demonstrating rotating product page reveal, with its exact source prompt and result video.

#### Prompt

```text
Reveal the layout from top to bottom. Upper and center typography slides down; lower typography slides up. Once the central product appears, let it rotate subtly.
```

#### Video

[▶ Play on the video site](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-rotating-product-page-reveal) · [↗ View the MP4 file in this repository](media/minimax-official-rotating-product-page-reveal.mp4)

#### Details

- **Parameters：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `first-last-frame` `official`
- **Source type：** Official example
- **Source：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **Source location：** `page`
- **Published：** 2026-07-31
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0035"></a>

### H3-0035 · Claymation Lava Canyon Leap

**First / Last Frame** · **Official example**

#### Description

A published MiniMax H3 example demonstrating claymation lava canyon leap, with its exact source prompt and result video.

#### Prompt

```text
Claymation. A fox sprints to the edge of a cliff and launches without hesitation, making a dramatic heroic leap in slow motion over an immense lava canyon. Midair, the camera races beneath the fox’s belly in a bold dynamic move, revealing the terrifying depth of the chasm and the fully extended motion of its clay body.
```

#### Video

[▶ Play on the video site](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-claymation-lava-canyon-leap) · [↗ View the MP4 file in this repository](media/minimax-official-claymation-lava-canyon-leap.mp4)

#### Details

- **Parameters：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `first-last-frame` `official`
- **Source type：** Official example
- **Source：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **Source location：** `page`
- **Published：** 2026-07-31
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0038"></a>

### H3-0038 · First-Person Tactical Gameplay

**First / Last Frame** · **Official example**

#### Description

A published MiniMax H3 example demonstrating first-person tactical gameplay, with its exact source prompt and result video.

#### Prompt

```text
Camera: first-person, eye level, handheld gameplay. Simulate a player operating a modern-warfare FPS, holding an assault rifle and advancing slowly around the perimeter of a military base. Move forward along a road beside cover, sweep the reticle across the passage ahead, pause to fire several rounds at a distant target, then continue pushing forward like authentic player-controlled footage.

Lighting: cool natural light across a modern military base, mixed with smoke and firelight. Keep the image photoreal and crisp, with AAA-quality weapons, materials, dust, and battlefield haze.

Camera movement: subtle player-driven sway while moving; begin with a slow advance, make small checks left and right, add light recoil when firing, then continue forward steadily.
```

#### Video

[▶ Play on the video site](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-first-person-tactical-gameplay) · [↗ View the MP4 file in this repository](media/minimax-official-first-person-tactical-gameplay.mp4)

#### Details

- **Parameters：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `first-last-frame` `official`
- **Source type：** Official example
- **Source：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **Source location：** `page`
- **Published：** 2026-07-31
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0039"></a>

### H3-0039 · Interactive Otome Game Transition

**First / Last Frame** · **Official example**

#### Description

A published MiniMax H3 example demonstrating interactive otome game transition, with its exact source prompt and result video.

#### Prompt

```text
Interactive Otome Game

Use the first image as the exact opening frame and the second as the exact ending frame. Create a transition within a premium Chinese otome visual-novel interface, capturing an intimate backstage moment before and after a performance. Move naturally from “Choose to watch his performance” to “Han Xu reacts with intrigued interest after hearing the heroine.” Reveal UI copy, choices, and dialogue boxes with refined otome-game motion design. Keep transitions fluid and the romantic tension suggestive but restrained.
```

#### Video

[▶ Play on the video site](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-interactive-otome-game-transition) · [↗ View the MP4 file in this repository](media/minimax-official-interactive-otome-game-transition.mp4)

#### Details

- **Parameters：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `first-last-frame` `official`
- **Source type：** Official example
- **Source：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **Source location：** `page`
- **Published：** 2026-07-31
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0054"></a>

### H3-0054 · Precision Costume Swap

**First / Last Frame** · **Official example**

#### Description

A published MiniMax H3 example demonstrating precision costume swap, with its exact source prompt and result video.

#### Prompt

```text
Two magicians stand onstage facing the audience and perform a “swap” illusion. They wave their wands simultaneously and smoke rises. When it clears, their suit colors have exchanged: the magician on the left now wears white, and the one on the right now wears black. Their glove colors do not change. They bow; the red curtain closes behind them and gradually shifts from deep red to dark blue.
```

#### Video

[▶ Play on the video site](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-precision-costume-swap) · [↗ View the MP4 file in this repository](media/minimax-official-precision-costume-swap.mp4)

#### Details

- **Parameters：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `first-last-frame` `official`
- **Source type：** Official example
- **Source：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **Source location：** `page`
- **Published：** 2026-07-31
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

## Reference Generation

*Related prompts in the compilation above:* [H3-0027](#h3-0027) · [H3-0048](#h3-0048)

<a id="h3-0004"></a>

### H3-0004 · Vintage beret fashion walk

**Reference Generation** · **Official example** · ⭐ Featured

#### Description

An official reference-image example for subject consistency and cinematic fashion motion.

#### Prompt

```text
On an overcast day, in an ancient cobbled alleyway, the model walks and adjusts a vintage beret with a smile; natural lighting and cinematic colors.
```

#### Video

[▶ Play on the video site](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-reference) · [↗ View the MP4 file in this repository](media/minimax-official-reference.mp4)

#### Details

- **Parameters：** `duration: 5s` · `resolution: 2K` · `ratio: adaptive`
- **Tags：** `fashion` `character-consistency` `cinematic` `official`
- **Source type：** Official example
- **Source：** [MiniMax](https://platform.minimax.io/docs/guides/video-generation)
- **Published：** 2026-07-31
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** Published with a reference image in the official API guide.

---

<a id="h3-0005"></a>

### H3-0005 · Hitchcock move with referenced singer and audio

**Reference Generation** · **Official example** · ⭐ Featured

#### Description

A full-modality official example combining camera motion, a character image, and a vocal reference.

#### Prompt

```text
Reference the Hitchcock camera movement from Video 1, have the character in Image 2 sing, with the vocals matching Audio 3.
```

#### Video

[▶ Play on the video site](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-hitchcock-reference) · [↗ View the MP4 file in this repository](media/minimax-official-hitchcock-reference.mp4)

#### Details

- **Parameters：** `duration: not stated` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `multimodal` `camera-reference` `voice-reference` `official`
- **Source type：** Official example
- **Source：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **Published：** 2026-07-31
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** Published in the official MiniMax H3 launch article.

---

<a id="h3-0017"></a>

### H3-0017 · Vintage binocular brand film

**Reference Generation** · **Official example** · ⭐ Featured

#### Description

A four-reference brand film with a locked binocular mask, focus-driven typography, and whip-scan transitions.

#### Prompt

```text
Use Images 1–4 as sequential keyframes, seen through a vintage binocular viewfinder searching for the MINIMAX installation. Open out of focus with subtle handheld shake, then push in quickly and rack focus onto Image 1. Between keyframes, use fast binocular-scan transitions with whip movement, motion blur, optical smearing, and brief exposure flicker. Cut at peak blur, then settle and snap back into focus.

Keep the twin circular lens mask absolutely fixed throughout: identical position, scale, feathered black vignette, and edge softness, with no warping or drift. Only the image inside the mask may move.

In Image 2, let the fabric move gently in the wind while the MINIMAX lettering follows the folds and remains legible. In Image 3, the subject should feel like a stylish passerby caught by chance, walking, turning, and swinging their arms naturally. In Image 4, the subject adjusts their glasses or lifts their chin slightly with a cool, effortless fashion-campaign attitude.

Red typography should resolve with the focus: begin slightly blurred and at low opacity, then fade into clarity over 0.3–0.5 seconds. A subtle vertical slide or slight tracking expansion is allowed. Fade it out before the next transition or let motion blur carry it away. No spins, bounces, or large fly-ins/outs.

Visual language: a voyeuristic, Wes Anderson-inspired 35 mm film look with fine grain, soft highlight halation, restrained color, and red typographic accents. Minimal, premium, lightly playful. Do not add people, vehicles, buildings, or logos. Preserve the core composition and the MINIMAX installation exactly.
```

#### Video

[▶ Play on the video site](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-vintage-binocular-brand-film) · [↗ View the MP4 file in this repository](media/minimax-official-vintage-binocular-brand-film.mp4)

#### Details

- **Parameters：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `brand-film` `multi-image` `typography` `transition` `official`
- **Source type：** Official example
- **Source：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **Source location：** `page`
- **Published：** 2026-07-31
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0019"></a>

### H3-0019 · Interactive game equipment UI

**Reference Generation** · **Community tested** · ⭐ Featured

#### Description

A detailed 15-second timecoded UI sequence that transforms a character and loads a cyberpunk world.

#### Prompt

```text
Use Image 1 for the character and Image 2 for the UI style.

[0–2 seconds] High-angle overhead shot. The character sits on a vivid, highly saturated purple floor, looks up at camera, and matches Image 1. A game menu appears on the right: START NEW GAME, CONTINUE (highlighted), SETTINGS, EXIT GAME. Player profile MINIMAX appears top left. The cursor selects CONTINUE.

[2–4 seconds] Smoothly push in to her right arm. A RIGHT ARM EQUIPMENT panel slides in from the right. PHANTOM GRIP is selected, then the selection moves to CHRONOS CLAW. Her mechanical hand reconfigures: fingers separate, new claw-like joints lock into place, and cyan LEDs flare brighter.

[4–7 seconds] Arc smoothly to her left. An ARMAMENT CUSTOMIZATION grid slides in, showing hand, forearm, elbow, and upper-arm components. The selector cycles rapidly. Her left arm disassembles section by section: the forearm plate releases, new armor slides in, the elbow joint swaps, and the hand reconfigures, with exposed wiring and pistons visible during the change.

[7–8.5 seconds] Pull back to a medium shot. CONFIRM CONFIG flashes; click it. All UI panels collapse inward and vanish. She uncrosses her legs and settles into a relaxed seated pose with one knee raised, lifting the prosthetic hand for a subtle post-configuration movement.

[8.5–10 seconds] A LOADING bar appears along the bottom and races from 0% to 100%. The saturated purple environment darkens as shadows creep inward and warm golden light begins to bleed through.

[10–15 seconds] As she stands, the full world loads around her: a dense cyberpunk slum with flickering neon, rain-wet streets, moving crowds, passing motorcycles, tangled overhead cables, and stacked buildings stretching toward futuristic towers. Settle into a third-person camera behind her. HUD elements fade in: minimap top right, health and ammo bottom left, then a mission marker. She steps into the street.
```

#### Video

[▶ Play on the video site](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-fal-interactive-game-equipment-ui) · [↗ View the MP4 file in this repository](media/fal-interactive-game-equipment-ui.mp4)

#### Details

- **Parameters：** `duration: 15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `game-ui` `timecoded` `typography` `cyberpunk` `community-tested`
- **Source type：** Community tested
- **Source：** [Bennett Heyn / fal](https://fal.ai/learn/devs/minimax-h3-prompting-guide)
- **Source location：** `page`
- **Published：** 2026-07-30
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** Published by fal as a MiniMax H3 reference-to-video example with two reference images and the result visible.

---

<a id="h3-0020"></a>

### H3-0020 · Macro coffee-to-desert transition

**Reference Generation** · **Community tested** · ⭐ Featured

#### Description

A continuous macro-to-landscape material match using two image references.

#### Prompt

```text
@Image 1: Push in rapidly toward the milk foam, cocoa particles, and dark liquid texture on the coffee until particles, bubbles, and ripples fill the frame. Keep the macro photography realistic, with extremely shallow depth of field and fine powder drifting through backlight. Let the surface feel suspended between granular sand and fluid.

At the exact moment when the cocoa particles, foam contours, and coffee swirl closely resemble the dune ridges, wind-carved textures, and airborne sand in @Image 2, transition seamlessly into the desert landscape. Continue pushing forward until the full dunes from @Image 2 are revealed.

No tearing, black frames, hard cuts, obvious VFX, or compositing seams. Keep it photoreal, quiet, and restrained—as though one granular material naturally expands from the microscopic coffee surface into a vast desert. One continuous shot with no visible edit.
```

#### Video

[▶ Play on the video site](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-fal-macro-coffee-desert-transition) · [↗ View the MP4 file in this repository](media/fal-macro-coffee-desert-transition.mp4)

#### Details

- **Parameters：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `macro` `seamless-transition` `material-match` `multi-image` `community-tested`
- **Source type：** Community tested
- **Source：** [Bennett Heyn / fal](https://fal.ai/learn/devs/minimax-h3-prompting-guide)
- **Source location：** `page`
- **Published：** 2026-07-30
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** Published by fal as a MiniMax H3 reference-to-video example with two reference images and the result visible.

---

<a id="h3-0021"></a>

### H3-0021 · Cat-to-dog video replacement

**Reference Generation** · **Community tested**

#### Description

A minimal localized-edit instruction that changes one subject while preserving the source clip.

#### Prompt

```text
Replace the cat in the video with a dog.
```

#### Video

[▶ Play on the video site](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-fal-cat-to-dog-replacement) · [↗ View the MP4 file in this repository](media/fal-cat-to-dog-replacement.mp4)

#### Details

- **Parameters：** `duration: source dependent` · `resolution: 2K` · `ratio: adaptive`
- **Tags：** `video-editing` `subject-replacement` `localized-edit` `community-tested`
- **Source type：** Community tested
- **Source：** [Bennett Heyn / fal](https://fal.ai/learn/devs/minimax-h3-prompting-guide)
- **Source location：** `page`
- **Published：** 2026-07-30
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** Published by fal as a precise MiniMax H3 video-editing example with the source and result visible.

---

<a id="h3-0023"></a>

### H3-0023 · Desert Fashion Campaign

**Reference Generation** · **Official example**

#### Description

A published MiniMax H3 example demonstrating desert fashion campaign, with its exact source prompt and result video.

#### Prompt

```text
Create a premium 16:9 landscape fashion film. Use Image 1 for the overall mood, location, and film texture; Image 2 for the talent; Image 3 for the bag; and Image 4 for the closing brand mark. This is a fashion campaign for the clothing and bag. The tone is elevated, cool, and restrained, but the edit should still feel lively and fashion-forward—not like a conventional narrative film or an e-commerce ad.

Keep the story simple: beside a vintage car on a desert highway, a woman walks to the rear of the car, opens the trunk, takes out a black bag, shares a quiet beat with the man standing nearby, then leaves carrying the bag. Integrate the clothing and bag naturally into the performance so they feel like part of the characters’ identity.
```

#### Video

[▶ Play on the video site](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-desert-fashion-campaign) · [↗ View the MP4 file in this repository](media/minimax-official-desert-fashion-campaign.mp4)

#### Details

- **Parameters：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **Source type：** Official example
- **Source：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **Source location：** `page`
- **Published：** 2026-07-31
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0024"></a>

### H3-0024 · Cyber-Grunge Fashion Film

**Reference Generation** · **Official example**

#### Description

A published MiniMax H3 example demonstrating cyber-grunge fashion film, with its exact source prompt and result video.

#### Prompt

```text
Use Image 1 as the reference for texture and mood, and Image 2 for the subject’s appearance. Generate a 15-second, 16:9 fashion short. Preserve the subject’s identity: long platinum-blonde hair, narrow black vintage sunglasses, a glossy black patent-leather trench coat, a cool, self-assured expression, and orange firelight reflected across the coat.

Style: fast-cut fashion film on analog stock, set against a nighttime blaze with black smoke and orange-red flames. Layer in VHS glitches, CCTV signal interruptions, 1990s film grain, scanlines, chromatic aberration, light leaks, flash-to-white transitions, and subtle frame jitter.
```

#### Video

[▶ Play on the video site](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-cyber-grunge-fashion-film) · [↗ View the MP4 file in this repository](media/minimax-official-cyber-grunge-fashion-film.mp4)

#### Details

- **Parameters：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **Source type：** Official example
- **Source：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **Source location：** `page`
- **Published：** 2026-07-31
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0026"></a>

### H3-0026 · Cyber-Grunge Rap Music Video

**Reference Generation** · **Official example**

#### Description

A published MiniMax H3 example demonstrating cyber-grunge rap music video, with its exact source prompt and result video.

#### Prompt

```text
Style: dark-pop / cyber-grunge / rap music video with photoreal high-fashion polish and the texture of a scanned film magazine—high contrast without looking cheap. Reference late-1990s to early-2000s indie magazines, photocopies, film scans, underground-music posters, and zine collage. Add coarse grain, subtle gate weave, halftone dots, rough print edges, and slight scan misregistration. Keep the edit fast and use hard cuts only—no fades or soft transitions. Match the typographic treatment and surface texture of the reference images.
```

#### Video

[▶ Play on the video site](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-cyber-grunge-rap-music-video) · [↗ View the MP4 file in this repository](media/minimax-official-cyber-grunge-rap-music-video.mp4)

#### Details

- **Parameters：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **Source type：** Official example
- **Source：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **Source location：** `page`
- **Published：** 2026-07-31
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0029"></a>

### H3-0029 · Vertical Family Confrontation

**Reference Generation** · **Official example**

#### Description

A published MiniMax H3 example demonstrating vertical family confrontation, with its exact source prompt and result video.

#### Prompt

```text
A 9:16 vertical family-confrontation scene with grounded live-action performances, set in a Chinese family home or small restaurant. Use warm interior light, red decorations and calligraphy in the background, shallow depth of field, intense emotion, and tight pacing.

Performance: natural short-form drama, never theatrical. Qin Haoxuan argues back with anger, hurt, and urgency. The older woman questions him in a sharp, forceful, relentless tone. Build the confrontation steadily.

Shoot mainly in medium-close shots with frequent shot/reverse-shot cutting. Keep the setting lived-in and realistic. No sci-fi, period costume, or animation styling. Do not show subtitles, added text, platform watermarks, or stickers.
```

#### Video

[▶ Play on the video site](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-vertical-family-confrontation) · [↗ View the MP4 file in this repository](media/minimax-official-vertical-family-confrontation.mp4)

#### Details

- **Parameters：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **Source type：** Official example
- **Source：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **Source location：** `page`
- **Published：** 2026-07-31
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0030"></a>

### H3-0030 · Futuristic Eyewear Campaign

**Reference Generation** · **Official example**

#### Description

A published MiniMax H3 example demonstrating futuristic eyewear campaign, with its exact source prompt and result video.

#### Prompt

```text
Create a premium 9:16 fashion-eyewear commercial. Match the reference video’s shot rhythm, edit speed, white-cyclorama look, and severe fashion attitude. Use a seamless minimal white studio with clean, bold, avant-garde art direction worthy of a global luxury campaign.

Use Image 1 for the key visual: two full-body female models, one Black and one white, preserving their elevated wardrobe, body language, studio lighting, runway presence, and cool attitude. Use Image 2 for facial details. Both models wear futuristic luxury eyewear based on Image 3: wraparound curved lenses, a sharp cat-eye/goggle hybrid silhouette, mirrored reflections, streamlined temples, and the finish of a premium fashion accessory.
```

#### Video

[▶ Play on the video site](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-futuristic-eyewear-campaign) · [↗ View the MP4 file in this repository](media/minimax-official-futuristic-eyewear-campaign.mp4)

#### Details

- **Parameters：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **Source type：** Official example
- **Source：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **Source location：** `page`
- **Published：** 2026-07-31
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0031"></a>

### H3-0031 · Ergonomic Chair Product Film

**Reference Generation** · **Official example**

#### Description

A published MiniMax H3 example demonstrating ergonomic chair product film, with its exact source prompt and result video.

#### Prompt

```text
Product Feature Visualization

Present a black Herman Miller ergonomic chair in a premium office with a full 360-degree product reveal. Cut to macro views of the breathable mesh back with airflow visualization, an engineering animation of the lumbar support and ergonomic curve, and demonstrations of multidirectional armrest and seat-height adjustment. Show designers, developers, and creative professionals working comfortably over long sessions. Include a 3D skeletal-support visualization that communicates all-day comfort, plus refined interior styling. End with the line: “WHERE INSPIRATION MEETS COMFORT.” Keep the direction minimal, cool-toned, professional, futuristic, and slow-paced. Use Image 1 for feature details and Image 2 for the product.
```

#### Video

[▶ Play on the video site](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-ergonomic-chair-product-film) · [↗ View the MP4 file in this repository](media/minimax-official-ergonomic-chair-product-film.mp4)

#### Details

- **Parameters：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **Source type：** Official example
- **Source：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **Source location：** `page`
- **Published：** 2026-07-31
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0032"></a>

### H3-0032 · Nike-Style Product Landing Page

**Reference Generation** · **Official example**

#### Description

A published MiniMax H3 example demonstrating nike-style product landing page, with its exact source prompt and result video.

#### Prompt

```text
Create a dynamic product-landing-page UI/UX demo inspired by Nike’s digital language, built around the product in Image 1. Use oversized, bold, italicized sans-serif typography and backgrounds that combine speed-driven light streaks with dark carbon fiber or breathable performance-mesh textures. Show a smooth, fast, powerful scroll through the page, plus high-impact hover interactions with scale-ups and color inversion.
```

#### Video

[▶ Play on the video site](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-nike-style-product-landing-page) · [↗ View the MP4 file in this repository](media/minimax-official-nike-style-product-landing-page.mp4)

#### Details

- **Parameters：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **Source type：** Official example
- **Source：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **Source location：** `page`
- **Published：** 2026-07-31
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0036"></a>

### H3-0036 · Fantasy Wuxia Character Film

**Reference Generation** · **Official example**

#### Description

A published MiniMax H3 example demonstrating fantasy wuxia character film, with its exact source prompt and result video.

#### Prompt

```text
Use Image 2 as the locked character reference. Preserve the half-up long black hair, openwork silver crown, indigo ribbon, layered pale hanfu, translucent blue outer robe, deep-blue sash, silver floral fastener, and long tassels. Use Image 1 for storyboard order and pacing.

Render in high-quality 4K, 16:9 Chinese-inspired 3D with cinematic xianxia production value: intense, solemn, and shaped by destiny. Follow the storyboard beat by beat, with natural camera movement and seamless transitions—never a slideshow. Show the face only in close-up or extreme close-up. In wide shots, use back view, rear three-quarter view, or empty environment shots; never show a distant frontal face.
```

#### Video

[▶ Play on the video site](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-fantasy-wuxia-character-film) · [↗ View the MP4 file in this repository](media/minimax-official-fantasy-wuxia-character-film.mp4)

#### Details

- **Parameters：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **Source type：** Official example
- **Source：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **Source location：** `page`
- **Published：** 2026-07-31
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0037"></a>

### H3-0037 · Otome Male Lead Character Promo

**Reference Generation** · **Official example**

#### Description

A published MiniMax H3 example demonstrating otome male lead character promo, with its exact source prompt and result video.

#### Prompt

```text
Create a character promo for a male lead in an otome game. Use Image 2 as a strict identity reference. Preserve the same face, hairstyle, body proportions, costume design, material detail, and polished otome-CG aesthetic throughout.
```

#### Video

[▶ Play on the video site](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-otome-male-lead-character-promo) · [↗ View the MP4 file in this repository](media/minimax-official-otome-male-lead-character-promo.mp4)

#### Details

- **Parameters：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **Source type：** Official example
- **Source：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **Source location：** `page`
- **Published：** 2026-07-31
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0040"></a>

### H3-0040 · Multi-Asset Cinematic Remix

**Reference Generation** · **Official example**

#### Description

A published MiniMax H3 example demonstrating multi-asset cinematic remix, with its exact source prompt and result video.

#### Prompt

```text
Use Images 1–6 as assets. Match Reference Video 1 closely for shot rhythm, transition language, and music.
```

#### Video

[▶ Play on the video site](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-multi-asset-cinematic-remix) · [↗ View the MP4 file in this repository](media/minimax-official-multi-asset-cinematic-remix.mp4)

#### Details

- **Parameters：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **Source type：** Official example
- **Source：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **Source location：** `page`
- **Published：** 2026-07-31
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0041"></a>

### H3-0041 · Live-Action Voxel Transformation

**Reference Generation** · **Official example**

#### Description

A published MiniMax H3 example demonstrating live-action voxel transformation, with its exact source prompt and result video.

#### Prompt

```text
Preserve the buildings, pedestrians, and overall environment in Video 1 as photoreal live action. Transform only the trees and cars into 3D pixel-art or voxel-block objects in the style of Minecraft, using Image 1 as the visual reference. Keep their motion physically correct, and preserve the real environment’s shadows and transmitted light. Use Video 2 as the overall target.
```

#### Video

[▶ Play on the video site](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-live-action-voxel-transformation) · [↗ View the MP4 file in this repository](media/minimax-official-live-action-voxel-transformation.mp4)

#### Details

- **Parameters：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **Source type：** Official example
- **Source：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **Source location：** `page`
- **Published：** 2026-07-31
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0042"></a>

### H3-0042 · Character Swap with Performance Reference

**Reference Generation** · **Official example**

#### Description

A published MiniMax H3 example demonstrating character swap with performance reference, with its exact source prompt and result video.

#### Prompt

```text
Match the character motion, expressions, and performance timing in Image 1 closely to Input Video 1.

At the sink on the right side of frame, the man hands a washed plate to the woman on the left. He turns, then suddenly flicks dish-soap foam at her with his right hand. Startled, she immediately retaliates. They laugh, dodge, and playfully throw foam back and forth.
```

#### Video

[▶ Play on the video site](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-character-swap-with-performance-reference) · [↗ View the MP4 file in this repository](media/minimax-official-character-swap-with-performance-reference.mp4)

#### Details

- **Parameters：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **Source type：** Official example
- **Source：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **Source location：** `page`
- **Published：** 2026-07-31
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0043"></a>

### H3-0043 · Street Dance Motion Transfer

**Reference Generation** · **Official example**

#### Description

A published MiniMax H3 example demonstrating street dance motion transfer, with its exact source prompt and result video.

#### Prompt

```text
Use Video 1 as the motion reference for a street-dance performance. Use Images 1 and 2 as the character references.
```

#### Video

[▶ Play on the video site](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-street-dance-motion-transfer) · [↗ View the MP4 file in this repository](media/minimax-official-street-dance-motion-transfer.mp4)

#### Details

- **Parameters：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **Source type：** Official example
- **Source：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **Source location：** `page`
- **Published：** 2026-07-31
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0044"></a>

### H3-0044 · Capybara Motion Recreation

**Reference Generation** · **Official example**

#### Description

A published MiniMax H3 example demonstrating capybara motion recreation, with its exact source prompt and result video.

#### Prompt

```text
Motion reference for a DIY reaction clip

Match the action in Video 1 from a locked-off wide camera. Replace the three suited men with three highly photoreal capybaras. Preserve the original movement path exactly: all three drop quickly to the floor; the left capybara jumps to center; the center capybara rolls to the far left; the new center capybara rolls to the far right; the right capybara jumps to center; finally, the center capybara jumps onto the other two, forming a pyramid. Keep the camera fixed and integrate fur, lighting, and shadows realistically into the scene.
```

#### Video

[▶ Play on the video site](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-capybara-motion-recreation) · [↗ View the MP4 file in this repository](media/minimax-official-capybara-motion-recreation.mp4)

#### Details

- **Parameters：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **Source type：** Official example
- **Source：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **Source location：** `page`
- **Published：** 2026-07-31
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0045"></a>

### H3-0045 · Voice Clone Dialogue Transfer

**Reference Generation** · **Official example**

#### Description

A published MiniMax H3 example demonstrating voice clone dialogue transfer, with its exact source prompt and result video.

#### Prompt

```text
The character says: “Follow the wind, live free. Leave worries behind, enjoy the moment.” Match the voice in Audio 1.
```

#### Video

[▶ Play on the video site](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-voice-clone-dialogue-transfer) · [↗ View the MP4 file in this repository](media/minimax-official-voice-clone-dialogue-transfer.mp4)

#### Details

- **Parameters：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **Source type：** Official example
- **Source：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **Source location：** `page`
- **Published：** 2026-07-31
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0046"></a>

### H3-0046 · Add a Character in Sync with the Others

**Reference Generation** · **Official example**

#### Description

A published MiniMax H3 example demonstrating add a character in sync with the others, with its exact source prompt and result video.

#### Prompt

```text
Add one person on the left side of frame wearing the same team uniform and moving in sync with the others.
```

#### Video

[▶ Play on the video site](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-add-a-character-in-sync-with-the-others) · [↗ View the MP4 file in this repository](media/minimax-official-add-a-character-in-sync-with-the-others.mp4)

#### Details

- **Parameters：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **Source type：** Official example
- **Source：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **Source location：** `page`
- **Published：** 2026-07-31
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0047"></a>

### H3-0047 · Subject & Wardrobe Replacement

**Reference Generation** · **Official example**

#### Description

A published MiniMax H3 example demonstrating subject & wardrobe replacement, with its exact source prompt and result video.

#### Prompt

```text
Precise Subject and Wardrobe Replacement

Replace the child at the back of Video 1 with the golden retriever from Image 1. Replace the khaki jacket worn by the child on the far left with the denim jacket from Image 2.
```

#### Video

[▶ Play on the video site](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-subject-wardrobe-replacement) · [↗ View the MP4 file in this repository](media/minimax-official-subject-wardrobe-replacement.mp4)

#### Details

- **Parameters：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **Source type：** Official example
- **Source：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **Source location：** `page`
- **Published：** 2026-07-31
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0049"></a>

### H3-0049 · Day-to-Night Relighting

**Reference Generation** · **Official example**

#### Description

A published MiniMax H3 example demonstrating day-to-night relighting, with its exact source prompt and result video.

#### Prompt

```text
Relighting

Change the lighting in the reference video from daytime to night.
```

#### Video

[▶ Play on the video site](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-day-to-night-relighting) · [↗ View the MP4 file in this repository](media/minimax-official-day-to-night-relighting.mp4)

#### Details

- **Parameters：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **Source type：** Official example
- **Source：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **Source location：** `page`
- **Published：** 2026-07-31
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0050"></a>

### H3-0050 · Window View Replacement

**Reference Generation** · **Official example**

#### Description

A published MiniMax H3 example demonstrating window view replacement, with its exact source prompt and result video.

#### Prompt

```text
Live-action environment replacement

Replace the view outside the window in Video 1 with Image 1.
```

#### Video

[▶ Play on the video site](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-window-view-replacement) · [↗ View the MP4 file in this repository](media/minimax-official-window-view-replacement.mp4)

#### Details

- **Parameters：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **Source type：** Official example
- **Source：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **Source location：** `page`
- **Published：** 2026-07-31
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0051"></a>

### H3-0051 · Dialogue & Performance Replacement

**Reference Generation** · **Official example**

#### Description

A published MiniMax H3 example demonstrating dialogue & performance replacement, with its exact source prompt and result video.

#### Prompt

```text
In Video 1, replace the woman’s line—“There’s no way we can be together. It’s not that I don’t love you; we simply can’t make it to the end.”—with the line from Audio 1: “Please don’t go. This time, let’s not let each other go.” Adjust the performance subtly to match the new dialogue.
```

#### Video

[▶ Play on the video site](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-dialogue-performance-replacement) · [↗ View the MP4 file in this repository](media/minimax-official-dialogue-performance-replacement.mp4)

#### Details

- **Parameters：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **Source type：** Official example
- **Source：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **Source location：** `page`
- **Published：** 2026-07-31
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0052"></a>

### H3-0052 · Multi-Element Scene Editing

**Reference Generation** · **Official example**

#### Description

A published MiniMax H3 example demonstrating multi-element scene editing, with its exact source prompt and result video.

#### Prompt

```text
In the reference video: replace the newspaper with a green hardcover book; replace the chair with a red sofa; remove the subject’s sunglasses and reveal a clear face; remove the burning-car effect and restore the vehicle to normal; replace the photograph taken from the coat with a small black notebook; and add a tree on the left side of frame.
```

#### Video

[▶ Play on the video site](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-multi-element-scene-editing) · [↗ View the MP4 file in this repository](media/minimax-official-multi-element-scene-editing.mp4)

#### Details

- **Parameters：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **Source type：** Official example
- **Source：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **Source location：** `page`
- **Published：** 2026-07-31
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0053"></a>

### H3-0053 · Product, Sign & Dialogue Replacement

**Reference Generation** · **Official example**

#### Description

A published MiniMax H3 example demonstrating product, sign & dialogue replacement, with its exact source prompt and result video.

#### Prompt

```text
In the reference video, replace the canned drink shown at the beginning with Coca-Cola. Change the illuminated “FamilyMart” convenience-store sign in the background to “HUHUI.” At the end, replace every snack in the plastic bag with cans of Coca-Cola, and change the final line from “I bought a few snacks” to “I bought a whole bunch of Coke.”
```

#### Video

[▶ Play on the video site](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-product-sign-dialogue-replacement) · [↗ View the MP4 file in this repository](media/minimax-official-product-sign-dialogue-replacement.mp4)

#### Details

- **Parameters：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **Source type：** Official example
- **Source：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **Source location：** `page`
- **Published：** 2026-07-31
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

<a id="h3-0055"></a>

### H3-0055 · Hand-Drawn Romance VFX

**Reference Generation** · **Official example**

#### Description

A published MiniMax H3 example demonstrating hand-drawn romance vfx, with its exact source prompt and result video.

#### Prompt

```text
Creative interpretation + animated graphic effects

Add orange-yellow hand-drawn marks like Image 1 around the two people in Video 1. As they move closer, the marks multiply and build from tiny sparks into bright radiance. When they kiss, introduce pink brushstrokes.
```

#### Video

[▶ Play on the video site](https://ecomimagelab.github.io/awesome-minimax-h3-prompts/#video-minimax-official-hand-drawn-romance-vfx) · [↗ View the MP4 file in this repository](media/minimax-official-hand-drawn-romance-vfx.mp4)

#### Details

- **Parameters：** `duration: 5–15s` · `resolution: 2K` · `ratio: not stated`
- **Tags：** `reference-generation` `official`
- **Source type：** Official example
- **Source：** [MiniMax](https://www.minimax.io/blog/minimax-h3)
- **Source location：** `page`
- **Published：** 2026-07-31
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** Matched to the same prompt and result video in MiniMax's official H3 materials.

---

## Contributing

Submit a prompt through the issue form or a pull request. Include the original author, direct source URL, exact prompt, generation mode, and whether a visible output confirms MiniMax H3. See [CONTRIBUTING.md](docs/CONTRIBUTING.md).

## License and removals

Original repository content is available under [CC BY 4.0](LICENSE). Third-party prompts and media retain their original rights; see [NOTICE.md](NOTICE.md). Rights holders may open a removal request.

---

MiniMax and Hailuo are trademarks of their respective owners. This community project is not affiliated with or endorsed by MiniMax.

Generated from structured data curated through 2026-08-01.
