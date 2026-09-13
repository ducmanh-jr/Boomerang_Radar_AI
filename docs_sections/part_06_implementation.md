<!-- CHƯƠNG 6: CÀI ĐẶT HỆ THỐNG VÀ XÂY DỰNG ỨNG DỤNG -->

<div class="academic-section">
    <h1 class="chapter-title">CHƯƠNG 6: CÀI ĐẶT HỆ THỐNG VÀ XÂY DỰNG ỨNG DỤNG</h1>
    
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
