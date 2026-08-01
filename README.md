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
> **Copyright and verification notice：** Public availability does not remove an author's rights. Every entry preserves attribution and a direct source link. `H3 confirmed: No` means the prompt was published for H3 but the source did not show a verifiable H3 result. Third-party media is linked rather than copied.

## Library statistics

| Metric | Count |
| --- | ---: |
| Total prompts | **11** |
| Official examples | **5** |
| Community tested | **2** |
| Community guide templates | **4** |
| Last curated | **2026-08-01** |

## Browse by mode

- [Text to Video (7)](#text-to-video)
- [Image to Video (1)](#image-to-video)
- [First / Last Frame (1)](#first-last-frame)
- [Reference Generation (2)](#reference-generation)

## Featured prompts

- [Drone-riding TikTok dancer](#h3-0001) — Official example
- [Contemporary dance from a first frame](#h3-0002) — Official example
- [A little girl grows up](#h3-0003) — Official example
- [Vintage beret fashion walk](#h3-0004) — Official example
- [Hitchcock move with referenced singer and audio](#h3-0005) — Official example
- [Frutiger Aero shopping mall walk](#h3-0007) — Community tested

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
