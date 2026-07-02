---
name: design-skill-router
description: >-
  Master design intelligence router. Use for ANY design, UI, visual, or creative
  request: landing pages, hero sections, marketing sites, UI critique, premium
  aesthetics, SaaS dashboards, admin panels, data interfaces, Figma files or URLs,
  design-to-code, accessibility audits (full or fast), WCAG compliance, design
  tokens, Tailwind tokens, CSS variables, motion design, animation, micro-
  interactions, Remotion video, brand guidelines, canvas art, illustration, design
  systems, component libraries, creative direction, AI ad creative, UGC videos,
  Arcads, Sora, Veo, Kling, YouTube thumbnails. Single entry point. Routes
  silently to the correct specialist and applies its complete methodology.
---

# Design Skill Router

Classify the user's intent, load the matching specialist skill, apply its complete methodology, and return output that skill defines — silently, without surfacing this routing layer.

---

## Phase 1 — Classify

### Force Signals [apply before scoring; highest precedence]
| Signal in query | Route to |
|---|---|
| `quick` `fast` `pre-ship` `component` + a11y keyword | `accessibility-quick-audit` |
| `video` `remotion` `React animation` `composition` | `remotion-video-creation` |
| `dashboard` `admin panel` `analytics` `data table` `settings page` | `saas-dashboard-review` |
| `figma.com` `.fig` `design spec` `Figma URL` `node-id` | `figma-to-implementation` |
| `Arcads` `Sora2` `Veo3` `Kling` `Nano Banana` `UGC video` `b-roll` | `arcads-external-api` |
| `YouTube thumbnail` `thumbnail batch` `Nano Banana 2` | `generate-youtube-thumbnail` |
| `design token` `token architecture` `CSS variable` `Style Dictionary` | `design-token-extractor` |
| `landing page` `hero section` `product page` `marketing site` `CTA` | `landing-page-design` |

### Intent Scoring [when no force signal matches]
Compute semantic match against each skill's TRIGGER field below.
- Score ≥ 0.70 → load that skill
- Score 0.60–0.69 → load + note low confidence internally
- Score < 0.60 → load closest match + state gap to user
- Two scores within 0.05 of each other → MULTI_SKILL (see Phase 3)

---

## Phase 2 — Load

### LOCAL skills
Read directly from the installed path under `.claude/skills/` or the repo root.
`retry_safe=true`. If file unreadable → surface: "Skill file missing at [path] — reinstall from registry."

### FETCH skills
`GET [raw_url]` → assert HTTP 200 → `sha256(body)` compare against `registered_sha`.
- SHA mismatch → proceed with note: "Skill content may have changed upstream — validate output."
- HTTP failure → fall back to LOCAL stub if present → note `[DEGRADED:fetch_fail]`
- After fetch: extract frontmatter `name:` + `description:` and confirm they match registry entry. Significant semantic drift → note `[SKILL_MUTATED]`.

### CHAIN skills
Load all listed dependencies first in order. Enforce handoff contract between each:
`{output_schema, sha256(prior_output), timestamp_iso8601}` — halt chain on contract failure.

### CREDENTIAL_REQUIRED skills
Before executing: emit exactly once — *"This skill requires `[VAR]` set in `.env`. Run `./scripts/setup.sh` if not configured."*
If env is absent: offer dry-run simulation mode. Await signal or proceed with simulation.
`retry_safe=false` — API call side effects; do not retry silently.

---

## Phase 3 — Execute

### Single skill
Inject full skill content into context. Apply every step the skill defines. Output exactly what that skill's output format specifies.

### MULTI_SKILL [tie-break or compound query]
- Execute each matched skill in isolated scope — no shared context between skills mid-execution.
- Budget allocation: LEAN (≤200 lines) = 1× share · DENSE (>200 lines) = 2× share.
- Token overflow: drop lowest-confidence DENSE skill → retry with n-1. Never truncate a skill mid-read.
- Merge outputs at synthesis layer under a unified schema with clear section headings per skill.

### AESTHETIC_ETHICS [post-execution · creative skills only · non-blocking]
After generating any aesthetic recommendation (color, typography, motion, layout):
- Check: contrast ratio ≥ 4.5:1 body / 3:1 large · no auto-play motion without `prefers-reduced-motion` guard · colorblind-safe palette · dyslexia-friendly type if body copy.
- Violations → append `[WCAG_FLAG: criterion=<WCAG_ID>, fix=<one-sentence correction>]` inline. Do not block or rewrite — annotate only.

---

## Phase 4 — Error Protocol

| Failure | Response |
|---|---|
| `url_fail` | Use LOCAL stub → `[DEGRADED:fetch_fail·using_stub]` |
| `sha_mismatch` | Proceed → `[STALE_SKILL:validate_output]` |
| `chain_break` | Emit completed steps → `[PARTIAL:chain_id,failed_at=<step>]` |
| `budget_exhaust` | Drop lowest-confidence skill → retry n-1 |
| `all_scores<0.60` | `[NO_MATCH]` → surface nearest skill + state what's missing |
| `skill_mutated` | `[SKILL_MUTATED:Δ=<diff>]` → flag for human review → proceed |
| `credential_missing` | Offer dry-run → await or simulate |

