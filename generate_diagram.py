import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.font_manager import FontProperties

def create_workflow_diagram():
    # Set high DPI and figure dimensions (wide canvas 16:9 ratio)
    fig, ax = plt.subplots(figsize=(19, 10.5), dpi=300)
    fig.patch.set_facecolor('#F8FAFC')  # Slate-50 background
    ax.set_facecolor('#F8FAFC')
    ax.set_xlim(0, 19)
    ax.set_ylim(0, 10.5)
    ax.axis('off')

    # Fonts
    font_family = 'Segoe UI'
    title_font = FontProperties(family=font_family, size=21, weight='bold')
    subtitle_font = FontProperties(family=font_family, size=11.5, weight='normal')
    step_num_font = FontProperties(family=font_family, size=10.5, weight='bold')
    step_title_font = FontProperties(family=font_family, size=12.5, weight='bold')
    body_font = FontProperties(family=font_family, size=10, weight='normal')
    body_bold = FontProperties(family=font_family, size=10, weight='bold')
    metric_font = FontProperties(family=font_family, size=11, weight='bold')

    # 1. Header Section
    # Title & Subtitle
    ax.text(0.8, 9.8, "CURRENT-STATE WORKFLOW: QUY TRÌNH XỬ LÝ SỰ CỐ CẠN PIN THỰC ĐỊA", 
            fontproperties=title_font, color='#0F172A')
    ax.text(0.8, 9.35, "Trung tâm Điều vận Taxi điện Xanh SM (GSM) • Phân tích hiện trạng vận hành thủ công trước khi ứng dụng AI", 
            fontproperties=subtitle_font, color='#475569')

    # Total Time KPI Banner
    bbox_time = patches.FancyBboxPatch((13.8, 9.15), 4.4, 0.85,
                                      boxstyle="round,pad=0.1,rounding_size=0.15",
                                      facecolor='#FEF2F2', edgecolor='#EF4444', linewidth=1.6)
    ax.add_patch(bbox_time)
    
    # Red bullet indicator
    time_circle = patches.Circle((14.2, 9.57), 0.12, facecolor='#DC2626', edgecolor='none')
    ax.add_patch(time_circle)
    ax.text(14.45, 9.57, "TỔNG THỜI GIAN: 15 PHÚT / LƯỢT", 
            fontproperties=metric_font, color='#991B1B', va='center')
    ax.text(16.0, 9.32, "Thiệt hại: ~20h công/ngày (80 ca/ngày) • Tốn ~15% doanh thu", 
            fontproperties=FontProperties(family=font_family, size=8.5), color='#B91C1C', ha='center', va='center')

    # 2. Main Steps (1 to 4) - Top Lane
    steps = [
        {
            "num": "BƯỚC 1",
            "title": "Tiếp nhận thông tin",
            "actor": "Điều phối viên (Dispatcher)",
            "time": "2 phút",
            "in": "Hotline / In-App tài xế báo cạn pin",
            "out": "Phiếu ghi nhận sự cố (Log)",
            "bottleneck": False,
            "x": 0.8, "y": 4.8, "w": 3.9, "h": 3.9,
            "theme": "normal"
        },
        {
            "num": "BƯỚC 2",
            "title": "Tra cứu định vị & Pin",
            "actor": "Điều phối viên (Dispatcher)",
            "time": "2 phút",
            "in": "Biển số xe / ID tài xế",
            "out": "Tọa độ GPS, Mức pin SoC (%)",
            "bottleneck": False,
            "x": 5.2, "y": 4.8, "w": 3.9, "h": 3.9,
            "theme": "normal"
        },
        {
            "num": "BƯỚC 3",
            "title": "Tìm trạm sạc VinFast",
            "actor": "Điều phối viên (Dispatcher)",
            "time": "5 phút (CHẬM)",
            "in": "Tọa độ GPS + Cổng sạc CCS2",
            "out": "Trạm sạc trống & khoảng cách",
            "bottleneck": True,
            "bn_tag": "BOTTLENECK #1 (ĐIỂM NGHẼN)",
            "bottleneck_desc": "Mở dashboard mạng lưới trụ sạc riêng, tra cứu thủ công từng trạm lân cận còn trụ trống tương thích.",
            "x": 9.6, "y": 4.8, "w": 4.1, "h": 3.9,
            "theme": "danger"
        },
        {
            "num": "BƯỚC 4",
            "title": "Soạn tin nhắn chỉ đường",
            "actor": "Điều phối viên (Dispatcher)",
            "time": "5 phút (CHẬM)",
            "in": "Thông tin địa chỉ trạm sạc",
            "out": "SMS / Chat text hướng dẫn tài xế",
            "bottleneck": True,
            "bn_tag": "BOTTLENECK #2 (ĐIỂM NGHẼN)",
            "bottleneck_desc": "Tự gõ tay toàn bộ tin nhắn SMS chỉ đường và khuyến cáo an toàn; dễ sai sót khi tài xế hoảng loạn.",
            "x": 14.2, "y": 4.8, "w": 4.1, "h": 3.9,
            "theme": "danger"
        }
    ]

    for s in steps:
        is_danger = s["theme"] == "danger"
        card_bg = '#FFF1F2' if is_danger else '#FFFFFF'
        border_color = '#F43F5E' if is_danger else '#CBD5E1'
        border_width = 2.0 if is_danger else 1.2

        # Card body
        card = patches.FancyBboxPatch((s["x"], s["y"]), s["w"], s["h"],
                                     boxstyle="round,pad=0.1,rounding_size=0.18",
                                     facecolor=card_bg, edgecolor=border_color, linewidth=border_width)
        ax.add_patch(card)

        # Card header banner
        header_color = '#FFE4E6' if is_danger else '#F1F5F9'
        step_header = patches.FancyBboxPatch((s["x"] + 0.12, s["y"] + s["h"] - 0.75), s["w"] - 0.24, 0.65,
                                            boxstyle="round,pad=0.06,rounding_size=0.12",
                                            facecolor=header_color, edgecolor='none')
        ax.add_patch(step_header)

        # Step Number badge
        num_color = '#BE123C' if is_danger else '#0284C7'
        ax.text(s["x"] + 0.3, s["y"] + s["h"] - 0.42, s["num"], 
                fontproperties=step_num_font, color=num_color, va='center')
        
        # Time badge inside header
        time_pill = patches.FancyBboxPatch((s["x"] + s["w"] - 1.65, s["y"] + s["h"] - 0.62), 1.45, 0.4,
                                          boxstyle="round,pad=0.04,rounding_size=0.08",
                                          facecolor='#FECDD3' if is_danger else '#E0F2FE',
                                          edgecolor='#FDA4AF' if is_danger else '#BAE6FD', linewidth=0.8)
        ax.add_patch(time_pill)
        ax.text(s["x"] + s["w"] - 0.92, s["y"] + s["h"] - 0.42, s["time"],
                fontproperties=FontProperties(family=font_family, size=9.0, weight='bold'),
                color='#BE123C' if is_danger else '#0369A1', ha='center', va='center')

        # Step Title
        ax.text(s["x"] + 0.3, s["y"] + s["h"] - 1.12, s["title"],
                fontproperties=step_title_font, color='#0F172A', va='center')

        # Details
        curr_y = s["y"] + s["h"] - 1.55
        line_spacing = 0.30

        # Operator
        ax.text(s["x"] + 0.3, curr_y, "Nhân sự:", fontproperties=body_bold, color='#334155')
        ax.text(s["x"] + 1.25, curr_y, s["actor"], fontproperties=body_font, color='#475569')
        curr_y -= line_spacing

        # Input
        ax.text(s["x"] + 0.3, curr_y, "Đầu vào:", fontproperties=body_bold, color='#334155')
        ax.text(s["x"] + 1.25, curr_y, s["in"], fontproperties=body_font, color='#475569')
        curr_y -= line_spacing

        # Output
        ax.text(s["x"] + 0.3, curr_y, "Đầu ra:", fontproperties=body_bold, color='#334155')
        ax.text(s["x"] + 1.25, curr_y, s["out"], fontproperties=body_font, color='#475569')
        curr_y -= line_spacing + 0.08

        # Bottleneck warning box if danger
        if is_danger and "bottleneck_desc" in s:
            bn_box = patches.FancyBboxPatch((s["x"] + 0.18, s["y"] + 0.18), s["w"] - 0.36, 1.2,
                                           boxstyle="round,pad=0.06,rounding_size=0.1",
                                           facecolor='#FFE4E6', edgecolor='#F43F5E', linewidth=1.4, linestyle='--')
            ax.add_patch(bn_box)
            
            # Bottleneck tag
            bn_dot = patches.Circle((s["x"] + 0.42, s["y"] + 1.12), 0.1, facecolor='#E11D48', edgecolor='none')
            ax.add_patch(bn_dot)
            ax.text(s["x"] + 0.62, s["y"] + 1.12, s["bn_tag"],
                    fontproperties=FontProperties(family=font_family, size=8.5, weight='bold'),
                    color='#9F1239', va='center')
            
            # Text description
            ax.text(s["x"] + 0.3, s["y"] + 0.62, s["bottleneck_desc"],
                    fontproperties=FontProperties(family=font_family, size=8.2),
                    color='#881337', va='center')

    # Connecting Arrows between Steps 1 -> 2, 2 -> 3, 3 -> 4
    for i in range(3):
        start_x = steps[i]["x"] + steps[i]["w"] + 0.05
        end_x = steps[i+1]["x"] - 0.05
        y_pos = 6.75
        arrow = patches.FancyArrowPatch((start_x, y_pos), (end_x, y_pos),
                                       arrowstyle='simple,head_width=8,head_length=8',
                                       color='#64748B', linewidth=1.2)
        ax.add_patch(arrow)

    # 3. Decision & Handoff Section (Bottom Lane)
    # Arrow from Step 4 down to Decision Box
    arrow_down = patches.FancyArrowPatch((16.25, 4.8), (16.25, 3.65),
                                        arrowstyle='simple,head_width=8,head_length=8',
                                        color='#BE123C', linewidth=1.4)
    ax.add_patch(arrow_down)
    
    # Decision Box: "Kiểm tra mức pin xe"
    cond_box = patches.FancyBboxPatch((14.4, 2.4), 3.7, 1.25,
                                     boxstyle="round,pad=0.08,rounding_size=0.15",
                                     facecolor='#FEF3C7', edgecolor='#F59E0B', linewidth=1.6)
    ax.add_patch(cond_box)
    
    warn_dot = patches.Circle((14.8, 3.25), 0.12, facecolor='#D97706', edgecolor='none')
    ax.add_patch(warn_dot)
    ax.text(15.05, 3.25, "ĐIỀU KIỆN PIN NGUY CẤP?",
            fontproperties=FontProperties(family=font_family, size=10, weight='bold'),
            color='#92400E', va='center')
    ax.text(16.25, 2.85, "Nếu Pin xe < 5% hoặc xe đã dừng giữa đường,\nkhông đủ pin tự lăn bánh về trạm sạc",
            fontproperties=FontProperties(family=font_family, size=8.5),
            color='#78350F', ha='center', va='center')

    # Arrow from Decision to Step 5 (Handoff)
    arrow_handoff = patches.FancyArrowPatch((14.4, 3.0), (11.8, 3.0),
                                           arrowstyle='simple,head_width=9,head_length=9',
                                           color='#D97706', linewidth=1.4)
    ax.add_patch(arrow_handoff)
    
    branch_tag = patches.FancyBboxPatch((12.1, 3.15), 1.9, 0.42,
                                       boxstyle="round,pad=0.04,rounding_size=0.08",
                                       facecolor='#FDE68A', edgecolor='#D97706', linewidth=1.0)
    ax.add_patch(branch_tag)
    ax.text(13.05, 3.36, "CÓ (Pin < 5%)", fontproperties=FontProperties(family=font_family, size=8.5, weight='bold'),
            color='#92400E', ha='center', va='center')

    # Step 5: Handoff Card
    s5_x, s5_y, s5_w, s5_h = 4.4, 1.1, 7.3, 3.1
    handoff_card = patches.FancyBboxPatch((s5_x, s5_y), s5_w, s5_h,
                                         boxstyle="round,pad=0.1,rounding_size=0.18",
                                         facecolor='#FFFBEB', edgecolor='#D97706', linewidth=2.2)
    ax.add_patch(handoff_card)

    # Step 5 Header
    s5_header = patches.FancyBboxPatch((s5_x + 0.12, s5_y + s5_h - 0.75), s5_w - 0.24, 0.65,
                                       boxstyle="round,pad=0.06,rounding_size=0.12",
                                       facecolor='#FEF3C7', edgecolor='none')
    ax.add_patch(s5_header)

    ho_tag_pill = patches.FancyBboxPatch((s5_x + 0.3, s5_y + s5_h - 0.62), 3.2, 0.4,
                                        boxstyle="round,pad=0.04,rounding_size=0.08",
                                        facecolor='#D97706', edgecolor='none')
    ax.add_patch(ho_tag_pill)
    ax.text(s5_x + 1.9, s5_y + s5_h - 0.42, "BƯỚC 5: ĐIỂM CHUYỂN GIAO (HANDOFF)",
            fontproperties=FontProperties(family=font_family, size=9.0, weight='bold'),
            color='#FFFFFF', ha='center', va='center')

    # Step 5 time
    time_pill5 = patches.FancyBboxPatch((s5_x + s5_w - 1.45, s5_y + s5_h - 0.62), 1.25, 0.4,
                                       boxstyle="round,pad=0.04,rounding_size=0.08",
                                       facecolor='#FDE68A', edgecolor='#D97706', linewidth=0.8)
    ax.add_patch(time_pill5)
    ax.text(s5_x + s5_w - 0.825, s5_y + s5_h - 0.42, "1 phút",
            fontproperties=FontProperties(family=font_family, size=9.0, weight='bold'),
            color='#92400E', ha='center', va='center')

    ax.text(s5_x + 0.3, s5_y + s5_h - 1.15, "Điều phối Xe cứu hộ sạc pin di động (Mobile Charging Van)",
            fontproperties=step_title_font, color='#78350F', va='center')

    # Step 5 details
    h_curr_y = s5_y + s5_h - 1.58
    ax.text(s5_x + 0.3, h_curr_y, "Đơn vị nhận bàn giao:", fontproperties=body_bold, color='#78350F')
    ax.text(s5_x + 2.5, h_curr_y, "Đội xe cứu hộ sạc pin lưu động Xanh SM / VinFast", fontproperties=body_font, color='#92400E')
    h_curr_y -= 0.32
    ax.text(s5_x + 0.3, h_curr_y, "Phương thức chuyển giao:", fontproperties=body_bold, color='#78350F')
    ax.text(s5_x + 2.5, h_curr_y, "Bắn tọa độ khẩn cấp qua tổng đài + Gọi bộ đàm cứu hộ", fontproperties=body_font, color='#92400E')
    h_curr_y -= 0.32
    ax.text(s5_x + 0.3, h_curr_y, "Hệ quả của độ trễ:", fontproperties=body_bold, color='#DC2626')
    ax.text(s5_x + 2.5, h_curr_y, "Nếu bước 3 & 4 kéo dài 10 phút, xe cạn pin chết máy gây ùn tắc giao thông", 
            fontproperties=FontProperties(family=font_family, size=9.2), color='#B91C1C')

    # Branch for Normal case: Pin >= 5%
    arrow_normal = patches.FancyArrowPatch((16.25, 2.4), (16.25, 1.4),
                                          arrowstyle='simple,head_width=8,head_length=8',
                                          color='#059669', linewidth=1.2)
    ax.add_patch(arrow_normal)
    normal_end_box = patches.FancyBboxPatch((14.4, 0.4), 3.7, 0.95,
                                           boxstyle="round,pad=0.06,rounding_size=0.12",
                                           facecolor='#ECFDF5', edgecolor='#10B981', linewidth=1.4)
    ax.add_patch(normal_end_box)
    
    ok_dot = patches.Circle((14.8, 0.92), 0.1, facecolor='#10B981', edgecolor='none')
    ax.add_patch(ok_dot)
    ax.text(15.05, 0.92, "KHÔNG (Pin >= 5%)", 
            fontproperties=FontProperties(family=font_family, size=9.0, weight='bold'),
            color='#065F46', va='center')
    ax.text(16.25, 0.62, "Tài xế tự di chuyển theo SMS hướng dẫn", 
            fontproperties=FontProperties(family=font_family, size=8.5),
            color='#047857', ha='center', va='center')

    # 4. Legend & Summary Panel (Bottom Left)
    legend_box = patches.FancyBboxPatch((0.8, 0.4), 3.3, 3.8,
                                       boxstyle="round,pad=0.08,rounding_size=0.15",
                                       facecolor='#FFFFFF', edgecolor='#CBD5E1', linewidth=1.2)
    ax.add_patch(legend_box)

    ax.text(1.1, 3.85, "CHÚ GIẢI (LEGEND)", fontproperties=FontProperties(family=font_family, size=11, weight='bold'), color='#0F172A')
    
    # Normal step
    norm_box = patches.Rectangle((1.1, 3.25), 0.35, 0.25, facecolor='#FFFFFF', edgecolor='#CBD5E1', linewidth=1.2)
    ax.add_patch(norm_box)
    ax.text(1.6, 3.37, "Bước bình thường (2 phút)", fontproperties=FontProperties(family=font_family, size=8.5), color='#334155', va='center')

    # Bottleneck
    bn_box_sample = patches.Rectangle((1.1, 2.75), 0.35, 0.25, facecolor='#FFE4E6', edgecolor='#F43F5E', linewidth=1.5)
    ax.add_patch(bn_box_sample)
    ax.text(1.6, 2.87, "[BOTTLENECK] Điểm nghẽn xử lý", fontproperties=FontProperties(family=font_family, size=8.5, weight='bold'), color='#BE123C', va='center')

    # Handoff
    ho_box_sample = patches.Rectangle((1.1, 2.25), 0.35, 0.25, facecolor='#FEF3C7', edgecolor='#D97706', linewidth=1.5)
    ax.add_patch(ho_box_sample)
    ax.text(1.6, 2.37, "[HANDOFF] Điểm chuyển giao", fontproperties=FontProperties(family=font_family, size=8.5, weight='bold'), color='#B45309', va='center')

    # Key conclusion note
    note_box = patches.FancyBboxPatch((1.0, 0.55), 2.9, 1.45,
                                     boxstyle="round,pad=0.06,rounding_size=0.1",
                                     facecolor='#F0FDFA', edgecolor='#0D9488', linewidth=1.2)
    ax.add_patch(note_box)
    ax.text(1.15, 1.68, "MỤC TIÊU CẢI TIẾN VỚI AI:",
            fontproperties=FontProperties(family=font_family, size=8.8, weight='bold'), color='#0F766E')
    ax.text(1.15, 1.15, "Tự động hóa Bước 3 & Bước 4\nbằng Gemini Flash Co-pilot:\n• Rút ngắn từ 15' xuống < 3'\n• Giảm 80% thời gian xử lý",
            fontproperties=FontProperties(family=font_family, size=8.2), color='#115E59')

    plt.tight_layout()
    output_png = '04-workflow-diagram.png'
    output_pdf = '04-workflow-diagram.pdf'
    plt.savefig(output_png, dpi=300, bbox_inches='tight')
    plt.savefig(output_pdf, bbox_inches='tight')
    plt.close()
    print(f"[SUCCESS] Exported {output_png} and {output_pdf} successfully without missing glyphs.")

if __name__ == '__main__':
    create_workflow_diagram()
