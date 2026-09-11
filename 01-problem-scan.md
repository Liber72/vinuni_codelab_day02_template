# 📑 01-problem-scan.md — Quét & Đánh Giá Nhanh Cơ Hội AI (Vin Smart Future)

> **Học phần:** Lab 02 — AI Product Scoping  
> **Đơn vị:** Vin Smart Future (Vingroup)  
> **Người thực hiện:** Nguyễn Thế Khang — AI Product Engineer  
> **Mục tiêu:** Quét cơ hội vận hành trên các công ty thành viên Vingroup qua 4 Lenses và đánh giá nhanh 3 bài toán tiềm năng nhất.

---

## 🏛️ Bối cảnh: Tôi là ai?

Tôi là **Nguyễn Thế Khang**, AI Product Engineer tại **Vin Smart Future** (đơn vị công nghệ thống nhất của Tập đoàn Vingroup). Nhiệm vụ của tôi là khảo sát các điểm nghẽn (bottlenecks) trong vận hành thực tế tại các công ty thành viên: **VinFast, Xanh SM (GSM), Vinhomes, Vinmec, Vinpearl**, từ đó đánh giá tính khả thi và đề xuất các giải pháp AI mang lại giá trị kinh doanh đo lường được, kiểm soát được rủi ro vận hành.

---

# 🔍 Phase 1 — SCAN: Quét cơ hội qua 4 Lenses

Sử dụng **4 Lenses** phân tích nghiệp vụ:
1. **Lặp lại (Repetitive):** Tác vụ diễn ra tần suất cao, logic xử lý có tính quy luật lặp lại.
2. **Tốn thời gian (Time-consuming):** Tác vụ thủ công ngốn nhiều giờ của nhân sự trình độ cao.
3. **AI có thể tốt hơn (AI-upgrade):** Dịch vụ hiện tại rập khuôn, chưa cá nhân hóa, hoặc chậm trễ.
4. **Pain từ người khác (Stakeholder Pain):** Điểm nghẽn gây phàn nàn trực tiếp từ khách hàng hoặc nhân viên thực địa.

### 📝 Bảng quét 6 bài toán vận hành tại Vingroup:

| # | Đơn vị thành viên | Tên bài toán vận hành | Lens áp dụng | Mô tả ngắn bài toán & Điểm nghẽn hiện tại |
|---|-------------------|------------------------|--------------|--------------------------------------------|
| 1 | **Xanh SM (GSM)** | Xử lý sự cố pin khẩn cấp & điều vận cứu hộ pin | **Tốn thời gian & Stakeholder Pain** | Tài xế báo xe sắp hết pin hoặc sự cố trụ sạc giữa đường. Điều phối viên phải tra cứu bản đồ, kiểm tra trụ trống thủ công và soạn tin hướng dẫn (mất 12-15 phút/lượt), gây nguy cơ xe chết máy giữa đường. |
| 2 | **VinFast** | Phân loại và chẩn đoán sơ bộ lỗi xe từ mô tả tiếng Việt | **AI-upgrade & Lặp lại** | Khách hàng mô tả triệu chứng hỏng hóc bằng ngôn ngữ đời thường (ví dụ: *"xe đi qua gờ giảm tốc kêu lộc cộc phía trước"*). Kỹ thuật viên tiếp nhận mất 10-15 phút để tra cứu mã lỗi DTC sơ bộ. |
| 3 | **Vinhomes** | Phân loại và định tuyến thông minh phản ánh cư dân | **Lặp lại & Stakeholder Pain** | Mỗi ngày có hàng nghìn phản ánh qua App Vinhomes Resident (mùi rác, tiếng ồn, hỏng đèn...). Nhân viên CSKH phải đọc tay và chuyển tiếp thủ công tới từng ban quản lý tòa nhà, trễ SLA tiếp nhận. |
| 4 | **Vinmec** | Trợ lý trích xuất & soạn thảo tóm tắt bệnh án xuất viện (Discharge Summary) | **Tốn thời gian** | Bác sĩ điều trị mất 20-30 phút/bệnh nhân để tổng hợp xét nghiệm, phác đồ điều trị thành bản tóm tắt dễ hiểu cho bệnh nhân trước khi xuất viện. |
| 5 | **Vinpearl** | Tự động đọc và xử lý yêu cầu đặt phòng đoàn (Group Booking) | **Tốn thời gian & Lặp lại** | Nhân viên kinh doanh mất hàng giờ đọc email booking đoàn phức tạp của các công ty lữ hành, so khớp quỹ phòng trống trên hệ thống PMS và lập báo giá nháp. |
| 6 | **VinFast / V-GREEN** | Đối chiếu và phát hiện bất thường dữ liệu sạc điện | **Lặp lại** | So khớp hàng triệu phiên sạc xe điện hàng tuần giữa trạm sạc V-GREEN và hóa đơn đối soát đối tác để tìm giao dịch sai lệch hoặc rò rỉ điện năng. |

