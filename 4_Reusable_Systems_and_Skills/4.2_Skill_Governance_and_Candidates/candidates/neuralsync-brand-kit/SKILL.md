---
name: neuralsync-brand-kit
description: Use when a NeuralSync proposal, PDF, slide deck, sales asset, landing page, or campaign needs approved brand tokens, logos, typography, layout rules, or master-template references. Resolves the canonical asset and approval state without treating drafts as approved or copying client-confidential material.
---

# NeuralSync Brand Kit Resolver

## Purpose

Provide one shared, reviewable source for NeuralSync visual identity. This candidate is a resolver and governance contract; it is not proof that the brand kit has been installed in OpenMaus or on the VPS.

## Workflow

1. Read `references/source-manifest.md`.
2. Identify the requested output type and the required logo, colors, fonts, spacing, imagery, and master template.
3. Confirm the approval state and owner of each asset. A draft or review file is not approved.
4. Return a compact brand packet containing exact source links, approved tokens, missing assets, and unresolved conflicts.
5. Stop final rendering when any required token or master is unapproved.

## Hard rules

- NeuralSync is the only public-facing brand.
- Do not use legacy AgentOSync or Founder OS branding.
- Never recreate a logo from memory when an approved source exists.
- Never declare a Drive asset approved without explicit evidence.
- Never expose credentials, client-confidential assets, or private Drive permissions.

## Completion

Complete only when the consuming skill receives an approved brand packet or a precise blocker list. Deployment to OpenMaus/VPS requires separate runtime verification and applicable human approval.
