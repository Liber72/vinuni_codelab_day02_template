# 02 — Problem Deep-Dive Report: AI Co-pilot for Xanh SM Dispatchers

**Đơn vị:** Vin Smart Future — Khối Công nghệ Tập đoàn Vingroup  
**Dự án:** Trợ lý Điều vận Thông minh Xử lý Sự cố Năng lượng Thực địa (Xanh SM Dispatcher Co-pilot)  
**Bài toán lựa chọn:** Card #1 — Xử lý sự cố sạc pin / cạn pin khẩn cấp thực địa  

---

## 3.1. Current-State Workflow Mapping
Quy trình thủ công hiện tại xử lý sự cố hết pin/cạn pin thực địa tại Trung tâm Điều vận Xanh SM:

```text
┌────────────────┐     ┌────────────────┐     ┌────────────────┐     ┌────────────────┐
│ Bước 1         │     │ Bước 2         │     │ Bước 3 🔴      │     │ Bước 4 🔴      │
│ Nhận cuộc gọi  │     │ Tra cứu toạ độ │     │ Tra cứu trạm   │     │ Soạn thảo tin  │
│ / tin khẩn cấp │ ──> │ GPS & dung     │ ──> │ sạc VinFast    │ ──> │ nhắn chỉ đường │
│ từ tài xế      │     │ lượng pin xe   │     │ còn trụ trống  │     │ cho tài xế     │
│                │     │                │     │                │     │                │
│ Ai: Dispatcher │     │ Ai: Dispatcher │     │ Ai: Dispatcher │     │ Ai: Dispatcher │
│ ⏱ 2 phút       │     │ ⏱ 2 phút       │     │ ⏱ 5 phút (Chậm)│     │ ⏱ 5 phút (Chậm)│
│ In: Điện thoại │     │ In: Biển số xe │     │ In: Toạ độ GPS │     │ In: Dữ liệu raw│
│ Out: Log sự cố │     │ Out: Toạ độ, % │     │ Out: Trạm sạc  │     │ Out: SMS/Chat  │
└────────────────┘     └────────────────┘     └────────────────┘     └────────────────┘
                                                                             │
                                                                             ▼ 🔄 Handoff
                                                                      ┌────────────────┐
                                                                      │ Bước 5         │
                                                                      │ Điều xe cứu hộ │
                                                                      │ sạc di động    │
                                                                      │ (nếu pin < 5%) │
                                                                      │                │
                                                                      │ Ai: Dispatcher │
                                                                      │ ⏱ 1 phút       │
                                                                      └────────────────┘
```
* 🔴 **Bottleneck (Điểm nghẽn):** Bước 3 & Bước 4 (mất tổng cộng 10 phút để tra cứu trạm sạc khả dụng và gõ tay tin nhắn chỉ đường).
* 🔄 **Handoff (Điểm chuyển giao):** Bước 5 chuyển thông tin sang đội xe sạc pin lưu động (Mobile Charging Van) khi pin nguy cấp.
* ⏱ **Tổng thời gian xử lý thủ công:** **15 phút/lượt**.

---

## 3.2. Problem Statement (6-field) — Vin Smart Future Standard

| Field | Nội dung chi tiết |
|---|---|
| **1. Actor / Operator** | Điều phối viên trực ban (Dispatcher Co-pilot) thuộc Trung tâm Điều vận Taxi điện Xanh SM (GSM). |
| **2. Current Workflow** | Khi tài xế báo sự cố cạn pin hoặc không sạc được giữa đường, điều phối viên phải mở nhiều màn hình riêng biệt: hệ thống định vị GPS xe, dashboard mạng lưới trụ sạc VinFast, rồi gõ thủ công tin nhắn SMS/In-App hướng dẫn tài xế, hoặc gọi điện điều xe cứu hộ nếu pin dưới 5%. Quy trình qua 5 bước thủ công, mất trung bình 15 phút/lượt. |
| **3. Bottleneck** | **Bước 3 & 4 (chiếm 10/15 phút):** Tra cứu thủ công trụ sạc trống tương thích cổng sạc (CCS2/GBT) theo thời gian thực và tự soạn thảo tin nhắn hướng dẫn đường đi bằng ngôn ngữ tự nhiên. |
| **4. Business Impact** | Mỗi ngày có ~80 sự cố cảnh báo pin khẩn cấp tại Hà Nội và TP.HCM. Tốn ~20 giờ công/ngày của đội điều vận. Xe nằm chờ gây lãng phí cơ hội phục vụ cuốc khách, rò rỉ ~15% doanh thu ca chạy và gây bức xúc, hoang mang cho tài xế. |
| **5. Success Metric** | 1. **Efficiency (Hiệu suất):** Giảm tổng thời gian xử lý sự cố từ 15 phút ──> dưới 3 phút/lượt (giảm 80%).<br>2. **Accuracy (Độ chính xác):** 98% gợi ý trạm sạc đúng chủng loại cổng và còn trụ trống khả dụng.<br>3. **Safety (An toàn):** 100% các xe có pin < 5% được hệ thống tự động kích hoạt điều xe sạc di động (Zero stranded vehicles). |
| **6. Operational Boundary** | • **AI ĐƯỢC PHÉP:** Đọc tọa độ GPS, tra cứu dữ liệu trạm sạc VinFast, dự thảo tin nhắn hướng dẫn chuẩn Tiếng Việt bắt buộc có tag `[DRAFT_ONLY]`, và tạo lệnh gọi xe sạc pin di động (`dispatch_mobile_charger`) khi pin < 5%.<br>• **AI CẤM:** TUYỆT ĐỐI không được tự ý gửi tin đi cho tài xế khi chưa qua Điều phối viên phê duyệt (bắt buộc Human-In-The-Loop); TUYỆT ĐỐI không đề xuất trạm sạc xa > 5km khi pin < 5%. |

