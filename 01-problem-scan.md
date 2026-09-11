# Deliverable — Vin Smart Future (VinFast & GSM Use Cases)

## 🏛️ Bối cảnh: Tôi là ai?

Tôi là **Thái Đạt**, sinh viên ngành Fintech tại PTIT. Nhóm chúng tôi đại diện cho các kỹ sư trẻ tại **Vin Smart Future**, phối hợp cùng Khối Vận Hành của **VinFast**, **V-GREEN** và **GSM (Xanh SM)** để quét các cơ hội tối ưu hóa quy trình vận hành và nâng cao trải nghiệm người dùng bằng Trí tuệ Nhân tạo.

---

# 🔍 Phase 1 — SCAN: Tìm kiếm cơ hội (Cá nhân)

Dùng **4 Lenses** quét qua vận hành của các công ty thành viên Vingroup.

| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|------------|------|---------------------|
| 1 | **VinFast** | Pain từ người khác | Dịch vụ sạc xe điện: tài xế không muốn canh thời gian sạc để rút súng sạc. Xe sạc xong chiếm dụng trụ gây tắc nghẽn trạm và phát sinh phí phạt. Cần hệ thống điều phối kết thúc sạc và luân chuyển xe sang điểm đỗ an toàn. |
| 2 | **Xanh SM** | Lặp lại | Xử lý các vấn đề cơ bản và lặp đi lặp lại của tài xế và khách hàng như phản hồi ban đầu khi tài xế báo cáo sự cố, tai nạn giao thông trên đường. |
| 3 | **VinFast** | AI-upgrade | Trợ lý ảo trên xe tư vấn thông minh thời điểm sạc và tự động điều hướng đến trạm sạc tối ưu khi đang lái xe dựa trên lượng pin còn lại và tình trạng trụ trống thực tế. |
| 4 | **Vinhomes** | AI-upgrade | Hệ thống phân loại và route tự động các phản hồi/khiếu nại của cư dân trên App Vinhomes Resident (CSKH phản hồi rập khuôn, mất 12 tiếng). |
| 5 | **Xanh SM** | Tốn thời gian | Tóm tắt lý do khách hàng hủy chuyến từ cuộc gọi ghi âm và ghi chú của tài xế để tìm pattern lỗi hệ thống. |

---

# 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards (Cá nhân)

Chọn top 3 bài toán từ danh sách Phase 1: **Card #1 (VinFast Dịch vụ sạc & luân chuyển xe), Card #2 (Xanh SM Hỗ trợ sự cố khẩn cấp), Card #3 (VinFast Trợ lý tư vấn trạm sạc trên xe).**

---

### 📌 Thẻ bài toán 1: Card #1 — VinFast / V-GREEN Dịch vụ sạc xe điện thông minh & Điều phối luân chuyển trạm sạc (Smart Valet Charging)

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán (1 câu): Tài xế sạc xe điện không muốn canh giờ;   │
│ xe sạc đầy chiếm dụng trụ gây ùn tắc trạm và phạt đỗ quá giờ│
│ Cần hệ thống thông minh điều phối kết thúc sạc & dời xe.    │
│ Công ty thành viên: [x] VinFast / V-GREEN   [ ] Xanh SM     │
│                                                             │
│ Ai đang đau (Actor)? Tài xế xe điện (chờ đợi, lo bị phạt),  │
│                      Nhân viên vận hành trạm sạc (quá tải). │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Tài xế cắm sạc nhanh và rời xe đi ăn uống/làm việc     │
│   ──> 2. Canh giờ sạc thủ công bằng mắt hoặc đặt chuông     │
│   ──> 3. Phát hiện sạc xong, nhân viên đi tìm và gọi chủ xe │
│   ──> 4. Tài xế quay lại hoặc nhân viên valet dời xe ra bãi │
│   ──> 5. Bàn giao xe và xử lý khiếu nại phí chiếm trụ quá giờ│
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 3 & 4 (⏱ 15-20 min)    │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2, 3, 4          │
│ (AI dự báo thời điểm sạc xong qua Telematics -> Tìm ô đỗ    │
│  trống -> Soạn draft tin nhắn điều phối kèm ủy quyền Valet) │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ 1. Giảm thời gian chiếm trụ sau khi sạc xong từ 20m -> < 2m.│
│ 2. Tăng công suất quay vòng trụ trong giờ cao điểm thêm 20%.│
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```

---

### 📌 Thẻ bài toán 2: Card #2 — Xanh SM Trợ lý phân loại & Phản hồi khẩn cấp sự cố tài xế (Driver Incident Response Co-pilot)

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán (1 câu): Tiếp nhận, phân loại mức độ khẩn cấp và    │
│ tự động soạn phản hồi hướng dẫn xử lý ban đầu khi tài xế    │
│ Xanh SM gặp sự cố kỹ thuật xe hoặc va chạm trên đường.      │
│ Công ty thành viên: [ ] VinFast   [x] Xanh SM (GSM)         │
│                                                             │
│ Ai đang đau (Actor)? Điều phối viên tổng đài (Dispatcher),  │
│                      Tài xế gặp nạn trên đường (hoang mang).│
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Tài xế gọi hotline hoặc nhắn tin báo sự cố hiện trường │
│   ──> 2. Điều phối viên nghe, ghi chép tay địa điểm, sự việc│
│   ──> 3. Tra cứu quy trình xử lý theo loại sự cố (cứu hộ/y tế)
│   ──> 4. Soạn tin nhắn hướng dẫn các bước xử lý gửi tài xế  │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 & 3 (⏱ 8-12 min)     │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 & 3            │
│ (AI trích xuất tự động tọa độ, loại xe, tình trạng người    │
│  và xe -> Phân loại mức độ khẩn -> Draft hướng dẫn an toàn).│
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ 1. Giảm thời gian phản hồi hướng dẫn từ 10 min -> < 1 min.  │
│ 2. Tỷ lệ phân loại đúng mức độ khẩn cấp (Triage) đạt >= 95%.│
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```

