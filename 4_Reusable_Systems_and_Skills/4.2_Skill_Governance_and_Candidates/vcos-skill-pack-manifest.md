# VCOS Skill Pack Manifest

Purpose: govern which SOPs become skills and how skill adoption is managed.

## Skill Foundry Interfaces

| File | Purpose |
| --- | --- |
| `skill-registry.md` | Single source of truth for reusable capabilities, lifecycle stage, owner department, tools, gates, proof lane, and next action. |
| `weekly-skill-harvest.md` | Weekly ritual for turning repeated learning into capability candidates instead of scattered notes. |
| `department-capability-map.md` | Map of Mini Intern departments, boundaries, tools, handoff packet rules, and approval gates. |
| `promotion-rules.md` | Rules for moving experiments into candidates, validated skills, installed capabilities, and marketplace skills. |
| `../4.3_Department_Skill_Packs/` | Department-specific installed/candidate capability packs for Marketing, Sales Ops, Ops, Finance, Reviewer QA, Infrastructure, and Marketplace. |
| `../4.4_Validated_Marketplace_Skills/` | Client-safe validated skills that are close to packageable. |

## Installed Local Skills

| Skill | Path | Purpose |
| --- | --- | --- |
| `vcos-command-router` | `.agents/4_Reusable_Systems_and_Skills/4.2_Skill_Governance_and_Candidates/vcos-command-router/SKILL.md` | Routes work between VCOS HQ, command rooms, Drive, skill policy, and domain packs. |

## Candidate Skills

| Candidate | Status | Purpose |
| --- | --- | --- |
| `clickup-command-review` | SOP candidate | Review Production, Delivery, and Q3 command rooms. |
| `drive-clickup-sync` | SOP candidate | Keep Drive as file home and ClickUp as execution home. |
| `client-delivery-triage` | SOP candidate | Keep delivery focused on outcomes, blockers, demos, proposals, and close paths. |
| `production-control-room` | SOP candidate | Keep production tasks consolidated into reusable systems. |
| `q3-command-center` | SOP candidate | Protect Umair's brain from overload. |
| `higgsfield-media-generation` | SOP candidate | Generate Open Claw/AgentOSync images, clips, avatar/course videos, and tracked creative-testing batches through Higgsfield-friendly workflows. |
| `higgsfield-creative-agency-loop` | Marketing candidate | Use Higgsfield CLI/MCP as a tracked creative agency: plan slates, generate approved rows, log job IDs/results, review winners, and extract style recipes. |
| `higgsfield-generation-tracker` | Marketing candidate | Maintain the creative database for prompts, references, job IDs, statuses, QA scores, output URLs, human feedback, and lessons learned. |
| `hypermotion-style-recipe-extraction` | Marketing pattern | Convert winning Higgsfield/Marketing Studio outputs into repeatable Hypermotion or ad-style recipes before promoting them to sub-skills. |
| `avatar-video-production-route` | Marketing candidate | Orchestrate avatar, talking-head, course, and founder-style video production through Higgsfield-friendly or provider-specific routes with consent and approval gates. |
| `hyperframes-motion-graphics` | Marketing candidate | Assemble generated assets, transcripts, UI recordings, captions, social cards, product demos, and final MP4 renders through Hyperframes. |
| `seedance-loop-prompt` | Pattern / Marketing candidate | Create seamless Seedance 2 looping website background video prompts from a reference image and hero concept. |
| `luxury-ai-video-website-builder` | Marketing candidate to define | Orchestrate ICP, reference image, Seedance hero loop, front-end design, GitHub/Vercel demo deployment, and QA gates. |
| `agentosync-media-review` | SOP candidate | Critique generated AgentOSync/Open Claw/Amax media for brand fit, approval safety, platform fit, revision prompts, and draft-only posting packets. |
| `superpowers-development-discipline` | Evaluation candidate | Claude Code development discipline plugin for clarify, brainstorm, plan, TDD, verification, review, worktrees, and branch finishing on medium/complex builds. |
| `session-context-discipline` | Active protocol | Keep Claude/Codex sessions cheap and sharp through rewind, clear, handoff, sidecar delegation, Markdown conversion, and file-backed state. |
| `travel-crm-intake` | Domain candidate | Travel-specific lead and CRM intake. |
| `travel-lead-followup` | Domain candidate | Travel-specific follow-up flow. |
| `travel-proposal-deck` | Domain candidate | Travel proposal/deck generation. |

See `4_Reusable_Systems_and_Skills/4.2_Skill_Governance_and_Candidates/vcos-task-skill-map.md` for the broader task-to-skill-to-automation registry.

## Promotion Rule

A SOP becomes a permanent skill only when:

- It has been used successfully at least 3 times.
- It produces a repeatable output.
- It reduces time, cost, mistakes, or context load.
- It has a clear owner or recurring use case.

## Good Output Examples

When a skill candidate produces a strong result, save a short example under `4_Reusable_Systems_and_Skills/4.2_Skill_Governance_and_Candidates/candidates/<skill-name>/examples/`.
