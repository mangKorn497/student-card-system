"""CardService: Service layer สำหรับจัดการบัตรนักศึกษา."""

from datetime import datetime
from typing import List, Optional

from ..models.student import Student
from ..models.student_card import StudentCard
from .card_validator import CardValidator


class CardService:
    """Service สำหรับจัดการบัตรนักศึกษา."""

    def __init__(self) -> None:
        self._cards: List[StudentCard] = []
        self._validator = CardValidator()

    def create_student(self, **kwargs) -> Student:
        """สร้างนักศึกษาใหม่."""
        return Student(**kwargs)

    def create_card(
        self,
        student: Student,
        expire_years: int = 4,
        card_type: str = "VISA",
    ) -> StudentCard:
        """สร้างบัตรนักศึกษา."""
        card = StudentCard(
            student=student,
            expire_years=expire_years,
            card_type=card_type,
        )
        self._cards.append(card)
        return card

    def get_card_by_student_id(self, student_id: str) -> Optional[StudentCard]:
        """ค้นหาบัตรตามรหัสนักศึกษา."""
        for card in self._cards:
            if card.student.student_id == student_id:
                return card
        return None

    def get_all_cards(self) -> List[StudentCard]:
        """ดึงบัตรทั้งหมด."""
        return self._cards

    def get_active_cards(self) -> List[StudentCard]:
        """ดึงบัตรที่ยังไม่หมดอายุ."""
        return [card for card in self._cards if card.is_valid()]

    def validate_card(self, card: StudentCard) -> dict:
        """ตรวจสอบบัตร."""
        return self._validator.validate_card(card)

    def renew_card(
        self, card: StudentCard, additional_years: int = 4
    ) -> StudentCard:
        """ต่ออายุบัตร."""
        card.issue_date = datetime.now()
        card.expire_years = additional_years
        return card

    def get_statistics(self) -> dict:
        """สถิติบัตรทั้งหมด."""
        total = len(self._cards)
        active = len(self.get_active_cards())
        expired = total - active
        return {
            "total_cards": total,
            "active_cards": active,
            "expired_cards": expired,
        }
