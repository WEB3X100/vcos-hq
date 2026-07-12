# Dream Cycle Lite — Before Sleep (L1)

**Profile:** `vcos-brain-grok`  
**When:** Variable, before sleep (not a cron until brief loop proven)  
**Output:** Draft only — human approves before durable writes

## Manual trigger prompt

```
Dream Cycle lite for VCOS. Read today's Hermes sessions, mission-control/briefs/ latest, and any handoffs in session-briefs/handoffs/.

Output exactly these 3 fields + optional soul draft:

## Dream Cycle Lite — [DATE]

1. What worked (promote): [1-3 bullets]
2. What failed (root cause): [1-3 bullets]
3. Tomorrow prevention rule: [1 sentence]

Optional DRAFT soul.md tweak (do not apply):
- [proposed change or "none"]

Write to mission-control/dream-cycles/YYYY-MM-DD-dream-cycle-lite.md
Do not mutate ClickUp, GitHub main, or client systems.
```

## Promotion rule

Only after Umair scores the 7pm brief ≥3.5 for 5 consecutive nights → consider promoting to nightly cron at 11:30 PM.