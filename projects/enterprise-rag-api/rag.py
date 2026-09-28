"""Small dependency-free RAG core used for deterministic local tests.

Production adapters can replace the tokenizer/retriever/generator without
changing the public contract.
"""
from dataclasses import dataclass
import re
from typing import Iterable


@dataclass(frozen=True)
class Document:
    id: str
    text: str


def _tokens(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]+", text.lower()))


def retrieve(query: str, documents: Iterable[Document], k: int = 3) -> list[Document]:
    """Rank documents using transparent lexical overlap."""
    q = _tokens(query)
    scored = []
    for doc in documents:
        score = len(q & _tokens(doc.text))
        if score:
            scored.append((score, doc.id, doc))
    scored.sort(key=lambda row: (-row[0], row[1]))
    return [row[2] for row in scored[:k]]


def build_grounded_answer(query: str, documents: Iterable[Document]) -> dict:
    """Return an auditable extractive answer with source IDs.

    This local implementation intentionally avoids external LLM calls so CI is
    reproducible. A production generator can consume the returned context.
    """
    hits = retrieve(query, documents)
    if not hits:
        return {"answer": "I do not have enough grounded context to answer.", "sources": []}
    context = " ".join(doc.text.strip() for doc in hits)
    return {"answer": context, "sources": [doc.id for doc in hits]}
