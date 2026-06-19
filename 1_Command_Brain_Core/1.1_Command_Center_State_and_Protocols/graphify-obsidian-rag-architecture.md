# Graphify, Obsidian, And Light RAG Architecture

Purpose: define how VCOS HQ uses Graphify with Obsidian and GBrain so agents can resume work with less token burn and better project memory.

Source inputs: Graphify repo `https://github.com/safishamsi/graphify`, Graphify + Obsidian transcripts provided by Umair on 2026-06-10, and existing VCOS HQ architecture.

## Core Decision

VCOS uses a four-level context stack:

1. **Obsidian vault:** human navigation and backlink UI over VCOS HQ.
2. **Graphify:** project/corpus maps for code, docs, transcripts, and source relationships.
3. **QMD:** fast local context routing over approved markdown/docs/transcripts collections.
4. **GBrain:** text-first memory retrieval over approved curated Markdown.

These do different jobs. Do not blur them.

| Layer | Job | Best for | Not for |
| --- | --- | --- | --- |
| Obsidian | Browse, link, inspect, and think visually | Human navigation, backlinks, project maps | Acting, sending, mutating systems |
| Graphify | Build/query relationship maps | Large repos, docs, codebases, transcripts, project corpora | Source of truth, blind full-HQ dumping |
| QMD | Retrieve relevant files/snippets quickly | Local markdown/docs/transcripts search, agent context routing, MCP/CLI retrieval | Replacing Obsidian, owning decisions, blind whole-HQ indexing |
| GBrain | Search and recall curated text | Fast memory lookup, office-hours critique, summaries | Replacing source docs or graph relationships |

## Operating Principle

The goal is not to stuff more context into agents.

The goal is:

```text
Fast path -> graph query -> smallest source file -> output packet -> durable capture
```

Agents should load less context, not more. Graphify provides the map. QMD provides fast local file/snippet retrieval. Obsidian provides the visual vault. HQ Markdown provides truth. GBrain provides curated memory recall.

## Folder Architecture

```text
_VCOS_Headquarters/
├── Home.md
├── .graphifyignore
├── 1_Command_Brain_Core/
│   ├── 1.1_Command_Center_State_and_Protocols/
│   │   └── graphify-obsidian-rag-architecture.md
│   ├── 1.2_Headquarters_Memory/
│   └── 1.3_Knowledge_Graphs/
│       ├── README.md
│       ├── registry.md
│       ├── imports/
│       │   ├── agentosync/
│       │   ├── dealership-employee-01/
│       │   ├── skill-foundry/
│       │   └── vcos-hq-core/
│       └── summaries/
├── 2_Domain_Packs/
├── 3_Project_Workspaces/
├── 4_Reusable_Systems_and_Skills/
├── 5_Legacy_Reference_Archive/
└── 6_Arsenal/
```

## Graph Types

| Graph type | Scope | Where source lives | Where graph lives | When to build |
| --- | --- | --- | --- | --- |
| HQ core graph | Fast path, state, roadmap, decisions, key interfaces | HQ curated Markdown | `graphify-out/` at HQ root or exported copy | After `.graphifyignore` is reviewed |
| Project graph | One active workspace | `3_Project_Workspaces/<project>/` | Project `graphify-out/` | When a project will be resumed repeatedly |
| Domain graph | One reusable vertical | `2_Domain_Packs/<domain>/` | Domain `graphify-out/` | When domain patterns are reused across clients |
| Skill graph | Skill Foundry and Employee OS | `4_Reusable_Systems_and_Skills/` | Skill-system `graphify-out/` | When building repeatable Mini Intern capabilities |
| Reference graph | External repo/docs/tool | `6_Arsenal/repos/<tool>` or curated docs | Tool repo `graphify-out/` | When evaluating a tool deeply |

## Import Strategy

Use the transcript's safest pattern:

1. Build the graph in the source folder.
2. Generate Graphify wiki/Obsidian output into a quarantine folder.
3. Move or export that output under `1.3_Knowledge_Graphs/imports/<source-slug>/`.
4. Inspect in Obsidian.
5. Promote only the durable summary, decisions, blockers, and next actions into HQ memory.

Do not spray hundreds of generated concept files across active HQ folders.

Preferred import shape:

```text
1_Command_Brain_Core/1.3_Knowledge_Graphs/imports/<source-slug>/
├── index.md
├── GRAPH_REPORT.md
├── wiki/
├── obsidian/
└── source-links.md
```

## Default Commands

Check installation:

