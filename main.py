"""Entry point: สร้างและแสดงบัตรนักศึกษา.

ตัวอย่างการใช้งาน:
    python main.py                         # ใช้ข้อมูลตัวอย่าง (ลิซ่า)
    python main.py --photo assets/photos/me.jpg
    python main.py --first-th สมชาย --last-th ใจดี \\
        --first-en Somchai --last-en Jaidee \\
        --student-id 67123456 --faculty "คณะวิทยาศาสตร์" \\
        --photo assets/photos/me.jpg
    python main.py --no-open                # ไม่ต้องเปิดเบราว์เซอร์อัตโนมัติ
"""

import argparse
import sys
import webbrowser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from src.services.card_service import CardService  # noqa: E402
from src.views.card_renderer import CardRenderer  # noqa: E402


def parse_args() -> argparse.Namespace:
    """อ่าน argument จาก command line (มีค่าตั้งต้นเป็นข้อมูลตัวอย่าง)."""
    parser = argparse.ArgumentParser(
        description="สร้างบัตรนักศึกษา (HTML) จากข้อมูลที่กำหนด"
    )
    parser.add_argument("--student-id", default="674259002", help="รหัสนักศึกษา")
    parser.add_argument("--first-th", default="ชญานนท์", help="ชื่อ (ไทย)")
    parser.add_argument("--last-th", default="อารีย์", help="สกุล (ไทย)")
    parser.add_argument("--first-en", default="Chayanon", help="ชื่อ (อังกฤษ)")
    parser.add_argument("--last-en", default="Aree", help="สกุล (อังกฤษ)")
    parser.add_argument(
        "--faculty", default="คณะวิทยาศาสตร์และเทคโนโลยี", help="สาขาวิชา/คณะ"
    )
    parser.add_argument(
        "--photo",
        default="assets/photos/default.jpg",
        help="path ของรูปถ่าย (ใส่รูปตัวเองได้)",
    )
    parser.add_argument("--prefix-th", default="นาย", help="คำนำหน้า (ไทย)")
    parser.add_argument("--prefix-en", default="MR", help="คำนำหน้า (อังกฤษ)")
    parser.add_argument(
        "--output", default="student_card.html", help="ชื่อไฟล์ HTML ที่จะสร้าง"
    )
    parser.add_argument(
        "--no-open",
        action="store_true",
        help="ไม่ต้องเปิดไฟล์ในเบราว์เซอร์อัตโนมัติ",
    )
    return parser.parse_args()


def main() -> None:
    """ฟังก์ชันหลัก."""
    args = parse_args()

    print("=" * 60)
    print("ระบบจัดการบัตรนักศึกษา - มหาวิทยาลัยราชภัฏนครปฐม")
    print("=" * 60)

    # เตือนถ้าหารูปไม่เจอ (จะยังสร้างบัตรได้ แต่รูปจะไม่ขึ้น)
    if not Path(args.photo).exists():
        print(f"\n[!] หารูปไม่เจอ: {args.photo}")
        print("    วางไฟล์รูปไว้ในโฟลเดอร์ assets/photos/ แล้วระบุด้วย --photo")

    # สร้าง Service
    service = CardService()

    # สร้างข้อมูลนักศึกษา
    student = service.create_student(
        student_id=args.student_id,
        first_name_th=args.first_th,
        last_name_th=args.last_th,
        first_name_en=args.first_en,
        last_name_en=args.last_en,
        faculty=args.faculty,
        photo_path=args.photo,
        prefix_th=args.prefix_th,
        prefix_en=args.prefix_en,
    )
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
    output_path = Path(args.output).resolve()
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"\n[OK] สร้างไฟล์ HTML: {output_path}")

    # สถิติ
    stats = service.get_statistics()
    print("\nสถิติ:")
    print(f"  Total Cards: {stats['total_cards']}")
    print(f"  Active Cards: {stats['active_cards']}")
    print(f"  Expired Cards: {stats['expired_cards']}")

    # เปิดบัตรในเบราว์เซอร์อัตโนมัติ
    if not args.no_open:
        webbrowser.open(output_path.as_uri())
        print("\n[OK] เปิดบัตรในเบราว์เซอร์แล้ว (ถ้าไม่ขึ้น เปิดไฟล์ HTML เองได้)")


if __name__ == "__main__":
    main()
