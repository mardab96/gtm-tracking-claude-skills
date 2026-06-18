---
name: duplicate-event-finder
description: Finds events counted twice across browser tags, server events, GA4, Meta Pixel/CAPI, Google Ads and ecommerce data layers. Use when reported conversions are too high, inconsistent or fired from multiple sources.
---

# Duplicate Event Finder

Use the shared quality bar in `../references/output-standard.md` and `../references/skill-design-principles.md` when those files are available.

## Use this skill when

- the user suspects double-counting or duplicated conversion events.
- browser, server, GA4, Meta, Google Ads or backend counts disagree.
- the same event fires from multiple tags, containers, plugins or integrations.

Do not use this skill for a generic brainstorming request. Use it when there is a concrete asset, setup, report, page, funnel, tracking issue or decision to diagnose.

## Required input

- GTM container export, tag list, GA4 event list, Google Ads conversion actions, Meta Pixel/CAPI setup or screenshots.
- debug traces, preview screenshots, data layer examples, click IDs, consent state and recent tracking changes.
- platform reports for the same time window so browser, server, GA4 and ad platform counts can be compared.
- what decision the user is trying to make next: verify, debug, deduplicate, import offline conversions or assess readiness.
- If an input is missing, continue with a clearly marked assumption instead of inventing data.

## Analysis workflow

1. List every source that can fire the same event and the trigger condition for each source.
2. Check event names, event_id, transaction_id, order_id, value, currency and timing.
3. Compare browser, server and platform counts for the same time window.
4. Classify likely duplicates as confirmed, probable or unproven.
5. Score confidence as high, medium or low based on data quality, sample size and source reliability.
6. Produce the smallest useful next action, not a broad redesign or system rebuild.

## Decision rules

- If the data does not connect to revenue, pipeline, qualified leads or conversion quality, label the recommendation as a hypothesis.
- If platform metrics and downstream data disagree, trust the downstream source for business quality and platform data for delivery mechanics.
- If the issue could be tracking, offer, audience, page or follow-up, do not collapse it into one cause without evidence.
- Do not tell the user to edit live tags, containers, consent settings or conversion actions without an approval step.

## Output format

| Finding | Evidence | Why it matters | Recommended action | Confidence |
|---|---|---|---|---|
| Short diagnostic claim | Data, quote, screenshot, export or missing-data note | Business impact or risk | Specific next step and owner | High / Medium / Low |

End with:

- `Decision:` fix / test / monitor / ask for data / do not act yet
- `Approval needed:` yes/no and what would change if approved
- `Missing data:` only the inputs that would materially change the recommendation

## Practical example

User: "Can you check this duplicate event finder before we make a change?"

Assistant should: ask for or use the relevant exports/screenshots/notes, run the workflow above, produce a ranked diagnostic table, and stop at approval-ready recommendations.

## Guardrails

- Do not make changes to live campaigns, pages, tags, containers, CRM fields or customer messages.
- Do not claim performance impact without evidence.
- Mark missing data clearly.
- Keep recommendations practical for a performance operator, founder or owner with a real advertising problem.
