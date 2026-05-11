# Install Plan — Claude Design-Skill Registry
> Audited: 2026-05-11T00:53:02Z · No Claude account installations performed yet

This plan covers INSTALL_NOW and INSTALL_OPTIONAL candidates only.
Stop before actual installation — verify license and token cost first.

---

## INSTALL_NOW (Score 85–100)

| Skill | Bucket | Source URL | Raw URL | Install Target | Score | Reason | Token Note | Risk |
|-------|--------|-----------|---------|----------------|-------|--------|------------|------|
| frontend-design | frontend-design | [GitHub](https://github.com/anthropics/claude-code/blob/main/plugins/frontend-design/skills/frontend-design/SKILL.md) | [raw](https://raw.githubusercontent.com/anthropics/claude-code/main/plugins/frontend-design/skills/frontend-design/SKILL.md) | project-local | 92 | Official Anthropic; 41 lines; bold aesthetic direction; avoids AI slop | 41 lines — excellent | License unknown — link-only until verified |
| brand-guidelines | brand-guidelines | [GitHub](https://github.com/anthropics/skills/blob/main/skills/brand-guidelines/SKILL.md) | [raw](https://raw.githubusercontent.com/anthropics/skills/main/skills/brand-guidelines/SKILL.md) | global-after-approval | 88 | Official Anthropic; 73 lines; Anthropic-specific colors + Poppins/Lora typography | 73 lines — good | License unknown — link-only until verified |
| canvas-design | frontend-design | [GitHub](https://github.com/anthropics/skills/blob/main/skills/canvas-design/SKILL.md) | [raw](https://raw.githubusercontent.com/anthropics/skills/main/skills/canvas-design/SKILL.md) | project-local | 85 | Official Anthropic; 129 lines; visual art + design philosophy creation | 129 lines — acceptable | License unknown — link-only until verified |

**Install command (once approved):**
```bash
# Via Claude Code skills platform (preferred — handles license automatically)
# /plugin marketplace add anthropics/claude-code --skill frontend-design
# /plugin marketplace add anthropics/skills --skill brand-guidelines
# /plugin marketplace add anthropics/skills --skill canvas-design
```

---

## INSTALL_OPTIONAL (Score 70–84)

| Skill | Bucket | Source URL | Raw URL | Repo Path | Install Target | Score | Reason | Token Note | Risk |
|-------|--------|-----------|---------|-----------|----------------|-------|--------|------------|------|
| design-taste-frontend | frontend-design | [GitHub](https://github.com/Leonxlnx/taste-skill/blob/main/skills/taste-skill/SKILL.md) | [raw](https://raw.githubusercontent.com/Leonxlnx/taste-skill/main/skills/taste-skill/SKILL.md) | skills/frontend-design/design-taste-frontend/ | project-local | 82 | MIT; 226 lines; anti-slop enforcer with parameterized design variance (8/6/4); RSC + Tailwind guards | 226 lines — moderate; project-local only | None |
| interface-design | frontend-design | [GitHub](https://github.com/Dammyjay93/interface-design/blob/main/.claude/skills/interface-design/SKILL.md) | [raw](https://raw.githubusercontent.com/Dammyjay93/interface-design/main/.claude/skills/interface-design/SKILL.md) | skills/frontend-design/interface-design/ | project-local | 79 | MIT; 391 lines; dashboard/app/tools focus; memory + audit workflow | 391 lines — use only for dashboard projects | None |
| design-motion-principles | motion-design | [GitHub](https://github.com/kylezantos/design-motion-principles/blob/main/skills/design-motion-principles/SKILL.md) | [raw](https://raw.githubusercontent.com/kylezantos/design-motion-principles/main/skills/design-motion-principles/SKILL.md) | skills/motion/design-motion-principles/ | project-local | 78 | MIT; 203 lines; 3-designer audit (Kowalski/Krehel/Tompkins); context-aware weighting | 203 lines — moderate | None |
| accessibility | accessibility-review | [GitHub](https://github.com/addyosmani/web-quality-skills/blob/main/skills/accessibility/SKILL.md) | [raw](https://raw.githubusercontent.com/addyosmani/web-quality-skills/main/skills/accessibility/SKILL.md) | skills/accessibility/accessibility/ | project-local | 76 | MIT; WCAG 2.2; Addy Osmani; stack-agnostic | Unknown line count | None |
| remotion-video-creation | remotion-video | [GitHub](https://github.com/affaan-m/everything-claude-code/blob/main/skills/remotion-video-creation/SKILL.md) | [raw](https://raw.githubusercontent.com/affaan-m/everything-claude-code/main/skills/remotion-video-creation/SKILL.md) | skills/motion/remotion-video-creation/ | project-local | 74 | MIT; 43 lines index + 25 progressive rule files; token-efficient | 43 lines — excellent; rules loaded on demand | External rules not bundled in this stub |
| creative-direction | marketing-design | [GitHub](https://github.com/rampstackco/claude-skills/blob/main/skills/creative-direction/SKILL.md) | [raw](https://raw.githubusercontent.com/rampstackco/claude-skills/main/skills/creative-direction/SKILL.md) | skills/marketing-design/creative-direction/ | project-local | 73 | MIT; 153 lines; 4-axis aesthetic brief for cross-skill coherence | 153 lines — good | Dedupes with brand-guidelines; use for multi-touchpoint projects |
| design-system | design-system-architecture | [GitHub](https://github.com/rampstackco/claude-skills/blob/main/skills/design-system/SKILL.md) | [raw](https://raw.githubusercontent.com/rampstackco/claude-skills/main/skills/design-system/SKILL.md) | skills/design-systems/design-system/ | project-local | 72 | MIT; ~200 lines; component library + tokens + governance; stack-agnostic | ~200 lines — acceptable | Use when building a design system; skip for one-off UI work |

---

## Deduplication Notes

- Do NOT install both `frontend-design` and `design-taste-frontend` globally — they overlap significantly. Pick one per project based on the design challenge (frontend-design = aesthetic direction; taste-skill = rules enforcement).
- Do NOT install `interface-design` alongside `design-taste-frontend` for the same project — they cover the same general scope with different specializations.
- Do NOT install `creative-direction` and `brand-guidelines` simultaneously unless the project requires both aesthetic briefs AND Anthropic brand identity.
