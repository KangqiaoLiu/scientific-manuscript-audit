# Claim-to-Endpoint Audit

## Synthetic manuscript excerpt

> We predict which of two coupled cells enters thermal runaway first. For each cell, we compute the maximum local runaway indicator reached during the simulated interval and assign first runaway to the larger maximum. In one representative trajectory, cell A crosses the nominal threshold at 0.42 s. Cell B remains below threshold until 0.61 s and reaches a larger maximum at 0.67 s. The maximum-based rule assigns first runaway to cell B.

## Example major comment

**Severity:** Major-blocking  
**Claim tested:** The method identifies the first-runaway cell.  
**Evidence inspected:** The definition based on separate full-interval maxima and the representative threshold-crossing times.  
**Finding:** The reported proxy orders eventual maxima, while the scientific endpoint is the earliest threshold event. The example supplied by the manuscript already reverses those orderings.  
**Why it matters:** The phase diagram can label the wrong cell even when the simulated histories are accepted as given.  
**Bounded resolution:** Recompute the primary result with first-passage times or a cell-resolved competing-risk integral. Retain maximum asymmetry as a secondary observable and report where the two orderings differ.  
**Recommendation impact:** The first-runaway claim remains unsupported until the endpoint is computed directly.  
**Evidence status:** Checked directly from the synthetic excerpt.
