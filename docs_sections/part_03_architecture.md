<!-- CHƯƠNG 3: THIẾT KẾ SƠ ĐỒ KHỐI VÀ KIẾN TRÚC HỆ THỐNG -->

<div class="academic-section">
    <h1 class="chapter-title">CHƯƠNG 3: THIẾT KẾ SƠ ĐỒ KHỐI VÀ KIẾN TRÚC HỆ THỐNG</h1>
    
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
