"""CardValidator: ตรวจสอบความถูกต้องของบัตรนักศึกษา."""

from typing import Any, Dict

from ..models.student_card import StudentCard


class CardValidator:
    """Validator สำหรับตรวจสอบความถูกต้องของบัตร."""

    @staticmethod
    def validate_card(card: StudentCard) -> Dict[str, Any]:
        """ตรวจสอบบัตรทั้งหมด."""
        errors = []
        warnings = []

        # ตรวจสอบข้อมูลนักศึกษา
        if not card.student.student_id:
            errors.append("รหัสนักศึกษาว่างเปล่า")
        elif len(card.student.student_id) < 8:
            errors.append("รหัสนักศึกษาต้องมีความยาวอย่างน้อย 8 หลัก")

        if not card.student.first_name_th or not card.student.last_name_th:
            errors.append("ชื่อ-สกุล ภาษาไทยไม่ครบถ้วน")

        if not card.student.first_name_en or not card.student.last_name_en:
            errors.append("ชื่อ-สกุล ภาษาอังกฤษไม่ครบถ้วน")

        # ตรวจสอบบัตร
        if not card.card_number:
            errors.append("หมายเลขบัตรว่างเปล่า")
        else:
            card_digits = card.card_number.replace(" ", "")
            if len(card_digits) != 16:
                errors.append("หมายเลขบัตรต้องมีความยาว 16 หลัก")

        if card.is_expired():
            errors.append("บัตรหมดอายุแล้ว")
        elif card.get_days_until_expire() < 30:
            warnings.append("บัตรจะหมดอายุในอีก 30 วัน")

        return {
            "is_valid": len(errors) == 0,
            "errors": errors,
            "warnings": warnings,
        }

    @staticmethod
    def validate_card_number(card_number: str) -> bool:
        """ตรวจสอบรูปแบบหมายเลขบัตร (Luhn Algorithm)."""
        digits = card_number.replace(" ", "")
        if not digits.isdigit() or len(digits) != 16:
            return False

        total = 0
        reverse_digits = digits[::-1]
        for i, digit in enumerate(reverse_digits):
            n = int(digit)
            if i % 2 == 1:
                n *= 2
                if n > 9:
                    n -= 9
            total += n
        return total % 10 == 0
