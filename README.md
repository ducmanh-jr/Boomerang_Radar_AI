# DMC Khả Năng Khách Hàng Quay Lại (Customer Repurchase Prediction)

## 400

Bao gồm toàn bộ source code, mô hình AI đã huấn luyện (Gradient Boosting 94.23%), web dashboard 4-tab hoàn chỉnh, và hướng dẫn triển khai.

---

## Overview

This repository implements a **Flask web application** that predicts whether a customer will return (repurchase) based on eight engineered RFM+ features. The core workflow consists of:

1. **Data ingestion & cleaning** – loads the Kaggle “E‑Commerce Customer Churn” dataset (or a cached CSV) and transforms it into the required feature set.
2. **Pre‑processing** – `StandardScaler` for numeric columns and `OneHotEncoder` for categorical columns, with strict train/test split to avoid data leakage.
3. **Model training** – Logistic Regression, Decision Tree, and Random Forest (the primary model) are trained with `GridSearchCV` and evaluated on a held‑out test set.
4. **Inference API** – Flask endpoints expose:
   - `/api/stats` – dataset statistics & preview
   - `/api/models` – model evaluation metrics
   - `/api/predict` – single‑customer prediction
   - `/api/predict-batch` – batch prediction (CSV upload or sample data)

The UI (`templates/index.html`) provides three tabs:

- **Predictor** – enter a single customer record and get a probability, risk level, and natural‑language synthesis.
- **Benchmark** – view model performance tables, confusion matrix, and feature‑importance chart.
- **Batch** – upload a CSV or run a sample batch prediction and export results.

A new **Overview** tab was added to quickly glance at dataset statistics and a preview of the first 15 rows.

## Project Structure

```
c:\Users\Admin\ducmanh\DMC_kha-nang-khach-hang-quay-lai
│
├─ app.py                     # Flask entry point
├─ requirements.txt           # Python dependencies
├─ .gitignore                 # Ignored files/folders
│
├─ data/
│   ├─ customer_repurchase_data.csv   # Cached cleaned dataset (generated on first run)
│   └─ raw/
│       └─ E Commerce Dataset.xlsx   # Original Kaggle Excel (not tracked)
│
├─ models/
│   ├─ decision_tree_model.joblib
│   ├─ logistic_regression_model.joblib
│   ├─ random_forest_model.joblib
│   ├─ preprocessor.joblib
│   ├─ feature_names.joblib
│   ├─ raw_feature_cols.joblib
│   └─ evaluation_results.json
│
├─ src/
│   ├─ __init__.py
│   ├─ data_processing.py    # Load, clean, split, and save preprocessing artifacts
│   ├─ train.py               # Model training & evaluation
│   └─ predict.py             # Inference utilities
│
└─ templates/
    └─ index.html            # Front‑end UI (Bootstrap‑styled)
```

## Setup & Usage

1. **Create a virtual environment (optional but recommended)**  

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1   # PowerShell
   ```

2. **Install dependencies**  

   ```powershell
   pip install -r requirements.txt
   ```

3. **Run the training script (creates model artifacts)**  

   ```powershell
   python src/train.py
   ```

   This will:
   - Load the raw Excel (or cached CSV) from `data/raw/`.
   - Save `data/customer_repurchase_data.csv`.
   - Store preprocessing objects and trained models under `models/`.
   - Generate `models/evaluation_results.json`.

4. **Start the Flask app**  

   ```powershell
   python app.py
   ```

   Open a browser and navigate to `http://localhost:5000`. The UI will load with the Overview, Predictor, Benchmark, and Batch tabs.

5. **Predict a single customer** – fill the form on the **Predictor** tab and click **Dự đoán**.

6. **Batch prediction** – on the **Batch** tab, either:
   - Click **Dự đoán mẫu** to run a built‑in sample (first 30 rows), or
   - Upload a CSV with the required columns (`age`, `gender`, `total_purchases`, `avg_order_value`, `days_since_last_purchase`, `membership_level`, `used_voucher`, `satisfaction_score`) and click **Dự đoán**.

   Export results to CSV via the **Export CSV** button.

## Development Notes

- **Data leakage protection** – the train/test split occurs **before** any scaler or encoder is fitted.
- **Model artifacts** are saved under `models/` and are loaded lazily by the API; if missing, the training script will be re‑run automatically. dẹp

This project is provided under the MIT License. Feel free to adapt, extend, or integrate it into your own solutions.
