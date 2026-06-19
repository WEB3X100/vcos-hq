---
name: seedance-loop-prompt
description: Use when generating a Seedance 2 video prompt for a seamless looping background video. Trigger when the user describes a product, scene, or concept for a website background loop, mentions Seedance, asks for a looping video prompt, background video, or provides a product with headlines for a cinematic background. Also trigger on phrases like "loop video", "website background video", "product loop", "endless loop video", or any visual concept intended for continuous playback on a webpage.
---

# Seedance Loop Prompt Builder

Generate hyper-detailed, structured video prompts for Seedance 2 that produce seamless looping background videos. Forces exhaustive specificity on camera, lighting, timing, text choreography, and loop mechanics — the details humans leave vague.

## Input expectations

**Required:**
- Product or subject (what's on screen)

**Optional — infer if not provided:**
- Headlines (1-2 text strings to bake into the video)
- Loop direction/concept (deconstruction, orbit, flythrough, etc.)
- Mood/tone
- Duration (default: 10 seconds)
- Color palette

## Confidence gate

- Has product/subject → generate immediately
- Missing product/subject → ask ONE focused question, then generate
- Never over-interrogate. Make creative decisions where the user hasn't specified.

## Direction inference

When the user doesn't specify a loop direction, infer from the product type:

| Product Type | Default Direction | Why |
|---|---|---|
| Mechanical / tech / electronics | Deconstruction reveal | Shows engineering, internals, precision |
| Vehicles / transportation | Motion flythrough or speed orbit | Emphasizes movement and power |
| Fashion / wearables / accessories | Slow orbit with material/texture focus | Highlights craftsmanship and detail |
| Food / beverage | Ingredient explosion or pour sequence | Shows freshness, composition |
| Abstract / software / SaaS | Particle morph or data visualization | Visualizes the intangible |
| Architecture / real estate | Cinematic flythrough or reveal | Shows space and scale |
| Beauty / skincare | Liquid or texture flow | Emphasizes sensory qualities |

## Output format

Generate a single structured prompt with ALL 7 sections below. Every section is mandatory — never skip one. Read `references/example-prompts.md` for calibration on detail level.

---

### SCENE
Describe the subject and environment:
- Product/subject: material, color, form factor, key visual details. Be precise — "matte black over-ear headphones with brushed aluminum hinges" not "headphones."
- Environment: void, studio, abstract space, etc. Describe what surrounds the product.
- Mood references: 1-2 real-world visual references to anchor the aesthetic (e.g., "Apple product film meets Dyson engineering reveal," "Nothing CMF reveal cinematics"). Always include at least one.
- Color palette: background tone, accent colors, highlight colors.

### CAMERA
Describe the camera behavior for the full duration:
- Motion type: 360-degree orbit, slow arc, push-pull, static, etc.
- Speed: "slow, unhurried, cinematic" or "aggressive, dynamic" — be specific.
- Start position = end position. The camera MUST return to its exact starting angle and distance. Specify the degree of rotation (e.g., "single continuous 360-degree horizontal orbit").
- Elevation, angle, and distance from subject.
- Any focal length or depth-of-field notes.

### ACTION ARC
Describe what happens between the identical first and last frames:
- Starting state (product at rest, fully assembled, etc.)
- Transformation: what changes, how it changes, in what order. Be granular — "panels peel back along invisible seams, revealing the 40mm drivers, neodymium magnets, voice coils, and acoustic chambers floating outward in orbital positions."
- Peak visual moment: the point of maximum visual drama (typically 40-60% through the duration). Call this out explicitly.
- Return: how everything comes back together. "Components drift back and reconstruct with precise mechanical clicks" — not just "it reverses."
- Pacing: slow build to peak, then satisfying resolution. Don't front-load all drama.

### TEXT CHOREOGRAPHY
**If the user provided headlines, include this section with full detail. If no headlines were provided, write exactly:** "No text. No UI. Background plate only."

For each headline:
- **Text:** The exact string, quoted
- **Entrance:** When it appears relative to the action arc (e.g., "appears as components reach full separation")
- **Position:** Upper third, center, lower third, left/right aligned — be specific
- **Size:** Large, dominant, unmissable. Text is the primary focus element on screen.
- **Contrast:** Text MUST sit against the darkest or simplest region of the frame. If the background behind text is busy or bright, specify a subtle darkening gradient, vignette, or clear zone behind the text. Describe how the text is ensured to be readable.
- **Exit:** When and how it leaves (or if it persists through the loop)
- **Motion:** How it enters — fade in, slide from edge, scale up from center, etc.

**HARD RULE: Readability is priority #1.** Text must never compete with or blend into the product or background. If a visual effect would reduce text legibility, the effect yields. The viewer's eye goes to the text first.

### LIGHTING & ATMOSPHERE
- Light source: direction, type (rim, key, ambient), color temperature
- **Static lighting throughout.** No shifts, flickers, or color temperature changes at any point in the video. This is non-negotiable for loop consistency.
- Edge/rim light: color, intensity, which edges it catches
- Atmospheric effects: particles, dust, bokeh, energy fields, etc.
- Particle state: density and distribution MUST be identical at the start and end of the loop. Specify this explicitly.

### LOOP SEAL
This section ensures the video loops seamlessly:
- **First frame and last frame are the same reference image.** Instruct image-to-video mode in Seedance with the identical image for start and end.
- Camera returns to exact starting position and angle.
- All animated or moving elements (product components, particles, effects) return to their starting state.
- No residual motion, particle drift, or lighting variation at the loop point.
- The return to starting state should feel satisfying and intentional — a mechanical click, a gentle settling, a clean resolve. Not abrupt.

### TECHNICAL
- Duration: [specified or default 10 seconds]
- Seamlessly looping video
- Image-to-video generation mode: use the same image for first frame and last frame
- No watermarks
- 4K resolution if supported

---

After presenting the prompt, always include this reminder:

> **Seedance setup:** Use image-to-video mode. Set the same image as both the first frame and last frame reference to ensure a seamless loop.

## Hard rules — enforced on every prompt

1. **Loop integrity.** The prompt describes a complete cycle returning to its starting state. Camera, product, particles, lighting — everything resets.
2. **Text readability is priority #1.** When headlines are present, text is large, high-contrast, and positioned against the calmest/darkest region. Visual effects yield to text legibility.
3. **Static lighting.** No light shifts, flickers, or color temperature changes throughout. Non-negotiable for seamless looping.
4. **Same first/last frame.** Always instruct image-to-video mode with identical start and end reference image.
5. **Describe visual results, not editing software.** "The frame scales inward rapidly" — not "apply a keyframed scale effect in After Effects." Seedance interprets descriptions of what happens on screen.

## Creative principles

1. **Specificity over vagueness.** "Slow 360-degree horizontal orbit at fixed 15-degree elevation, completing one full rotation" beats "camera moves around the subject." Include exact angles, speeds, degrees, percentages.
2. **The action arc needs a peak.** Every loop has a visual climax — maximum separation, closest zoom, most dramatic reveal — roughly 40-60% through.
3. **Contrast in pacing.** Slow build, peak, satisfying resolution. The quiet moments make the dramatic ones hit.
4. **Mood references anchor style.** Always include 1-2 real-world references (brand films, product reveals, director styles) to ground the aesthetic.
5. **Energy must resolve.** The return to starting state should feel earned and satisfying, not like the prompt ran out of ideas.

## Tone

- Direct and technical — like a director's shot notes, not a marketing brief
- No hype words: never use "stunning," "breathtaking," "incredible," "mesmerizing"
- Concise but complete — every detail earns its place
- Bullet points within sections for scanability
- Describe what happens, let the visuals speak
