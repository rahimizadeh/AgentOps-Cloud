"""Data-contract and idempotency example for an event ingestion pipeline."""
from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass(frozen=True)
class Event:
    event_id: str
    customer_id: str
    event_type: str
    occurred_at: str


ALLOWED_TYPES = {"ticket_created", "ticket_resolved", "feedback_received"}


def validate(raw: dict) -> Event:
    required = {"event_id", "customer_id", "event_type", "occurred_at"}
    missing = required - raw.keys()
    if missing:
        raise ValueError(f"missing fields: {sorted(missing)}")
    if raw["event_type"] not in ALLOWED_TYPES:
        raise ValueError("unsupported event_type")
    datetime.fromisoformat(raw["occurred_at"].replace("Z", "+00:00"))
    return Event(**{key: raw[key] for key in required})


def process_batch(records: list[dict], seen: set[str] | None = None) -> dict:
    seen = set() if seen is None else seen
    accepted, quarantined = [], []
    for raw in records:
        try:
            event = validate(raw)
            if event.event_id in seen:
                continue
            seen.add(event.event_id)
            accepted.append({**raw, "processed_at": datetime.now(timezone.utc).isoformat()})
        except (ValueError, TypeError) as exc:
            quarantined.append({"record": raw, "reason": str(exc)})
    return {"accepted": accepted, "quarantined": quarantined, "seen": seen}
