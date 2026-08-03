# AGENTS.md: GTM and tracking diagnostic skills

This repo is a pack of 15 Claude Skills for diagnosing GTM, GA4, Google Ads
conversions, Meta Pixel + CAPI, Consent Mode and deduplication. Each skill is a
self-contained `SKILL.md` under its own folder, following the Agent Skills
standard, so the pack also runs in any other Agent Skills tool.

## How these skills behave

- **Data-first.** Every skill reads what you provide: GTM container exports,
  GA4 reports, Tag Assistant output, event exports, screenshots. If the input
  is missing, the skill says so and marks an assumption instead of guessing.
- **Diagnostic, not mutating.** Skills read and reason. They do not log into
  GTM, GA4 or the ad accounts, and they do not publish container changes.
- **Empty is not broken.** A signal that shows nothing is treated as "nothing
  arrived this way", never as proof the event does not fire. Skills separate
  "I cannot see X with this input" from "X is not happening".
- **Honest about limits.** Thresholds inside skills are labeled heuristics,
  not platform-published rules.

## How the pack composes

- `gtm-container-health-check` is the entry point on an unfamiliar setup. It
  establishes the state of the container and routes to the right deep dive.
- Signal-quality skills (`duplicate-event-finder`,
  `conversion-deduplication-review`, `ga4-event-quality-audit`) come before
  attribution and readiness skills. Interpreting numbers on top of duplicated
  or missing events produces confident, wrong answers.
- `weekly-tracking-signal-readout` is the recurring summary skill; run it last.
- `references/` holds the shared output standard and design principles every
  skill follows. `examples/` holds worked sample outputs for two skills.
  `evals/review-checklist.md` is the internal review bar for pack changes.

## Verticals

Ecommerce setups lean on the data layer and purchase dedup skills; lead gen
setups lean on Google Ads conversion tracking, enhanced conversions readiness
and offline import audits. Consent Mode impact matters most for EU traffic.
