from agent import IncidentAgent, IncidentState


def tools():
    return {
        "get_logs": lambda service: "new deployment followed by HTTP 500 spike",
        "get_health": lambda service: "degraded",
    }


def test_low_severity_does_not_call_tools():
    state = IncidentState("payments", 0.01, 250)
    result = IncidentAgent(tools()).run(state)
    assert result["recommendation"] == "observe"
    assert result["actions"] == []


def test_high_severity_is_auditable_and_requires_approval():
    state = IncidentState("payments", 0.20, 1800)
    result = IncidentAgent(tools()).run(state)
    assert result["recommendation"] == "propose-rollback-for-approval"
    assert result["actions"] == [
        "get_logs:new deployment followed by HTTP 500 spike",
        "get_health:degraded",
    ]


def test_unknown_tool_is_blocked():
    state = IncidentState("payments", 0.2, 1800)
    agent = IncidentAgent(tools())
    try:
        agent._call("delete_database", "payments", state)
        assert False, "expected ValueError"
    except ValueError as exc:
        assert "not allowed" in str(exc)
