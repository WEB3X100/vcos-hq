# Content Intel Routine Claude Code Guide

Purpose: monitor important AI/operator signals, synthesize what matters, and draft approval-gated posts in Umair's voice.

This is the first Claude Code routine to validate because it solves a real daily pain: falling behind on AI updates while also needing proof-driven public content.

## Outcome

Every approved run should produce:

- 3 draft posts or captions.
- A short source summary explaining what changed and why it matters.
- A recommendation for which draft, if any, should be approved.
- A learning update from approved/rejected drafts.

Nothing posts automatically.

## Sources To Monitor

Start with a manually curated list. Do not add broad feeds.

Source categories:

- Claude Code and Anthropic updates.
- n8n / automation builders.
- AI agent builders and operators.
- Open-source AI workflow repos already in the VCOS Arsenal.
- SME posts from X, LinkedIn, Instagram, GitHub releases, and newsletters approved by Umair.

Store source candidates in `sources/source-list.md`.

## Voice Calibration

Voice examples live in `voice-calibration/`.

Required before automation:

- 10 approved Umair/AgentOSync posts or drafts.
- 5 rejected examples or "never say this" patterns.
- Tone rules.

Critical path:

Umair must fill `voice-calibration/approved-posts.md`, `voice-calibration/rejected-patterns.md`, and `voice-calibration/tone-rules.md` before this routine can produce differentiated content. Without those files, drafts are expected to sound generic.

Temporary tone rules:

- Direct, operational, proof-first.
- No vague hype.
- No unverified performance claims.
- No pretending a demo is a live client result.
- Explain why the update matters to operators and SMB owners.
- Tie content back to AgentOSync, VCOS, Amax, dealership, or delivery lessons when true.

## Workflow

1. Collect new source items.
2. Filter for relevance to VCOS, AgentOSync, Amax, dealership, automation, Claude Code, n8n, or AI-native services.
3. Summarize the signal:
   - what changed,
   - why it matters,
   - how it applies to live VCOS work,
   - what is noise.
4. Draft 3 posts:
   - LinkedIn operator post,
   - short X-style post,
   - Instagram caption or reel angle.
5. Run skeptic review:
   - claim safety,
   - approval gate,
   - proof level,
   - brand/voice fit.
6. Save output in `drafts/draft-content-YYYY-MM-DD.md`.
7. Wait for Umair approval before posting.

## Manual Before Automation

Run this routine manually at least 5 times before n8n or any scheduled trigger is built.

Automation gate:

- At least 5 manual runs completed.
- Drafts are good enough that Umair approves roughly 2 of 3 without heavy edits.
- Approved and rejected examples have been logged.
- Source list is stable.
- Approval surface is chosen.

Until those are true, do not build a scheduled scraper, API connection, Telegram bot, Buffer integration, or auto-posting flow.

## Approval Gates

Umair approval required before:

- Posting on LinkedIn, X, Instagram, YouTube, or any public channel.
- Mentioning a client, team member, prospect, or private workflow.
- Making proof claims about Amax, dealership, barbershop, or AgentOSync.
- Using screenshots, recordings, or customer-facing assets.
- Connecting n8n, Buffer, LinkedIn API, Telegram, or any auto-posting integration.

## Learning Loop

When Umair approves a draft:

- Copy it into `voice-calibration/approved-posts.md`.
- Record why it worked if known.

When Umair rejects a draft:

- Copy the draft or summary into `voice-calibration/rejected-patterns.md`.
- Add the rejection reason.

After 20 approved posts, use the approved set as the first real voice dataset.

## Avoid

- Do not build a dashboard for this routine first.
- Do not monitor too many accounts.
- Do not post automatically.
- Do not use private/client data as proof without approval.
- Do not let AI news chasing replace shipping dealership, Amax, or AgentOSync proof assets.
