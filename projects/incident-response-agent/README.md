# Incident Response Agent

## Scenario
An SRE assistant triages a service incident using approved diagnostic tools, records every action and keeps destructive remediation behind human approval.

## Agent loop
`telemetry -> severity gate -> approved tools -> evidence -> recommendation -> human approval`

## Safety and reliability properties
- Tool allow-list prevents arbitrary actions.
- Low-severity incidents avoid unnecessary tool calls.
- Every tool result is recorded in an audit trail.
- The agent can **propose** rollback but cannot execute it.
- Deterministic policy tests make behavior easy to inspect.

## Test
```bash
python -m pytest -q
```

## Production extension
Wrap the state machine with LangGraph or another LLM orchestration framework; expose tools for CloudWatch/log search/change history; add RBAC, OpenTelemetry spans, retry budgets, model/tool timeouts and approval events.