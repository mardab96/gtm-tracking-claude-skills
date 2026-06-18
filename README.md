# 15 Claude Skills for Google Tag Manager and Tracking

A pack of 15 production-ready Claude Skills for GTM, GA4, Google Ads, Meta Pixel+CAPI, consent, click IDs, duplicate events and CRM offline conversions.

Each skill is a self-contained `SKILL.md` with explicit triggers, required inputs, analysis workflow, decision rules, a practical example, output format, and guardrails. Drop them into Claude Code and they activate automatically when their use case matches the conversation.

## What is inside

| # | Skill | Folder | Purpose |
|---|---|---|---|
| 1 | Gtm Container Health Check | `gtm-container-health-check` | Reviews container structure, naming, versions and obvious errors. |
| 2 | Ga4 Event Quality Audit | `ga4-event-quality-audit` | Checks event naming, parameters, key events and reporting logic. |
| 3 | Google Ads Conversion Tracking Audit | `google-ads-conversion-tracking-audit` | Verifies conversion actions, values, attribution and primary/secondary setup. |
| 4 | Meta Pixel Capi Signal Quality Audit | `meta-pixel-capi-signal-quality-audit` | Reviews Pixel, Conversions API, event quality scores and deduplication. |
| 5 | Consent Mode Impact Review | `consent-mode-impact-review` | Evaluates consent setup and estimates signal loss impact. |
| 6 | Click Id And Utm Sanitization Check | `click-id-and-utm-sanitization-check` | Checks gclid, fbclid, UTM handling across pages and redirects. |
| 7 | Duplicate Event Finder | `duplicate-event-finder` | Finds events counted twice or fired from multiple sources. |
| 8 | Conversion Deduplication Review | `conversion-deduplication-review` | Verifies deduplication logic for Google Ads and Meta. |
| 9 | Offline Conversion Import Audit | `offline-conversion-import-audit` | Reviews CRM offline import setup and match quality. |
| 10 | Enhanced Conversions Readiness Check | `enhanced-conversions-readiness-check` | Checks if Enhanced Conversions for Web or Leads are set up correctly. |
| 11 | Server Side Tagging Feasibility Review | `server-side-tagging-feasibility-review` | Evaluates whether sGTM is worth it and what needs to move first. |
| 12 | Attribution Window Sanity Check | `attribution-window-sanity-check` | Checks if attribution settings match your sales cycle and reporting needs. |
| 13 | Ecommerce Data Layer Audit | `ecommerce-data-layer-audit` | Reviews purchase, item and checkout data layer quality. |
| 14 | Ios Privacy Signal Loss Review | `ios-privacy-signal-loss-review` | Diagnoses impact of privacy changes on signal quality. |
| 15 | Weekly Tracking Signal Readout | `weekly-tracking-signal-readout` | Produces a weekly tracking summary with confidence score and next actions. |

## How to install

### Option A — Claude Code (recommended)

1. Clone or download this repository.
2. Copy the skill folders into your project's `.claude/skills/` directory, or into the user-level skills directory at `~/.claude/skills/`.
3. Start a new Claude Code session in that project. Skills will activate automatically when their description matches the conversation.

```bash
git clone https://github.com/mardab96/gtm-tracking-claude-skills.git
cp -r gtm-tracking-claude-skills/* ~/.claude/skills/
```

### Option B — Other Claude environments

The skills are plain Markdown with YAML frontmatter and work anywhere Claude can read files. Paste the relevant `SKILL.md` content into context when you want to use it.

## How to use

Once installed, describe what you want in natural language. Skills self-trigger on the patterns documented in their `## Use this skill when` section.

## Activation and trigger reliability

Claude Skills usually activate from the YAML `description` field first, then use the full `SKILL.md` instructions after activation. Each skill in this pack now names the moment it should be used in both places:

- `description` explains the tracking situation that should trigger the skill.
- `## Use this skill when` lists concrete request patterns and decision moments.
- `## Required input` tells the user what exports, screenshots, traces and reports make the skill reliable.

For best results, ask for the job and include the tracking object being diagnosed. Example: "Audit Google Ads conversion tracking before we scale" will trigger `google-ads-conversion-tracking-audit` more reliably than "Check tracking."

## Bring your data

Every skill is data-first. They work best when you provide actual exports, reports, screenshots or notes. Each `SKILL.md` documents exactly which inputs it expects under `## Required input`.

## Guardrails

These skills are designed for diagnosis and approval-ready recommendations. By default they do not:

- publish ads
- change budgets
- pause campaigns
- edit tracking setup
- change optimization events
- modify landing pages
- modify CRM fields
- send customer messages
- make performance claims without data

Use them to structure the work, not to hand over control of the account.

## Validate the pack

Run the validator before publishing changes:

```bash
python3 scripts/validate-skills.py
```

It checks for placeholder text, missing required sections, weak activation descriptions and workflows that are too short to be useful.

## Examples and review

Use the sample outputs to judge the expected depth of analysis:

- [`examples/google-ads-conversion-tracking-audit-sample.md`](examples/google-ads-conversion-tracking-audit-sample.md)
- [`examples/duplicate-event-finder-sample.md`](examples/duplicate-event-finder-sample.md)

Use [`evals/review-checklist.md`](evals/review-checklist.md) for the next manual review pass.

## License and attribution

Free to use, modify, and redistribute for personal and commercial work. If you ship something built on top of these skills, a credit is appreciated but not required.

Built and maintained by [AdLume](https://adlume.co) — performance marketing infrastructure for AI-native operators.
