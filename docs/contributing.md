# Contributing Guide — APS GenAI Firewall Scripts

## 1. Before You Start

- Ensure you have access to the repository and APS product backlog (Azure Boards).
- Identify the right folder:
  - `genai-firewall/calypsoAI/maintenance`
  - `genai-firewall/calypsoAI/deployment`
  - `genai-firewall/calypsoAI/monitoring`
  - `genai-firewall/calypsoAI/test`
  - `shared/modules` or `shared/templates`

## 2. Script Naming Convention

Use:

- `calypsoai-<description-using-verbs>.<ext>`

Examples:

- `calypsoai-rotate-keys.ps1`
- `calypsoai-export-metrics.py`
- `calypsoai-test-connection.ps1`

## 3. Mandatory Script Metadata Header

Each script must include a header like:

```text
.METADATA
  Product: genai-firewall
  SubProduct: calypsoAI
  Owner: <team or individual>
  AB_WorkItem: AB#<id>
  Sensitivity: <Public-Internal|Restricted|Confidential>
  Dependencies: <list>
```
