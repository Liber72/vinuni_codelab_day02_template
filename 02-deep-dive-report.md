# 02 — Deep-Dive Report: AI Product Scoping (Vin Smart Future)

> **Mảng kinh doanh lựa chọn:** Xanh SM (GSM) — Tự động hóa điều phối tài xế taxi điện thông minh.
> **Nhóm:** [Điền tên nhóm] | **Ngày:** 2026-09-11

---

## 🗳️ Bài Toán Được Chọn

Từ 3 Quick Problem Cards đã hoàn thành ở Phase 1–2, nhóm chọn **Card #1 — Xanh SM AI Dispatcher** để thực hiện Deep-Dive.

### Lý do lựa chọn:
- **Tần suất cao:** ~200 lượt điều vận/ca × 3 ca/ngày = ~600 lượt/ngày tại một trung tâm điều vận.
- **Bottleneck đo được:** 4–6 phút/lượt thủ công → tổng ~40–50 giờ nhân lực/ngày bị tiêu tốn.
- **Rủi ro có thể kiểm soát:** Output cuối vẫn cần dispatcher xác nhận (HITL), không tự phát lệnh.
- **AI Fit rõ ràng:** Tác vụ có cấu trúc đủ để LLM hỗ trợ ranking & draft, nhưng không đủ đơn giản để rule-based thay thế hoàn toàn (biến động theo ngữ cảnh thực địa).

### Lý do không chọn Card #2 và #3:
- **Card #2 (VinFast — Log BMS):** Dữ liệu log kỹ thuật cần được làm sạch và chuẩn hóa trước. Hiện chưa có pipeline dữ liệu sẵn sàng → **NOT YET**.
- **Card #3 (Vinhomes — Phản hồi 1-sao):** Tốt để tự động hóa nhưng rủi ro pháp lý khi AI soạn nội dung liên quan đến tranh chấp căn hộ, phí quản lý → cần legal review thêm trước khi triển khai.

---

# 🏗️ Phase 3 — DEEP-DIVE

## 3.1. Current-State Workflow Mapping

Quy trình điều vận thủ công hiện tại của Dispatcher tại Trung tâm Điều vận Xanh SM:

```text
┌─────────────────┐    ┌──────────────────┐    ┌──────────────────┐
│    BƯỚC 1        │    │     BƯỚC 2        │    │     BƯỚC 3        │
│  Nhận yêu cầu   │    │  Dispatcher mở   │    │  Dispatcher gọi  │
│  đặt xe từ App  │──→ │  bản đồ, tìm     │──→ │  điện / chat     │
│  khách hàng     │    │  tài xế gần nhất │    │  từng tài xế     │
│                 │    │                  │    │                  │
│  Ai: Hệ thống   │    │  Ai: Dispatcher  │    │  Ai: Dispatcher  │
│  ⏱ 0 phút       │    │  ⏱ 2–3 phút 🔴   │    │  ⏱ 2–3 phút 🔴   │
└─────────────────┘    └──────────────────┘    └──────────────────┘
                                                        │
                                                        ▼
                        ┌──────────────────┐    ┌──────────────────┐
                        │     BƯỚC 5        │    │     BƯỚC 4        │
                        │  Dispatcher cập  │    │  Tài xế xác nhận │
                        │  nhật hệ thống   │←── │  hoặc từ chối    │
                        │  & đóng lượt     │    │  chuyến          │
                        │                  │    │                  │
                        │  Ai: Dispatcher  │    │  Ai: Tài xế      │
                        │  ⏱ 1 phút        │    │  ⏱ 1–2 phút      │
                        └──────────────────┘    └──────────────────┘

🔴 = Bottleneck (Bước 2 & 3: Tìm kiếm + Liên lạc thủ công)
🔄 = Handoff (Bước 1→2: App→Dispatcher | Bước 3→4: Dispatcher→Tài xế)
⏱  Tổng thời gian trung bình: 6–10 phút/lượt điều vận
```

**Nhận xét Bottleneck:**
- **Bước 2:** Dispatcher phải tự đánh giá bằng mắt trên bản đồ; không có scoring tự động về tài xế nào phù hợp nhất (khoảng cách, điểm đánh giá, mức pin xe, hành trình tiếp theo).
- **Bước 3:** Liên lạc tuần tự từng tài xế — nếu tài xế từ chối, phải lặp lại toàn bộ bước 2–3. Trường hợp xấu có thể gọi 3–4 tài xế mới xong.

---

## 3.2. Problem Statement (6-Field)

