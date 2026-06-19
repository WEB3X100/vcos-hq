# Research Agent Skill Pack

Purpose: install a Morning Research Agent into a VCOS employee or department workflow.

Use this pack when the system needs to monitor trusted sources, filter signal from noise, synthesize what changed, and produce a short daily or weekly intelligence brief.

## Files

- `capabilities.md` - what the Research Agent can do and what is still candidate/future work
- `orchestration.md` - morning brief, weekly calibration, handoffs, and runtime paths
- `least-privilege.md` - access boundaries, approval gates, and data rules
- `templates/research-context-template.md` - starting context for `CLAUDE.md` or a dedicated research context file
- `templates/morning-research-agent-prompt.md` - reusable prompt for the daily brief
- `templates/weekly-feedback-loop-prompt.md` - prompt for improving the agent from human annotations
- `templates/n8n-workflow-spec.md` - node-by-node n8n implementation spec

## First Setup Pass

1. Create or copy the research context template into the target vault.
2. Create a `BRIEFINGS/` folder.
3. Run one manual brief using the morning prompt.
4. Review the output for signal, sources, and noise.
5. Only after the manual run is useful, wire the n8n scheduled workflow.
6. Keep production activation behind the approval gates in `least-privilege.md`.
