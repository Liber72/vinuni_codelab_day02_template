# 🏗️ Phase 3 — DEEP-DIVE REPORT
## Bài toán: Dịch vụ Sạc Xe Điện Thông Minh & Điều Phối Luân Chuyển Trạm Sạc (VinFast Smart Valet Charging & Turn-around Co-pilot)

> **Nhóm thực hiện:** Nhóm Dự án Vin Smart Future  
> **Người đại diện:** Thái Đạt — Sinh viên ngành Fintech, PTIT  
> **Đơn vị phối hợp:** VinFast & V-GREEN (Hệ thống trạm sạc nhượng quyền toàn cầu) phối hợp cùng GSM (Xanh SM)  
> **Tài liệu tham chiếu từ:** Card #1 trong [01-problem-scan.md](file:///c:/Users/Admin/AI_Thucchien/vinuni_codelab_day02_template/01-problem-scan.md)

---

## 3.1. Current-State Workflow (Quy trình thủ công hiện tại)

Hiện tại, tại các trạm sạc nhanh VinFast và các Hub sạc tập trung (TTTM Vincom, khu đô thị Vinhomes, trạm dừng nghỉ cao tốc), quy trình sạc xe và giải phóng trụ hoàn toàn phụ thuộc vào việc tài xế tự canh giờ:

```text
┌─────────────────┐      ┌─────────────────┐      ┌─────────────────┐      ┌─────────────────┐
│ Bước 1          │      │ Bước 2          │      │ Bước 3          │      │ Bước 4          │
│ Cắm sạc &       │      │ Canh giờ sạc pin│      │ Phát hiện sạc   │      │ Điều phối &     │
│ rời khỏi xe     │ ───> │ thủ công        │ ───> │ xong            │ ───> │ dời xe ra bãi    │
│                 │      │                 │      │                 │      │                 │
│ Actor: Tài xế   │      │ Actor: Tài xế / │      │ Actor:          │      │ Actor:Tài xế│
│ ⏱ 2 phút        │      │        NV trạm  │      │        Tài xế   │      │                │
│ In: Cắm súng sạc│      │ ⏱ 30-45 phút    │      │ ⏱ 8-10 phút     │      │ ⏱ 7-10 phút   │
│ Out: Xe bắt đầu │      │ In: Mắt nhìn trụ│      │ In: Biển số, sđt│      │ In: Vị trí đỗ   │
│      sạc điện   │      │ Out: Đoán chừng │      │ Out: Gọi giục xe│      │ Out: Trụ trống  │
└─────────────────┘      └─────────────────┘      └─────────────────┘      └─────────────────┘
                                                                            

🔴 = Điểm nghẽn nghiêm trọng (Bottlenecks):
     - Bước 4: Mất thời gian tìm kiếm chỗ đỗ trống, tài xế từ xa chạy lại tự đánh xe đi tìm chỗ.
     - Tổng quát, tài xế phải chờ đợi xe sạc xong để di dời rồi tránh bị phạt, từ đó lãng phí thời gian và có thể gây khó chịu cho khách hàng mua xe.
⏱ Tổng thời gian chiếm trụ lãng phí sau khi sạc xong (Idle time): 15 - 20 phút/xe.
```

---

## 3.2. Problem Statement (6-field) — Tiêu chuẩn Vin Smart Future

