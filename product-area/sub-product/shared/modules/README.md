# <SUB_PRODUCT> - Shared Modules

Reusable functions for repository automation scripts.

## Structure Reference

- [Architecture Overview](../../../../docs/architecture.md)

- PowerShell modules (`*.psm1`)
- Python libraries (`*.py`)

Governance:

- Shared modules should be generic and **not tied to a single product**.
- Changes require review from at least one shared-modules CODEOWNER.
- Versioning / breaking changes must be documented in `docs/migration-evidence.md`.
