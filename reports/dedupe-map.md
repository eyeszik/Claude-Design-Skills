# Deduplication Map — Claude Design-Skill Registry
> Audited: 2026-05-11T00:53:02Z

These decisions prevent redundant skill overlap that wastes context tokens and produces conflicting instructions.

---

## Frontend Design Bucket (3 candidates, all kept — different specializations)

| Removed / Lower Priority | Kept Instead | Reason |
|--------------------------|--------------|--------|
| None removed | frontend-design (92) + design-taste-frontend (82) + interface-design (79) | These complement: frontend-design = broad aesthetic direction; design-taste-frontend = anti-slop rules enforcement; interface-design = dashboard/app specialization. Do NOT install all three simultaneously — pick 1–2 per project. |

**Per-project selection guide:**
- Marketing site, landing page, product page → `frontend-design`
- SaaS app, dashboard, admin panel → `interface-design`
- Any project needing anti-slop enforcement + Tailwind guards → `design-taste-frontend`

---

## Brand / Identity Bucket (2 candidates, scoped differently)

| Removed / Lower Priority | Kept Instead | Reason |
|--------------------------|--------------|--------|
| rampstackco/brand-identity (203 lines, not installed) | anthropic/brand-guidelines (73 lines, INSTALL_NOW) | brand-guidelines is official, concise, Anthropic-specific. rampstackco/brand-identity is generic and larger — referenced via raw URL only. |
| rampstackco/design-standards (213 lines, not installed) | design-taste-frontend (226 lines, installed) | taste-skill already enforces production design standards; design-standards adds redundant coverage. |

---

## Motion / Video Bucket (2 candidates, different scopes)

| Removed / Lower Priority | Kept Instead | Reason |
|--------------------------|--------------|--------|
| remotion-dev/skills (internal, no docs) | affaan-m/remotion-video-creation (MIT, 43 lines) | remotion-dev/skills is an internal package with no documentation; affaan-m has a properly documented SKILL.md with progressive rule loading. |
| None removed | design-motion-principles (web UI motion) + remotion-video-creation (video creation) | These don't overlap: motion-principles audits CSS/React animations; remotion-video-creation is for Remotion video production. |

---

## Accessibility Bucket (2 candidates, different approaches)

| Removed / Lower Priority | Kept Instead | Reason |
|--------------------------|--------------|--------|
| accesslint/claude-marketplace | addyosmani/accessibility (INSTALL_OPTIONAL) | addyosmani is text-based WCAG 2.2 audit installable as a skill. accesslint requires MCP + browser automation — too much infrastructure for accessibility review. Use accesslint only if live DOM auditing is specifically required. |

---

## Marketing / Creative Direction Bucket (scoped)

| Removed / Lower Priority | Kept Instead | Reason |
|--------------------------|--------------|--------|
| rampstackco/landing-page-copy (260 lines) | creative-direction (153 lines) | creative-direction is upstream aesthetic brief that governs landing pages. landing-page-copy is copy-only — not design layout. Reference via raw URL; do not install both unless explicitly doing copy + design work. |

---

## Skill Development Bucket (scoped)

| Removed / Lower Priority | Kept Instead | Reason |
|--------------------------|--------------|--------|
| mcp-builder (236 lines, LINK_ONLY) | skill-development (637 lines, LINK_ONLY) | Both are link-only due to unknown license. mcp-builder is narrower (MCP servers only); skill-development covers all skill creation. Use skill-development when building any skill; mcp-builder only when specifically building MCP integrations. |

---

## Large Packs (All Mined, None Installed as Packs)

| Removed / Lower Priority | Kept Instead | Reason |
|--------------------------|--------------|--------|
| partme-ai/full-stack-skills (421+ skills) | Individual skills from verified sources | Do not bulk install; mine specific skills when needed |
| Jeffallan/claude-skills (66 skills) | Individual skills from verified sources | Mostly dev/infra; no design-specific skills worth installing |
| wondelai/skills (50+ skills) | Raw URL reference only | Business/UX focus; mine if UX methodology skills are needed |

---

## Awesome Lists (All Reference-Only)

| Removed / Lower Priority | Kept Instead | Reason |
|--------------------------|--------------|--------|
| All 4 awesome lists | Raw link index in /registries/raw-links.md | Awesome lists are discovery tools only; specific skills are already cataloged with direct raw URLs |
