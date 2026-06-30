# ระบบแสดงบัตรนักศึกษา (Student Card System)

ระบบแสดง/จัดการบัตรนักศึกษา พัฒนาด้วย **Python OOP** ตามกระบวนการ **SDLC** แบบครบวงจร
(Requirements → Design → Implementation → Testing → Deployment → Maintenance)

สร้างจากสเปกในเอกสาร `python_oop.pdf`

## คุณสมบัติ (Features)

- เก็บข้อมูลนักศึกษา (ไทย/อังกฤษ), รหัสนักศึกษา, สาขาวิชา, รูปถ่าย
- สร้างบัตรพร้อมหมายเลขบัตร 16 หลัก, CVV, วันหมดอายุแบบ พ.ศ.
- ตรวจสอบความถูกต้องของบัตร (รวม Luhn Algorithm)
- คำนวณวันหมดอายุ / สถานะบัตร (ยังใช้ได้ / หมดอายุ)
- แสดงบัตรเป็น **HTML** (ด้านหน้า + ด้านหลัง) และเป็น **Text**
- จัดการบัตรหลายใบและดูสถิติผ่าน Service layer

## หลักการ OOP ที่ใช้

1. **Encapsulation** – ซ่อนข้อมูลด้วย private attribute (`_cards`)
2. **Abstraction** – แยกชั้น Model / Service / View
3. **Composition** – `StudentCard` มี `Student` เป็นส่วนประกอบ
4. **Polymorphism** – interface สำหรับ render หลายรูปแบบ (`render_html`, `render_text`)
5. **Dataclass** + **Type Hints** – เพื่อความชัดเจนของโค้ด

## โครงสร้างโปรเจกต์

```
student_card_system/
├── src/
│   ├── models/        # Student, StudentCard
│   ├── services/      # CardService, CardValidator
│   ├── views/         # CardRenderer
│   └── utils/         # ThaiDate
├── templates/         # student_card.html (Jinja2)
├── tests/             # pytest
├── assets/            # logo.png, photos/
├── main.py
├── requirements.txt
├── requirements-dev.txt
├── pyproject.toml
├── Dockerfile
└── README.md
```

## การติดตั้งและรัน

```bash
# (แนะนำ) สร้าง virtual environment
python3 -m venv .venv && source .venv/bin/activate

# ติดตั้ง dependency แบบเต็ม
pip install -r requirements.txt
# หรือแบบขั้นต่ำ (พอสำหรับรันระบบ + เทสต์)
pip install -r requirements-dev.txt

# รันระบบ (สร้างไฟล์ student_card.html)
python main.py

# รันเทสต์
pytest tests/ -v

# รันเทสต์พร้อม coverage
pytest tests/ --cov=src --cov-report=html
```

เปิดไฟล์ `student_card.html` ในเบราว์เซอร์เพื่อดูบัตรที่สร้างขึ้น

## รันด้วย Docker

```bash
docker build -t student-card-system .
docker run --rm student-card-system
```

## แนวทางต่อยอด (Maintenance)

1. เพิ่ม Database Integration (SQLite/PostgreSQL + SQLAlchemy)
2. เพิ่ม REST API (FastAPI/Flask)
3. เพิ่ม QR Code บนบัตร
4. เพิ่มระบบพิมพ์บัตร (ReportLab/WeasyPrint)
5. เพิ่ม Authentication (JWT/OAuth2)
6. เพิ่มระบบแจ้งเตือนบัตรใกล้หมดอายุ
7. เพิ่ม Admin Dashboard
