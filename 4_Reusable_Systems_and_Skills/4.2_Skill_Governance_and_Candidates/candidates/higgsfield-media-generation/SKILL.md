---
name: higgsfield-media-generation
description: Use this skill when creating or planning AI-generated images, pictures, diagrams, thumbnails, static ads, avatar videos, talking-head clips, course videos, website hero loops, short video clips, or tracked creative-testing batches through Higgsfield-friendly workflows. Routes high-quality images to Nano Banana Pro (`nano_banana_2`), short reference-driven clips to Seedance 2.0 (`seedance_2_0`), Marketing Studio / Hypermotion-style ads through the creative agency loop, and avatar/course-video requests through the avatar production route with approval gates for public or client-facing use.
---

# Higgsfield Media Generation

## Purpose

Create reusable Marketing Mini Intern media outputs through Higgsfield:

- Images, pictures, text-heavy visuals, diagrams, thumbnails, and static ads -> Nano Banana Pro (`nano_banana_2`).
- Short clips, image-to-video, reference-driven motion, product/identity-consistent clips -> Seedance 2.0 (`seedance_2_0`).
- Product launch ads, UGC-style ads, Instagram/TikTok/Meta creative variants, Hypermotion-style videos, and batch testing slates -> Higgsfield creative agency loop.
- Avatar videos, talking-head explainers, AI spokesperson clips, course lessons, and founder-style narrated videos -> avatar production route. Prefer Higgsfield-compatible generation when available; use HeyGen/ElevenLabs-style pipelines only as a provider-specific implementation option.

Use this as a production skill candidate for Open Claw / AgentOSync creative workflows. It can generate internal drafts, but publishing remains human-gated.

## Routing

| Request | Route |
| --- | --- |
| Static image, picture, diagram, thumbnail, text-on-image, 4K visual | `generate_image` with `model: "nano_banana_2"` |
| Short clip, image-to-video, start/end frame animation, reference-driven motion | `generate_video` with `model: "seedance_2_0"` |
| Avatar video, talking-head clip, course lesson, narrated educational clip, founder-style explainer | Avatar production route in `references/avatar-production-routing.md`; choose Higgsfield, HeyGen, or prompt packet based on available tools |
| Seamless website background loop or luxury hero video | Use Seedance loop prompt pattern, then route through `seedance_2_0` or prompt packet |
| Product/site ad from URL or Marketing Studio preset | Use creative agency loop in `references/creative-agency-loop.md` |
| Batch creative testing, ad matrix, weekly creative slate, or performance remixing | Use generation tracker in `references/generation-tracker.md`, then generate only approved rows |
| Reverse-engineer a winning output into a repeatable style recipe | Use `references/style-recipe-extraction.md` |
| Reusable digital twin / trained character | Use Soul Characters workflow, not this default route |
| Video virality or retention analysis | Use Virality Predictor workflow, not this default route |

Prefer the Higgsfield CLI for Claude Code / agentic batch workflows when available because it keeps the tool surface smaller than loading every MCP tool. Use the Higgsfield MCP when the user is already working inside Claude web/chat or when MCP is the only available integration. If neither is available, produce an approval-ready prompt packet instead of pretending generation happened.

## Browser Session Safety (mandatory)

**2026-06-19 incident:** Running `gstack/bin/chrome-cdp` force-quit the user's Chrome, symlinked their real profile, and caused mass browser logouts. See `3_Project_Workspaces/3.1_AgentOSync_Revenue_Pipeline/03_gtm_campaigns/higgsfield/browser-session-incident-2026-06-19.md`.

When the user says they are logged in or asks to "use my browser":

- Use **`higgsfield auth login`** + **`higgsfield generate create`** (same account, no browser hijack), or
- Ask the user to complete **Grok MCP OAuth** (`/mcps` → higgsfield → authenticate), or
- Let the user generate in the Higgsfield UI.

**Never without explicit human approval:**

- `gstack/bin/chrome-cdp` (no `--help` — mistaken args still run quit/kill + profile symlink + relaunch)
- `pkill` / `osascript quit` on the user's browser
- GStack cookie-import or CDP flows that close the active browser session
- Attaching to the live default browser profile for "session reuse"

## Progressive Context Loading

Load only what the current request needs:

- Every media request: read `references/creative-brief.md` and `references/quality-rubric.md`.
- Static image only: read `references/image-routing.md`; do not read `references/storyboard-patterns.md`.
- Short clip/video only: read `references/video-routing.md` and `references/storyboard-patterns.md`.
- Avatar/course/talking-head video only: read `references/avatar-production-routing.md`; read `references/storyboard-patterns.md` only if adding motion graphics, B-roll, or short-form pacing.
- Marketing Studio, Hypermotion, product ad, batch testing, or creative agency workflow: read `references/creative-agency-loop.md` and `references/generation-tracker.md`; read `references/style-recipe-extraction.md` only when turning a winning output into a reusable sub-skill.
- QA-only request: read `references/quality-rubric.md` and `references/uat-rubric.md`.
- Failed/rejected output: read `references/self-improving-loop.md`.

Do not load all references by default.

## V3 Workflow

1. Identify the asset type: image, short clip, website loop, avatar video, or course-style narrated video.
2. Interview the user when the visual vision is underspecified. Establish the shared design concept before prompt writing.
3. Confirm the business lane: Amax internal proof, AgentOSync public acquisition, or client-facing.
4. Create a creative brief using `references/creative-brief.md`.
5. Create the Higgsfield-ready prompt and settings.
6. Run QA against the Four Hook Commandments using `references/quality-rubric.md` and the pass/fail checklist in `references/uat-rubric.md`.
7. If QA fails, rewrite before requesting human approval or spending credits.
8. Ask for human approval before generation when the result is public-facing, credit-sensitive, uses client materials, or includes claims.
9. Generate through Higgsfield MCP.
10. Return the result plus exact prompt/settings used.
11. Stop before publishing, sending, posting, or using the result in public unless human approval is explicit.
12. If the human rejects the render, run the Self-Improving Loop and update the relevant reference with a negative constraint.

