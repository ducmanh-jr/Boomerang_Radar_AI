<!-- PHẦN 1: BÌA ĐIỀU HÀNH, TÓM TẮT DÀNH CHO LÃNH ĐẠO & CHƯƠNG 1 -->

<div class="cover-page">
    <div class="institution">BỘ GIÁO DỤC VÀ ĐÀO TẠO &bull; HỆ THỐNG ĐÀO TẠO CÔNG NGHỆ THÔNG TIN</div>
    <div class="faculty">KHOA CÔNG NGHỆ THÔNG TIN & KHOA HỌC DỮ LIỆU ỨNG DỤNG</div>
    
    <div style="margin: 30px 0 15px 0;">
        <div class="cover-badge">BÁO CÁO NGHIÊN CỨU & PHÁT TRIỂN HỆ THỐNG AI DOANH NGHIỆP</div>
        <h1 class="main-title">BOOMERANG RADAR AI</h1>
        <div class="sub-title-cover">
            HỆ THỐNG TRÍ TUỆ NHÂN TẠO DỰ ĐOÁN KHẢ NĂNG KHÁCH HÀNG QUAY LẠI<br>
            VÀ ĐỊNH VỊ SỚM NGUY CƠ RỜI BỎ DỰA TRÊN MÔ HÌNH HÀNH VI RFM+
        </div>
    </div>

    <!-- HỘP ĐỐI TƯỢNG VÀ CÂU HỎI TRUNG TÂM -->
    <div style="width: 100%; background: #f8fafc; border: 1.5px solid #0284c7; border-radius: 6px; padding: 12px 18px; text-align: left; margin: 15px 0; font-family: 'Segoe UI', sans-serif;">
        <div style="font-size: 11pt; font-weight: bold; color: #0f172a; margin-bottom: 4px; text-transform: uppercase;">
            &bull; ĐỐI TƯỢNG BÁO CÁO & CÂU HỎI TRUNG TÂM (EXECUTIVE SCOPE)
        </div>
        <div style="font-size: 10pt; color: #334155; line-height: 1.5;">
            <strong>Đối tượng phục vụ chính:</strong> Ban Giám Đốc (CEO, CMO, CTO), Trưởng bộ phận Tăng trưởng (Head of Growth) và Trưởng phòng Chăm sóc khách hàng (Head of Customer Service).<br>
            <strong>Câu hỏi chiến lược giải quyết:</strong> <em>"Làm thế nào để doanh nghiệp bán lẻ/E-Commerce phát hiện chính xác khách hàng sắp rời bỏ trước 30–60 ngày, tối ưu hóa ngân sách tiếp thị giữ chân (Retention Marketing) và tối đa hóa Giá trị Trọn đời của Khách hàng (LTV) với độ chính xác đạt trên 94%?"</em>
        </div>
    </div>

    <div class="cover-metrics-box">
        <div class="metric-item">
            <span class="m-val">94.23%</span>
            <span class="m-lbl">Độ chính xác (Accuracy)</span>
        </div>
        <div class="metric-item">
            <span class="m-val">96.56%</span>
            <span class="m-lbl">F1-Score</span>
        </div>
        <div class="metric-item">
            <span class="m-val">96.95%</span>
            <span class="m-lbl">Chỉ số ROC-AUC</span>
        </div>
        <div class="metric-item">
            <span class="m-val">&lt; 50ms</span>
            <span class="m-lbl">Độ trễ suy luận API</span>
        </div>
    </div>

    <div class="cover-meta-info">
        <table class="meta-table">
            <tr>
                <td style="width: 32%;"><strong>Đề tài nghiên cứu:</strong></td>
                <td>Dự đoán Khả năng Khách hàng Quay lại Mua sắm (Customer Repurchase & Churn Prediction)</td>
            </tr>
            <tr>
                <td><strong>Mô hình tối ưu nhất:</strong></td>
                <td>Gradient Boosting Classifier (550 cây Boosting, Tốc độ học 0.0562, Độ sâu 14)</td>
            </tr>
            <tr>
                <td><strong>Bộ dữ liệu thử nghiệm:</strong></td>
                <td>5.630 hồ sơ khách hàng thương mại điện tử thực tế chuẩn hóa theo hành vi bán lẻ</td>
            </tr>
            <tr>
                <td><strong>Nền tảng công nghệ:</strong></td>
                <td>Python 3.10, Scikit-learn, Flask Framework, REST API, Bootstrap 5 UI</td>
            </tr>
            <tr>
                <td><strong>Thời gian nghiệm thu:</strong></td>
                <td>Năm học 2025 – 2026</td>
            </tr>
        </table>
    </div>
</div>

<div class="page-break"></div>

<!-- TÓM TẮT ĐIỀU HÀNH DÀNH CHO LÃNH ĐẠO (EXECUTIVE SUMMARY) -->
<div class="academic-section">
    <h1 class="chapter-title">TÓM TẮT ĐIỀU HÀNH (EXECUTIVE SUMMARY)</h1>
    
    <div class="callout callout-success" style="font-size: 11pt; line-height: 1.6;">
        <strong>THÔNG ĐIỆP CỐT LÕI DÀNH CHO BAN LÃNH ĐẠO (C-LEVEL TAKEAWAYS):</strong>
        <ol style="margin: 6px 0 0 0; padding-left: 20px;">
            <li><strong>Thực trạng:</strong> Chi phí thu hút khách hàng mới (CAC) ngày càng đắt đỏ (gấp 5 – 7 lần chi phí giữ chân). Việc phát khuyến mãi đại trà vừa làm suy giảm biên lợi nhuận ròng, vừa tạo ra nhóm khách hàng "săn voucher" không có lòng trung thành.</li>
            <li><strong>Giải pháp đột phá:</strong> Hệ thống <em>Boomerang Radar AI</em> tích hợp 4 đặc trưng tương tác phi tuyến vào mô hình học máy <em>Gradient Boosting</em>, đạt độ chính xác <strong>94.23%</strong> và $F_1\text{-score}$ đạt <strong>96.56%</strong>, vượt xa các giải pháp truyền thống (Logistic Regression 68.47%).</li>
            <li><strong>Tác động tài chính kỳ vọng:</strong> Giúp doanh nghiệp giảm thiểu <strong>78.4%</strong> nguy cơ mất khách hàng tiềm năng, tiết kiệm <strong>25% – 35%</strong> ngân sách khuyến mãi nhờ cơ chế phân bổ voucher đúng đối tượng, mang lại tỷ suất hoàn vốn đầu tư (ROI) dự kiến đạt <strong>320%</strong> trong 12 tháng triển khai.</li>
        </ol>
    </div>

    <h2 class="sub-title">Bảng tra cứu từ viết tắt và thuật ngữ chuyên môn</h2>
    <table>
        <thead>
            <tr>
                <th style="width: 20%;">Thuật ngữ viết tắt</th>
                <th style="width: 35%;">Tên tiếng Anh đầy đủ</th>
                <th>Định nghĩa & Ý nghĩa nghiệp vụ</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>CAC</strong></td>
                <td>Customer Acquisition Cost</td>
                <td>Chi phí trung bình để thu hút được một khách hàng mới hoàn tất đơn đầu tiên.</td>
            </tr>
            <tr>
                <td><strong>CLV / LTV</strong></td>
                <td>Customer Lifetime Value</td>
                <td>Tổng giá trị doanh thu hoặc lợi nhuận ròng một khách hàng đóng góp trong suốt vòng đời.</td>
            </tr>
            <tr>
                <td><strong>Churn Rate</strong></td>
                <td>Tỷ lệ rời bỏ khách hàng</td>
                <td>Tỷ lệ phần trăm khách hàng ngừng mua sắm hoặc hủy dịch vụ trong một khoảng thời gian.</td>
            </tr>
            <tr>
                <td><strong>Retention Rate</strong></td>
                <td>Tỷ lệ giữ chân khách hàng</td>
                <td>Tỷ lệ phần trăm khách hàng tiếp tục phát sinh đơn hàng lặp lại (Repurchase).</td>
            </tr>
            <tr>
                <td><strong>RFM</strong></td>
                <td>Recency, Frequency, Monetary</td>
                <td>Mô hình phân khúc khách hàng dựa trên: Độ mới, Tần suất và Giá trị tiền tệ giao dịch.</td>
            </tr>
            <tr>
                <td><strong>GBDT</strong></td>
                <td>Gradient Boosted Decision Trees</td>
                <td>Thuật toán học máy kết hợp tuần tự các cây quyết định để sửa chữa sai số thặng dư.</td>
            </tr>
            <tr>
                <td><strong>XAI</strong></td>
                <td>Explainable Artificial Intelligence</td>
                <td>Trí tuệ nhân tạo có khả năng giải thích tường minh cơ sở đưa ra quyết định.</td>
            </tr>
            <tr>
                <td><strong>MLOps</strong></td>
                <td>Machine Learning Operations</td>
                <td>Quy trình chuẩn hóa triển khai, giám sát và vận hành mô hình học máy trong doanh nghiệp.</td>
            </tr>
        </tbody>
    </table>
</div>

<div class="page-break"></div>

<!-- MỤC LỤC PHÂN CẤP CHUẨN THỐNG NHẤT -->
<div class="academic-section">
    <h1 class="chapter-title">MỤC LỤC HỆ THỐNG</h1>
    <table class="toc-table">
        <tr class="toc-head"><th style="width: 82%;">Cấu trúc đề mục</th><th style="width: 18%; text-align: right;">Trang</th></tr>
        <tr><td><strong>TÓM TẮT ĐIỀU HÀNH & DANH MỤC THUẬT NGỮ</strong></td><td style="text-align: right;">ii</td></tr>
        <tr><td><strong class="toc-chap">1. PHÁT BIỂU BÀI TOÁN & CƠ SỞ KHOA HỌC</strong></td><td style="text-align: right;">1</td></tr>
        <tr><td class="toc-sub">1.1. Bối cảnh kinh tế bán lẻ và bài toán chi phí giữ chân khách hàng</td><td style="text-align: right;">1</td></tr>
        <tr><td class="toc-sub">1.2. Cơ sở lý thuyết Vòng đời Khách hàng và Giá trị Trọn đời (CLV)</td><td style="text-align: right;">2</td></tr>
        <tr><td class="toc-sub">1.3. Mô hình toán học của bài toán Phân loại Khách hàng Quay lại</td><td style="text-align: right;">3</td></tr>
        <tr><td class="toc-sub">1.4. Tuyên ngôn giá trị và Sứ mệnh của Boomerang Radar AI</td><td style="text-align: right;">4</td></tr>
        <tr><td><strong class="toc-chap">2. XÁC ĐỊNH YÊU CẦU HỆ THỐNG, INPUT VÀ OUTPUT</strong></td><td style="text-align: right;">5</td></tr>
        <tr><td class="toc-sub">2.1. Yêu cầu chức năng và tiêu chuẩn phi chức năng</td><td style="text-align: right;">5</td></tr>
        <tr><td class="toc-sub">2.2. Đặc tả 8 thuộc tính dữ liệu đầu vào (Input Specification)</td><td style="text-align: right;">6</td></tr>
        <tr><td class="toc-sub">2.3. Cấu trúc dữ liệu đầu ra và Ma trận phân tầng 4 cấp rủi ro</td><td style="text-align: right;">7</td></tr>
        <tr><td><strong class="toc-chap">3. THIẾT KẾ SƠ ĐỒ KHỐI VÀ KIẾN TRÚC HỆ THỐNG</strong></td><td style="text-align: right;">9</td></tr>
        <tr><td class="toc-sub">3.1. Kiến trúc phân tầng 6 lớp độc lập (6-Layer Architecture)</td><td style="text-align: right;">9</td></tr>
        <tr><td class="toc-sub">3.2. Thiết kế luồng dữ liệu kép: Huấn luyện Offline & Suy luận Online</td><td style="text-align: right;">11</td></tr>
        <tr><td class="toc-sub">3.3. Cơ chế quản lý tài nguyên mô hình và giao tiếp API Gateway</td><td style="text-align: right;">12</td></tr>
        <tr><td><strong class="toc-chap">4. MÔ TẢ THUẬT TOÁN & NỀN TẢNG TOÁN HỌC</strong></td><td style="text-align: right;">13</td></tr>
        <tr><td class="toc-sub">4.1. Cơ sở giải tích của 4 đặc trưng tương tác phi tuyến (Interaction Features)</td><td style="text-align: right;">13</td></tr>
        <tr><td class="toc-sub">4.2. Thuật toán Hồi quy Logistic (Logistic Regression)</td><td style="text-align: right;">15</td></tr>
        <tr><td class="toc-sub">4.3. Thuật toán Cây quyết định (Decision Tree Classifier)</td><td style="text-align: right;">16</td></tr>
        <tr><td class="toc-sub">4.4. Thuật toán Rừng ngẫu nhiên (Random Forest Classifier)</td><td style="text-align: right;">17</td></tr>
        <tr><td class="toc-sub">4.5. Thuật toán Gradient Boosting Classifier (Champion Model)</td><td style="text-align: right;">18</td></tr>
        <tr><td class="toc-sub">4.6. Chiến lược tối ưu hóa siêu tham số qua RandomizedSearchCV & 5-Fold CV</td><td style="text-align: right;">20</td></tr>
        <tr><td><strong class="toc-chap">5. MÔ TẢ DỮ LIỆU & QUY TRÌNH TIỀN XỬ LÝ CHỐNG RÒ RỈ</strong></td><td style="text-align: right;">21</td></tr>
        <tr><td class="toc-sub">5.1. Nguồn dữ liệu và Thống kê mô tả khám phá (EDA)</td><td style="text-align: right;">21</td></tr>
        <tr><td class="toc-sub">5.2. Vấn đề mất cân bằng mẫu và giải pháp Stratified Splitting</td><td style="text-align: right;">22</td></tr>
        <tr><td class="toc-sub">5.3. Pipeline chuẩn hóa dữ liệu 14 chiều tuân thủ Anti-Data Leakage</td><td style="text-align: right;">23</td></tr>
        <tr><td><strong class="toc-chap">6. CÀI ĐẶT HỆ THỐNG VÀ XÂY DỰNG ỨNG DỤNG</strong></td><td style="text-align: right;">24</td></tr>
        <tr><td class="toc-sub">6.1. Môi trường công nghệ và Cấu trúc mã nguồn Clean Code</td><td style="text-align: right;">24</td></tr>
        <tr><td class="toc-sub">6.2. Cài đặt chi tiết các Module lõi (data_processing, train, predict)</td><td style="text-align: right;">25</td></tr>
        <tr><td class="toc-sub">6.3. Xây dựng dịch vụ REST API và Web Dashboard Bootstrap 5</td><td style="text-align: right;">26</td></tr>
        <tr><td><strong class="toc-chap">7. ĐÁNH GIÁ KẾT QUẢ THỰC NGHIỆM</strong></td><td style="text-align: right;">27</td></tr>
        <tr><td class="toc-sub">7.1. Bảng đối chuẩn hiệu năng thực nghiệm giữa 4 mô hình</td><td style="text-align: right;">27</td></tr>
        <tr><td class="toc-sub">7.2. Phân tích Ma trận nhầm lẫn và Tác động kinh tế của sai số (FP vs FN)</td><td style="text-align: right;">28</td></tr>
        <tr><td class="toc-sub">7.3. Xếp hạng độ quan trọng đặc trưng (Chứng minh vai trò 37.08% của FE)</td><td style="text-align: right;">29</td></tr>
        <tr><td><strong class="toc-chap">8. KẾ HOẠCH TRIỂN KHAI ACTIONABLE, HƯỚNG PHÁT TRIỂN & KẾT LUẬN</strong></td><td style="text-align: right;">30</td></tr>
        <tr><td class="toc-sub">8.1. Kế hoạch triển khai hành động (Ma trận RACI, Lộ trình Gantt, Ngân sách ROI)</td><td style="text-align: right;">30</td></tr>
        <tr><td class="toc-sub">8.2. Ứng dụng Trí tuệ Nhân tạo có thể giải thích (Explainable AI với SHAP)</td><td style="text-align: right;">32</td></tr>
        <tr><td class="toc-sub">8.3. Mở rộng kiến trúc thuật toán chuyên sâu (LightGBM, CatBoost, TabNet)</td><td style="text-align: right;">33</td></tr>
        <tr><td class="toc-sub">8.4. Thiết lập hệ thống MLOps và Tự động hóa tiếp thị đa kênh</td><td style="text-align: right;">34</td></tr>
        <tr><td class="toc-sub">8.5. Kết luận tổng quan đề tài</td><td style="text-align: right;">35</td></tr>
        <tr><td><strong>TÀI LIỆU THAM KHẢO CHUẨN APA</strong></td><td style="text-align: right;">36</td></tr>
    </table>
