"""ทดสอบ Student Model."""

from src.models.student import Student


class TestStudent:
    """ทดสอบ Student Model."""

    def test_create_student(self):
        student = Student(
            student_id="67123456",
            first_name_th="ลิซ่า",
            last_name_th="Blackpink",
            first_name_en="Lisa",
            last_name_en="Blackpink",
            faculty="วิทยาศาสตร์",
        )
        assert student.student_id == "67123456"
        assert student.get_full_name_th() == "ลิซ่า Blackpink"
        assert student.get_full_name_en() == "LISA BLACKPINK"

    def test_student_to_dict(self):
        student = Student(
            student_id="67123456",
            first_name_th="ลิซ่า",
            last_name_th="Blackpink",
            first_name_en="Lisa",
            last_name_en="Blackpink",
            faculty="วิทยาศาสตร์",
        )
        data = student.to_dict()
        assert "student_id" in data
        assert "full_name_th" in data
        assert "full_name_en" in data
