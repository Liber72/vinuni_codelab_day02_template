# 01 — Problem Scan: AI Product Scoping (Vin Smart Future)

---

## 📊 Phase 1 — SCAN: Bảng Quét Cơ Hội AI

> Sử dụng 4 Lenses để quét pain point tại các công ty thành viên Vingroup.

| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|------------|------|---------------------|
| 1 | **Xanh SM (GSM)** | Lặp lại (Repetitive) | Điều phối tài xế thủ công: mỗi lượt điều vận, dispatcher phải xem bản đồ, gọi điện thoại từng tài xế để xác nhận chuyến — mỗi ca xử lý ~200 lượt. |
| 2 | **VinFast** | Tốn thời gian (Time-consuming) | Kiểm tra lỗi pin/BMS thủ công: kỹ thuật viên đọc log lỗi từng xe EV để phân loại lỗi pin, mất 15–20 phút/xe, trong khi đội có hàng trăm xe cần xét mỗi ngày. |
| 3 | **Vinhomes** | AI-upgrade | Phản hồi đánh giá 1-sao của cư dân: nhân viên CSKH Vinhomes phải đọc thủ công và soạn email phản hồi riêng cho từng khiếu nại — trung bình 10 phút/yêu cầu, ~150 yêu cầu/ngày. |
| 4 | **Vinmec** | Stakeholder Pain | Tóm tắt hồ sơ bệnh án trước khám: bác sĩ phải đọc toàn bộ lịch sử bệnh nhân trước mỗi buổi tư vấn (trung bình 8–12 trang/hồ sơ) dù hầu hết thông tin không liên quan ca khám hôm đó. |
| 5 | **Vinpearl / VinWonders** | ⏱ Tốn thời gian (Time-consuming) | Phân loại và định tuyến yêu cầu hỗ trợ khách: nhân viên tổng đài Vinpearl nhận yêu cầu qua nhiều kênh (chat, email, hotline), phải đọc và phân loại thủ công trước khi chuyển bộ phận xử lý — gây trễ phản hồi ~8 phút/yêu cầu. |

---

## 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

Chọn top 3 bài toán tiềm năng nhất từ danh sách trên.

---

### 🃏 QUICK PROBLEM CARD #1

```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán (1 câu): Tự động hóa điều phối tài xế Xanh SM     │
│ bằng AI dispatcher thay thế quy trình gọi điện thủ công.    │
│                                                             │
│ Công ty thành viên: [x] Xanh SM (GSM)                       │
│                                                             │
│ Ai đang đau (Actor)?                                         │
│   Dispatcher (nhân viên điều vận trung tâm) và tài xế        │
│   Xanh SM trực ca.                                           │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                         │
│   1. Hệ thống nhận yêu cầu đặt xe từ app khách hàng         │
│      ──> 2. Dispatcher mở bản đồ, tìm tài xế gần nhất       │
│      ──> 3. Dispatcher gọi điện/nhắn tin từng tài xế         │
│      ──> 4. Tài xế xác nhận hoặc từ chối chuyến             │
│      ──> 5. Dispatcher ghi nhận kết quả và cập nhật hệ thống │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất?                             │
│   Bước 2–3: Tìm tài xế và xác nhận thủ công                 │
│   ⏱ ~4–6 phút/lượt điều vận, ~200 lượt/ca                   │
│                                                             │
│ AI có thể nhảy vào hỗ trợ ở bước nào?                       │
│   Bước 2–4: AI ranking tài xế phù hợp (gần nhất, sẵn sàng,  │
│   đánh giá tốt nhất) và tự động đẩy thông báo chuyến —      │
│   con người chỉ cần xử lý exception.                        │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│   Giảm thời gian điều vận từ 4–6 phút → dưới 45 giây;       │
│   tỷ lệ tài xế nhận chuyến ngay lần đề xuất đầu ≥ 85%.      │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```

---

### 🃏 QUICK PROBLEM CARD #2

```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán (1 câu): Tự động phân loại lỗi pin BMS xe VinFast  │
│ từ log dữ liệu thô thay vì kỹ thuật viên đọc thủ công.      │
│                                                             │
│ Công ty thành viên: [x] VinFast                              │
│                                                             │
│ Ai đang đau (Actor)?                                         │
│   Kỹ thuật viên bảo trì tại trung tâm dịch vụ VinFast.      │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                         │
│   1. Xe EV gửi log lỗi về hệ thống giám sát từ xa           │
│      ──> 2. Kỹ thuật viên mở dashboard, đọc raw log         │
│      ──> 3. Phân loại lỗi theo danh mục (pin/BMS/nhiệt độ…) │
│      ──> 4. Tạo ticket bảo trì và phân công đội xử lý       │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất?                             │
│   Bước 2–3: Đọc và phân loại log kỹ thuật                   │
│   ⏱ ~15–20 phút/xe; ~100 xe cần review mỗi ngày             │
│                                                             │
│ AI có thể nhảy vào hỗ trợ ở bước nào?                       │
│   Bước 2–3: LLM đọc log thô, trích xuất mã lỗi, tự phân     │
│   loại và gợi ý mức độ ưu tiên — kỹ thuật viên chỉ cần      │
│   duyệt ticket đã được AI điền sẵn.                         │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│   Giảm thời gian phân loại log từ 15–20 phút → dưới 2 phút; │
│   độ chính xác phân loại lỗi của AI ≥ 90% so với chuyên gia.│
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```

---

### 🃏 QUICK PROBLEM CARD #3

```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán (1 câu): Tự động soạn phản hồi cá nhân hóa cho     │
│ đánh giá 1-sao của cư dân Vinhomes thay vì soạn thủ công.   │
│                                                             │
│ Công ty thành viên: [x] Vinhomes                             │
│                                                             │
│ Ai đang đau (Actor)?                                         │
│   Nhân viên CSKH Vinhomes và quản lý tòa nhà.               │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                         │
│   1. Cư dân gửi đánh giá 1-sao qua app/zalo/email           │
│      ──> 2. Nhân viên CSKH đọc nội dung khiếu nại           │
│      ──> 3. Phân loại vấn đề (thang máy/vệ sinh/bảo vệ…)   │
│      ──> 4. Soạn email phản hồi cá nhân hóa thủ công        │
│      ──> 5. Gửi cho cư dân và log ticket nội bộ             │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất?                             │
│   Bước 3–4: Phân loại và soạn phản hồi cá nhân hóa          │
│   ⏱ ~10 phút/yêu cầu; ~150 yêu cầu/ngày                    │
│                                                             │
│ AI có thể nhảy vào hỗ trợ ở bước nào?                       │
│   Bước 3–4: LLM đọc nội dung khiếu nại, phân loại chủ đề,   │
│   soạn draft phản hồi lịch sự và cá nhân hóa —              │
│   CSKH chỉ cần review và bấm gửi (Human-in-the-loop).       │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│   Giảm thời gian xử lý mỗi yêu cầu từ 10 phút → dưới 2     │
│   phút; tỷ lệ cư dân hài lòng với phản hồi ≥ 80%;           │
│   không có phản hồi nào bị gửi mà thiếu bước CSKH duyệt.   │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```

---

> *Hoàn thành bởi: [Ngô Xuân Hoàng] — VinUni Codelab Day 02*