</div>

<div class="page-break"></div>

<!-- CHƯƠNG 1: PHÁT BIỂU BÀI TOÁN & CƠ SỞ KHOA HỌC -->
<div class="academic-section">
    <h1 class="chapter-title">1. PHÁT BIỂU BÀI TOÁN & CƠ SỞ KHOA HỌC</h1>
    
    <h2 class="sub-title">1.1. Bối cảnh kinh tế bán lẻ và bài toán chi phí giữ chân khách hàng</h2>
    <p>
        Trong thị trường bán lẻ và thương mại điện tử hiện đại, sự bùng nổ của các kênh phân phối kỹ thuật số đã làm thay đổi hoàn toàn hành vi của người tiêu dùng. Người mua hàng ngày nay có vô số sự lựa chọn và chi phí chuyển đổi (Switching Cost) sang đối thủ cạnh tranh gần như bằng không. Trước đây, nhiều doanh nghiệp chỉ tập trung vào việc chi tiêu mạnh cho quảng cáo trực tuyến nhằm thu hút khách hàng mới một lần rồi bỏ mặc họ. Tuy nhiên, sự gia tăng liên tục của <strong>Chi phí thu hút khách hàng mới (Customer Acquisition Cost - CAC)</strong>—tăng từ 40% đến 60% trong 5 năm gần đây trên các mạng xã hội và công cụ tìm kiếm—đã biến chiến lược này thành một cái bẫy làm suy giảm biên lợi nhuận ròng.
    </p>
    <p>
        <strong>Nút thắt thực tế trong quản trị quan hệ khách hàng (CRM):</strong> Hầu hết doanh nghiệp hiện nay vận hành hệ thống CRM theo hướng phản ứng bị động. Khách hàng chỉ được định nghĩa là "đã rời bỏ" khi họ không phát sinh đơn hàng trong hơn 90 hoặc 180 ngày. Ở thời điểm đó, sự chú ý của khách hàng đã thuộc về thương hiệu khác và chi phí để thuyết phục họ quay lại là cực kỳ tốn kém hoặc bất khả thi.
    </p>

    <h2 class="sub-title">1.2. Cơ sở lý thuyết Vòng đời Khách hàng và Giá trị Trọn đời (CLV)</h2>
    <p>
        Mô hình quản trị giá trị khách hàng xác định rằng tổng giá trị của một doanh nghiệp phụ thuộc trực tiếp vào <strong>Giá trị trọn đời của tập khách hàng (Customer Lifetime Value - CLV)</strong>. Theo công thức tài chính chuẩn tắc:
    </p>
    <div class="formula-box">
        \text{CLV} = \sum_{t=0}^{T} \frac{(p_t - c_t) \times r_t}{(1 + d)^t}
    </div>
    <p>
        Trong đó:
    </p>
    <ul>
        <li>$p_t$: Doanh thu kỳ vọng từ khách hàng tại chu kỳ $t$.</li>
        <li>$c_t$: Chi phí chăm sóc, vận hành đơn hàng tại chu kỳ $t$.</li>
        <li>$r_t$: Xác suất khách hàng tiếp tục quay lại mua sắm tại chu kỳ $t$ (Retention Rate).</li>
        <li>$d$: Tỷ lệ chiết khấu chi phí vốn của doanh nghiệp.</li>
    </ul>
    <p>
        <strong>Insight kinh tế then chốt:</strong> Xác suất quay lại $r_t$ là biến số nhân tử trực tiếp tác động theo cấp số nhân lên CLV. Nếu $r_t$ giảm đột ngột (khách rời bỏ), toàn bộ dòng tiền tiềm năng trong tương lai của khách hàng đó lập tức trở về $0$. Ngược lại, theo nghiên cứu kinh điển của <em>Bain & Company</em> và <em>Harvard Business Review</em>, chỉ cần nâng tỷ lệ giữ chân khách hàng thêm <strong>5%</strong>, lợi nhuận doanh nghiệp có thể tăng vọt từ <strong>25% đến 95%</strong> nhờ việc giảm thiểu chi phí tiếp thị lặp lại và tận dụng xu hướng khách hàng cũ chi tiêu cho các đơn hàng lớn hơn.
    </p>

    <h2 class="sub-title">1.3. Mô hình toán học của bài toán Phân loại Khách hàng Quay lại</h2>
    <p>
        Bài toán được thiết lập dưới dạng <strong>Học máy có giám sát - Phân loại nhị phân (Supervised Binary Classification)</strong> trên tập dữ liệu có tính chất mất cân bằng tự nhiên:
    </p>
    <p>
        Cho tập dữ liệu huấn luyện $\mathcal{D} = \{(\mathbf{x}_i, y_i)\}_{i=1}^N$, trong đó $\mathbf{x}_i \in \mathbb{R}^d$ là vector đặc trưng đại diện cho lịch sử giao dịch RFM, đặc điểm nhân khẩu học và trải nghiệm dịch vụ của khách hàng thứ $i$. Biến mục tiêu $y_i \in \{0, 1\}$ được định nghĩa:
    </p>
    <div class="formula-box">
        y_i = 
        \begin{cases}
        1 & \text{Khách hàng sẽ quay lại mua hàng trong chu kỳ kế tiếp (Repurchase)} \\
        0 & \text{Khách hàng không quay lại mua sắm / có nguy cơ rời bỏ (Churn)}
        \end{cases}
    </div>
    <p>
        Mục tiêu của giải thuật học máy là học một hàm dự báo $f: \mathbb{R}^d \to [0, 1]$ ước lượng chính xác xác suất hậu nghiệm:
    </p>
    <div class="formula-box">
        \hat{p}_i = P(y_i = 1 \mid \mathbf{x}_i) = f(\mathbf{x}_i)
    </div>
    <p>
        Nhãn dự đoán nhị phân $\hat{y}_i$ được xác định dựa trên ngưỡng phân loại tối ưu $\theta \in (0, 1)$ (mặc định $\theta = 0.50$):
    </p>
    <div class="formula-box">
        \hat{y}_i = \mathbb{I}(\hat{p}_i \ge \theta)
    </div>

    <h2 class="sub-title">1.4. Tuyên ngôn giá trị và Sứ mệnh của Boomerang Radar AI</h2>
    <p>
        Hệ thống <strong>Boomerang Radar AI</strong> được phát triển nhằm giải quyết triệt để bài toán giữ chân khách hàng thông qua 3 trụ cột giá trị:
    </p>
    <ol>
        <li>
            <strong>Cơ chế cảnh báo sớm (Proactive Early-Warning Radar):</strong> Quét liên tục hồ sơ khách hàng để nhận diện sớm các dấu hiệu phai nhạt tương tác ngay khi khoảng cách ngày mua bắt đầu vượt khỏi nhịp độ thông thường.
        </li>
        <li>
            <strong>Phân bổ ngân sách tiếp thị thông minh (Smart Voucher Targeting):</strong> Chấm dứt tình trạng phát mã giảm giá đại trà làm tổn hại biên lợi nhuận. Chỉ tập trung nguồn lực kích cầu vào nhóm khách hàng đứng trước nguy cơ rời bỏ nhưng vẫn còn khả năng cứu vãn.
        </li>
        <li>
            <strong>Tạo lập "Hiệu ứng Boomerang":</strong> Tự động kích hoạt các kịch bản can thiệp kịp thời (ưu đãi cá nhân hóa, tri ân VIP, gọi điện chăm sóc), đưa khách hàng quay trở lại vòng lặp mua sắm trung thành.
        </li>
    </ol>
</div>


<div class='page-break'></div>

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


<div class='page-break'></div>

<!-- CHƯƠNG 3: THIẾT KẾ SƠ ĐỒ KHỐI VÀ KIẾN TRÚC HỆ THỐNG -->

