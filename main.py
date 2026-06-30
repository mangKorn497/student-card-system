"""Entry point: สร้างและแสดงบัตรนักศึกษา."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from src.services.card_service import CardService  # noqa: E402
from src.views.card_renderer import CardRenderer  # noqa: E402


def main() -> None:
    """ฟังก์ชันหลัก."""
    print("=" * 60)
    print("ระบบจัดการบัตรนักศึกษา - มหาวิทยาลัยราชภัฏนครปฐม")
    print("=" * 60)

    # สร้าง Service
    service = CardService()

    # สร้างข้อมูลนักศึกษา (ตัวอย่างจากบัตร)
    student_data = {
        "student_id": "67123456",
        "first_name_th": "ลิซ่า",
        "last_name_th": "Blackpink",
        "first_name_en": "Lisa",
        "last_name_en": "Blackpink",
        "faculty": "คณะวิทยาศาสตร์และเทคโนโลยี",
        "photo_path": "assets/photos/lisa.jpg",
    }

    # สร้างนักศึกษา
    student = service.create_student(**student_data)
    print(f"\n[OK] สร้างนักศึกษา: {student}")

    # สร้างบัตร
    card = service.create_card(student, expire_years=4, card_type="VISA")
    print(f"[OK] สร้างบัตร: {card}")

    # ตรวจสอบบัตร
    validation = service.validate_card(card)
    print("\nผลการตรวจสอบบัตร:")
    print(f"  Valid: {validation['is_valid']}")
    if validation["errors"]:
        print(f"  Errors: {validation['errors']}")
    if validation["warnings"]:
        print(f"  Warnings: {validation['warnings']}")

    # แสดงข้อมูลบัตร
    print("\nข้อมูลบัตร:")
    print(f"  Card Number: {card.formatted_card_number}")
    print(f"  CVV: {card.cvv}")
    print(f"  Issue Date: {card.issue_date.strftime('%d/%m/%Y')}")
    print(f"  Expire Date: {card.expire_date_thai}")
    print(f"  Days Until Expire: {card.get_days_until_expire()}")

    # แสดงบัตรแบบ text
    renderer = CardRenderer(card)
    print(f"\n{renderer.render_text()}")

    # สร้างไฟล์ HTML
    html_content = renderer.render_html()
    output_file = "student_card.html"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"\n[OK] สร้างไฟล์ HTML: {output_file}")

    # สถิติ
    stats = service.get_statistics()
    print("\nสถิติ:")
    print(f"  Total Cards: {stats['total_cards']}")
    print(f"  Active Cards: {stats['active_cards']}")
    print(f"  Expired Cards: {stats['expired_cards']}")


if __name__ == "__main__":
    main()