| Trường thông tin (Field) | Nội dung chi tiết chuẩn hóa |
|---|---|
| **1. Actor / Operator** | • **Nhân viên điều phối trạm sạc / Nhân viên Valet** (Station Operator / Hub Coordinator) tại các Hub trạm sạc VinFast/V-GREEN.<br>• **Tài xế xe điện** (Chủ xe cá nhân VinFast VF5/VF8/VF9 và Tài xế taxi Xanh SM). |
| **2. Current Workflow** | Khi tài xế cắm sạc nhanh, họ thường rời xe đi ăn uống hoặc nghỉ ngơi. Tài xế phải tự đặt báo thức hoặc thi thoảng vào app VinFast canh % pin. Khi pin đầy (100%), trụ ngừng sạc nhưng xe vẫn cắm súng chiếm chỗ. Khách hàng phải chịu phạt nếu vẫn cắm súng nếu pin đã đầy. Quy trình gồm 4 bước thủ công, mất 20–25 phút chỉ để giải phóng một trụ sạc. Điều này gây lãng phí tài nguyên nghiêm trọng khi tình trạng thiếu trụ sạc ngày càng lớn. |
| **3. Bottleneck** | **Bước 3 & Bước 4:**<br>1. Không có hệ thống tự động tháo sạc và di chuyển xe vào điểm đỗ xe thay thế, dù cho các tài xế rất có nhu cầu.<br>2.  Mất thời gian tìm kiếm vị trí đỗ xe thay thế và mất thời gian khiến chủ xe phải chờ đợi tại chạm sạc. |
| **4. Business Impact** | • **Lãng phí công suất trạm:** Tại mỗi Hub sạc lớn (20 trụ sạc), trung bình 35% lượt sạc bị trễ rút súng sạc (quá hạn ~15 phút/lượt), gây lãng phí khoảng 12–15 giờ công suất sạc của toàn trạm mỗi ngày.<br>• **Tổn thất doanh thu:** Lượng xe đến thấy hết trụ phải quay đầu đi nơi khác gây thiệt hại ước tính ~15–20 triệu VNĐ tiền điện sạc/trạm/tháng.<br>• **Trải nghiệm khách hàng:** Tài xế bị tính phí phạt đỗ quá giờ (idle fee 1.000đ/phút sau khi sạc xong), gây xung đột, cãi vã và làm giảm chỉ số hài lòng. |
| **5. Success Metric** | 1. **Giảm thời gian chiếm dụng trụ sau sạc (Turn-around / Idle time):** Từ 15–20 phút xuống **dưới 2 phút** (giải phóng trụ ngay khi pin đạt ngưỡng sạc).<br>2. **Tăng công suất quay vòng trụ sạc (Station Throughput):** Tăng **$+20\%$** số lượt xe được sạc trong khung giờ cao điểm (Peak Hours). |
| **6. Operational Boundary** | • **AI ĐƯỢC PHÉP:** Đọc dữ liệu Telematics sạc thời gian thực (SoC %, công suất kW, nhiệt độ pin); tính toán dự báo thời điểm hoàn thành sạc; tự động quét tìm ô đỗ xe còn trống trong bãi đỗ liên kết;.<br>• **AI TUYỆT ĐỐI CẤM (Safety Boundaries):**<br>  1. Không được tự ý gửi lệnh ngắt sạc khẩn cấp khi xe chưa đạt ngưỡng an toàn đã cài đặt mà không có xác nhận của tài xế/kỹ thuật viên.<br>  2. Không được gửi lệnh mở khóa xe từ xa nếu chưa có Token xác thực điện tử (Digital Valet Pass) do chủ xe phê duyệt.<br>  3. Bắt buộc có **Human-in-the-loop (HITL):** Mọi tin nhắn gửi ra ngoài hệ thống và lệnh điều phối dời xe đều phải có sự xác nhận của tài xế hoặc nhân viên trạm sạc. |

---

## 3.3. Future-State Flow & Kiến trúc AI Fit

### A. Lựa chọn AI-Fit (AI-Fit Matrix)
* **Giải pháp lựa chọn:** **LLM Feature kết hợp Event-Driven State Machine (Telematics Pipeline)**.
* **Lý do lựa chọn:**
  - Tác vụ an toàn điện và di chuyển xe cơ giới cần tính chính xác và kiểm soát tuyệt đối (Deterministic Rule/State Machine).
  - LLM đóng vai trò là **Smart Co-pilot**:
    1. Tổng hợp dữ liệu phi cấu trúc (loại cổng sạc CCS2/GBT, đặc tính pin dòng xe VF5/VF8/VF9, nhiệt độ môi trường, trạng thái bãi đỗ) để dự báo thời điểm vàng kết thúc sạc (thường là 80% đối với sạc nhanh để tránh sạc chậm giai đoạn cuối).
    2. Tự động soạn thảo thông điệp cá nhân hóa, thân thiện, rõ ràng gửi tới tài xế theo đúng ngữ cảnh thực tế (vị trí xe, số trụ, thời gian còn lại, hướng dẫn nhận xe).

### B. Quy trình vận hành tương lai (Future-State Workflow)

