# 01 — Problem Scan & Quick Problem Cards (Vin Smart Future)

**Sinh viên / Nhóm thực hiện:** AI Product Engineer @ Vin Smart Future  
**Bối cảnh:** Quét cơ hội tối ưu hóa bằng AI xuyên suốt các công ty thành viên Vingroup.

---

## 🔍 Phase 1 — SCAN: Danh sách 5 bài toán vận hành thực tế

| # | Subsidiary (VinFast/Xanh SM...) | Lens | Mô tả ngắn bài toán |
|---|----------------------------------|------|---------------------|
| 1 | **Xanh SM (GSM)** | Tốn thời gian (Time-consuming) | Điều phối viên xử lý thủ công các báo cáo khẩn cấp của tài xế khi xe sắp hết pin/hỏng giữa đường, mất 12-15 phút để định vị và hướng dẫn trạm sạc hoặc điều xe cứu hộ. |
| 2 | **VinFast** | Lặp lại (Repetitive) | Nhân viên đối soát phải so khớp thủ công hàng nghìn phiên sạc xe điện hằng tuần giữa log dữ liệu từ các trụ sạc và hóa đơn thanh toán trên hệ thống. |
| 3 | **Vinhomes** | AI có thể tốt hơn (AI-upgrade) | Cư dân phản ánh trên App Vinhomes Resident mất nhiều tiếng chờ xử lý; hệ thống cần tự động phân loại mức độ khẩn cấp và chuyển tiếp đúng Ban Quản Lý từng tòa nhà. |
| 4 | **Vinmec** | Pain từ người khác (Stakeholder Pain) | Bác sĩ mất 20-30 phút/bệnh nhân để tóm tắt bệnh án xuất viện thủ công, gây quá tải hành chính và khiến bệnh nhân/thân nhân phải chờ đợi lâu. |
| 5 | **Vinpearl** | Tốn thời gian (Time-consuming) | Bộ phận kinh doanh phải đọc thủ công các email đặt phòng khách đoàn phức tạp từ đại lý du lịch để tra cứu quỹ phòng trống và soạn báo giá. |

---

## 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

### 🎴 QUICK PROBLEM CARD #1: Xanh SM — Xử lý sự cố sạc pin / hết pin khẩn cấp thực địa
```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán (1 câu): Tài xế Xanh SM báo cáo sự cố sắp hết pin  │
│ (< 5%) hoặc cạn kiệt pin giữa đường cần điều phối xe cứu hộ │
│ hoặc chỉ đường đến trạm sạc VinFast khả dụng gần nhất.       │
│ Công ty thành viên: [ ] VinFast  [x] Xanh SM  [ ] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? Tài xế (bị động, lo lắng bị phạt/mất   │
│ khách), Điều phối viên trực ca (Dispatchers - quá tải ca trực).│
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Tài xế gọi/nhắn tin báo nguy cấp về tình trạng pin     │
│   ──> 2. Điều phối viên tra cứu vị trí GPS xe trên màn hình │
│   ──> 3. Tra cứu thủ công các trạm sạc VinFast còn trụ trống │
│   ──> 4. Soạn tin nhắn hướng dẫn đường đi cho tài xế        │
│   ──> 5. Gọi đội xe sạc di động (Mobile Charger) nếu pin <5%│
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 3 & 4 (⏱ 12 phút/lượt) │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 3 & 4 (Tự động    │
│ hóa đọc định vị/mức pin -> Gợi ý trạm sạc trống hoặc kích   │
│ hoạt cứu hộ -> Draft tin nhắn kèm nhãn [DRAFT_ONLY]).        │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ - Giảm thời gian xử lý sự cố từ 15 phút ──> dưới 3 phút/lượt.│
│ - 100% xe pin < 5% được điều xe sạc di động, không bị chết máy.│
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```

