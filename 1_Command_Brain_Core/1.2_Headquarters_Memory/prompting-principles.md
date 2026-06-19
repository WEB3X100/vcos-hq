# Prompting Principles

Purpose: help Umair ask sharper questions, give cleaner context, save tokens, and get better results from AI teammates.

## Best Prompt Shape

Use this structure when a request matters:

```text
Outcome:
Context:
Source of truth:
Constraints:
Tools allowed:
Approval gate:
Output format:
Definition of done:
```

## Tool-First Prompting

Claude Code works best when the prompt implies concrete actions:

- read specific files
- search specific areas
- inspect specific tasks
- edit a defined surface
- run bounded checks
- summarize a known source
- delegate a bounded investigation when allowed
- verify with screenshots, tests, logs, or API readbacks

Avoid monolithic prompts that ask the agent to "figure everything out" without boundaries.

## The 95 Percent Confidence Rule

For ambiguous or important work, ask the agent:

```text
Ask me focused questions until you are 95 percent confident you understand the outcome, constraints, approval gates, and definition of done. Then propose a plan before executing.
```

Use this for:

- client delivery
- proposals
- automations
- dashboards
- workflows touching customer data
- new agent or skill design
- architecture decisions

Do not use it for tiny commands or obvious edits.

## Better Question Patterns

Weak:

```text
Make this better.
```

Stronger:

```text
Review this as a skeptical operator. Identify the top 5 issues that would block client trust, then propose a tighter version with approval gates preserved.
```

Weak:

```text
Build an automation.
```

Stronger:

```text
Design the workflow broker packet for this automation: inputs, state store, worker, agents, output packet, approval gate, failure modes, and success metric.
```

Weak:

```text
Summarize this transcript.
```

Stronger:

```text
Extract reusable operating patterns from this transcript and map them to VCOS HQ, ClickUp, Airtable, n8n, and AgentOSync delivery. Keep only decisions, patterns, and next actions.
```

## Context Hygiene

- Give links, IDs, file paths, and short summaries first.
- Paste raw material only when the agent must inspect it directly.
- Separate facts from guesses.
- Say what should not change.
- Say whether the output is draft-only, internal, client-facing, or production-sensitive.
- Name the source of truth: ClickUp, Drive, Airtable, GitHub, local repo, or user memory.
- Ask whether the whole source is needed or only the relevant section.
- Prefer editing the original prompt and regenerating over piling on correction messages when possible.
- Ask for bounded command output before running noisy shell commands.
- Clear between unrelated tasks.
- Compact around 60 percent context with explicit keep-instructions.
- If a session feels polluted, ask for a session handoff and clear rather than piling on corrections.
- Use rewind for wrong turns when available; do not keep failed approaches in the active context.
- Convert large documents to Markdown or summarized packets unless exact layout or OCR matters.

## Strategic Prompt Add-Ons

Use these clauses when useful:

- "Challenge my assumptions before giving the answer."
- "Give me the smallest next action that moves this forward."
- "Create a reusable template from this if it is likely to repeat."
- "Preserve existing descriptions and links."
- "Do not send, publish, mutate CRM, or spend money."
- "Return a handoff packet, not a long essay."
- "Focus on blockers, decisions needed, and next actions."
- "Use the business-service-broker pattern."
- "Use the smallest context needed."
- "Tell me what you need before loading more files."
- "Verify before marking done."
- "Summarize what should become durable memory."
- "Create a session handoff I can paste into a fresh session."
- "Use a sidecar/sub-agent for noisy reading and return only distilled findings."

## Output Standards

Ask for:

- concise executive summary for decisions
- task packet for ClickUp
- schema for Airtable
- workflow map for n8n
- prompt template for reuse
- acceptance criteria for demos
- QA rubric for review
- deployment gate for production

## Learning Loop

After useful work, ask:

```text
What did we learn that should become a VCOS rule, skill candidate, ClickUp template, or project decision?
```

If the answer is durable, save it in the correct place. If it is only temporary status, keep it in ClickUp or the active project task.
