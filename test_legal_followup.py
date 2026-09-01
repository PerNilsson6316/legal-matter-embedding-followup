from datetime import date

from src.legal_followup import Matter, follow_up_decision


def test_signed_delivery_close_to_deadline_enters_follow_up_queue() -> None:
    matter = Matter(
        matter_id="matter-test",
        intake_note="Signed lease is ready for the client confirmation.",
        signed_document_delivered=True,
        deadline=date(2026, 8, 16),
    )

    assert follow_up_decision(matter, date(2026, 8, 10)) == "follow_up_now"

