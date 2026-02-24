# <SUB_PRODUCT> - Deployment Scripts

This folder contains **deployment** automation for your sub-product: policy deployment, configuration rollout, and environment onboarding.

## Structure Reference

- [Architecture Overview](../../../docs/architecture.md)

## Governance Rules

- Deployment scripts must:
  - Be idempotent where possible.
  - Reference configuration from `shared/templates` or local config files (no hard-coded values).
  - Be linked to change requests / tracked work items.

- Branching:
  - Use `feat/<WORK_ITEM_ID>-deployment-...` for new deployment flows.
  - Use `fix/<WORK_ITEM_ID>-deployment-...` for corrections.

- PRs:
  - Require review from both product owner and operations (when applicable).
  - Must demonstrate testing in a lower environment before merging to `dev`.

## Mini Project Example

- `sub-product-deploy-policy/`
  - A small project that deploys product policy using config + helper module.
  - See `sub-product-deploy-policy/README.md` for details.
