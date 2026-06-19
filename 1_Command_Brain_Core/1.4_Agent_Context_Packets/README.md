# Agent Context Packets

Purpose: store curated Markdown packets that can be added to Claude Projects, Claude Code sessions, Hermes profiles, or other agent runtimes without forcing the agent to scan all of VCOS HQ.

This folder is for packaged context, not raw memory. Each packet should be short, current, and opinionated about what to read first.

## Packet Rules

1. Start from the VCOS fast path.
2. Prefer links to canonical files over copied content.
3. Include the task trigger, source files, output format, and approval gates.
4. Keep raw logs, chat dumps, exports, screenshots, and old project files out of packets.
5. Refresh packets after weekly office hours when priorities change.

## Current Packet Areas

| Area | Use |
| --- | --- |
| `claude-project/` | Markdown files and prompts to add to Claude Projects or run through Claude Code. |

## When To Add A Packet

Add a packet when an agent repeatedly needs the same context and keeps making the same context mistake.

Examples:

- weekly review context
- Claude Code automation prompts
- project-specific brief for a focused Claude Project
- skill harvest packet
- revenue sprint packet

