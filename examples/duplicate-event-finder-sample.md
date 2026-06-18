# Example output: Duplicate Event Finder

Sample data is fictional. Use this as a shape reference for the expected output, not as a benchmark.

## Input summary

Event under review:

- `lead_submit`
- Destination: GA4, Google Ads, Meta Pixel, Meta CAPI
- Sources: GTM web container, form plugin native integration, server endpoint

Observed 7-day counts:

| Source | Count |
|---|---:|
| Backend confirmed leads | 297 |
| GA4 `lead_submit` | 310 |
| Google Ads conversions | 304 |
| Meta Pixel Lead | 548 |
| Meta CAPI Lead | 289 |

## Findings

| Finding | Evidence | Duplicate risk | Recommended action | Confidence |
|---|---|---|---|---|
| Meta browser Lead fires from 2 sources. | GTM Preview shows a GTM Meta tag and the form plugin native Pixel firing on the same submit. | Confirmed duplicate. | Disable one browser-side Meta Lead source. Keep the GTM tag if it carries cleaner parameters. | High |
| Meta CAPI has `event_id`, browser Pixel does not. | Server event includes `event_id`. Browser event has no matching ID in Pixel Helper. | Deduplication cannot work reliably. | Generate the same `event_id` on submit and send it to both browser and server events. | High |
| GA4 count is close to backend count. | GA4 shows 310 vs 297 backend leads. Difference is 4.4%. | Low duplicate risk. | Keep GA4 as the temporary reference while Meta is fixed. | Medium |
| Google Ads count is close to GA4, but source definition needs checking. | Google Ads has 304 conversions. Trigger appears to be thank-you page view, not form submit. | Possible duplicate or refresh risk. | Check whether thank-you page refresh or direct access can fire the conversion. | Medium |

## Timeline check

| Step | Expected | Observed | Status |
|---|---|---|---|
| Form submit | 1 `lead_submit` event | 1 GA4 event, 1 Google Ads event, 2 Meta browser events, 1 Meta CAPI event | Meta duplicate confirmed |
| `event_id` creation | Same ID in browser and server | Server ID only | Deduplication broken |
| Thank-you page load | 1 conversion only after valid submit | Conversion can fire on direct page load | Needs trigger guard |

## Decision

Fix Meta duplicate firing before using Meta Lead volume for budget or bidding decisions.

Use backend leads and GA4 as the temporary reference. Treat Meta Lead volume as inflated until the duplicate source and `event_id` mismatch are fixed.

## Approval needed

- Confirm whether the form plugin native Pixel can be disabled.
- Approve one `event_id` generation method for browser and server events.
- Confirm whether Google Ads conversion should move from thank-you page view to form-submit event.

## Missing data

- Pixel Helper trace with event parameters
- Server event payload sample
- GTM trigger configuration screenshots
- Thank-you page access rules
