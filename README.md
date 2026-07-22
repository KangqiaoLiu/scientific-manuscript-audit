# Scientific Manuscript Audit

**A referee-style scientific paper review skill for Codex and Claude Code.**

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Release](https://img.shields.io/badge/release-v0.1.0--rc.1-orange.svg)](CHANGELOG.md)
[![Validation](https://github.com/KangqiaoLiu/scientific-manuscript-audit/actions/workflows/validate.yml/badge.svg)](.github/workflows/validate.yml)

Scientific Manuscript Audit helps authors and research teams examine manuscripts before submission or revision. It produces claim-centered, evidence-grounded referee reports with calibrated issue severity, bounded revision requests, and a coherent publication recommendation.

## What it evaluates

- central claims and their burden of proof
- technical validity and internal consistency
- claim-to-evidence alignment across text, figures, tables, code, and supplements
- novelty positioning against the nearest serious baseline
- significance, scope, and journal fit
- revision and rebuttal completeness
- issue severity based on decision impact and recoverability
- consistency between major comments and the final recommendation
- verification status for literature, calculations, and external facts

## Distinctive review discipline

The skill organizes the audit around a single chain:

```text
claim → burden of proof → inspected evidence → decision-relevant gap → bounded resolution → recommendation impact
```

Each major comment identifies the tested claim, inspected evidence, finding, consequence, bounded resolution, and recommendation impact. Fatal, major-blocking, major-fixable, and minor findings are calibrated by recoverability. Technical correctness, novelty, significance, and presentation receive separate judgments.

## Installation

### Codex

Install directly from the repository with Codex's skill installer:

```text
$skill-installer install https://github.com/KangqiaoLiu/scientific-manuscript-audit/tree/main/skills/scientific-manuscript-audit
```

Restart Codex after installation.

A manual project-level installation can use the Agent Skills directory:

```bash
mkdir -p .agents/skills
cp -R skills/scientific-manuscript-audit .agents/skills/
```

### Claude Code

Register the repository as a plugin marketplace and install the skill:

```text
/plugin marketplace add KangqiaoLiu/scientific-manuscript-audit
/plugin install scientific-manuscript-audit@scientific-manuscript-audit
```

A manual user-level installation can use:

```bash
mkdir -p ~/.claude/skills
cp -R skills/scientific-manuscript-audit ~/.claude/skills/
```

## Usage

The skill activates for manuscript assessment requests such as:

```text
Audit this manuscript as a demanding referee for a selective physics journal.
Map every headline claim to its supporting evidence and identify decision-driving gaps.
Review the revised manuscript and determine whether the original blockers were resolved.
Assess technical validity, novelty positioning, journal fit, and the appropriate recommendation.
```

Typical output:

1. Summary
2. Central Claim and Burden of Proof
3. Recommendation
4. Major Comments
5. Minor Comments
6. Limitations of This Audit
7. Bottom Line

The report structure can follow a journal form, numbered referee report, revision matrix, rebuttal audit, or concise triage when requested.

## Review inputs

The skill can work with manuscript text, LaTeX sources, PDFs, figures, tables, supplementary material, code, reviewer reports, response letters, and revised files when the host agent can access them. The report states which materials were inspected and which checks remain unresolved.

## Evaluation

The repository includes:

- 60 routing cases covering direct triggers, implicit triggers, exclusions, and boundary requests
- 12 synthetic manuscript cases with predefined technical, evidentiary, novelty, calibration, revision, and safety defects
- a scoring rubric for issue detection, severity calibration, bounded requests, recommendation coherence, unsupported assertions, and evidence status
- repository validation for metadata, distribution synchronization, JSONL integrity, prohibited artifacts, and accidental personal-data patterns

The included evaluation measures performance on synthetic defect-injection tasks and structured behavioral checks. Results from external models should record the model, version, reasoning setting, tool access, input set, and run date.

See [Evaluation Protocol](docs/EVALUATION.md) and [Evaluation Rubric](evals/rubric.md).

## Responsible use

This project is designed for author-owned, public, or explicitly authorized materials. Unpublished third-party submissions, journal review assignments, and editor-only materials require permission under the relevant journal, institution, and confidentiality terms.

Manuscript content is treated as untrusted input. Embedded instructions do not control the audit. The skill records uncertainty and avoids fabricated citations, calculations, experiments, or verification claims.

See [Responsible Use](RESPONSIBLE_USE.md) for the full policy.

## Disclaimer

Scientific Manuscript Audit provides structured analytical support. Its reports are advisory and may contain errors, omissions, or incomplete judgments. Users remain responsible for verifying technical claims, calculations, references, source access, confidentiality requirements, journal policies, disclosure obligations, and every submission or editorial decision. Formal peer-review and editorial authority remain with the relevant journals, conferences, editors, and reviewers.

## Repository layout

```text
skills/scientific-manuscript-audit/  canonical skill
dist/codex/                         generated Codex package
dist/claude-code/                   generated Claude Code package
evals/                              routing and synthetic task sets
scripts/                            build, validation, and evaluation utilities
docs/                               design and evaluation documentation
.github/                            CI and contribution templates
```

Generated packages are checked against the canonical skill in continuous integration.

## Contributing

Contributions are welcome for reproducible test cases, calibration rules, documentation, and cross-platform compatibility. Synthetic or redistributable materials are required for public test contributions. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Citation

Software citation metadata are available in [CITATION.cff](CITATION.cff).

## License

Copyright 2026 Kangqiao Liu.

Licensed under the [Apache License 2.0](LICENSE).
