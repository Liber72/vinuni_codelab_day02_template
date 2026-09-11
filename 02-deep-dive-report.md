# 📘 02-deep-dive-report.md — Báo Cáo Phân Tích Sâu Dự Án AI (Vin Smart Future)

> **Dự án:** Xanh SM Intelligent Dispatcher Co-Pilot (Hệ thống Trợ lý Điều vận Thông minh & Cứu hộ Pin Thực địa)  
> **Đơn vị phát triển:** Vin Smart Future (Vingroup)  
> **Đơn vị tiếp nhận chuyển giao:** Công ty CP Di chuyển Xanh và Thông minh (GSM - Xanh SM)  
> **Người thực hiện:** Nguyễn Thế Khang — AI Product Engineer  
> **Bài toán lựa chọn:** Phân tích sâu & thiết kế giải pháp cho Quick Problem Card #1  

---

## 🏛️ 1. Tổng quan Dự án & Bối cảnh Nghiệp vụ

Trong hệ sinh thái di chuyển xanh của Vingroup, **Xanh SM** hiện đang vận hành đội xe thuần điện (EV) quy mô lớn nhất Việt Nam với hơn 30.000 xe taxi điện (VF5 Plus, VFe34, VF8) và xe máy điện Feliz S. 

Khác với xe xăng truyền thống, xe điện có những đặc thù vận hành mang tính sống còn:
1. **Dải pin tới hạn:** Khi dung lượng pin xuống dưới 5-10%, tốc độ sụt pin tăng nhanh do tiêu thụ phụ tải (điều hòa, định vị), nếu không được chỉ dẫn sạc kịp thời xe sẽ chết máy giữa đường và phải dùng xe cẩu kéo, gây ách tắc giao thông và giảm tuổi thọ pin pack.
2. **Khả năng tương thích trạm sạc:** Mỗi dòng xe hỗ trợ công suất sạc và chuẩn cổng khác nhau (sạc nhanh DC 30kW-60kW-150kW-250kW).
3. **Áp lực Trung tâm Điều vận (Dispatch Center):** Vào các khung giờ cao điểm (7h30-9h00 và 17h00-19h00) hoặc thời tiết mưa bão ngập lụt, số lượng cuộc gọi báo sự cố pin tăng vọt từ 15 lên tới 80-100 cuộc/giờ tại Hà Nội và TP.HCM, khiến các điều phối viên quá tải trầm trọng.

Dự án **Xanh SM Intelligent Dispatcher Co-Pilot** được xây dựng nhằm hỗ trợ điều phối viên tự động hóa việc tổng hợp tọa độ xe, kiểm tra tình trạng trạm sạc VinFast/V-GREEN trống, dự thảo chỉ dẫn sạc tối ưu và tự động kích hoạt quy trình điều xe sạc di động khi pin chạm ngưỡng nguy hiểm.

---

# 🏗️ Phase 3 — DEEP-DIVE

## 3.1. Quy trình vận hành hiện tại (Current-State Workflow Mapping)

Quy trình thủ công hiện tại khi một tài xế Xanh SM gặp sự cố pin giữa ca chạy:

```text
┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
│ Bước 1          │       │ Bước 2          │       │ Bước 3          │
│ Tiếp nhận cuộc  │ ───>  │ Tra cứu tọa độ  │ ───>  │ Tra cứu trạm sạc│
│ gọi / tin nhắn  │       │ & dải pin xe    │       │ VinFast trống   │
│                 │       │                 │       │                 │
│ Actor: Dispatch │       │ Actor: Dispatch │       │ Actor: Dispatch │
│ ⏱ 2 phút       │       │ ⏱ 2 phút        │       │ ⏱ 5 phút 🔴     │
│ In: Cuộc gọi KH │       │ In: Biển số xe  │       │ In: Tọa độ GPS  │
│ Out: Ticket log │       │ Out: Lat, Long  │       │ Out: Danh sách  │
└─────────────────┘       └─────────────────┘       └─────────────────┘
                                                             │
                                                             ▼
┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
│ Kết thúc        │       │ Bước 5          │       │ Bước 4          │
│ Tài xế di chuyển│ <───  │ Kích hoạt cứu hộ│ <───  │ Soạn thảo tin   │
│ tới trạm / chờ  │       │ (nếu pin < 5%)  │       │ nhắn hướng dẫn  │
│                 │       │                 │       │                 │
│ Actor: Tài xế   │       │ Actor: Dispatch │       │ Actor: Dispatch │
│ ⏱ Tùy lộ trình │       │ ⏱ 1 phút        │       │ ⏱ 5 phút 🔴     │
│                 │       │ In: Ticket info │       │ In: Dữ liệu thô │
│                 │       │ Out: Lệnh cứu hộ│       │ Out: Tin SMS/App│
└─────────────────┘       └─────────────────┘       └─────────────────┘

Ký hiệu:
🔴 Bottlenecks: Bước 3 (tra cứu thủ công) & Bước 4 (gõ tin chỉ dẫn thủ công)
🔄 Handoffs: Từ Tài xế ──> Dispatcher (Bước 1), Từ Dispatcher ──> Hệ thống bản đồ (Bước 2, 3), 
             Từ Dispatcher ──> Tài xế (Bước 4), Từ Dispatcher ──> Đội Cứu hộ pin V-GREEN (Bước 5)
⏱ Tổng thời gian xử lý trung bình hiện tại: 15 phút / sự cố.
```

