from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape, A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas
from reportlab.lib.utils import simpleSplit
from reportlab.lib.units import mm

OUTPUT = "04-workflow-diagram.pdf"
PAGE_W, PAGE_H = landscape(A4)

font_path = "C:/Windows/Fonts/arial.ttf"
try:
    pdfmetrics.registerFont(TTFont("Arial", font_path))
    FONT = "Arial"
except OSError:
    FONT = "Helvetica"

c = canvas.Canvas(OUTPUT, pagesize=(PAGE_W, PAGE_H))
margin = 13 * mm

# Background and title
c.setFillColor(colors.HexColor("#F8FAFC"))
c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
c.setFillColor(colors.HexColor("#0F172A"))
c.setFont(FONT, 19)
c.drawString(margin, PAGE_H - margin, "Current-State Workflow - Dieu phoi lai chuyen Xanh SM")
c.setFont(FONT, 9)
c.setFillColor(colors.HexColor("#475569"))
c.drawString(margin, PAGE_H - margin - 17, "Bai toan: tai xe huy hoac khong nhan cuoc | Tong thoi gian xu ly uoc tinh: khoang 5 phut/luot")

# Flow nodes
node_y = PAGE_H - 103
node_h = 52
nodes = [
    ("1", "He thong phat hien", "Tai xe huy / timeout", "Duoi 10 giay", "#E0F2FE", "#0369A1", 76),
    ("2", "HANDOFF", "Canh bao -> dieu phoi vien", "Khoang 30 giay", "#FFF7ED", "#C2410C", 86),
    ("3", "Kiem tra chuyen", "Vi tri, trang thai, loai xe", "Khoang 1 phut", "#E0F2FE", "#0369A1", 91),
    ("4", "BOTTLENECK", "Tim va lien he tai xe thay the", "Khoang 2-3 phut", "#FEE2E2", "#B91C1C", 105),
    ("5", "HANDOFF", "Tai xe xac nhan nhan chuyen", "Phu thuoc phan hoi", "#FFF7ED", "#C2410C", 94),
    ("6", "Cap nhat chuyen", "Bao khach hang", "Khoang 30 giay", "#E0F2FE", "#0369A1", 82),
]

def draw_node(x, data):
    number, title, body, time, fill, stroke, width = data
    c.setFillColor(colors.HexColor(fill))
    c.setStrokeColor(colors.HexColor(stroke))
    c.setLineWidth(2.2 if number == "4" else 1.2)
    c.roundRect(x, node_y, width, node_h, 6, stroke=1, fill=1)
    c.setFillColor(colors.HexColor(stroke))
    c.setFont(FONT, 8.5)
    c.drawCentredString(x + width / 2, node_y + node_h - 13, f"{number}. {title}")
    c.setFillColor(colors.HexColor("#1E293B"))
    c.setFont(FONT, 7.3)
    lines = simpleSplit(body, FONT, 7.3, width - 10)
    for i, line in enumerate(lines[:2]):
        c.drawCentredString(x + width / 2, node_y + node_h - 26 - i * 9, line)
    c.setFillColor(colors.HexColor(stroke))
    c.setFont(FONT, 7)
    c.drawCentredString(x + width / 2, node_y + 7, time)
    return width

x = margin
for index, data in enumerate(nodes):
    width = draw_node(x, data)
    if index < len(nodes) - 1:
        next_x = x + width + 7
        c.setStrokeColor(colors.HexColor("#64748B"))
        c.setLineWidth(1.2)
        c.line(x + width, node_y + node_h / 2, next_x - 2, node_y + node_h / 2)
        c.line(next_x - 5, node_y + node_h / 2 + 3, next_x - 2, node_y + node_h / 2)
        c.line(next_x - 5, node_y + node_h / 2 - 3, next_x - 2, node_y + node_h / 2)
    x += width + 7

# Exception and fallback paths
fallback_y = node_y - 59
c.setStrokeColor(colors.HexColor("#CA8A04"))
c.setFillColor(colors.HexColor("#FEFCE8"))
c.setLineWidth(1.2)
c.roundRect(PAGE_W - margin - 205, fallback_y, 205, 38, 5, stroke=1, fill=1)
c.setFillColor(colors.HexColor("#854D0E"))
c.setFont(FONT, 8)
c.drawString(PAGE_W - margin - 195, fallback_y + 24, "FALLBACK THU CONG")
c.setFillColor(colors.HexColor("#713F12"))
c.setFont(FONT, 7.2)
c.drawString(PAGE_W - margin - 195, fallback_y + 11, "Khong co tai xe phu hop -> dieu phoi vien xu ly tiep")

# Dashed line from bottleneck area to fallback
c.setDash(3, 2)
c.setStrokeColor(colors.HexColor("#CA8A04"))
bottleneck_x = margin + nodes[0][6] + 7 + nodes[1][6] + 7 + nodes[2][6] + 7
bottleneck_x += nodes[3][6] / 2
c.line(bottleneck_x, node_y, PAGE_W - margin - 205 / 2, fallback_y + 38)
c.setDash()

# Legend
legend_y = 105
c.setFillColor(colors.HexColor("#0F172A"))
c.setFont(FONT, 10)
c.drawString(margin, legend_y + 43, "Chu giai")
legend = [
    ("#FFF7ED", "#C2410C", "🔄 HANDOFF: Chuyen giao giua he thong, dieu phoi vien va tai xe"),
    ("#FEE2E2", "#B91C1C", "🔴 BOTTLENECK: Tim va lien he tai xe thay the"),
    ("#FEFCE8", "#CA8A04", "Fallback: Quay ve quy trinh thu cong khi du lieu loi / khong du tin cay"),
]
for i, (fill, stroke, text) in enumerate(legend):
    y = legend_y + 25 - i * 16
    c.setFillColor(colors.HexColor(fill))
    c.setStrokeColor(colors.HexColor(stroke))
    c.roundRect(margin, y - 4, 11, 10, 2, stroke=1, fill=1)
    c.setFillColor(colors.HexColor("#334155"))
    c.setFont(FONT, 7.5)
    c.drawString(margin + 17, y, text)

# Timing table
x_table = PAGE_W - margin - 255
table_top = legend_y + 43
c.setFillColor(colors.HexColor("#0F172A"))
c.setFont(FONT, 10)
c.drawString(x_table, table_top, "Thoi gian van hanh")
rows = [
    ("Phat hien + handoff", "Duoi 40 giay"),
    ("Kiem tra thong tin", "Khoang 1 phut"),
    ("Tim va lien he thay the", "Khoang 2-3 phut"),
    ("Cap nhat + bao khach", "Khoang 30 giay"),
    ("TONG CONG", "Khoang 5 phut/luot"),
]
row_y = table_top - 15
for i, (label, value) in enumerate(rows):
    if i == len(rows) - 1:
        c.setFillColor(colors.HexColor("#DBEAFE"))
        c.rect(x_table - 4, row_y - 3, 255, 14, stroke=0, fill=1)
    c.setFillColor(colors.HexColor("#334155"))
    c.setFont(FONT, 7.5 if i < len(rows) - 1 else 8)
    c.drawString(x_table, row_y, label)
    c.drawRightString(x_table + 245, row_y, value)
    row_y -= 15

c.setFillColor(colors.HexColor("#64748B"))
c.setFont(FONT, 6.5)
c.drawString(margin, 22, "So lieu la uoc tinh scoping; can doi chieu voi log van hanh thuc te truoc khi trien khai.")
c.save()
print(f"Created {OUTPUT}")
