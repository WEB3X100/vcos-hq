# Tool decisions and integrations

## Principle

Tools follow an approved workflow. Do not give an agent a broad arsenal and ask it to invent a use.

## Least-privilege rule

For each goal, record:

- capability needed;
- minimum repo/folder/tool access;
- data read and data written;
- authentication owner;
- cost and lock-in;
- human approval point;
- rollback/export path.

## Current email stack

Apollo, Instantly, and Airtable have been mentioned as an existing stack. Their current configuration, access, deliverability, data provenance, compliance, cost, and performance are **not verified**.

Before build-vs-buy:

1. inventory accounts, domains, inboxes, lists, automations, and owners;
2. inspect deliverability and suppression controls;
3. verify list sources and jurisdictions;
4. calculate full cost and data portability;
5. compare all-in-one, composed stack, and owned build;
6. make a decision record; do not install or migrate during the audit.

## Repository access

Nova gets the marketing intern workspace and task-specific references. Development, infrastructure, finance, and client repos remain out of scope unless a named task requires read access.

## Integration gates

GitHub/Drive: read-only first. Airtable/CRM: no writes. Email platforms: no send permission. Public/social tools: no publish permission. Any expansion requires an approval record.