---

## 3.2. Problem Statement (6-field) — Chuẩn Vin Smart Future

Bảng tuyên bố bài toán 6 trường thông tin định lượng:

| STT | Trường thông tin (Field) | Chi tiết phân tích bài toán Xanh SM |
|:---:|---|---|
| **1** | **Actor / Operator** | **Điều phối viên vận hành (Dispatcher)** tại Trung tâm Điều hành Xanh SM, phối hợp với **Tài xế thực địa** và **Đội xe sạc pin lưu động (Mobile Charging Van)**. |
| **2** | **Current Workflow** | Khi tài xế gọi điện/bấm nút SOS trên Driver App vì pin yếu, điều phối viên copy biển số xe sang hệ thống Telematics để xem tọa độ GPS và % pin còn lại. Sau đó, điều phối viên mở dashboard V-GREEN để tìm các trạm sạc gần nhất còn trụ trống, kiểm tra xem loại cổng có cắm vừa xe (VF5 sạc DC 30-60kW, VF8 sạc DC siêu nhanh), tính toán cự ly xem xe có lết tới nơi được không. Cuối cùng, gõ tin nhắn tiếng Việt gửi qua App tài xế chỉ đường, hoặc gọi điện cho đội xe cứu hộ nếu xe đã cạn pin. |
| **3** | **Bottleneck** | **Bước 3 & 4 (chiếm 10/15 phút):** Tra cứu phân tán giữa 2 màn hình dashboard, tính nhẩm bán kính an toàn, và soạn thảo tin nhắn chỉ dẫn bằng tay. Vào giờ cao điểm, việc gõ tay chậm dẫn đến trễ thông tin, tài xế hoảng loạn cố lái xe tìm trạm dẫn đến chết máy giữa đường. |
| **4** | **Business Impact** | - Mỗi ngày tại Hà Nội và TP.HCM ghi nhận trung bình **~120 sự cố cảnh báo pin khẩn cấp**.<br>- Tiêu tốn **~30 giờ công lao động/ngày** của đội ngũ điều phối viên chỉ để tra cứu và gõ tin nhắn lặp lại.<br>- Ước tính **5-8 xe/ngày** bị chết máy cạn pin giữa đường do chỉ dẫn chậm, phát sinh chi phí cẩu kéo cứu hộ (~1.200.000 VNĐ/lượt) và mất doanh thu khai thác cuốc xe (~800.000 VNĐ/ca xe). Tổng thiệt hại ước tính **~300 - 450 triệu VNĐ/tháng**. |
| **5** | **Success Metric** | 1. **Thời gian xử lý (Efficiency):** Giảm thời gian từ lúc nhận sự cố đến lúc gửi chỉ dẫn từ **15 phút ──> dưới 2.5 phút** (giảm > 80%).<br>2. **Độ chính xác an toàn (Safety & Quality):** Đạt **100%** không đề xuất trạm sạc cách xa quá 5km cho xe có pin `< 5%`. Tỉ lệ hướng dẫn đúng loại trụ sạc tương thích đạt **>= 98%**.<br>3. **Giảm thiểu xe chết máy (Business Metric):** Giảm tỉ lệ xe cạn pin phải cẩu kéo về xưởng ít nhất **70%**. |
| **6** | **Operational Boundary (Ranh giới an toàn)** | - **QUY TẮC BẮT BUỘC 1 (HITL Tag):** Toàn bộ nội dung văn bản chỉ dẫn do AI sinh ra phải luôn bắt đầu bằng tiền tố `[DRAFT_ONLY]`. Hệ thống phần mềm nghiệp vụ sẽ chặn không cho phép tự động gửi tin ra ngoài nếu thiếu nhãn này, bắt buộc điều phối viên là người click xác nhận duyệt cuối cùng.<br>- **QUY TẮC BẮT BUỘC 2 (Safety Boundary - Critical Battery):** Nếu xe báo pin `< 5%`, AI **TUYỆT ĐỐI KHÔNG ĐƯỢC** gợi ý trạm sạc cách xa trên 5km. Thay vào đó, AI bắt buộc phải trả về chỉ thị điều xe cứu hộ sạc di động: `{"action": "dispatch_mobile_charger", "reason": "<lý do cụ thể>"}`.<br>- **QUY TẮC 3:** AI không được tự ý trừ tiền hoặc tính phí cứu hộ của tài xế. |

