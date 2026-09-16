# Changelog

All notable changes are recorded in this file.

## [0.2.0] - 2026-09-16

### Added

- OpenAI `agents/openai.yaml` interface metadata for the canonical skill and generated distributions
- explicit full-package audit guidance for figures, code/data, supplements, rendered documents, cover letters, and submission metadata when relevant

### Changed

- rewrote the runtime skill around an instruction-first workflow aligned with current OpenAI Agent Skills guidance
- strengthened independent reconstruction of the strongest supported contribution before judging correctness, novelty, significance, or venue fit
- made prior referee reports and response letters contextual evidence rather than substitutes for direct verification
- preserved the project-specific claim-to-evidence chain, recoverability-calibrated severity, bounded resolutions, and recommendation coherence while removing unnecessary fixed-output structure
- updated Codex and Claude Code distributions to ship only runtime-relevant skill files

### Removed

- `TESTS.md` from the canonical runtime skill and generated host distributions; behavioral evaluation remains in the repository `evals/` suite

## [0.1.0] - 2026-07-22

### Added

- canonical `scientific-manuscript-audit` Agent Skill
- Codex and Claude Code distribution packages
- Claude Code plugin marketplace metadata
- 60 trigger and boundary cases
- 12 atomic synthetic manuscript-audit cases
- 6 composite synthetic manuscript-audit cases
- worked synthetic examples, evaluation protocol, and scoring rubric
- repository validation, security, responsible-use, citation, licensing, and release documentation
- complete English, Simplified Chinese, and Japanese README documentation

### Changed

- strengthened claim-to-evidence checks, severity calibration, bounded revision requests, and recommendation coherence
- aligned Claude Code plugin metadata with current manifest and default skill discovery
- hardened GitHub Actions, repository protections, dependency monitoring, and distribution synchronization
- clarified author-side scope, confidentiality requirements, and the boundary with formal peer review and editorial judgment

## [0.1.0-rc.3] - 2026-07-22

### Added

- repository checks for version synchronization and Claude Code plugin metadata
- pre-publication compatibility and exposure audit
- prominent author-side scope guidance in all README translations

### Changed

- aligned the Claude Code plugin manifest with the current manifest schema and default skill discovery
- removed duplicate component declarations from the Claude Code marketplace entry
- updated pinned GitHub Actions to the current checkout and setup-python v6 releases
- clarified Claude Code CLI activation instructions in all README translations
- clarified that the project supports pre-submission and revision quality control and does not replace human peer review or editorial judgment

## [0.1.0-rc.2] - 2026-07-22

### Added

- 6 longer composite manuscript-audit cases constructed under explicit de-identification and quality gates
- worked synthetic README examples for claim-to-endpoint and revision-resolution audits
- synthetic case design and provenance documentation
- evaluation export support for atomic, composite, or combined suites
- complete Simplified Chinese and Japanese README translations with synchronized language policy
- trademark policy, code ownership rules, GitHub Actions dependency monitoring, and secure release checklist

### Changed

- strengthened checks for variable-role conflation, proxy-to-endpoint validity, inherited theorems, known constructions, stochastic support, protocol fidelity, and convergence of claim-bearing quantities
- expanded repository validation and tests to cover the composite suite and repository protection controls
- pinned external GitHub Actions to full commit SHAs, disabled persisted checkout credentials, and added workflow timeout and concurrency controls
- strengthened contribution rights, licensing, confidential-material, and official-distribution guidance

## [0.1.0-rc.1] - 2026-07-22

### Added

- canonical `scientific-manuscript-audit` Agent Skill
- Codex and Claude Code distribution packages
- Claude Code plugin marketplace metadata
- 60 trigger and boundary cases
- 12 synthetic manuscript-audit cases
- evaluation rubric and protocol
- repository validation and distribution synchronization checks
- responsible-use, security, contribution, citation, and licensing files
