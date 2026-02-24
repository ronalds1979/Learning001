# <SUB_PRODUCT> - Test Scripts

This folder hosts **non-production test utilities** for validating connectivity, configuration, and policies.

## Structure Reference

- [Architecture Overview](../../../docs/architecture.md)

## Governance Rules

- Test scripts:
  - Must be clearly labeled as **Non-Production**.
  - Must not contain or export production credentials.
  - Should be safe to run in lab environments.

- PRs:
  - Can be lighter weight but still require a review and passing checks.

## Scripts

- `sub-product-test-connection.ps1`
  - Simple connectivity test against sub-product endpoints.
  - Classification: `Public-Internal`.