### 🎴 QUICK PROBLEM CARD #2: Vinhomes — Phân loại & Điều hướng phản ánh cư dân
```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán (1 câu): Cư dân gửi phản ánh sự cố trên App        │
│ Vinhomes Resident nhưng chatbot phản hồi chậm và chuyển sai │
│ bộ phận kỹ thuật / Ban Quản Lý (BQL) từng tòa nhà.          │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [x] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? Cư dân (bức xúc chờ đợi), Nhân viên    │
│ CSKH/Điều phối viên Vinhomes (quá tải đọc hàng nghìn ticket).│
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Cư dân gửi nội dung phản ánh qua ứng dụng Resident     │
│   ──> 2. CSKH trung tâm đọc nội dung và phân loại thủ công   │
│   ──> 3. Xác định tòa nhà, mức độ khẩn cấp (nước/điện/ồn)    │
│   ──> 4. Tạo phiếu yêu cầu và chuyển về BQL tòa nhà phụ trách│
│   ──> 5. Kỹ thuật viên tòa nhà tiếp nhận và xử lý thực địa   │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 & 3 (⏱ 15 phút/ticket,│
│ độ trễ chuyển giao kéo dài 8-12 tiếng).                      │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 & 3 (Phân tích   │
│ ngữ nghĩa khiếu nại -> Gán tag khẩn cấp -> Điều hướng ticket).│
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ - Rút ngắn thời gian phân loại & routing từ 8 tiếng ──> <15p.│
│ - Độ chính xác định tuyến ticket tới đúng BQL đạt trên 92%. │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```

### 🎴 QUICK PROBLEM CARD #3: Vinmec — Soạn thảo tóm tắt hồ sơ xuất viện (Discharge Summary)
```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán (1 câu): Bác sĩ mất quá nhiều thời gian đọc lại    │
│ bệnh án điện tử để soạn thảo văn bản tóm tắt xuất viện bằng  │
│ ngôn ngữ phổ thông cho bệnh nhân.                           │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes  │
│                     [x] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? Bác sĩ điều trị (quá tải thủ tục giấy  │
│ tờ), Bệnh nhân/người nhà (chờ đợi lâu để thanh toán ra viện).│
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Bác sĩ mở EMR đọc lịch sử điều trị, xét nghiệm, thuốc  │
│   ──> 2. Gõ thủ công văn bản tóm tắt tình trạng và kết quả   │
│   ──> 3. Viết lời dặn tái khám và hướng dẫn sử dụng thuốc    │
│   ──> 4. Trưởng khoa rà soát, ký số và in bàn giao           │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 1 & 2 (⏱ 25-30 phút/ca) │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 1 & 2 (Đọc tóm tắt│
│ hồ sơ bệnh án ẩn danh -> Draft trước bản tóm tắt xuất viện   │
│ để bác sĩ chỉ cần review và chỉnh sửa).                      │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ - Giảm thời gian soạn thảo từ 25-30 phút ──> dưới 5 phút/ca. │
│ - 100% bản tóm tắt bắt buộc phải qua Bác sĩ duyệt (HITL).    │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```

### 🎯 Quyết định lựa chọn bài toán cho Phase 3 (DEEP-DIVE):
* **Bài toán được chọn:** **Card #1 (Xanh SM — Xử lý sự cố sạc pin / hết pin khẩn cấp thực địa)**.
* **Lý do lựa chọn:**
  1. **Tính cấp bách thời gian thực (Real-time critical):** Ảnh hưởng trực tiếp đến an toàn vận hành xe điện và SLA phục vụ khách hàng của Xanh SM.
  2. **Ranh giới an toàn rõ ràng (Strict Operational Boundary):** AI chỉ đóng vai trò trợ lý soạn thảo (`[DRAFT_ONLY]`) và có ranh giới kích hoạt xe cứu hộ khi pin `< 5%` để đảm bảo an toàn tuyệt đối.
  3. **Đồng bộ với Prototype kỹ thuật:** Hoàn toàn ăn khớp với mã nguồn mẫu trong `starter-code/prompt_prototype.py`.
