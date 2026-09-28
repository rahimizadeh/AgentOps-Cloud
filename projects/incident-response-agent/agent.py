"""Auditable incident-response agent with constrained tool use."""
from dataclasses import dataclass, field
from typing import Callable


@dataclass
class IncidentState:
    service: str
    error_rate: float
    latency_ms: int
    actions: list[str] = field(default_factory=list)


class IncidentAgent:
    def __init__(self, tools: dict[str, Callable[[str], str]]):
        self.tools = tools

    def _call(self, name: str, service: str, state: IncidentState) -> str:
        if name not in self.tools:
            raise ValueError(f"tool not allowed: {name}")
        result = self.tools[name](service)
        state.actions.append(f"{name}:{result}")
        return result

    def run(self, state: IncidentState) -> dict:
        """Conservative policy: inspect first; never auto-deploy/rollback."""
        if state.error_rate < 0.05 and state.latency_ms < 1000:
            return {"severity": "low", "recommendation": "observe", "actions": state.actions}

        logs = self._call("get_logs", state.service, state)
        health = self._call("get_health", state.service, state)
        recommendation = "escalate-to-human"
        if "deployment" in logs.lower() or health.lower() == "degraded":
            recommendation = "propose-rollback-for-approval"
        return {"severity": "high", "recommendation": recommendation, "actions": state.actions}