---

## 3.3. Đánh giá AI Fit & Quy trình tương lai (Future-State Flow)

### Phân tích Ma trận AI-Fit (AI-Fit Matrix):
* **Lựa chọn kiến trúc:** **LLM Feature (Copilot with Strict Policy Boundaries & Structured Output)**.
* **Tại sao không dùng Pure Rule-based?** 
  - Rule thông thường chỉ lọc được trạm sạc theo cự ly hình học đơn thuần, nhưng không thể tổng hợp ngôn ngữ tự nhiên thành tin nhắn chỉ dẫn linh hoạt (hướng dẫn tài xế vị trí đặt trụ sạc trong hầm B2 TTTM Vincom, số hotline bảo vệ tòa nhà, điều kiện giao thông giờ cao điểm).
* **Tại sao KHÔNG dùng Autonomous Multi-Agent?** 
  - Điều phối cứu hộ xe điện ảnh hưởng trực tiếp đến an toàn tính mạng tài xế và tài sản xe (tránh nguy cơ chập cháy điện áp cao). Một Agent tự trị tự ý ra quyết định mà không có sự kiểm tra của con người tiềm ẩn rủi ro khôn lường (hallucination điều xe đi nhầm điểm). Do đó, mô hình **Copilot (Hỗ trợ con người)** kết hợp **Human-in-the-loop (HITL)** là lựa chọn tối ưu nhất.

### Sơ đồ Quy trình Tương lai (Future-State Flow):

```text
┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
│ Bước 1          │       │ Bước 2          │       │ Bước 3          │
│ Tài xế bấm nút  │ ───>  │ 🔵 Hệ thống tự   │ ───>  │ 🔵 Gemini 2.5   │
│ SOS trên App    │       │ động pull GPS & │       │ kiểm tra dải pin│
│                 │       │ trạm sạc trống  │       │ & draft chỉ dẫn │
│ Actor: Tài xế   │       │ (Backend API)   │       │                 │
│ ⏱ 5 giây       │       │ ⏱ 2 giây        │       │ ⏱ 3 giây        │
└─────────────────┘       └─────────────────┘       └─────────────────┘
                                                             │
                                                             ▼
┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
│ Bước 6          │       │ Bước 5          │       │ Bước 4          │
│ App nhận tin &  │ <───  │ 🟢 Dispatcher   │ <───  │ 🟢 Hiển thị tin │
│ điều hướng map  │       │ kiểm tra nhanh  │       │ nháp có gắn thẻ │
│ hoặc xe cứu hộ  │       │ & click DUYỆT   │       │ [DRAFT_ONLY]    │
│                 │       │ (1-click Send)  │       │                 │
│ Actor: Hệ thống │       │ Actor: Dispatch │       │ Actor: Giao diện│
│ ⏱ 2 giây        │       │ ⏱ 15 - 30 giây  │       │ ⏱ Tức thì       │
└─────────────────┘       └─────────────────┘       └─────────────────┘
                                  │
                                  ▼
                          ┌─────────────────┐
                          │ ↩️ Fallback      │
                          │ Khi AI timeout  │
                          │ hoặc JSON lỗi:  │
                          │ Chuyển về mẫu   │
                          │ tin nhắn chuẩn  │
                          │ có sẵn (Rule).  │
                          └─────────────────┘

Chú thích:
🔵 AI Step: Tác vụ tự động do hệ thống & Gemini 2.5 Flash xử lý.
🟢 Human Step (HITL): Bước điều phối viên con người kiểm soát và phê duyệt.
↩️ Fallback: Kế hoạch dự phòng đảm bảo hệ thống không bao giờ bị nghẽn mạch.
⏱ Tổng thời gian xử lý toàn trình: ~ 1 phút (so với 15 phút ban đầu).
```

