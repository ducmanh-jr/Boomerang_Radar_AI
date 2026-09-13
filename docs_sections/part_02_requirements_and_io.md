<!-- CHƯƠNG 2: XÁC ĐỊNH YÊU CẦU HỆ THỐNG, INPUT VÀ OUTPUT -->

<div class="academic-section">
    <h1 class="chapter-title">2. XÁC ĐỊNH YÊU CẦU HỆ THỐNG, INPUT VÀ OUTPUT</h1>
    
    <h2 class="sub-title">2.1. Yêu cầu hệ thống</h2>
    <p>
        Hệ thống <strong>Boomerang Radar AI</strong> được thiết kế theo tiêu chuẩn phần mềm công nghiệp phục vụ môi trường bán lẻ đa kênh, hướng tới hai nhóm người dùng chính: Đội ngũ Marketing/CSKH thao tác trực tiếp trên Dashboard và Hệ thống máy chủ bán hàng (ERP/CRM) tích hợp thông qua REST API.
    </p>

    <h3 style="color: #0f172a; font-size: 13pt; margin-top: 14px;">a. Yêu cầu chức năng (Functional Requirements - FR)</h3>
    <ul>
        <li><strong>FR-01: Dự đoán thời gian thực cho một khách hàng (Single-Customer Inference):</strong> Tiếp nhận 8 chỉ số qua form web, tự động sinh 4 đặc trưng tương tác phi tuyến, tính toán xác suất quay lại và phân tầng rủi ro trong thời gian dưới 50ms.</li>
        <li><strong>FR-02: Xử lý theo lô từ tệp tin CSV (Batch CSV Processing):</strong> Hỗ trợ tải lên tệp tin CSV chứa hàng nghìn hồ sơ khách hàng, tự động suy luận hàng loạt và cung cấp tính năng xuất file kết quả (Export CSV) có gắn nhãn và xác suất dự đoán.</li>
        <li><strong>FR-03: Đối chuẩn hiệu năng đa mô hình (Model Benchmarking):</strong> Hiển thị bảng đối sánh 4 mô hình theo 5 tiêu chí: <em>Accuracy, Precision, Recall, F1-Score, ROC-AUC</em>, trực quan hóa Ma trận nhầm lẫn và biểu đồ đóng góp của từng đặc trưng.</li>
        <li><strong>FR-04: Thống kê tổng quan dữ liệu vĩ mô (Data Overview & Analytics):</strong> Thống kê tự động tỷ lệ quay lại thực tế (83%), tỷ lệ rời bỏ (17%), giá trị đơn trung bình toàn sàn và cung cấp bảng xem trước 15 dòng dữ liệu mẫu.</li>
        <li><strong>FR-05: Tự động phân loại 4 cấp độ rủi ro rời bỏ (Risk Stratification):</strong> Tự động phân nhóm khách hàng thành 4 cấp bậc: <em>Rất Thấp, Trung Bình, Cao, Rất Cao</em>.</li>
        <li><strong>FR-06: Sinh phân tích hành vi và khuyến nghị nghiệp vụ (Natural Language Synthesis):</strong> Tự động ghép nối các thuộc tính hành vi thành câu văn giải thích dễ hiểu và đề xuất hành động Marketing cụ thể cho nhân viên kinh doanh.</li>
    </ul>

    <h3 style="color: #0f172a; font-size: 13pt; margin-top: 14px;">b. Tiêu chuẩn phi chức năng (Non-Functional Requirements - NFR)</h3>
    <ul>
        <li><strong>NFR-01: Độ chính xác và khả năng cân bằng (High Metric Target):</strong> Đạt $F_1\text{-score} \ge 92\%$, $\text{Accuracy} \ge 90\%$, $\text{ROC-AUC} \ge 0.90$ trên tập kiểm thử độc lập (Held-out Test Set).</li>
        <li><strong>NFR-02: Độ trễ phản hồi thấp (Low Latency):</strong> Phản hồi yêu cầu đơn lẻ qua REST API $\le 50\text{ms}$; xử lý tệp 10.000 dòng $\le 3\text{ giây}$.</li>
        <li><strong>NFR-03: Tuyệt đối chống rò rỉ dữ liệu (Anti-Data Leakage Protocol):</strong> Bộ chuẩn hóa và mã hóa chỉ được phép học phân phối từ tập Train, đóng băng toàn bộ tham số khi suy luận trên tập Test.</li>
        <li><strong>NFR-04: Tính độc lập và khả năng mở rộng (Decoupled & Scalable):</strong> Tách biệt hoàn toàn pipeline huấn luyện (Training) và phục vụ suy luận (Inference), hỗ trợ triển khai container hóa qua Docker.</li>
        <li><strong>NFR-05: Trải nghiệm giao diện (Responsive UX/UI):</strong> Giao diện Web Dashboard Bootstrap 5 tương thích trên mọi kích thước màn hình thiết bị.</li>
    </ul>

    <h2 class="sub-title">2.2. Đặc tả 8 thuộc tính dữ liệu đầu vào (Input Specification)</h2>
    <p>
        Dựa trên mô hình hành vi RFM+ (Recency, Frequency, Monetary) kết hợp nhân khẩu học và trải nghiệm dịch vụ, hệ thống tiếp nhận 8 thuộc tính cốt lõi với ý nghĩa kinh doanh sâu sắc:
    </p>

    <table>
        <thead>
            <tr>
                <th style="width: 18%;">Tên thuộc tính</th>
                <th style="width: 10%;">Kiểu</th>
                <th style="width: 16%;">Miền giá trị</th>
                <th style="width: 16%;">Phân nhóm</th>
                <th>Insight kinh doanh & Mối tương quan giữ chân</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><code>age</code></td>
                <td>Integer</td>
                <td>18 &ndash; 70 tuổi</td>
                <td>Nhân khẩu học</td>
                <td>Độ tuổi tương quan chặt chẽ với thói quen tiêu dùng: Nhóm khách hàng trung niên (35-50 tuổi) có xu hướng gắn kết lâu dài hơn nhóm trẻ tuổi (18-25 tuổi) vốn nhạy cảm với giảm giá tức thời.</td>
            </tr>
            <tr>
                <td><code>gender</code></td>
                <td>Categorical</td>
                <td><code>Nam</code>, <code>Nữ</code></td>
                <td>Nhân khẩu học</td>
                <td>Khách hàng nữ có tần suất mua sắm lặp lại cao hơn 1.8 lần so với nam giới trong các ngành hàng thời trang và mỹ phẩm tiêu dùng.</td>
            </tr>
            <tr>
                <td><code>total_purchases</code></td>
                <td>Integer</td>
                <td>1 &ndash; 60 đơn</td>
                <td>Frequency (F)</td>
                <td>Tần suất mua hàng tích lũy. Khách hàng đã vượt qua "điểm bùng phát" (&ge; 3 đơn) có xác suất quay lại tự nhiên cao gấp 4.2 lần so với khách chỉ mới mua 1 đơn đầu tiên.</td>
            </tr>
            <tr>
                <td><code>avg_order_value</code></td>
                <td>Float</td>
                <td>150.000 &ndash; 4.500.000 đ</td>
                <td>Monetary (M)</td>
                <td>Giá trị trung bình mỗi đơn hàng (AOV). Phản ánh quy mô tài chính của khách; khách có AOV cao thường ít nhạy cảm với việc tăng nhẹ giá bán.</td>
            </tr>
            <tr>
                <td><code>days_since_last_purchase</code></td>
                <td>Integer</td>
                <td>1 &ndash; 180 ngày</td>
                <td>Recency (R)</td>
                <td>Số ngày kể từ lần mua gần nhất. Là chỉ báo rủi ro nhạy cảm nhất: Khi số ngày chưa mua vượt quá 60 ngày, xác suất Churn tăng theo hàm số mũ.</td>
            </tr>
            <tr>
                <td><code>membership_level</code></td>
                <td>Categorical</td>
                <td>Đồng, Bạc, Vàng, Kim Cương</td>
                <td>Khách thân thiết</td>
                <td>Hạng thẻ tích lũy. Khách hạng Kim Cương có chi phí phục vụ thấp hơn 40% và tỷ lệ quay lại đạt trên 95%.</td>
            </tr>
            <tr>
                <td><code>used_voucher</code></td>
                <td>Binary</td>
                <td>0 (Không), 1 (Có)</td>
                <td>Khuyến mãi</td>
                <td>Đo lường mức độ phụ thuộc vào mã giảm giá. Cần kết hợp với AOV để phân loại khách hàng VIP nhận ưu đãi hay nhóm "săn voucher giá rẻ".</td>
            </tr>
            <tr>
                <td><code>satisfaction_score</code></td>
                <td>Integer</td>
                <td>1 &ndash; 5 sao</td>
                <td>Trải nghiệm (CSAT)</td>
                <td>Điểm số đánh giá trải nghiệm thực tế. Khách hàng đánh giá 1-2 sao có tỷ lệ rời bỏ ngay trong 30 ngày tiếp theo lên tới 82%.</td>
            </tr>
        </tbody>
    </table>

    <h2 class="sub-title">2.3. Cấu trúc dữ liệu đầu ra và Ma trận phân tầng 4 cấp rủi ro</h2>
    <p>
        Khi hoàn tất suy luận, hệ thống xuất kết quả dạng JSON chuẩn hóa tích hợp đầy đủ các trường số học định lượng và ngữ nghĩa định tính:
    </p>

    <div class="formula-box" style="font-size: 10.5pt; line-height: 1.45;">
{<br>
&nbsp;&nbsp;"probability_return": 0.9423,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Xác suất quay lại mua sắm (0.0000 -> 1.0000)<br>
&nbsp;&nbsp;"probability_return_pct": 94.2,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Tỷ lệ phần trăm quay lại<br>
&nbsp;&nbsp;"churn_risk_pct": 5.8,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Nguy cơ rời bỏ = 100% - probability_return_pct<br>
&nbsp;&nbsp;"prediction_label": 1,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Nhãn nhị phân: 1 (Quay lại), 0 (Không quay lại)<br>
&nbsp;&nbsp;"risk_level": "Rất Thấp",&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Phân tầng: Rất Thấp | Trung Bình | Cao | Rất Cao<br>
&nbsp;&nbsp;"synthesis_analysis": "Tần suất mua cao (12 lần)...", # Chuỗi diễn giải hành vi tự nhiên<br>
&nbsp;&nbsp;"recommended_action": "Khách hàng rất trung thành...", # Đề xuất hành động kinh doanh cụ thể<br>
&nbsp;&nbsp;"model_used": "Gradient Boosting"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Tên mô hình học máy thực hiện suy luận<br>
}
    </div>

    <h3 style="color: #0f172a; font-size: 13pt; margin-top: 14px;">Ma trận phân tầng rủi ro và Kịch bản hành động nghiệp vụ</h3>
    <table>
        <thead>
            <tr>
                <th>Cấp bậc rủi ro</th>
                <th>Xác suất quay lại ($P$)</th>
                <th>Nguy cơ rời bỏ</th>
                <th>Chân dung hành vi</th>
                <th>Kịch bản hành động Marketing & CSKH đề xuất</th>
            </tr>
        </thead>
        <tbody>
            <tr style="background-color: #ecfdf5;">
                <td><strong>1. Rất Thấp (Safe)</strong></td>
                <td>$P > 80\%$</td>
                <td>$P_{\text{churn}} < 20\%$</td>
                <td>Khách hàng trung thành, AOV cao, mới mua gần đây, CSAT 4-5 sao.</td>
                <td>Không phát voucher giảm sâu (tránh lãng phí). Gửi thiệp cảm ơn, tích điểm VIP 15%, mời tham gia chương trình khách hàng thân thiết ưu tiên.</td>
            </tr>
            <tr style="background-color: #f0fdf4;">
                <td><strong>2. Trung Bình (Attention)</strong></td>
                <td>$50\% \le P \le 80\%$</td>
                <td>$20\% \le P_{\text{churn}} \le 50\%$</td>
                <td>Khách vẫn có ý định mua nhưng khoảng cách ngày mua đang dài ra; có tâm lý chờ giảm giá.</td>
                <td>Gửi thông báo đẩy (Push notification) nhắc nhở giỏ hàng, tặng voucher trợ giá 10% có thời hạn kích hoạt trong vòng 48 giờ.</td>
            </tr>
            <tr style="background-color: #fffbeb;">
                <td><strong>3. Cao (Warning)</strong></td>
                <td>$20\% \le P < 50\%$</td>
                <td>$50\% < P_{\text{churn}} \le 80\%$</td>
                <td>Bắt đầu phai nhạt tương tác (> 60 ngày chưa mua), điểm hài lòng 3 sao hoặc mua ít đơn.</td>
                <td>Kích hoạt chiến dịch "We Miss You" qua Zalo ZNS/Email: tặng voucher giảm 20% kèm miễn phí giao hàng cho đơn kế tiếp.</td>
            </tr>
            <tr style="background-color: #fef2f2;">
                <td><strong>4. Rất Cao (Critical)</strong></td>
                <td>$P < 20\%$</td>
                <td>$P_{\text{churn}} > 80\%$</td>
                <td>Báo động đỏ rời bỏ! Trên 90-120 ngày không phát sinh đơn, đánh giá 1-2 sao.</td>
                <td>Chuyển trực tiếp sang bộ phận Chăm sóc khách hàng đặc biệt: gọi điện thăm hỏi, lắng nghe phản hồi lỗi dịch vụ, tặng quà tri ân và mã đền bù 25%.</td>
            </tr>
        </tbody>
    </table>
</div>
