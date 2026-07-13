# VCOS Dual-Laptop Architecture Overview

**VCOS HQ** is the canonical brain. GitHub serves as the coordination bus for all cross-laptop and multi-agent work.

- **L1 (Mac)**: Sentinel with exclusive authority to merge to `main`. Owns orchestration, approvals, and final human gates.
- **L2 (Windows)**: Bounded Builder. Operates exclusively on feature branches (`l2/*`), creates draft PRs, and never merges to `main` without explicit L1 approval.

**Truth sources**:
- ClickUp: business outcomes, tasks, and human decisions.
- GitHub: engineering evidence, versioned artifacts, and code history.

**Agent coordination**: Agents do not share memory directly. They exchange versioned artifacts and structured handoff packets only.

**Communication**: Telegram is the human relay channel. No autonomous external sends, publishes, or client mutations.

**Networking**: Tailscale (if used) provides optional private networking between laptops. It is never a public Git service or replacement for GitHub.

**Security & gates**:
- All secrets, credentials, and private runtime files stay outside the repository.
- Strict Draft-Only mode and human approval gates remain active at all times.
- L2 never performs CRM mutations, external sends, production deploys, or silent main merges.

This structure ensures scope control, clear ownership, and safe parallel operation across the dual-Hermes flywheel.