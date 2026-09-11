# Lab 02 — Worksheet: AI Product Scoping (Vin Smart Future)

---

## 🏛️ 1. Bối cảnh thực tế: Vin Smart Future (Vingroup)

**Vingroup** — Tập đoàn tư nhân lớn nhất Việt Nam — vừa sáp nhập toàn bộ các phòng ban công nghệ thuộc các công ty thành viên thành một đơn vị công nghệ thống nhất mang tên **Vin Smart Future**. 

Nhiệm vụ của **Vin Smart Future** là xây dựng các giải pháp AI, số hóa, và tự động hóa cốt lõi để nâng cao hiệu suất vận hành và trải nghiệm khách hàng xuyên suốt các công ty thành viên:
* 🚗 **VinFast:** Hệ thống xe điện thông minh (EV), trợ lý AI ảo trong xe, dự đoán bảo trì pin, và quản lý chuỗi cung ứng sản xuất.
* 🚕 **Xanh SM (GSM):** Vận hành đội xe taxi/xe máy điện thông minh, điều vận thông minh (Smart Dispatching), tối ưu hóa lộ trình di chuyển.
* 🏢 **Vinhomes:** Quản lý đô thị thông minh (Smart Cities), trợ lý cư dân thông minh, tối ưu hóa mức tiêu thụ năng lượng.
* 🏥 **Vinmec:** Y tế thông minh, chẩn đoán hình ảnh bằng AI, tối ưu hóa quản lý hồ sơ bệnh án.
* 🎢 **Vinpearl / VinWonders:** Trải nghiệm du lịch số hóa, quản lý phòng và luồng khách thông minh tại các khu vui chơi.

Trong buổi Lab hôm nay, nhóm của bạn sẽ đóng vai trò là **AI Product Engineer** tại **Vin Smart Future**, tiến hành tìm kiếm, scoping, phân tích độ khả thi, thiết lập ranh giới vận hành, và xây dựng một **bản mẫu kỹ thuật (prompt prototype)** cho một bài toán cụ thể thuộc một trong những mảng kinh doanh trên.

---

## 📊 2. Cơ cấu tính điểm bài lab

### 👥 Điểm nhóm (60 điểm)

| Gate | Điểm | Deliverable | Tiêu chí chấm |
|---|---:|---|---|
| **G1. Workflow Mapping** | 20 | Problem Deep-Dive | Vẽ chi tiết quy trình hiện tại: các bước, handoff, thời gian, bottleneck |
| **G2. Problem Statement** | 20 | Problem Deep-Dive | Problem Statement 6-field bám sát thực tế, metric có số và ranh giới rõ ràng |
| **G3. AI Fit & Future Flow** | 10 | Problem Deep-Dive | So sánh Rule vs LLM vs Agent, future flow có bước AI, ranh giới và Fallback |
| **G4. Decision Quality** | 10 | Problem Deep-Dive | Quyết định Go/Not Yet/No-Go trung thực và có chứng cứ rõ ràng |

### 👤 Điểm cá nhân (40 điểm)

| Gate | Điểm | Deliverable | Tiêu chí chấm |
|---|---:|---|---|
| **I1. Scan & Cards** | 15 | Quick Cards | Liệt kê 5 problems sử dụng 3 lenses, hoàn thiện 3 quick cards chất lượng |
| **I2. Prototyping** | 10 | 02-lab/ | Chạy thử nghiệm programmatic prompt prototype thành công |
| **I3. AI Log & Reflection** | 15 | 03-ai-log.md | Phản ánh trung thực về việc dùng AI làm thought-partner (giúp gì, sai gì, sửa gì) |

---

# 🚀 Phase 0 — worked Example: Xanh SM Intelligent Dispatcher (15 min)

*Giảng viên walk-through ví dụ thực tế từ Vin Smart Future để bạn hiểu rõ cách scoping một bài toán AI.*
Đọc chi tiết worked example tại file [02-deliverable-example.md](02-deliverable-example.md).

