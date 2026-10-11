---
name: conversion-deduplication-review
description: Verifies deduplication logic for Google Ads and Meta. Use when GTM, GA4, Google Ads, Meta, consent, click ID or CRM import data must be checked before trusting reporting or changing bidding.
---

# Conversion Deduplication Review

Use the shared quality bar in `../references/output-standard.md` and `../references/skill-design-principles.md` when those files are available.

## Use this skill when

- the user shares GTM, GA4, Google Ads, Meta Pixel/CAPI, consent, click ID, data layer or CRM import evidence tied to conversion deduplication review.
- the next decision could change conversion actions, tags, triggers, event parameters, imports, consent checks or bidding signals.
- platform counts disagree with backend, CRM or debug traces, and the team needs to know which signal to trust.

Do not use this skill for broad analytics theory. Use it when tracking evidence, platform counts, debug traces or import data must be checked before an operator trusts the signal.

## Required input

- GTM container export, tag list, GA4 event list, Google Ads conversion actions, Meta Pixel/CAPI setup or screenshots.
- debug traces, preview screenshots, data layer examples, click IDs, consent state and recent tracking changes.
- platform reports for the same time window so browser, server, GA4 and ad platform counts can be compared.
- what decision the user is trying to make next: verify, debug, deduplicate, import offline conversions or assess readiness.
- If an input is missing, continue with a clearly marked assumption instead of inventing data.

## Analysis workflow

1. Identify each platform, conversion action or destination, and sending path. Check its current documented duplicate-suppression fields, scope and timing window; do not assume event_id, transaction_id or order_id are interchangeable. Distinguish click IDs used for attribution matching from identifiers for the business event: one click may lead to several valid conversions.
2. For browser/server pairs, retries and parallel integrations, trace the same business event through the provider's actual deduplication contract. Verify required identifiers and event/action context are stable across retries and paired paths, while distinct purchases or lead stages remain distinct. Sharing an ID alone does not prove deduplication across different actions or destinations.
3. Compare deduplication diagnostics, duplicate warnings and event count differences.
4. Flag mismatched IDs, regenerated IDs, delayed server events and parallel integrations.
5. Recommend deduplication fixes only after a reproducible debug trace.

For example, Google's [offline conversion guide](https://developers.google.com/google-ads/api/docs/conversions/upload-offline) separates click matching identifiers from the optional order_id/transaction ID. Consult the current guide for the specific ingestion mechanism rather than copying one platform's key or window to another. If documentation or diagnostics are unavailable, mark duplicate suppression as unverified.

## Decision rules

- If the data does not connect to revenue, pipeline, qualified leads or conversion quality, label the recommendation as a hypothesis.
- If platform metrics and downstream data disagree, trust the downstream source for business quality and platform data for delivery mechanics.
- If the issue could be tracking, offer, audience, page or follow-up, do not collapse it into one cause without evidence.
- Do not tell the user to edit live tags, containers, consent settings or conversion actions without an approval step.

## Output format

| Finding | Tracking evidence | Signal risk | Recommended fix or check | Confidence |
|---|---|---|---|---|
| Specific diagnostic claim | Data, screenshot, report, note or missing-data marker | Business or signal consequence | Smallest useful next step and owner | High / Medium / Low |

End with:

- `Decision:` fix / test / monitor / ask for data / do not act yet
- `Approval needed:` yes/no and what would change if approved
- `Missing data:` only the inputs that would materially change the recommendation

## Practical example

User: "Here are GTM screenshots, platform counts and debug traces for conversion deduplication review. Is this signal safe to trust?"

Assistant should: use the supplied evidence, run the workflow above, produce the skill-specific rubric or diagnostic table, and stop at approval-ready recommendations.

## Guardrails

- Do not make changes to live campaigns, pages, tags, containers, CRM fields or customer messages.
- Do not claim performance impact without evidence.
- Mark missing data clearly.
- Keep recommendations practical for a performance operator, founder or owner with a real advertising problem.