<div class="academic-section">
    <h1 class="chapter-title">3. THIẾT KẾ SƠ ĐỒ KHỐI VÀ KIẾN TRÚC HỆ THỐNG</h1>
    
    <h2 class="sub-title">3.1. Kiến trúc phân tầng tổng thể (6-Layer Architecture)</h2>
    <p>
        Để đảm bảo tính độc lập, khả năng kiểm thử từng phần (Unit Testing) và khả năng sẵn sàng triển khai trong môi trường doanh nghiệp thực tế, hệ thống <strong>Boomerang Radar AI</strong> được thiết kế theo <strong>Kiến trúc phân tầng 6 lớp (6-Layer Decoupled Architecture)</strong>. Mỗi tầng chịu trách nhiệm xử lý một nghiệp vụ chuyên biệt và chỉ giao tiếp với các tầng liền kề thông qua các giao diện định nghĩa rõ ràng (Clean Interfaces).
    </p>

    <!-- HTML SƠ ĐỒ KHỐI CHI TIẾT -->
    <div class="arch-container avoid-break" style="margin: 20px 0;">
        <!-- Layer 1 -->
        <div class="arch-layer">
            <div class="arch-layer-header">
                <span class="arch-layer-badge">TẦNG 1</span>
                <span>TẦNG THU THẬP & NHẬP LIỆU DỮ LIỆU (DATA INGESTION LAYER)</span>
            </div>
            <div class="arch-items">
                <div class="arch-card">
                    <div class="arch-card-title">Tệp CSV/Excel Gốc</div>
                    <div>Nạp dữ liệu lịch sử giao dịch bán lẻ (data/raw/ hoặc customer_repurchase_data.csv)</div>
                </div>
                <div class="arch-card">
                    <div class="arch-card-title">Web Form Input</div>
                    <div>Giao diện nhập liệu trực quan 8 chỉ số của một khách hàng trên Dashboard</div>
                </div>
                <div class="arch-card">
                    <div class="arch-card-title">Batch CSV Ingestion</div>
                    <div>Nhận tệp tin CSV tải lên chứa danh sách khách hàng cần quét đồng thời</div>
                </div>
                <div class="arch-card">
                    <div class="arch-card-title">REST API Payload</div>
                    <div>Tiếp nhận các truy vấn JSON gửi đến từ các dịch vụ Backend/CRM bên ngoài</div>
                </div>
            </div>
        </div>

        <!-- Layer 2 -->
        <div class="arch-layer">
            <div class="arch-layer-header">
                <span class="arch-layer-badge">TẦNG 2</span>
                <span>TẦNG TIỀN XỬ LÝ & KỸ THUẬT ĐẶC TRƯNG (PREPROCESSING & FEATURE PIPELINE)</span>
            </div>
            <div class="arch-items">
                <div class="arch-card">
                    <div class="arch-card-title">Data Cleaning Engine</div>
                    <div>Điền khuyết thiếu bằng trung vị (Median Imputation), chuẩn hóa định dạng số và nhãn</div>
                </div>
                <div class="arch-card">
                    <div class="arch-card-title">Interaction Engineering</div>
                    <div>Tính 4 biến phi tuyến: purchase_intensity, ltv_score, satisfaction_recency, voucher_low_value</div>
                </div>
                <div class="arch-card">
                    <div class="arch-card-title">Stratified Splitting</div>
                    <div>Chia tách Train/Test 80/20 có phân tầng bảo toàn phân phối nhãn trước khi fit transformer</div>
                </div>
                <div class="arch-card">
                    <div class="arch-card-title">ColumnTransformer</div>
                    <div>StandardScaler (10 cột liên tục) + OneHotEncoder (2 cột danh mục drop='first') &rarr; 14 chiều</div>
                </div>
            </div>
        </div>

        <!-- Layer 3 -->
        <div class="arch-layer">
            <div class="arch-layer-header">
                <span class="arch-layer-badge">TẦNG 3</span>
                <span>TẦNG MÔ HÌNH HÓA & TỐI ƯU HỌC MÁY (MODELING & OPTIMIZATION LAYER)</span>
            </div>
            <div class="arch-items">
                <div class="arch-card">
                    <div class="arch-card-title">Logistic Regression</div>
                    <div>Baseline tuyến tính, tối ưu C qua GridSearchCV trên không gian tham số logarit</div>
                </div>
                <div class="arch-card">
                    <div class="arch-card-title">Decision Tree</div>
                    <div>Cây quyết định phi tuyến, tối ưu max_depth, min_samples_split qua RandomizedSearchCV</div>
                </div>
                <div class="arch-card">
                    <div class="arch-card-title">Random Forest</div>
                    <div>Ensemble 550 cây Bagging độc lập, tối ưu số lượng cây và tỷ lệ đặc trưng con</div>
                </div>
                <div class="arch-card">
                    <div class="arch-card-title">Gradient Boosting</div>
                    <div>Champion Model! 550 cây Boosting tuần tự, lr=0.0562, depth=14, subsample=0.95</div>
                </div>
            </div>
        </div>

        <!-- Layer 4 -->
        <div class="arch-layer">
            <div class="arch-layer-header">
                <span class="arch-layer-badge">TẦNG 4</span>
                <span>TẦNG LƯU TRỮ ARTIFACTS & TÀI NGUYÊN MÔ HÌNH (STORAGE & ARTIFACTS LAYER)</span>
            </div>
            <div class="arch-items">
                <div class="arch-card">
                    <div class="arch-card-title">preprocessor.joblib</div>
                    <div>Chứa đối tượng ColumnTransformer đã học các tham số &mu;, &sigma; từ tập Train</div>
                </div>
                <div class="arch-card">
                    <div class="arch-card-title">gradient_boosting.joblib</div>
                    <div>Tập tin nhị phân lưu trữ toàn bộ cấu trúc và trọng số của mô hình vô địch</div>
                </div>
                <div class="arch-card">
                    <div class="arch-card-title">feature_names.joblib</div>
                    <div>Danh mục tên 14 đặc trưng sau khi mã hóa one-hot phục vụ mapping Feature Importance</div>
                </div>
                <div class="arch-card">
                    <div class="arch-card-title">evaluation_results.json</div>
                    <div>Lưu trữ toàn bộ chỉ số thực nghiệm, ma trận nhầm lẫn và siêu tham số tối ưu</div>
                </div>
            </div>
        </div>

        <!-- Layer 5 -->
        <div class="arch-layer">
            <div class="arch-layer-header">
                <span class="arch-layer-badge">TẦNG 5</span>
                <span>TẦNG DỊCH VỤ & SUY LUẬN THỜI GIAN THỰC (APPLICATION & INFERENCE LAYER)</span>
            </div>
            <div class="arch-items">
                <div class="arch-card">
                    <div class="arch-card-title">REST API Gateway</div>
                    <div>Flask Router định tuyến các Endpoint: /api/predict, /api/predict-batch, /api/models, /api/stats</div>
                </div>
                <div class="arch-card">
                    <div class="arch-card-title">Inference Engine</div>
                    <div>Thực hiện nạp mô hình lười (Lazy-loading), biến đổi vector đặc trưng và tính toán predict_proba()</div>
                </div>
                <div class="arch-card">
                    <div class="arch-card-title">Synthesis Logic Engine</div>
                    <div>Engine quy tắc tự động phân tích sâu đa chiều và sinh câu diễn giải ngữ cảnh tự nhiên</div>
                </div>
                <div class="arch-card">
                    <div class="arch-card-title">Batch Processing Engine</div>
                    <div>Xử lý song song dữ liệu bảng từ file CSV, định dạng kết quả và xuất tệp tin</div>
                </div>
            </div>
        </div>

        <!-- Layer 6 -->
        <div class="arch-layer">
            <div class="arch-layer-header">
                <span class="arch-layer-badge">TẦNG 6</span>
                <span>TẦNG GIAO DIỆN NGƯỜI DÙNG & TƯƠNG TÁC (PRESENTATION & DASHBOARD LAYER)</span>
            </div>
            <div class="arch-items">
                <div class="arch-card">
                    <div class="arch-card-title">Tab 1: Overview</div>
                    <div>Thống kê trực quan chỉ số vĩ mô (tỷ lệ rời bỏ, AOV) và bảng xem trước dữ liệu mẫu</div>
                </div>
                <div class="arch-card">
                    <div class="arch-card-title">Tab 2: Predictor</div>
                    <div>Form nhập liệu trực quan, Radar quét nguy cơ, thẻ kết quả cảnh báo và đề xuất hành động</div>
                </div>
                <div class="arch-card">
                    <div class="arch-card-title">Tab 3: Benchmark</div>
                    <div>Bảng so sánh 4 mô hình, Ma trận nhầm lẫn và biểu đồ Feature Importance bằng Chart.js</div>
                </div>
                <div class="arch-card">
                    <div class="arch-card-title">Tab 4: Batch</div>
                    <div>Kéo thả tệp CSV hàng loạt, hiển thị kết quả phân loại phân trang và nút Export CSV</div>
                </div>
            </div>
        </div>
    </div>

    <h2 class="sub-title">3.2. Thiết kế luồng dữ liệu (Data Pipeline & Inference Flow)</h2>
    <p>
        Kiến trúc hệ thống được phân định rạch ròi thành hai chu trình luồng dữ liệu: <strong>Chu trình huấn luyện ngoại tuyến (Offline Training Pipeline)</strong> và <strong>Chu trình suy luận trực tuyến (Online Inference Pipeline)</strong>.
    </p>

    <h3 style="color: #0f172a; font-size: 14px;">3.2.1. Chu trình huấn luyện ngoại tuyến (Offline Pipeline)</h3>
    <ol>
        <li><strong>Thu nạp & Làm sạch (Ingestion & Cleaning):</strong> Tập dữ liệu lịch sử được nạp từ <code>data/customer_repurchase_data.csv</code>. Thuật toán Median Imputation được áp dụng để điền các giá trị thiếu ở các trường số, các thuộc tính phân loại được chuẩn hóa về định dạng nhị phân hoặc chuỗi tiếng Việt đồng nhất.</li>
        <li><strong>Đặc trưng hóa tương tác (Interaction Feature Engineering):</strong> Dữ liệu được đưa qua hàm <code>engineer_features()</code> để tính toán 4 chỉ số mở rộng.</li>
        <li><strong>Phân chia tập có bảo toàn nhãn (Stratified Split):</strong> Toàn bộ bảng dữ liệu được chia theo tỷ lệ 80% cho tập huấn luyện và 20% cho tập kiểm thử bằng hàm <code>train_test_split(stratify=y)</code>.</li>
        <li><strong>Đóng băng bộ biến đổi (Fit Preprocessor):</strong> Đối tượng <code>ColumnTransformer</code> thực hiện học các tham số chuẩn hóa trên $X_{\text{train}}$ và biến đổi sang vector 14 chiều. Sau đó, toàn bộ đối tượng biến đổi được lưu thành <code>models/preprocessor.joblib</code>.</li>
        <li><strong>Tối ưu hóa và Kiểm định chéo (Tuning & Cross-Validation):</strong> Thực hiện chạy <code>RandomizedSearchCV</code> trên không gian tham số của từng thuật toán với 5-Fold Stratified CV.</li>
        <li><strong>Đánh giá độc lập và Xuất Artifacts:</strong> Mô hình tối ưu được kiểm tra trên $X_{\text{test}}$. Toàn bộ trọng số mô hình tốt nhất, danh mục đặc trưng và file JSON đánh giá được tuần tự hóa và ghi vào thư mục <code>models/</code>.</li>
    </ol>

    <h3 style="color: #0f172a; font-size: 14px;">3.2.2. Chu trình suy luận trực tuyến (Online Inference Pipeline)</h3>
    <ol>
        <li><strong>Tiếp nhận yêu cầu (Request Ingestion):</strong> Khách hàng nhập thông tin trên form web hoặc gửi một payload JSON đến <code>POST /api/predict</code>.</li>
        <li><strong>Ánh xạ đặc trưng (Dynamic Feature Engineering):</strong> Dữ liệu đơn lẻ dạng Dictionary được chuyển thành DataFrame 1 dòng và đưa qua cùng hàm <code>engineer_features()</code> để sinh 4 biến tương tác phi tuyến giống hệt như lúc huấn luyện.</li>
        <li><strong>Biến đổi không rò rỉ (Deterministic Transform):</strong> Đối tượng <code>preprocessor.joblib</code> được gọi qua phương thức <code>.transform()</code> (tuyệt đối không fit lại), chuyển đổi 1 dòng dữ liệu thô thành vector số học chuẩn 14 chiều.</li>
        <li><strong>Ước lượng xác suất (Probability Estimation):</strong> Mô hình Champion <code>gradient_boosting_model.joblib</code> thực hiện hàm <code>predict_proba()</code> để trích xuất xác suất quay lại $P(y=1 \mid \mathbf{x})$.</li>
        <li><strong>Phân tích quy tắc & Sinh khuyến nghị:</strong> Xác suất cùng 8 thuộc tính ban đầu được đưa qua bộ phân tích quy tắc <code>generate_synthesis_analysis()</code> để tạo ra câu diễn giải hành vi, mức độ rủi ro và khuyến nghị hành động tương ứng.</li>
        <li><strong>Đóng gói phản hồi:</strong> Toàn bộ kết quả được đóng gói thành JSON và phản hồi về client với độ trễ dưới 50ms.</li>
    </ol>

    <h2 class="sub-title">3.3. Cơ chế phân tách module và quản lý trạng thái mô hình</h2>
    <p>
        Hệ thống áp dụng cơ chế <strong>Decoupled Architecture</strong>: Mã nguồn huấn luyện (<code>src/train.py</code>) và mã nguồn phục vụ suy luận (<code>src/predict.py</code>, <code>app.py</code>) hoàn toàn độc lập với nhau. Trong môi trường Production, máy chủ web không bao giờ phải chạy lại quá trình huấn luyện tốn kém tài nguyên mà chỉ nạp (load) các file nhị phân tĩnh đã được kiểm định chất lượng nghiêm ngặt. Điều này cho phép mở rộng quy mô hệ thống (Scale-out) theo chiều ngang một cách dễ dàng thông qua việc khởi chạy nhiều instance Flask đằng sau một bộ cân bằng tải (Load Balancer).
    </p>
</div>


<div class='page-break'></div>

<!-- CHƯƠNG 4: MÔ TẢ THUẬT TOÁN & NỀN TẢNG TOÁN HỌC -->

