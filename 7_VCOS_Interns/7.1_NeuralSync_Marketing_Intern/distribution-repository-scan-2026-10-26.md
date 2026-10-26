# NeuralSync Distribution Repository Scan — 2026-10-26

Scope: repositories accessible to GitHub account `WEB3X100`, reviewed for NeuralSync / AgentOSync marketing, content, proof, GTM, campaign, landing-page, and publishing assets.

## Canonical and directly transferable

| Repository | Role | Relevant assets | OpenMaus access |
| --- | --- | --- | --- |
| `WEB3X100/vcos-hq` | Canonical policy, intern identity, approval gates, and reusable Marketing skills | `7_VCOS_Interns/7.1_NeuralSync_Marketing_Intern/`; Marketing department pack; Higgsfield, media-review, Seedance-loop, and Hyperframes skills | Required working repository; read/write through branch + PR |
| `WEB3X100/VCOS-Employee` | Production system, content intelligence, writer/producer patterns, swipe frameworks, review portal, and media skills | `3_Production_Work/3.1_Marketing_Intern_Content_Intel/`; `2_Reusable_Deployment_Assets/2.3_Content_and_Copy_Swipe_File/`; `.claude/skills/`; `VCOS_Neural_Sync/content-intel/` | Read-only initially; selective writes only after ownership is defined |
| `WEB3X100/VCOS-Project-Workspaces` | AgentOSync GTM strategy and proof context | `3.1_AgentOSync_Revenue_Pipeline/00_strategy/proof-library-ledger.md`; `01_website/landing-page-brief.md`; `03_gtm_campaigns/social-media-campaign-plan.md`; lead funnel, media-review workflow, and outreach game plan | Read-only reference |
| `WEB3X100/AgentoSync_Ammar_Platforms` | Existing channel-ready content packages | Seven-day LinkedIn/X packages, repost copies, schedule, weekly mix, and publishing checklist under `content/` | Read-only initially; candidate active distribution workspace after human confirmation |

## Product-proof and conversion surfaces

| Repository | Role | Relevant assets | OpenMaus access |
| --- | --- | --- | --- |
| `WEB3X100/AgentoSync` | Product and public landing-page proof | Landing components, testimonials, ROI calculator, CTA, problem/solution sections | Read-only; never publish or change claims without approval |
| `WEB3X100/NeuralSync_Dealership_SaaS` | Dealership wedge marketing surface | `src/components/marketing/`, ROI calculator, social proof, video testimonials, onboarding video metadata | Read-only; claims and testimonials are approval-gated |
| `WEB3X100/neuralsync-qbo-landing` | NeuralSync/QBO landing surface | Landing repository; no distribution-named paths found in the tree scan | Read-only only when a QBO campaign is active |

## Adjacent or lane-specific distribution repositories

| Repository | Why adjacent | Decision |
| --- | --- | --- |
| `WEB3X100/gstack-Travel` | Travel-domain execution limb; not the NeuralSync public-acquisition source of truth | Do not grant by default; add only for approved Amax/travel campaigns |
| `WEB3X100/LeanForce-landing-page` | Public landing page for another product/brand | Exclude from this intern unless explicitly assigned |
| `WEB3X100/hadi-clinic-site` | Clinic site that may supply vertical proof | Exclude by default; client/brand access requires approval |
| `WEB3X100/VALAVON-Website` | Separate client/product website | Exclude by default |
| `WEB3X100/amax-vacations` and `WEB3X100/amax-vacations-vietnam-2027` | Amax/travel marketing surfaces | Exclude by default; add only for the Amax lane with client-safe constraints |

## Do not use as the canonical marketing workspace

| Repository | Finding |
| --- | --- |
| `WEB3X100/content-os-gsd-planning` | Repository currently contains only a small `README.md`; it does not hold the operative NeuralSync content system. |

## Recommended access boundary

Use `WEB3X100/vcos-hq` as the OpenMaus working repository. Give the bot read-only visibility to `VCOS-Employee`, `VCOS-Project-Workspaces`, `AgentoSync_Ammar_Platforms`, `AgentoSync`, and `NeuralSync_Dealership_SaaS`. Add write access one repository at a time after a dry-run review. Keep all client-specific, finance, personal, and unrelated product repositories out of the bot's default tool scope.

## GitHub implementation note

OpenMaus connected-app grants are tool-scoped, not repository-scoped. For strong isolation, authorize GitHub through a separate installation/account whose repository selection contains only the approved repositories. A broad personal GitHub connection plus prompt-only restrictions is a convenience boundary, not a hard security boundary.

