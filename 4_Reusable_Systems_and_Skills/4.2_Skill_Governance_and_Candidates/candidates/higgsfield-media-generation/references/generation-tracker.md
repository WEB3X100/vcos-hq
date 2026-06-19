# Generation Tracker

Use this when the workflow creates more than one asset or when the output may become a reusable pattern.

## Purpose

The tracker is the creative database. It prevents the Marketing Mini Intern from pulling the slot machine lever blindly and makes every generation learnable.

## Recommended Tabs Or Tables

1. `Generations`
2. `Creative Slate`
3. `By Product`
4. `By Style Recipe`
5. `Performance`
6. `Failures And Constraints`
7. `Approved Assets`

If Google Sheets or Airtable is unavailable, create a local Markdown or CSV tracker packet with the same columns.

## Generations Columns

| Column | Purpose |
| --- | --- |
| `asset_id` | Stable ID for the creative. |
| `created_at` | Date/time generated or planned. |
| `business_lane` | Amax internal proof, AgentOSync acquisition, client demo, etc. |
| `product_or_offer` | Product, service, demo, or offer. |
| `platform` | LinkedIn, TikTok, Reels, Meta, YouTube, website, etc. |
| `format` | Static ad, carousel, story, UGC, Hypermotion, hero loop, etc. |
| `aspect_ratio` | 9:16, 4:5, 1:1, 16:9. |
| `funnel_stage` | Awareness, education, proof, conversion. |
| `angle` | Curiosity, contrarian, stat flash, pain agitation, demo proof, etc. |
| `style_recipe` | Named recipe or source winner. |
| `model_route` | Nano Banana, Seedance, Marketing Studio, prompt packet, etc. |
| `reference_asset` | Link/path to required product or brand reference. |
| `prompt` | Exact prompt used. |
| `negative_constraints` | Constraints applied before generation. |
| `status` | planned, approved, generating, complete, in_review, revise, rejected, blocked. |
| `approval_status` | not_required, pending, approved, rejected. |
| `job_id` | Higgsfield job ID or provider job ID. |
| `result_url` | Output URL or local path. |
| `qa_score` | Pass/fail or numeric score. |
| `human_feedback` | One-sentence taste/quality note. |
| `lesson_learned` | Reusable learning. |

## Creative Slate Columns

Use this before generation.

| Column | Purpose |
| --- | --- |
| `priority` | ASAP, high, medium, low. |
| `test_variable` | What changed from the control. |
| `hypothesis` | Why this variant might work. |
| `prompt_ready` | yes/no. |
| `approved_to_generate` | yes/no. |
| `status` | blank, queued, generating, complete, blocked. |

## Status Rules

- Never generate rows with `approved_to_generate = no`.
- Never duplicate rows with `status = complete`.
- If a job is blocked or restricted, record the exact risky wording if known and add a cleaner replacement.
- If product identity drifts, mark `revise` and add product fidelity constraints before rerun.
- If an asset wins, copy its style recipe into `By Style Recipe`.

## Minimum Local Tracker Packet

```markdown
## Creative Tracker Packet

- Tracker owner:
- Business lane:
- Product / offer:
- Platform:
- Batch goal:
- Approved reference assets:
- Credit/budget boundary:

| priority | format | angle | style | prompt | status | approval | result | lesson |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
```
