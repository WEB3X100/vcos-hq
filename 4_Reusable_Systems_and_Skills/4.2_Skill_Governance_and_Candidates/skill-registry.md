# Skill Registry

Purpose: single source of truth for reusable VCOS capabilities before they are installed into Mini Interns or packaged for clients.

## Lifecycle

| Stage | Meaning | Installable? |
| --- | --- | --- |
| Experiment | A raw workflow, prompt, tool test, or discovery. | No |
| Pattern | A repeated shape is emerging, but the input/output contract is still loose. | No |
| Skill Candidate | Has a trigger, owner department, input packet, output packet, and approval gate. | Only for internal/manual use |
| Validated Skill | Used successfully 3+ times or proven across multiple client-like scenarios. | Yes |
| Installed Intern Capability | Added to one or more department skill packs with least-privilege boundaries. | Yes |
| Marketplace Skill | Packaged with install/use instructions and client-safe assumptions. | Yes, after final human review |

## Registry

| Capability | Department | Stage | Source / Path | Tools | Approval Gate | Proof Lane | Next Step |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `higgsfield-media-generation` | Marketing | Skill Candidate | `candidates/higgsfield-media-generation/SKILL.md` | Higgsfield MCP, Nano Banana Pro, Seedance 2.0 | Human approval before paid generation, public use, client assets, claims, publishing, or external send | AgentOSync public acquisition; Amax internal proof | Run 3 controlled media generations and record results |
| `higgsfield-creative-agency-loop` | Marketing | Skill Candidate | `candidates/higgsfield-media-generation/references/creative-agency-loop.md` | Higgsfield CLI/MCP, tracker sheet/table, reference assets, advertising research | Human approval before credit spend, public use, client assets, claims, paid campaigns, publishing, or external send | AgentOSync creative testing; Amax internal proof; client demo ads | Build one local/Sheet creative tracker and run a 3-5 asset controlled batch |
| `higgsfield-generation-tracker` | Marketing | Skill Candidate | `candidates/higgsfield-media-generation/references/generation-tracker.md` | Google Sheets/Airtable/CSV/Markdown tracker, Higgsfield job metadata | Human approval before generating from tracker rows or connecting ad account performance data | AgentOSync creative database | Create tracker template and log all future Higgsfield tests |
| `hypermotion-style-recipe-extraction` | Marketing | Pattern | `candidates/higgsfield-media-generation/references/style-recipe-extraction.md` | Higgsfield winning outputs, prompt history, human feedback | Human approval before promoting to reusable house style or marketplace skill | AgentOSync ad formats | Extract one recipe from a confirmed winning output |
| `avatar-video-production-route` | Marketing | Skill Candidate | `candidates/higgsfield-media-generation/references/avatar-production-routing.md` | Higgsfield-friendly video workflows; optional HeyGen/ElevenLabs-style providers when approved | Human approval before likeness/voice use, credit spend, public use, external delivery, or publishing | AgentOSync educational content; internal training/course demos | Validate one Higgsfield-friendly avatar/video prompt packet and one dry-run batch pattern |
| `hyperframes-motion-graphics` | Marketing | Skill Candidate | `candidates/hyperframes-motion-graphics/SKILL.md` | Hyperframes, HTML/CSS/GSAP, FFmpeg, Chrome, transcripts, brand tokens | Human approval before public publishing, client-facing delivery, claims, paid campaigns, or external send | AgentOSync LinkedIn/video demos; Amax dashboard walkthroughs; barber AVAPI explainer | Test on one internal 15-30s AgentOSync/Amax clip and record render QA |
| `seedance-loop-prompt` | Marketing | Pattern | `../seedance-loop-prompt/SKILL.md` | Seedance 2.0, reference image/video workflow | Human approval before generation spending and website publication | AgentOSync demo sites; client-style luxury website demos | Fold into Marketing pack as website hero-loop sub-capability |
| `agentosync-media-review` | Reviewer QA | Skill Candidate | `candidates/agentosync-media-review/SKILL.md` | Claude/Codex review, quality rubrics | None for internal review; human approval still required for external action | AgentOSync content QA | Pair with Marketing media generation before every public draft |
| `superpowers-development-discipline` | Infrastructure | Evaluation Candidate | `skill-leverage-stack.md` | Claude Code Superpowers plugin | Human approval before install, remote actions, deploys, destructive changes, or client-facing use | VCOS Employee template refactors; medium/complex builds | Verify install status, test on one non-client build, then decide global vs project-level adoption |
| `session-context-discipline` | Infrastructure | Active Protocol | `../../1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/session-context-discipline.md` | Claude/Codex commands, handoff files, sidecar agents when allowed | Approval before external actions only; internal session hygiene is always allowed | VCOS HQ and Employee OS operations | Use in long sessions; consider packaging `/session-handoff` after 3 successful handoffs |
| `travel-crm-intake` | Ops | Skill Candidate | `vcos-skill-pack-manifest.md` | CRM, forms, ClickUp, Drive | Human approval before CRM/customer data mutation | Amax / travel proof lane | Convert into a packetized Ops capability after Amax forms work |
| `travel-lead-followup` | Sales Ops | Skill Candidate | `vcos-skill-pack-manifest.md` | CRM, WhatsApp/email draft workflows | Human approval before external communication | Amax / travel proof lane | Define lead handoff packet and approval queue |
| `travel-proposal-deck` | Sales Ops | Skill Candidate | `vcos-skill-pack-manifest.md` | Docs/slides/design tools | Human approval before final client use | Amax / travel proof lane | Create proposal output packet and QA checklist |
| `one-person-ai-agency-sales-os` | Sales Ops | Skill Candidate | `candidates/one-person-ai-agency-sales-os/SKILL.md` | Transcript/source notes, ClickUp leads, meeting notes, proof assets, draft outreach/call packets | Human approval before outbound messages, calendar links, proposal terms, pricing, payment links, CRM/customer-data mutation, client-facing claims, publishing, or external sends | Dealership OS one-day sales packet first; Amax/travel and SMB kits second | Run one manual Dealership OS offer/call/delivery packet and record whether it improves the close path |
| `session-handoff` | Infrastructure | Skill Candidate | `candidates/session-handoff/SKILL.md` | Claude/Codex session chat, plan/todo/state files | None for internal handoff; approval before external action | VCOS HQ long sessions; Agent Team handoffs | Use in 2 sessions and confirm output format works; then evaluate for global Claude Code skill install |
| `claude-design-brand-system` | Marketing | Validated Skill | `skill-leverage-stack.md` | Claude Design, B.R.A.N.D. framework, Figma, Vercel | Human approval before client brand systems, final pitch decks, or published guidelines | AgentOSync brand identity; Amax partner/employee collateral; client proposal visuals | Brand system reference in all marketing materials; integrate B.R.A.N.D. framework into design workflow |
| `website-hero-video-pipeline` | Marketing | Skill Candidate | `skill-leverage-stack.md` | Claude Design, Nano Banana 2, Kling 2.0, Vercel, single-change-per-prompt discipline | Human approval before client delivery, paid ads, or public publishing | AgentOSync demo sites; internal course/training videos | Validate one full website-to-hero-video build; test Opus 4.7 → Sonnet 4.6 model-by-stage approach |
| `gbrain-project-memory-layer` | Infrastructure | Evaluation Candidate | `gbrain-activation.md`; `../../6_Arsenal/repos/gbrain/README.md`; `../../6_Arsenal/repos/gbrain/INSTALL_FOR_AGENTS.md` | GBrain CLI, Bun, local markdown brain repo, optional MCP | Human approval before API key setup, client/private data import, external connectors, recurring jobs, public MCP servers, or project-wide rollout | VCOS project memory; AgentOSync handoffs; future company-brain evaluation | Run one controlled local markdown import and retrieval test after search mode and credential strategy are approved |
| `gbrain-office-hours` | Infrastructure / Strategy | Skill Candidate | `candidates/gbrain-office-hours/SKILL.md` | GBrain CLI, HQ fast-path files, project workspace files, optional GStack office-hours/review patterns | Human approval before external sends, publishing, CRM mutation, spending, deployment, or final client-facing strategy/pricing | VCOS project development; AgentOSync conversion; Amax/dealership solution critique; Skill Foundry reviews | Run on one real AgentOSync offer/build plan and record whether it improved the output |
| `agentosync-presentation-quality` | Marketing / Sales Ops / Reviewer QA | Skill Candidate | `candidates/agentosync-presentation-quality/SKILL.md` | Presentations skill, AgentOSync brand asset, coded deck design system, rendered slide QA, language scanner | Human approval before final client use, external send, publishing, public claims, pricing, or proposal terms | Dealership OS client walkthroughs; AgentOSync sales assets; reusable branded deck system | Use on 3 client-facing deck/PDF builds and record failures prevented |
| `claude-visible-weekly-review` | Infrastructure / Sentinel | Skill Candidate | `candidates/claude-visible-weekly-review/SKILL.md`; ClickUp task `86e1w6343` | ClickUp, Claude Project/Claude Code, VCOS fast-path files, Sunday Office Hours brief | Human approval before notifying team, external sends, ClickUp mutation beyond the approved task, public/client use, or packaging | VCOS weekly review; Skill Foundry; Claude agent review | Have Claude/team review task `86e1w6343`, log feedback, and run 2 more weekly cycles before promotion |

## Capture Rule

When a workflow is repeated or likely reusable, add it here before installing it into a department pack. Do not skip straight from experiment to Mini Intern capability.

Minimum fields:

- capability name
- owning department
- lifecycle stage
- source path
- tools required
- approval gate
- proof lane
- next validation step
