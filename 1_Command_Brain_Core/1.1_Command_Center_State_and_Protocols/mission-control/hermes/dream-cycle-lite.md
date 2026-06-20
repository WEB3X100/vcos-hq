# Dream Cycle Lite — Before Sleep (L1)

**Profile:** `vcos-brain-grok`  
**When:** Variable, before sleep (not a cron until brief loop proven)  
**Output:** Draft only — human approves before durable writes

## Manual trigger prompt

```
Dream Cycle lite for VCOS.

PATH PREFIX:
MC=1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/mission-control
HANDOFFS=1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/session-briefs/handoffs

Read today's Hermes sessions, MC/briefs/ latest, and any handoffs in HANDOFFS/.

Output exactly these 3 fields + optional soul draft:

## Dream Cycle Lite — [DATE]

1. What worked (promote): [1-3 bullets]
2. What failed (root cause): [1-3 bullets]
3. Tomorrow prevention rule: [1 sentence]

Optional DRAFT soul.md tweak (do not apply):
- [proposed change or "none"]

Write to MC/dream-cycles/YYYY-MM-DD-dream-cycle-lite.md
Do not mutate ClickUp, GitHub main, or client systems.
```

## Promotion rule

Only after Umair scores the 7pm brief ≥3.5 for 5 consecutive nights → consider promoting to nightly cron at 11:30 PM.