<div class="academic-section">
    <h1 class="chapter-title">4. MÔ TẢ THUẬT TOÁN & NỀN TẢNG TOÁN HỌC</h1>
    
    <p>
        Chương này đi sâu vào cơ sở lý thuyết toán học, các phương trình vi tích phân, đại số tuyến tính và cơ chế tối ưu hóa đằng sau toàn bộ quy trình xây dựng đặc trưng và 4 mô hình học máy được triển khai trong hệ thống <strong>Boomerang Radar AI</strong>.
    </p>

    <h2 class="sub-title">4.1. Cơ sở toán học của 4 đặc trưng tương tác phi tuyến (Interaction Features)</h2>
    <p>
        Trong các bài toán dữ liệu bảng (Tabular Data), nếu chỉ đưa các biến thô độc lập vào mô hình, các giải thuật phân loại tuyến tính hoặc cây quyết định có độ sâu nông sẽ rất khó nắm bắt được những mối quan hệ nhân quả tương hỗ phi tuyến giữa các chiều không gian. Dựa trên lý thuyết kinh tế học hành vi và mô hình RFM, chúng tôi thiết kế 4 biến tương tác giải tích:
    </p>

    <h3 style="color: #0f172a; font-size: 14px;">1. Cường độ mua sắm (Purchase Intensity)</h3>
    <p>
        Biến số này đo lường nhịp độ phát sinh giao dịch trên một đơn vị thời gian gần nhất của khách hàng. Công thức giải tích được xác định như sau:
    </p>
    <div class="formula-box">
        \text{purchase\_intensity} = \frac{\text{total\_purchases}}{\text{days\_since\_last\_purchase} + 1}
    </div>
    <p>
        <strong>Phân tích toán học:</strong><br>
        Hệ số cộng mẫu số $+1$ đóng vai trò là tham số làm mịn (smoothing parameter), ngăn chặn triệt để lỗi chia cho $0$ trong trường hợp khách hàng vừa phát sinh giao dịch trong ngày ($\text{days} = 0$).<br>
        Xét đạo hàm riêng theo số ngày chưa mua lại:
    </p>
    <div class="formula-box">
        \frac{\partial (\text{purchase\_intensity})}{\partial (\text{days})} = -\frac{\text{total\_purchases}}{(\text{days} + 1)^2} < 0 \quad (\forall \text{total} \ge 1, \text{days} \ge 0)
    </div>
    <p>
        Đạo hàm luôn mang dấu âm, phản ánh tính chất giảm đơn điệu phi tuyến theo luật nghịch đảo bình phương: Càng nhiều ngày không mua, cường độ tương tác suy giảm rất nhanh ở giai đoạn đầu và tiệm cận về $0$ ở giai đoạn sau.
    </p>

    <h3 style="color: #0f172a; font-size: 14px;">2. Điểm giá trị vòng đời giản lược (LTV Score)</h3>
    <p>
        Kết hợp trực tiếp giữa tần suất giao dịch lũy kế và giá trị trung bình trên mỗi đơn hàng nhằm ước lượng quy mô tổng đóng góp tài chính của khách hàng cho hệ thống bán lẻ:
    </p>
    <div class="formula-box">
        \text{ltv\_score} = \frac{\text{total\_purchases} \times \text{avg\_order\_value}}{1.000.000} \quad (\text{đơn vị: triệu VNĐ})
    </div>
    <p>
        Việc chia cho hệ số quy đổi tỷ lệ $10^6$ giúp chuẩn hóa thang đo về miền giá trị trực quan từ $0.15$ đến hơn $200$ triệu đồng, hỗ trợ các thuật toán gradient hội tụ ổn định hơn.
    </p>

    <h3 style="color: #0f172a; font-size: 14px;">3. Mức độ hài lòng theo hàm suy giảm thời gian (Satisfaction Recency)</h3>
    <p>
        Một khách hàng từng đánh giá 5 sao nhưng đã 150 ngày không quay lại có tâm lý hoàn toàn khác với một khách hàng đánh giá 5 sao vừa mua hàng cách đây 7 ngày. Để mô hình hóa hiện tượng "phai nhạt ký ức trải nghiệm" (Memory Decay Effect), chúng tôi xây dựng công thức:
    </p>
    <div class="formula-box">
        \text{satisfaction\_recency} = \left( \frac{\text{satisfaction\_score}}{\text{days\_since\_last\_purchase} + 1} \right) \times 30
    </div>
    <p>
        Trong đó, thừa số $30$ biểu diễn chu kỳ chuẩn hóa 1 tháng. Nếu khách hàng đánh giá 5 sao và mua hàng cách đây 29 ngày ($\text{days} + 1 = 30$), điểm số được chuẩn hóa chính xác bằng $5.0$. Nếu số ngày tăng lên 90 ngày, giá trị này sẽ suy giảm chỉ còn $1.67$, phản ánh đúng thực tế trải nghiệm tốt trước đây đã mất dần tác dụng giữ chân.
    </p>

    <h3 style="color: #0f172a; font-size: 14px;">4. Nhận diện nhóm chuyên săn giảm giá giá trị thấp (Voucher Low Value)</h3>
    <p>
        Trong bán lẻ, nhóm khách hàng "Voucher Hunters" chỉ mua sắm khi có mã giảm giá và thường chọn những mặt hàng có giá trị thấp nhất để tối đa hóa mức chiết khấu. Nhóm này có mức độ trung thành thương hiệu cực kỳ kém. Đặc trưng nhị phân này được xây dựng thông qua hàm chỉ thị (Indicator Function):
    </p>
    <div class="formula-box">
        \text{voucher\_low\_value} = \text{used\_voucher} \times \mathbb{I}(\text{avg\_order\_value} \le 300.000\text{ VNĐ})
    </div>
    <p>
        Biến nhận giá trị $1$ nếu khách hàng vừa thỏa mãn điều kiện có áp dụng voucher vừa có giá trị đơn hàng trung bình dưới 300.000 VNĐ; ngược lại nhận giá trị $0$.
    </p>

    <h2 class="sub-title">4.2. Thuật toán Hồi quy Logistic (Logistic Regression)</h2>
    <p>
        Hồi quy Logistic là thuật toán phân loại tuyến tính nền tảng. Thay vì khớp một đường hồi quy trực tiếp, mô hình liên kết tổ hợp tuyến tính của các biến đầu vào với xác suất phân loại thông qua hàm kích hoạt <strong>Sigmoid (Logistic Function)</strong>:
    </p>
    <div class="formula-box">
        z = \mathbf{w}^T \mathbf{x} + b = w_1 x_1 + w_2 x_2 + \dots + w_d x_d + b<br>
        \sigma(z) = \frac{1}{1 + e^{-z}} \in (0, 1)
    </div>
    <p>
        Xác suất hậu nghiệm có điều kiện được tính như sau:
    </p>
    <div class="formula-box">
        P(y = 1 \mid \mathbf{x}) = \sigma(z) = \frac{1}{1 + e^{-(\mathbf{w}^T \mathbf{x} + b)}}<br>
        P(y = 0 \mid \mathbf{x}) = 1 - P(y = 1 \mid \mathbf{x}) = \frac{e^{-(\mathbf{w}^T \mathbf{x} + b)}}{1 + e^{-(\mathbf{w}^T \mathbf{x} + b)}}
    </div>

    <h3 style="color: #0f172a; font-size: 14px;">Hàm mất mát và Tối ưu hóa điều chuẩn $L_2$ (Ridge)</h3>
    <p>
        Hàm mục tiêu được xây dựng dựa trên nguyên lý Hợp lý cực đại (Maximum Likelihood Estimation - MLE), tương đương với việc tối thiểu hóa hàm mất mát <strong>Binary Cross-Entropy</strong> có bổ sung số hạng phạt điều chuẩn $L_2$:
    </p>
    <div class="formula-box">
        J(\mathbf{w}, b) = -\frac{1}{N} \sum_{i=1}^N \left[ y_i \ln(\hat{y}_i) + (1 - y_i) \ln(1 - \hat{y}_i) \right] + \frac{1}{2C} \|\mathbf{w}\|_2^2
    </div>
    <p>
        Trong đó:
    </p>
    <ul>
        <li>$\hat{y}_i = \sigma(\mathbf{w}^T \mathbf{x}_i + b)$ là xác suất dự đoán của mẫu thứ $i$.</li>
        <li>$C > 0$ là siêu tham số nghịch đảo của cường độ điều chuẩn (Inverse Regularization Strength). $C$ càng nhỏ thì mức phạt trọng số càng lớn, giúp chống quá khớp (Overfitting).</li>
        <li>Hệ thống thực hiện tối ưu hóa qua thuật toán <strong>L-BFGS (Limited-memory Broyden–Fletcher–Goldfarb–Shanno)</strong> kết hợp <code>GridSearchCV</code> trên miền $C \in \{0.001, 0.01, 0.1, 0.5, 1.0, 5.0, 10.0, 50.0\}$.</li>
    </ul>

    <h2 class="sub-title">4.3. Thuật toán Cây quyết định (Decision Tree Classifier)</h2>
    <p>
        Cây quyết định phân chia không gian đặc trưng một cách đệ quy thành các siêu hình hộp chữ nhật đồng nhất thông qua cấu trúc cây phân cấp gồm: Gốc (Root), Các nút điều kiện phân nhánh (Decision Nodes) và Các nút lá (Leaf Nodes) gán nhãn dự đoán.
    </p>
    <p>
        Tại mỗi bước phân chia tại nút $S$, thuật toán tìm kiếm đặc trưng $A$ và ngưỡng phân chia $\theta$ sao cho độ tinh khiết sau phân tách đạt mức tối đa. Hai tiêu chí đo lường độ hỗn loạn thông tin được thử nghiệm:
    </p>

    <h3 style="color: #0f172a; font-size: 14px;">1. Entropy và Độ lợi thông tin (Information Gain)</h3>
    <div class="formula-box">
        H(S) = -\sum_{c \in \{0, 1\}} p_c \log_2(p_c)<br>
        \text{Gain}(S, A) = H(S) - \sum_{v \in \{\text{left}, \text{right}\}} \frac{|S_v|}{|S|} H(S_v)
    </div>

    <h3 style="color: #0f172a; font-size: 14px;">2. Chỉ số vẩn đục Gini (Gini Impurity)</h3>
    <div class="formula-box">
        I_G(S) = 1 - \sum_{c \in \{0, 1\}} p_c^2 = 1 - (p_0^2 + p_1^2) = 2 p_0 p_1
    </div>
    <p>
        Trong đó $p_c$ là tỷ lệ mẫu thuộc lớp $c$ tại nút $S$. Thuật toán chọn điểm cắt cực đại hóa $\Delta I_G = I_G(S) - \frac{|S_L|}{|S|} I_G(S_L) - \frac{|S_R|}{|S|} I_G(S_R)$.
    </p>
    <p>
        <strong>Chiến lược kiểm soát quá khớp:</strong> Để tránh việc cây phát triển quá sâu ghi nhớ nhiễu (Overfitting), hệ thống sử dụng <code>RandomizedSearchCV</code> để khống chế: <code>max_depth &le; 16</code>, <code>min_samples_split &ge; 5</code>, <code>min_samples_leaf &ge; 2</code>.
    </p>

    <h2 class="sub-title">4.4. Thuật toán Rừng ngẫu nhiên (Random Forest Classifier)</h2>
    <p>
        Rừng ngẫu nhiên là thuật toán học kết hợp nhóm (Ensemble Learning) theo phương pháp <strong>Bagging (Bootstrap Aggregating)</strong> do <em>Leo Breiman</em> đề xuất. Thuật toán xây dựng một quần thể gồm $B$ cây quyết định độc lập $\{T_1, T_2, \dots, T_B\}$.
    </p>

    <h3 style="color: #0f172a; font-size: 14px;">Cơ sở toán học của việc giảm phương sai (Variance Reduction)</h3>
    <p>
        Giả sử mỗi cây quyết định đơn lẻ có phương sai là $\sigma^2$ và hệ số tương quan giữa hai cây bất kỳ là $\rho$. Khi lấy trung bình dự đoán của $B$ cây độc lập, phương sai của tổ hợp Rừng ngẫu nhiên được tính bằng:
    </p>
    <div class="formula-box">
        \text{Var}\left( \frac{1}{B} \sum_{b=1}^B T_b(\mathbf{x}) \right) = \rho \sigma^2 + \frac{1 - \rho}{B} \sigma^2
    </div>
    <p>
        Khi số lượng cây $B \to \infty$, số hạng thứ hai $\frac{1-\rho}{B}\sigma^2 \to 0$, phương sai tổng thể chỉ còn bị giới hạn bởi $\rho \sigma^2$. Để làm giảm phương sai xuống mức thấp nhất, Random Forest áp dụng hai cơ chế tạo tính ngẫu nhiên:
    </p>
    <ol>
        <li><strong>Lấy mẫu Bootstrap (Bootstrap Sampling):</strong> Mỗi cây $T_b$ được huấn luyện trên một tập dữ liệu con kích thước $N$ được rút ngẫu nhiên có hoàn lại từ tập dữ liệu gốc. Xác suất một mẫu không được chọn vào cây (Out-of-Bag - OOB) xấp xỉ bằng:
        $$\lim_{N \to \infty} \left(1 - \frac{1}{N}\right)^N = e^{-1} \approx 36.8\%$$
        Tập OOB này đóng vai trò như tập kiểm thử chéo nội tại để ước lượng sai số không chệch.</li>
        <li><strong>Không gian con ngẫu nhiên (Random Subspace Method):</strong> Tại mỗi nút phân chia, thuật toán không xem xét toàn bộ $d$ đặc trưng mà chỉ chọn ngẫu nhiên một tập con $m = \sqrt{d}$ hoặc $m = \log_2(d)$ đặc trưng. Điều này làm giảm mạnh độ tương quan $\rho$ giữa các cây, từ đó triệt tiêu phương sai của mô hình.</li>
    </ol>
    <p>
        Dự đoán xác suất cuối cùng là trung bình xác suất của toàn bộ các cây:
    </p>
    <div class="formula-box">
        \hat{P}(y = 1 \mid \mathbf{x}) = \frac{1}{B} \sum_{b=1}^B P_b(y = 1 \mid \mathbf{x})
    </div>

    <h2 class="sub-title">4.5. Thuật toán Gradient Boosting Classifier (Mô hình Champion)</h2>
    <p>
        Khác biệt căn bản với Random Forest (các cây hoạt động song song độc lập), <strong>Gradient Boosting (GBDT)</strong> do <em>Jerome Friedman (2001)</em> phát minh hoạt động theo nguyên lý Boosting tuần tự (Sequential Ensemble): Mỗi cây quyết định kế tiếp được xây dựng để sửa chữa những sai lầm còn sót lại của tổ hợp các cây phía trước.
    </p>

    <h3 style="color: #0f172a; font-size: 14px;">Toán học tối ưu hóa trên không gian hàm (Functional Gradient Descent)</h3>
    <p>
        Xét bài toán cực tiểu hóa hàm mất mát tổng thể $\mathcal{L}(y, F(\mathbf{x}))$:
    </p>
    <div class="formula-box">
        F^*(\mathbf{x}) = \arg\min_{F} \mathbb{E}_{(\mathbf{x}, y)} \left[ \mathcal{L}(y, F(\mathbf{x})) \right]
    </div>
    <p>
        Trong bài toán phân loại nhị phân, hàm mất mát là <strong>Log-Loss (Binary Deviance)</strong>. Giả sử $F(\mathbf{x}) = \ln \left( \frac{p}{1-p} \right)$ là hàm log-odds (logit):
    </p>
    <div class="formula-box">
        \mathcal{L}(y, F(\mathbf{x})) = \ln\left(1 + e^{F(\mathbf{x})}\right) - y \cdot F(\mathbf{x})
    </div>
    <p>
        <strong>Quy trình lặp của thuật toán Gradient Boosting:</strong>
    </p>
    <ol>
        <li>
            <strong>Khởi tạo mô hình cơ sở $F_0(\mathbf{x})$:</strong> Là một giá trị hằng số tối ưu hóa hàm mất mát trên toàn bộ dữ liệu:
            $$F_0(\mathbf{x}) = \arg\min_{\gamma} \sum_{i=1}^N \mathcal{L}(y_i, \gamma) = \ln\left( \frac{\sum y_i}{N - \sum y_i} \right) = \ln\left( \frac{\bar{y}}{1 - \bar{y}} \right)$$
        </li>
        <li>
            <strong>Với mỗi vòng lặp $m = 1, 2, \dots, M$ (với $M = 550$ cây):</strong>
            <ul>
                <li>
                    <strong>Bước a:</strong> Tính toán phần dư giả (Pseudo-Residuals) hay đạo hàm riêng âm của hàm mất mát đối với mô hình hiện tại:
                    $$r_{im} = -\left[ \frac{\partial \mathcal{L}(y_i, F(\mathbf{x}_i))}{\partial F(\mathbf{x}_i)} \right]_{F(\mathbf{x}) = F_{m-1}(\mathbf{x})} = y_i - \sigma(F_{m-1}(\mathbf{x}_i)) = y_i - p_{i, m-1}$$
                    <em>Nhận xét sâu sắc:</em> Phần dư tại mỗi bước chính là hiệu số giữa nhãn thực tế $y_i \in \{0, 1\}$ và xác suất dự đoán hiện tại $p_{i, m-1}$. Mẫu nào bị dự đoán sai nhiều sẽ có $|r_{im}|$ lớn, buộc cây kế tiếp phải tập trung sửa sai cho mẫu đó!
                </li>
                <li>
                    <strong>Bước b:</strong> Huấn luyện một cây hồi quy (Regression Tree) $h_m(\mathbf{x})$ để khớp với các phần dư $r_{im}$, tạo ra các vùng lá $R_{jm}$ với $j = 1, \dots, J_m$.
                </li>
                <li>
                    <strong>Bước c:</strong> Với mỗi vùng lá $R_{jm}$, tính giá trị đầu ra tối ưu $\gamma_{jm}$:
                    $$\gamma_{jm} = \arg\min_{\gamma} \sum_{\mathbf{x}_i \in R_{jm}} \mathcal{L}(y_i, F_{m-1}(\mathbf{x}_i) + \gamma) = \frac{\sum_{\mathbf{x}_i \in R_{jm}} r_{im}}{\sum_{\mathbf{x}_i \in R_{jm}} p_{i, m-1} (1 - p_{i, m-1})}$$
                </li>
                <li>
                    <strong>Bước d:</strong> Cập nhật hàm dự đoán tổng thể có kết hợp tham số co rút (Shrinkage / Learning Rate) $\nu \in (0, 1]$:
                    $$F_m(\mathbf{x}) = F_{m-1}(\mathbf{x}) + \nu \sum_{j=1}^{J_m} \gamma_{jm} \mathbb{I}(\mathbf{x} \in R_{jm})$$
                </li>
            </ul>
        </li>
        <li>
            <strong>Dự đoán xác suất cuối cùng sau $M$ cây:</strong>
            $$\hat{P}(y = 1 \mid \mathbf{x}) = \sigma(F_M(\mathbf{x})) = \frac{1}{1 + e^{-F_M(\mathbf{x})}}$$
        </li>
    </ol>

    <h3 style="color: #0f172a; font-size: 14px;">Bảng tham số tối ưu đạt được qua RandomizedSearchCV (N_iter = 80)</h3>
    <table>
        <thead>
            <tr>
                <th>Siêu tham số (Hyperparameter)</th>
                <th>Giá trị tối ưu</th>
                <th>Miền tìm kiếm</th>
                <th>Tác động kỹ thuật & Vai trò</th>
            </tr>
        </thead>
        <tbody>
            <tr class="highlight-row">
                <td><code>n_estimators</code></td>
                <td><strong>550</strong></td>
                <td>$[100, 200, 300, 500, 600]$</td>
                <td>Số lượng cây Boosting tuần tự. 550 cây đủ lớn để học sâu các chi tiết mà không làm tràn bộ nhớ.</td>
            </tr>
            <tr class="highlight-row">
                <td><code>learning_rate</code> ($\nu$)</td>
                <td><strong>0.0562</strong></td>
                <td>$[0.01, 0.20]$</td>
                <td>Tốc độ học (Shrinkage). Giá trị nhỏ giúp mô hình bước đi cẩn trọng trên không gian hàm, chống Overfitting.</td>
            </tr>
            <tr class="highlight-row">
                <td><code>max_depth</code></td>
                <td><strong>14</strong></td>
                <td>$[3, 4, 5, 6, 7, 10, 14, 16]$</td>
                <td>Độ sâu tối đa của mỗi cây. Cho phép mô hình học được các tương tác bậc cao giữa 14 thuộc tính.</td>
            </tr>
            <tr class="highlight-row">
                <td><code>subsample</code></td>
                <td><strong>0.95</strong></td>
                <td>$[0.6, 0.7, 0.8, 0.9, 1.0]$</td>
                <td>Tỷ lệ mẫu ngẫu nhiên cho mỗi cây (Stochastic Gradient Boosting), giúp bổ sung tính ngẫu nhiên làm giảm phương sai.</td>
            </tr>
            <tr>
                <td><code>min_samples_split</code></td>
                <td><strong>3</strong></td>
                <td>$[2, 5, 10]$</td>
                <td>Số lượng mẫu tối thiểu để tiếp tục phân nhánh tại một nút nội vi.</td>
            </tr>
            <tr>
                <td><code>min_samples_leaf</code></td>
                <td><strong>1</strong></td>
                <td>$[1, 2, 3]$</td>
                <td>Số lượng mẫu tối thiểu tại một nút lá.</td>
            </tr>
        </tbody>
    </table>
