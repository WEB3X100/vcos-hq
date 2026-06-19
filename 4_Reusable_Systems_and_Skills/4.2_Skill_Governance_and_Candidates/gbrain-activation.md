# GBrain Activation Note

Purpose: evaluate GBrain as the VCOS/project memory layer without turning every project into a separate brain.

## Status

- Source repo cloned locally: `6_Arsenal/repos/gbrain`
- Upstream: `https://github.com/garrytan/gbrain`
- Local version checked: `gbrain 0.42.1.0`
- Local checkout revision: `eefe8b57`
- CLI status: installed on PATH via Bun link
- Lifecycle: Infrastructure evaluation candidate, locally initialized for HQ text-first retrieval
- Local brain: `/Users/umairkhalid/.gbrain/brain.pglite`
- Search mode: `conservative`
- Current import scope: `/Users/umairkhalid/_VCOS_Headquarters`
- Import status: 2026-06-10 text-first import completed with `--no-embed`; 1,500 pages, 7,657 chunks, 0 embedded chunks

## Fit For VCOS

GBrain is a candidate for:

- project memory search and synthesis
- brain-first lookup before external API calls
- project and meeting context retrieval
- skillpack/reference architecture learning
- future company-brain or multi-user memory experiments

GBrain is not yet the system of record for VCOS HQ. HQ fast-path files, ClickUp, Drive, and project manifests remain authoritative until a human-approved migration exists.

## Activation Rules

- Use pointer-first references from project `SKILLS_MANIFEST.md` files.
- Do not scaffold GBrain's 43 bundled skills into every project by default.
- Do not import client, CRM, email, calendar, Drive, or ClickUp data without explicit human approval.
- Do not start recurring jobs, autopilot, dream cycles, webhooks, public MCP servers, or remote connectors without explicit human approval.
- Before `gbrain init` becomes operational, the human must choose search mode because GBrain's installer documents meaningful cost differences.
- API keys must be supplied through the approved credential path, not pasted into durable project files.

## Project Usage Pattern

Add GBrain to a project only when the project needs persistent context retrieval or cross-session memory beyond the normal README plus handoff pattern.

Recommended manifest entry:

| Skill ID | Department | Purpose | Source in HQ | Proof Lane | Blocker? |
| --- | --- | --- | --- | --- | --- |
| `gbrain-project-memory-layer` | Infrastructure | Search and synthesize project memory, notes, decisions, and handoffs before external lookup | `4_Reusable_Systems_and_Skills/4.2_Skill_Governance_and_Candidates/gbrain-activation.md` | Internal project-memory evaluation | No |

## Next Activation Gate

Initial HQ activation is complete in deferred-embedding mode. To complete semantic activation:

1. Confirm API key strategy for embeddings.
2. Configure an embedding provider with `gbrain config set embedding_model <id>`.
3. Run embeddings for imported HQ pages.
4. Decide whether future sync should exclude noisy vendor docs under `6_Arsenal/repos/`.
5. Add one controlled project-memory retrieval test using semantic search before any broader rollout.
