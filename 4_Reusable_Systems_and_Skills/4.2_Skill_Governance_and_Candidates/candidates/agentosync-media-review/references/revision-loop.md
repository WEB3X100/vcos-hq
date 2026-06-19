# Revision Loop

Use this when an asset fails review or a repeated creative mistake appears.

## Steps

1. Name the failure in one sentence.
2. Identify the cause:
   - prompt ambiguity
   - wrong model/format
   - missing reference asset
   - weak business story
   - unsupported claim
   - brand mismatch
   - platform mismatch
3. Write a negative constraint.
4. Write a revised prompt.
5. Decide whether to retry generation or change the asset format.
6. Save the lesson if it is likely to repeat.

## Failure Log Format

```markdown
## Failure

Asset:
Lane:
Prompt:
Issue:
Root cause:
Negative constraint:
Revision:
Retry decision:
```

## Common Negative Constraints

- Do not show customer messages as sent; show them as pending human approval.
- Do not use fake revenue numbers.
- Do not use private Amax/client/passenger data.
- Do not render important text inside the video; leave room for editable overlays.
- Do not make the interface look like a fake crypto dashboard.
- Do not use generic blue-purple AI glow visuals.
- Do not use stock-office scenes without a visible business workflow.

## When To Change Format

Switch formats when:

- generated text keeps failing -> use editable overlay or carousel
- scene is too abstract -> use workflow diagram
- video feels fake -> use Loom/screen mockup
- asset is too dense -> split into carousel
- public risk is high -> keep internal training asset

