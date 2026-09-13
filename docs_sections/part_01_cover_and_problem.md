<!-- PHẦN 1: BÌA, TÓM TẮT & CHƯƠNG 1: PHÁT BIỂU BÀI TOÁN -->

<div class="cover-page">
    <div class="institution">BỘ GIÁO DỤC VÀ ĐÀO TẠO &bull; HỆ THỐNG ĐÀO TẠO CÔNG NGHỆ THÔNG TIN</div>
    <div class="faculty">KHOA CÔNG NGHỆ THÔNG TIN & TRÍ TUỆ NHÂN TẠO</div>
    
    <div style="margin: 40px 0 20px 0;">
        <div class="cover-badge">BÁO CÁO NGHIÊN CỨU & PHÁT TRIỂN HỆ THỐNG AI</div>
        <h1 class="main-title">BOOMERANG RADAR AI</h1>
        <div class="sub-title-cover">
            HỆ THỐNG TRÍ TUỆ NHÂN TẠO DỰ ĐOÁN KHẢ NĂNG KHÁCH HÀNG QUAY LẠI<br>
            VÀ NHẬN DIỆN SỚM NGUY CƠ RỜI BỎ TRÊN NỀN TẢNG DỮ LIỆU RFM+ MỞ RỘNG
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
            <span class="m-val">550</span>
            <span class="m-lbl">Cây Boosting tối ưu</span>
        </div>
    </div>

    <div class="cover-meta-info">
        <table class="meta-table">
            <tr>
                <td style="width: 35%;"><strong>Đề tài nghiên cứu:</strong></td>
                <td>Dự đoán Khả năng Khách hàng Quay lại Mua sắm (Customer Repurchase & Churn Prediction)</td>
            </tr>
            <tr>
                <td><strong>Lĩnh vực chuyên môn:</strong></td>
                <td>Học máy ứng dụng (Applied Machine Learning), Khoa học Dữ liệu (Data Science)</td>
            </tr>
            <tr>
                <td><strong>Thuật toán chủ đạo:</strong></td>
                <td>Gradient Boosting Classifier, Random Forest, Decision Tree, Logistic Regression</td>
            </tr>
            <tr>
                <td><strong>Nền tảng triển khai:</strong></td>
                <td>Python 3.10, Scikit-learn, Flask REST API, Bootstrap 5 Responsive Dashboard</td>
            </tr>
            <tr>
                <td><strong>Thời gian thực hiện:</strong></td>
                <td>Năm học 2025 - 2026</td>
            </tr>
        </table>
    </div>
</div>

<div class="page-break"></div>