</div>


<div class='page-break'></div>

<!-- CHƯƠNG 5: MÔ TẢ DỮ LIỆU & QUY TRÌNH TIỀN XỬ LÝ CHỐNG RÒ RỈ -->

<div class="academic-section">
    <h1 class="chapter-title">5. MÔ TẢ DỮ LIỆU & QUY TRÌNH TIỀN XỬ LÝ CHỐNG RÒ RỈ</h1>
    
    <h2 class="sub-title">5.1. Nguồn gốc dữ liệu & Phân tích khám phá (EDA)</h2>
    <p>
        Hệ thống sử dụng bộ dữ liệu chuẩn hóa từ tập dữ liệu thương mại điện tử thực tế <em>E-Commerce Customer Churn Analysis and Prediction</em>, sau đó được tiền xử lý và chuyển dịch sang miền giá trị tiền tệ và nhân khẩu học phù hợp với thị trường bán lẻ Việt Nam.
    </p>
    <ul>
        <li><strong>Tổng số quan sát:</strong> 5.630 bản ghi khách hàng hoàn chỉnh.</li>
        <li><strong>Tập huấn luyện (Training Set - 80%):</strong> 4.504 bản ghi.</li>
        <li><strong>Tập kiểm thử độc lập (Test Set - 20%):</strong> 1.126 bản ghi (được cô lập hoàn toàn).</li>
        <li><strong>Số lượng đặc trưng ban đầu:</strong> 8 thuộc tính RFM+ và nhân khẩu học.</li>
        <li><strong>Số lượng đặc trưng sau biến đổi:</strong> 14 chiều (gồm 10 biến số sau chuẩn hóa và 4 biến nhị phân từ mã hóa One-Hot).</li>
    </ul>

    <h3 style="color: #0f172a; font-size: 14px;">Bảng thống kê mô tả các thuộc tính số học (Descriptive Statistics)</h3>
    <table>
        <thead>
            <tr>
                <th>Thuộc tính</th>
                <th>Giá trị trung bình (Mean)</th>
                <th>Độ lệch chuẩn (Std)</th>
                <th>Giá trị nhỏ nhất (Min)</th>
                <th>Trung vị (Median - 50%)</th>
                <th>Giá trị lớn nhất (Max)</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><code>age</code></td>
                <td>39.18 tuổi</td>
                <td>9.24</td>
                <td>18 tuổi</td>
                <td>38 tuổi</td>
                <td>70 tuổi</td>
            </tr>
            <tr>
                <td><code>total_purchases</code></td>
                <td>16.22 đơn</td>
                <td>9.45</td>
                <td>1 đơn</td>
                <td>14 đơn</td>
                <td>60 đơn</td>
            </tr>
            <tr>
                <td><code>avg_order_value</code></td>
                <td>1.768.420 đ</td>
                <td>842.150 đ</td>
                <td>150.000 đ</td>
                <td>1.520.000 đ</td>
                <td>4.500.000 đ</td>
            </tr>
            <tr>
                <td><code>days_since_last_purchase</code></td>
                <td>35.41 ngày</td>
                <td>28.62</td>
                <td>1 ngày</td>
                <td>28 ngày</td>
                <td>180 ngày</td>
            </tr>
            <tr>
                <td><code>satisfaction_score</code></td>
                <td>3.07 sao</td>
                <td>1.21</td>
                <td>1 sao</td>
                <td>3 sao</td>
                <td>5 sao</td>
            </tr>
            <tr class="highlight-row">
                <td><code>purchase_intensity</code> (FE)</td>
                <td>0.82 đơn/ngày</td>
                <td>1.14</td>
                <td>0.008</td>
                <td>0.48</td>
                <td>15.00</td>
            </tr>
            <tr class="highlight-row">
                <td><code>ltv_score</code> (FE)</td>
                <td>28.65 triệu đ</td>
                <td>24.31</td>
                <td>0.15 triệu đ</td>
                <td>21.28 triệu đ</td>
                <td>270.00 triệu đ</td>
            </tr>
            <tr class="highlight-row">
                <td><code>satisfaction_recency</code> (FE)</td>
                <td>4.12 điểm</td>
                <td>4.85</td>
                <td>0.16</td>
                <td>2.72</td>
                <td>75.00</td>
            </tr>
        </tbody>
    </table>

    <h2 class="sub-title">5.2. Vấn đề mất cân bằng mẫu và giải pháp phân tầng (Stratified Sampling)</h2>
    <p>
        Một thách thức kinh điển trong bài toán Churn là <strong>Sự mất cân bằng nhãn tự nhiên (Natural Class Imbalance)</strong>: Trong một doanh nghiệp đang hoạt động ổn định, đa số khách hàng sẽ ở lại hoặc phát sinh giao dịch tiếp theo, chỉ một tỷ lệ nhỏ quyết định rời bỏ:
    </p>
    <div class="formula-box">
        N_{\text{total}} = 5.630 \quad \implies \quad 
        \begin{cases}
        N(y = 1) = 4.672 \quad (\approx 83.0\% \text{ - Khách hàng quay lại}) \\
        N(y = 0) = 958 \quad (\approx 17.0\% \text{ - Khách hàng rời bỏ / Churn})
        \end{cases}
    </div>

    <h3 style="color: #0f172a; font-size: 14px;">Hiểm họa từ "Nghịch lý độ chính xác" (Accuracy Paradox)</h3>
    <p>
        Nếu một mô hình tầm thường (Naive Model) luôn dự đoán $100\%$ khách hàng đều quay lại ($y=1$), mô hình đó vẫn dễ dàng đạt độ chính xác $\text{Accuracy} = 83.0\%$. Tuy nhiên, mô hình này hoàn toàn vô dụng trong thực tế vì bỏ sót toàn bộ $100\%$ các khách hàng đang rời bỏ ($Recall_{\text{churn}} = 0$).<br>
        Để giải quyết triệt để vấn đề này, hệ thống áp dụng đồng thời hai giải pháp kỹ thuật:
    </p>
    <ol>
        <li>
            <strong>Phân chia lấy mẫu phân tầng (Stratified Train/Test Split):</strong><br>
            Sử dụng <code>train_test_split(..., stratify=y)</code> để đảm bảo cả hai tập Train (4.504 mẫu) và Test (1.126 mẫu) đều giữ tỷ lệ nhãn chính xác tuyệt đối là $83.0\%$ và $17.0\%$, loại bỏ hoàn toàn hiện tượng lệch phân phối.
        </li>
        <li>
            <strong>Cân bằng trọng số hàm mất mát (Cost-Sensitive Weighting):</strong><br>
            Trong quá trình huấn luyện các mô hình Logistic Regression và Random Forest, hệ thống kích hoạt tùy chọn <code>class_weight='balanced'</code>. Thuật toán tự động nhân trọng số phạt nghịch đảo với tần suất xuất hiện của từng lớp:
            $$w_c = \frac{N}{2 \times N_c}$$
            Theo đó, lớp Churn ($y=0$) được gán trọng số phạt $w_0 \approx 2.94$, cao gấp gần 5 lần so với lớp đa số ($w_1 \approx 0.60$). Điều này buộc giải thuật phải chú trọng học chính xác các trường hợp rời bỏ.
        </li>
    </ol>

    <h2 class="sub-title">5.3. Quy trình tiền xử lý dữ liệu chuẩn hóa chống rò rỉ dữ liệu (Anti-Data Leakage Pipeline)</h2>
    <p>
        <strong>Định nghĩa Data Leakage:</strong> Rò rỉ dữ liệu xảy ra khi thông tin từ tập kiểm thử (Test Set) vô tình được đưa vào quá trình huấn luyện của mô hình. Lỗi phổ biến nhất là việc người lập trình áp dụng các hàm như <code>StandardScaler.fit()</code> hoặc <code>SimpleImputer.fit()</code> trên toàn bộ bảng dữ liệu trước khi thực hiện chia tách Train/Test. Khi đó, giá trị trung bình $\mu$ và độ lệch chuẩn $\sigma$ của tập Test đã "thấm" vào tập Train, khiến mô hình đạt kết quả kiểm thử ảo rất cao nhưng thất bại khi chạy dữ liệu thực tế.
    </p>

    <div class="callout callout-warning">
        <strong>Kiến trúc Anti-Data Leakage của Boomerang Radar AI:</strong><br>
        Hàm <code>prepare_data()</code> trong <code>src/data_processing.py</code> được thiết kế theo quy trình nghiêm ngặt:
        <ol style="margin-bottom: 0;">
            <li>Bước 1: Nạp dữ liệu & Thực hiện Feature Engineering (các phép toán hoàn toàn mang tính độc lập trên từng dòng dữ liệu).</li>
            <li>Bước 2: Gọi <code>train_test_split()</code> để cô lập hoàn toàn tập $X_{\text{train}}$ và $X_{\text{test}}$.</li>
            <li>Bước 3: Khởi tạo <code>ColumnTransformer</code> chứa <code>StandardScaler</code> cho 10 cột số và <code>OneHotEncoder(drop='first')</code> cho 2 cột danh mục.</li>
            <li>Bước 4: Gọi <code>preprocessor.fit_transform(X_train)</code> <strong>DUY NHẤT trên tập Train</strong> để tính toán và lưu giữ vector $(\mu_{\text{train}}, \sigma_{\text{train}})$.</li>
            <li>Bước 5: Áp dụng <code>preprocessor.transform(X_test)</code> trên tập Test bằng các tham số đã đóng băng của tập Train mà không học lại.</li>
            <li>Bước 6: Lưu trữ đối tượng biến đổi ra file <code>models/preprocessor.joblib</code> phục vụ cho tầng suy luận (Inference).</li>
        </ol>
    </div>

    <h3 style="color: #0f172a; font-size: 14px;">Không gian đặc trưng 14 chiều sau khi biến đổi</h3>
    <p>Sau khi đi qua bộ <code>ColumnTransformer</code>, vector đầu vào có chính xác 14 chiều số học:</p>
    <table>
        <thead>
            <tr>
                <th>STT</th>
                <th>Tên đặc trưng sau biến đổi</th>
                <th>Phép biến đổi toán học</th>
                <th>Miền giá trị sau xử lý</th>
            </tr>
        </thead>
        <tbody>
            <tr><td>1</td><td><code>age</code></td><td>StandardScaler: $(x - \mu) / \sigma$</td><td>$\mathbb{R}$ (Mean $\approx 0$, Var $\approx 1$)</td></tr>
            <tr><td>2</td><td><code>total_purchases</code></td><td>StandardScaler: $(x - \mu) / \sigma$</td><td>$\mathbb{R}$</td></tr>
            <tr><td>3</td><td><code>avg_order_value</code></td><td>StandardScaler: $(x - \mu) / \sigma$</td><td>$\mathbb{R}$</td></tr>
            <tr><td>4</td><td><code>days_since_last_purchase</code></td><td>StandardScaler: $(x - \mu) / \sigma$</td><td>$\mathbb{R}$</td></tr>
            <tr><td>5</td><td><code>used_voucher</code></td><td>StandardScaler: $(x - \mu) / \sigma$</td><td>$\mathbb{R}$</td></tr>
            <tr><td>6</td><td><code>satisfaction_score</code></td><td>StandardScaler: $(x - \mu) / \sigma$</td><td>$\mathbb{R}$</td></tr>
            <tr><td>7</td><td><code>purchase_intensity</code></td><td>StandardScaler: $(x - \mu) / \sigma$</td><td>$\mathbb{R}$</td></tr>
            <tr><td>8</td><td><code>ltv_score</code></td><td>StandardScaler: $(x - \mu) / \sigma$</td><td>$\mathbb{R}$</td></tr>
            <tr><td>9</td><td><code>satisfaction_recency</code></td><td>StandardScaler: $(x - \mu) / \sigma$</td><td>$\mathbb{R}$</td></tr>
            <tr><td>10</td><td><code>voucher_low_value</code></td><td>StandardScaler: $(x - \mu) / \sigma$</td><td>$\mathbb{R}$</td></tr>
            <tr><td>11</td><td><code>gender_Nữ</code></td><td>OneHotEncoder (drop='first', Nam làm gốc)</td><td>$0$ hoặc $1$</td></tr>
            <tr><td>12</td><td><code>membership_level_Đồng</code></td><td>OneHotEncoder (drop='first', Bạc làm gốc)</td><td>$0$ hoặc $1$</td></tr>
            <tr><td>13</td><td><code>membership_level_Vàng</code></td><td>OneHotEncoder</td><td>$0$ hoặc $1$</td></tr>
            <tr><td>14</td><td><code>membership_level_Kim Cương</code></td><td>OneHotEncoder</td><td>$0$ hoặc $1$</td></tr>
        </tbody>
    </table>
</div>


<div class='page-break'></div>

<!-- CHƯƠNG 6: CÀI ĐẶT HỆ THỐNG VÀ XÂY DỰNG ỨNG DỤNG -->

<div class="academic-section">
    <h1 class="chapter-title">6. CÀI ĐẶT HỆ THỐNG VÀ XÂY DỰNG ỨNG DỤNG</h1>
    
    <h2 class="sub-title">6.1. Môi trường công nghệ và Cấu trúc mã nguồn</h2>
    <p>
        Hệ thống được phát triển trên nền tảng ngôn ngữ <strong>Python 3.10</strong> kết hợp với hệ sinh thái các thư viện khoa học dữ liệu hiện đại. Cấu trúc dự án được phân cấp mô-đun hóa rõ ràng, đáp ứng các tiêu chuẩn Clean Code và kiến trúc phần mềm hướng dịch vụ (Service-Oriented Architecture):
    </p>

    <div class="formula-box" style="font-size: 11px; line-height: 1.45;">
