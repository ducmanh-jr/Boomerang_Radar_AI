<!-- CHƯƠNG 7: ĐÁNH GIÁ KẾT QUẢ THỰC NGHIỆM -->

<div class="academic-section">
    <h1 class="chapter-title">CHƯƠNG 7: ĐÁNH GIÁ KẾT QUẢ THỰC NGHIỆM</h1>
    
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