| Field | Nội dung chi tiết |
|---|---|
| **1. Actor / Operator** | Dispatcher (Điều phối viên) tại Trung tâm Điều vận Xanh SM Hà Nội & TP.HCM — mỗi ca làm việc có 5–8 dispatcher xử lý đồng thời toàn bộ đội xe trong khu vực. |
| **2. Current Workflow** | Khi App ghi nhận yêu cầu đặt xe, dispatcher thủ công quan sát bản đồ nội bộ, chọn tài xế gần nhất theo cảm quan, gọi điện/nhắn tin để xác nhận chuyến, chờ phản hồi, và cập nhật hệ thống. Toàn bộ 5 bước mất 6–10 phút/lượt. Công cụ hiện tại: Bản đồ GIS nội bộ + điện thoại nội bộ + hệ thống log thủ công. |
| **3. Bottleneck** | Bước 2–3 chiếm 4–6 phút: Dispatcher không có công cụ ranking tự động — việc chọn tài xế phụ thuộc vào kinh nghiệm cá nhân và quan sát trực quan bản đồ. Vào giờ cao điểm (7–9h, 17–19h), số lượng yêu cầu tăng 3× trong khi số dispatcher không đổi → backlog tích lũy, thời gian chờ của khách tăng lên 8–12 phút. |
| **4. Business Impact** | ~600 lượt/ngày × 8 phút trung bình = **80 giờ nhân lực dispatcher bị tiêu tốn mỗi ngày**. Tỷ lệ khách hủy chuyến do chờ lâu ở giờ cao điểm ước tính ~18%, tương đương mất ~15–20% doanh thu tiềm năng trong khung giờ peak. Chi phí lương dispatcher: ~2,5 triệu VNĐ/ca × 3 ca × 30 ngày = **225 triệu VNĐ/tháng** chỉ cho tác vụ này. |
| **5. Success Metric** | **Metric chính:** Giảm thời gian điều vận trung bình từ 6–10 phút → **dưới 45 giây** (đo bằng timestamp hệ thống từ lúc App nhận yêu cầu đến khi tài xế xác nhận). **Metric phụ:** Tỷ lệ tài xế nhận chuyến ngay ở lần đề xuất đầu tiên ≥ **85%** (giảm số lần dispatcher phải thử lại). **Metric bảo vệ:** 100% tin nhắn điều vận phải có tag `[DRAFT_ONLY]` trước khi dispatcher duyệt — không có lượt nào bị gửi tự động. |
| **6. Operational Boundary** | ✅ **AI được phép:** Truy xuất API định vị xe, đánh giá và ranking tài xế theo thuật toán (khoảng cách, điểm rating, mức pin, trạng thái sẵn sàng), soạn thảo tin nhắn thông báo chuyến dạng **[DRAFT_ONLY]**. ❌ **AI tuyệt đối không được:** Tự gửi lệnh phân công chuyến hoặc tin nhắn đến tài xế mà không có dispatcher duyệt; không được điều phối xe khi phát hiện mức pin < 5% mà không kích hoạt lệnh `dispatch_mobile_charger`; không được ưu tiên tài xế có điểm đánh giá dưới 3.5/5. |

---

## 3.3. Future-State Flow & AI Fit

### AI-Fit Matrix:

| Phương án | Đánh giá |
|---|---|
| ❌ **No AI** | Hiện trạng — không giải quyết bottleneck. |
| ⚠️ **Rule / State-Machine** | Có thể tạo rule đơn giản (gần nhất = tốt nhất) nhưng không xử lý được biến động ngữ cảnh thực địa (tắc đường, tài xế vừa kết thúc chuyến dài, pin xe, v.v.). |
| ✅ **LLM Feature** | **Phù hợp nhất.** LLM có thể đọc ngữ cảnh đa chiều (vị trí, pin, lịch sử tài xế, điều kiện giao thông), ranking hợp lý và soạn tin nhắn tự nhiên bằng tiếng Việt. Output vẫn cần HITL — rủi ro được kiểm soát. |
| ❌ **Agentic Loop** | Quá phức tạp và rủi ro cao — dispatcher mất quyền kiểm soát nếu Agent tự gửi lệnh. Không phù hợp ở giai đoạn này. |

**Quyết định: ✅ LLM Feature**

### Future-State Workflow:

```text
┌─────────────────┐    ┌──────────────────────────────┐    ┌──────────────────┐
│    BƯỚC 1        │    │          BƯỚC 2               │    │     BƯỚC 3        │
│  App nhận yêu   │    │  🔵 AI ENGINE tự động:        │    │  🟢 HITL:         │
│  cầu đặt xe     │──→ │  • Pull vị trí GPS xe         │──→ │  Dispatcher xem  │
│                 │    │  • Đánh giá & ranking tài xế  │    │  AI draft, click │
│                 │    │  • Soạn [DRAFT_ONLY] tin nhắn │    │  "Duyệt & Gửi"   │
│  ⏱ 0 giây       │    │  ⏱ < 10 giây 🔵               │    │  ⏱ < 5 giây 🟢   │
└─────────────────┘    └──────────────────────────────┘    └──────────────────┘
                                                                    │
                                                                    ▼
                        ┌──────────────────┐              ┌──────────────────┐
                        │  ↩️ FALLBACK       │              │     BƯỚC 4        │
                        │  Nếu AI lỗi hoặc  │              │  Tài xế nhận     │
                        │  không tìm được   │              │  thông báo &     │
                        │  tài xế phù hợp: │              │  xác nhận        │
                        │  Alert dispatcher │              │  chuyến qua App  │
                        │  xử lý thủ công  │              │  ⏱ < 30 giây     │
                        └──────────────────┘              └──────────────────┘

🔵 = AI Step (LLM tự động xử lý)
🟢 = Human-in-the-Loop (Dispatcher duyệt)
↩️ = Fallback (Xử lý thủ công khi AI thất bại)

⏱ Tổng thời gian dự kiến: < 45 giây/lượt (so với 6–10 phút hiện tại)
```

