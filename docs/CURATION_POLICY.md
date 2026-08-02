# Curation and attribution policy

This library publishes a case only when its original output video has been
downloaded into the repository and can be played from the GitHub Pages site.

## Deduplication

- Compare exact file hashes first, then sampled-frame perceptual similarity and
  a manual visual check for re-encoded copies.
- Do not publish a second case card for the same output video.
- When one output has multiple useful prompt variants, keep one video and group
  the prompt variants beneath it.

## Source precedence

Attribution follows the earliest authoritative source that can be verified:

1. MiniMax official materials
2. The original public creator post
3. A public republisher or secondary guide

If a secondary guide republishes the same MiniMax official prompt and result,
the case is attributed to MiniMax and is not imported a second time from the
secondary page. A genuinely non-overlapping example keeps its own public source.

## Video-only cases

A public video with no visible prompt may be included only after the original
video is stored locally. Its prompt is reconstructed from the visible result and
must be clearly labeled as reconstructed rather than quoted from the creator.
