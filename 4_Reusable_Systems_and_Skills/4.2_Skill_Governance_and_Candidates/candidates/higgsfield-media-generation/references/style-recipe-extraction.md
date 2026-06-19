# Style Recipe Extraction

Use this when a Higgsfield output is strong enough that the user says some version of:

- "I love this one."
- "Make more like this."
- "Turn this into a skill."
- "This is the winning style."
- "Use this as the format going forward."

## Goal

Reverse-engineer the winning output into a reusable recipe without overfitting to one product.

## Extraction Questions

Capture:

- What product or offer was shown?
- What platform was the asset for?
- What was the hook or first-frame promise?
- What made the output feel good?
- What should remain constant next time?
- What should vary next time?
- What failure should be avoided?
- Does the recipe require a reference image?
- Does it use a person/model or product-only?
- What aspect ratio and duration worked?

## Recipe Template

~~~markdown
# Style Recipe: <name>

## Trigger

Use when:

## Best For

- Platform:
- Funnel stage:
- Product type:

## Required Inputs

- Product reference:
- Offer:
- Buyer avatar:
- On-screen hook:
- CTA:

## Visual DNA

- Camera:
- Motion:
- Lighting:
- Background:
- Product behavior:
- Text style:
- Pacing:

## Prompt Skeleton

```text
<prompt skeleton here>
```

## Hard Rules

- Preserve approved product reference exactly.
- Keep product visible in the first second.
- Use 3-5 words for first on-screen hook text.

## Avoid

- 

## QA Checklist

- Alignment:
- Speed to value:
- Clarity:
- Curiosity:
- Product fidelity:
- Text legibility:
~~~

## Promotion Rule

Do not promote a style recipe into a standalone skill until:

- it has produced at least 2 good outputs, or
- the user explicitly chooses it as a house style, or
- it maps directly to a high-priority revenue workflow.

When promoted, register it in `skill-registry.md` and the Marketing department capability map.
