# calypsoAI â€“ Deployment Scripts

This folder contains **deployment** automation for calypsoAI: policy deployment, configuration rollout, and environment onboarding.

## Governance Rules

- Deployment scripts must:
  - Be idempotent where possible.
  - Reference configuration from `shared/templates` or local config files (no hardâ€‘coded values).
  - Be linked to change requests / AB# work items.

- Branching:
  - Use `feat/<AB#id>-deployment-...` for new deployment flows.
  - Use `fix/<AB#id>-deployment-...` for corrections.

- PRs:
  - Require review from both APS product owner and operations (when applicable).
  - Must demonstrate testing in a lower environment before merging to `dev`.

## Miniâ€‘project Example

- `calypsoai-deploy-policy/`
  - A small project that deploys GenAI firewall policy using config + helper module.
  - See `calypsoai-deploy-policy/README.md` for details.
