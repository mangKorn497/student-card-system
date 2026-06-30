"""ทดสอบ StudentCard Model."""

from datetime import datetime, timedelta

import pytest

from src.models.student import Student
from src.models.student_card import StudentCard


class TestStudentCard:
    """ทดสอบ StudentCard Model."""

    @pytest.fixture
    def sample_student(self):
        return Student(
            student_id="67123456",
            first_name_th="ลิซ่า",
            last_name_th="Blackpink",
            first_name_en="Lisa",
            last_name_en="Blackpink",
            faculty="วิทยาศาสตร์",
        )

    def test_create_card(self, sample_student):
        card = StudentCard(student=sample_student)
        assert card.student == sample_student
        assert len(card.card_number.replace(" ", "")) == 16
        assert len(card.cvv) == 3

    def test_card_not_expired(self, sample_student):
        card = StudentCard(student=sample_student, expire_years=4)
        assert card.is_valid() is True
        assert card.is_expired() is False
        assert card.get_days_until_expire() > 0

    def test_card_expired(self, sample_student):
        card = StudentCard(
            student=sample_student,
            issue_date=datetime.now() - timedelta(days=5 * 365),
            expire_years=4,
        )
        assert card.is_valid() is False
        assert card.is_expired() is True