### Cơ chế Human-in-the-Loop (HITL):
- Dispatcher nhìn thấy: Top 3 tài xế được AI đề xuất kèm điểm ranking, mức pin xe, ETA.
- Dispatcher nhìn thấy: Tin nhắn `[DRAFT_ONLY]` đã được soạn sẵn — có thể chỉnh sửa trước khi gửi.
- Dispatcher bấm **"Duyệt & Gửi"** → hệ thống mới thực sự gửi thông báo đến tài xế.

### Cơ chế Fallback:
1. **AI không tìm được tài xế phù hợp** (tất cả đều đang bận hoặc pin thấp) → Alert đỏ cho dispatcher xử lý thủ công.
2. **AI phát hiện pin tài xế/xe < 5%** → Không đề xuất chuyến, tự động kích hoạt `dispatch_mobile_charger`.
3. **Tài xế từ chối trong 30 giây** → AI tự động ranking lại và đề xuất tài xế kế tiếp cho dispatcher.

---

# 🏁 Phase 5 — EVALUATE

## AI Readiness Checklist

| # | Tiêu chí | Trạng thái | Ghi chú |
|---|---|---|---|
| 1 | Chúng tôi có sẵn dữ liệu mẫu/logs sạch để test? | ✅ **Có** | Log điều vận lịch sử 6 tháng sẵn sàng; dữ liệu GPS real-time từ App Xanh SM có API. |
| 2 | Rủi ro khi AI sai có nằm trong tầm kiểm soát? | ✅ **Có** | HITL bắt buộc — dispatcher duyệt 100% trước khi gửi; tag `[DRAFT_ONLY]` ngăn tự động gửi. |
| 3 | Stakeholders sẵn sàng thay đổi quy trình làm việc? | ✅ **Có** | Quản lý vận hành Xanh SM đã xác nhận ủng hộ sau khi trình bày metric. Dispatcher được đào tạo 1 buổi trước triển khai. |

**Tổng đánh giá: 3/3 tiêu chí ĐẠT ✅**

---

## Quyết định cuối cùng của Ban Giám Đốc Vin Smart Future

> **[x] GO — Bắt đầu xây dựng Prototype với scope hẹp**

### Justification (Lý giải quyết định):

**Bằng chứng kỹ thuật:**
1. **Bài toán có cấu trúc đủ rõ ràng:** Input (vị trí, số xe, trạng thái tài xế) và output (ranking tài xế + draft tin nhắn) đều có thể định nghĩa chính xác → LLM Feature là đủ, không cần Agent phức tạp.
2. **Dữ liệu huấn luyện sẵn có:** 6 tháng log điều vận thực tế với outcome (tài xế nào được chọn, chuyến nào thành công) → có thể đánh giá chất lượng ranking của AI so với baseline dispatcher.
3. **Ranh giới an toàn đã được kiểm chứng qua Prototype:** Prompt prototype đã pass 2/2 adversarial test case (pin < 5% → dispatch mobile charger; không bỏ tag `[DRAFT_ONLY]` dù bị tấn công prompt).

**Bằng chứng kinh doanh:**
- ROI ước tính: Tiết kiệm 80 giờ dispatcher/ngày → tương đương **~7,5 triệu VNĐ/ngày** chi phí lương (hoặc tái phân bổ nhân lực sang xử lý exception phức tạp hơn).
- Giảm tỷ lệ hủy chuyến 18% → tăng doanh thu ~15–20% trong khung giờ peak.

**Phạm vi Prototype (Scope hẹp để GO):**
- Giai đoạn 1 (4 tuần): Deploy thử nghiệm tại 1 trung tâm điều vận (Hà Nội), 2 dispatcher tham gia pilot, 50 lượt/ngày.
- Ngưỡng thành công để mở rộng: Đạt thời gian điều vận < 45 giây và tỷ lệ nhận chuyến lần đầu ≥ 80% trong 2 tuần liên tiếp.

---

> *Hoàn thành bởi: [Ngô Xuân Hoàng] — VinUni Codelab Day 02 | 2026-09-11*
