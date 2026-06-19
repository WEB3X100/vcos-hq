# Creative Agency Loop

Use this when Higgsfield is being used as a repeatable creative production system, not a one-off generator.

## Goal

Turn Claude/Codex + Higgsfield into a Marketing Mini Intern workflow that can:

- research and plan creative angles
- generate tracked image/video variants
- preserve product and brand identity
- update a creative database
- learn from winners, rejections, and blocked prompts
- produce repeatable style recipes
- stop at human approval gates before public use

## Integration Preference

- Claude web/chat: Higgsfield MCP is acceptable.
- Claude Code / local agent workflow: prefer Higgsfield CLI when available to reduce MCP tool context overhead.
- If neither is available: produce prompt packets, tracker rows, and approval checklists.

Do not claim generation happened unless a job ID, result URL, or local output exists.

## Creative Agency Flow

1. Intake:
   - product / offer
   - ICP / buyer avatar
   - platform
   - desired format
   - proof source
   - reference assets
   - budget/credit tolerance
   - approval owner

2. Research layer:
   - Use an internal advertising masterclass, platform notes, performance data, or prior winners when available.
   - If no research exists, create a short research brief first instead of guessing.
   - Keep research summaries compact. Do not paste full raw articles into the skill context.

3. Creative slate:
   - Build rows before generating.
   - Each row should test a deliberate variable: angle, headline, platform, style, avatar/person presence, CTA, offer proof, or motion style.
   - Prioritize 3-5 rows for the first batch.

4. Generation:
   - QA before spending credits.
   - Generate the approved priority rows.
   - Update tracker status and result metadata immediately.

5. Review:
   - Mark each asset: `winner`, `usable`, `revise`, `reject`, or `blocked`.
   - Capture one-sentence human feedback.
   - For winners, extract the style recipe.
   - For rejects/blocks, add a negative constraint.

6. Next slate:
   - Remix winning mechanisms.
   - Do not blindly generate more of everything.
   - Change one or two variables at a time so the test remains interpretable.

## Product Fidelity Rule

When product identity matters, the prompt must include:

```markdown
Use the provided reference product exactly. Preserve shape, packaging color, logo placement, label hierarchy, visible text, cap, materials, and proportions. Do not redesign the product. Do not invent alternate labels or replace the product with a generic lookalike.
```

If video generation repeatedly distorts small product text, recommend one of these instead:

- simplify the label for video-only hero shots
- keep the product further from macro distortion
- use static product frame plus motion graphics
- generate product-only static ads before video
- use Hyperframes/remotion-style overlay text instead of asking the video model to render exact text

## Hypermotion Style Recipe

Use for premium product launch videos and fast paid-social tests.

Required ingredients:

- 4-7 second or 8-12 second duration
- product hero is visible in the first second
- fast push-in or orbit camera move
- macro detail shot
- kinetic background elements
- speed ramp or snap zoom
- 3-5 scene beats
- short on-screen hook text
- final product payoff frame

Avoid:

- slow generic lifestyle B-roll
- vague "cinematic" motion with no product action
- intimate or odd product touching unless the concept explicitly needs it
- unreadable product labels in close macro motion
- too many text claims inside generated video frames

## Batch Cadence

Draft cadence for a future routine:

- Sunday: analyze prior results and create 30-100 new tracker rows.
- Monday: generate approved priority rows with blank status.
- Wednesday: review winners/rejects and extract style recipes.
- Thursday: generate variants of winners.

This is a planning pattern, not permission to run unattended. External publishing and budget spend remain human-gated.
