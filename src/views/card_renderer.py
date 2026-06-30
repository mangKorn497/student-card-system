"""CardRenderer: View layer สำหรับแสดงบัตรนักศึกษา (HTML / Text)."""

from ..models.student_card import StudentCard


class CardRenderer:
    """Renderer สำหรับแสดงบัตรนักศึกษา."""

    def __init__(self, card: StudentCard) -> None:
        self.card = card
        self.student = card.student

    def render_html(self) -> str:
        """สร้าง HTML สำหรับแสดงบัตร."""
        return f"""<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>บัตรนักศึกษา - {self.student.get_full_name_th()}</title>
<style>
{self._get_styles()}
</style>
</head>
<body>
<div class="card-container">
{self._render_front()}
{self._render_back()}
</div>
</body>
</html>
"""

    def _render_front(self) -> str:
        """ด้านหน้าบัตร."""
        return f"""
<div class="card-front">
    <div class="card-header">
        <div class="logo-section">
            <img src="assets/logo.png" alt="Logo" class="university-logo">
        </div>
        <div class="university-info">
            <h1 class="university-name-th">{self.student.university_th}</h1>
            <h2 class="university-name-en">{self.student.university_en}</h2>
        </div>
    </div>
    <div class="card-body">
        <div class="photo-section">
            <img src="{self.student.photo_path}" alt="Student Photo" class="student-photo">
        </div>
        <div class="info-section">
            <div class="info-row">
                <span class="label">ชื่อ-สกุล</span>
                <span class="separator">:</span>
                <span class="value">{self.student.get_prefix_th()} {self.student.get_full_name_th()}</span>
            </div>
            <div class="info-row">
                <span class="label">รหัสนักศึกษา</span>
                <span class="separator">:</span>
                <span class="value">{self.student.student_id}</span>
            </div>
            <div class="info-row">
                <span class="label">สาขาวิชา</span>
                <span class="separator">:</span>
                <span class="value">{self.student.faculty}</span>
            </div>
        </div>
        <div class="chip">
            <div class="chip-icon"></div>
        </div>
    </div>
    <div class="card-number">
        {self.card.formatted_card_number}
    </div>
    <div class="card-footer">
        <div class="student-name-en">
            {self.student.get_prefix_en()} {self.student.get_full_name_en()}
        </div>
        <div class="valid-thru">
            <span class="cvv">{self.card.cvv}</span>
            <div class="expire-info">
                <span class="label">VALID THRU</span>
                <span class="date">{self.card.expire_date_thai}</span>
            </div>
        </div>
        <div class="card-brand">
            <span class="visa-logo">{self.card.card_type}</span>
        </div>
        <div class="card-symbol">
            <div class="symbol-circles"></div>
        </div>
    </div>
    <div class="card-type-label">
        บัตรประจำตัวนักศึกษา
    </div>
</div>
"""

    def _render_back(self) -> str:
        """ด้านหลังบัตร."""
        return f"""
<div class="card-back">
    <div class="magnetic-strip"></div>
    <div class="signature-panel">
        <div class="signature-line"></div>
        <div class="signature-text">ลายมือชื่อผู้ถือบัตร</div>
    </div>
    <div class="barcode-section">
        <div class="barcode-placeholder">
            [BARCODE: {self.student.student_id}]
        </div>
        <div class="barcode-number">{self.student.student_id}</div>
    </div>
    <div class="back-decoration">
        <div class="flower-pattern"></div>
    </div>
</div>
"""

    def _get_styles(self) -> str:
        """CSS Styles."""
        return """
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
body {
    font-family: 'Sarabun', 'Arial', sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 20px;
}
.card-container {
    display: flex;
    flex-direction: column;
    gap: 30px;
}
.card-front, .card-back {
    width: 540px;
    height: 340px;
    border-radius: 15px;
    overflow: hidden;
    box-shadow: 0 20px 60px rgba(0,0,0,0.3);
    position: relative;
}
.card-front {
    background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 50%, #fecfef 100%);
}
.card-back {
    background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
}
.card-header {
    background: linear-gradient(90deg, #c0392b 0%, #e74c3c 50%, #ecf0f1 100%);
    padding: 15px;
    display: flex;
    align-items: center;
    gap: 15px;
    color: white;
}
.university-logo {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    background: white;
}
.university-name-th {
    font-size: 18px;
    font-weight: bold;
}
.university-name-en {
    font-size: 12px;
    margin-top: 3px;
}
.card-body {
    padding: 20px;
    display: flex;
    gap: 20px;
    margin-top: 10px;
}
.student-photo {
    width: 120px;
    height: 150px;
    object-fit: cover;
    border: 3px solid white;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
}
.info-section {
    flex: 1;
    font-size: 14px;
}
.info-row {
    margin-bottom: 10px;
    display: flex;
    align-items: center;
}
.info-row .label {
    font-weight: bold;
    width: 120px;
    color: #2c3e50;
}
.info-row .separator {
    margin: 0 10px;
    color: #7f8c8d;
}
.info-row .value {
    flex: 1;
    color: #34495e;
    font-weight: 500;
}
.chip {
    position: absolute;
    right: 20px;
    top: 120px;
}
.chip-icon {
    width: 50px;
    height: 35px;
    background: linear-gradient(135deg, #f1c40f 0%, #f39c12 100%);
    border-radius: 5px;
    border: 2px solid #d68910;
}
.card-number {
    text-align: center;
    font-size: 24px;
    font-weight: bold;
    color: #2c3e50;
    margin: 15px 0;
    letter-spacing: 2px;
    font-family: 'Courier New', monospace;
}
.card-footer {
    padding: 0 20px 15px;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
}
.student-name-en {
    font-size: 16px;
    font-weight: bold;
    color: #2c3e50;
    text-transform: uppercase;
}
.valid-thru {
    text-align: center;
    font-size: 12px;
}
.cvv {
    font-weight: bold;
    color: #2c3e50;
    font-size: 14px;
}
.expire-info .label {
    display: block;
    color: #7f8c8d;
    font-size: 10px;
}
.expire-info .date {
    font-weight: bold;
    color: #2c3e50;
    font-size: 14px;
}
.visa-logo {
    font-size: 32px;
    font-weight: bold;
    color: #1a1f71;
    font-style: italic;
}
.symbol-circles {
    width: 80px;
    height: 80px;
    border: 8px solid #e74c3c;
    border-radius: 50%;
    position: relative;
}
.symbol-circles::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 50px;
    height: 50px;
    border: 8px solid #c0392b;
    border-radius: 50%;
}
.card-type-label {
    background: linear-gradient(90deg, #c0392b, #e74c3c);
    color: white;
    text-align: center;
    padding: 8px;
    font-weight: bold;
    font-size: 14px;
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
}
.magnetic-strip {
    height: 50px;
    background: #000;
    margin-top: 20px;
}
.signature-panel {
    margin: 20px;
    padding: 15px;
    background: white;
    border-radius: 5px;
}
.signature-line {
    border-bottom: 2px dashed #bdc3c7;
    height: 40px;
    margin-bottom: 5px;
}
.signature-text {
    text-align: right;
    font-size: 12px;
    color: #7f8c8d;
}
.barcode-section {
    text-align: center;
    margin: 20px;
    padding: 10px;
    background: white;
    border-radius: 5px;
}
.barcode-placeholder {
    font-family: 'Courier New', monospace;
    font-size: 12px;
    padding: 10px;
}
.barcode-number {
    margin-top: 5px;
    font-family: 'Courier New', monospace;
    font-size: 14px;
}
.flower-pattern {
    position: absolute;
    bottom: 10px;
    left: 10px;
    width: 80px;
    height: 80px;
    background: radial-gradient(circle, #e74c3c 20%, transparent 20%);
    background-size: 30px 30px;
    opacity: 0.3;
}
@media print {
    body {
        background: white;
    }
    .card-front, .card-back {
        box-shadow: none;
        page-break-inside: avoid;
    }
}
"""

    def render_text(self) -> str:
        """แสดงข้อมูลบัตรแบบ text."""
        status = "VALID" if self.card.is_valid() else "EXPIRED"
        lines = [
            "=" * 60,
            f" บัตรนักศึกษา - {self.student.university_th}",
            "=" * 60,
            f" ชื่อ-สกุล    : {self.student.get_full_name_th()}",
            f" Name        : {self.student.get_full_name_en()}",
            f" รหัสนักศึกษา : {self.student.student_id}",
            f" สาขาวิชา    : {self.student.faculty}",
            "-" * 60,
            f" Card Number : {self.card.formatted_card_number}",
            f" CVV         : {self.card.cvv}",
            f" Valid Thru  : {self.card.expire_date_thai}",
            f" Status      : {status}",
            "=" * 60,
        ]
        return "\n".join(lines)
