# Marketing Orchestration

Purpose: show how Marketing combines capabilities into revenue workflows.

## Website + Campaign Workflow

Use when Marketing needs to build a demo website and campaign around an ICP.

```mermaid
flowchart TD
  A["ICP + offer + desired feeling"] --> B["Creative brief"]
  B --> C["Nano Banana reference image"]
  C --> D["Seedance loop prompt"]
  D --> E["Seedance hero video"]
  E --> F["Website build with front-end design skill"]
  F --> G["Reviewer QA"]
  G --> H["Human approval"]
  H --> I["GitHub/Vercel deploy"]
  H --> J["LinkedIn campaign packet"]
  J --> K["Sales Ops handoff"]
```

## Handoff To Sales Ops

Marketing sends Sales Ops only:

- ICP
- offer angle
- asset links
- hook and CTA
- proof claims requiring source
- approved/rejected status
- recommended DM/proposal angle

Marketing does not send full prompt history unless Sales Ops explicitly needs it.

## Handoff To Operations

Marketing sends Operations only:

- site/page asset requirements
- publishing status
- CMS/webhook needs
- tracking needs
- dashboard/reporting requirements

## Current Priority Capability

`luxury-ai-video-website-builder`

Goal: let the Marketing Mini Intern build Apple/luxury-style demo sites by orchestrating Nano Banana, Seedance, front-end design, GitHub, Vercel, and Reviewer QA.

Validation target:

1. Internal architecture-style demo.
2. AgentOSync demo site.
3. Client-style demo such as barber shop AVAPI or Amax campaign page.

## Video Editing / Motion Graphics Workflow

Use Hyperframes when the raw creative assets already exist and Marketing needs a polished video.

```mermaid
flowchart TD
  A["Script / transcript / campaign angle"] --> B["Asset inventory"]
  B --> C["Higgsfield / Seedance / Nano assets"]
  B --> D["Screen recordings / UI stills"]
  C --> E["Hyperframes storyboard"]
  D --> E
  E --> F["HTML/CSS/GSAP compositions"]
  F --> G["Lint + preview"]
  G --> H["Draft render"]
  H --> I["Frame verification"]
  I --> J["Reviewer QA"]
  J --> K["Human approval"]
  K --> L["Final MP4 / posting packet"]
```

Best first use cases:

1. AgentOSync LinkedIn short with captions and motion graphics.
2. Amax WhatsApp/forms insights dashboard walkthrough.
3. Barber AVAPI demo explainer with UI callouts.

## Higgsfield Creative Agency Workflow

Use this when Marketing needs many tracked creative variants instead of one-off media.

```mermaid
flowchart TD
  A["Product / offer / ICP"] --> B["Approved reference assets"]
  B --> C["Advertising research / prior winners"]
  C --> D["Creative slate"]
  D --> E["Generation tracker"]
  E --> F["QA priority rows"]
  F --> G["Human approval to spend credits"]
  G --> H["Higgsfield CLI / MCP generation"]
  H --> I["Update job IDs + result URLs"]
  I --> J["Reviewer QA + human feedback"]
  J --> K["Style recipe extraction"]
  K --> L["Next variant slate"]
```

Rules:

- Prefer CLI for Claude Code batch workflows when available; MCP is fine for Claude web/chat.
- Product ads must use approved reference assets and product fidelity constraints.
- Generate 3-5 priority rows first; do not blindly run a whole slate.
- Every generated asset gets status, prompt, job ID, result URL, QA result, and lesson learned.
- Winners become style recipes; repeated style recipes become skill candidates.

## Hermes Niche Intelligence + Seedance Backlog Workflow

Use this when Marketing needs to convert creator research, YC/company signals, and audience comments into Seedance-ready content briefs.

```mermaid
flowchart TD
  A["Niche / signal lane"] --> B["Manual transcript, comments, or sourced YC snippets"]
  B --> C["VCOS-Niche-Intelligence-Operator"]
  C --> D["Recipe: hook, structure, content gap, visual format"]
  D --> E["3 content briefs + claim-risk labels"]
  E --> F["Umair approval / proprietary angle"]
  F --> G["Seedance prompt final"]
  G --> H["Draft generation"]
  H --> I["Reviewer QA + lesson learned"]
  I --> J["Asset bank / skill candidate"]
```

Rules:

- Start with manual data collection.
- YC signals are strategic framing inputs, not investment advice.
- Do not use "top startup" claims unless the criterion is stated.
- Do not imply a company endorses AgentOSync.
- Do not launch public niche accounts or schedules from this workflow without approval.
- **Higgsfield/browser safety (2026-06-19):** Generate via `higgsfield auth login` + CLI or user-driven MCP OAuth only. Never run `gstack/bin/chrome-cdp` or quit/kill the user's browser to "reuse" a session. Incident: `3_Project_Workspaces/3.1_AgentOSync_Revenue_Pipeline/03_gtm_campaigns/higgsfield/browser-session-incident-2026-06-19.md`.