---

# 🔍 Phase 1 — SCAN (Cá nhân, 20 min)

Hãy sử dụng **4 Lenses** dưới đây để quét qua hoạt động vận hành của các công ty thành viên Vingroup. Ghi lại **ít nhất 5 bài toán/bottleneck** thực tế.

### 4 Lenses tìm bài toán AI cho Vingroup:
1. **Lặp lại (Repetitive):** Tác vụ lặp đi lặp lại nhiều lần hằng ngày. (Ví dụ: So khớp hóa đơn sạc điện tại VinFast, route lại chuyến taxi tại Xanh SM).
2. **Tốn thời gian (Time-consuming):** Tác vụ ngốn thời gian xử lý thủ công của nhân viên. (Ví dụ: Soạn thảo phản hồi đánh giá 1-star của cư dân Vinhomes).
3. **AI có thể tốt hơn (AI-upgrade):** Dịch vụ khách hàng hiện tại còn chậm hoặc phản hồi rập khuôn. (Ví dụ: Chatbot CSKH Vinpearl hỗ trợ đặt vé vui chơi).
4. **Pain từ người khác (Stakeholder Pain):** Bottleneck khiến khách hàng hoặc nhân viên thực địa phàn nàn. (Ví dụ: Tài xế Xanh SM phàn nàn về việc hệ thống gợi ý điểm đón khách không chính xác).

> [!TIP]
> **🤖 AI Prompts — Partner brainstorm:**
> Hãy sử dụng prompt sau để brainstorm các bài toán thực tế nếu bạn chưa có ý tưởng:
> *"Tôi là AI Engineer tại Vin Smart Future (Vingroup). Tôi đang tìm kiếm các pain point vận hành cụ thể có thể tối ưu bằng AI cho mảng [Chọn một: VinFast / Xanh SM / Vinhomes / Vinmec]. Hãy gợi ý cho tôi 5 quy trình nghiệp vụ thủ công, tốn nhiều thời gian và gây rò rỉ hiệu suất kèm con số thống kê ước tính về tổn thất."*

### 📝 List bài toán của tôi:
| # | Subsidiary (VinFast/Xanh SM...) | Lens | Mô tả ngắn bài toán |
|---|----------------------------------|------|---------------------|
| 1 | **Xanh SM (GSM)** | Tốn thời gian (Time-consuming) | Điều phối viên xử lý thủ công các báo cáo khẩn cấp của tài xế khi xe sắp hết pin/hỏng giữa đường, mất 12-15 phút để định vị và hướng dẫn trạm sạc hoặc điều xe cứu hộ. |
| 2 | **VinFast** | Lặp lại (Repetitive) | Nhân viên đối soát phải so khớp thủ công hàng nghìn phiên sạc xe điện hằng tuần giữa log dữ liệu từ các trụ sạc và hóa đơn thanh toán trên hệ thống. |
| 3 | **Vinhomes** | AI có thể tốt hơn (AI-upgrade) | Cư dân phản ánh trên App Vinhomes Resident mất nhiều tiếng chờ xử lý; hệ thống cần tự động phân loại mức độ khẩn cấp và chuyển tiếp đúng Ban Quản lý từng tòa nhà. |
| 4 | **Vinmec** | Pain từ người khác (Stakeholder Pain) | Bác sĩ mất 20-30 phút/bệnh nhân để tóm tắt bệnh án xuất viện thủ công, gây quá tải hành chính và khiến bệnh nhân/thân nhân phải chờ đợi lâu. |
| 5 | **Vinpearl** | Tốn thời gian (Time-consuming) | Bộ phận kinh doanh phải đọc thủ công các email đặt phòng khách đoàn phức tạp từ đại lý du lịch để tra cứu quỹ phòng trống và soạn báo giá. |

---

# 🃏 Phase 2 — QUICK-ASSESS (Cá nhân, 30 min)