---

# 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

Từ danh sách trên, tôi chọn **Top 3 bài toán tiềm năng nhất** để phân tích sâu theo mẫu Quick Problem Card:
1. **Card #1:** Xanh SM — Điều phối cứu hộ pin & trạm sạc khẩn cấp cho tài xế taxi điện.
2. **Card #2:** VinFast — Trợ lý AI chẩn đoán sơ bộ và phân loại lỗi xe điện từ mô tả tiếng Việt.
3. **Card #3:** Vinhomes — Hệ thống phân loại và định tuyến phản ánh của cư dân theo thời gian thực.

---

### 📇 QUICK PROBLEM CARD #1 (Xanh SM)

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                                       │
│                                                                             │
│ Bài toán (1 câu): Hỗ trợ điều phối viên Xanh SM tra cứu trạm sạc khả dụng   │
│ và tự động soạn thảo chỉ dẫn khẩn cấp / điều xe cứu hộ cho tài xế taxi điện.│
│ Công ty thành viên: [x] Xanh SM (GSM)   [ ] VinFast   [ ] Vinhomes           │
│                                                                             │
│ Ai đang đau (Actor)?                                                        │
│ - Tài xế Xanh SM (lo lắng xe hết pin giữa đường, nguy cơ trễ cuốc của khách)│
│ - Điều phối viên tổng đài (Dispatcher) (áp lực xử lý gấp nhiều sự cố cùng lúc)│
│                                                                             │
│ Workflow thủ công hiện tại (5 bước):                                        │
│   1. Nhận báo cáo sự cố qua hotline/app ──>                                 │
│   2. Tra cứu tọa độ GPS của xe ──>                                          │
│   3. Mở hệ thống trạm VinFast kiểm tra trụ sạc trống phù hợp ──>            │
│   4. Soạn tin nhắn hướng dẫn đường đi & loại cổng sạc gửi tài xế ──>        │
│   5. Gọi đội xe cứu hộ pin di động nếu pin xe đã xuống mức nguy hiểm (< 5%).│
│                                                                             │
│ Bước nào tốn thời gian/lỗi nhất?                                            │
│   Bước 3 & 4 (⏱ 10-12 phút/lượt, dễ nhầm lẫn loại chân sạc hoặc trạm hết chỗ)│
│                                                                             │
│ AI có thể nhảy vào hỗ trợ ở bước nào?                                       │
│   Bước 3 & 4: Tự động tổng hợp dữ liệu GPS + trạm sạc trống gần nhất và     │
│   dùng LLM soạn sẵn tin nhắn nháp ([DRAFT_ONLY]) cho điều phối viên duyệt.  │
│   Nếu pin < 5%, cảnh báo và kích hoạt mẫu điều xe sạc di động ngay lập tức. │
│                                                                             │
│ Đo thành công bằng gì (Metric có số)?                                        │
│   - Giảm thời gian xử lý sự cố từ 15 phút ──> dưới 3 phút/lượt.             │
│   - Độ chính xác gợi ý trạm sạc đạt >= 98%.                                 │
│   - Giảm 80% trường hợp xe cạn pin phải cẩu kéo về xưởng.                   │
│                                                                             │
│ Quick Architecture: [x] LLM Feature (kết hợp HITL - Human in the loop)      │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 📇 QUICK PROBLEM CARD #2 (VinFast)

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                                       │
│                                                                             │
│ Bài toán (1 câu): Trích xuất triệu chứng hỏng hóc từ mô tả tự nhiên của     │
│ chủ xe VinFast để gợi ý nhóm mã lỗi kỹ thuật sơ bộ cho xưởng dịch vụ.       │
│ Công ty thành viên: [ ] Xanh SM   [x] VinFast   [ ] Vinmec                  │
│                                                                             │
│ Ai đang đau (Actor)?                                                        │
│ - Khách hàng sở hữu xe điện (không hiểu mã lỗi kỹ thuật, khó giải thích bệnh)│
│ - Cố vấn dịch vụ VinFast Service (mất nhiều thời gian gặng hỏi và tra sổ tay)│
│                                                                             │
│ Workflow thủ công hiện tại (4 bước):                                        │
│   1. Khách gọi/đến xưởng mô tả triệu chứng bằng lời nói ──>                 │
│   2. Cố vấn dịch vụ ghi chép triệu chứng vào phiếu giấy ──>                 │
│   3. Tra cứu catalog sự cố và đối chiếu mã lỗi kỹ thuật (DTC) ──>           │
│   4. Tạo phiếu tiếp nhận và chỉ định kỹ thuật viên chuyên trách.            │
│                                                                             │
│ Bước nào tốn thời gian/lỗi nhất?                                            │
│   Bước 2 & 3 (⏱ 12-15 phút/xe, ngôn ngữ khách hàng không đồng nhất).        │
│                                                                             │
│ AI có thể nhảy vào hỗ trợ ở bước nào?                                       │
│   Bước 2 & 3: Nhận diện thực thể (triệu chứng, vị trí, điều kiện xảy ra lỗi)│
│   từ mô tả tự do và map sang danh sách top 3 mã lỗi tiềm năng kèm câu hỏi    │
│   bổ trợ để cố vấn dịch vụ hỏi lại khách hàng.                              │
│                                                                             │
│ Đo thành công bằng gì (Metric có số)?                                        │
│   - Giảm thời gian tiếp nhận ban đầu từ 15 phút ──> dưới 4 phút.            │
│   - Tỉ lệ khớp đúng nhóm linh kiện/hệ thống cần kiểm tra đạt >= 90%.        │
│                                                                             │
│ Quick Architecture: [x] LLM Feature (kết hợp tra cứu dữ liệu kỹ thuật)      │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 📇 QUICK PROBLEM CARD #3 (Vinhomes)

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                                       │
│                                                                             │
│ Bài toán (1 câu): Tự động phân loại mức độ khẩn cấp và định tuyến phản ánh  │
│ của cư dân Vinhomes tới đúng bộ phận kỹ thuật / an ninh / vệ sinh tòa nhà.  │
│ Công ty thành viên: [ ] VinFast   [ ] Xanh SM   [x] Vinhomes                │
│                                                                             │
│ Ai đang đau (Actor)?                                                        │
│ - Cư dân khu đô thị Vinhomes (bực bội vì phản ánh chậm được xử lý)          │
│ - Nhân viên trực ban quản lý (quá tải vì đọc phân loại hàng trăm ticket/ngày)│
│                                                                             │
│ Workflow thủ công hiện tại (4 bước):                                        │
│   1. Cư dân gửi ticket khiếu nại qua App Vinhomes Resident ──>              │
│   2. CSKH tổng đọc nội dung, xác định tòa nhà và tính chất sự việc ──>      │
│   3. Gán nhãn thủ công (An ninh / Kỹ thuật / Vệ sinh / Cảnh quan) ──>        │
│   4. Forward ticket cho tổ kỹ thuật hoặc giám sát tòa nhà xử lý.            │
│                                                                             │
│ Bước nào tốn thời gian/lỗi nhất?                                            │
│   Bước 2 & 3 (⏱ trung bình mất 4-6 tiếng trong giờ cao điểm để chuyển tiếp).│
│                                                                             │
│ AI có thể nhảy vào hỗ trợ ở bước nào?                                       │
│   Bước 2 & 3: Phân loại tự động nội dung, trích xuất căn hộ/tòa nhà, phát   │
│   hiện từ khóa khẩn cấp (chập điện, cháy nổ, kẹt thang) để đẩy lên đầu hàng.│
│                                                                             │
│ Đo thành công bằng gì (Metric có số)?                                        │
│   - Giảm thời gian định tuyến từ 4 tiếng ──> dưới 30 giây (Real-time).       │
│   - Tỉ lệ phân loại đúng phòng ban đạt >= 95%.                              │
│                                                                             │
│ Quick Architecture: [x] LLM Feature / Rule-Router Hybrid                    │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

