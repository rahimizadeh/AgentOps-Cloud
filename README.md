# FlowFusion — Cloud-Native AI Engineering Portfolio

A production-oriented portfolio demonstrating software engineering, machine learning, agentic AI, RAG, evaluation, observability, AWS infrastructure as code, DevSecOps, and data engineering.

## Projects

| Project | Real-world problem | Core capabilities |
|---|---|---|
| `projects/enterprise-rag-api` | Grounded Q&A over enterprise knowledge | Python, FastAPI, RAG, citations, retrieval evaluation |
| `projects/incident-response-agent` | Triage cloud incidents with auditable tool use | Python, agentic workflow, guardrails, deterministic tests |
| `projects/ai-eval-observability` | Measure quality/reliability of LLM systems | Python, evaluation, latency/cost/quality metrics, regression gates |
| `projects/aws-ai-platform` | Provision a secure scalable AI API platform | TypeScript, AWS CDK, ECS/Fargate, ALB, CloudWatch, IAM |
| `projects/secure-data-pipeline` | Validate and transform event data safely | Python, data contracts, idempotency, quarantine, unit tests |

## Design principles

- **Traceable:** each project maps directly to a capability in a modern AI/cloud engineering role.
- **Testable:** core logic runs without paid APIs or cloud credentials; `pytest` covers deterministic behavior.
- **Production-minded:** typed interfaces, structured logging, health endpoints, explicit failure modes, security controls, CI and documentation.
- **Cloud-native:** stateless services, containers, AWS-oriented IaC, least-privilege patterns and observability.
- **Evaluation-first AI:** quality, groundedness, latency and regression checks are treated as engineering requirements.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
pytest -q
```

## Repository layout

```text
FlowFusion/
├── .github/workflows/ci.yml
├── projects/
│   ├── enterprise-rag-api/
│   ├── incident-response-agent/
│   ├── ai-eval-observability/
│   ├── aws-ai-platform/
│   └── secure-data-pipeline/
├── requirements-dev.txt
└── README.md
```

## Job-description coverage

- **Python + TypeScript:** Python services/data/evaluation; TypeScript AWS CDK.
- **AI agents / RAG:** auditable incident agent and retrieval-grounded knowledge API.
- **Evaluation / observability / optimisation:** offline metrics, regression thresholds and operational telemetry patterns.
- **AWS + IaC:** CDK stack for containerised deployment with logging, health checks and autoscaling-ready architecture.
- **DevSecOps + data engineering:** CI, dependency/security scanning hooks, data contracts, validation, idempotency and quarantine.

Each subproject contains its own README with architecture, test commands, acceptance criteria and extension points.