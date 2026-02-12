# calypsoAI - Maintenance Scripts

This folder contains **maintenance** scripts for the APS GenAI Firewall (calypsoAI), such as key rotation, cleanup tasks, and periodic housekeeping.

## Governance Rules (Local View)

- All scripts must:
  - Follow naming convention `calypsoai-<description-using-verbs>.<ext>`.
  - Include the metadata header defined in `docs/contributing.md`.
  - Be classified according to `docs/classification-model.md`.

- Changes to this folder:
  - Must be done via feature branches: `feat/<AB#id>-maintenance-...`.
  - Must go through PR review by a CODEOWNER for `calypsoAI`.
  - Must pass linting and security checks (CodeQL, secret scanning).

## Scripts

- `calypsoai-rotate-keys.ps1`
  - Rotates API keys / credentials used by calypsoAI according to security policy.
  - Classification: `Restricted`.
