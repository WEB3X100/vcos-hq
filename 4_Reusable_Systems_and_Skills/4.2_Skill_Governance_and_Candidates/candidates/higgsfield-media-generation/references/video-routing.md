# Video Routing

## Seedance 2.0

Use Higgsfield `generate_video` with:

```json
{
  "model": "seedance_2_0",
  "prompt": "<final video prompt>",
  "aspect_ratio": "9:16",
  "duration": 6,
  "resolution": "720p",
  "mode": "fast",
  "genre": "auto",
  "count": 1
}
```

Supported duration range:

- Minimum: 4 seconds
- Maximum: 15 seconds

Supported aspect ratios:

- `auto`
- `21:9`
- `16:9`
- `4:3`
- `1:1`
- `3:4`
- `9:16`

Supported resolutions:

- `480p`
- `720p`
- `1080p`

Modes:

- `fast`: exploration, rough drafts, hook testing
- `std`: polished draft

Genres:

- `auto`
- `action`
- `horror`
- `comedy`
- `noir`
- `drama`
- `epic`

## Prompt Packet

Use this structure after `creative-brief.md` and storyboard selection, before generation:

```markdown
## Short Clip Prompt Packet

- Outcome:
- Audience:
- Brand/proof lane:
- Funnel stage:
- Aspect ratio:
- Duration:
- Opening frame:
- Motion:
- Camera movement:
- On-screen text:
- Visual hook:
- Scene beats:
- Style:
- Negative constraints:
- Approval status:
```

## Reference Media

Seedance accepts reference roles:

- `image`
- `start_image`
- `end_image`
- `video`
- `audio`

For image-to-video, prefer:

```json
"medias": [
  { "role": "start_image", "value": "<image_media_id_or_job_id_or_url>" }
]
```

For start/end transitions:

```json
"medias": [
  { "role": "start_image", "value": "<start_image_id>" },
  { "role": "end_image", "value": "<end_image_id>" }
]
```

Do not pass `generate_audio` to Seedance 2.0.

## LinkedIn Video Hook Defaults

For AgentOSync LinkedIn clips:

- Use `9:16`.
- Keep the hook clip 4-8 seconds.
- Make the visual pain obvious immediately.
- Put bold on-screen text in the first 1-2 seconds when relevant.
- Follow the 3-5 Word Rule for hook text.
- Use a visual switch or re-hook for clips longer than 8 seconds.
- Use a Visual Pacifier for educational clips where the concept is abstract.
- Avoid public client claims unless approved.
- Generate drafts first; publishing requires human approval.
