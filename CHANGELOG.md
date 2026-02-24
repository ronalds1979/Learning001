# Changelog

All notable changes to this project are documented in this file.

This changelog format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and uses [Semantic Versioning](https://semver.org/) where applicable.

## [Unreleased]

### Added

- _No changes yet._

### Changed

- _No changes yet._

### Deprecated

- _No changes yet._

### Removed

- _No changes yet._

### Fixed

- _No changes yet._

### Security

- _No changes yet._

---

## [1.0.0] - YYYY-MM-DD

### Added

- Initial release.

---

## Release Entry Guidelines

Use the sections below only when they apply:

- **Added** – for new features.
- **Changed** for updates to existing behavior.
- **Deprecated** for soon-to-be removed features.
- **Removed** for now-removed features.
- **Fixed** for bug fixes.
- **Security** for vulnerability fixes and hardening.

Write entries in past tense and user-impact language.

Recommended style:

- Keep each bullet concise and user-facing.
- Include scope when helpful (for example: API, CI, docs, security).
- Reference tickets/PRs when available (for example: `(#123)`).
- Avoid internal-only noise unless it affects users or operations.

Examples:

- Added token refresh support for long-running API sessions.
- Changed CodeQL workflow to skip languages with no source files.
- Fixed dependency installation in monorepo subfolders.
- Security: Hardened secret-handling guidance in repository templates.

---

## Versioning and Dates

- Tag stable releases as `MAJOR.MINOR.PATCH` (for example `1.4.2`).
- Use date format `YYYY-MM-DD`.
- Keep newest versions at the top, directly below `Unreleased`.
- Move items from `Unreleased` to a new version section at release time.

Release workflow:

1. Finalize `Unreleased` entries.
2. Create version heading with release date.
3. Update comparison links at the end of this file.

---

## Link References (Optional but Recommended)

Add link references at the end of the file so version headers are clickable:

```markdown
[Unreleased]: https://github.com/ORG/REPO/compare/v1.0.1...HEAD
[1.0.1]: https://github.com/ORG/REPO/compare/v1.0.0...v1.0.1
[1.0.0]: https://github.com/ORG/REPO/releases/tag/v1.0.0
```

Replace `ORG/REPO` with your repository path.
