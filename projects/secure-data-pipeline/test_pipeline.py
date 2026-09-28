from pipeline import process_batch


VALID = {
    "event_id": "e-1",
    "customer_id": "c-42",
    "event_type": "ticket_created",
    "occurred_at": "2026-09-28T00:00:00Z",
}


def test_valid_event_is_accepted():
    result = process_batch([VALID])
    assert len(result["accepted"]) == 1
    assert result["quarantined"] == []


def test_duplicate_event_is_idempotently_ignored():
    result = process_batch([VALID, VALID])
    assert len(result["accepted"]) == 1


def test_bad_record_is_quarantined_not_silently_dropped():
    bad = {**VALID, "event_type": "unknown"}
    result = process_batch([bad])
    assert result["accepted"] == []
    assert result["quarantined"][0]["reason"] == "unsupported event_type"
