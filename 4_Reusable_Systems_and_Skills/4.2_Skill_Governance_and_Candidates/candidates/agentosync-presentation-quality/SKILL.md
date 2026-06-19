---
name: agentosync-presentation-quality
description: Use when creating, coding, redesigning, or reviewing AgentOSync client-facing PowerPoint/PDF presentations, pitch assets, demo walkthroughs, proposal decks, dealership/SMB operating-system decks, or reusable slide design systems. Enforces AgentOSync brand tokens, trusted-partner storytelling, hook/retention structure, visual proof quality, layout QA, and client-ready next steps.
---

# AgentOSync Presentation Quality And Design System

Use this skill to produce client-ready AgentOSync presentations that feel diagnosed, visual, credible, and ready to send after content is known.

## Required Resources

Load only what the task needs:

- For coded deck generation, import or copy patterns from `assets/presentation-design-system/agentosyncDeckSystem.mjs`.
- For visual design rules, read `references/agentosync-slide-design-system.md`.
- For story hooks, slide diagnosis, and attention/retention formats, read `references/client-story-hooks.md`.
- For final deck review, read `references/client-readiness-review.md` and run `scripts/review_deck_language.py` on deck source or extracted slide text.

## Non-Negotiables

- Never ship client-facing slides with internal coaching words: `Positioning`, `Sales framing`, `wow moment`, `pitch`, `close`, `conversion`, `no-brainer`.
- Never use blurry screenshots, unreadable phone captures, overflowing text, or cramped boxes.
- Never end with a sales-team coaching slide. End with a client decision path.
- Never frame AgentOSync as AI replacing people. Frame it as an operating layer that organizes, enhances, and optimizes the work already happening.
- Prefer plain language: `organize`, `enhance`, `optimize`, `route`, `review`, `approve`, `surface`, `follow up`, `keep visible`.

## Brand Core

Use `assets/agentosync-logo-preview.png` as the visual brand reference and `assets/AgentoSync.ai.pdf` as the source asset when available.

Default deck feel:

- Deep navy foundation, white claims, cyan/blue signal accents, limited green/gold/red status colors.
- Confident, technical, human, precise.
- Visual proof first: workflow maps, queues, matrices, tables, simple charts, before/after diagrams.
- Short claims and clean proof objects. The client should understand the slide at thumbnail size and remember it after the meeting.

Core dealership explanation:

```text
We are not onboarding a new text app. We are organizing and optimizing how data moves through the current WhatsApp workflow, so operations, sales, and ownership can see the right context at the right time.
```

## Build Workflow

1. Diagnose the client’s actual day: roles, tasks, delays, handoffs, anxiety points, and approval moments.
2. Write a claim spine where every slide has one client-relevant claim and one proof object.
3. Select 3-5 attention hooks from `references/client-story-hooks.md`; do not use clickbait language, but do create contrast.
4. Build with the coded design system where possible: colors, spacing, role panels, queues, approval matrices, flow lanes, CTA steps.
5. Render every slide and inspect contact sheet plus full-size high-risk slides.
6. Run the client-readiness review and language scan before delivering PPTX/PDF.

## Client CTA Rule

The final slide must answer: what we validate together, what sample data/workflow is needed, which approval rules are defined, what the client sees at the end, and the smallest safe live lane to decide on.
