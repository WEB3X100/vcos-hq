# Managed Agent Runtime Evaluation

Purpose: give VCOS a practical decision guide for Claude Managed Agents, Agent SDK + Trigger.dev, OpenClaw/Hermes-style self-hosting, n8n, and local Claude Code.

This file is strategy guidance. Validate implementation details against current official docs before building.

## Core Concepts

Managed agent systems usually separate:

- Agent: model, system prompt, tools, MCP servers, skills, permissions.
- Environment: container, packages, networking, filesystem, runtime.
- Session: one running instance of an agent in an environment.
- Events: messages, tool uses, custom tool requests, confirmations, streaming outputs, interrupts.
- Memory: durable stores or state sources that survive session boundaries.

## VCOS Decision Matrix

| Need | Preferred Pattern |
| --- | --- |
| Operator-driven repo work | Claude Code local |
| API-driven product agent | Managed Agents after docs validation |
| Scheduled/proactive work | Agent SDK + Trigger.dev, n8n, GitHub Actions, cron, or OpenClaw |
| Multi-channel assistant | OpenClaw/Hermes-style runtime |
| Business workflow glue | n8n as worker/router |
| Durable client state | Airtable, Supabase, Postgres, CRM, or ClickUp |
| Reusable expertise | skill.md, prompt template, workflow map, or role template |

## Managed Agent Fit

Good fit:

- product features where users trigger the agent from an app
- one-off async reports
- teams without DevOps capacity
- prototypes before self-hosting
- enterprise environments that need networking controls, vaults, audit trails, and versioning

Poor fit by itself:

- always-on monitoring
- heartbeat behavior
- cron-driven operations
- proactive multi-channel assistants
- workflows that need custom scheduling, retries, and observability without an external orchestrator

## Scheduling Rule

If the agent must wake up by itself, identify the scheduler explicitly:

- Trigger.dev
- n8n
- GitHub Actions
- Linux cron
- OpenClaw/Hermes heartbeat or cron
- app webhook server

Managed execution without scheduling is reactive. It is not a complete proactive agent system.

## Permission Rule

Separate actions into:

- always allow: safe reads, bounded searches, formatting, local non-destructive checks
- ask first: shell commands, external APIs, client data access, webhooks, generated sends
- deny or human-only: destructive actions, production deploys, spend, CRM mutation, external messages, credentials

## Memory Rule

Durable memory should store preferences, conventions, decisions, schemas, and post-mortem learnings.

Do not store raw customer data, secrets, noisy logs, or full message exports in durable agent memory unless the client system and compliance requirements explicitly allow it.

## Versioning Rule

Record a new version when changing:

- system prompt
- model
- tools
- MCP servers
- skills
- memory sources
- permissions
- environment packages
- networking

For client delivery, include version and run/session IDs in the handoff packet.
