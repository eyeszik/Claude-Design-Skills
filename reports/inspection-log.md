# Inspection Log — Claude Design-Skill Registry
> Audit date: 2026-05-11T00:53:02Z

All commands run during GATE_A read-only audit. No repo writes performed during inspection phase.

---

## Workspace Setup

```bash
mkdir -p /tmp/claude-design-skill-review/{reports,repos,direct-skills,raw,manifests}
```
Result: Created successfully.

---

## Source Commit Checks (git ls-remote)

| Repo | HEAD Commit | Status |
|------|-------------|--------|
| anthropics/claude-code | 831608a360511febd4b10c77d4d03b47afda2f5b | OK |
| anthropics/skills | f458cee31a7577a47ba0c9a101976fa599385174 | OK |
| affaan-m/everything-claude-code | 841beea45cb25ba51f29fa45b7e272938d19b80a | OK |
| kylezantos/design-motion-principles | 74d1f62d8095c51c024bcd828cccda793b5f26e4 | OK |
| Dammyjay93/interface-design | 8c407c1c42890010a9eb403a9f419b1eeadcfdad | OK |
| remotion-dev/skills | 277510e78245ac0fa275d7cb6520d52e0ac2e212 | OK |
| addyosmani/web-quality-skills | 7b59d48aaf1f793935002f4998dfccc656f40839 | OK |
| Leonxlnx/taste-skill | c8075169cd63d1430bbf492dd4ddd478ea9fa4da | OK |
| rampstackco/claude-skills | f1aa1d724387f64d3c59bb0c84b9b68e39f11d66 | OK |
| garrytan/gstack | 49cc4ff9c99e9b24f39aa7dcbfc456e840be29a8 | OK |
| Cranot/claude-code-guide | 712c838303b18f31d4859b24c2946fab9bed252c | OK |
| accesslint/claude-marketplace | 9870609e81f277187a2bb3a78a6afccc7aa8af84 | OK |
| figma/mcp-server-guide | fabc1ca81d839602ba7c1ca0f445a64246b3870e | OK |
| Leonxlnx/taste-skill | c8075169cd63d1430bbf492dd4ddd478ea9fa4da | OK |
| claudekit/frontend-design-pro-demo | 756b8d99618b2c4e8a90c89a99f678009468aae3 | OK |
| yusufkaraaslan/Skill_Seekers | 4cd5140b56b44a42cc3c5be0a0c1ba81e20a4af1 | OK |
| OpenCoworkAI/open-codesign | 38fb7ecde5a727785ca7eb2cddeec56aa2864d64 | OK |
| CloudAI-X/threejs-skills | b1c623076c661fc9b03dac19292e825a5d106823 | OK |
| hesreallyhim/awesome-claude-code | 614f102accbcd48206d63a21df64adc984026b40 | OK |
| travisvn/awesome-claude-skills | 1da55aa810f206d3fe2005e7e3989b15a275d942 | OK |
| coreyhaines31/marketingskills | — | 404 NOT FOUND |
| bencium/bencium-claude-code-design-skill | — | 404 NOT FOUND |
| nextlevelbuilder/ui-ux-pro-max-skill | — | 404 NOT FOUND |

---

## SKILL.md Fetch Results (curl -L --fail --max-time 20 --silent)

| File | Target Path | HTTP | Lines | Risk Scan |
|------|-------------|------|-------|-----------|
| anthropic-frontend-design-SKILL.md | plugins/frontend-design/skills/frontend-design/SKILL.md | 200 | 41 | Clean |
| anthropic-brand-guidelines-SKILL.md | skills/brand-guidelines/SKILL.md | 200 | 73 | Clean |
| anthropic-canvas-design-SKILL.md | skills/canvas-design/SKILL.md | 200 | 129 | Clean |
| anthropic-mcp-builder-SKILL.md | skills/mcp-builder/SKILL.md | 200 | 236 | Clean |
| anthropic-skill-development-SKILL.md | plugins/plugin-dev/skills/skill-development/SKILL.md | 200 | 637 | Clean |
| affaan-remotion-video-SKILL.md | skills/remotion-video-creation/SKILL.md | 200 | 43 | Clean |
| dammyjay93-interface-design-SKILL.md | .claude/skills/interface-design/SKILL.md | 200 | 391 | Clean |
| kylezantos-design-motion-SKILL.md | skills/design-motion-principles/SKILL.md | 200 | 203 | Clean |
| leonxlnx-taste-skill-SKILL.md | skills/taste-skill/SKILL.md | 200 | 226 | Clean |

---

## License Check Results

| Repo | License File Path | Status | License |
|------|------------------|--------|---------|
| anthropics/claude-code | /plugins/frontend-design/LICENSE.txt | Empty/404 | UNKNOWN |
| anthropics/skills | /LICENSE | Empty/404 | UNKNOWN |
| anthropics/skills | /LICENSE.txt | Empty/404 | UNKNOWN |
| affaan-m/everything-claude-code | /LICENSE | 200 | MIT ✓ |
| kylezantos/design-motion-principles | /LICENSE | 200 | MIT ✓ |
| Dammyjay93/interface-design | /LICENSE | 200 | MIT ✓ |
| addyosmani/web-quality-skills | /LICENSE | 200 | MIT ✓ |
| Leonxlnx/taste-skill | /LICENSE | 200 | MIT ✓ |
| rampstackco/claude-skills | /LICENSE | 200 | MIT ✓ |

---

## Risk Scan Results

```
Command: rg -n "postinstall|curl .*sh|wget .*sh|eval|chmod \+x|sudo|api_key|secret|stealth|bypass|anti-bot|credential|exfiltrate|rm -rf|browser profile|keychain|oauth|private key|ssh" /tmp/claude-design-skill-review/direct-skills/
```

**Result: NO RISK FILES FLAGGED**

(Note: mcp-builder matched `eval` pattern due to the word "evaluation" in context of test evaluations, not `eval()` code execution. False positive confirmed — not a risk.)

---

## URL HTTP Status Summary

| URL Category | Status |
|-------------|--------|
| skills.sh (all pages) | 403 Forbidden |
| firecrawl.dev/agent-onboarding/SKILL.md | 403 Forbidden |
| claude.com/plugins/* | Requires authenticated browser session |
| claude-plugins.dev/* | JS-heavy, cannot parse headlessly |
| claudemarketplaces.com | JS-heavy, cannot parse |
| mcp-market.vercel.app/* | Cannot parse headlessly |
| claudecodeskills.wayjet.io/* | Cannot access |
| gist liskl | Empty response |
| remotion-dev/skills README | "Internal package, no documentation" |

---

## Commands NOT Run (Hard Rules Compliance)

The following were NOT executed during this audit (per hard rules):

- `npm install` / `pnpm install` / `bun install`
- `npx` / `uvx`
- `curl | sh` / `wget | sh`
- `chmod +x`
- `*.sh` scripts
- Any MCP server execution
- Any browser automation
- Any plugin installer
- Any write to Claude global config
- Any commit, push, or PR creation during audit phase
