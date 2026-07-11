# Capability Specification — Marketing Mini Intern

**Capability ID:** `marketing-mini-intern.linkedin-kit.v1`
**Status:** Draft-Only
**Authority:** Umair owns mission activation, preference confirmation, and external approval.

## 1. GCUA body mapping

| Layer | Marketing Mini Intern responsibility | Castle representation |
| --- | --- | --- |
| Brain | Hermes reasons over source material and creates five strategies. | Model/profile shown only with observed source and timestamp. |
| Eyes | Reads supplied transcripts, screenshots, files, or explicitly retrieved pages. | Input manifest and retrieval evidence. |
| Body | Mission state machine, caps, retries, validation, and handoffs. | Mission timeline and honest status. |
| Hands | File reading/writing and approved visual-generation tools. | Tool/effect log; no hidden external action. |
| Feet | L2 Windows Hermes runtime and scheduled overnight job. | Runtime heartbeat with freshness; stale becomes unknown. |

## 2. Telegram activation contract

Minimum operator command:

```text
CONTENT START
OUTCOME: <what this post should achieve>
SOURCE: <Telegram attachment, transcript, URL, screenshot, or file pointer>
AUDIENCE: <who it is for>
LEAD MAGNET: <existing asset/path or ASK HERMES TO PROPOSE>
CONSTRAINTS: <claims, client privacy, words/angles to avoid>
DUE: <time>
```

Hermes must return:

```text
MISSION RECEIVED — DRAFT GENERATION ONLY
ID: content-YYYYMMDD-NNN
INPUTS: <accepted / missing>
OUTPUT: <approved handoff directory>
HARD CAP: <time/turn/tool budget>
NEXT: working | blocked
NOT AUTHORIZED: publish, DM, comment, CRM, QBO, spend, deploy
```

If Telegram attachments cannot be accessed safely, Hermes asks for a transcript or file placed in the approved inbox. It does not pretend it read the source.

## 3. Mission state machine

```text
DRAFT_MISSION
  → RECEIVED
  → VALIDATING
  → WORKING
  → ARTIFACT_RETURNED
  → HUMAN_REVIEW
  → REVISION_REQUESTED
  → FINAL_REVIEW
  → APPROVED_FOR_MANUAL_USE

Any state → BLOCKED | FAILED | CANCELLED
Any edit after approval → FINAL_REVIEW (approval invalidated)
```

`READY` is not a mission state because it is ambiguous. `APPROVED_FOR_MANUAL_USE` still performs no external action.

## 4. Artifact layout

```text
cofounder-handoffs/
  01_content_drafts/
    <mission-id>/
      mission.json
      source-manifest.md
      handoff.md
      concepts/
        concept-a-authority.md
        concept-b-founder-story.md
        concept-c-contrarian.md
        concept-d-tactical.md
        concept-e-experimental.md
      visuals/
        concept-a-visual-brief.md
        ...
      claims-review.md
      feedback.json
      revisions/
        final-v1.md
      approval.json
```

Generated images, PDFs, or PPTX files may be added under `visuals/`; source prompts and generation provenance must stay beside them.

## 5. Mission schema

```json
{
  "schema_version": "1.0",
  "mission_id": "content-YYYYMMDD-NNN",
  "status": "RECEIVED",
  "requested_by": "umair",
  "requested_at": "ISO-8601",
  "due_at": "ISO-8601",
  "objective": "string",
  "audience": "string",
  "source_manifest": [],
  "constraints": [],
  "hard_cap": {"minutes": 90, "retries": 1},
  "runtime": {"device": "L2", "profile": "string", "observed_at": "ISO-8601"},
  "output_root": "relative/path",
  "revision": 0,
  "content_checksum": null,
  "approval": null,
  "errors": []
}
```

Runtime files must be validated, written atomically, and excluded from source-control seeds unless they are intentional handoff artifacts.

## 6. Feedback schema

```json
{
  "mission_id": "content-YYYYMMDD-NNN",
  "reviewer": "umair",
  "concept_feedback": [
    {
      "concept": "A",
      "verdict": "like|dislike|mixed",
      "keep": ["hook", "framework", "slide_3"],
      "remove": ["phrase", "claim"],
      "notes": "string"
    }
  ],
  "combine": {
    "base": "C",
    "elements": ["A.hook", "D.framework", "E.visual"]
  }
}
```

## 7. Approval record

```json
{
  "mission_id": "content-YYYYMMDD-NNN",
  "revision": 2,
  "checksum": "sha256:...",
  "decision": "APPROVED_FOR_MANUAL_USE",
  "approved_by": "umair",
  "approved_at": "ISO-8601",
  "external_action_performed": false
}
```

## 8. Quality gates

- Five distinct theses and structures.
- Tone grounded in confirmed voice references; uncertainty labeled.
- No invented results, clients, revenue, metrics, quotes, or experiences.
- Private AMAX information excluded from public-facing content.
- Lead magnet exists or is explicitly labeled `PROPOSED — NOT YET BUILT`.
- Visual brief matches the post and follows the 3–5 word on-screen hook rule where applicable.
- Every claim is supported, qualified, removed, or routed to human verification.
- Handoff packet is complete before `ARTIFACT_RETURNED`.

## 9. Failure behavior

- Missing input → `BLOCKED_INPUT`, with exact request.
- Retrieval failure → cite failure; never summarize unread material.
- Partial generation → preserve completed files and mark missing deliverables.
- Write failure → retain draft in process response and do not claim artifact saved.
- Duplicate mission ID → reject; never overwrite.
- L2 heartbeat stale → Castle displays `UNKNOWN/STALE`, not `working`.
- Invalid handoff schema → quarantine from morning review queue.
