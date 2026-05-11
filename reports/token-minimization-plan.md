# Token Minimization Plan — Claude Design-Skill Registry
> Audited: 2026-05-11T00:53:02Z

---

## Guiding Principles

1. Every active skill adds to context on every turn — minimize to what the current project needs.
2. Prefer ≤150 line skills for always-loaded context; use larger skills only project-locally.
3. Progressive disclosure: small index file + external references loaded on demand > monolithic SKILL.md.
4. No more than 3–4 skills active simultaneously in any single project.
5. Archive skills not used in the last 2 weeks to reduce noise.

---

## Skill Size Reference

| Skill | Lines | Token Est. | Classification |
|-------|-------|-----------|----------------|
| frontend-design | 41 | ~500 tokens | Lightweight ✓ |
| brand-guidelines | 73 | ~900 tokens | Lightweight ✓ |
| remotion-video-creation | 43 | ~550 tokens | Lightweight ✓ (rules loaded on demand) |
| canvas-design | 129 | ~1,600 tokens | Moderate ✓ |
| creative-direction | 153 | ~1,900 tokens | Moderate ✓ |
| design-motion-principles | 203 | ~2,500 tokens | Moderate — project-local only |
| design-system | ~200 | ~2,500 tokens | Moderate — project-local only |
| design-taste-frontend | 226 | ~2,800 tokens | Moderate — project-local only |
| accessibility | ? | ~? | Moderate — project-local only |
| mcp-builder | 236 | ~3,000 tokens | LINK_ONLY |
| interface-design | 391 | ~4,900 tokens | Large — project-local dashboard projects only |
| skill-development | 637 | ~7,900 tokens | LINK_ONLY — do not load as active skill |

---

## Which Skills Should Be Project-Local

**Always project-local (context is project-specific):**
- `design-taste-frontend` — parameterized design variance; values depend on project style
- `interface-design` — dashboard/app specific; irrelevant for marketing sites
- `design-motion-principles` — motion audit; only relevant during motion review sessions
- `design-system` — only relevant when building a design system
- `remotion-video-creation` — only relevant in Remotion projects
- `creative-direction` — generates project-specific aesthetic brief; don't carry between projects
- `accessibility` — useful as project-local; run during accessibility review sessions

**Can be global (brand/style applies across projects):**
- `brand-guidelines` — Anthropic brand identity is stable across projects (global after license verified)
- `canvas-design` — visual art creation workflow; stable across projects

---

## Which Skills Should NEVER Be Global

| Skill | Reason |
|-------|--------|
| `skill-development` (637 lines) | 7,900 tokens on every turn regardless of task; only needed when building skills |
| `mcp-builder` (236 lines) | Only needed when building MCP integrations; not general-purpose |
| `interface-design` (391 lines) | Dashboard-specific; irrelevant on marketing/landing page projects |
| `design-taste-frontend` (226 lines) | Parameterized values are project-specific; global defaults may conflict |

---

## Active Skill Limit Recommendations

| Project Type | Recommended Active Skills | Avoid |
|-------------|--------------------------|-------|
| Landing page / marketing site | frontend-design + creative-direction | interface-design, design-motion-principles |
| SaaS dashboard / app | interface-design + accessibility | frontend-design, creative-direction |
| Design system build | design-system + design-taste-frontend | interface-design, canvas-design |
| Remotion video project | remotion-video-creation | all design-focused skills |
| Brand work | brand-guidelines + creative-direction | design-taste-frontend |
| Motion/interaction review | design-motion-principles | all others |

**Rule**: Never exceed 4 active skills per project context.

---

## How to Archive Rarely Used Skills

```bash
# Move to reference-wrappers when not actively used
mv /your-project/.claude/skills/design-motion-principles/ \
   /your-project/.claude/skills/archived/design-motion-principles/

# Or remove entirely and reinstall when needed via raw URL
rm -rf /your-project/.claude/skills/design-motion-principles/
# Reinstall: curl -o SKILL.md https://raw.githubusercontent.com/...
```

**Archive trigger**: If a skill hasn't been triggered in the last 10 working sessions, archive it.

---

## How to Avoid Metadata Bloat

- Keep `source-metadata.json` files ≤ 20 fields (enforced in this registry).
- Do not embed full SKILL.md content in metadata files.
- Do not store screenshots, examples, or generated assets in the registry.
- Use raw URL references instead of copying large content.
- Use one `source-metadata.json` per skill — never per session.

---

## How to Convert Broad Guidance Into Small Custom Skills

Instead of installing a 400-line design guide, distill it into a ≤100-line skill that covers only what your project needs:

```markdown
---
name: my-project-design-rules
description: Design constraints for [project name]. Use when building UI components, pages, or reviewing designs.
---

# [Project] Design Rules

## Typography
- Headings: Fraunces (display), 700 weight
- Body: Inter, 400/500 weight
- Scale: 12/14/16/20/24/32/48px

## Colors
- Primary: #1a1a2e
- Accent: #e94560

## Spacing
- Base unit: 4px; use 8/16/24/32/48px steps

## Component Rules
- Buttons: 8px radius, 48px min height
- Cards: 16px padding, 1px border #e2e8f0

## Do Not
- No generic purple gradients
- No system fonts
- No absolute positioning for layout
```

This 30-line custom skill outperforms a 400-line generic guide in token efficiency and precision.
