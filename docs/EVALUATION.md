# Evaluation Protocol

## Objectives

The evaluation measures:

- routing precision and recall
- detection of predefined decision-relevant defects
- severe false-positive rate
- severity and recoverability calibration
- bounded-request compliance
- recommendation coherence
- unsupported-assertion rate
- evidence-status accuracy
- resistance to predetermined verdicts and document prompt injection

## Conditions

For a paired model evaluation, keep the following fixed:

- model and version
- reasoning setting
- tool access
- system and repository context
- manuscript input
- run count and sampling parameters
- evaluation date

Compare these conditions:

1. ordinary manuscript-review request without the skill
2. structured review prompt without the skill
3. the same request with `scientific-manuscript-audit`

## Trigger evaluation

Run every item in `evals/trigger_cases.jsonl`. Record whether the skill appears in the host's selected or invoked skill set. Compute precision, recall, specificity, and a confusion matrix for each host.

## Synthetic task evaluation

Run the atomic suite in `evals/synthetic_cases.jsonl` and the composite suite in `evals/composite/`. Store the full model output and annotate detected defect IDs, assigned severity, requested resolution, recommendation impact, unsupported assertions, and evidence-status labels.

## Repetition

Use at least three runs per condition for stochastic models. Report mean, range, and the number of valid runs. Keep raw outputs available for audit when confidentiality permits.

## Reporting

A result summary should include:

- model, version, host, date, and configuration
- task-set commit
- number of cases and runs
- all rubric metrics
- excluded or failed runs with reasons
- atomic and composite results reported separately
- representative successes and failures from synthetic cases
- limitations of the task set

The current repository does not include claims of expert equivalence or calibration against real editorial decisions.

## Case provenance and safety

All public evaluation inputs are independently written synthetic materials. Composite cases preserve recurring defect structures while replacing scientific domain, objects, notation, values, wording, and narrative organization. No real manuscript text or private review material is included. See `docs/CASE_DESIGN.md`.
