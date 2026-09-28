from evaluate import EvalCase, evaluate, passes_gate


def test_good_release_passes_quality_cost_latency_gate():
    case = EvalCase(
        answer="Use managed secrets service for application secrets",
        reference="Use managed secrets service for application secrets",
        context="Policy: use managed secrets service for application secrets",
        latency_ms=850,
        cost_usd=0.006,
    )
    assert passes_gate(evaluate(case))


def test_hallucinated_answer_fails_groundedness_gate():
    case = EvalCase(
        answer="Store secrets in public source control",
        reference="Use managed secrets service",
        context="Use managed secrets service for application secrets",
        latency_ms=500,
        cost_usd=0.004,
    )
    metrics = evaluate(case)
    assert metrics["groundedness"] < 0.90
    assert not passes_gate(metrics)


def test_slow_release_fails_operational_gate():
    case = EvalCase("approved answer", "approved answer", "approved answer", 3000, 0.001)
    assert not passes_gate(evaluate(case))
