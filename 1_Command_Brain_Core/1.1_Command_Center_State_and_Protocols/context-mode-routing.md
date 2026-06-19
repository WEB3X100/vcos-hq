# Context Mode Routing

Purpose: prevent context rot from raw tool outputs, API responses, logs, and scraping.

## Rule

All raw tool outputs, API responses, web scraping, browser snapshots, and long terminal logs should be routed through Context Mode when available.

## If Context Mode Is Available

Run noisy collection in an isolated subprocess and return only:

- Key facts
- Errors
- IDs
- Links
- Decisions
- Next actions
- Short evidence snippets

## If Context Mode Is Unavailable

Manually compress before adding to the main context:

- Summarize output.
- Keep exact IDs and URLs.
- Drop repeated logs.
- Drop raw HTML/JSON unless explicitly required.
- Save large raw artifacts outside active memory.

## Durable Memory Rule

Never paste raw logs into:

- `1_Command_Brain_Core/1.2_Headquarters_Memory/active-context.md`
- `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/state.md`
- domain README files
- AGENTS.md

Only durable summaries belong there.

