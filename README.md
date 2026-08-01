<p align="center"><img src="public/cover.svg" alt="Awesome MiniMax H3 Prompts" width="100%"></p>

# Awesome MiniMax H3 Prompts

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](LICENSE)
[![Validate data](https://github.com/ecomimagelab/awesome-minimax-h3-prompts/actions/workflows/validate.yml/badge.svg)](https://github.com/ecomimagelab/awesome-minimax-h3-prompts/actions/workflows/validate.yml)

> A curated bilingual library of public prompts, examples, and prompting patterns for MiniMax H3.

[简体中文](README_zh.md) · **English**

## About MiniMax H3

MiniMax H3 is a multimodal video generation model that accepts text, images, video, and audio as context. This repository separates official examples, community-tested prompts, and unverified guide templates so readers can judge the evidence behind every entry.

- Official model: `MiniMax-H3`
- Output: up to 2K, 4–15 seconds
- Inputs: text, image, video, and audio references
- Official guide: [MiniMax H3 Video Generation](https://platform.minimax.io/docs/guides/video-generation)

> [!IMPORTANT]
> **Copyright and verification notice：** Public availability does not remove an author's rights. Publicly accessible media may be mirrored for research, discovery, and click-to-play viewing; every entry preserves attribution, the original URL, and retrieval metadata. Mirrored third-party material is excluded from this repository's CC BY 4.0 license and can be removed through the rights-holder request form. `H3 confirmed: No` means the source did not show a verifiable H3 result.

## Library statistics

| Metric | Count |
| --- | ---: |
| Total prompts | **16** |
| Official examples | **5** |
| Community tested | **7** |
| Community guide templates | **4** |
| Last curated | **2026-08-01** |

## Browse by mode

- [Text to Video (11)](#text-to-video)
- [Image to Video (2)](#image-to-video)
- [First / Last Frame (1)](#first-last-frame)
- [Reference Generation (2)](#reference-generation)

## Featured prompts

- [Drone-riding TikTok dancer](#h3-0001) — Official example
- [Contemporary dance from a first frame](#h3-0002) — Official example
- [A little girl grows up](#h3-0003) — Official example
- [Vintage beret fashion walk](#h3-0004) — Official example
- [Hitchcock move with referenced singer and audio](#h3-0005) — Official example
- [Frutiger Aero shopping mall walk](#h3-0007) — Community tested
- [Don't say my name again](#h3-0012) — Community tested
- [The unanswered letter](#h3-0013) — Community tested
- [I can see the dust](#h3-0014) — Community tested

## All prompts

## Text to Video

<a id="h3-0001"></a>

### H3-0001 · Drone-riding TikTok dancer

**Text to Video** · **Official example** · ⭐ Featured

#### Description

A compact official text-to-video API example focused on acrobatic motion.

#### Prompt

```text
A tiktok dancer is dancing on a drone, doing flips and tricks.
```

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

<a id="h3-0008"></a>

### H3-0008 · Traveler crossing a desert ridge

**Text to Video** · **Community guide**

#### Description

A public H3-oriented cinematic template with clear motion, environment response, camera path, and end state.

#### Prompt

```text
Wide cinematic shot of a lone traveler crossing a windswept desert at sunset. He leans forward against the wind while his coat and scarf stream naturally behind him; fine sand curls around his boots with each step. The camera performs a slow lateral tracking move at waist height, maintaining his profile. Warm backlight, long shadows, restrained teal-and-orange grade. One continuous shot ending as he stops on the ridge and sees a distant city.
```

#### Details

- **Parameters：** `duration: not stated` · `resolution: not stated` · `ratio: landscape`
- **Tags：** `cinematic` `desert` `tracking-shot` `community-guide`
- **Source type：** Community guide
- **Source：** [VideoToPrompt](https://www.videotoprompt.app/posts/hailuo-h3-prompt-guide)
- **Published：** 2026-07-21
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ⚪ No · Output visible ⚪ No
- **Note：** Published as an H3 prompt template; no generated H3 output is shown beside the prompt.

---

<a id="h3-0009"></a>

### H3-0009 · Premium citrus drink advertisement

**Text to Video** · **Community guide**

#### Description

A public product-ad template designed around liquid physics, label stability, and a controlled orbit.

#### Prompt

```text
Macro product shot of a chilled citrus drink can standing upright on black stone. A thin stream of water strikes the surface beside it, producing a controlled splash that wraps around the base while condensation beads slide down the aluminum. The camera makes a slow 30-degree clockwise orbit, keeping the logo sharp and facing forward. Crisp studio rim lighting, dark premium commercial style. End with the splash settled and the can centered.
```

#### Details

- **Parameters：** `duration: not stated` · `resolution: not stated` · `ratio: landscape`
- **Tags：** `product` `advertising` `water-physics` `orbit` `community-guide`
- **Source type：** Community guide
- **Source：** [VideoToPrompt](https://www.videotoprompt.app/posts/hailuo-h3-prompt-guide)
- **Published：** 2026-07-21
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ⚪ No · Output visible ⚪ No
- **Note：** Published as an H3 prompt template; no generated H3 output is shown beside the prompt.

---

<a id="h3-0010"></a>

### H3-0010 · Handheld vacuum creator review

**Text to Video** · **Community guide**

#### Description

A public vertical UGC template with explicit hand use, product interaction, and natural facial behavior.

#### Prompt

```text
Vertical smartphone video of a woman in a bright apartment demonstrating a compact handheld vacuum. She looks into the lens, raises the product with her right hand, points to its nozzle with her left index finger, then bends slightly and cleans crumbs from the sofa in one smooth pass. Natural blinking and conversational expression. Light handheld camera movement, soft window light, authentic creator-review style, no cuts.
```

#### Details

- **Parameters：** `duration: not stated` · `resolution: not stated` · `ratio: 9:16`
- **Tags：** `ugc` `product-demo` `vertical-video` `community-guide`
- **Source type：** Community guide
- **Source：** [VideoToPrompt](https://www.videotoprompt.app/posts/hailuo-h3-prompt-guide)
- **Published：** 2026-07-21
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ⚪ No · Output visible ⚪ No
- **Note：** Published as an H3 prompt template; no generated H3 output is shown beside the prompt.

---

<a id="h3-0011"></a>

### H3-0011 · Anime rooftop swordswoman

**Text to Video** · **Community guide**

#### Description

A public anime-action template with a chronological movement chain and parallel camera tracking.

#### Prompt

```text
Anime-style medium-wide shot of a teenage swordswoman sprinting across rain-soaked rooftops at night. Her feet push off each tile in sequence, loose roof fragments slide behind her, and her coat follows the direction of motion. The camera tracks parallel at full-body distance, then gradually moves ahead as she leaps across a narrow alley. Bold linework, dramatic blue moonlight, rain streaks, controlled motion blur. She lands in a balanced crouch.
```

#### Details

- **Parameters：** `duration: not stated` · `resolution: not stated` · `ratio: landscape`
- **Tags：** `anime` `action` `rain` `tracking-shot` `community-guide`
- **Source type：** Community guide
- **Source：** [VideoToPrompt](https://www.videotoprompt.app/posts/hailuo-h3-prompt-guide)
- **Published：** 2026-07-21
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ⚪ No · Output visible ⚪ No
- **Note：** Published as an H3 prompt template; no generated H3 output is shown beside the prompt.

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

#### Video

[▶ Play the original video](media/alex-patrascu-minimax-h3-scenes.mp4)

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

#### Video

[▶ Play the original video](media/alex-patrascu-minimax-h3-scenes.mp4)

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

#### Video

[▶ Play the original video](media/alex-patrascu-minimax-h3-scenes.mp4)

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

#### Video

[▶ Play the original video](media/alex-patrascu-minimax-h3-scenes.mp4)

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

## Image to Video

<a id="h3-0002"></a>

### H3-0002 · Contemporary dance from a first frame

**Image to Video** · **Official example** · ⭐ Featured

#### Description

An official image-to-video example that animates the people in a supplied first frame.

#### Prompt

```text
Contemporary dance, the people in the picture are performing contemporary dance.
```

#### Details

- **Parameters：** `duration: 5s` · `resolution: 2K` · `ratio: adaptive`
- **Tags：** `dance` `human-motion` `first-frame` `official`
- **Source type：** Official example
- **Source：** [MiniMax](https://platform.minimax.io/docs/guides/video-generation)
- **Published：** 2026-07-31
- **Retrieved：** 2026-08-01
- **Verification：** Prompt visible ✅ Yes · H3 confirmed ✅ Yes · Output visible ✅ Yes
- **Note：** Published with a first-frame input in the official API guide.

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

#### Video

[▶ Play the original video](media/alex-patrascu-minimax-h3-scenes.mp4)

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

## Reference Generation

<a id="h3-0004"></a>

### H3-0004 · Vintage beret fashion walk

**Reference Generation** · **Official example** · ⭐ Featured

#### Description

An official reference-image example for subject consistency and cinematic fashion motion.

#### Prompt

```text
On an overcast day, in an ancient cobbled alleyway, the model walks and adjusts a vintage beret with a smile; natural lighting and cinematic colors.
```

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

## Contributing

Submit a prompt through the issue form or a pull request. Include the original author, direct source URL, exact prompt, generation mode, and whether a visible output confirms MiniMax H3. See [CONTRIBUTING.md](docs/CONTRIBUTING.md).

## License and removals

Original repository content is available under [CC BY 4.0](LICENSE). Third-party prompts and media retain their original rights; see [NOTICE.md](NOTICE.md). Rights holders may open a removal request.

---

MiniMax and Hailuo are trademarks of their respective owners. This community project is not affiliated with or endorsed by MiniMax.

Generated from structured data curated through 2026-08-01.
