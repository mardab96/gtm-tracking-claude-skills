# Example output: Google Ads Conversion Tracking Audit

Sample data is fictional. Use this as a shape reference for the expected output, not as a benchmark.

## Input summary

Inputs reviewed:

- Google Ads conversion action export
- GA4 key event list
- GTM container screenshots
- CRM offline conversion import history
- Thank-you page URL and form submit trigger notes

Account setup:

- Demo form submit: Primary
- Imported SQL: Primary
- Imported closed-won: Secondary
- Enhanced Conversions: inactive on main web conversion
- Default value: $1 for demo form submit

## Findings

| Finding | Evidence | Bidding impact | Recommended action | Confidence |
|---|---|---|---|---|
| Two funnel stages are marked Primary. | Demo form submit and imported SQL are both Primary. | Google may optimize toward mixed intent signals. | Keep only the chosen bidding event as Primary. Set the other action to Secondary. | High |
| Demo value is static. | Every demo form submit imports with $1 value. | Value-based bidding cannot tell strong and weak leads apart. | Use weighted values by qualified stage or keep the action count-only. | Medium |
| Enhanced Conversions are inactive. | Main web conversion shows no Enhanced Conversions status. | Match quality may be lower than it needs to be. | Check whether hashed email or phone can be sent safely from the form. | Medium |
| Offline import lag is too long. | Median SQL import delay is 9 days. | Smart Bidding receives quality feedback late. | Shorten import cadence or start with web conversion as Primary until import reliability improves. | High |
| GA4 key event and Google Ads conversion use different definitions. | GA4 counts `generate_lead`; Google Ads counts thank-you page view. | Reports may disagree even when tracking is working. | Pick one source of truth for optimization and document the difference. | Medium |

## Decision

Fix conversion action structure before increasing spend.

Recommended interim setup:

- Primary: demo form submit
- Secondary: imported SQL and closed-won
- After 30 days of reliable imports: consider moving imported SQL to Primary

Do not move imported SQL to Primary until import lag and match rate are stable.

## Approval needed

- Confirm the bidding event for the next 30 days.
- Approve Primary / Secondary changes in Google Ads.
- Confirm whether customer email or phone can be used for Enhanced Conversions.

## Missing data

- Conversion action status screenshot
- Enhanced Conversions diagnostics
- Offline import match rate by week
- SQL value distribution from CRM
