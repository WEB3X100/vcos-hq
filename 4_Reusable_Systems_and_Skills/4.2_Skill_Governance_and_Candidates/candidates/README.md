# Skill Candidates

This folder holds SOPs that may become permanent skills.

## Promotion Rule

Promote a SOP only after 3 successful uses with clear value.

## Candidate Structure

```text
4_Reusable_Systems_and_Skills/4.2_Skill_Governance_and_Candidates/candidates/<candidate>/
├─ SKILL.md
├─ agents/openai.yaml
├─ assets/
├─ references/
├─ scripts/
└─ validation-log.md
```

Only include folders needed by the candidate. `SKILL.md` is the runnable interface; reference material, templates, and deterministic validators stay separate to keep runtime context lean.

## Current Candidates

| Candidate | Purpose | Proof requirement |
| --- | --- | --- |
| `hermes-prd-sprint-conductor` | Convert an approved outcome into a code-grounded PRD, GitHub sprint, reviewed implementation, and evidence-backed draft PR. | Three supervised missions with accepted artifacts and no unverifiable delivery claims. |
