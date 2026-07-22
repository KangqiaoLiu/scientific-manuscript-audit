# Contributing

Contributions are welcome for review logic, documentation, synthetic evaluation cases, validation utilities, and compatibility improvements.

## Contribution requirements

- Use original, public-domain, openly licensed, or otherwise redistributable material.
- Exclude confidential manuscripts, real private referee reports, editor correspondence, personal data, credentials, and local paths.
- Keep claims supported by tests or clearly identified design rationale.
- Add or update behavioral cases for changes to routing, severity, recommendation, or safety behavior.
- Run the repository validation before opening a pull request.

```bash
python scripts/build_dist.py
python scripts/validate_repo.py
python -m unittest discover -s tests -v
```

## Synthetic evaluation cases

Each new synthetic case should define:

- the manuscript fragment or revision scenario
- the central advertised claim
- one or more predefined defects
- expected severity
- acceptable bounded resolutions
- recommendation impact
- evidence needed for verification

Keep cases compact enough to inspect and free of material derived from confidential manuscripts.

## Pull requests

Describe the purpose, files changed, tests run, and expected behavioral effect. Changes to `skills/scientific-manuscript-audit/` require regenerated distribution packages.
