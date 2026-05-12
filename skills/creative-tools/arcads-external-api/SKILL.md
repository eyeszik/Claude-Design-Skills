---
name: arcads-external-api
description: >-
  Creates and retrieves AI video and image assets via the Arcads external API
  (Seedance 2.0, Sora 2, Veo 3.1, Kling, Grok Video, Nano Banana, b-roll, scene,
  script/actor flows). Loads prompts from the bundled prompting guide and model
  library, respects HTTP Basic auth from ARCADS_API_KEY, and polls assets/videos
  until ready. Use when the user mentions Arcads, external-api.arcads.ai, Seedance,
  Sora2, Veo, Kling, Nano Banana, b-roll, UGC scripts, or generating marketing
  creative through Arcads.
---

# LINK_ONLY — No license file in source repository

This skill is available at the canonical source below. No license file was found
in `krusemediallc/arcads-claude-code`, so the full content is not copied here.

**Canonical raw URL:**
https://raw.githubusercontent.com/krusemediallc/arcads-claude-code/main/skills/arcads-external-api/SKILL.md

**Source repo:** https://github.com/krusemediallc/arcads-claude-code

**Prerequisites before use:**
- Arcads account at arcads.ai
- `ARCADS_API_KEY` set in `.env`
- Run `./scripts/setup.sh` for first-time setup

**Companion skill:** `generate-youtube-thumbnail` — YouTube thumbnail batch workflow
using the Nano Banana 2 image endpoint.
https://raw.githubusercontent.com/krusemediallc/arcads-claude-code/main/skills/generate-youtube-thumbnail/SKILL.md
