# Security Policy

## Supported Versions

We provide security updates for the following branches:

| Version / Branch | Supported |
| --- | --- |
| `main` | ✅ Yes |
| `release/*` | ✅ Yes (until EOL) |
| `dev` | ⚠️ Best effort |
| Other / older | ❌ No |

> Update this table if your project uses a different release model.

---

## Reporting a Vulnerability

**Do not report vulnerabilities through public GitHub issues, discussions, or pull requests.**

Report privately through one of the channels below.

### Preferred Channel

- Security mailbox: `security-contact@company.com`

### Alternative Channels

- GitHub Security Advisories: use the repository **Report a vulnerability** feature (if enabled).
- Internal process: follow your organization’s incident-reporting process.

Please include:

- Clear description of the issue and potential impact
- Steps to reproduce (PoC if possible and safe)
- Affected components, endpoints, files, or configurations
- Relevant logs, screenshots, or error messages (sanitized)
- Severity assessment (if known) and suggested remediation (optional)

---

## Response and Remediation

After receiving a valid report, we will:

1. Acknowledge receipt within **2 business days**
2. Triage and validate the issue (may request more details)
3. Assign severity (**Critical / High / Medium / Low**)
4. Develop and test a fix or mitigation
5. Release a patch and/or mitigation guidance
6. Credit the reporter (optional), if requested

### Target remediation timelines

| Severity | Target timeline |
| --- | --- |
| Critical | 7-14 days |
| High | 14-30 days |
| Medium | 30-60 days |
| Low | Best effort / next planned release |

> Timelines are targets and may vary by complexity, dependencies, and release constraints.

---

## Scope

This policy applies to vulnerabilities affecting:

- Source code in this repository
- CI/CD workflows and configuration in this repository
- Scripts, automation, and infrastructure-as-code in this repository (if applicable)

Out of scope (unless there is a clear and demonstrable security impact):

- Issues affecting only outdated or unsupported versions
- Local/self-inflicted misconfiguration outside documented repository guidance
- Denial-of-service testing that harms availability
- Social engineering, phishing, or physical attacks

If you are unsure whether an issue is in scope, report it privately and we will triage.

---

## Safe Harbor (Good-Faith Research)

We support coordinated vulnerability disclosure and do not pursue legal action against researchers who:

- Act in good faith and avoid privacy violations, data destruction, and service disruption
- Access only the minimum data needed to prove impact
- Avoid public disclosure until we have had a reasonable chance to remediate
- Stop testing and report immediately if sensitive data is exposed

---

## Security Testing Guidelines

Please:

- Use the minimum testing necessary to demonstrate the issue
- Avoid high-volume or disruptive automated scanning
- Do not access, modify, or delete data you do not own
- Do not commit secrets (tokens, credentials, keys) to this repository

---

## Security Guidance for Contributors

When contributing changes:

- Do not include secrets in code, tests, examples, or docs
- Prefer secure defaults (least privilege, input validation, safe logging)
- Add or update tests for security-relevant changes
- Keep dependencies updated and avoid introducing known vulnerable packages

Recommended checks before opening a PR:

- Dependency scanning (SCA)
- Secret scanning
- Static analysis (SAST) and linting
- Unit and integration tests

---

## Disclosure and Public Communication

We follow coordinated disclosure:

- Public disclosure occurs only after a fix is available or mitigations are published
- Any advisory should include affected versions, impact, mitigation/fix details, and optional credits

---

## Contact

- Security: `security-contact@company.com`
- Maintainers: `maintainers@company.com`

---

## Project-Specific Notes (Optional)

If this repository includes CI security gates, document them here.

Example:

- SAST/SCA reports are generated in CI and reviewed for **Critical/High** findings.
- For details, see `docs/security-scanning.md`.
