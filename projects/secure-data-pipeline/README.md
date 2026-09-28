# Secure Data Pipeline

## Scenario
Customer-support events arrive from multiple producers. Analytics and AI systems require trustworthy records without duplicate processing or silent data loss.

## Flow
`producer -> schema validation -> deduplication -> accepted dataset`
`                              -> quarantine + reason`

## Engineering properties
- Explicit data contract and allowed event taxonomy.
- ISO timestamp validation.
- Idempotent event IDs.
- Invalid records are quarantined with a reason rather than discarded.
- Processing metadata supports lineage/audit.

## Test
```bash
python -m pytest -q
```

## AWS production mapping
API Gateway/Kinesis or SQS -> Lambda/ECS consumer -> S3 raw/curated/quarantine zones -> Glue catalog -> Athena/warehouse. Add KMS encryption, IAM least privilege, DLQs, schema registry, data-quality metrics and lifecycle policies.