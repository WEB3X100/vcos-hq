# Model Routing Policy

## Score

Score each dimension from 0 to 2:

| Dimension | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Consequence | internal/reversible | meaningful rework | money, client trust, public or irreversible |
| Ambiguity | exact procedure | some judgment | mechanism or direction unclear |
| Novelty | repeated pattern | adapted pattern | new architecture or creative system |
| Quality leverage | polish has little impact | quality affects adoption | marginal quality materially changes outcome |
| Verification difficulty | binary | mixed | semantic/adversarial |

Total `0-3`: Luna eligible for mechanical roles.

Total `4-7`: Terra default.

Total `8-10`: Sol eligible for the narrow quality kernel or final judge.

Record all five component scores in `ARTIFACT-CONTRACT.yaml`. `risk_score` is their sum; ambiguity is already included and must not be added twice. The routing helper accepts component scores and computes the total.

## Forced minimums

- Finance, legal, security, privacy, public claims, production mutation, or irreversible action: Terra semantic review minimum.
- Flagship executive/client artifact: Sol quality kernel recommended.
- Formatting, extraction, evidence reconciliation, variants, and deterministic check classification: Luna default.
- Normal repo implementation with an approved design: Terra default.

## Escalation

Escalate Luna -> Terra when:

- a new judgment or tradeoff appears
- the checklist cannot decide pass/fail
- two mechanical attempts fail
- output affects client trust or public positioning

Escalate Terra -> Sol when:

- architecture remains disputed
- a critical finding survives remediation
- flagship quality depends on the decision
- security, financial, legal, or irreversible consequences are material

## De-escalation

After Sol defines the mechanism or quality kernel, return scoped implementation to Terra. After Terra defines the semantic remediation, return formatting and evidence reconciliation to Luna.

## Current official price constants

These values are only for proxy estimates and must be reverified before financial reporting:

| Model | Input / 1M | Output / 1M |
| --- | ---: | ---: |
| `gpt-5.6-sol` | $5.00 | $30.00 |
| `gpt-5.6-terra` | $2.50 | $15.00 |
| `gpt-5.6-luna` | $1.00 | $6.00 |

Never claim actual savings from character estimates. Use provider usage records or CodeBurn for actual cost comparison.
