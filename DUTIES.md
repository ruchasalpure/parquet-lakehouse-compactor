# Duties and Responsibilities for Parquet Lakehouse Compactor Agent

## Dual-Control Architecture
Maker:
row-group-compactor

Checker:
query-speedup-verifier

## Operational Workflow
1. The Maker (row-group-compactor) analyzes incoming telemetry, context, and requirements.
2. The Maker synthesizes a draft operational execution plan with supporting data.
3. The Checker (query-speedup-verifier) independently verifies all assumptions and constraints.
4. If validation passes, the plan is signed, logged, and committed.
5. All actions are appended to the immutable governance audit trail.