<!-- TÓM TẮT ĐỀ TÀI (ABSTRACT) -->
<div class="academic-section">
    <h1 class="chapter-title">TÓM TẮT ĐỀ TÀI (ABSTRACT)</h1>
    
    <div class="abstract-box">
        <p><strong>Tiếng Việt:</strong> Trong bối cảnh bùng nổ của thương mại điện tử và bán lẻ đa kênh, bài toán duy trì lòng trung thành của khách hàng và tối ưu hóa giá trị trọn đời (Customer Lifetime Value - CLV) đã trở thành trọng tâm chiến lược sống còn của mọi doanh nghiệp. Chi phí thu hút một khách hàng mới (CAC) hiện nay đắt gấp 5 đến 7 lần so với chi phí giữ chân một khách hàng hiện hữu. Tuy nhiên, phần lớn các doanh nghiệp bán lẻ vẫn đang tiếp cận bài toán chăm sóc khách hàng một cách thụ động, chỉ can thiệp khi khách hàng đã ngừng phát sinh giao dịch trong một thời gian dài, dẫn đến hiệu quả cứu vãn thấp và chi phí tiếp thị bị lãng phí nghiêm trọng.</p>
        <p>Báo cáo này trình bày quá trình nghiên cứu, thiết kế và phát triển toàn diện hệ thống <strong>Boomerang Radar AI</strong> – một giải pháp Trí tuệ Nhân tạo thông minh hoạt động như trạm radar liên tục quét và giám sát dữ liệu hành vi của người tiêu dùng. Hệ thống tích hợp bộ chỉ số hành vi mở rộng RFM+ (Recency, Frequency, Monetary kết hợp Nhân khẩu học và Điểm hài lòng trải nghiệm), tự động sinh 4 biến tương tác phi tuyến (Interaction Features) giúp khai phá sâu sắc nhịp độ tiêu dùng và mức độ gắn kết của khách hàng. Trên cơ sở đó, 4 thuật toán Học máy đại diện (Logistic Regression, Decision Tree, Random Forest, Gradient Boosting) được xây dựng, huấn luyện và tối ưu hóa siêu tham số thông qua kỹ thuật Stratified 5-Fold Cross-Validation và RandomizedSearchCV. Kết quả thực nghiệm trên tập kiểm thử độc lập gồm 1.126 khách hàng chứng minh mô hình <strong>Gradient Boosting Classifier</strong> đạt hiệu năng vượt bậc với độ chính xác <strong>94.23%</strong>, $F_1\text{-score}$ đạt <strong>96.56%</strong> và chỉ số $\text{ROC-AUC}$ đạt <strong>96.95%</strong>. Hệ thống được đóng gói hoàn chỉnh dưới dạng Web Application với kiến trúc REST API độ trễ cực thấp (< 50ms), hỗ trợ dự đoán thời gian thực cho từng khách hàng đơn lẻ, xử lý hàng loạt theo tệp CSV, cung cấp cơ chế phân loại rủi ro 4 cấp độ, tự động sinh phân tích hành vi tự nhiên và đề xuất kịch bản can thiệp kịp thời nhằm tạo ra "hiệu ứng Boomerang" kéo khách hàng quay trở lại.</p>
        <p><strong>Từ khóa:</strong> Khách hàng quay lại (Customer Repurchase), Rời bỏ khách hàng (Customer Churn), Gradient Boosting, RFM Analysis, Kỹ thuật đặc trưng (Feature Engineering), Trí tuệ Nhân tạo trong Thương mại điện tử.</p>
        <hr style="border: 0; border-top: 1px solid #cbd5e1; margin: 15px 0;">
        <p><strong>English Abstract:</strong> In modern retail and e-commerce ecosystems, customer retention and Customer Lifetime Value (CLV) optimization have emerged as core competitive advantages. Acquiring a new customer (CAC) is five to seven times more costly than retaining an existing one. Nevertheless, traditional Customer Relationship Management (CRM) workflows remain reactive, identifying churned clients only after prolonged inactivity. This paper introduces <strong>Boomerang Radar AI</strong>, a comprehensive end-to-end Machine Learning system designed to predict customer repurchase probability and deliver early churn warnings. Leveraging engineered RFM+ attributes alongside non-linear interaction features, the pipeline benchmarked Logistic Regression, Decision Trees, Random Forests, and Gradient Boosting algorithms under Stratified 5-Fold Cross-Validation and Randomized Hyperparameter Optimization. Experimental evaluations on a strictly isolated holdout test set of 1,126 customer records demonstrate that the <strong>Gradient Boosting Classifier</strong> outperforms competing baselines, achieving an accuracy of <strong>94.23%</strong>, an $F_1\text{-score}$ of <strong>96.56%</strong>, and an area under the ROC curve ($\text{ROC-AUC}$) of <strong>96.95%</strong>. The production-ready system is delivered as an interactive Flask-based Web Dashboard and low-latency REST API, featuring real-time single-customer inference, batch CSV ingestion, 4-tier churn risk stratification, automated natural-language behavioral synthesis, and actionable omnichannel marketing interventions.</p>
    </div>
</div>

<div class="page-break"></div>