Boomerang_Radar_AI/<br>
&boxvr;&boxh;&boxh; app.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Máy chủ Flask, điều phối HTTP Endpoints & API Routing<br>
&boxvr;&boxh;&boxh; requirements.txt&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Danh mục các gói phụ thuộc (Flask, Scikit-learn, Pandas, Joblib)<br>
&boxvr;&boxh;&boxh; README.md&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Tài liệu hướng dẫn cài đặt môi trường và vận hành hệ thống<br>
&boxvr;&boxh;&boxh; .gitignore&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Bộ lọc tệp tin rác biên dịch (.pyc, cache, virtualenvs)<br>
&boxvr;&boxh;&boxh; BAO_CAO_DU_AN_BOOMERANG_RADAR_AI.pdf # Bản báo cáo toàn diện 30 trang in ấn chuẩn A4<br>
&boxvr;&boxh;&boxh; data/<br>
&boxv;&nbsp;&nbsp; &boxur;&boxh;&boxh; customer_repurchase_data.csv&nbsp;&nbsp;# Tệp dữ liệu sạch 5.630 bản ghi chuẩn hóa RFM+<br>
&boxvr;&boxh;&boxh; models/<br>
&boxv;&nbsp;&nbsp; &boxvr;&boxh;&boxh; gradient_boosting_model.joblib # Trọng số mô hình Champion (Gradient Boosting 94.23%)<br>
&boxv;&nbsp;&nbsp; &boxvr;&boxh;&boxh; random_forest_model.joblib&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Trọng số mô hình đối sánh Random Forest (91.56%)<br>
&boxv;&nbsp;&nbsp; &boxvr;&boxh;&boxh; decision_tree_model.joblib&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Trọng số mô hình đối sánh Decision Tree (74.96%)<br>
&boxv;&nbsp;&nbsp; &boxvr;&boxh;&boxh; logistic_regression_model.joblib# Trọng số mô hình Baseline Logistic Regression (68.47%)<br>
&boxv;&nbsp;&nbsp; &boxvr;&boxh;&boxh; preprocessor.joblib&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Đối tượng ColumnTransformer đã fit tham số<br>
&boxv;&nbsp;&nbsp; &boxvr;&boxh;&boxh; feature_names.joblib&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Danh mục tên 14 đặc trưng sau mã hóa OneHot<br>
&boxv;&nbsp;&nbsp; &boxvr;&boxh;&boxh; raw_feature_cols.joblib&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Danh mục 8 cột thuộc tính đầu vào ban đầu<br>
&boxv;&nbsp;&nbsp; &boxur;&boxh;&boxh; evaluation_results.json&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Tệp kết quả đánh giá thực nghiệm, metrics & Feature Importances<br>
&boxvr;&boxh;&boxh; src/<br>
&boxv;&nbsp;&nbsp; &boxvr;&boxh;&boxh; __init__.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Khởi tạo gói Python nội bộ<br>
&boxv;&nbsp;&nbsp; &boxvr;&boxh;&boxh; data_processing.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Pipeline nạp dữ liệu, FE, chống data leakage & lưu preprocessor<br>
&boxv;&nbsp;&nbsp; &boxvr;&boxh;&boxh; train.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Kịch bản huấn luyện, RandomizedSearchCV, 5-Fold CV & xuất artifacts<br>
&boxv;&nbsp;&nbsp; &boxur;&boxh;&boxh; predict.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Bộ máy suy luận đơn lẻ, batch inference & logic sinh khuyến nghị<br>
&boxur;&boxh;&boxh; templates/<br>
&nbsp;&nbsp;&nbsp;&nbsp;&boxur;&boxh;&boxh; index.html&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Giao diện Web Dashboard Bootstrap 5 tích hợp 4 phân hệ
    </div>

    <h2 class="sub-title">6.2. Cài đặt chi tiết các Module lõi trong hệ thống</h2>

    <h3 style="color: #0f172a; font-size: 14px;">Module 1: Tiền xử lý dữ liệu và Kỹ thuật đặc trưng (<code>src/data_processing.py</code>)</h3>
    <p>Module này đảm nhận hai nhiệm vụ sống còn: Kỹ thuật đặc trưng tương tác và Tiền xử lý chống rò rỉ dữ liệu.</p>
    <ul>
        <li>
            <strong>Hàm <code>engineer_features(df)</code>:</strong> Áp dụng các phép tính véc-tơ hóa bằng Pandas/NumPy để sinh đồng thời 4 cột tương tác mới:
            <div class="formula-box" style="font-size: 11px;">
df['purchase_intensity'] = df['total_purchases'] / (df['days_since_last_purchase'] + 1)<br>
df['ltv_score'] = df['total_purchases'] * df['avg_order_value'] / 1_000_000<br>
df['satisfaction_recency'] = df['satisfaction_score'] / (df['days_since_last_purchase'] + 1) * 30<br>
df['voucher_low_value'] = ((df['used_voucher'] == 1) & (df['avg_order_value'] &le; 300_000)).astype(int)
            </div>
        </li>
        <li>
            <strong>Hàm <code>prepare_data(test_size=0.2, random_state=42)</code>:</strong>
            Thiết lập <code>ColumnTransformer</code> chứa <code>StandardScaler</code> cho 10 biến số học và <code>OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore')</code> cho 2 biến danh mục. Gọi <code>fit_transform</code> trên <code>X_train</code> và chỉ <code>transform</code> trên <code>X_test</code>. Lưu giữ bộ biến đổi ra <code>models/preprocessor.joblib</code>.
        </li>
    </ul>

    <h3 style="color: #0f172a; font-size: 14px;">Module 2: Huấn luyện và Tối ưu hóa mô hình (<code>src/train.py</code>)</h3>
    <p>Chịu trách nhiệm thực thi pipeline huấn luyện tự động với tiêu chí dừng nghiệm khắt khe:</p>
    <ul>
        <li>
            <strong>Ngưỡng mục tiêu đánh giá:</strong> Thiết lập các hằng số kiểm định:
            $$F_1 \ge 0.92, \quad \text{Accuracy} \ge 0.90, \quad \text{ROC-AUC} \ge 0.90$$
        </li>
        <li>
            <strong>Chiến lược kiểm định chéo phân tầng:</strong> Khởi tạo <code>StratifiedKFold(n_splits=5, shuffle=True, random_state=42)</code> để duy trì tỷ lệ nhãn Churn 17% đồng đều trong cả 5 lần lặp.
        </li>
        <li>
            <strong>Tối ưu hóa siêu tham số:</strong> 
            Sử dụng <code>RandomizedSearchCV</code> với số vòng lặp $N_{\text{iter}} = 60$ cho Random Forest và $N_{\text{iter}} = 80$ cho Gradient Boosting. Tự động tính toán ma trận nhầm lẫn, trích xuất độ quan trọng của đặc trưng (Feature Importance), ghi nhận mô hình tốt nhất vào khóa <code>_best_model</code> và xuất báo cáo hoàn chỉnh ra file <code>models/evaluation_results.json</code>.
        </li>
    </ul>

    <h3 style="color: #0f172a; font-size: 14px;">Module 3: Bộ máy suy luận thời gian thực và sinh khuyến nghị (<code>src/predict.py</code>)</h3>
    <p>Module trung tâm phục vụ cho ứng dụng thực tế:</p>
    <ul>
        <li>
            <strong>Hàm <code>load_inference_artifacts(model_name)</code>:</strong> Áp dụng kỹ thuật nạp lười (Lazy Loading) để lưu bộ nhớ. Nạp đúng file nhị phân <code>.joblib</code> của mô hình được yêu cầu và bộ biến đổi <code>preprocessor.joblib</code>.
        </li>
        <li>
            <strong>Hàm <code>generate_synthesis_analysis(customer_dict)</code>:</strong>
            Phân tích 5 khía cạnh hành vi (tần suất mua, quy mô đơn hàng, khoảng cách ngày mua, trải nghiệm dịch vụ và hành vi săn khuyến mãi) để ghép nối thành câu văn ngữ cảnh tự nhiên tiếng Việt mượt mà, giúp chuyên viên bán hàng nắm bắt nhanh tâm lý khách hàng mà không cần phân tích từng con số thô.
        </li>
        <li>
            <strong>Hàm <code>predict_single_customer(...)</code>:</strong>
            Thực hiện toàn bộ quy trình: Ánh xạ 4 biến tương tác &rarr; Transform qua preprocessor &rarr; Tính $P(y=1) = \text{predict\_proba}()[0, 1]$ &rarr; So sánh với Threshold &rarr; Gán mức rủi ro &rarr; Gán kịch bản hành động Marketing tương ứng &rarr; Đóng gói Dictionary kết quả.
        </li>
        <li>
            <strong>Hàm <code>predict_batch_df(df_input, threshold=0.50)</code>:</strong>
            Tối ưu hóa vector hóa để dự đoán đồng thời hàng nghìn dòng dữ liệu từ DataFrame, gắn thêm 3 cột: <code>xac_suat_quay_lai_%</code>, <code>du_doan_quay_lai</code>, và <code>trang_thai</code> phục vụ xuất file CSV.
        </li>
    </ul>

    <h2 class="sub-title">6.3. Xây dựng dịch vụ Web REST API (<code>app.py</code>)</h2>
    <p>
        Máy chủ Flask cung cấp các REST API Endpoints được chuẩn hóa theo chuẩn trao đổi dữ liệu JSON:
    </p>
    <table>
        <thead>
            <tr>
                <th>HTTP Method</th>
                <th>Tuyến đường (Endpoint)</th>
                <th>Dữ liệu đầu vào (Payload)</th>
                <th>Chức năng nghiệp vụ & Phản hồi (Response)</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><code>GET</code></td>
                <td><code>/</code></td>
                <td>None</td>
                <td>Render giao diện trang chủ Web Dashboard Bootstrap 5 (<code>templates/index.html</code>).</td>
            </tr>
            <tr>
                <td><code>GET</code></td>
                <td><code>/api/stats</code></td>
                <td>None</td>
                <td>Trả về số lượng khách hàng, tỷ lệ quay lại, tỷ lệ rời bỏ, AOV toàn sàn và 15 dòng dữ liệu xem trước.</td>
            </tr>
            <tr>
                <td><code>GET</code></td>
                <td><code>/api/models</code></td>
                <td>None</td>
                <td>Trả về toàn bộ nội dung file <code>evaluation_results.json</code> phục vụ vẽ bảng benchmark và biểu đồ.</td>
            </tr>
            <tr>
                <td><code>POST</code></td>
                <td><code>/api/predict</code></td>
                <td>JSON chứa 8 chỉ số của 1 khách hàng + <code>threshold</code> + <code>model_name</code></td>
                <td>Thực hiện suy luận thời gian thực, trả về xác suất, phân tầng rủi ro, câu phân tích và lời khuyên nghiệp vụ.</td>
            </tr>
            <tr>
                <td><code>POST</code></td>
                <td><code>/api/predict-batch</code></td>
                <td>Multipart File Upload (CSV) hoặc lấy 30 dòng mẫu</td>
                <td>Dự đoán hàng loạt, trả về danh sách các bản ghi đã gán nhãn và xác suất phục vụ tải file kết quả.</td>
            </tr>
        </tbody>
    </table>

    <h2 class="sub-title">6.4. Thiết kế giao diện Dashboard tương tác (<code>templates/index.html</code>)</h2>
    <p>
        Giao diện Web Dashboard được thiết kế theo phong cách hiện đại với 4 phân hệ tương tác riêng biệt:
    </p>
    <ul>
        <li><strong>Tab 1: Overview (Tổng quan dữ liệu):</strong> Hiển thị 4 thẻ KPI vĩ mô (Tổng khách hàng, Tỷ lệ quay lại 83%, Tỷ lệ rời bỏ 17%, AOV trung bình) và bảng hiển thị 15 dòng dữ liệu mẫu trực quan.</li>
        <li><strong>Tab 2: Predictor (Radar dự đoán cá nhân):</strong> Cung cấp form nhập liệu trực quan cho 8 chỉ số; cho phép người dùng tùy chỉnh ngưỡng phân loại (Threshold Slider) từ $0.1$ đến $0.9$; thanh tiến trình radar hiển thị xác suất quay lại kèm mã màu trạng thái (Xanh lá: An toàn, Vàng: Cảnh báo, Đỏ: Rủi ro Churn cực cao) và hộp khuyến nghị hành động Marketing.</li>
        <li><strong>Tab 3: Benchmark (Đối chuẩn mô hình):</strong> Bảng so sánh 4 mô hình theo 5 chỉ số; bảng ma trận nhầm lẫn (Confusion Matrix) trực quan; và biểu đồ cột nằm ngang hiển thị mức độ quan trọng của 14 đặc trưng được vẽ tự động bằng thư viện <strong>Chart.js</strong>.</li>
        <li><strong>Tab 4: Batch Processing (Xử lý hàng loạt):</strong> Khu vực kéo thả tệp tin CSV, hiển thị bảng kết quả phân loại phân trang và nút chức năng <strong>Export CSV</strong> tải về máy.</li>
    </ul>
</div>


<div class='page-break'></div>

<!-- CHƯƠNG 7: ĐÁNH GIÁ KẾT QUẢ THỰC NGHIỆM -->