## Creative Agency Workflow

Use this when the user wants to scale ad creative, generate batches, build a creative database, or turn Higgsfield into a Marketing Mini Intern production desk.

1. Confirm the product, offer, platform, buyer avatar, proof source, and asset owner.
2. Collect approved reference assets. If product fidelity matters, store or tag the reference image and state: "Product must match the reference exactly; do not alter label, color, shape, logo, packaging, or visible product text."
3. Build or update the generation tracker using `references/generation-tracker.md`.
4. Create a creative slate with rows for product, platform, format, angle, style, model/route, prompt, status, approval status, job ID, result URL, and lesson learned.
5. Do not generate the full slate at once. Start with 3-5 priority rows.
6. QA each row before generation.
7. Generate only approved rows through Higgsfield CLI/MCP or return prompt packets.
8. Update the tracker with status, job ID, result URL, model/route, prompt, and review outcome.
9. Identify winners and rejected patterns.
10. Convert winners into a style recipe or sub-skill only after the user confirms what they liked.
11. Add negative constraints for blocked prompts, weak outputs, inconsistent product rendering, broken text, slow pacing, or off-brand visuals.

For details, read `references/creative-agency-loop.md`.

## Image Defaults

Use `nano_banana_2`.

Default settings:

- `aspect_ratio`: `1:1` for general images, `16:9` for website/YouTube, `9:16` for LinkedIn/TikTok/Reels, `4:5` for feed posts.
- `resolution`: `2k` by default; use `4k` for final polished visuals or diagrams with text.
- `count`: `1` unless the user asks for variants.

For detailed image patterns, read `references/image-routing.md`.

## Video Defaults

Use `seedance_2_0`.

Default settings:

- `aspect_ratio`: `9:16` for LinkedIn vertical video and short-form clips.
- `duration`: 4-8 seconds for hooks, up to 15 seconds for short concept clips.
- `resolution`: `720p` for drafts; `1080p` for polished review.
- `mode`: `fast` for exploration, `std` for final draft.
- `genre`: `auto` unless the creative explicitly needs action, comedy, noir, drama, epic, or horror.

For detailed video patterns, read `references/video-routing.md`.

For pacing and storyboard patterns, read `references/storyboard-patterns.md`.

## Marketing Studio / Hypermotion Defaults

Use this route for product launch videos, paid-social style ads, UGC variants, unboxing-style creative, fast-cut product motion, and conversion-focused creative batches.

Default stance:

- Treat vague words like "cool," "premium," "engaging," or "fast-paced" as inputs to translate into concrete camera motion, cut rhythm, product behavior, lighting, text, and scene changes.
- Preserve product identity from approved references. If the model struggles with small label text in video, recommend a simplified hero-label variant rather than silently changing the product.
- Use platform-specific output: `9:16` for TikTok/Reels/LinkedIn vertical, `4:5` for feed, `1:1` for square tests, `16:9` for website/YouTube/landing pages.
- For Hypermotion-style videos, specify fast product pushes, macro detail shots, speed ramps, kinetic background elements, 3-5 scene beats, and a clear product payoff.
- For UGC-style videos, specify whether a human/model should appear before generation. If the user did not approve a person, default to product-only.
- For batch testing, vary one or two variables per row: angle, headline, avatar, visual style, CTA, platform, or offer proof.

## Avatar / Course Video Defaults

Use `references/avatar-production-routing.md` for talking-head, avatar, digital twin, voiceover, course lesson, founder-style explainer, or news-style video workflows.

Default stance:

- Keep the human in the loop for the idea, script, and public claims.
- Treat avatar/video tooling as production acceleration, not strategy replacement.
- Use provider-neutral pipeline language: script source, chunking, voice/audio, avatar/video provider, render state, output, QA, approval.
- Prefer Higgsfield-compatible generation when the requested visual can be produced through Higgsfield tools.
- If a provider such as HeyGen is required, mark it as provider-specific and do not assume credentials/API access exist.
- Always start with a dry run or one short chunk before generating a full course/video batch.

## Approval Gates

Human approval is required before:

- public posting
- LinkedIn publishing
- sending generated media to prospects or clients
- making public claims in the media
- using client logos/testimonials
- paid campaigns or budget use
- generating sensitive likenesses or identity-based assets
- creating or publishing digital twins, voice clones, avatar videos, founder likenesses, client likenesses, or any video that could be mistaken for a real human recording

Reviewer/QA should check high-stakes outputs for factual claims, brand fit, visual clarity, text legibility, and hallucination risk before human approval.

## Tracking Requirements

Every generated or planned asset should be logged when the workflow is more than a one-off draft.

Minimum fields:

- asset ID
- date
- business lane
- product / offer
- platform
- format
- funnel stage
- angle
- style recipe
- model / route
- prompt
- reference asset
- status
- approval status
- job ID
- result URL
- QA score
- human feedback
- lesson learned

Use Google Sheets, Airtable, a CSV, or a local Markdown table depending on available tools. Do not require live Google Sheets access; if unavailable, create a local tracker packet the human can import.

## Agent Team Boundary

When separate agents are available:

- Marketing Intern owns creative brief and prompt writing.
- Reviewer/QA Intern owns `quality-rubric.md` and `uat-rubric.md` checks.
- Agent Infrastructure owns model routing and MCP setup.
- Human Operator owns final approval.

If the Reviewer/QA Intern fails the prompt, return it to Marketing Intern for revision instead of generating.
