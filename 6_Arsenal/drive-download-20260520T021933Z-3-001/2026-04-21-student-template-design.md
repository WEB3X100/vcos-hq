# Student Template Design

A standalone, runnable template project that mirrors the AIS Website's core
scroll/3D/parallax architecture with generic content, intended for students to
analyze alongside the production site.

## Goals

- Teach the core "scrubbable canvas background + sliding 3D panels + char-fade
  hero" effect stack by providing a clean, working reference.
- Mirror the real architecture file-for-file where it matters (same component
  names, same scroll wiring) so students can map template → production.
- Remain deliberately non-clone-able: different color palette, generic copy,
  no AIS branding, no Skool/Nate Herk links, fewer panels.
- Be runnable on its own with zero ties to the parent AIS project.

## Non-Goals

- Full feature parity with the live site (no PlusPanel, no Achievements gallery,
  no `/first-agent` route, no workshop page).
- A production-ready site. This is a learning artifact.
- Bundled deploy tooling (Cloudflare config, wrangler, etc.).
- TypeScript. The live project is JSX; template matches.

## Location

`student-template/` at the AIS project root. Added to `.gitignore` is NOT
required — this folder is committed to the repo as part of the project. It is,
however, fully standalone: no symlinks, no shared imports, no references to
files outside its own directory.

## Folder Layout

```
student-template/
  README.md
  package.json
  vite.config.js
  index.html
  .gitignore
  scripts/
    make-frames.js          ← Node script: generates sample bg frames
  public/
    logo.svg                ← Neutral geometric placeholder
    bg-frames/
      frame-0001.jpg        ← ~30 generated gradient+noise frames
      ...
      frame-0030.jpg
  src/
    main.jsx
    App.jsx
    components/
      ScrollVideoBackground.jsx
      ScrollVideoBackground.css
      ScrollFloat.jsx
      SlidePanel.jsx
      ContentStack.jsx
      PillNav.jsx
      PanelOne.jsx
      PanelTwo.jsx
      PanelThree.jsx
      FinalCTA.jsx
    styles/
      tokens.css
      components.css
```

## Architecture

Mirrors the production site's composition:

- **App.jsx** — renders `ScrollVideoBackground`, `PillNav`, a full-viewport
  hero with `ScrollFloat`, then `ContentStack`, then a bottom spacer.
- **ScrollVideoBackground** — canvas that draws the currently-indexed frame
  from a preloaded array; index is computed from `window.scrollY / scrollMax`.
  Uses `requestAnimationFrame` throttling and a fallback-to-nearest-loaded
  frame strategy. Respects `prefers-reduced-motion`.
- **ScrollFloat** — hero copy where each character is wrapped in a `.char`
  span; GSAP ScrollTrigger with `scrub` drives a stagger that fades+pushes
  them down as the user scrolls the first ~900px.
- **SlidePanel** — wrapper that (1) slides its contents up from `y: 100%` to
  `y: 0%` via ScrollTrigger scrub between the slot's `top bottom` and
  `top top` positions, and (2) on `mousemove`, tilts the panel with
  `rotationX/Y` and translates `x/y` based on cursor distance from the
  panel's center. `transform-style: preserve-3d` + `perspective: 1200` on
  the wrapper make the tilt feel real.
- **ContentStack** — a vertical stack of `SectionSlot` divs (each
  `100vh`, flex-end bottom alignment). Each slot triggers the panel inside
  it. Three generic panels + a final CTA pill.
- **PillNav** — floating top nav. `PillItem` precomputes a circle radius
  from its bounding rect so the hover circle "fills" the pill on enter.
  Scroll-to via `gsap.scrollTo`.

## Content (Deliberately Generic)

- **Brand name**: "Motion Template" (used in logo alt text and footer)
- **Hero**: `BUILD / WITH MOTION` + generic subtitle + two CTAs that link
  to `#`
- **Panels**: "Section One", "Section Two", "Section Three" with short
  placeholder body copy (4–6 sentences each) and 2–3 simple cards per
  panel laid out in a grid. No domain-specific terminology.
- **Stats**: `10K+ / 500+ / #1` with generic labels ("Users", "Members",
  "Rank")
- **Final CTA**: "Get Started" pill linking to `#`
- **Nav items**: HOME, ABOUT, FEATURES, CONTACT, JOIN

## Visual Style (Deliberately Distinct)

Different from AIS so it doesn't read as a clone:

- **Primary**: indigo `#6366F1`
- **Accent**: violet `#A78BFA`
- **Dark BG**: `#0B0B14` / `#050510`
- **Text**: `#E5E7EB` / `#9CA3AF`
- **Font**: Inter (headings + body) or system stack — not Roboto Mono +
  Montserrat. Keeps it visually clearly *not* AIS.

Design tokens live in `styles/tokens.css`; all components reference them —
no hardcoded hex values in component files. Mirrors the AIS convention so
students see the same "tokens → components" pattern.

## Background Frames

- A Node script `scripts/make-frames.js` generates 30 JPG frames (800×450,
  indigo→violet gradient with a softly animated noise pattern). Uses only
  Node core + the `canvas` npm package (listed as a devDependency).
- The generator is run once by the implementer and committed JPGs ship
  with the template — students don't need to install `canvas` to run the
  demo.
- `ScrollVideoBackground.jsx` uses `FRAME_COUNT = 30` and the same frame
  loading / RAF-throttled draw strategy as the production component.
- `ANCHOR_ID` is removed (or set to a known element in ContentStack) —
  scrollMax falls back to full document scroll height.

## Teaching Aids

- Each of the three "effect" files (`ScrollVideoBackground`, `ScrollFloat`,
  `SlidePanel`) gets a 3–5 line header comment: what it does and the
  mechanism in one breath. No per-line narration — students read `README.md`
  for depth.
- `README.md` contains:
  1. How to run the template
  2. File-by-file walkthrough of each effect (what + how)
  3. How to swap in custom background frames (with an `ffmpeg` example
     command for extracting frames from a video)
  4. How to add a new section

## Dependencies

Independent `package.json`:

```json
{
  "name": "motion-template",
  "private": true,
  "version": "0.1.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "gsap": "^3.12.5",
    "react": "^18.3.1",
    "react-dom": "^18.3.1"
  },
  "devDependencies": {
    "@vitejs/plugin-react": "^4.3.0",
    "canvas": "^2.11.2",
    "vite": "^6.0.0"
  }
}
```

`canvas` is devDependency-only (used exclusively by `scripts/make-frames.js`).
Students who don't regenerate frames never need it.

## What Is Deliberately Excluded

- **AchievementsPanel, PlusPanel, ServicesPanel** (AIS-specific copy/layout)
- **FirstAgent / workshop route**
- **Cloudflare `wrangler.jsonc`, `_redirects`**
- **AIS logo, AIS color palette, Roboto Mono font**
- **Member counts, Skool links, Nate Herk references**
- **TypeScript, ESLint configs, Prettier configs** (keeps template readable)

## Acceptance

- `cd student-template && npm install && npm run dev` starts Vite, and the
  resulting page shows: hero with fade-down text, canvas background
  responding to scroll, three panels that slide up and tilt on mousemove,
  pill nav that scrolls smoothly, final CTA. No errors in console.
- No import path, asset reference, or string in the template folder points
  at anything outside `student-template/`.
- A grep for `AIS`, `Skool`, `Nate`, `2CA9E1`, `F39237`, `300K`, `260K`,
  `Montserrat`, `Roboto Mono` across `student-template/` returns nothing.