# 🗳️ Quyết định lựa chọn bài toán cho Deep-Dive

Sau khi so sánh 3 thẻ bài toán dựa trên các tiêu chí: **Tính khả thi kỹ thuật**, **Giá trị kinh doanh thực tế**, **Ranh giới an toàn (Operational Boundaries)** và **Khả năng xây dựng nguyên mẫu prompt (Prompt Prototyping)** trong khuôn khổ bài lab, tôi quyết định lựa chọn:

### 🎯 Bài toán được chọn: **QUICK PROBLEM CARD #1 — Xanh SM Xử lý sự cố pin khẩn cấp & điều vận cứu hộ pin**

### 💡 Lý do lựa chọn và phân tích loại trừ:
1. **Vì sao chọn Card #1 (Xanh SM):**
   - **Tính cấp bách và thời gian thực (Real-time):** Sự cố cạn pin của xe taxi điện ảnh hưởng trực tiếp đến an toàn giao thông, uy tín dịch vụ của Xanh SM và doanh thu của tài xế.
   - **Ranh giới vận hành rõ ràng, có rủi ro thực tế cần bảo vệ:** Cần có ranh giới nghiêm ngặt: nếu pin `< 5%`, mô hình **tuyệt đối không được chỉ dẫn đi trạm sạc xa (> 5km)** mà phải lập tức đề xuất **xe sạc di động (mobile charger)**; đồng thời mọi chỉ dẫn phải có thẻ `[DRAFT_ONLY]` để điều phối viên duyệt trước khi gửi (Human-in-the-loop).
   - **Phù hợp hoàn hảo với bài tập kỹ thuật (Phase 4):** Dễ dàng lập trình prompt prototype và thiết kế các bài test tấn công ranh giới an toàn (Adversarial Tests) bằng Python và Gemini 2.5 Flash.

2. **Lý do hoãn/loại trừ các bài toán khác:**
   - **Card #2 (VinFast - Chẩn đoán lỗi xe):** Đòi hỏi cơ sở dữ liệu kỹ thuật OBD-II và catalog độc quyền của VinFast (rào cản dữ liệu lớn, chưa sẵn sàng trong 1 buổi lab).
   - **Card #3 (Vinhomes - CSKH cư dân):** Có thể giải quyết hiệu quả bằng mô hình phân loại văn bản truyền thống hoặc rule-based router rẻ hơn mà không nhất thiết phải cần tới LLM phức tạp; rủi ro pháp lý về tranh chấp phí dịch vụ cần thêm thời gian khảo sát nghiệp vụ.
