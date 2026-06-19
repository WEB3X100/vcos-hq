# n8n Morning Research Workflow Spec

Purpose: generate a daily research brief and save it to the vault.

## Environment Variables

- `ANTHROPIC_API_KEY`
- `ANTHROPIC_MODEL`
- `BRAVE_API_KEY`
- `RESEARCH_CONTEXT_PATH`
- `BRIEFINGS_DIR`
- `TIMEZONE`

## Nodes

### 1. Schedule Trigger

Recommended schedules:

- Weekdays at 6 AM: `0 6 * * 1-5`
- Every day at 6 AM: `0 6 * * *`

Use the user's local timezone.

### 2. Read Research Context

Read file:

```text
$env.RESEARCH_CONTEXT_PATH
```

Expected output:

```json
{
  "content": "full research context markdown"
}
```

### 3. Build Search Plan

Use a Code node to extract:

- primary focus areas
- competitive landscape names
- trusted source domains
- exclusion terms

Output a compact query list. Keep the first version conservative: 5-10 queries total.

### 4. Brave Search

Call Brave Search API for each query.

Keep:

- title
- URL
- snippet
- published date if available
- query that found it

Discard obvious duplicates before calling Claude.

### 5. Prepare Claude Request

Construct the request body:

```json
{
  "model": "{{$env.ANTHROPIC_MODEL}}",
  "max_tokens": 4096,
  "system": "You are a personal research agent. Today's date is {{date}}. Current time is {{time}}. Use only the supplied research context and search results unless a tool-enabled runtime is explicitly available.",
  "messages": [
    {
      "role": "user",
      "content": "Research context:\n\n{{research_context}}\n\nSearch results:\n\n{{search_results}}\n\nGenerate my morning research brief using the approved morning research agent prompt."
    }
  ]
}
```

Set `ANTHROPIC_MODEL` to the current approved Claude model after checking provider support.

### 6. Claude API Call

HTTP Request:

- URL: `https://api.anthropic.com/v1/messages`
- Method: `POST`
- Headers:
  - `x-api-key: {{$env.ANTHROPIC_API_KEY}}`
  - `anthropic-version: 2023-06-01`
  - `content-type: application/json`
- Body: output from node 5

### 7. Save Brief

Extract:

```javascript
const response = $node["Claude API Call"].json;
const content = response.content[0].text;
const date = new Date().toISOString().split("T")[0];

return {
  filename: `${date}-morning-brief.md`,
  content
};
```

Write to:

```text
{{$env.BRIEFINGS_DIR}}/{{$json.filename}}
```

### 8. Optional Notification

Send only after human approval.

Suggested message:

```text
Morning brief ready: BRIEFINGS/{{date}}-morning-brief.md
```

## Safety Checks

- Do not run the production schedule until a human approves credentials, destination path, and recurring cost.
- Do not send external notifications during test runs.
- Log failed runs without dumping secrets.
- Keep search results compact so the Claude request stays within budget.
- If search fails, write a failure note instead of inventing a brief.
