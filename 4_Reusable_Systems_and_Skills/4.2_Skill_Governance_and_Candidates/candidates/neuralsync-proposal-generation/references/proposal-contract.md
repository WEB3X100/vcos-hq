# Proposal Contract and Chrome Auto Test

## Minimum sections

1. title and confidentiality state;
2. executive context;
3. current-state diagnosis;
4. proposed outcome;
5. in-scope deliverables;
6. delivery plan and milestones;
7. roles and dependencies;
8. investment and payment terms;
9. assumptions and exclusions;
10. proof with source labels;
11. next step and approval route.

## Test case A — Chrome Auto

- Context source: Chrome Auto × NeuralSync document in the Drive manifest.
- Pricing source: Proposal Pricing sheet in the Drive manifest.
- Expected test: produce a source ledger and identify every unresolved scope, price, proof, and approval field before rendering.
- Pass for static preflight: no unsupported value is silently introduced.
- Pass for production: PDF opens, every page is visually inspected, totals reconcile, and a human approves the client-facing version.
