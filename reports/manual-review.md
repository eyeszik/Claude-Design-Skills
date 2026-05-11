# Manual Review List — Claude Design-Skill Registry
> Audited: 2026-05-11T00:53:02Z

These candidates require human approval, credentials, or external account access before any installation.
Do NOT install any of these automatically.

---

## Requires Claude Account (install via claude.com UI only)

| Candidate | Risk | Exact Approval Needed | Safe Next Step |
|-----------|------|-----------------------|----------------|
| https://claude.com/plugins/skill-creator | Plugin install changes global Claude context for all sessions; unknown token footprint | Explicitly approve Claude account plugin install | Log into claude.com → Plugins → search "skill-creator" → review permissions → install manually |
| https://claude.com/plugins/firecrawl | Plugin install + potential web scraping credentials; unknown token footprint | Explicitly approve Claude account plugin install + Firecrawl key storage | Log into claude.com → Plugins → search "firecrawl" → review permissions → install manually if desired |

---

## Requires Firecrawl Credentials

| Candidate | Risk | Exact Approval Needed | Safe Next Step |
|-----------|------|-----------------------|----------------|
| https://www.firecrawl.dev/agent-onboarding/SKILL.md | 403 Forbidden — content inaccessible without auth | Provide Firecrawl account credentials or API key | Authenticate with Firecrawl → re-fetch URL → inspect content → make classification decision |

---

## Requires MCP Server Installation + Browser Automation

| Candidate | Risk | Exact Approval Needed | Safe Next Step |
|-----------|------|-----------------------|----------------|
| https://github.com/accesslint/claude-marketplace | Installs `@accesslint/mcp` MCP server; auto-launches Chrome minimized for live DOM audit; requires browser automation | Approve: (1) `claude mcp add accesslint npx @accesslint/mcp`, (2) Chrome headless launch, (3) optional `chrome-devtools-mcp` for auth sessions | Review source code at https://github.com/AccessLint/accesslint/tree/main/mcp; verify no credential exfiltration; then approve MCP install |

---

## Requires Figma Account + API Token + MCP Server

| Candidate | Risk | Exact Approval Needed | Safe Next Step |
|-----------|------|-----------------------|----------------|
| https://github.com/figma/mcp-server-guide | Requires Figma account, Figma API token, MCP server setup; not a skill — it is a setup guide | Approve: (1) Figma account creation/use, (2) Figma Personal Access Token generation, (3) MCP server install | Read guide at github.com/figma/mcp-server-guide; follow setup steps manually; verify token scope before use |
| https://mcpservers.org/claude-skills/figma/create-design-system-rules | MCP marketplace page; JS-heavy, cannot parse headlessly; may require Figma MCP | Inspect content manually in browser | Navigate to URL in browser → inspect the skill → determine if safe and relevant |

---

## Requires Token/Line-Count Review Before Install (LINK_ONLY until resolved)

| Candidate | Risk | Exact Approval Needed | Safe Next Step |
|-----------|------|-----------------------|----------------|
| skill-development (637 lines) | 637 lines always loaded = significant context overhead; Anthropic license unknown | Confirm acceptable token budget; verify license | Review full file at raw URL; decide if trimmed version or progressive-disclosure wrapper is needed |
| mcp-builder (236 lines) | Not a design skill; Anthropic license unknown | Confirm relevance; verify license | Review full file; use only when actively building MCP integrations |
