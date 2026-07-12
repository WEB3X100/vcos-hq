# VCOS Dual-Laptop Architecture Overview

**Mission Reference**: VCOS-STAB-03  
**Date**: 2026-07-11  
**Status**: Candidate Documentation

## Laptop Boundaries

### Laptop 1 (Mac Sentinel)
- **Role**: Chief of Staff (CoS)
- **Authority**: Exclusive merge rights over `main`
- **Responsibilities**:
  - Performs SHA-256 verification on incoming branches
  - Acts as the secure operational cockpit
  - Final review and merge authority
  - Maintains the canonical source of truth

### Laptop 2 (Windows Builder / NeuralSync Intern Builder)
- **Role**: Bounded mission executor
- **Authority**: Feature branch work only
- **Responsibilities**:
  - Executes bounded missions inside isolated Git worktrees
  - Runs automated tests and validation
  - Pushes feature branches for L1 review
  - Never pushes directly to `main`

## Git Transport & Coordination
- All coordination occurs via GitHub feature branches
- L2 creates branches prefixed with `feature/` or `l2/`
- L1 reviews, verifies, and merges
- No direct `main` push rights for L2

## Security & Clean Tree Policy
- No credentials, tokens, or private environment variables (`.env`, `~/.hermes/`, etc.) may be staged or committed
- Protected untracked directories (`.hermes/`, `cofounder-handoffs/`) must remain untouched during missions

## Current Mission Status
This document was created as part of the initial dual-laptop flywheel stabilization (VCOS-STAB-03).