---

# 🏁 Phase 5 — EVALUATE: Đánh Giá Sẵn Sàng & Quyết Định

## 5.1. AI Readiness Checklist (Đánh giá mức độ sẵn sàng)

| Tiêu chí sẵn sàng | Đánh giá thực tế tại Vin Smart Future & GSM | Đạt / Chưa đạt |
|---|---|:---:|
| **1. Dữ liệu mẫu/Logs sạch** | Đã có hệ thống Telematics của VinFast ghi nhận nhật ký GPS, mức pin từng phút của xe taxi Xanh SM. Cơ sở dữ liệu vị trí và số trụ sạc trống của hệ thống trạm sạc V-GREEN đã có API nội bộ kết nối sẵn. | **ĐẠT (Ready)** |
| **2. Kiểm soát rủi ro (HITL & Fallback)** | Cơ chế bắt buộc nhãn `[DRAFT_ONLY]` đảm bảo AI không bao giờ tự ý gửi tin sai lệch cho tài xế. Nếu pin `< 5%`, mô hình tự động chuyển hướng cứu hộ. Nếu API Gemini gặp sự cố, hệ thống tự fallback về template tin nhắn SMS cứng. | **ĐẠT (Ready)** |
| **3. Mức độ đón nhận của Stakeholders** | Đội ngũ điều phối viên Xanh SM đang rất áp lực vì quá tải giờ cao điểm, ban lãnh đạo GSM cực kỳ ủng hộ giải pháp hỗ trợ giảm tải và tối ưu chi phí cứu hộ. | **ĐẠT (Ready)** |
| **4. Chi phí suy luận & Hạ tầng** | Mô hình Gemini 2.5 Flash có chi phí suy luận cực kỳ thấp (~0.075 USD / triệu token), thời gian phản hồi dưới 1.5 giây, hoàn toàn phù hợp với ngân sách vận hành của GSM. | **ĐẠT (Ready)** |

---

## 5.2. Quyết định cuối cùng (Final Verdict)

* Ban Giám Đốc Công Nghệ **Vin Smart Future** và Khối Vận Hành **Xanh SM** thống nhất phê duyệt:

### ✅ **QUYẾT ĐỊNH: [ GO ] — BẮT ĐẦU XÂY DỰNG PROTOTYPE VÀ THỬ NGHIỆM THỰC ĐỊA**

### 📝 Lý giải quyết định (Justification):
1. **Giá trị kinh doanh cụ thể và hoàn vốn nhanh:** 
   - Giảm thời gian xử lý sự cố từ 15 phút xuống dưới 2.5 phút giúp tăng năng suất điều vận lên gấp **6 lần**.
   - Ngăn chặn triệt để tình trạng xe cạn kiệt pin giữa đường, tiết kiệm cho GSM ước tính hơn **3.5 tỷ VNĐ/năm** chi phí cứu hộ cẩu kéo và bảo dưỡng pin, đồng thời nâng cao chỉ số hài lòng của tài xế và hành khách.
2. **Kiến trúc kỹ thuật tối ưu và an toàn tuyệt đối:**
   - Việc lựa chọn mô hình **LLM Feature (Copilot)** với ranh giới an toàn nghiêm ngặt (Enforced System Instructions) và cơ chế duyệt **Human-in-the-loop** loại bỏ 100% rủi ro AI tự ý hành động gây lỗi hệ thống.
   - Luồng **Fallback** dự phòng đảm bảo tính liên tục trong vận hành 24/7 của Xanh SM ngay cả khi mất kết nối mạng bên ngoài.
3. **Lộ trình triển khai rõ ràng (Rollout Plan):**
   - **Giai đoạn 1 (Tuần 1-2):** Thử nghiệm nội bộ (Shadow Mode) trên 50 tài xế khu vực Ocean Park và Smart City Hà Nội.
   - **Giai đoạn 2 (Tuần 3-4):** Triển khai Copilot chính thức cho toàn bộ 50 bàn điều vận Xanh SM tại Hà Nội.
   - **Giai đoạn 3 (Tháng 2):** Mở rộng áp dụng cho TP.HCM và tích hợp sâu vào hệ thống V-GREEN toàn quốc.
