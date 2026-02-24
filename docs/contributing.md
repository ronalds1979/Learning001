# Contributing Guide — Automation Scripts

## 1. Before You Start

- Ensure you have access to the repository and your project backlog/tracker.
- Identify the right folder:
  - `product-area/sub-product/maintenance`
  - `product-area/sub-product/deployment`
  - `product-area/sub-product/monitoring`
  - `product-area/sub-product/test`
  - `shared/modules` or `shared/templates`

## 2. Script Naming Convention

Use:

- `sub-product-<description-using-verbs>.<ext>`

Examples:

- `sub-product-rotate-keys.ps1`
- `sub-product-export-metrics.py`
- `sub-product-test-connection.ps1`

## 3. Mandatory Script Metadata Header

Each script must include a header like:

```text
.METADATA
  Product: <PRODUCT_AREA>
  SubProduct: <SUB_PRODUCT>
  Owner: <team or individual>
  WorkItem: <WORK-1234>
  Sensitivity: <Public-Internal|Restricted|Confidential>
  Dependencies: <list>
```
