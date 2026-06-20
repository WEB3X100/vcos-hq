# Obsidian Second Brain

Purpose: use Obsidian as the human visual layer for VCOS HQ without creating duplicate memory.

Canonical architecture: `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/ai-os-second-brain-architecture.md`.

Obsidian is part of the **Second Brain** layer. It helps humans browse, link, and review HQ memory. It is not the AI OS action layer and it is not a duplicate source of truth.

## Setup

Status: activated on 2026-06-10 with local vault config in `.obsidian/`.

Open Obsidian and choose:

```text
Open folder as vault -> /Users/umairkhalid/_VCOS_Headquarters
```

Use `Home.md` as the vault home note.

Current vault config:

- Opens `Home.md` in preview mode.
- Enables file explorer, search, backlinks, graph, tags, command palette, and file recovery.
- Ignores noisy folders: `5_Legacy_Reference_Archive/`, `6_Arsenal/repos/`, `node_modules/`, and `.git/`.
- Uses `1_Command_Brain_Core/1.3_Knowledge_Graphs/imports/` as the quarantine lane for Graphify-generated Obsidian/wiki imports.

## Folder Roles

| Folder | Role |
| --- | --- |
| `1_Command_Brain_Core/1.2_Headquarters_Memory/` | Compact active memory and durable decisions |
| `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/` | Operating state, requirements, roadmaps, approvals, cadence, automation registries |
| `2_Domain_Packs/` | Deep-module interfaces for specialized limbs |
| `4_Reusable_Systems_and_Skills/4.2_Skill_Governance_and_Candidates/` | SOP governance, skill candidates, task-skill map |
| `3_Project_Workspaces/3.2_Project_Briefs/` | Project-specific context and handoffs |
| `5_Legacy_Reference_Archive/5.1_Legacy_Reference_Singular/`, `5_Legacy_Reference_Archive/5.2_Legacy_References_Plural/` | Legacy material awaiting migration; do not load by default |

## Capture Flow

Raw capture should not go straight into active memory.

Use this flow:

1. Capture rough notes, transcripts, and research into a project/domain artifact or temporary inbox.
2. Distill into wiki-style notes only when the material will be queried again.
3. Promote only durable decisions, blockers, and routing changes into active memory.
4. Link source docs instead of copying long raw material into `1_Command_Brain_Core/1.2_Headquarters_Memory/`.

## Graphify Import Flow

Use Graphify when a project, repo, transcript set, or doc corpus is too large to reread every session.

1. Build/query the graph in the owning source folder.
2. Export wiki/Obsidian output into `1_Command_Brain_Core/1.3_Knowledge_Graphs/imports/<source-slug>/`.
3. Inspect the generated import in Obsidian.
4. Promote only durable summaries, decisions, blockers, next actions, and source links into active HQ memory.

Do not redistribute hundreds of generated node files across HQ until the import has proven useful.

## Wiki Pattern

Use a Markdown wiki only for knowledge that compounds:

- Client/project facts reused across weeks.
- Repeated meeting themes.
- Research areas that need backlinks.
- Dealership wedge insights.
- Sales objections and proof points.
- Tool/API notes repeatedly needed by agents.

Preferred wiki note shape:

```markdown
# Topic

## Summary

## Source Links

## Relationships

- [[Related Topic]]

## Decisions / Implications

## Open Questions
```

## Guardrails

- Do not duplicate `1_Command_Brain_Core/1.2_Headquarters_Memory/active-context.md` into another note.
- Do not paste huge transcripts into active memory.
- Do not let Obsidian become the execution source of truth; ClickUp owns execution.
- Do not let Obsidian become the file source of truth; Drive owns client files.
- Do not use generated Graphify files as source of truth; they are maps back to source material.
- Do not create a heavier vector/RAG layer until Markdown retrieval, Graphify query, and GBrain text search fail in a specific workflow.
