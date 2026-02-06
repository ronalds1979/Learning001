# APS â€“ GenAI Firewall (calypsoAI) â€“ Automation Scripts

This repository contains automation scripts for the **APS GenAI Firewall**, focusing on the **calypsoAI** sub-product.

It is designed to:
- Centralize all APS GenAI Firewall automation scripts in one governed, auditable place.
- Ensure scripts are **tagged, documented, reviewed, classified** as per APS Script Migration Framework.
- Align with NestlÃ© ITIP and APS GitHub Governance for Source Code Management and DevSecOps.

---

## Repository Structure

- `.github/workflows` â€“ CI workflows (linting, CodeQL, secret scanning, dependency review).
- `docs` â€“ Repository overview, classification model, contributing guide, migration evidence.
- `shared/modules` â€“ Reusable PowerShell modules / Python libraries.
- `shared/templates` â€“ Shared configuration and JSON/YAML templates.
- `genai-firewall/calypsoAI` â€“ Product-specific scripts, organized by functional area:
  - `maintenance`
  - `deployment`
  - `monitoring`
  - `test`

---

## Branching Model

We follow a simplified trunk-based APS GitHub Governance model:

- **`main`**
  - Production-ready code only.
  - Protected: no direct pushes, PRs required, all checks must pass.

- **`dev`**
  - Integration branch for upcoming releases.
  - All feature work is merged here first.

- **Short-lived branches** (examples):
  - `feat/<AB#id>-short-description`
  - `fix/<AB#id>-short-description`
  - `chore/<AB#id>-short-description`
  - `hotfix/<AB#id>-short-description`

Every branch must reference an Azure Boards work item ID (e.g. `AB#123456`) in the branch name and PR description.

---

## Pull Request (PR) Model

- **PRs are mandatory** for all changes.
- PRs must:
  - Target `dev` (or `main` for hotfixes).
  - Include:
    - Purpose and scope of change.
    - Reference to AB# work item(s).
    - Sensitivity classification for new/changed scripts.
    - Evidence of local testing where applicable.
  - Be approved by at least **one CODEOWNER**.

CI checks (linting, CodeQL, secret scanning, dependency review) **must pass** before merge.

---

## Sensitivity Classification

Scripts must be classified as one of:

- `Public-Internal` â€“ No production credentials or sensitive business logic.
- `Restricted` â€“ Touches security infrastructure, identity, or sensitive flows.
- `Confidential` â€“ Only allowed if an approved pattern and design exist; otherwise do **not** commit.

See `docs/classification-model.md` for detailed rules.

---

## Adding New Scripts

1. Identify the correct product and functional folder:
   - `genai-firewall/calypsoAI/maintenance`
   - `genai-firewall/calypsoAI/deployment`
   - `genai-firewall/calypsoAI/monitoring`
   - `genai-firewall/calypsoAI/test`

2. Use the naming convention:
   - `calypsoai-<description-using-verbs>.<ext>`
   - Examples:
     - `calypsoai-rotate-keys.ps1`
     - `calypsoai-export-metrics.py`

3. Add mandatory metadata header to the script (see `docs/contributing.md`).

4. Update the corresponding folder `README.md`:
   - Describe the script.
   - Set classification.
   - Declare the owner.

5. Open a PR from a feature branch â†’ `dev`, referencing AB# work item and classification.
# Learning001

This is a description for the readme file.
