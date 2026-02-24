# <SUB_PRODUCT> - Maintenance Scripts

This folder contains **maintenance** scripts for your product/sub-product, such as key rotation, cleanup tasks, and periodic housekeeping.

## Structure Reference

- [Architecture Overview](../../../docs/architecture.md)

## Governance Rules (Local View)

- All scripts must:
  - Follow naming convention `<sub-product>-<description-using-verbs>.<ext>`.
  - Include the metadata header defined in `docs/contributing.md`.
  - Be classified according to `docs/classification-model.md`.

- Changes to this folder:
  - Must be done via feature branches: `feat/<WORK_ITEM_ID>-maintenance-...`.
  - Must go through PR review by a CODEOWNER for the sub-product area.
  - Must pass linting and security checks (CodeQL, secret scanning).

## Scripts

- `sub-product-rotate-keys.ps1`
  - Rotates API keys / credentials used by the sub-product according to security policy.
  - Classification: `Restricted`.
