# Security Policy

## Supported versions

Security fixes are applied to the latest released version and the current default branch.

## Reporting a vulnerability

Use GitHub's private vulnerability reporting or a private security advisory for this repository when available. Include the affected version, reproduction steps, impact, and any proposed mitigation. Avoid posting confidential manuscripts, credentials, private prompts, or exploit details in a public issue.

## Relevant security concerns

Reports are especially useful for:

- prompt injection through manuscripts or attachments
- unauthorized disclosure of manuscript content
- secret or personal-data leakage through examples, logs, or build artifacts
- unsafe file handling in repository scripts
- distribution packages that diverge from the canonical skill
- evaluation fixtures containing restricted third-party material
- altered or misleading packages presented as official distributions

## Verifying official distributions

The official source is the `KangqiaoLiu/scientific-manuscript-audit` repository. Before the first stable release, the default branch is the development source of record and the version badge identifies a prerelease version rather than a GitHub Release.

For stable releases, use tags and release assets published from the official repository. Verify any published checksum before installing a downloaded archive. Treat third-party mirrors, repackaged archives, modified forks, and hosted services as independent distributions unless the official repository explicitly identifies them as maintained releases.

Report checksum mismatches, replaced assets, misleading branding, or packages that claim official status through a private security channel when possible.

## Workflow security

Repository workflows use read-only default permissions. External GitHub Actions are pinned to full commit SHAs, checkout credentials are not persisted, and Dependabot monitors GitHub Actions references. Changes to workflows, build scripts, canonical skill files, generated distributions, security policy, or release-critical metadata should receive explicit maintainer review.
