# <SUB_PRODUCT> - Monitoring Scripts

This folder includes scripts to export, aggregate, or alert on product metrics.

## Structure Reference

- [Architecture Overview](../../../docs/architecture.md)

## Governance Rules

- Monitoring scripts must:
  - Avoid embedding credentials; use GitHub Secrets and/or platform-specific secret stores.
  - Declare performance impact clearly (e.g. polling frequency, API limits).

- PRs:
  - Must include description of which metrics are touched and where data is sent.
  - Require at least one reviewer from monitoring/operations.

## Scripts

- `sub-product-export-metrics.py`
  - Exports sub-product metrics to the central monitoring stack.
  - Classification: `Restricted`.
