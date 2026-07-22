# Release Process

This checklist defines the minimum integrity controls for an official release.

## 1. Prepare the release commit

- start from the current `main` branch
- confirm that the working tree contains only intended release changes
- synchronize `VERSION`, `CHANGELOG.md`, `CITATION.cff`, plugin metadata, README badges, and distribution packages
- run:

```bash
python scripts/build_dist.py
python scripts/validate_repo.py
python -m unittest discover -s tests -v
```

- require the repository `validate` workflow to pass on the release commit

## 2. Create an immutable version reference

Create a signed annotated tag when signing is available:

```bash
git tag -s vX.Y.Z -m "Scientific Manuscript Audit vX.Y.Z"
git push origin vX.Y.Z
```

A lightweight tag should not be used for an official stable release. Do not move or reuse a published version tag.

## 3. Build release assets

Create the archive from the tagged commit. Exclude local environments, caches, credentials, private evaluation outputs, unpublished manuscripts, and operating-system metadata.

Use stable asset names:

```text
scientific-manuscript-audit-vX.Y.Z.zip
SHA256SUMS
```

Generate the checksum from the final archive and verify it before upload.

## 4. Publish the GitHub Release

- create the release from the version tag
- include a concise change summary, installation instructions, compatibility notes, responsible-use notice, and known limitations
- upload the checked archive and `SHA256SUMS`
- mark prerelease versions as prereleases
- enable immutable releases when the repository and account support them
- do not replace an asset silently; publish a new version when release contents change

## 5. Verify publication

After publication:

- download the release asset from GitHub
- verify its SHA-256 checksum
- confirm the archive contains the expected `VERSION`, canonical skill, generated distributions, license, notice, security policy, and documentation
- confirm the tag resolves to the intended release commit
- confirm installation commands reference the official repository

## 6. Provenance and archives

The official repository and its GitHub Releases are the source of record. Third-party mirrors and modified packages remain independent distributions unless explicitly identified by the maintainer.

A stable release may also be archived with a long-term research repository such as Zenodo. External archival records should point back to the exact Git tag and official release page.
