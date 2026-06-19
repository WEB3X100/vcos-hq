# Client-Readiness Review

Use this reference before delivering any AgentOSync client-facing PPTX/PDF.

## Review Score

Score each dimension from 1-5. Do not ship if any dimension is below 4.

| Dimension | Pass Standard |
| --- | --- |
| Diagnosis depth | The deck shows the client’s real roles, tasks, handoffs, delays, and approval points. |
| Story hook | The first 3 slides create recognition, urgency, and trust without hype. |
| Visual proof | Every content slide has a table, flow, queue, matrix, map, or chart that carries the point. |
| Brand consistency | AgentOSync navy/cyan/white system is consistent and the logo is clean. |
| Plain language | Copy sounds like a trusted operator, not a salesperson. |
| Layout precision | No overflow, clipping, overlap, tiny text, or cramped boxes. |
| Screenshot quality | Screenshots are crisp or replaced with recreated visuals. |
| Decision path | The last slide gives client-facing next steps and approval-safe validation. |

## Red Flags

Fix immediately:

- Any client slide says `Positioning`, `Sales framing`, `wow moment`, `pitch`, `close`, `conversion`, or `no-brainer`.
- Final slide tells the salesperson what to do instead of telling the client what happens next.
- Text crosses a box edge or rests against a lower border.
- Phone screenshots are blurry or unreadable.
- Slide title is a topic label instead of a claim.
- Deck uses generic AI hype instead of the client’s operating reality.

## Required Final Pass

1. Render all slides to PNG.
2. Inspect the contact sheet for rhythm and brand consistency.
3. Inspect full-size slides with tables, queues, boxes, screenshots, and CTA steps.
4. Run `scripts/review_deck_language.py` against slide source or extracted text.
5. Confirm PDF page count and PPTX slide count.
6. Confirm the final assets are named clearly for client use.

## Client CTA Template

Use this structure for the final slide:

```text
What we validate together next

1. Pick one workflow.
2. Confirm sample data.
3. Define review points.
4. Walk the demo.
5. Decide the smallest safe live lane.
```

Keep this client-facing. Do not write a sales script.
