# AI Evaluation & Observability

## Scenario
A team needs objective release gates for an LLM/RAG service instead of relying on demo quality.

This project treats four dimensions as first-class signals: **answer relevance, groundedness, latency and cost**. The included implementation is intentionally deterministic and CI-friendly.

## Run
```bash
python -m pytest -q
```

## Release gate
A candidate must meet configured thresholds for semantic proxy metrics and operational SLOs. Tests demonstrate passing, hallucination-like failure and latency regression.

## Production extension
- Curated golden dataset with versioned prompts and expected evidence.
- LLM-as-judge only as a complementary metric, calibrated against human labels.
- OpenTelemetry traces for model, retrieval and tool spans.
- Dashboards for p50/p95 latency, token/cost usage, error rate, retrieval hit rate and quality drift.
- A/B or canary evaluation before full rollout.

The key engineering point is that model quality becomes measurable, observable and enforceable in CI/CD.