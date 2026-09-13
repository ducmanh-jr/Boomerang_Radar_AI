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