```text
┌─────────────────┐      ┌───────────────────────────┐      ┌───────────────────────────┐      ┌───────────────────────────┐
│ Bước 1          │      │ Bước 2                    │      │ Bước 3                    │      │ Bước 4                    │
│ Xe cắm sạc &    │      │ 🔵 AI Dự Báo Thời Gian   │      │ 🔵 AI Tự Động Soạn Tin    │      │ 🟢 Tài Xế / NV Valet     │
│ kết nối hệ thống│ ───> │ & Quét Vị Trí Đỗ Trống    │ ───> │ Điều Phối Đa Kênh (Draft) │ ───> │ Xác Nhận & Dời Xe        │
│                 │      │                           │      │                           │      │                           │
│ In: Cắm súng sạc│      │ In: SoC %, kW, nhiệt độ   │      │ In: Thời gian, ô đỗ trống │      │ In: Tin nhắn gợi ý        │
│ Out: Telematics │      │ Out: Dự kiến đầy sau 8 min│      │ Out: SMS/Push notification│      │ Out: Trụ sạc trống        │
│      kích hoạt  │      │      Ô đỗ trống: Slot P-05│      │      sẵn sàng duyệt       │      │      trong < 2 phút       │
└─────────────────┘      └───────────────────────────┘      └───────────────────────────┘      └───────────────────────────┘
                                                                                                              │
                                                                                                              ▼
                                                                                                   ┌───────────────────────────┐
                                                                                                   │ ↩️ Fallback Plan          │
                                                                                                   │ Nếu mất kết nối AI hoặc   │
                                                                                                   │ tài xế không phản hồi:    │
                                                                                                   │ Kích hoạt Auto CallBot gọi│
                                                                                                   │ thẳng tới hotline nhân viên. │
                                                                                                   └───────────────────────────┘
```

### C. Chi tiết các bước tích hợp AI & Cơ chế Phòng thủ (Safety & Fallback)

1. **🔵 AI Step — Predictive Charging Model & Slot Finder:**
   - Hệ thống theo dõi đường cong công suất sạc (Charging Curve). Khi pin chạm mức 75–80%, tốc độ sạc giảm dần (tapering), hệ thống tính toán chính xác thời điểm đạt mục tiêu sạc trong 5–7 phút tới.
   - Hệ thống đồng thời truy vấn camera giám sát bãi xe, hoặc hệ thống đỗ xe liên kết để chỉ định sẵn ô đỗ trống gần nhất (ví dụ: Ô đỗ P-08, cách trụ sạc 20m).

2. **🔵 AI Step — Generative Notification Draft:**
   - LLM sinh ra thông báo súc tích, chuyên nghiệp:
     > ` Kính gửi Quý khách, xe VF8 (29A-123.45) tại Trụ Sạc DC-04 sẽ hoàn tất sạc đạt 80% trong 5 phút nữa. Để tránh phát sinh phí chiếm trụ (1.000đ/phút), Quý khách có thể tự dời xe hoặc nhấn "Ủy quyền Valet" để nhân viên trạm và hệ thống robot tự hành hỗ trợ đưa xe về Ô đỗ P-08 an toàn.`

3. **🟢 Human-in-the-loop (HITL):**
   - Tài xế nhận thông báo trên App VinFast / Xanh SM, bấm xác nhận chọn 1 trong 2 phương án:
     - **Phương án A (Tự di chuyển):** Tài xế bấm "Tôi đang ra xe" (hệ thống gia hạn 5 phút).
     - **Phương án B (Valet hỗ trợ):** Tài xế cấp "One-Time Digital Valet Token", nhân viên trạm nhận lệnh trên thiết bị cầm tay, quét mã rút súng sạc và sử dụng hệ thống robot tự hành di chuyển xe vào ô P-08. Trụ sạc được giải phóng ngay lập tức cho xe tiếp theo.

4. **↩️ Failure Modes & Kế hoạch Dự phòng (Fallback Mechanism):**
   - **Trường hợp 1 (Mất mạng / Lỗi Telematics trạm sạc):** Hệ thống lập tức fallback về Rule-based Timer tính toán theo công suất danh định của trụ sạc.
   - **Trường hợp 2 (Tài xế không phản hồi sau 3 phút):** Hệ thống chuyển tiếp cho tổng đài tự động (Voice CallBot) gọi trực tiếp thông báo bằng giọng nói. Nếu vẫn không liên lạc được, chuyển cờ báo cho nhân viên trạm xử lý theo quy chế an toàn trạm sạc V-GREEN.
