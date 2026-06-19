# Research Agent Mini Intern Capabilities

Purpose: turn noisy daily information streams into short, sourced, action-ready intelligence briefs for VCOS work.

## Candidate Capabilities

| Capability | Status | Source | Job |
| --- | --- | --- | --- |
| Morning intelligence brief | Candidate | `templates/morning-research-agent-prompt.md` | Search trusted sources, filter signal, synthesize a 5-minute brief, and save it to the briefing folder |
| Research context calibration | Candidate | `templates/research-context-template.md` | Keep focus areas, competitive landscape, trusted sources, and explicit noise filters current |
| n8n scheduled research workflow | Candidate | `orchestration.md` | Run the brief on a weekday or daily schedule and write the output to the vault |
| Feedback loop updater | Pattern | `templates/weekly-feedback-loop-prompt.md` | Use annotations from prior briefs to improve source priority, search queries, and exclusion rules |
| Competitive watch alerts | Future extension | `orchestration.md` | Monitor high-priority competitors more frequently and notify only when something material changes |
| Topic deep dive queue | Future extension | `orchestration.md` | Convert a brief item or queued topic into a longer research note |

## Default Research Workflow

1. Read the research context from `CLAUDE.md` or a dedicated research context file.
2. Search priority topics and competitive landscape sources.
3. Filter out stale, generic, repeated, or explicitly unwanted items.
4. Synthesize only the developments that affect current work, decisions, opportunities, or risks.
5. Save a dated brief to `BRIEFINGS/YYYY-MM-DD-morning-brief.md`.
6. Preserve sources and links for anything included.
7. Leave a `My Notes on This Brief` section so the human can calibrate future runs.

## Output Standard

Every brief should answer:

- What is the one thing I need to know today?
- What changed in the last 24 hours?
- Why does it matter for my work specifically?
- Did anyone in my competitive landscape move?
- Is there a concrete action worth considering?
- Which 2-3 links are worth reading in full?

## Approval Gates

Human approval is required before production schedule activation, credential setup, external notifications, sharing briefs outside VCOS, writing into client-owned vaults, or using paid APIs at a meaningful recurring cost.

## Runtime Note

Claude Desktop MCP access and Anthropic API calls are separate runtimes. A Claude Desktop MCP setup can run the research manually or interactively. An n8n workflow calling the Anthropic API needs its own web-search path, such as Brave Search API calls inside n8n, an MCP-capable worker, or another approved search connector.