<div class="academic-section">
    <h1 class="chapter-title">7. ĐÁNH GIÁ KẾT QUẢ THỰC NGHIỆM</h1>
    
    <h2 class="sub-title">7.1. Hệ thống chỉ số đánh giá thực nghiệm (Evaluation Metrics Framework)</h2>
    <p>
        Để đánh giá khách quan và toàn diện năng lực của các mô hình học máy trên tập kiểm thử độc lập (Held-out Test Set gồm 1.126 khách hàng), hệ thống sử dụng một khung chỉ số đo lường chuẩn mực theo tiêu chuẩn quốc tế:
    </p>

    <h3 style="color: #0f172a; font-size: 14px;">1. Độ chính xác tổng thể (Accuracy)</h3>
    <div class="formula-box">
        \text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}
    </div>
    <p>Đo lường tỷ lệ các dự đoán đúng (cả khách quay lại và khách rời bỏ) trên tổng số mẫu kiểm thử.</p>

    <h3 style="color: #0f172a; font-size: 14px;">2. Độ chuẩn xác (Precision)</h3>
    <div class="formula-box">
        \text{Precision} = \frac{TP}{TP + FP}
    </div>
    <p>
        Trong số các khách hàng mà mô hình dự đoán là <em>"Sẽ quay lại"</em>, có bao nhiêu phần trăm thực sự quay lại mua sắm. Precision cao đồng nghĩa với việc hạn chế việc đưa ra dự báo lạc quan sai lầm.
    </p>

    <h3 style="color: #0f172a; font-size: 14px;">3. Độ nhạy / Thu hồi (Recall / Sensitivity)</h3>
    <div class="formula-box">
        \text{Recall} = \frac{TP}{TP + FN}
    </div>
    <p>
        Trong toàn bộ số khách hàng thực tế quay lại, mô hình đã "bắt trúng" được bao nhiêu phần trăm. Recall càng cao nghĩa là số lượng khách hàng trung thành bị bỏ sót (FN) càng nhỏ.
    </p>

    <h3 style="color: #0f172a; font-size: 14px;">4. Điểm F1 (F1-Score - Trung bình điều hòa)</h3>
    <div class="formula-box">
        F_1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} = \frac{2TP}{2TP + FP + FN}
    </div>
    <p>
        Là thước đo quan trọng nhất đối với bài toán mất cân bằng nhãn, đảm bảo mô hình không thể "gian lận" bằng cách hy sinh Precision để đổi lấy Recall hoặc ngược lại.
    </p>

    <h3 style="color: #0f172a; font-size: 14px;">5. Diện tích dưới đường cong ROC (Area Under the ROC Curve - ROC-AUC)</h3>
    <div class="formula-box">
        \text{ROC-AUC} = \int_{0}^{1} \text{TPR}(\text{FPR}^{-1}(t)) \, dt
    </div>
    <p>
        Đo lường năng lực phân biệt (Discriminative Power) tổng quát của mô hình trên mọi ngưỡng quyết định $\theta \in [0, 1]$. Giá trị $\text{ROC-AUC} \in [0.5, 1.0]$, giá trị càng tiệm cận $1.0$ thể hiện mô hình xếp hạng xác suất cực kỳ tin cậy.
    </p>

    <h2 class="sub-title">7.2. Bảng so sánh tổng hợp hiệu năng giữa các mô hình</h2>
    <p>
        Bảng đối chuẩn hiệu năng thực nghiệm trên tập kiểm thử độc lập gồm <strong>1.126 khách hàng</strong> hoàn toàn chưa từng xuất hiện trong quá trình huấn luyện hay tối ưu siêu tham số:
    </p>

    <table>
        <thead>
            <tr>
                <th>STT</th>
                <th>Mô hình thuật toán</th>
                <th>Accuracy</th>
                <th>Precision</th>
                <th>Recall</th>
                <th>F1-Score</th>
                <th>ROC-AUC</th>
                <th>Trạng thái mục tiêu</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>1</td>
                <td><strong>Logistic Regression</strong></td>
                <td>68.47%</td>
                <td>0.9395</td>
                <td>0.6635</td>
                <td>0.7777</td>
                <td>0.7906</td>
                <td>Chưa đạt (Baseline)</td>
            </tr>
            <tr>
                <td>2</td>
                <td><strong>Decision Tree</strong></td>
                <td>74.96%</td>
                <td>0.9348</td>
                <td>0.7511</td>
                <td>0.8329</td>
                <td>0.8089</td>
                <td>Khá tốt</td>
            </tr>
            <tr>
                <td>3</td>
                <td><strong>Random Forest</strong></td>
                <td>91.56%</td>
                <td>0.9367</td>
                <td>0.9637</td>
                <td>0.9500</td>
                <td>0.9575</td>
                <td>Đạt chỉ tiêu</td>
            </tr>
            <tr class="highlight-row">
                <td>4</td>
                <td><strong>Gradient Boosting</strong></td>
                <td><strong>94.23%</strong></td>
                <td><strong>0.9570</strong></td>
                <td><strong>0.9744</strong></td>
                <td><strong>0.9656</strong></td>
                <td><strong>0.9695</strong></td>
                <td><strong>&starf; VÔ ĐỊCH (Champion)</strong></td>
            </tr>
        </tbody>
    </table>

    <div class="callout callout-success">
        <strong>Phân tích khoa học lý giải sự vượt trội của Gradient Boosting:</strong><br>
        1. <strong>So với Logistic Regression (+25.76% Accuracy):</strong> Không gian ranh giới quyết định giữa khách quay lại và rời bỏ có tính phi tuyến cao. Mô hình tuyến tính hoàn toàn bất lực trong việc nắm bắt các quy tắc điều kiện lồng nhau.<br>
        2. <strong>So với Decision Tree (+19.27% Accuracy):</strong> Cây quyết định đơn lẻ có phương sai rất lớn và dễ bị mắc kẹt tại các cực tiểu cục bộ.<br>
        3. <strong>So với Random Forest (+2.67% Accuracy, +1.56% F1):</strong> Random Forest chỉ giảm phương sai nhờ việc lấy trung bình độc lập các cây. Ngược lại, Gradient Boosting sử dụng kỹ thuật tối ưu hóa phần dư theo hướng Gradient Descent, giúp mô hình tập trung học tỉ mỉ từng trường hợp biên giới khó phân loại, đạt được độ cân bằng hoàn hảo giữa phương sai và độ chệch (Bias-Variance Tradeoff).
    </div>

    <h2 class="sub-title">7.3. Phân tích Ma trận nhầm lẫn (Confusion Matrix Breakdown) và Tác động kinh tế</h2>
    <p>
        Ma trận nhầm lẫn của mô hình Gradient Boosting trên 1.126 khách hàng kiểm thử độc lập:
    </p>

    <table style="width: 75%; margin: 15px auto;">
        <thead>
            <tr>
                <th rowspan="2" style="text-align: center; vertical-align: middle;">Thực tế (Ground Truth)</th>
                <th colspan="2" style="text-align: center;">Dự đoán của mô hình AI (Predicted)</th>
            </tr>
            <tr>
                <th style="text-align: center; background: #334155;">Dự đoán Churn ($y=0$)</th>
                <th style="text-align: center; background: #334155;">Dự đoán Quay lại ($y=1$)</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td style="font-weight: bold; background: #f8fafc;">Khách Churn thực tế ($y=0$)</td>
                <td style="text-align: center; font-weight: bold; color: #0284c7;">TN = 149</td>
                <td style="text-align: center; font-weight: bold; color: #ef4444;">FP = 41</td>
            </tr>
            <tr>
                <td style="font-weight: bold; background: #f8fafc;">Khách Quay lại thực tế ($y=1$)</td>
                <td style="text-align: center; font-weight: bold; color: #ef4444;">FN = 24</td>
                <td style="text-align: center; font-weight: bold; color: #10b981;">TP = 912</td>
            </tr>
        </tbody>
    </table>

    <h3 style="color: #0f172a; font-size: 14px;">Phân tích tác động kinh tế học của hai loại sai lầm</h3>
    <ul>
        <li>
            <strong>Sai lầm loại 2 - Âm tính giả (False Negative - FN = 24):</strong><br>
            Khách hàng thực tế vẫn sẽ quay lại mua sắm nhưng hệ thống dự đoán nhầm thành có nguy cơ rời bỏ. Trong trường hợp này, doanh nghiệp sẽ gửi nhầm mã khuyến mãi hoặc voucher tri ân giảm 15% cho khách hàng này. Thiệt hại kinh tế chỉ là một phần nhỏ biên lợi nhuận của đơn hàng tiếp theo. <em>Mô hình đã khống chế số ca FN xuống mức cực thấp (chỉ 24 trên 1.126 khách, tương đương <strong>2.13%</strong>), bảo đảm doanh nghiệp không bị thất thoát lợi nhuận do phát voucher tràn lan.</em>
        </li>
        <li>
            <strong>Sai lầm loại 1 - Dương tính giả (False Positive - FP = 41):</strong><br>
            Khách hàng thực tế đã có ý định rời bỏ nhưng hệ thống chủ quan dự đoán họ vẫn sẽ quay lại. Doanh nghiệp sẽ không tiến hành can thiệp chăm sóc và hậu quả là mất vĩnh viễn khách hàng này vào tay đối thủ. Với số lượng 41 ca trên 190 khách Churn thực tế, tỷ lệ phát hiện sớm Churn của mô hình đạt:
            $$\text{Specificity} = \frac{TN}{TN + FP} = \frac{149}{149 + 41} \approx 78.42\%$$
            Đây là một tỷ lệ phát hiện rất ấn tượng đối với bài toán mất cân bằng nhãn cao trong thực tế thương mại điện tử.
        </li>
    </ul>

    <h2 class="sub-title">7.4. Xếp hạng và Đánh giá mức độ quan trọng của đặc trưng (Feature Importance)</h2>
    <p>
        Trong thuật toán Gradient Boosting, độ quan trọng của một đặc trưng $j$ được tính toán dựa trên mức độ suy giảm trung bình của hàm mất mát (MDI - Mean Decrease in Impurity) qua toàn bộ các điểm phân tách có sử dụng đặc trưng đó trong tất cả $M = 550$ cây:
    </p>

    <table>
        <thead>
            <tr>
                <th>Xếp hạng</th>
                <th>Tên đặc trưng</th>
                <th>Tỷ lệ đóng góp (%)</th>
                <th>Phân loại nguồn gốc</th>
                <th>Ý nghĩa và Phân tích tương quan</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>1</td>
                <td><code>avg_order_value</code></td>
                <td><strong>23.59%</strong></td>
                <td>Đặc trưng gốc</td>
                <td>Giá trị đơn trung bình là chỉ báo tài chính trực tiếp phản ánh mức độ cam kết của khách.</td>
            </tr>
            <tr>
                <td>2</td>
                <td><code>age</code></td>
                <td><strong>23.08%</strong></td>
                <td>Đặc trưng gốc</td>
                <td>Độ tuổi tương quan chặt chẽ với thói quen mua sắm và độ trung thành nhãn hàng.</td>
            </tr>
            <tr class="highlight-row">
                <td>3</td>
                <td><code>ltv_score</code></td>
                <td><strong>20.61%</strong></td>
                <td><strong>Kỹ thuật đặc trưng (FE)</strong></td>
                <td>Tổng đóng góp doanh thu tích lũy khẳng định nhóm khách hàng VIP luôn có xác suất quay lại cao nhất.</td>
            </tr>
            <tr class="highlight-row">
                <td>4</td>
                <td><code>satisfaction_recency</code></td>
                <td><strong>9.90%</strong></td>
                <td><strong>Kỹ thuật đặc trưng (FE)</strong></td>
                <td>Sự suy giảm điểm hài lòng theo thời gian cảnh báo chính xác thời điểm khách hàng chuẩn bị chuyển đổi.</td>
            </tr>
            <tr class="highlight-row">
                <td>5</td>
                <td><code>purchase_intensity</code></td>
                <td><strong>6.57%</strong></td>
                <td><strong>Kỹ thuật đặc trưng (FE)</strong></td>
                <td>Khách hàng có nhịp độ mua hàng dày đặc luôn có quán tính tiếp tục phát sinh giao dịch.</td>
            </tr>
            <tr>
                <td>6</td>
                <td><code>days_since_last_purchase</code></td>
                <td><strong>3.73%</strong></td>
                <td>Đặc trưng gốc</td>
                <td>Khoảng cách ngày mua càng lớn, rủi ro rời bỏ càng tăng cao.</td>
            </tr>
            <tr>
                <td>7</td>
                <td><code>satisfaction_score</code></td>
                <td><strong>3.58%</strong></td>
                <td>Đặc trưng gốc</td>
                <td>Điểm số đánh giá trải nghiệm thực tế.</td>
            </tr>
            <tr>
                <td>8</td>
                <td><code>gender_Nữ</code></td>
                <td><strong>3.23%</strong></td>
                <td>Mã hóa danh mục</td>
                <td>Khách hàng nữ có xu hướng phát sinh các giao dịch lặp lại thường xuyên hơn trong ngành thời trang/tiêu dùng.</td>
            </tr>
            <tr>
                <td>9</td>
                <td><code>membership_level_Đồng</code></td>
                <td><strong>2.02%</strong></td>
                <td>Mã hóa danh mục</td>
                <td>Hội viên hạng Đồng có mức độ gắn kết yếu nhất, tỷ lệ Churn cao nhất.</td>
            </tr>
            <tr>
                <td>10</td>
                <td><code>used_voucher</code></td>
                <td><strong>1.46%</strong></td>
                <td>Đặc trưng gốc</td>
                <td>Thói quen sử dụng mã giảm giá để kích thích mua sắm.</td>
            </tr>
            <tr>
                <td>11 - 14</td>
                <td>Các biến còn lại</td>
                <td><strong>2.23%</strong></td>
                <td>Mã hóa danh mục & FE</td>
                <td>Hạng Vàng, Kim Cương, Tổng đơn và nhóm săn voucher giá trị thấp.</td>
            </tr>
        </tbody>
    </table>

    <div class="callout callout-success">
        <strong>Tổng kết then chốt:</strong> Tổng tỷ trọng đóng góp của 4 biến sinh ra từ Feature Engineering (<code>ltv_score</code>, <code>satisfaction_recency</code>, <code>purchase_intensity</code>, <code>voucher_low_value</code>) chiếm tới <strong>37.08%</strong> tổng năng lực phân loại của mô hình. Điều này chứng minh luận điểm khoa học: <em>Kỹ thuật đặc trưng tương tác kết hợp tri thức kinh doanh sâu sắc chính là nhân tố cốt lõi giúp hệ thống AI bứt phá từ mức khá (91%) lên mức xuất sắc (94.23%)</em>.
    </div>
</div>


<div class='page-break'></div>

<!-- CHƯƠNG 8: KẾ HOẠCH TRIỂN KHAI HÀNH ĐỘNG, HƯỚNG PHÁT TRIỂN & KẾT LUẬN -->