---

## Skill Registry

> **KEY** — MODE: `F`=FETCH `L`=LOCAL · DENSITY: `D`=Dense >200 lines `N`=Lean ≤200 lines · `SHA`=registered commit · `CRED`=required env var · `DEP`=chain dependency

### Design & Frontend

| Skill | M | Den | SHA | TRIGGER (key signals) | Path / URL |
|---|---|---|---|---|---|
| `brand-guidelines` | F | N | f458cee | Anthropic brand, colors #141413 #d97757, Poppins/Lora, logo, tone | `rgh/anthropics/skills/main/skills/brand-guidelines/SKILL.md` |
| `canvas-design` | F | N | f458cee | Visual art, illustration, generative image, canvas, two-step visual philosophy | `rgh/anthropics/skills/main/skills/canvas-design/SKILL.md` |
| `design-taste-frontend` | L | D | — | Anti-slop React/Tailwind/RSC, production aesthetics, DESIGN_VARIANCE, reject AI defaults | `.claude/skills/frontend-design/design-taste-frontend/SKILL.md` |
| `interface-design` | L | D | — | Product interfaces, apps, tools, NOT marketing pages, dashboards/tools/admin craft | `.claude/skills/frontend-design/interface-design/SKILL.md` |
| `premium-ui-critique` | L | N | — | UI review, visual quality, hierarchy, spacing, typography, color, 7-axis critique | `.claude/skills/frontend-design/premium-ui-critique/SKILL.md` |
| `landing-page-design` | L | N | — | Landing page, hero, product page, marketing site, CTA, section architecture | `.claude/skills/frontend-design/landing-page-design/SKILL.md` |
| `saas-dashboard-review` | L | N | — | SaaS dashboard, admin panel, analytics, data density, navigation architecture | `.claude/skills/frontend-design/saas-dashboard-review/SKILL.md` |

### Figma & Tokens

| Skill | M | Den | SHA | TRIGGER | Path / URL |
|---|---|---|---|---|---|
| `figma-to-implementation` | L | N | — | Figma URL, .fig, design spec, screenshot → production code, token mapping, handoff | `.claude/skills/figma-workflows/figma-to-implementation/SKILL.md` |
| `design-token-extractor` | L | N | — | Design tokens, primitive→semantic→component, CSS vars, Tailwind config, Style Dictionary | `.claude/skills/design-tokens/design-token-extractor/SKILL.md` |
| `design-system` | L | D | — | Component library, token governance, contribution model, documentation, design system build | `.claude/skills/design-systems/design-system/SKILL.md` |

### Accessibility

| Skill | M | Den | SHA | TRIGGER | Path / URL |
|---|---|---|---|---|---|
| `accessibility` | L | D | — | Full WCAG 2.2 audit, comprehensive, 50+ criteria, full page or app | `.claude/skills/accessibility/accessibility/SKILL.md` |
| `accessibility-quick-audit` | L | N | — | Fast a11y check, pre-ship, single component, 12-point checklist, <2 minutes | `.claude/skills/accessibility/accessibility-quick-audit/SKILL.md` |

### Motion & Video

| Skill | M | Den | SHA | TRIGGER | Path / URL |
|---|---|---|---|---|---|
| `design-motion-principles` | L | D | — | Animation audit, motion design, transitions, micro-interactions, Kowalski/Krehel/Tompkins | `.claude/skills/motion/design-motion-principles/SKILL.md` |
| `remotion-video-creation` | L | N | — | Programmatic video, Remotion, React compositions, sequences, video export | `.claude/skills/motion/remotion-video-creation/SKILL.md` |

### Marketing & Brand

| Skill | M | Den | SHA | TRIGGER | Path / URL |
|---|---|---|---|---|---|
| `creative-direction` | L | N | — | Creative brief, 4-axis aesthetic (mood/palette/motion/type), brand personality | `.claude/skills/marketing-design/creative-direction/SKILL.md` |

### Creative Tools (API-gated)

| Skill | M | Den | SHA | CRED | DEP | TRIGGER | Path / URL |
|---|---|---|---|---|---|---|---|
| `arcads-external-api` | F | D | b50ff8e | ARCADS_API_KEY | — | Arcads, AI video, UGC, Sora2, Veo3.1, Kling, Nano Banana, b-roll, influencer | `rgh/krusemediallc/arcads-claude-code/main/skills/arcads-external-api/SKILL.md` |
| `generate-youtube-thumbnail` | F | N | b50ff8e | ARCADS_API_KEY | arcads-external-api | YouTube thumbnail, thumbnail batch, Nano Banana 2 image endpoint | `rgh/krusemediallc/arcads-claude-code/main/skills/generate-youtube-thumbnail/SKILL.md` |

> `rgh` = `https://raw.githubusercontent.com`

---

## Output Contract

- Output format, section structure, and rating schema are defined by the loaded skill — follow them exactly.
- In MULTI_SKILL: separate loaded skills' outputs with clear `---` dividers and skill name headers.
- AESTHETIC_ETHICS flags appear inline immediately after the flagged recommendation.
- Never surface router names, phase labels, confidence scores, SHA values, or routing decisions in output.
- If no skill matches: state what design domain the query falls into and which skill would be closest if installed.