<!-- MỤC LỤC CHI TIẾT -->
<div class="academic-section">
    <h1 class="chapter-title">MỤC LỤC BÁO CÁO</h1>
    <table class="toc-table">
        <tr class="toc-head"><th style="width: 80%;">Nội dung chương mục</th><th style="width: 20%; text-align: right;">Trang</th></tr>
        <tr><td><strong>LỜI NÓI ĐẦU & TÓM TẮT ĐỀ TÀI (ABSTRACT)</strong></td><td style="text-align: right;">ii</td></tr>
        <tr><td><strong>DANH MỤC CÁC TỪ VIẾT TẮT & THUẬT NGỮ CHUYÊN MÔN</strong></td><td style="text-align: right;">iv</td></tr>
        <tr><td><strong>DANH MỤC BẢNG BIỂU & HÌNH VẼ</strong></td><td style="text-align: right;">v</td></tr>
        <tr><td><strong class="toc-chap">CHƯƠNG 1: PHÁT BIỂU BÀI TOÁN & CƠ SỞ LÝ THUYẾT</strong></td><td style="text-align: right;">1</td></tr>
        <tr><td class="toc-sub">1.1. Bối cảnh ngành kinh doanh Bán lẻ và Thương mại điện tử</td><td style="text-align: right;">1</td></tr>
        <tr><td class="toc-sub">1.2. Lý thuyết Vòng đời Khách hàng (Customer Lifecycle) và Chỉ số LTV</td><td style="text-align: right;">2</td></tr>
        <tr><td class="toc-sub">1.3. Bản chất toán học của bài toán Phân loại Khách hàng Quay lại</td><td style="text-align: right;">3</td></tr>
        <tr><td class="toc-sub">1.4. Ý nghĩa thực tiễn và Sứ mệnh của giải pháp Boomerang Radar AI</td><td style="text-align: right;">4</td></tr>
        <tr><td><strong class="toc-chap">CHƯƠNG 2: XÁC ĐỊNH YÊU CẦU HỆ THỐNG, INPUT VÀ OUTPUT</strong></td><td style="text-align: right;">5</td></tr>
        <tr><td class="toc-sub">2.1. Yêu cầu chức năng và phi chức năng</td><td style="text-align: right;">5</td></tr>
        <tr><td class="toc-sub">2.2. Đặc tả chi tiết các thuộc tính đầu vào (Input Specification)</td><td style="text-align: right;">6</td></tr>
        <tr><td class="toc-sub">2.3. Đặc tả cấu trúc dữ liệu đầu ra và logic phân tầng rủi ro (Output)</td><td style="text-align: right;">7</td></tr>
        <tr><td><strong class="toc-chap">CHƯƠNG 3: THIẾT KẾ SƠ ĐỒ KHỐI VÀ KIẾN TRÚC HỆ THỐNG</strong></td><td style="text-align: right;">9</td></tr>
        <tr><td class="toc-sub">3.1. Kiến trúc phân tầng tổng thể (6-Layer Architecture)</td><td style="text-align: right;">9</td></tr>
        <tr><td class="toc-sub">3.2. Thiết kế luồng dữ liệu (Data Pipeline & Inference Flow)</td><td style="text-align: right;">11</td></tr>
        <tr><td class="toc-sub">3.3. Cơ chế phân tách module và đóng gói Artifacts</td><td style="text-align: right;">12</td></tr>
        <tr><td><strong class="toc-chap">CHƯƠNG 4: MÔ TẢ THUẬT TOÁN & CƠ SỞ TOÁN HỌC</strong></td><td style="text-align: right;">13</td></tr>
        <tr><td class="toc-sub">4.1. Cơ sở toán học của 4 đặc trưng tương tác phi tuyến (Interaction Features)</td><td style="text-align: right;">13</td></tr>
        <tr><td class="toc-sub">4.2. Thuật toán Hồi quy Logistic (Logistic Regression)</td><td style="text-align: right;">15</td></tr>
        <tr><td class="toc-sub">4.3. Thuật toán Cây quyết định (Decision Tree Classifier)</td><td style="text-align: right;">16</td></tr>
        <tr><td class="toc-sub">4.4. Thuật toán Rừng ngẫu nhiên (Random Forest Classifier)</td><td style="text-align: right;">17</td></tr>
        <tr><td class="toc-sub">4.5. Thuật toán Gradient Boosting Classifier (Champion Model)</td><td style="text-align: right;">18</td></tr>
        <tr><td class="toc-sub">4.6. Phương pháp tối ưu siêu tham số và Đánh giá chéo phân tầng (Stratified CV)</td><td style="text-align: right;">20</td></tr>
        <tr><td><strong class="toc-chap">CHƯƠNG 5: MÔ TẢ DỮ LIỆU & QUY TRÌNH TIỀN XỬ LÝ CHỐNG RÒ RỈ</strong></td><td style="text-align: right;">21</td></tr>
        <tr><td class="toc-sub">5.1. Nguồn gốc dữ liệu và Phân tích khám phá (EDA)</td><td style="text-align: right;">21</td></tr>
        <tr><td class="toc-sub">5.2. Vấn đề mất cân bằng mẫu và giải pháp xử lý phân tầng</td><td style="text-align: right;">22</td></tr>
        <tr><td class="toc-sub">5.3. Quy trình tiền xử lý dữ liệu chuẩn hóa chống Data Leakage</td><td style="text-align: right;">23</td></tr>
        <tr><td><strong class="toc-chap">CHƯƠNG 6: CÀI ĐẶT HỆ THỐNG VÀ XÂY DỰNG ỨNG DỤNG</strong></td><td style="text-align: right;">24</td></tr>
        <tr><td class="toc-sub">6.1. Môi trường công nghệ và Cấu trúc mã nguồn</td><td style="text-align: right;">24</td></tr>
        <tr><td class="toc-sub">6.2. Cài đặt chi tiết các Module nghiệp vụ (Data, Train, Predict)</td><td style="text-align: right;">25</td></tr>
        <tr><td class="toc-sub">6.3. Xây dựng dịch vụ Web REST API và Giao diện Dashboard</td><td style="text-align: right;">26</td></tr>
        <tr><td><strong class="toc-chap">CHƯƠNG 7: ĐÁNH GIÁ KẾT QUẢ THỰC NGHIỆM</strong></td><td style="text-align: right;">27</td></tr>
        <tr><td class="toc-sub">7.1. Bảng so sánh tổng hợp hiệu năng giữa các mô hình</td><td style="text-align: right;">27</td></tr>
        <tr><td class="toc-sub">7.2. Phân tích chi tiết Ma trận nhầm lẫn (Confusion Matrix)</td><td style="text-align: right;">28</td></tr>
        <tr><td class="toc-sub">7.3. Xếp hạng và Đánh giá độ quan trọng của đặc trưng (Feature Importance)</td><td style="text-align: right;">29</td></tr>
        <tr><td><strong class="toc-chap">CHƯƠNG 8: HƯỚNG PHÁT TRIỂN & KẾT LUẬN</strong></td><td style="text-align: right;">30</td></tr>
        <tr><td class="toc-sub">8.1. Ứng dụng Trí tuệ Nhân tạo có thể giải thích (Explainable AI - XAI)</td><td style="text-align: right;">30</td></tr>
        <tr><td class="toc-sub">8.2. Mở rộng kiến trúc thuật toán chuyên biệt cho dữ liệu bảng</td><td style="text-align: right;">31</td></tr>
        <tr><td class="toc-sub">8.3. Thiết kế hệ thống MLOps và Tự động hóa tiếp thị đa kênh</td><td style="text-align: right;">31</td></tr>
        <tr><td><strong>TÀI LIỆU THAM KHẢO (REFERENCES)</strong></td><td style="text-align: right;">32</td></tr>
    </table>
