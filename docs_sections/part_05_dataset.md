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
