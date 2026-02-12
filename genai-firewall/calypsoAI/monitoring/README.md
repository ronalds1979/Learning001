# calypsoAI - Monitoring Scripts

This folder includes scripts to export, aggregate, or alert on GenAI Firewall metrics for calypsoAI.

## Governance Rules

- Monitoring scripts must:
  - Avoid embedding credentials; use GitHub Secrets and/or platformâ€‘specific secret stores.
  - Declare performance impact clearly (e.g. polling frequency, API limits).

- PRs:
  - Must include description of which metrics are touched and where data is sent.
  - Require at least one reviewer from APS monitoring/ops.

## Scripts

- `calypsoai-export-metrics.py`
  - Exports calypsoAI metrics to the central monitoring stack.
  - Classification: `Restricted`.
