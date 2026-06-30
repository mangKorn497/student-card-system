"""StudentCard entity: บัตรนักศึกษาที่ประกอบด้วย Student (Composition)."""

import random
from dataclasses import dataclass, field
from datetime import datetime, timedelta

from .student import Student


@dataclass
class StudentCard:
    """Entity สำหรับบัตรนักศึกษา."""

    student: Student
    card_number: str = field(
        default_factory=lambda: StudentCard._generate_card_number()
    )
    cvv: str = field(default_factory=lambda: StudentCard._generate_cvv())
    issue_date: datetime = field(default_factory=datetime.now)
    expire_years: int = 4
    card_type: str = "VISA"

    @staticmethod
    def _generate_card_number() -> str:
        """สร้างหมายเลขบัตร 16 หลัก (จัดรูปแบบเป็น 4 กลุ่ม)."""
        prefix = "1234"
        middle = f"{random.randint(1000, 9999)}"
        random1 = f"{random.randint(1000, 9999)}"
        random2 = f"{random.randint(1000, 9999)}"
        return f"{prefix} {middle} {random1} {random2}"

    @staticmethod
    def _generate_cvv() -> str:
        """สร้าง CVV 3 หลัก."""
        return f"{random.randint(100, 999)}"

    @property
    def expire_date(self) -> datetime:
        """คำนวณวันหมดอายุ."""
        return self.issue_date + timedelta(days=self.expire_years * 365)

    @property
    def expire_date_thai(self) -> str:
        """วันหมดอายุรูปแบบ พ.ศ. (MM/YY) เช่น 06/73."""
        thai_year_short = (self.expire_date.year + 543) % 100
        return f"{self.expire_date.strftime('%m')}/{thai_year_short:02d}"

    @property
    def formatted_card_number(self) -> str:
        """หมายเลขบัตรแบบจัดรูปแบบ."""
        return self.card_number

    def is_expired(self) -> bool:
        """ตรวจสอบว่าบัตรหมดอายุหรือไม่."""
        return datetime.now() > self.expire_date

    def is_valid(self) -> bool:
        """ตรวจสอบว่าบัตรยังใช้ได้หรือไม่."""
        return not self.is_expired()

    def get_days_until_expire(self) -> int:
        """จำนวนวันก่อนหมดอายุ."""
        delta = self.expire_date - datetime.now()
        return max(0, delta.days)

    def to_dict(self) -> dict:
        """แปลงข้อมูลเป็น dictionary."""
        return {
            "card_number": self.card_number,
            "cvv": self.cvv,
            "issue_date": self.issue_date.isoformat(),
            "expire_date": self.expire_date.isoformat(),
            "expire_date_thai": self.expire_date_thai,
            "card_type": self.card_type,
            "is_valid": self.is_valid(),
            "days_until_expire": self.get_days_until_expire(),
            "student": self.student.to_dict(),
        }

    def __str__(self) -> str:
        return f"Card({self.card_number} - {self.student.student_id})"

    def __repr__(self) -> str:
        return self.__str__()