Chọn **top 3 bài toán** từ danh sách trên và hoàn thiện **3 Quick Problem Cards** dưới đây:

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
  1. Tính cấp bách thời gian thực (Real-time critical): Ảnh hưởng trực tiếp đến an toàn vận hành xe điện và SLA phục vụ khách hàng của Xanh SM.
  2. Ranh giới an toàn rõ ràng: AI chỉ làm nhiệm vụ gợi ý/soạn thảo (`[DRAFT_ONLY]`) và có ranh giới kích hoạt xe cứu hộ khi pin `< 5%`.
  3. Hoàn toàn đồng bộ với mã nguồn mẫu trong `starter-code/prompt_prototype.py`.

---

# 🏗️ Phase 3 — DEEP-DIVE (Nhóm, 85 min)

## 3.1. Current-State Workflow Mapping (25 min)
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

## 3.2. Problem Statement (6-field) & Metrics (15 min)

| Field | Nội dung chi tiết |
|---|---|
| **1. Actor / Operator** | Điều phối viên trực ban (Dispatcher Co-pilot) thuộc Trung tâm Điều vận Taxi điện Xanh SM (GSM). |
| **2. Current Workflow** | Khi tài xế báo sự cố cạn pin hoặc không sạc được giữa đường, điều phối viên phải mở nhiều màn hình riêng biệt: hệ thống định vị GPS xe, dashboard mạng lưới trụ sạc VinFast, rồi gõ thủ công tin nhắn SMS/In-App hướng dẫn tài xế, hoặc gọi điện điều xe cứu hộ nếu pin dưới 5%. Quy trình qua 5 bước thủ công, mất trung bình 15 phút/lượt. |
| **3. Bottleneck** | **Bước 3 & 4 (chiếm 10/15 phút):** Tra cứu thủ công trụ sạc trống tương thích cổng sạc (CCS2/GBT) theo thời gian thực và tự soạn thảo tin nhắn hướng dẫn đường đi bằng ngôn ngữ tự nhiên. |
| **4. Business Impact** | Mỗi ngày có ~80 sự cố cảnh báo pin khẩn cấp tại Hà Nội và TP.HCM. Tốn ~20 giờ công/ngày của đội điều vận. Xe nằm chờ gây lãng phí cơ hội phục vụ cuốc khách, rò rỉ ~15% doanh thu ca chạy và gây bức xúc, hoang mang cho tài xế. |
| **5. Success Metric** | 1. **Efficiency (Hiệu suất):** Giảm tổng thời gian xử lý sự cố từ 15 phút ──> dưới 3 phút/lượt (giảm 80%).<br>2. **Accuracy (Độ chính xác):** 98% gợi ý trạm sạc đúng chủng loại cổng và còn trụ trống khả dụng.<br>3. **Safety (An toàn):** 100% các xe có pin < 5% được hệ thống tự động kích hoạt điều xe sạc di động (Zero stranded vehicles). |
| **6. Operational Boundary** | • **AI ĐƯỢC PHÉP:** Đọc tọa độ GPS, tra cứu dữ liệu trạm sạc VinFast, dự thảo tin nhắn hướng dẫn chuẩn Tiếng Việt bắt buộc có tag `[DRAFT_ONLY]`, và tạo lệnh gọi xe sạc pin di động (`dispatch_mobile_charger`) khi pin < 5%.<br>• **AI CẤM:** TUYỆT ĐỐI không được tự ý gửi tin đi cho tài xế khi chưa qua Điều phối viên phê duyệt (bắt buộc Human-In-The-Loop); TUYỆT ĐỐI không đề xuất trạm sạc xa > 5km khi pin < 5%. |

---

## 3.3. Future-State Flow & AI Fit (25 min)

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

# 💻 Phase 4 — TECHNICAL PROMPT PROTOTYPE (Nhóm, 30 min)

