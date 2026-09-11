# 🛒 Dự Án Dự Đoán Khách Hàng Quay Lại Mua Sắm (Customer Repurchase Prediction AI System)

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Machine Learning](https://img.shields.io/badge/ML-Scikit--Learn-orange)
![Web App](https://img.shields.io/badge/Framework-Flask%20%7C%20HTML5-green)
![Dataset](https://img.shields.io/badge/Data-Kaggle%20Real%20Data-purple)

Hệ thống **Customer Repurchase Prediction AI System** được xây dựng chuẩn mực theo quy trình Học máy có giám sát (Supervised ML - Binary Classification), giải quyết bài toán dự đoán xác suất khách hàng phát sinh đơn hàng tiếp theo trong 30 ngày tới (`will_return` = 1 hoặc 0).

---

## 📌 1. Bảng Chỉ Số Đánh Giá Mô Hình Thực Tế (Test Set: 1,126 Khách Hàng)

Tất cả chỉ số thu được sau khi huấn luyện trên bộ dữ liệu thực tế Kaggle (5,630 bản ghi):

| Thuật Toán (Algorithm) | Accuracy (%) | Precision | Recall | F1-Score | ROC-AUC | Ghi chú kỹ thuật |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Logistic Regression** | 66.61% | **0.9294** | 0.6474 | 0.7632 | 0.7824 | `C=10.0`, `solver='lbfgs'` |
| **Decision Tree** | 85.17% | 0.9166 | 0.9038 | 0.9102 | 0.7493 | `criterion='entropy'` |
| **Random Forest (Mô hình chính)** | **88.45%** | 0.9014 | **0.9669** | **0.9330** | **0.9283** | `n_estimators=200`, `max_features='sqrt'` |

---

## 📂 2. Cấu Trúc Thư Mục Dự Án

```
DMC_/
├── data/
│   └── raw/
│       └── E Commerce Dataset.xlsx     # Dữ liệu thực tế Kaggle (5,630 bản ghi)
├── models/
│   ├── preprocessor.joblib             # Scaler & Encoder đã fit
│   ├── random_forest_model.joblib      # Mô hình Random Forest đã train
│   ├── decision_tree_model.joblib      # Mô hình Decision Tree đã train
│   ├── logistic_regression_model.joblib# Mô hình Logistic Regression đã train
│   └── evaluation_results.json         # Kết quả đo đạc chỉ số thực tế
├── src/
│   ├── __init__.py
│   ├── data_processing.py              # Xử lý dữ liệu Kaggle thực tế chuẩn ML chống Leakage
│   ├── train.py                        # Huấn luyện 3 mô hình + GridSearchCV 5-Fold
│   └── predict.py                      # Pipeline suy luận & custom decision threshold
├── app.py                              # Flask REST API & Web Dashboard Server
├── templates/
│   └── index.html                      # Giao diện Web Dashboard hiện đại
├── kaggle_notebook.ipynb               # File Notebook hoàn chỉnh sẵn sàng tải lên Kaggle
└── README.md                           # Tài liệu hướng dẫn dự án
```

---

## 🚀 3. Hướng Dẫn Chạy Dự Án Cục Bộ (Local Environment)

### Bước 1: Cài đặt thư viện phụ thuộc
```bash
pip install pandas numpy scikit-learn matplotlib seaborn flask joblib openpyxl
```

### Bước 2: Huấn luyện mô hình từ đầu
```bash
python -m src.train
```

### Bước 3: Khởi chạy Giao diện Web Dashboard
```bash
python app.py
```
*Truy cập trình duyệt tại:* `http://localhost:5000`

---

## ☁️ 4. Hướng Dẫn Đăng Lên Kaggle (Kaggle Notebook Upload)

1. Đăng nhập tài khoản Kaggle của bạn tại `https://www.kaggle.com`.
2. Tạo một Notebook mới: Chọn **Create -> New Notebook**.
3. Thêm bộ dữ liệu Kaggle vào Notebook:
   - Nhấn **+ Add Data** ở góc phải màn hình.
   - Tìm kiếm bộ dữ liệu: `Ecommerce Customer Churn Analysis and Prediction` (tác giả: `ankitverma2010`).
   - Nhấn **Add**.
4. Upload Notebook code:
   - Vào menu **File -> Import Notebook**.
   - Chọn file `kaggle_notebook.ipynb` từ máy tính của bạn.
5. Nhấn **Run All** để thực thi toàn bộ pipeline huấn luyện và tạo báo cáo trên Kaggle!
