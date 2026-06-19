# Motion Quality Rubric

Use before calling a Hyperframes render final.

## Creative Rules

- One idea per beat.
- Cut fast unless the moment is a hero shot or outro.
- Typography carries meaning, not decoration.
- Motion should clarify the message.
- Every scene needs a focal point.
- No flat backgrounds unless silence/contrast is intentional.
- Avoid visual soup: one primary idea, one primary color meaning, one main action.

## VCOS Hook Checks

| Check | Pass Criteria |
| --- | --- |
| Alignment | Motion, captions, visuals, and CTA reinforce the same idea. |
| Speed to Value | Viewer understands the point in the first 1-3 seconds. |
| Clarity | Text is readable and scenes are not overloaded. |
| Curiosity | The video opens a useful question or contrast. |
| Proof Safety | Claims are sourced, internal-only, or approval-gated. |

## Render Verification

Before final handoff:

- run lint
- preview in browser when possible
- render a draft
- pull frames at each hero moment
- inspect frames for cropped faces, text overflow, blank frames, broken brand colors, and awkward overlaps
- verify audio/caption sync where relevant
- only then render standard/final

## Common Failure Modes

- timeline shorter than clip slot creates black flashes
- catalog block CSS leaks into parent document
- unscoped `html, body` rules break canvas size
- video freezes if the video element itself is animated
- hard cuts feel cheap when a whip/blur transition is expected
- captions become unreadable over busy footage
- too many full-screen filters can cause flicker

