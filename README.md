# 🪃 Boomerang Radar AI (Customer Repurchase & Churn Prediction System)

> **Hệ thống Trí tuệ Nhân tạo phát hiện sớm nguy cơ rời bỏ và dự đoán khả năng khách hàng quay lại mua sắm dựa trên 8 chỉ số RFM+ và mô hình Gradient Boosting (Accuracy 94.23%, F1 96.56%).**

---

## 🌟 Giới thiệu dự án
**Boomerang Radar AI** hoạt động như một "trạm radar thông minh" dành cho các doanh nghiệp bán lẻ và thương mại điện tử:
* **Quét và định vị:** Liên tục phân tích hành vi của khách hàng thông qua tần suất, giá trị đơn hàng, độ tươi mới giao dịch và trải nghiệm dịch vụ.
* **Cảnh báo sớm:** Phân cấp rủi ro rời bỏ thành 4 cấp độ (*Rất thấp*, *Trung bình*, *Cao*, *Rất cao*).
* **Đề xuất hành động tự động:** Đưa ra các gợi ý marketing/CSKH tức thì để kích hoạt khách hàng quay lại ("hiệu ứng Boomerang").

---

## 📄 Báo cáo dự án chuyên sâu (Luận văn cấp cao)
* 📘 **Bản báo cáo hoàn chỉnh định dạng Word (DOCX):** [BAO_CAO_BOOMERANG_RADAR_AI.docx](BAO_CAO_BOOMERANG_RADAR_AI.docx) *(Bỏ trống bìa, công thức sạch, mục lục đầy đủ, không lỗi hiển thị)*
* 📕 **Báo cáo toàn diện PDF:** [BAO_CAO_TOAN_DIEN_BOOMERANG_RADAR_AI_30_TRANG.pdf](BAO_CAO_TOAN_DIEN_BOOMERANG_RADAR_AI_30_TRANG.pdf)
* 📝 **Bản Markdown toàn diện:** [BAO_CAO_TOAN_DIEN_30_TRANG_BOOMERANG_RADAR_AI.md](BAO_CAO_TOAN_DIEN_30_TRANG_BOOMERANG_RADAR_AI.md)
* 📂 **Thư mục các chương chi tiết:** [docs_sections/](docs_sections/)
* ⚙️ **Kịch bản tự động xuất file DOCX:** [build_word_doc.py](build_word_doc.py)

---

## 📊 Kết quả kiểm thử thực nghiệm

| Mô hình | Accuracy | Precision | Recall | F1-Score | ROC-AUC | Xếp hạng |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Logistic Regression** | 68.47% | 0.9395 | 0.6635 | 0.7777 | 0.7906 | Baseline |
| **Decision Tree** | 74.96% | 0.9348 | 0.7511 | 0.8329 | 0.8089 | Khá |
| **Random Forest** | 91.56% | 0.9367 | 0.9637 | 0.9500 | 0.9575 | Tốt |
| **Gradient Boosting** | **94.23%** | **0.9570** | **0.9744** | **0.9656** | **0.9695** | **★ Champion** |

---

## 🚀 Cài đặt và Chạy ứng dụng

### 1. Cài đặt môi trường
```powershell
# Kích hoạt môi trường ảo (nếu có)
python -m venv venv
.\venv\Scripts\Activate.ps1

# Cài đặt các thư viện cần thiết
pip install -r requirements.txt
```

### 2. Huấn luyện mô hình (Tùy chọn nếu muốn huấn luyện lại)
```powershell
python src/train.py
```

### 3. Khởi chạy Web Dashboard
```powershell
python app.py
```
Mở trình duyệt và truy cập: **`http://localhost:5000`**

---

## 📁 Cấu trúc thư mục
* `app.py`: Web server Flask và REST API endpoints.
* `src/data_processing.py`: Module nạp dữ liệu, chống Data Leakage và sinh 4 đặc trưng tương tác.
* `src/train.py`: Pipeline huấn luyện và tối ưu siêu tham số.
* `src/predict.py`: Bộ máy suy luận và phân tích tự nhiên.
* `templates/index.html`: Giao diện Dashboard 4 tab (Overview, Predictor, Benchmark, Batch).
* `BAO_CAO_DU_AN_BOOMERANG_RADAR_AI.pdf`: File báo cáo PDF 12 trang hoàn chỉnh.
* `BAO_CAO_DU_AN_BOOMERANG_RADAR_AI.md`: Báo cáo chi tiết kỹ thuật 8 phần theo đúng đề cương.
