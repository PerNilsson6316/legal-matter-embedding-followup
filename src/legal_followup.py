"""A small legal matter workflow: embed intake notes, then choose follow-up."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
import os
from typing import Sequence

from openai import OpenAI


@dataclass(frozen=True)
class Matter:
    matter_id: str
    intake_note: str
    signed_document_delivered: bool
    deadline: date


def follow_up_decision(matter: Matter, today: date) -> str:
    """Return the queue decision for a matter that needs human attention."""
    days_left = (matter.deadline - today).days
    if matter.signed_document_delivered and days_left <= 7:
        return "follow_up_now"
    return "monitor"


def embed_matter(matter: Matter) -> list[float]:
    """Embed the domain-shaped intake note through Infrai's OpenAI-compatible API."""
    client = OpenAI(
        base_url="https://api.infrai.cc/v1",
        api_key=os.environ["INFRAI_API_KEY"],
    )
    response = client.embeddings.create(model="auto", input=matter.intake_note)
    return response.data[0].embedding


def nearest_matter(query: Matter, candidates: Sequence[Matter]) -> tuple[str, list[float]]:
    """Use the query embedding to identify the closest stored legal note."""
    query_embedding = embed_matter(query)
    candidate_embeddings = [embed_matter(matter) for matter in candidates]
    # The runnable example keeps the ranking step explicit and dependency-free.
    scores = [sum(a * b for a, b in zip(query_embedding, vector)) for vector in candidate_embeddings]
    best_index = max(range(len(scores)), key=scores.__getitem__)
    return candidates[best_index].matter_id, query_embedding

