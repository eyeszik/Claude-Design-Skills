# Claude Design-Skills Registry

A portable, audited, deduplicated registry of Claude design skills for use with Claude Code, Claude Desktop/Web, and other LLM chatbots via GitHub raw links.

**Audited**: 2026-05-11 · **Branch**: `claude/design-skill-audit-FW4TF` · **Repo**: `eyeszik/Claude-Design-Skills`

---

## Quick Start

Share any raw link below directly with Claude or paste the URL into your Claude Code session:

| Skill | Purpose | Raw URL |
|-------|---------|---------|
| `frontend-design` | Bold aesthetic direction, avoids AI slop (Official Anthropic) | [raw](https://raw.githubusercontent.com/anthropics/claude-code/main/plugins/frontend-design/skills/frontend-design/SKILL.md) |
| `brand-guidelines` | Anthropic brand colors + Poppins/Lora typography | [raw](https://raw.githubusercontent.com/anthropics/skills/main/skills/brand-guidelines/SKILL.md) |
| `canvas-design` | Visual art + design philosophy creation | [raw](https://raw.githubusercontent.com/anthropics/skills/main/skills/canvas-design/SKILL.md) |
| `design-taste-frontend` | Anti-slop enforcer, RSC + Tailwind guards (MIT) | [raw](https://raw.githubusercontent.com/Leonxlnx/taste-skill/main/skills/taste-skill/SKILL.md) |
| `interface-design` | Dashboard/app/tool craft + memory system (MIT) | [raw](https://raw.githubusercontent.com/Dammyjay93/interface-design/main/.claude/skills/interface-design/SKILL.md) |
| `design-motion-principles` | 3-designer motion audit (Kowalski/Krehel/Tompkins) (MIT) | [raw](https://raw.githubusercontent.com/kylezantos/design-motion-principles/main/skills/design-motion-principles/SKILL.md) |
| `accessibility` | WCAG 2.2 audit (Addy Osmani) (MIT) | [raw](https://raw.githubusercontent.com/addyosmani/web-quality-skills/main/skills/accessibility/SKILL.md) |
| `remotion-video-creation` | Remotion + React video, 25 progressive rules (MIT) | [raw](https://raw.githubusercontent.com/affaan-m/everything-claude-code/main/skills/remotion-video-creation/SKILL.md) |
| `creative-direction` | 4-axis aesthetic brief for cross-skill coherence (MIT) | [raw](https://raw.githubusercontent.com/rampstackco/claude-skills/main/skills/creative-direction/SKILL.md) |
| `design-system` | Component library + design tokens + governance (MIT) | [raw](https://raw.githubusercontent.com/rampstackco/claude-skills/main/skills/design-system/SKILL.md) |

---

## Repository Structure

```
/sources/          # All audited URLs with classification annotations
/registries/       # Full registry in JSON, Markdown, CSV, and raw-link formats
/skills/           # Copied (MIT) and stub (LINK_ONLY) skill files with metadata
/reports/          # Install plan, manual review, rejected, reference-only, dedupe, token, rollback
/scripts/          # verify-skills.py — verification script
```

## Skill Buckets

| Bucket | Skills |
|--------|--------|
| `frontend-design` | frontend-design, canvas-design, design-taste-frontend, interface-design |
| `brand-guidelines` | brand-guidelines |
| `accessibility` | accessibility |
| `motion` | design-motion-principles, remotion-video-creation |
| `design-systems` | design-system |
| `marketing-design` | creative-direction |
| `skill-development` | skill-development (link-only) |

## Design-Quality Gate

Before installing any skill, it must improve at least one of:
- Visual hierarchy · Usability · Accessibility · Responsiveness
- Composition · Brand alignment · Implementation quality
- Repetitive-prompt reduction · Claude design-failure prevention
- Context efficiency · Clean removal/rollback

## Token Budget Rules

- No more than 4 active skills per project
- Prefer skills with 150 lines or fewer for always-loaded context
- Project-local preferred over global for design skills
- See `/reports/token-minimization-plan.md` for full guidance

## Reports

| Report | Contents |
|--------|---------|
| [install-plan.md](reports/install-plan.md) | INSTALL_NOW + INSTALL_OPTIONAL with install commands |
| [manual-review.md](reports/manual-review.md) | Credentials/MCP/account-required candidates |
| [rejected-risk.md](reports/rejected-risk.md) | 404s, profiles, non-design, inaccessible |
| [reference-only.md](reports/reference-only.md) | Discovery sources and curated lists |
| [dedupe-map.md](reports/dedupe-map.md) | Deduplication decisions and per-project selection guide |
| [token-minimization-plan.md](reports/token-minimization-plan.md) | Token budget, skill size table, archive strategy |
| [rollback-plan.md](reports/rollback-plan.md) | Removal commands and git rollback |
| [inspection-log.md](reports/inspection-log.md) | All commands run during audit, HTTP statuses, risk scan results |

## Verification

```bash
python3 scripts/verify-skills.py
python3 scripts/verify-skills.py --check-urls  # also verify raw GitHub URLs
```

## Next Custom Skills to Build

| Skill | Purpose | Trigger |
|-------|---------|---------|
| `premium-ui-critique` | Holistic visual quality + taste calibration | "review UI", "check design quality" |
| `landing-page-design` | Landing page layout + conversion design | "build landing page", "marketing site" |
| `design-token-extractor` | Extract tokens from Figma/CSS | "extract tokens", "design tokens" |
| `accessibility-quick-audit` | Fast WCAG checklist (60 lines) | "a11y check", "quick accessibility" |
| `figma-to-implementation` | Figma to production code with token mapping | "implement this Figma design" |
| `saas-dashboard-review` | Dashboard-specific design review | "review dashboard", "data density" |

## Hard Rules

- No bulk installs
- No global Claude config mutations
- No credentials stored or exposed
- No MCP servers executed without explicit approval
- No browser automation without explicit approval
- All Anthropic skills remain link-only until license is verified
