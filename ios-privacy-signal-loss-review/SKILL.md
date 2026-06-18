---
name: ios-privacy-signal-loss-review
description: Diagnoses impact of privacy changes on signal quality. Use when the user is diagnosing, planning, reviewing or deciding next actions for ios privacy signal loss review in GTM, GA4 and paid ads tracking.
---

# IOS Privacy Signal Loss Review

Use the shared quality bar in `../references/output-standard.md` and `../references/skill-design-principles.md` when those files are available.

## Use this skill when

- the user asks for help with ios privacy signal loss review in GTM, GA4 and paid ads tracking.
- the user provides data, screenshots, exports, notes or a URL related to ios privacy signal loss review.
- the user needs an approval-ready diagnosis before changing campaigns, pages, tracking, CRM or follow-up.

Do not use this skill for a generic brainstorming request. Use it when there is a concrete asset, setup, report, page, funnel, tracking issue or decision to diagnose.

## Required input

- GTM container export, tag list, GA4 event list, Google Ads conversion actions, Meta Pixel/CAPI setup or screenshots.
- debug traces, preview screenshots, data layer examples, click IDs, consent state and recent tracking changes.
- platform reports for the same time window so browser, server, GA4 and ad platform counts can be compared.
- what decision the user is trying to make next: verify, debug, deduplicate, import offline conversions or assess readiness.
- If an input is missing, continue with a clearly marked assumption instead of inventing data.

## Analysis workflow

1. Restate the specific decision the user is trying to make about ios privacy signal loss review.
2. Inventory the evidence provided and mark missing inputs before judging performance.
3. Compare surface metrics against downstream business quality for GTM, GA4 and paid ads tracking.
4. Separate facts, likely causes, hypotheses and approval-required actions.
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

User: "Can you check this ios privacy signal loss review before we make a change?"

Assistant should: ask for or use the relevant exports/screenshots/notes, run the workflow above, produce a ranked diagnostic table, and stop at approval-ready recommendations.

## Guardrails

- Do not make changes to live campaigns, pages, tags, containers, CRM fields or customer messages.
- Do not claim performance impact without evidence.
- Mark missing data clearly.
- Keep recommendations practical for a performance operator, founder or owner with a real advertising problem.
