"""ThaiDate: Utility สำหรับจัดการวันที่แบบไทย (พ.ศ.)."""

from datetime import datetime


class ThaiDate:
    """Utility สำหรับจัดการวันที่แบบไทย."""

    THAI_MONTHS = [
        "มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน",
        "พฤษภาคม", "มิถุนายน", "กรกฎาคม", "สิงหาคม",
        "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม",
    ]

    @staticmethod
    def to_thai_year(year: int) -> int:
        """แปลง ค.ศ. เป็น พ.ศ."""
        return year + 543

    @staticmethod
    def to_buddhist_year(year: int) -> int:
        """แปลง ค.ศ. เป็น พ.ศ. (แบบย่อ 2 หลัก)."""
        return year + 543 - 2500

    @staticmethod
    def format_thai_date(date: datetime, format_type: str = "full") -> str:
        """จัดรูปแบบวันที่ภาษาไทย."""
        thai_year = ThaiDate.to_thai_year(date.year)
        month_name = ThaiDate.THAI_MONTHS[date.month - 1]

        if format_type == "full":
            return f"{date.day} {month_name} {thai_year}"
        elif format_type == "short":
            return f"{date.day}/{date.month}/{thai_year}"
        elif format_type == "card":
            return f"{date.strftime('%m')}/{ThaiDate.to_buddhist_year(date.year)}"
        return str(date)
