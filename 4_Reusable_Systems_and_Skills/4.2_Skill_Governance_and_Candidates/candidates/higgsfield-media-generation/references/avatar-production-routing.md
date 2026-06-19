# Avatar Production Routing

Use this for avatar videos, talking-head explainers, course videos, AI spokesperson clips, founder-style narration, or news-style content. This route is provider-flexible: Higgsfield-friendly first when available, HeyGen-style only when a specific avatar API is chosen.

## Core Shift

The bottleneck moves from production to thinking.

- Human owns: idea, strategy, script, claims, final approval.
- Agent owns: production orchestration, chunking, prompt packets, state tracking, QA packets, and tool handoffs.
- Reviewer QA owns: authenticity risk, claim risk, brand fit, and whether the video should stay draft-only.

## Provider Routing

| Need | Preferred Route | Fallback |
| --- | --- | --- |
| Cinematic B-roll, website hero loop, product/service visual | Higgsfield `generate_video` / Seedance route | Prompt packet for manual Higgsfield UI |
| Static image, avatar backdrop, thumbnail, diagram | Higgsfield `generate_image` / Nano Banana route | Prompt packet |
| Avatar/talking-head video using a digital twin | Higgsfield avatar/character workflow if available and approved | HeyGen-style provider-specific route |
| Voice clone or narration | Approved voice provider or existing recorded audio | Human-recorded audio |
| Course/module video batch | Provider-neutral batch pipeline | HeyGen-style script/audio/video pipeline if credentials and approval exist |

Do not claim a provider can do a specific feature unless it has been validated in the current environment.

## Provider-Neutral Pipeline

```markdown
## Avatar Video Production Packet

- Outcome:
- Business lane:
- Audience:
- Funnel stage:
- Human likeness / avatar source:
- Voice source:
- Script source:
- Chunking rule:
- Visual style:
- Background / B-roll needs:
- Motion graphics needs:
- Provider route:
- Dry-run plan:
- State tracking plan:
- QA gate:
- Approval status:
- Output destination:
```

## Batch Workflow

1. Load scripts from local text, Google Docs, Drive, ClickUp, or approved source.
2. Split into chunks at natural sentence or section boundaries.
3. Generate or attach narration/audio.
4. Route each chunk to the selected avatar/video provider.
5. Track state per chunk so the job is resumable.
6. Poll/download outputs or record manual output links.
7. Stitch, sequence, or prepare handoff instructions when needed.
8. Run Reviewer QA before public use.
9. Record prompt/settings/provider/output links.
10. Stop before publishing or external delivery until human approval is explicit.

## Lessons From HeyGen Studio Template

The referenced HeyGen template is useful as an architecture pattern:

- `config.json` stores avatar, voice, chunking, concurrency, and lesson metadata.
- `.env` stores API keys and must never be committed.
- `state.json` tracks progress so jobs can resume.
- `--dry-run` exports/splits scripts without spending credits.
- `--lesson` and `--max-parts` enable small tests before full generation.
- output folders separate scripts, audio, and videos.

Do not copy this as a HeyGen-only assumption. Translate it into a provider-neutral production pattern.

## Safety Rules

- Digital twins, client likenesses, founder likenesses, and voice clones require explicit human approval.
- Never generate a voice/avatar that impersonates someone without consent.
- Never publish avatar content without approval.
- Mark AI-generated avatar/video content according to platform/client requirements when needed.
- Do not invent claims, metrics, testimonials, customer results, or source attributions.
- Keep API keys in `.env` only and exclude `.env` from Git.
- Start every new provider with one short dry run or one chunk before batch processing.

## Higgsfield-Friendly Prompt Packet

When routing avatar or narrator-adjacent work through Higgsfield, prepare:

```markdown
## Higgsfield Avatar / Narrated Video Prompt Packet

- Scene:
- Avatar / subject description:
- Facial expression / gesture style:
- Wardrobe / presentation style:
- Background:
- Camera framing:
- Motion / gesture direction:
- On-screen text:
- B-roll or visual inserts:
- Audio / narration source:
- Duration:
- Aspect ratio:
- Negative constraints:
- Approval status:
```

## QA Checks

- Does the script have a clear idea worth producing?
- Would the avatar make the content more useful, or only cheaper?
- Is the viewer likely to feel misled?
- Are all claims sourced or approval-gated?
- Is the voice/likeness consent clear?
- Is the first 3 seconds strong enough for the platform?
- Is the batch small enough for a safe first test?

