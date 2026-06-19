# Dealership AI Command Layer MVP Implementation Pointer

Primary implementation package:

`/Users/umairkhalid/_VCOS_Headquarters/3_Project_Workspaces/3.1_AgentOSync_Revenue_Pipeline/dealership-ai-command-layer-mvp`

## Domain Notes

This implementation upgrades the dealership wedge from missed-call recovery only to an inventory-speed-first MVP:

```text
WhatsApp vehicle intake
-> Hermes parser
-> Airtable Inventory record
-> owner approval
-> demo website card live
-> FB/Kijiji draft only
-> audit log
```

## Approval Boundary

No real client messages, CRM mutations, marketplace posts, website publishes, or customer-facing sends happen without explicit human approval. Demo data is seeded and fake.