<div class="academic-section">
    <h1 class="chapter-title">8. KẾ HOẠCH TRIỂN KHAI ACTIONABLE, HƯỚNG PHÁT TRIỂN & KẾT LUẬN</h1>
    
    <h2 class="sub-title">8.1. Kế hoạch triển khai hành động trong doanh nghiệp (Actionable Implementation Plan)</h2>
    <p>
        Để đưa hệ thống <strong>Boomerang Radar AI</strong> từ môi trường nghiên cứu vào vận hành thực tế tạo ra giá trị doanh thu thặng dư, chúng tôi xây dựng kế hoạch triển khai chi tiết gồm: Ma trận phân công trách nhiệm (RACI Matrix), Lộ trình triển khai 12 tuần (Gantt Roadmap) và Dự toán ngân sách kèm phân tích hoàn vốn đầu tư (ROI).
    </p>

    <h3 style="color: #0f172a; font-size: 13pt; margin-top: 14px;">a. Ma trận phân công trách nhiệm nghiệp vụ (RACI Matrix)</h3>
    <p>
        Quy định rõ ràng vai trò của từng bộ phận: <strong>R</strong> (Responsible - Người thực hiện), <strong>A</strong> (Accountable - Người chịu trách nhiệm phê duyệt), <strong>C</strong> (Consulted - Người được tham vấn), <strong>I</strong> (Informed - Người được thông báo kết quả).
    </p>

    <table>
        <thead>
            <tr>
                <th style="width: 32%;">Hạng mục công việc / Giai đoạn</th>
                <th style="width: 13%; text-align: center;">Ban Giám Đốc (C-Level)</th>
                <th style="width: 14%; text-align: center;">Đội ngũ Data / AI</th>
                <th style="width: 14%; text-align: center;">Kỹ thuật Backend / IT</th>
                <th style="width: 14%; text-align: center;">Đội ngũ Marketing / Growth</th>
                <th style="width: 13%; text-align: center;">Bộ phận CSKH</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>1. Phê duyệt ngân sách & KPI mục tiêu</td>
                <td style="text-align: center; font-weight: bold; color: #0284c7;">A</td>
                <td style="text-align: center;">C</td>
                <td style="text-align: center;">I</td>
                <td style="text-align: center;">C</td>
                <td style="text-align: center;">I</td>
            </tr>
            <tr>
                <td>2. Đóng gói & Triển khai Docker, REST API</td>
                <td style="text-align: center;">I</td>
                <td style="text-align: center; font-weight: bold; color: #0284c7;">R</td>
                <td style="text-align: center; font-weight: bold; color: #0f172a;">A / R</td>
                <td style="text-align: center;">I</td>
                <td style="text-align: center;">I</td>
            </tr>
            <tr>
                <td>3. Tích hợp Webhook CRM & Cổng Zalo/SMS</td>
                <td style="text-align: center;">I</td>
                <td style="text-align: center;">C</td>
                <td style="text-align: center; font-weight: bold; color: #0284c7;">R</td>
                <td style="text-align: center; font-weight: bold; color: #0f172a;">A</td>
                <td style="text-align: center;">C</td>
            </tr>
            <tr>
                <td>4. Thiết kế chính sách Voucher & Thông điệp</td>
                <td style="text-align: center;">C</td>
                <td style="text-align: center;">I</td>
                <td style="text-align: center;">I</td>
                <td style="text-align: center; font-weight: bold; color: #0284c7;">A / R</td>
                <td style="text-align: center;">C</td>
            </tr>
            <tr>
                <td>5. Vận hành gọi điện chăm sóc khách nguy cơ</td>
                <td style="text-align: center;">I</td>
                <td style="text-align: center;">I</td>
                <td style="text-align: center;">I</td>
                <td style="text-align: center;">C</td>
                <td style="text-align: center; font-weight: bold; color: #0284c7;">A / R</td>
            </tr>
            <tr>
                <td>6. Đánh giá kiểm định A/B Testing & Tái huấn luyện</td>
                <td style="text-align: center;">I</td>
                <td style="text-align: center; font-weight: bold; color: #0284c7;">A / R</td>
                <td style="text-align: center;">C</td>
                <td style="text-align: center;">R</td>
                <td style="text-align: center;">I</td>
            </tr>
        </tbody>
    </table>

    <h3 style="color: #0f172a; font-size: 13pt; margin-top: 14px;">b. Lộ trình triển khai thực tế 12 tuần (Gantt Timeline)</h3>
    <table>
        <thead>
            <tr>
                <th style="width: 15%;">Giai đoạn</th>
                <th style="width: 18%;">Mốc thời gian</th>
                <th style="width: 42%;">Mục tiêu & Công việc trọng tâm</th>
                <th style="width: 25%;">Sản phẩm bàn giao (Deliverables)</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Giai đoạn 1</strong></td>
                <td>Tuần 1 &ndash; Tuần 3</td>
                <td>Hoàn tất hạ tầng Cloud (AWS/GCP), đóng gói Docker container, thiết lập CI/CD pipeline tự động hóa kiểm thử mã nguồn.</td>
                <td>Docker Image chuẩn, API Endpoint nội bộ sẵn sàng.</td>
            </tr>
            <tr>
                <td><strong>Giai đoạn 2</strong></td>
                <td>Tuần 4 &ndash; Tuần 6</td>
                <td>Tích hợp kết nối 2 chiều giữa Boomerang Radar AI với hệ thống CRM (HubSpot/Salesforce) và hệ thống gửi tin Zalo ZNS / SMS.</td>
                <td>Webhook tự động kích hoạt chiến dịch theo phân tầng rủi ro.</td>
            </tr>
            <tr>
                <td><strong>Giai đoạn 3</strong></td>
                <td>Tuần 7 &ndash; Tuần 9</td>
                <td>Thực hiện thử nghiệm A/B Testing trên 20% tệp khách hàng có nguy cơ rời bỏ: Nhóm A (Can thiệp theo đề xuất của AI) vs Nhóm B (CSKH truyền thống).</td>
                <td>Báo cáo hiệu quả tỷ lệ chuyển đổi và tỷ lệ giữ chân thực tế.</td>
            </tr>
            <tr>
                <td><strong>Giai đoạn 4</strong></td>
                <td>Tuần 10 &ndash; Tuần 12</td>
                <td>Triển khai diện rộng 100% tệp khách hàng toàn sàn, bàn giao tài liệu hướng dẫn vận hành và kích hoạt cơ chế tự động tái huấn luyện định kỳ.</td>
                <td>Hệ thống vận hành chính thức (Go-live toàn diện).</td>
            </tr>
        </tbody>
    </table>

    <h3 style="color: #0f172a; font-size: 13pt; margin-top: 14px;">c. Dự toán ngân sách và Phân tích hiệu quả kinh tế (ROI Forecast)</h3>
    <p>
        Giả định áp dụng trên quy mô doanh nghiệp bán lẻ có <strong>50.000 khách hàng hoạt động</strong> với doanh thu trung bình 1.500.000 đ/khách/năm:
    </p>

    <table>
        <thead>
            <tr>
                <th>Hạng mục chi phí / Lợi ích</th>
                <th>Dự toán năm đầu tiên</th>
                <th>Cơ sở tính toán & Ý nghĩa tài chính</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Chi phí máy chủ Cloud & Hạ tầng</td>
                <td>45.000.000 VNĐ</td>
                <td>Máy chủ AWS EC2 c5.large + CloudWatch monitoring ($150/tháng &times; 12 tháng).</td>
            </tr>
            <tr>
                <td>Chi phí tích hợp Webhook & Zalo ZNS</td>
                <td>35.000.000 VNĐ</td>
                <td>Chi phí gửi 70.000 tin nhắn Zalo ZNS tương tác mục tiêu (500 đ/tin).</td>
            </tr>
            <tr>
                <td>Ngân sách Voucher kích hoạt cứu vãn</td>
                <td>180.000.000 VNĐ</td>
                <td>Phát 3.000 voucher giảm giá (trung bình 60.000 đ/voucher) cho nhóm rủi ro cao.</td>
            </tr>
            <tr>
                <td><strong>TỔNG CHI PHÍ ĐẦU TƯ (CAPEX + OPEX)</strong></td>
                <td><strong>260.000.000 VNĐ</strong></td>
                <td>Toàn bộ ngân sách cần phê duyệt để đưa hệ thống vào vận hành 1 năm.</td>
            </tr>
            <tr class="highlight-row">
                <td><strong>DOANH THU CỨU VÃN KỲ VỌNG (SAVED REVENUE)</strong></td>
                <td><strong>1.050.000.000 VNĐ</strong></td>
                <td>Giữ chân thành công 700 khách hàng tiềm năng &times; LTV tối thiểu 1.500.000 đ/năm.</td>
            </tr>
            <tr class="highlight-row">
                <td><strong>LỢI NHUẬN RÒNG GIA TĂNG (NET PROFIT)</strong></td>
                <td><strong>790.000.000 VNĐ</strong></td>
                <td>Doanh thu cứu vãn trừ đi toàn bộ chi phí vận hành và chiết khấu.</td>
            </tr>
            <tr class="highlight-row">
                <td><strong>TỶ SUẤT HOÀN VỐN (ROI)</strong></td>
                <td><strong>303.8%</strong></td>
                <td>$\text{ROI} = \frac{790.000.000}{260.000.000} \approx 303.8\%$ (Thu hồi vốn hoàn toàn sau 4 tháng).</td>
            </tr>
        </tbody>
    </table>

    <h2 class="sub-title">8.2. Ứng dụng Trí tuệ Nhân tạo có thể giải thích (Explainable AI với SHAP)</h2>
    <p>
        Để chuyển đổi từ mô hình "hộp đen" (Black-Box) sang "hộp kính" (Glass-Box) phục vụ kiểm toán quyết định, hệ thống tích hợp thuật toán <strong>TreeSHAP</strong> (Lundberg & Lee, 2017). Dựa trên lý thuyết giá trị Shapley trong Lý thuyết trò chơi hợp tác của nhà kinh tế học đoạt giải Nobel <em>Lloyd Shapley (1953)</em>:
    </p>
    <div class="formula-box">
        \phi_i(v) = \sum_{S \subseteq N \setminus \{i\}} \frac{|S|! \, (|N| - |S| - 1)!}{|N|!} \left[ v(S \cup \{i\}) - v(S) \right]
    </div>
    <p>
        Khi tích hợp SHAP vào Dashboard, nhân viên CSKH có thể xem <strong>Biểu đồ thác nước (Waterfall Plot)</strong> của từng khách hàng cá nhân. Ví dụ: Khách hàng Nguyễn Văn A bị cảnh báo Churn $85\%$ do số ngày chưa mua đạt $120$ ngày (kéo tụt $-35\%$ xác suất) và điểm hài lòng đạt $2$ sao (kéo tụt thêm $-25\%$). Điều này giúp nhân viên nắm đúng lý do cốt lõi để đưa ra lời xin lỗi và mã đền bù thỏa đáng.
    </p>

    <h2 class="sub-title">8.3. Mở rộng kiến trúc thuật toán chuyên sâu (LightGBM, CatBoost, TabNet)</h2>
    <p>Khi quy mô dữ liệu mở rộng từ hàng chục nghìn lên hàng triệu bản ghi, hệ thống sẽ mở rộng nghiên cứu sang 3 kiến trúc chuyên biệt:</p>
    <ul>
        <li><strong>LightGBM (Microsoft):</strong> Cơ chế phân nhánh theo lá (Leaf-wise) kết hợp gom cụm dữ liệu theo biểu đồ tần suất (Histogram-based), giúp tăng tốc độ huấn luyện lên 7 lần và giảm 75% RAM.</li>
        <li><strong>CatBoost (Yandex):</strong> Tối ưu số 1 cho các biến danh mục phức tạp (như danh mục sản phẩm, kênh quảng cáo) nhờ kỹ thuật Ordered Target Statistics chống rò rỉ mục tiêu.</li>
        <li><strong>TabNet (Google Cloud AI):</strong> Mạng nơ-ron học sâu sử dụng cơ chế chú ý tuần tự (Sequential Attention) dành riêng cho dữ liệu bảng, tự động học biểu diễn đặc trưng mà không cần tiền xử lý thủ công.</li>
    </ul>

    <h2 class="sub-title">8.4. Thiết lập hệ thống MLOps và Tự động hóa tiếp thị đa kênh</h2>
    <ul>
        <li>
            <strong>Giám sát trôi dữ liệu (Data Drift Monitoring):</strong> Đo lường chỉ số ổn định quần thể (Population Stability Index - PSI) hàng tuần:
            $$\text{PSI} = \sum_{k=1}^K \left( \text{Actual}_k - \text{Expected}_k \right) \times \ln\left( \frac{\text{Actual}_k}{\text{Expected}_k} \right)$$
            Nếu $\text{PSI} > 0.25$, hệ thống tự động gửi cảnh báo Slack/Email và kích hoạt quy trình huấn luyện lại (Auto-Retraining Pipeline).
        </li>
        <li>
            <strong>Tự động hóa đa kênh (Omnichannel Retention):</strong> Kết nối trực tiếp API của hệ thống với hệ sinh thái tiếp thị tự động (Zalo ZNS, Twilio SMS, SendGrid Email). Khách hàng có nguy cơ rời bỏ sẽ nhận được thông điệp cứu vãn ngay trong "thời điểm vàng" mà không cần sự can thiệp thủ công từ con người.
        </li>
    </ul>

    <h2 class="sub-title">8.5. Kết luận tổng quan đề tài</h2>
    <p>
        Dự án <strong>Boomerang Radar AI</strong> đã hoàn thành xuất sắc toàn bộ mục tiêu đề ra:
    </p>
    <ol>
        <li>Xây dựng cơ sở lý thuyết kinh tế học hành vi kết hợp giải tích toán học của mô hình RFM+ mở rộng.</li>
        <li>Chứng minh tính đột phá của 4 đặc trưng tương tác phi tuyến, đóng góp tới <strong>37.08%</strong> sức mạnh của mô hình.</li>
        <li>Thiết lập pipeline tiền xử lý dữ liệu chuẩn công nghiệp, tuân thủ tuyệt đối quy chuẩn chống rò rỉ dữ liệu (Anti-Data Leakage).</li>
        <li>Huấn luyện và đối chuẩn thành công 4 thuật toán học máy, khẳng định mô hình <strong>Gradient Boosting Classifier</strong> vượt trội với độ chính xác <strong>94.23%</strong>, $F_1\text{-score}$ đạt <strong>96.56%</strong> và $\text{ROC-AUC}$ đạt <strong>96.95%</strong>.</li>
        <li>Cung cấp kế hoạch triển khai hành động rõ ràng với Ma trận RACI, Lộ trình Gantt 12 tuần và tỷ suất hoàn vốn đầu tư kỳ vọng đạt <strong>303.8%</strong>, đưa giải pháp sẵn sàng đi vào thực tiễn kinh doanh.</li>
    </ol>

    <div class="page-break"></div>

    <!-- TÀI LIỆU THAM KHẢO CHUẨN APA -->
    <h1 class="chapter-title">TÀI LIỆU THAM KHẢO (REFERENCES - CHUẨN APA)</h1>
    <ol class="ref-list" style="font-size: 11.5pt; line-height: 1.65;">
        <li>Arik, S. Ö., & Pfister, T. (2021). <em>TabNet: Attentive interpretable tabular learning</em>. Proceedings of the AAAI Conference on Artificial Intelligence, 35(8), 6679-6687.</li>
        <li>Breiman, L. (2001). <em>Random forests</em>. Machine Learning, 45(1), 5-32. https://doi.org/10.1023/A:1010933404324</li>
        <li>Chen, T., & Guestrin, C. (2016). <em>XGBoost: A scalable tree boosting system</em>. Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 785-794.</li>
        <li>Fader, P. S., Hardie, B. G., & Lee, K. L. (2005). <em>"Counting your customers" the easy way: An alternative to the Pareto/NBD model</em>. Marketing Science, 24(2), 275-284.</li>
        <li>Friedman, J. H. (2001). <em>Greedy function approximation: A gradient boosting machine</em>. Annals of Statistics, 29(5), 1189-1232. https://doi.org/10.1214/aos/1013203451</li>
        <li>Hughes, A. M. (2005). <em>Strategic database marketing: The masterplan for starting and managing a profitable, customer-based marketing program</em> (3rd ed.). McGraw-Hill Companies.</li>
        <li>Lundberg, S. M., & Lee, S. I. (2017). <em>A unified approach to interpreting model predictions</em>. Advances in Neural Information Processing Systems (NeurIPS 2017), 30, 4765-4774.</li>
        <li>Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., ... & Duchesnay, É. (2011). <em>Scikit-learn: Machine learning in Python</em>. Journal of Machine Learning Research, 12, 2825-2830.</li>
        <li>Prokhorenkova, L., Gusev, G., Vorobev, A., Dorogush, A. V., & Gulin, A. (2018). <em>CatBoost: Unbiased boosting with categorical features</em>. Advances in Neural Information Processing Systems (NeurIPS 2018), 31, 6638-6648.</li>
        <li>Reichheld, F. F., & Sasser, W. E. (1990). <em>Zero defections: Quality comes to services</em>. Harvard Business Review, 68(5), 105-111.</li>
    </ol>
</div>
