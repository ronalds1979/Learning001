# Sensitivity Classification Model — APS Scripts

All scripts must be classified according to data and system impact.

## Levels

### Public-Internal

- No secrets or credentials.
- No direct connectivity to production-only endpoints.
- Safe for broad internal reuse.

**Examples:**

- Simple connectivity tests to non-prod.
- Utility scripts operating on synthetic data.

### Restricted

- Interacts with security infrastructure, identity, or production systems.
- Uses credentials provided via GitHub Secrets or other vaults.
- Logs must not expose sensitive values.

**Examples:**

- Key rotation scripts.
- Policy deployment to GenAI firewall.
- Metrics export from production systems.

### Confidential

- Only allowed with explicit design & pattern approval.
- Typically avoided for code in GitHub; prefer dedicated secured platforms.

**Default rule:**

If in doubt, classify as **Restricted** and consult APS Security before committing.
