# Image Routing

## Nano Banana Pro

Use Higgsfield `generate_image` with:

```json
{
  "model": "nano_banana_2",
  "prompt": "<final image prompt>",
  "aspect_ratio": "9:16",
  "resolution": "2k",
  "count": 1
}
```

Supported aspect ratios:

- `1:1`
- `3:2`
- `2:3`
- `4:3`
- `3:4`
- `4:5`
- `5:4`
- `9:16`
- `16:9`
- `21:9`

Supported resolutions:

- `1k`
- `2k`
- `4k`

## Prompt Packet

Use this structure after `creative-brief.md` and before generation:

```markdown
## Image Prompt Packet

- Outcome:
- Audience:
- Brand/proof lane:
- Format:
- Aspect ratio:
- Required text:
- Main subject:
- Setting/background:
- Style:
- Composition:
- Color/lighting:
- Negative constraints:
- Approval status:
```

## Open Claw Marketing Patterns

For LinkedIn/short-form static assets:

- Make the pain point readable in the first glance.
- Use bold title text when text is required; prefer the 3-5 Word Rule.
- Use Visual Format Inversion when the niche is visually repetitive.
- Target Shock Score 70+ for public awareness assets.
- Keep claims evidence-backed.
- Avoid tiny UI text unless generating at `4k`.
- Prefer concrete business scenes over abstract AI visuals.
- Do not include Amax/client details publicly unless approved.
- Ensure Visual-Audio Alignment even for static assets that support a spoken hook.

## Reference Images

If the user provides a reference image:

- Upload/confirm local files first when needed.
- Pass the media as `medias: [{ "role": "image", "value": "<media_id_or_url>" }]`.
- Preserve the user's requested identity/product/brand constraints.
- Do not train a reusable character unless the user explicitly asks for reusable identity training.