</div>

<div class="page-break"></div>

<!-- CHƯƠNG 1: PHÁT BIỂU BÀI TOÁN & CƠ SỞ LÝ THUYẾT -->
<div class="academic-section">
    <h1 class="chapter-title">CHƯƠNG 1: PHÁT BIỂU BÀI TOÁN & CƠ SỞ LÝ THUYẾT</h1>
    
    <h2 class="sub-title">1.1. Bối cảnh ngành kinh doanh Bán lẻ và Thương mại điện tử (E-Commerce)</h2>
    <p>
        Trong thập kỷ qua, sự bùng nổ của công nghệ thông tin và mạng Internet đã thúc đẩy sự chuyển dịch mạnh mẽ từ mô hình bán lẻ truyền thống (Brick-and-Mortar) sang thương mại điện tử (E-Commerce) và bán lẻ đa kênh (Omnichannel Retail). Người tiêu dùng hiện đại đứng trước vô số lựa chọn với rào cản chuyển đổi (Switching Costs) giữa các nhà cung cấp gần như bằng không. Chỉ bằng một cú nhấp chuột hoặc một thao tác lướt trên điện thoại thông minh, khách hàng hoàn toàn có thể tìm thấy một sản phẩm thay thế tương đương từ đối thủ cạnh tranh với mức giá hấp dẫn hơn hoặc chính sách giao hàng nhanh hơn.
    </p>
    <p>
        Hệ quả tất yếu của môi trường cạnh tranh khốc liệt này là <strong>Chi phí thu hút khách hàng mới (Customer Acquisition Cost - CAC)</strong> trên các kênh truyền thông số (như Google Ads, Facebook Ads, TikTok Ads) liên tục tăng phi mã từ 40% đến 60% mỗi năm. Các doanh nghiệp nhận ra rằng chiến lược "đốt tiền" chạy quảng cáo để tìm kiếm khách hàng mới một lần rồi bỏ mặc họ là một mô hình kinh doanh thiếu bền vững. Lợi nhuận tích lũy thực sự của doanh nghiệp chỉ có thể đạt được khi khách hàng thực hiện các giao dịch lặp lại (Repeat Purchases), gia tăng tần suất mua sắm và duy trì mối quan hệ lâu dài với thương hiệu.
    </p>

    <h2 class="sub-title">1.2. Lý thuyết Vòng đời Khách hàng (Customer Lifecycle) và Giá trị Trọn đời (CLV)</h2>
    <p>
        Theo lý thuyết quản trị quan hệ khách hàng hiện đại, vòng đời của một khách hàng (Customer Lifecycle) trải qua 5 giai đoạn cốt lõi: <em>Nhận biết (Awareness) &rarr; Tiếp cận & Mua lần đầu (Acquisition) &rarr; Phát triển gắn kết (Onboarding & Nurturing) &rarr; Duy trì lòng trung thành (Retention) &rarr; Suy thoái và Rời bỏ (Attrition / Churn)</em>.
    </p>
    <p>
        Trọng tâm kinh tế của vòng đời này được định lượng qua chỉ số <strong>Giá trị trọn đời của khách hàng (Customer Lifetime Value - CLV hoặc LTV)</strong>. Về mặt giải tích tài chính, LTV của một khách hàng trong khoảng thời gian $T$ với tỷ lệ chiết khấu $d$ được biểu diễn qua công thức tổng quát:
    </p>
    <div class="formula-box">
        CLV = &sum;_{t=0}^{T} [ (p_t - c_t) &times; r_t ] / (1 + d)^t
    </div>
    <p>
        Trong đó:
    </p>
    <ul>
        <li>$p_t$: Tổng doanh thu kỳ vọng thu được từ khách hàng tại chu kỳ thời gian $t$.</li>
        <li>$c_t$: Chi phí trực tiếp phục vụ và chăm sóc khách hàng tại chu kỳ $t$.</li>
        <li>$r_t$: Xác suất khách hàng tiếp tục duy trì tương tác và quay lại mua hàng tại chu kỳ $t$ (Retention Rate).</li>
        <li>$d$: Tỷ lệ chiết khấu tiền tệ theo thời gian.</li>
    </ul>
    <p>
        Công thức trên chứng minh rõ nét: <strong>Xác suất khách hàng quay lại ($r_t$) là biến số nhân tử quyết định trực tiếp độ lớn của CLV</strong>. Nếu $r_t \to 0$ (khách hàng rời bỏ sớm), toàn bộ dòng tiền kỳ vọng trong tương lai sẽ bị triệt tiêu, khiến tổng doanh thu không đủ bù đắp chi phí CAC ban đầu. Ngược lại, nghiên cứu kinh điển của <em>Frederick Reichheld</em> tại <em>Bain & Company</em> đã chỉ ra rằng: việc nâng cao tỷ lệ giữ chân khách hàng thêm <strong>5%</strong> có thể làm tăng lợi nhuận doanh nghiệp từ <strong>25% đến 95%</strong>, bởi vì chi phí vận hành cho khách hàng trung thành thấp hơn rất nhiều và họ sẵn sàng chi tiêu cho những đơn hàng có giá trị cao hơn.
    </p>

    <h2 class="sub-title">1.3. Bản chất toán học của bài toán Phân loại Khách hàng Quay lại</h2>
    <p>
        Để giải quyết bài toán dự đoán hành vi của người tiêu dùng, chúng tôi mô hình hóa bài toán dưới góc nhìn <strong>Học máy có giám sát (Supervised Machine Learning)</strong> theo bài toán <strong>Phân loại nhị phân (Binary Classification)</strong>.
    </p>
    <p>
        Giả sử không gian mẫu $\mathcal{X} \subseteq \mathbb{R}^d$ biểu diễn vector đặc trưng đa chiều của khách hàng, bao gồm lịch sử giao dịch RFM, đặc điểm nhân khẩu học và các thông tin phản hồi trải nghiệm dịch vụ:
    </p>
    <div class="formula-box">
        &mathbf;x}_i = [ x_{i1}, x_{i2}, \dots, x_{id} ]^T &isin; &Xscr;
    </div>
    <p>
        Không gian nhãn $\mathcal{Y} = \{0, 1\}$ thể hiện trạng thái phát sinh đơn hàng của khách hàng trong khoảng thời gian quan sát tiếp theo:
    </p>
    <ul>
        <li>$y_i = 1$: Khách hàng <strong>sẽ quay lại mua sắm</strong> (Repurchase / Retained).</li>
        <li>$y_i = 0$: Khách hàng <strong>không quay lại / rời bỏ dịch vụ</strong> (Churn / At-Risk).</li>
    </ul>
    <p>
        Mục tiêu của thuật toán học máy là tìm kiếm một hàm giả thuyết (Hypothesis function) $f: \mathcal{X} \to [0, 1]$ xấp xỉ phân phối xác suất hậu nghiệm thực tế:
    </p>
    <div class="formula-box">
        f(&mathbf;x}_i) = P(y_i = 1 \mid &mathbf;x}_i)
    </div>
    <p>
        Sau khi thu được xác suất $P(y_i = 1 \mid \mathbf{x}_i)$, hệ thống áp dụng một ngưỡng quyết định (Decision Threshold) $\theta \in (0, 1)$ (thông thường $\theta = 0.50$) để gán nhãn dự đoán nhị phân $\hat{y}_i$:
    </p>
    <div class="formula-box">
        y&#770;_i = 
        &lcub; 
        1 \quad \text{nếu } P(y_i = 1 \mid &mathbf;x}_i) &ge; &theta;,
        <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        0 \quad \text{nếu } P(y_i = 1 \mid &mathbf;x}_i) < &theta;
        &rcub;
    </div>

    <h2 class="sub-title">1.4. Ý nghĩa thực tiễn và Sứ mệnh của giải pháp Boomerang Radar AI</h2>
    <p>
        Trong thực tế vận hành doanh nghiệp, việc dự đoán chính xác xác suất khách hàng quay lại đem lại những giá trị chiến lược mang tính đột phá:
    </p>
    <ol>
        <li>
            <strong>Chuyển dịch từ CSKH thụ động sang phòng ngừa chủ động (Proactive Retention):</strong><br>
            Hầu hết các hệ thống CRM hiện tại chỉ ghi nhận một khách hàng đã rời bỏ khi họ đã bất hoạt 90 hay 180 ngày. Khi đó, sự quan tâm của khách hàng đã chuyển sang thương hiệu khác. <em>Boomerang Radar AI</em> hoạt động như một hệ thống cảnh báo sớm, phát hiện những dấu hiệu rạn nứt đầu tiên (tần suất giảm, ngày chưa mua dài hơn nhịp độ bình thường, điểm hài lòng thấp) để doanh nghiệp can thiệp ngay từ trong "thời điểm vàng".
        </li>
        <li>
            <strong>Tối ưu hóa ngân sách Marketing và Khuyến mãi (Voucher Allocation Optimization):</strong><br>
            Thay vì phát mã giảm giá đại trà gây lãng phí ngân sách (Discount Cannibalization) và làm giảm giá trị thương hiệu, hệ thống giúp phân loại chính xác:
            <ul>
                <li><em>Khách hàng trung thành tự nhiên ($P > 85\%$):</em> Không cần phát voucher giảm sâu, chỉ cần tặng ưu đãi tích lũy điểm VIP hoặc giới thiệu sản phẩm mới.</li>
                <li><em>Khách hàng đứng trước nguy cơ rời bỏ ($20\% \le P \le 50\%$):</em> Cần gửi ngay voucher trợ giá hoặc miễn phí vận chuyển để tái kích hoạt hành vi.</li>
                <li><em>Khách hàng Churn hoàn toàn ($P < 15\%$):</em> Kích hoạt kịch bản gọi điện chăm sóc cá nhân hóa từ trung tâm CSKH.</li>
            </ul>
        </li>
        <li>
            <strong>Hiện thực hóa "Hiệu ứng Boomerang":</strong><br>
            Giống như nguyên lý khí động học của chiếc boomerang luôn quay trở lại điểm xuất phát sau khi phóng đi, hệ thống Boomerang Radar AI hướng đến việc thiết lập một chu trình tuần hoàn kín trong việc nuôi dưỡng trải nghiệm, biến mỗi giao dịch đơn lẻ thành điểm khởi đầu cho chuỗi giá trị giao dịch bền vững trong tương lai.
        </li>
    </ol>
</div>
