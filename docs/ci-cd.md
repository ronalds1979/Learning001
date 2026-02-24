# CI/CD Workflows

This document describes the CI/CD workflows in this repository, including purpose, triggers, and permissions.

## Workflow Index

| Workflow | Purpose | Triggers | Key Permissions |
| --- | --- | --- | --- |
| [.github/workflows/ci.yml](../.github/workflows/ci.yml) | Orchestrates reusable workflows for lint, CodeQL, dependency review, and secret scanning. | pull_request (opened, synchronize, reopened), push, workflow_dispatch | contents: read (workflow); lint job adds pull-requests: write; CodeQL job adds security-events: write. |
| [.github/workflows/lint.yml](../.github/workflows/lint.yml) | Lints Python, PowerShell, and shell scripts with reports. | pull_request, push, workflow_dispatch, workflow_call | contents: read; pull-requests: write. |
| [.github/workflows/codeql.yml](../.github/workflows/codeql.yml) | Static analysis for Python and JavaScript. | pull_request, push, schedule (Mon 02:00 UTC), workflow_dispatch, workflow_call | actions: read; contents: read; security-events: write; pull-requests: write. |
| [.github/workflows/dependency-review.yml](../.github/workflows/dependency-review.yml) | Reviews dependency changes for vulnerabilities and license issues. | pull_request, push, schedule (Mon 02:00 UTC), workflow_dispatch, workflow_call | contents: read; pull-requests: write; issues: write. |
| [.github/workflows/secret-scanning.yml](../.github/workflows/secret-scanning.yml) | Scans for secrets using gitleaks and custom patterns, uploads SARIF. | pull_request, push, workflow_dispatch, workflow_call | contents: read; pull-requests: write; security-events: write. |

## Notes

- Reusable workflows use workflow_call. The caller determines the maximum permissions available.
- Scheduled runs use cron `0 2 * * 1` (Monday 02:00 UTC).
- Update this document when adding, removing, or changing workflow behavior.
