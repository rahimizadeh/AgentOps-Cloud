# Enterprise RAG API

## Scenario
An internal knowledge assistant must answer employee questions from approved documents while exposing evidence and refusing unsupported answers.

## Architecture
`query -> retriever -> ranked context -> grounded response -> source IDs`

The repository ships a deterministic lexical retriever so the acceptance tests run offline. In production, the same contract can be adapted to OpenSearch/pgvector plus an LLM framework such as LangChain or LlamaIndex and a managed model endpoint.

## Why this is production-relevant
- Explicit grounding and source traceability.
- Safe abstention when retrieval returns no evidence.
- Replaceable retrieval/generation boundaries.
- Deterministic CI tests rather than tests that depend on a live model.

## Test
From this directory:

```bash
python -m pytest -q
```

## Acceptance criteria
1. A security query retrieves the security document.
2. Every grounded answer exposes source IDs.
3. Unsupported questions abstain rather than hallucinate.

## Production extension
Add document ingestion/chunking, embeddings, hybrid retrieval, reranking, prompt-injection filtering, authentication, tenancy, FastAPI endpoints, OpenTelemetry traces and an offline evaluation dataset.