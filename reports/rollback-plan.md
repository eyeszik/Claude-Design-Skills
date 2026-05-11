# Rollback Plan — Claude Design-Skill Registry
> Audited: 2026-05-11T00:53:02Z

---

## What Was Created in This Registry Build

### Repository Files (eyeszik/Claude-Design-Skills, branch: claude/design-skill-audit-FW4TF)

```
/sources/design-skill-urls.txt
/registries/design-skills.json
/registries/design-skills.md
/registries/design-skills.csv
/registries/raw-links.md
/reports/install-plan.md
/reports/manual-review.md
/reports/rejected-risk.md
/reports/reference-only.md
/reports/dedupe-map.md
/reports/token-minimization-plan.md
/reports/rollback-plan.md
/reports/inspection-log.md
/scripts/verify-skills.py
/skills/frontend-design/frontend-design/SKILL.md (LINK_ONLY stub)
/skills/frontend-design/frontend-design/source-metadata.json
/skills/frontend-design/canvas-design/SKILL.md (LINK_ONLY stub)
/skills/frontend-design/canvas-design/source-metadata.json
/skills/frontend-design/design-taste-frontend/SKILL.md (COPIED, MIT)
/skills/frontend-design/design-taste-frontend/source-metadata.json
/skills/frontend-design/interface-design/SKILL.md (COPIED, MIT)
/skills/frontend-design/interface-design/source-metadata.json
/skills/brand-guidelines/brand-guidelines/SKILL.md (LINK_ONLY stub)
/skills/brand-guidelines/brand-guidelines/source-metadata.json
/skills/accessibility/accessibility/SKILL.md (COPIED, MIT)
/skills/accessibility/accessibility/source-metadata.json
/skills/motion/design-motion-principles/SKILL.md (COPIED, MIT)
/skills/motion/design-motion-principles/source-metadata.json
/skills/motion/remotion-video-creation/SKILL.md (COPIED, MIT)
/skills/motion/remotion-video-creation/source-metadata.json
/skills/design-systems/design-system/SKILL.md (COPIED, MIT)
/skills/design-systems/design-system/source-metadata.json
/skills/marketing-design/creative-direction/SKILL.md (COPIED, MIT)
/skills/marketing-design/creative-direction/source-metadata.json
/skills/skill-development/skill-development/SKILL.md (LINK_ONLY stub)
/skills/skill-development/skill-development/source-metadata.json
```

### Temporary Inspection Files (auto-cleaned on reboot)

```
/tmp/claude-design-skill-review/
```

---

## Removal Commands (Full Rollback)

```bash
# Remove all registry files
rm -rf /home/user/Claude-Design-Skills/sources/
rm -rf /home/user/Claude-Design-Skills/registries/
rm -rf /home/user/Claude-Design-Skills/skills/
rm -rf /home/user/Claude-Design-Skills/reports/
rm -rf /home/user/Claude-Design-Skills/scripts/

# Restore README.md to original state
echo "# Claude-Design-Skills" > /home/user/Claude-Design-Skills/README.md

# Verify removal
find /home/user/Claude-Design-Skills -type f | grep -v ".git"
```

---

## Git Rollback

```bash
# Find the commit hash before registry build
git -C /home/user/Claude-Design-Skills log --oneline

# Option 1: Revert (safe — creates a new commit)
git -C /home/user/Claude-Design-Skills revert HEAD

# Option 2: Reset to initial commit (destructive — only use on feature branch)
git -C /home/user/Claude-Design-Skills reset --hard <initial-commit-hash>

# Push the rollback
git -C /home/user/Claude-Design-Skills push -u origin claude/design-skill-audit-FW4TF
```

---

## Registry Restore Plan

No registry existed before this build. If rollback is needed:
1. Run removal commands above.
2. The repo returns to the initial state: only `README.md` with `# Claude-Design-Skills`.
3. No external state was modified (no Claude account changes, no global config changes, no MCP installs).

---

## Plugin Rollback Notes

**No Claude account plugins were installed.** This registry build was read-only on the account level.

If you later manually install plugins via claude.com:
- To uninstall: Log into claude.com → Settings → Plugins → find plugin → Remove
- Firecrawl plugin: Revoke Firecrawl API key from Firecrawl dashboard after uninstalling
- Figma MCP: Revoke Figma Personal Access Token from Figma account settings

---

## Per-Skill Rollback Commands

| Skill | Rollback Command |
|-------|-----------------|
| frontend-design (stub) | `rm -rf skills/frontend-design/frontend-design/` |
| canvas-design (stub) | `rm -rf skills/frontend-design/canvas-design/` |
| design-taste-frontend | `rm -rf skills/frontend-design/design-taste-frontend/` |
| interface-design | `rm -rf skills/frontend-design/interface-design/` |
| brand-guidelines (stub) | `rm -rf skills/brand-guidelines/brand-guidelines/` |
| accessibility | `rm -rf skills/accessibility/accessibility/` |
| design-motion-principles | `rm -rf skills/motion/design-motion-principles/` |
| remotion-video-creation | `rm -rf skills/motion/remotion-video-creation/` |
| design-system | `rm -rf skills/design-systems/design-system/` |
| creative-direction | `rm -rf skills/marketing-design/creative-direction/` |
| skill-development (stub) | `rm -rf skills/skill-development/skill-development/` |
