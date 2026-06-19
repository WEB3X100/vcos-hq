---
name: agentosync-media-review
description: Use this skill after an AgentOSync/Open Claw/Amax image, video, preview sheet, Higgsfield render, Seedance clip, Nano Banana image, carousel, proof asset, or social creative has been generated and needs critique, brand-fit review, posting-schedule fit, revision prompts, or a draft-only publishing packet.
---

# AgentOSync Media Review

## Purpose

Review generated media before it becomes public, client-facing, or part of the AgentOSync proof engine.

This skill is the Reviewer/QA and Kingmaker loop after `higgsfield-media-generation`:

- Judge whether the asset fits AgentOSync, Amax, or the dealership wedge.
- Catch generic AI visuals, broken text, unsupported claims, weak hooks, and missing human approval boundaries.
- Decide whether to approve internally, request revision, or block public use.
- Produce rewrite prompts for Higgsfield/OpenArt/Claude/GPT when the asset fails.
- Package passing assets into draft-only captions, posting slots, and proof-story angles.

## Progressive Context Loading

Load only what the review needs:

- Every review: read `references/review-rubric.md`.
- Brand or company-fit review: read `references/brand-fit.md`.
- Posting schedule or channel strategy: read `references/posting-fit.md`.
- Failed output or repeated mistake: read `references/revision-loop.md`.

Do not load all references by default.

## Inputs

Ask for or infer:

- Asset file, screenshot, frame, link, or description.
- Lane: `amax`, `dealership`, `ammar`, `agentosync`, or `lead-funnel`.
- Asset type: image, short video, preview sheet, carousel, thumbnail, Loom visual, proof post.
- Intended platform: LinkedIn, X, Instagram, Upwork, website, internal training, outbound, demo.
- Intended audience: SMB owner, dealership GM, travel agency operator, clinic operator, prospect, internal team.
- Original prompt/settings if available.
- Current posting calendar or desired publish window if schedule fit is requested.

If no asset is attached, review the prompt or storyboard as a preflight review.

## Review Workflow

1. Identify the lane, platform, audience, and approval boundary.
2. Score the asset using `references/review-rubric.md`.
3. If brand fit matters, score against `references/brand-fit.md`.
4. If posting fit matters, score against `references/posting-fit.md`.
5. Classify the asset:
   - `approved-internal`: usable inside the team or as a private draft.
   - `revise-before-use`: promising, but needs specific fixes.
   - `blocked-for-public`: do not publish or send externally.
   - `approved-for-human-review`: ready for Umair to approve, still not published.
6. Produce a compact review packet.
7. If revision is needed, produce a revised generation prompt and specific negative constraints.
8. If the asset passes, produce a draft-only posting packet.

## Output Format

```markdown
# Media Review Packet

Asset:
Lane:
Platform:
Audience:
Verdict:

## Score
- Hook clarity: /10
- Brand fit: /10
- Visual credibility: /10
- Offer accuracy: /10
- Approval-boundary safety: /10
- Platform fit: /10
- Overall: /10

## What Works
- ...

## Risks
- ...

## Required Fixes
- ...

## Revised Prompt
...

## Draft-Only Posting Packet
- Caption angle:
- Hook:
- CTA:
- Suggested platform:
- Suggested timing:
- Required approval:
```

## Approval Gates

Never mark an asset as live-publishable. The highest external-facing verdict is `approved-for-human-review`.

Human approval is required before:

- publishing on LinkedIn, X, Instagram, website, Upwork, or ads
- sending media to prospects or clients
- using client names, logos, screenshots, or private data
- making performance, revenue, compliance, finance, or CRM claims
- turning a draft into an automated posting workflow

## Failure Patterns To Catch

- Looks like generic AI stock art.
- Text inside image/video is misspelled, warped, or too small.
- Visual says "fully automated" while the workflow is draft-only/human-approved.
- Claims revenue impact without proof.
- Uses Amax/private client data publicly.
- Feels too flashy for B2B operations.
- The hook is clever but the offer is unclear.
- Platform mismatch: horizontal asset for vertical-first post, or dense text for mobile feed.
- Missing next action or CTA.

## Handoff

If the asset passes, hand off to Kingmaker for post drafting.

If the asset fails, hand off to Marketing Intern or `higgsfield-media-generation` with the revised prompt and negative constraints.

If the failure repeats, run the self-improving loop in `references/revision-loop.md`.

