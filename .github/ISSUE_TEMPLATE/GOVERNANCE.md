# Repository Governance

## 1) Purpose

This document defines how the repository is governed, maintained, and evolved.
It sets clear ownership, decision rights, and quality/security controls.

Canonical repository overview: [docs/repository-overview.md](../../docs/repository-overview.md).

## 2) Scope

This governance applies to:

- Source code, documentation, workflows, and configuration in this repository
- Pull request review, approval, and merge controls
- Release, security, and compliance processes tied to this repository

## 3) Roles and Ownership

Assign named teams or roles below:

- Product Owner: <Team / Role>
- Technical Owner: <Team / Role>
- Security Owner: <Team / Role>
- Operations Owner (optional): <Team / Role>

Responsibilities:

- Product Owner: prioritization, roadmap alignment, business acceptance
- Technical Owner: architecture, code quality, technical decisions
- Security Owner: threat/risk review, security controls, disclosure coordination
- Operations Owner: deployment, runtime reliability, rollback readiness

## 4) Decision-Making Model

### Standard Changes

- Approved by at least one required code owner and one maintainer review
- Must pass mandatory CI checks before merge

### High-Impact Changes

The following require explicit owner sign-off and implementation notes:

- Architectural changes
- Security-impacting changes
- Breaking API/schema/configuration changes
- Changes affecting compliance controls

### Escalation

If no consensus is reached, escalate to Product Owner + Technical Owner for final decision.

## 5) Contribution and Merge Policy

- All changes must be submitted via Pull Request
- Direct commits to protected branches are not allowed
- Linked work item is required (for traceability)
- PR template sections must be completed
- Fast PR mode is allowed only for tiny low-risk non-code changes

## 6) Branching and Release Policy

- `main`: production-ready code
- `dev`: integration and validation
- `release/*`: stabilization and release hardening

Release requirements:

- CI green for required checks
- Security scans completed with triaged findings
- Release notes/changelog updated
- Rollback approach documented for high-risk releases

## 7) Security and Vulnerability Handling

- Potential vulnerabilities must be reported through private channels
- Public issues must not include exploit details, secrets, or sensitive data
- Follow repository security policy and coordinated disclosure process

## 8) Compliance and Auditability

- Changes must be traceable to approved work items
- Approval records and CI evidence must be retained in PR history
- Material decisions should be documented in PR description or ADR/RFC docs

## 9) Exceptions

Policy exceptions require:

- Documented justification
- Time-bound approval from Technical Owner (and Security Owner if relevant)
- Follow-up action with due date

## 10) Review Cadence

Review this governance document at least quarterly or when any of the following changes:

- Team ownership
- Branching/release model
- Security/compliance requirements
- Major architecture or platform direction

## 11) Contacts

- Repository Maintainers: <team-or-owner-email@company.com>
- Security Contact: <security-contact@company.com>
- Compliance/Legal (optional): <legal-contact@company.com>
