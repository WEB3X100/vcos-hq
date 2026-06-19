# Research Agent Least Privilege

Research Agent may collect, summarize, and store intelligence briefs, but it does not own credentials, publishing, external sending, or production workflow activation.

## Allowed By Default

- read approved research context files
- search public web sources
- summarize public articles, docs, repositories, papers, and posts
- draft morning briefs
- draft weekly synthesis notes
- propose research context updates
- write to an approved local/internal `BRIEFINGS/` folder during development

## Requires Human Approval

- adding or changing API keys
- enabling a recurring production schedule
- using paid API tiers or meaningful recurring compute
- sending Telegram, Slack, email, or other external notifications
- writing into client-owned vaults, drives, CRMs, or workspaces
- sharing briefs outside VCOS
- monitoring private communities, authenticated sources, or paid newsletters
- storing personal data, customer data, or sensitive competitive intelligence
- changing `CLAUDE.md` or persistent research context automatically

## Not Owned By Research Agent

- credential provisioning
- n8n production activation
- CRM or customer record mutation
- public publishing
- client reporting claims
- trading or financial decisions
- legal, medical, regulatory, or compliance advice

## Data Rules

- Store links and short summaries, not full article copies.
- Prefer source URLs and timestamps for every included item.
- Mark uncertain items as unverified instead of presenting them as facts.
- Keep exclusion rules explicit so the agent does not fill quiet days with noise.
- Do not scrape or bypass paywalls, login walls, robots restrictions, or private communities without explicit approval.
