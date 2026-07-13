# VCOS Dual-Laptop Architecture Overview

VCOS HQ is the canonical command brain. GitHub is the durable coordination bus for cross-laptop repository work.

- Umair/L1 (Mac): Sentinel and merge authority. Owns orchestration, approvals, integration review, and final human gates.
- L2 (Windows): Bounded Builder. Works on l2/* feature branches, creates draft pull requests, and never merges to main without explicit Umair/L1 approval.

## Sources of truth

- ClickUp: Business outcomes, priorities, owners, status, and human approvals.
- GitHub Issues: Repository-scoped requirements and acceptance criteria.
- GitHub pull requests: Proposed changes, checks, review, and merge evidence.
- VCOS HQ: Durable policies, decisions, routing, and compact operating context.

## Agent coordination

Agents do not share memory directly. Durable cross-device artifacts use Git and GitHub. Operational handoffs may also use agent messages, ClickUp comments, Telegram or WhatsApp, and designated handoff notes. Important decisions must be promoted into their canonical system of record.

## Communication

- L1 Chief of Staff uses WhatsApp as its primary human relay.
- L2 Builder Intern uses Telegram as its primary human relay.
- No autonomous external sends, publishing, client mutations, or approval claims are permitted.

## Networking

Tailscale, if approved and installed, may provide private networking between laptops. It is not a public Git service or a replacement for GitHub.

## Security and approval gates

- Secrets, credentials, private runtime files, and raw operational logs remain outside the repository.
- Draft-Only is the default. Authority expands only through explicit human approval and the applicable release gate.
- L2 never performs CRM or QBO mutations, external sends, production deployments, spending, or merges to main without explicit approval.

This structure provides clear ownership, verifiable evidence, and safe parallel execution across the dual-Hermes operating loop.
