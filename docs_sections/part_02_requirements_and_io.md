<!-- CHƯƠNG 2: XÁC ĐỊNH YÊU CẦU, INPUT VÀ OUTPUT -->

<div class="academic-section">
    <h1 class="chapter-title">CHƯƠNG 2: XÁC ĐỊNH YÊU CẦU HỆ THỐNG, INPUT VÀ OUTPUT</h1>
    
    <h2 class="sub-title">2.1. Phân tích yêu cầu hệ thống</h2>
    <p>
        Hệ thống <strong>Boomerang Radar AI</strong> được thiết kế theo các tiêu chuẩn kỹ thuật phần mềm và kiến trúc học máy hướng dịch vụ (Service-Oriented Machine Learning Architecture). Hệ thống phải đáp ứng đầy đủ cả hai nhóm yêu cầu chức năng và phi chức năng nhằm phục vụ song song cho hai nhóm đối tượng: Chuyên viên Marketing/Bán hàng (thao tác trên giao diện trực quan) và Kỹ sư phần mềm/Hệ sinh thái bên ngoài (tích hợp qua API).
    </p>

    <h3 style="color: #0f172a; font-size: 14px;">2.1.1. Yêu cầu chức năng (Functional Requirements - FR)</h3>
    <ul>
        <li>
            <strong>FR-01: Dự đoán thời gian thực cho một khách hàng đơn lẻ (Real-Time Single Prediction):</strong><br>
            Cung cấp giao diện form web nhập liệu trực quan cho 8 chỉ số hành vi. Sau khi người dùng nhấn nút "Dự đoán", hệ thống chuyển đổi dữ liệu, thực hiện suy luận qua mô hình AI đã huấn luyện và phản hồi kết quả trong thời gian thực dưới 100 mili-giây.
        </li>
        <li>
            <strong>FR-02: Dự đoán hàng loạt theo lô từ tệp tin CSV (Batch CSV Prediction):</strong><br>
            Cho phép người dùng tải lên tệp tin định dạng <code>.csv</code> chứa từ vài trăm đến hàng chục nghìn bản ghi khách hàng. Hệ thống tự động kiểm tra tính hợp lệ của cấu trúc cột, thực hiện xử lý theo lô và trả về bảng kết quả phân loại kèm tính năng xuất tệp <strong>Export CSV</strong> đã bổ sung cột nhãn và xác suất.
        </li>
        <li>
            <strong>FR-03: Khảo sát và đối chuẩn mô hình (Model Benchmarking Dashboard):</strong><br>
            Cung cấp bảng so sánh chi tiết giữa 4 mô hình học máy theo các chỉ số: <em>Accuracy, Precision, Recall, F1-Score, ROC-AUC</em>. Hiển thị trực quan Ma trận nhầm lẫn (Confusion Matrix) dạng lưới và biểu đồ xếp hạng độ quan trọng của các đặc trưng (Feature Importance).
        </li>
        <li>
            <strong>FR-04: Thống kê và khám phá dữ liệu (Data Overview & Analytics):</strong><br>
            Tự động nạp và thống kê các chỉ số kinh doanh vĩ mô từ tệp dữ liệu sạch: tổng số lượng khách hàng, tỷ lệ khách quay lại thực tế, tỷ lệ rời bỏ, giá trị đơn hàng trung bình toàn hệ thống và bảng xem trước (preview) dữ liệu mẫu.
        </li>
        <li>
            <strong>FR-05: Tự động phân tầng mức độ rủi ro (Risk Stratification Engine):</strong><br>
            Căn cứ vào xác suất quay lại tính toán được, hệ thống tự động phân loại khách hàng vào 4 phân khúc rủi ro: <em>Rất Thấp, Trung Bình, Cao, Rất Cao (Nguy cơ Churn)</em>.
        </li>
        <li>
            <strong>FR-06: Sinh phân tích hành vi và đề xuất hành động nghiệp vụ (Synthesis & Actionable Recommendation):</strong><br>
            Dựa trên sự kết hợp giữa 8 thuộc tính RFM+ và cấp độ rủi ro, hệ thống tự động sinh câu văn giải thích ngắn gọn hành vi mua sắm và đưa ra kịch bản Marketing/CSKH cụ thể cho nhân viên kinh doanh.
        </li>
    </ul>

    <h3 style="color: #0f172a; font-size: 14px;">2.1.2. Yêu cầu phi chức năng (Non-Functional Requirements - NFR)</h3>
    <ul>
        <li>
            <strong>NFR-01: Tiêu chuẩn độ chính xác cao (High Accuracy & Balance):</strong><br>
            Do đặc thù dữ liệu phân loại nhị phân thực tế có tính mất cân bằng tự nhiên (Imbalanced Dataset), hệ thống đặt mục tiêu tối thượng vào việc tối ưu chỉ số $F_1\text{-score} \ge 92\%$, đồng thời đảm bảo $\text{Accuracy} \ge 90\%$ và chỉ số $\text{ROC-AUC} \ge 0.90$ trên tập kiểm thử độc lập (Held-out Test Set).
        </li>
        <li>
            <strong>NFR-02: Độ trễ phản hồi cực thấp (Low Latency):</strong><br>
            Bộ máy suy luận (Inference Engine) phải tối ưu hóa cấu trúc nạp mô hình vào bộ nhớ RAM (Lazy-loaded singleton model artifact), đảm bảo thời gian xử lý một yêu cầu qua REST API $\le 50\text{ms}$.
        </li>
        <li>
            <strong>NFR-03: Bảo toàn tính phân bố và chống rò rỉ dữ liệu (Anti-Data Leakage Protocol):</strong><br>
            Quy trình tiền xử lý phải cô lập hoàn toàn giữa tập huấn luyện và tập kiểm thử. Bộ chuẩn hóa (Scaler) và bộ mã hóa (Encoder) chỉ được phép học các tham số thống kê ($\mu, \sigma$) trên tập Train để đảm bảo mô hình không bị "học vẹt" trước các phân phối của tập Test.
        </li>
        <li>
            <strong>NFR-04: Tính mở rộng và khả năng tích hợp (Extensibility & Portability):</strong><br>
            Kiến trúc mã nguồn được phân rã thành các module độc lập (Data Processing, Training, Inference, API Web). Toàn bộ mô hình và bộ biến đổi được lưu trữ dưới dạng nhị phân <code>.joblib</code>, cho phép dễ dàng container hóa qua Docker hoặc tích hợp vào hệ thống ERP/CRM của doanh nghiệp.
        </li>
        <li>
            <strong>NFR-05: Trải nghiệm người dùng (UX/UI Responsiveness):</strong><br>
            Giao diện Web Dashboard được xây dựng trên nền tảng Bootstrap 5 tương thích trên cả trình duyệt máy tính để bàn (Desktop), máy tính bảng và thiết bị di động.
        </li>
    </ul>

    <h2 class="sub-title">2.2. Đặc tả dữ liệu đầu vào (Input Specification)</h2>
    <p>
        Để mô tả toàn diện chân dung khách hàng mà không làm phức tạp hóa quá trình nhập liệu, hệ thống chọn lọc <strong>8 đặc trưng cốt lõi</strong> thuộc 4 nhóm nghiệp vụ chính: Nhân khẩu học, Hành vi giao dịch RFM (Recency, Frequency, Monetary), Hành vi khuyến mãi và Phản hồi trải nghiệm dịch vụ.
    </p>

    <table>
        <thead>
            <tr>
                <th>Tên thuộc tính</th>
                <th>Kiểu dữ liệu</th>
                <th>Miền giá trị hợp lệ</th>
                <th>Phân loại nghiệp vụ</th>
                <th>Ý nghĩa kinh doanh & Ràng buộc logic</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><code>age</code></td>
                <td>Integer</td>
                <td>$18 \le \text{age} \le 70$</td>
                <td>Nhân khẩu học</td>
                <td>Độ tuổi sinh học của khách hàng. Nhóm khách hàng trẻ thường nhạy cảm với khuyến mãi hơn nhóm trung niên.</td>
            </tr>
            <tr>
                <td><code>gender</code></td>
                <td>Categorical</td>
                <td><code>Nam</code>, <code>Nữ</code></td>
                <td>Nhân khẩu học</td>
                <td>Giới tính khách hàng. Dùng để cá nhân hóa danh mục sản phẩm gợi ý khi tái kích hoạt.</td>
            </tr>
            <tr>
                <td><code>total_purchases</code></td>
                <td>Integer</td>
                <td>$1 \le \text{total} \le 60$ (đơn)</td>
                <td>Tần suất (Frequency)</td>
                <td>Tổng số lượng đơn hàng mà khách hàng đã thực hiện thành công kể từ khi đăng ký tài khoản.</td>
            </tr>
            <tr>
                <td><code>avg_order_value</code></td>
                <td>Float</td>
                <td>$150.000 \le \text{AOV} \le 4.500.000$ đ</td>
                <td>Giá trị tiền tệ (Monetary)</td>
                <td>Giá trị trung bình trên mỗi đơn hàng (VNĐ). Phản ánh khả năng chi trả và mức độ giàu có của khách hàng.</td>
            </tr>
            <tr>
                <td><code>days_since_last_purchase</code></td>
                <td>Integer</td>
                <td>$1 \le \text{days} \le 180$ (ngày)</td>
                <td>Độ mới tương tác (Recency)</td>
                <td>Khoảng cách thời gian tính bằng ngày kể từ giao dịch thành công gần nhất. Biến số nhạy cảm nhất đối với nguy cơ rời bỏ.</td>
            </tr>
            <tr>
                <td><code>membership_level</code></td>
                <td>Categorical</td>
                <td><code>Đồng</code>, <code>Bạc</code>, <code>Vàng</code>, <code>Kim Cương</code></td>
                <td>Khách hàng thân thiết</td>
                <td>Hạng thẻ tích lũy dựa trên doanh thu. Phản ánh mức độ gắn kết chính sách và quyền lợi khách hàng thân thiết.</td>
            </tr>
            <tr>
                <td><code>used_voucher</code></td>
                <td>Binary</td>
                <td>$0$ (Không), $1$ (Có)</td>
                <td>Hành vi khuyến mãi</td>
                <td>Đo lường sự phụ thuộc vào các chương trình kích cầu giảm giá của khách hàng.</td>
            </tr>
            <tr>
                <td><code>satisfaction_score</code></td>
                <td>Integer</td>
                <td>$1, 2, 3, 4, 5$ (sao)</td>
                <td>Chất lượng dịch vụ (CSAT)</td>
                <td>Điểm số đánh giá trải nghiệm mua sắm gần nhất từ các phiếu khảo sát CSAT hoặc đánh giá đơn hàng.</td>
            </tr>
        </tbody>
    </table>

    <h2 class="sub-title">2.3. Đặc tả cấu trúc dữ liệu đầu ra và logic phân tầng rủi ro (Output)</h2>
    <p>
        Khi tiếp nhận một bản ghi thông tin khách hàng, hệ thống thực hiện pipeline suy luận và cấu trúc hóa kết quả đầu ra dưới định dạng JSON tiêu chuẩn phục vụ trực tiếp cho giao diện và hệ thống ngoài:
    </p>

    <div class="formula-box" style="font-size: 11px; line-height: 1.4;">
{<br>
&nbsp;&nbsp;"probability_return": 0.9423,<br>
&nbsp;&nbsp;"probability_return_pct": 94.2,<br>
&nbsp;&nbsp;"churn_risk_pct": 5.8,<br>
&nbsp;&nbsp;"prediction_label": 1,<br>
&nbsp;&nbsp;"label_formatted": "Nhãn 1 (Quay lại)",<br>
&nbsp;&nbsp;"status_text": "Quay lại mua sắm",<br>
&nbsp;&nbsp;"threshold_used": 0.50,<br>
&nbsp;&nbsp;"risk_level": "Rất Thấp",<br>
&nbsp;&nbsp;"synthesis_analysis": "Tần suất mua cao (12 lần) giá trị đơn lớn (1.850.000 VNĐ) mới mua dưới 30 ngày (14 ngày) điểm hài lòng tốt (5/5).",<br>
&nbsp;&nbsp;"recommended_action": "Khách hàng rất trung thành. Gửi mã ưu đãi Tri ân VIP 15% & đề xuất bộ sưu tập sản phẩm mới.",<br>
&nbsp;&nbsp;"model_used": "Gradient Boosting"<br>
}
    </div>

    <h3 style="color: #0f172a; font-size: 14px;">2.3.1. Ma trận phân tầng mức độ rủi ro rời bỏ (Risk Stratification Matrix)</h3>
    <p>Hệ thống chia xác suất quay lại $P = P(y=1 \mid \mathbf{x})$ thành 4 phân vùng rủi ro:</p>
    <table>
        <thead>
            <tr>
                <th>Cấp độ rủi ro (Risk Tier)</th>
                <th>Khoảng xác suất quay lại</th>
                <th>Khoảng nguy cơ rời bỏ (Churn)</th>
                <th>Đặc điểm hành vi tiêu biểu</th>
                <th>Hành động nghiệp vụ đề xuất</th>
            </tr>
        </thead>
        <tbody>
            <tr style="background-color: #ecfdf5;">
                <td><strong>1. Rất Thấp (Very Low)</strong></td>
                <td>$P > 80\%$</td>
                <td>$P_{\text{churn}} < 20\%$</td>
                <td>Khách VIP, tần suất mua đều đặn, AOV cao, điểm hài lòng 4 - 5 sao.</td>
                <td>Không giảm giá đại trà. Gửi thiệp tri ân, tặng quyền lợi phòng chờ VIP, ưu tiên xem trước bộ sưu tập mới.</td>
            </tr>
            <tr style="background-color: #f0fdf4;">
                <td><strong>2. Trung Bình (Moderate)</strong></td>
                <td>$50\% \le P \le 80\%$</td>
                <td>$20\% \le P_{\text{churn}} \le 50\%$</td>
                <td>Vẫn có ý định quay lại nhưng khoảng cách ngày mua đang dài ra; có thể chờ khuyến mãi.</td>
                <td>Gửi thông báo đẩy (App Push) nhắc nhở sản phẩm đã xem kèm mã giảm giá 10% có thời hạn 48 giờ.</td>
            </tr>
            <tr style="background-color: #fffbeb;">
                <td><strong>3. Cao (High Risk)</strong></td>
                <td>$20\% \le P < 50\%$</td>
                <td>$50\% < P_{\text{churn}} \le 80\%$</td>
                <td>Bắt đầu nguội lạnh tương tác (> 60 ngày chưa mua), điểm hài lòng ở mức trung bình (3 sao).</td>
                <td>Cảnh báo nguy cơ! Kích hoạt chiến dịch "We Miss You" qua Zalo/Email kèm Voucher 20% và chính sách miễn phí vận chuyển.</td>
            </tr>
            <tr style="background-color: #fef2f2;">
                <td><strong>4. Rất Cao (Critical Churn)</strong></td>
                <td>$P < 20\%$</td>
                <td>$P_{\text{churn}} > 80\%$</td>
                <td>Báo động đỏ! Đã quá lâu không mua (> 90 - 120 ngày), đánh giá 1 - 2 sao hoặc mua ít đơn.</td>
                <td>Chuyển danh sách cho bộ phận Chăm sóc khách hàng đặc biệt: gọi điện thăm hỏi trải nghiệm lỗi, tặng quà bù đắp và voucher 25%.</td>
            </tr>
        </tbody>
    </table>
</div>
