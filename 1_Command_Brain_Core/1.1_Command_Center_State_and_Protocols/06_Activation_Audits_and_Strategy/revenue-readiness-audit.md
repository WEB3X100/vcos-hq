# Revenue Readiness Audit

Purpose: prevent VCOS from improving the map while the revenue loop is not moving.

Use this before adding new Arsenal tools, new operating docs, new routines, or new lanes.

## Current Honest Read

Known from HQ context:

- AgentOSync GTM is the public proof engine.
- Barbershop live demo exists and produced useful pricing feedback, but is now parked as a proof/demo asset rather than the primary closing lane.
- Amax / Travel OS is the internal proof lab with real sales-team usage and feedback.
- Dealership OS is the primary execution lane when the engagement is real/paid or closest to paid proof.
- Content intel to content drafting is the first Claude Code routine candidate because it solves a real pain and can create daily proof/content.
- Trading Coach is coach-only and must not become a signal service, broker integration, or execution bot.
- Top-level `CLAUDE.md` exists.
- AgentOSync workspace `CLAUDE.md` exists.
- Current routine order is content intel first, then `sprint-closer`, then `skeptic-review`. `morning-cockpit` is deferred until one focused lane needs a daily brief.
- Content intel does not become useful until Umair writes the voice calibration files: 10 approved posts, 5 rejected/never-say examples, and 3-5 tone rules.

Unknown or not proven in durable HQ context:

- Whether dealership OS is paid engagement or spec work.
- Whether barbershop pricing failure was pricing, packaging, buyer fit, or market fit.
- Whether Claude Code is being used as the daily driver or only planned as the daily driver.
- Whether Amax feedback is structured enough to become a public/anonymized proof asset.
- The exact paid pilot sentence: price, deliverable, duration, and buyer.
- The main variance risk that would destroy trust first, especially dealership Facebook Marketplace automation, voice demo edge cases, CRM data drift, and proof-claim accuracy.
- Whether AgentOSync is currently selling an AI-native service company motion, an AI product motion, or a hybrid with explicit boundaries.
- Whether the content-intel routine has completed 5 manual runs with feedback before n8n automation.

Updated by Umair on 2026-06-11:

- Dealership OS is real-client MVP work, not speculative spec work. It owns the sprint unless a sharper paid/proof blocker appears.
- AMAX focus is QuickBooks cleanup using the upgraded COA / finance OS workbook feedback, with a CFO meeting on 2026-06-12.
- Content-intel voice samples will be provided by Umair; voice calibration files should be built from those samples before automation.

## Ten Questions

Answer these directly before expanding infrastructure.

1. What shipped in the last 30 days?
   - Shipped means running and producing output or response: DM, demo call, pilot, dollar, daily user feedback, or live artifact.
   - Current answer from latest context: barbershop demo built/demoed, dealership scraper and Airtable schema active, Amax sales team using the solution and giving feedback, LinkedIn auto-posting/school/community/content work active. Need exact shipped artifacts and external responses recorded.

2. Where does the day actually break down?
   - A: know what to do but cannot start.
   - B: start but burn context and lose the thread.
   - C: finish builds but they do not get reviewed/approved.
   - D: approved work does not get posted/shipped.
   - E: work ships but no one responds.

3. Is Claude Code the daily driver today?
   - If no, the first action is daily-driver setup and one validated routine, not more routine design.

4. What is the single most painful repeated session task?
   - Pick one concrete friction, not a category like "context management."
   - Current answer: monitoring AI/SME updates across X/Instagram/GitHub/news, synthesizing what matters, and drafting posts in Umair's voice.

5. Are AgentOSync, Amax, Dealership, and Trading running in parallel or are they a future-state map?
   - If available operator time is limited, AgentOSync barbershop proof should get the majority of execution time.
   - Current answer: multiple real lanes are active. This creates a focus allocation problem; do not treat them equally.

6. What does Amax as internal proof lab mean today?
   - Real user and real feedback, or theoretical test bed?
   - Current answer: sales team is using the solution and giving feedback. Need one structured before/after proof asset.

7. What is the paid pilot in one sentence?
   - Include buyer, deliverable, price, duration, and approval boundary.

8. Where is the highest variance risk?
   - Examples: voice demo edge cases, ClickUp formatting, image/video hallucination, CRM field drift, follow-up copy quality, reporting accuracy.

9. What is the current state of `CLAUDE.md` files?
   - Current HQ answer: top-level and AgentOSync exist. Other lane-specific files should only be added after a routing failure or active sprint need.

10. Is AgentOSync primarily an AI-native services company or an AI product company?
   - Default recommendation: services-first. Sell outcomes and pilots first; productize only after repeated delivery patterns.

## Default Answers Until Umair Updates Them

- Bottleneck assumption: focus allocation across too many real lanes, plus content-intel monitoring burden.
- Lane priority: Dealership OS first as confirmed real-client MVP work; Amax QuickBooks/CFO proof second; SME intel/content routine third after voice samples; AgentOSync short-form content fourth; barbershop demo parked as proof asset; Trading Coach protected as personal improvement.
- Company model: services-first with productized internal assets. Do not sell the platform before a paid workflow is proven.
- Paid pilot placeholder: not final. Do not present pricing or terms externally until Umair confirms the one-sentence offer.

## Decision Rule

If the answer to "what shipped in the last 30 days?" is unclear, the next task is not architecture. The next task is to ship one narrow artifact:

- one dealership OS client/proof milestone,
- one Amax before/after proof paragraph,
- one approved barbershop demo screen capture labeled as demo,
- one approved content-intel draft batch,
- one callable demo test with review notes,
- one Amax daily control brief from real data,
- or one clean session handoff posted after approval.

## Morning Use

Before running `morning-cockpit`, check:

1. Has a live artifact shipped since the last brief?
2. Did it produce a response?
3. If not, what single action ships today?
4. What approval is blocking shipment?
5. Which tool is actually needed to remove that blocker?

If no tool is needed, do not activate a new tool.

## Content Intel Reality Check

Do not automate the content-intel routine until:

1. Umair fills `voice-calibration/approved-posts.md` with 10 real approved posts or drafts.
2. Umair fills `voice-calibration/rejected-patterns.md` with 5 "never say this" examples or rejected drafts.
3. Umair fills `voice-calibration/tone-rules.md` with 3-5 rules in his own words.
4. The routine has run manually 5 times.
5. Approved/rejected feedback is logged after each run.

Until then, the first deliverable is the voice calibration file, not an n8n workflow.
