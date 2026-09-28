"""Offline AI quality metrics suitable for CI regression gates."""
from dataclasses import dataclass
import re


def tokens(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]+", text.lower()))


def answer_relevance(answer: str, reference: str) -> float:
    expected = tokens(reference)
    if not expected:
        return 1.0
    return len(tokens(answer) & expected) / len(expected)


def groundedness(answer: str, context: str) -> float:
    produced = tokens(answer)
    if not produced:
        return 1.0
    return len(produced & tokens(context)) / len(produced)


@dataclass(frozen=True)
class EvalCase:
    answer: str
    reference: str
    context: str
    latency_ms: int
    cost_usd: float


def evaluate(case: EvalCase) -> dict[str, float]:
    return {
        "relevance": round(answer_relevance(case.answer, case.reference), 4),
        "groundedness": round(groundedness(case.answer, case.context), 4),
        "latency_ms": float(case.latency_ms),
        "cost_usd": case.cost_usd,
    }


def passes_gate(metrics: dict[str, float]) -> bool:
    return (
        metrics["relevance"] >= 0.80
        and metrics["groundedness"] >= 0.90
        and metrics["latency_ms"] <= 2000
        and metrics["cost_usd"] <= 0.02
    )
