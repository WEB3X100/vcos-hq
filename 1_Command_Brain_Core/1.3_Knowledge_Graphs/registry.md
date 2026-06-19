# Knowledge Graph Registry

Purpose: track Graphify graphs that agents may query before reading many files.

| Graph | Source scope | Source path | Graph path | Obsidian import | Status | Owner | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| VCOS HQ Core | Command brain and curated project/domain interfaces | `/Users/umairkhalid/_VCOS_Headquarters` with `.graphifyignore` | Pending | Pending | planned | Sentinel / Infrastructure | Build only after confirming root scope; do not include legacy archive, Arsenal repos, node_modules, or generated imports. |
| AgentOSync Revenue Pipeline | Active AgentOSync project workspace | `/Users/umairkhalid/_VCOS_Headquarters/3_Project_Workspaces/3.1_AgentOSync_Revenue_Pipeline` | `/Users/umairkhalid/_VCOS_Headquarters/3_Project_Workspaces/3.1_AgentOSync_Revenue_Pipeline/graphify-out/graph.json` | `/Users/umairkhalid/_VCOS_Headquarters/1_Command_Brain_Core/1.3_Knowledge_Graphs/imports/agentosync/` | seed active; semantic blocked | Sales / Ops | Seed graph powers the first Daily Command Brief. Official Graphify semantic extraction is blocked until an LLM backend key is configured. |
| AI Native Company Arsenal | Curated Arsenal relationship capsule for cloned AI-native company tools | `/Users/umairkhalid/_VCOS_Headquarters/6_Arsenal/arsenal-index.md` + activation capsule | `/Users/umairkhalid/_VCOS_Headquarters/6_Arsenal/graphify-out/ai-native-company-arsenal-seed.json` | `/Users/umairkhalid/_VCOS_Headquarters/1_Command_Brain_Core/1.3_Knowledge_Graphs/imports/arsenal-ai-native-company/` | seed active | Sentinel / Infrastructure | Use before choosing QMD, Caveman, CodeBurn, Impeccable, Design Extract, Career Ops, Browser Harness, GBrain, Graphify, GStack/GSD, ToolJet, or AIS-OS for a workflow. Do not import vendor repos wholesale. |
| Dealership Employee 01 | Dealership domain + Sameer/Uzair project workspace | `2_Domain_Packs/2.1_Dealerships_Domain_Pack` + `3_Project_Workspaces/3.6_Sameer_Uzair_Dealership_Operating_System` | Pending | Pending | planned | Sales / Ops / Reviewer QA | Use for missed-call recovery, test-drive booking, CRM-safe handoff, and pilot packaging. |
| Skill Foundry | Reusable skills, candidates, employee template | `/Users/umairkhalid/_VCOS_Headquarters/4_Reusable_Systems_and_Skills` | Pending | Pending | planned | Infrastructure / Marketplace | Use for repeatable AI employee capabilities and skill promotion. |

## Query Rule

Before reading many files in a registered scope, query the graph first:

```bash
graphify query "question here" --graph path/to/graphify-out/graph.json --budget 1500
```

If the graph is stale or missing, read only the smallest interface file and decide whether a graph rebuild is worth the cost.
