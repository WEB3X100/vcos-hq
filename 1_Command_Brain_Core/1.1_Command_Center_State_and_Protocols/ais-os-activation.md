# AIS-OS Activation For VCOS HQ

Purpose: adapt `nateherkai/AIS-OS` into VCOS HQ without creating a second competing operating system.

Source: `https://github.com/nateherkai/AIS-OS` cloned locally at `6_Arsenal/repos/ais-os` on 2026-06-10.

Attribution: AIS-OS, the Three Ms of AI, and the Four Cs of an AIOS are from Nate Herk / AI Automation Society OS. VCOS uses the framework as an activation pattern, not as original branding.

## Activation Decision

AIS-OS is active as a VCOS operating pattern.

It should not replace HQ files, Obsidian, GBrain, Skill Foundry, or the Employee OS template. It should give VCOS a sharper weekly rhythm:

1. Onboard the HQ into a compact operator profile.
2. Audit the Four Cs weekly.
3. Level up one workflow weekly.
4. Ship one artifact at a time.

## Mapping To VCOS

| AIS-OS concept | VCOS location | Notes |
| --- | --- | --- |
| `CLAUDE.md` operating manual | root `CLAUDE.md`, `AGENTS.md` | VCOS already has these. Do not fork them. |
| `context/` | `1_Command_Brain_Core/1.2_Headquarters_Memory/` and project READMEs | HQ context already exists and should stay curated. |
| `connections.md` | `connections-map.md`, `key-workspaces.md` | Use VCOS connection registry and approval gates. |
| `decisions/log.md` | `1_Command_Brain_Core/1.2_Headquarters_Memory/decisions.md` | Use the existing VCOS decisions file. |
| `/audit` | `four-c-audit.md` | Run as a weekly structural audit. |
| `/level-up` | Skill Foundry + `gbrain-office-hours` | Use the Three Ms interview to select one automation or skill candidate. |
| `/onboard` | This activation note + fast path | Do not overwrite HQ; use a VCOS-native onboarding summary. |

## VCOS Day 1 Onboarding Summary

Q1: Who are you, what do you sell, who do you sell it to?

- Umair runs VCOS HQ as the command brain for AgentOSync, Open Claw, reusable Mini Interns, client delivery, and personal operating leverage.
- The sellable wedge is AI employees and operational automation for SMBs, starting with barbershop proof loops and then dealership `Employee 01: Front Desk`.
- Primary buyers are SMB operators who lose revenue through slow response, missed calls, scattered follow-up, weak proof, and manual execution.

Q2: Voice samples.

- Not captured yet. Need 1-2 raw pasted samples from real writing before drafting external-facing content in Umair's voice.

Q3: 90-day priorities.

1. Move AgentOSync toward paid proof and 100k MRR through daily ClickUp-driven execution.
2. Validate barbershop live demo loop, then convert the dealership wedge into a sellable Employee 01 package.
3. Turn VCOS HQ into a working Second Brain + AI OS with Obsidian, GBrain, skills, approval gates, and weekly cadence.

Q4: Revenue tracking.

- Not fully connected. Revenue/source-of-truth is pending. Stripe, CRM, accounting, and sales pipeline connections need explicit selection and approval.

Q5: Customer/team/outside communication.

- ClickUp is execution truth for AgentOSync.
- Slack or Telegram is preferred for mobile approval.
- Email/DM surfaces are not yet wired into the OS and remain approval-gated.

Q6: Meetings, notes, and docs.

- Obsidian opens VCOS HQ as the vault.
- Drive is intended file truth for client files.
- Meetily is an evaluation candidate for meeting intelligence.
- GBrain is initialized for conservative text-first retrieval over approved local Markdown.

Q7: Biggest recurring time sink and task tracking.

- Main bottleneck: turning many projects, tools, ideas, and client wedges into a focused daily operating rhythm.
- Task tracking should start from the AgentOSync ClickUp space/view when AgentOSync is discussed.

## Week 1 Build Order

1. **Context:** keep HQ Markdown curated; add only interpreted facts, decisions, blockers, and next actions.
2. **Connections:** verify read-first ClickUp, GitHub, Drive, Calendar, and approval-surface access before write access.
3. **Capabilities:** use `gbrain-office-hours` plus Skill Foundry to critique projects, branding, conversion, and delivery workflows.
4. **Cadence:** run a weekly Four C audit and a weekly Three Ms level-up session before automating recurring jobs.

## Next Steps To Create The OS

1. Fill the missing voice sample section with raw writing from real email, DM, LinkedIn, or docs.
2. Run the first VCOS Four C audit and save it to `four-c-audit.md`.
3. Choose one read-only connection to verify first: ClickUp, GitHub, Drive, or Calendar.
4. Use Three Ms level-up on one painful workflow, preferably AgentOSync daily execution or dealership missed-call recovery.
5. Produce one artifact from that session: prompt template, deterministic skill, AI-assisted skill, or Mini Intern SOP.
6. Add the artifact to Skill Foundry only if it is likely to repeat.
7. Add cadence only after two clean manual runs and clear approval gates.

## Conservative Rules

- Do not duplicate VCOS HQ into an AIS-OS folder.
- Do not overwrite `AGENTS.md`, `CLAUDE.md`, or existing HQ memory with AIS-OS templates.
- Do not connect write tools before read-only verification.
- Do not automate external sends, CRM mutations, publishing, spending, deletion, or production deployment without explicit human approval.
- Do not promote an idea into a skill until it has repeated value or a clear cross-client use case.