```bash
graphify --version
```

Build a project graph from inside the project folder:

```bash
graphify . --wiki --no-viz
```

Build with an Obsidian export only when the quarantine folder is ready:

```bash
graphify . --wiki --obsidian --obsidian-dir /Users/umairkhalid/_VCOS_Headquarters/1_Command_Brain_Core/1.3_Knowledge_Graphs/imports/<source-slug>/obsidian
```

Query before broad file reads:

```bash
graphify query "what connects this workflow to approval gates?" --budget 1500
```

For Codex, Graphify's assistant command is `$graphify`; for Claude Code, it is `/graphify`.

## Source Capsules

Every active project should eventually have a small graph source capsule in its `README.md` or `SKILLS_MANIFEST.md`:

```markdown
## Knowledge Graph

- Graph status:
- Source scope:
- Graph path:
- Obsidian import:
- Last built:
- Query examples:
- Do not index:
```

This is what lets Codex, Claude Code, and sub-agents resume without rediscovering the project.

## Agent Orchestration

Use strict ownership:

| Agent | Owns | May edit |
| --- | --- | --- |
| Sentinel | Routing, approvals, graph registry, final handoff | `state.md`, `registry.md`, project README summary sections |
| Graph Librarian | Graphify builds, imports, graph reports, source capsules | `1.3_Knowledge_Graphs/`, `.graphifyignore`, project graph sections |
| Builder | MVP/code/docs implementation | Active project implementation files |
| Reviewer / Skeptic | QA, adversarial review, stale graph checks | Review notes, test plans, findings |
| Documenter | SOPs, handoffs, summaries | README, handoff docs, promoted summaries |

Sub-agents should return distilled findings only: graph queried, source paths, decisions, risks, and next actions. They should not paste raw graph JSON or giant reports into the main session.

## Daily Resume Flow

When Umair returns to HQ:

1. Read fast path.
2. Identify project/domain owner.
3. Check `1.3_Knowledge_Graphs/registry.md` for a graph.
4. Query Graphify for the question before reading many files.
5. Open the project README or domain README only after graph query.
6. Use GBrain for cross-HQ memory recall.
7. Use QMD for local retrieval over approved collections when the graph points to a broad markdown/doc/transcript area.
8. Produce a compact output packet.
9. Update source capsule, decision, blocker, or next action only if durable.

## Best Practices From The Transcripts

- Combine Graphify and Obsidian instead of choosing one.
- Use Graphify as the relationship map, not as a document dump.
- Quarantine generated Obsidian files before bringing them into the main vault context.
- Keep generated graph imports in one removable subfolder per source.
- Link nodes back to source documents wherever possible.
- Query `graph.json` before asking agents to read directories.
- Use QMD after the graph query when the next step is "find the right file/snippet" rather than "understand relationships."
- Use Graphify reports for architecture orientation and suggested questions.
- Use Graphify wiki/Obsidian exports as navigation surfaces, then promote curated summaries.
- Avoid letting the Obsidian graph view become the goal; the goal is cleaner work resumption.

## Guardrails

- Do not run Graphify over all of HQ without `.graphifyignore`.
- Do not include `5_Legacy_Reference_Archive/` or `6_Arsenal/repos/` in the HQ core graph by default.
- Do not assume GBrain imports respect `.graphifyignore`; GBrain source scopes need their own explicit include/exclude design before importing project roots.
- Do not point QMD at all of HQ by default. Use approved collections such as fast-path command brain, active project workspace, meeting summaries, and curated graph summaries.
- Do not expose QMD HTTP/MCP beyond localhost without explicit approval.
- Do not commit or share graph outputs that include private/client material without review.
- Do not expose Graphify MCP over HTTP beyond localhost without an API key and explicit approval.
- Do not install always-on hooks into Claude/Codex project files until the graph query protocol is reviewed.
- Do not use Graphify as an approval bypass. External sends, CRM updates, publishing, spending, deleting, and production deployment still need human approval.

## First Build Sequence

1. Keep Graphify installed locally.
2. Use `.graphifyignore` to constrain the HQ root graph.
3. Create the first graph for `3_Project_Workspaces/3.1_AgentOSync_Revenue_Pipeline`.
4. Export wiki/Obsidian output into `1.3_Knowledge_Graphs/imports/agentosync/`.
5. Add an AgentOSync source capsule to its `README.md`.
6. Query the graph during the next AgentOSync daily brief.
7. Repeat for Dealership Employee 01 and Skill Foundry.
