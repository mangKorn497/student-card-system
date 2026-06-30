"""ทดสอบ CardService."""

from src.services.card_service import CardService


class TestCardService:
    """ทดสอบ CardService."""

    def test_create_student_and_card(self):
        service = CardService()
        student = service.create_student(
            student_id="67123456",
            first_name_th="ลิซ่า",
            last_name_th="Blackpink",
            first_name_en="Lisa",
            last_name_en="Blackpink",
            faculty="วิทยาศาสตร์",
        )
        card = service.create_card(student)
        assert card is not None
        assert card.student.student_id == "67123456"

    def test_get_card_by_student_id(self):
        service = CardService()
        student = service.create_student(
            student_id="67123456",
            first_name_th="ลิซ่า",
            last_name_th="Blackpink",
            first_name_en="Lisa",
            last_name_en="Blackpink",
            faculty="วิทยาศาสตร์",
        )
        card = service.create_card(student)
        found_card = service.get_card_by_student_id("67123456")
        assert found_card is not None
        assert found_card.card_number == card.card_number

    def test_validate_card(self):
        service = CardService()
        student = service.create_student(
            student_id="67123456",
            first_name_th="ลิซ่า",
            last_name_th="Blackpink",
            first_name_en="Lisa",
            last_name_en="Blackpink",
            faculty="วิทยาศาสตร์",
        )
        card = service.create_card(student)
        validation = service.validate_card(card)
        assert validation["is_valid"] is True
        assert len(validation["errors"]) == 0

    def test_get_statistics(self):
        service = CardService()
        for i in range(5):
            student = service.create_student(
                student_id=f"6712345{i}",
                first_name_th="ลิซ่า",
                last_name_th="Blackpink",
                first_name_en="Lisa",
                last_name_en="Blackpink",
                faculty="วิทยาศาสตร์",
            )
            service.create_card(student)
        stats = service.get_statistics()
        assert stats["total_cards"] == 5
        assert stats["active_cards"] == 5
        assert stats["expired_cards"] == 0