---

## 3.3. Future-State Flow & AI Fit

* **Xác định mức AI Fit (AI-Fit Matrix):** **[x] LLM Feature** (kết hợp Rule-based guardrails).
  * *Lý do:* Tác vụ yêu cầu phân tích ngôn ngữ tự nhiên và tổng hợp thông tin nhanh. Không dùng Agentic Loop hoàn toàn tự trị (Autonomous Agent) nhằm loại bỏ rủi ro AI tự quyết định sai gây cạn kiệt pin chết máy giữa đường phố đông đúc.

* **Sơ đồ quy trình tương lai (Future-State Flow):**

```text
┌────────────────┐     ┌────────────────┐     ┌────────────────┐     ┌────────────────┐
│ Bước 1         │     │ Bước 2         │     │ Bước 3         │     │ Bước 4         │
│ Tài xế báo sự  │     │ 🔵 Hệ thống    │     │ 🔵 AI Engine   │     │ 🟢 Dispatcher  │
│ cố pin hoặc xe │ ──> │ Auto-pull GPS, │ ──> │ Phân tích pin &│ ──> │ duyệt bản nháp │
│ gửi telemetry  │     │ mức pin & trạm │     │ Draft tin nhắn │     │ [DRAFT_ONLY]   │
│                │     │ sạc trống lân  │     │ kèm nhãn an    │     │ và bấm "Send"  │
│                │     │ cận qua API    │     │ toàn           │     │                │
└────────────────┘     └────────────────┘     └────────────────┘     └────────────────┘
                                                       │                      │
                                                       ▼                      ▼
                                            [Nếu pin xe < 5%]         ↩️ Fallback:
                                            Kích hoạt JSON:           Nếu AI timeout
                                            {"action":                hoặc lỗi kết nối,
                                             "dispatch_mobile_        chuyển sang giao diện
                                             charger"}                tra cứu thủ công.
```
* 🔵 **AI Step:** Tự động đối chiếu tọa độ, lọc trạm sạc phù hợp và sinh tin nhắn chỉ đường chuẩn phong cách CSKH Xanh SM.
* 🟢 **Human Step (HITL):** Điều phối viên chỉ mất 15-30 giây đọc lướt bản nháp và bấm xác nhận gửi qua App tài xế.
* ↩️ **Fallback Plan:** Nếu Gemini API mất kết nối (> 5 giây) hoặc trả về kết quả không tự tin, hệ thống tự động bật form thủ công truyền thống để điều phối viên gõ tin như cũ, đảm bảo SLA vận hành không bao giờ tắc nghẽn.

---

## 🏁 Phase 5 — EVALUATE: Quyết định Phê duyệt Dự án

### AI Readiness Checklist:
1. [x] **Dữ liệu:** Đã có telemetry GPS và trạng thái trụ sạc VinFast theo thời gian thực.
2. [x] **Kiểm soát rủi ro:** 100% bản nháp phải qua HITL duyệt; có Fallback quy trình cũ nếu hệ thống AI offline.
3. [x] **Văn hóa tiếp nhận:** Đội ngũ điều vận Xanh SM rất mong muốn giảm tải áp lực 20 giờ làm việc/ngày.

### Quyết định của Ban Giám Đốc Vin Smart Future:
**[x] GO (Bắt đầu xây dựng Prototype)**

**Justification (Lý giải quyết định dựa trên bằng chứng kỹ thuật và chi phí):**
1. **Hiệu quả kinh tế cao (High ROI):** Tiết kiệm 80% thời gian xử lý sự cố (từ 15 phút xuống dưới 3 phút), giải phóng 20 giờ lao động/ngày cho đội ngũ điều phối, giảm thiểu tỉ lệ xe chết máy giúp bảo vệ ~15% doanh thu cuốc xe.
2. **Chi phí công nghệ tối thiểu:** Sử dụng mô hình **Gemini 2.5 Flash** với chi phí inference cực thấp (~$0.0001 mỗi lượt request).
3. **Kiểm soát rủi ro an toàn tuyệt đối:** Ranh giới vận hành (Operational Boundary) được thiết lập chặt chẽ với cơ chế bắt buộc duyệt (Human-in-the-loop qua tag `[DRAFT_ONLY]`) và xử lý pin nguy cấp bằng xe sạc cứu hộ di động. Rủi ro vận hành gần như bằng 0.