Để đảm bảo kỹ sư của Vin Smart Future luôn giữ vững năng lực lập trình, nhóm của bạn sẽ tiến hành **lập trình bản mẫu prompt** trực tiếp trên **Gemini 2.5 Flash** bằng Python để stress-test hệ thống.

### Hướng dẫn thực hiện:
1. Mở file [starter-code/prompt_prototype.py](starter-code/prompt_prototype.py) bằng VS Code/Cursor.
2. Hoàn thiện các nội dung sau:
   * **System Prompt:** Viết chỉ thị cực kỳ nghiêm ngặt quy định vai trò, nhiệm vụ, định dạng output và **Operational Boundary (Ranh giới cấm)** của mô hình.
   * **Structured Output:** Định nghĩa định dạng JSON output rõ ràng.
   * **Adversarial Test Cases:** Viết ít nhất 3 prompts "tấn công" (Adversarial inputs) cố tình dụ AI vượt ranh giới hoặc đưa ra câu trả lời không được phép để kiểm tra xem ranh giới của bạn có thực sự vững chắc.
3. Chạy file python:
   ```bash
   python3 prompt_prototype.py
   ```
4. Kiểm tra xem các ranh giới an toàn có bị LLM phá vỡ hay không và ghi lại kết quả vào worksheet.

---

# 🏁 Phase 5 — EVALUATE (Nhóm, 20 min)

### AI Readiness Checklist:
1. [x] Chúng tôi có sẵn dữ liệu mẫu/logs sạch để test? *(Đã có telemetry GPS và trạng thái trụ sạc VinFast theo thời gian thực).*
2. [x] Rủi ro khi AI sai có nằm trong tầm kiểm soát (qua HITL hoặc Fallback)? *(100% bản nháp phải qua HITL duyệt; có Fallback quy trình cũ nếu hệ thống AI offline).*
3. [x] Stakeholders sẵn sàng thay đổi quy trình làm việc cũ? *(Đội ngũ điều vận Xanh SM rất mong muốn giảm tải áp lực 20 giờ làm việc/ngày).*

### Quyết định cuối cùng của Ban Giám Đốc Vin Smart Future:
[x] **GO (Bắt đầu xây dựng Prototype):** Bắt đầu phát triển với scope hẹp (Pilot tại Hà Nội).
[ ] **NOT YET (Cần tích lũy thêm dữ liệu/xác lập baseline):** Trì hoãn để chuẩn bị thêm.
[ ] **NO-GO (Không khả thi / Rule-based tốt hơn):** Hủy bỏ dự án AI này.

**Justification (Lý giải quyết định dựa trên bằng chứng kỹ thuật và chi phí):**
> Dự án đạt mức độ **GO** hoàn toàn vì:
> 1. **Hiệu quả kinh tế cao (High ROI):** Giúp tiết kiệm 80% thời gian xử lý sự cố (từ 15 phút xuống dưới 3 phút), giải phóng 20 giờ lao động/ngày cho đội ngũ điều phối, giảm thiểu tỉ lệ tài xế dừng hoạt động giúp bảo vệ ~15% doanh thu cuốc xe.
> 2. **Chi phí công nghệ tối thiểu:** Sử dụng mô hình **Gemini 2.5 Flash** với chi phí inference cực thấp (~$0.0001 mỗi lượt request).
> 3. **Kiểm soát rủi ro an toàn tuyệt đối:** Ranh giới vận hành (Operational Boundary) được thiết lập chặt chẽ với cơ chế bắt buộc duyệt (Human-in-the-loop qua tag `[DRAFT_ONLY]`) và xử lý pin nguy cấp bằng xe sạc cứu hộ di động. Rủi ro vận hành gần như bằng 0.

---

# 📝 Phase 6 — REFLECTION (Cá nhân)
*Ghi nhận phản ánh của cá nhân bạn về việc phối hợp với AI trong buổi học hôm nay vào file `03-ai-log.md`.*
