from datetime import date

from src.legal_followup import Matter, embed_matter, follow_up_decision


matter = Matter(
    matter_id="matter-104",
    intake_note="Client signed the settlement agreement; delivery receipt is filed.",
    signed_document_delivered=True,
    deadline=date(2026, 8, 14),
)

embedding = embed_matter(matter)
decision = follow_up_decision(matter, date(2026, 8, 10))
print({"matter_id": matter.matter_id, "embedding_dimensions": len(embedding), "decision": decision})

