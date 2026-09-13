<!-- PHẦN 1: BÌA ĐIỀU HÀNH, TÓM TẮT DÀNH CHO LÃNH ĐẠO & CHƯƠNG 1 -->

<div class="cover-page">
    <div class="institution">BỘ GIÁO DỤC VÀ ĐÀO TẠO &bull; HỆ THỐNG ĐÀO TẠO CÔNG NGHỆ THÔNG TIN</div>
    <div class="faculty">KHOA CÔNG NGHỆ THÔNG TIN & KHOA HỌC DỮ LIỆU ỨNG DỤNG</div>
    
    <div style="margin: 35px 0 20px 0;">
        <div class="cover-badge">BÁO CÁO NGHIÊN CỨU & PHÁT TRIỂN HỆ THỐNG AI DOANH NGHIỆP</div>
        <h1 class="main-title">BOOMERANG RADAR AI</h1>
        <div class="sub-title-cover">
            HỆ THỐNG TRÍ TUỆ NHÂN TẠO DỰ ĐOÁN KHẢ NĂNG KHÁCH HÀNG QUAY LẠI<br>
            VÀ ĐỊNH VỊ SỚM NGUY CƠ RỜI BỎ DỰA TRÊN MÔ HÌNH HÀNH VI RFM+
        </div>
    </div>

    <!-- HỘP ĐỐI TƯỢNG VÀ CÂU HỎI TRUNG TÂM -->
    <div style="width: 100%; background: #ffffff; border: 1.5px solid #000000; border-radius: 4px; padding: 12px 18px; text-align: left; margin: 15px 0; font-family: 'Times New Roman', serif;">
        <div style="font-size: 11pt; font-weight: bold; color: #000000; margin-bottom: 4px; text-transform: uppercase;">
            &bull; ĐỐI TƯỢNG BÁO CÁO & CÂU HỎI TRUNG TÂM (EXECUTIVE SCOPE)
        </div>
        <div style="font-size: 10.5pt; color: #111111; line-height: 1.5;">
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
    
    <div class="callout" style="font-size: 11pt; line-height: 1.6;">
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
