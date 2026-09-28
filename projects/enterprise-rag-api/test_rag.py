from rag import Document, build_grounded_answer, retrieve


def docs():
    return [
        Document("runbook", "Production incidents require an incident commander and rollback plan."),
        Document("security", "Secrets must be stored in a managed secrets service and never committed."),
        Document("leave", "Annual leave requests are submitted through the HR portal."),
    ]


def test_retrieval_is_relevant_and_traceable():
    hits = retrieve("Where should application secrets be stored?", docs(), k=1)
    assert [d.id for d in hits] == ["security"]


def test_answer_contains_source_ids():
    result = build_grounded_answer("incident rollback", docs())
    assert result["sources"] == ["runbook"]


def test_abstains_without_evidence():
    result = build_grounded_answer("quantum entanglement", docs())
    assert result["sources"] == []
    assert "enough grounded context" in result["answer"]
