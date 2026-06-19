# Session Context Discipline

Purpose: prevent Claude/Codex sessions from becoming expensive, confused, and hard to steer.

Use this when a session is long, repetitive, drifting, expensive, or about to switch tasks.

## Core Model

Context is the agent's current working memory:

- system prompt
- conversation history
- tool calls and tool outputs
- files read
- skills, MCP servers, agents, and project instructions

Every new message forces the model to reread the session. Cost compounds. Long sessions also degrade quality: the model gets more likely to forget, contradict itself, over-edit, or act without rereading.

The 1M context window is insurance, not a goal.

## Prime-Time Rule

Best work happens early in a clean session.

VCOS default:

- Treat 0-20 percent context as prime time.
- Avoid pushing past 120K tokens unless the task truly needs it.
- Manual handoff/clear is preferred before context rot.
- Auto-compaction at the edge of the window is a last resort, not a strategy.

## The Five Choices After Each Response

| Choice | Use When | VCOS Rule |
| --- | --- | --- |
| Continue | Same thread, still clean, same goal | Fine for short runs |
| Rewind | The agent went down the wrong path | Prefer over stacking corrections |
| Clear | New task or context feels polluted | Save handoff first if work must continue |
| Compact | Same task, context is large but still coherent | Use explicit keep-instructions |
| Sub-agent / sidecar | Bounded research, scan, summarization, or independent check | Return only distilled findings |

## Rewind Rule

If an attempt is wrong, do not keep arguing with the failed path in context.

Use rewind or restart when:

- a wrong implementation path took several turns
- generated code broke the shape of the solution
- tool output polluted the thread
- repeated correction messages are accumulating

## Clear + Handoff Rule

Before clearing a productive session, ask for a handoff:

```text
Create a session handoff. Include outcome, decisions locked, files changed, commands run, current state, blockers, open questions, and exact next action. Keep it concise enough to paste into a fresh session.
```

Then:

1. Copy/save the handoff.
2. Run `/clear` or start a new session.
3. Paste the handoff.
4. Continue from files and state, not from chat memory.

## Session Handoff Template

```markdown
## Session Handoff

- Outcome:
- Current status:
- Decisions locked:
- Files changed:
- Commands / checks run:
- Important IDs / links:
- Blockers:
- Open questions:
- Approval gates:
- Next action:
- Do not repeat:
```

## State Belongs In Files

Do not use chat history as the database.

Store durable state in:

- ClickUp for execution
- Drive for files
- Airtable/Supabase/Postgres for records
- GitHub for code, diffs, issues, PRs
- VCOS HQ for decisions, rules, capability maps, and reusable protocols

Save decisions, schemas, packets, and prevention rules. Do not save full raw conversations.

## Raw Material Conversion

Before loading large material:

- Convert HTML to Markdown when possible.
- Convert PDFs/DOCX to Markdown when visual layout is not needed.
- Keep originals only when OCR, screenshots, exact formatting, or vision inspection matters.
- Summarize transcripts into decisions, patterns, blockers, and next actions.

## Sub-Agent / Sidecar Rule

Use a fresh sidecar context for:

- reading many files
- summarizing long docs
- scanning noisy logs
- comparing many repos/tools
- independent QA

The sidecar should return only:

- findings
- evidence paths
- decisions/options
- risks
- next actions

Do not copy its raw working context into the main session.

## Startup Hygiene

At the start of important sessions:

- Use fast-path files.
- Check context/cost tools when available.
- Disconnect unused heavy MCP/tool surfaces when possible.
- Start in plan mode for ambiguous or risky work.
- Load only the exact skill/reference required.

## Exit Hygiene

Before ending a meaningful session:

- Record changed decisions.
- Update state only with durable blockers/next actions.
- Move repeatable workflows into the Skill Foundry.
- Create a handoff if work will continue later.

