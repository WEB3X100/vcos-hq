# Self-Improving Loop

Use this when a prompt fails QA, a Higgsfield render is rejected, or the human gives taste feedback.

## Failure Capture

Record:

- Asset type:
- Model:
- Route / provider:
- Prompt/settings:
- What failed:
- Why it failed:
- Human feedback:
- Blocked/restricted wording, if any:
- Replacement wording:
- Negative constraint to add:
- File to update:

## Where To Update

- Bad image composition, text, or static visual pattern -> `image-routing.md`
- Bad motion, pacing, storyboard, or video clarity -> `storyboard-patterns.md`
- Bad Marketing Studio / Hypermotion product ad pattern -> `creative-agency-loop.md`
- Missing tracker field, status issue, duplicate generation, or unclear job metadata -> `generation-tracker.md`
- Winning output that should be repeated -> `style-recipe-extraction.md` or a new style recipe file
- Bad QA decision or weak checklist -> `quality-rubric.md` or `uat-rubric.md`
- Wrong routing or missing approval gate -> `SKILL.md`
- Durable cross-VCOS vocabulary -> `1_Command_Brain_Core/1.2_Headquarters_Memory/ubiquitous_language.md`

## Rule

Do not add huge postmortems. Add one short negative constraint or rule that prevents the failure from recurring.

Example:

```markdown
- Avoid slow corporate B-roll pans for LinkedIn hook clips; use a visible action or transformation in the first 2 seconds.
```

```markdown
- Do not let product ad prompts describe the product from memory when a reference image exists; explicitly require exact reference fidelity for packaging, label, color, shape, and logo.
```
