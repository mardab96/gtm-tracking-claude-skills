# Review checklist

Use this checklist when reviewing the pack after changes.

## What this review checks

- Skill activation is clear from the YAML `description`.
- `## Use this skill when` names the right tracking decision moment.
- `## Required input` asks for exports, screenshots, traces and reports.
- `## Analysis workflow` has skill-specific tracking steps.
- `## Output format` produces a decision-ready artifact.
- Examples show the expected depth of output.

## Core skills covered by examples

- `google-ads-conversion-tracking-audit`
- `duplicate-event-finder`

## Pass criteria

- A reviewer can tell when each skill should activate without reading the whole repository.
- The skill separates confirmed tracking issues from probable issues.
- The workflow names the exact fields or traces to inspect, such as `event_id`, click IDs, conversion action status and import lag.
- The output ends with decision, approval needed and missing data.
- No placeholder language remains in any `SKILL.md`.

## Validator

Run this from the repository root:

```bash
python3 scripts/validate-skills.py
```

Expected result:

```text
OK: all skills passed validation
```

## Manual review questions

- Would this skill activate when an operator is about to trust or change tracking data?
- Does the output separate platform counts from backend truth?
- Does the skill name concrete GTM, GA4, Google Ads, Meta and CRM evidence?
- Does the skill avoid editing tracking setup without approval?
