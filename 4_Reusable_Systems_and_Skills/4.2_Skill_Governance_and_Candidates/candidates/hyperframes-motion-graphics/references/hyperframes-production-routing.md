# Hyperframes Production Routing

Use Hyperframes as the deterministic editing and motion graphics layer after raw creative assets exist.

## What Hyperframes Gives VCOS

- HTML/CSS/GSAP motion graphics instead of timeline-only manual editing.
- Deterministic renders that can be linted, previewed, versioned, and re-run.
- Reusable compositions for captions, lower thirds, social cards, product demos, app showcases, flowcharts, transitions, and outros.
- A bridge between AI-generated assets and polished marketing videos.

## Best VCOS Fit

| Need | Use Hyperframes For |
| --- | --- |
| LinkedIn short-form | Talking-head + captions + motion graphics + CTA |
| AgentOSync product proof | UI recordings, dashboard walkthroughs, social proof cards, app-showcase scenes |
| Amax/client demos | Workflow explainer videos, before/after data-flow visuals, dashboard signal walkthroughs |
| Higgsfield assets | Final assembly, typography, captions, transitions, lower thirds, outro cards |
| Website demos | Website-to-video capture and animated product walkthroughs |
| Educational content | Lesson sections, word-synced motion graphics, transcript-driven captions |

## Provider Relationship

Hyperframes does not replace Higgsfield.

- Nano Banana Pro: static hero frames, diagrams, thumbnails.
- Seedance: cinematic short clips and visual plates.
- Avatar/voice tools: narration and talking-head source clips.
- Hyperframes: edit, assemble, caption, animate, verify, render.

## Standard Project Shape

```text
video-projects/<project-slug>/
├── index.html
├── compositions/
├── assets/
├── renders/
├── hyperframes.json
├── meta.json
├── STORYBOARD.md
└── HANDOFF.md
```

## Commands To Know

```bash
npx hyperframes doctor
npx hyperframes lint
npx hyperframes preview
npx hyperframes compositions
npx hyperframes render --quality draft --output renders/draft.mp4
npx hyperframes render --quality standard --output renders/final.mp4
npx hyperframes transcribe <file> --model small.en --json
npx hyperframes tts "text" --voice am_adam --output narration.wav
```

## Build Rules

- Work inside `video-projects/<project-slug>`, not the workspace root.
- Every project needs `hyperframes.json` and `meta.json`.
- Every visible timed element needs timing metadata.
- Every composition registers one paused GSAP timeline on `window.__timelines`.
- Use deterministic logic only: no `Date.now`, unseeded `Math.random`, or render-time network fetches.
- Do not animate `width`, `height`, `top`, or `left` directly on video elements; wrap video in a div and animate the wrapper.
- Use separate audio elements for audio mixing.

## VCOS Marketing Routes

### Short-Form Social

Use for LinkedIn/TikTok/Reels.

Inputs:

- script
- transcript or voiceover
- talking-head/avatar/raw clip
- brand tokens
- CTA

Outputs:

- 9:16 MP4
- caption-synced motion graphics
- hook frames
- posting draft packet

### Product / Workflow Demo

Use for AgentOSync, Amax, barber AVAPI, dashboards, and app demos.

Inputs:

- screen recordings or screenshots
- workflow narrative
- product claims and sources
- logo/brand tokens

Outputs:

- polished demo MP4
- lower thirds
- UI zooms / callouts
- proof/claim review packet

### Educational Lesson

Use for training, onboarding, YouTube SME clips, or internal knowledge.

Inputs:

- long script or transcript
- lesson sections
- voice/audio
- supporting visuals

Outputs:

- sectioned lesson video
- word-synced motion graphics
- chapterized handoff notes

