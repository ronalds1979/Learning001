# calypsoAI - Test Scripts

This folder hosts **nonâ€‘production test utilities** for validating connectivity, configuration, and policies.

## Governance Rules

- Test scripts:
  - Must be clearly labeled as **Nonâ€‘Production**.
  - Must not contain or export production credentials.
  - Should be safe to run in lab environments.

- PRs:
  - Can be lighter weight but still require a review and passing checks.

## Scripts

- `calypsoai-test-connection.ps1`
  - Simple connectivity test against calypsoAI endpoints.
  - Classification: `Public-Internal`.
