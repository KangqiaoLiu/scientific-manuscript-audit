# Synthetic Case Design

## Purpose

The evaluation suite tests whether a manuscript-audit agent can recover decision-relevant defects, calibrate severity, preserve valid sub-results, and propose bounded resolutions. It contains compact atomic cases and longer composite cases.

## Construction protocol

Each case is built from a defect ledger before prose is written. The ledger records:

- advertised claim
- burden of proof
- evidence that supports the claim
- evidence that defeats or limits the claim
- root defect
- expected severity and recoverability
- acceptable bounded resolutions
- recommendation impact
- harmless or lower-priority decoys

The manuscript text is then written so that evidence is distributed across sections and the correct judgment requires linking claims, methods, results, positioning, and conclusion.

## Composite-case quality gates

A composite case is accepted only when it satisfies all of these gates:

1. **Determinable ground truth.** Every expected defect follows from the supplied text or a stated mathematical relation.
2. **Multiple interacting defects.** The case contains at least two independent decision-relevant defects and at least one valid sub-result or harmless decoy.
3. **Evidence dispersion.** The claim and the evidence that limits it appear in different parts of the case.
4. **Recoverability.** The reference ledger distinguishes removal of a claim, bounded revision, new evidence, and a substantially different paper.
5. **Admissible answer range.** The expected recommendation allows justified adjacent outcomes when severity depends on venue or repair feasibility.
6. **Semantic de-identification.** Scientific domain, objects, notation, values, narrative order, and wording are independently reconstructed. No source title, author, affiliation, formula sequence, dataset, figure, citation list, or project identifier is retained.
7. **Publication safety.** Cases contain no confidential manuscript text, private referee material, editor correspondence, personal data, credentials, source URLs, citation keys, or unpublished third-party results.
8. **Mechanical validation.** Composite cases contain 380–900 words, three to six predefined defects, one to three decoys, valid severity labels, complete reference fields, and unique identifiers.

## Two-tier suite

### Atomic cases

Atomic cases isolate one primary defect. They support fast regression testing, routing checks, and individual calibration tests.

### Composite cases

Composite cases test root-cause grouping, priority, variable-role separation, proxy validity, inherited-theorem positioning, known-construction attribution, stochastic support, protocol fidelity, convergence of claim-bearing quantities, and recommendation coherence.

## Scoring

Use the defect IDs and rubric in `evals/rubric.md`. Report defect-level recall, severe false positives, severity calibration, bounded-resolution quality, recommendation coherence, unsupported assertions, and evidence-status accuracy separately.

The suite measures performance on its stated synthetic tasks. It does not establish equivalence to expert peer review or calibration against editorial outcomes.
