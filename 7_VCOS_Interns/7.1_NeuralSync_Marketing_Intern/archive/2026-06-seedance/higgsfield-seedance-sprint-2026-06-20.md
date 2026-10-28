# Higgsfield Seedance Sprint — Jun 20–23, 2026

**Window:** 3 days unlimited Seedance on Higgsfield Ultimate  
**Account:** info@agentosync.com (Ultimate plan)  
**Goal:** Render 5+ approved LinkedIn shorts from the 1-week backlog; bank 2 hero loops for demo site.

## Credit Budget Strategy

| Tier | Count | Model | Purpose |
| --- | --- | --- | --- |
| P0 — LinkedIn shorts | 7 | `seedance_2_0` | One per backlog day, 9:16, 10–15s |
| P1 — Thumbnails | 7 | `nano_banana_2` | Text-on-dark stills for each post |
| P2 — Hero loops | 2 | `seedance_2_0` + loop seal | AgentOSync demo site backgrounds |
| P3 — Remix winners | 3 | `seedance_2_0` | Variant hooks on top-performing angle |

**Day 1 (Jun 20):** Generate P0 rows 1–3 (Mon–Wed backlog)  
**Day 2 (Jun 21):** Generate P0 rows 4–6 + P1 thumbnails batch  
**Day 3 (Jun 22):** Generate P0 row 7 + P2 hero loops + P3 remixes  
**Day 4 (Jun 23):** QA pass, revise failures, extract style recipes

## CLI Commands

```bash
# Verify auth + credits
higgsfield account status

# List video models
higgsfield model list --video

# Generate a LinkedIn short (replace prompt from day file)
higgsfield generate create seedance_2_0 \
  --prompt "..." \
  --aspect-ratio 9:16 \
  --duration 15

# Wait for job
higgsfield generate wait <job_id>

# Static thumbnail
higgsfield generate create nano_banana_2 \
  --prompt "..." \
  --aspect-ratio 9:16
```

## Batch Workflow (Claude Code)

1. Open repo: `vcos-hq` worktree or `vcos-employee-ns-marketing-intern`
2. Read `AGENTS.md` + today's backlog day file
3. Copy Seedance prompt block verbatim
4. Run CLI generate → log `job_id` in `generation-tracker.csv`
5. Run Reviewer QA rubric (internal) before marking `in_review`
6. Umair approves → status `approved` → queue for LinkedIn

## QA Gate (before marking complete)

- [ ] Hook readable in first 2 seconds
- [ ] Text contrast sufficient on mobile
- [ ] No watermarks
- [ ] Brand villain/hero clear without audio
- [ ] Claim-risk flags noted in tracker
- [ ] Lesson learned logged if revised

## Style Recipes To Extract

After sprint, document winners in `style-recipes/`:

1. **Phone Tag Horror** — burning cash + shake + red glitch
2. **8-Second Rule** — split screen missed calls vs green AI dashboard
3. **Incredulous WHAT** — minimalist black/white text slam

## Incident Prevention

Do **not** use `gstack/bin/chrome-cdp` to access Higgsfield. Use CLI auth or MCP OAuth only. See `claude-code-higgsfield-setup.md`.