---

### 📌 Thẻ bài toán 3: Card #3 — VinFast Trợ lý tư vấn lộ trình & Trạm sạc thông minh trên xe (In-car Charging Route Advisor)

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán (1 câu): Trợ lý ảo phân tích pin thực tế, lộ trình │
│ và mật độ trụ sạc để chủ động tư vấn thời điểm và điểm sạc  │
│ tối ưu nhất qua giọng nói cho người lái xe VinFast.         │
│ Công ty thành viên: [x] VinFast   [ ] Xanh SM   [ ] Vinhomes│
│                                                             │
│ Ai đang đau (Actor)? Chủ xe điện VinFast (lo hết pin giữa   │
│                      đường - range anxiety, mất tập trung). │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Tài xế lái xe, thỉnh thoảng liếc màn hình kiểm tra pin │
│   ──> 2. Pin dưới 20%, dừng xe hoặc vừa lái vừa mở app tìm  │
│   ──> 3. Tự so sánh khoảng cách và phỏng đoán trụ sạc trống │
│   ──> 4. Tự mở bản đồ Google Maps cài đặt điều hướng tới trạm│
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 & 3 (⏱ 5-7 min, nguy │
│ hiểm khi đang điều khiển phương tiện trên đường cao tốc).   │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 & 3            │
│ (AI tự kích hoạt khi pin chạm ngưỡng -> Dự báo trạm trống   │
│  theo thời gian thực -> Gợi ý 2 phương án sạc qua Voice AI). │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ 1. Giảm 100% việc tài xế phải dừng xe tra cứu app thủ công. │
│ 2. Tỷ lệ đến trạm có sẵn trụ sạc trống phù hợp đạt >= 90%.  │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```


# 🗳️ Quyết định lựa chọn của nhóm:
Nhóm quyết định chọn bài toán **"Card #1 — VinFast / V-GREEN Dịch vụ sạc xe điện thông minh & Điều phối luân chuyển trạm sạc"** để thực hiện Deep-Dive.

## Lý do lựa chọn Card #1 và loại bỏ các thẻ khác:
* **So với Card #2 (Xanh SM Hỗ trợ sự cố khẩn cấp):** Xử lý sự cố va chạm và tai nạn có liên quan đến tính mạng, hồ sơ công an và quy định bồi thường bảo hiểm phức tạp. Ranh giới an toàn (Operational Boundary) của AI trong mảng này khó cô lập và kiểm chứng trong phạm vi một bài lab kỹ thuật.
* **So với Card #3 (VinFast Trợ lý lộ trình trạm sạc):** Bài toán chủ yếu dựa trên thuật toán tối ưu hóa định tuyến bản đồ (Route Optimization / Dijkstra algorithm) kết hợp telemetry, vốn phần lớn có thể giải quyết tốt bằng rule-based truyền thống mà chưa khai thác tối đa thế mạnh xử lý ngôn ngữ và phối hợp đa bên của LLM.
* **Lý do chọn Card #1:** 
  1. **Tác động kinh doanh trực tiếp (High ROI):** Giải quyết bài toán nhức nhối nhất của hạ tầng xe điện VinFast — tình trạng "chiếm trụ sau khi sạc đầy" (idle chargers). Tăng trực tiếp doanh thu bán điện sạc và giảm chi phí đầu tư thêm trụ mới.
  2. **Dữ liệu rõ ràng (High AI Readiness):** Có sẵn luồng dữ liệu Telematics sạc (SoC %, dòng sạc, công suất, trạng thái trụ) và trạng thái ô đỗ xe.
  3. **Ranh giới an toàn rõ ràng (Strict Operational Boundary):** Dễ dàng thiết lập cơ chế Human-in-the-loop (HITL) với thẻ `[DRAFT_ONLY]` và ủy quyền số của tài xế, hoàn toàn phù hợp để prototype và kiểm thử ranh giới an toàn bằng LLM.
