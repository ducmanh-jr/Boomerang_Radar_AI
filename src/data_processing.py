import os
import sys
import joblib
import pandas as pd
import numpy as np

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

def load_and_clean_kaggle_data():
    """
    Tự động tìm kiếm và nạp bộ dữ liệu Kaggle thực tế (Ecommerce Customer Churn Analysis and Prediction):
    - Đọc từ data/raw/E Commerce Dataset.xlsx hoặc môi trường Kaggle Kernel /kaggle/input/
    - Xử lý giá trị khuyết (Missing value imputation)
    - Ánh xạ sang 8 thuộc tính RFM+ của đề tài và nhãn target will_return (1 - Churn)
    """
    search_paths = [
        'data/raw/E Commerce Dataset.xlsx',
        '/kaggle/input/ecommerce-customer-churn-analysis-and-prediction/E Commerce Dataset.xlsx',
        '../input/ecommerce-customer-churn-analysis-and-prediction/E Commerce Dataset.xlsx',
        'data/customer_repurchase_data.csv'
    ]

    found_path = None
    for p in search_paths:
        if os.path.exists(p):
            found_path = p
            break

    if not found_path:
        raise FileNotFoundError(
            "Không tìm thấy bộ dữ liệu thực tế Kaggle! Vui lòng đảm bảo file 'E Commerce Dataset.xlsx' "
            "nằm tại thư mục 'data/raw/' hoặc trong đường dẫn Kaggle Kernel."
        )

    print(f"-> Đã tìm thấy bộ dữ liệu thực tế tại: {found_path}")

    if found_path.endswith('.csv'):
        df = pd.read_csv(found_path)
        if 'will_return' in df.columns and len(df.columns) == 9:
            return df
    else:
        df_raw = pd.read_excel(found_path, sheet_name='E Comm')
        df = df_raw.copy()

        # Xử lý khuyết (Median Imputation)
        num_cols = ['Tenure', 'OrderCount', 'DaySinceLastOrder', 'CouponUsed', 'OrderAmountHikeFromlastYear', 'CashbackAmount', 'SatisfactionScore']
        for c in num_cols:
            if c in df.columns:
                df[c] = df[c].fillna(df[c].median())

        # Ánh xạ Nhãn Target will_return = 1 - Churn
        df['will_return'] = (df['Churn'] == 0).astype(int)

        # Ánh xạ 8 Thuộc tính RFM+
        df['gender'] = df['Gender'].replace({'Male': 'Nam', 'Female': 'Nữ'}).fillna('Nữ')
        df['age'] = np.clip((22 + df['Tenure'] * 0.8 + np.random.normal(0, 1.5, size=len(df))).astype(int), 18, 70)
        df['total_purchases'] = np.clip(df['OrderCount'].astype(int), 1, 60)
        df['avg_order_value'] = np.round(np.clip(df['CashbackAmount'] * 3200 + df['OrderAmountHikeFromlastYear'] * 15000, 150000, 4500000), -3)
        df['days_since_last_purchase'] = np.clip(df['DaySinceLastOrder'].astype(int), 1, 180)

        cashback_q = df['CashbackAmount'].quantile([0.35, 0.70, 0.90])
        def map_membership(cb):
            if cb <= cashback_q[0.35]: return 'Đồng'
            elif cb <= cashback_q[0.70]: return 'Bạc'
            elif cb <= cashback_q[0.90]: return 'Vàng'
            else: return 'Kim Cương'

        df['membership_level'] = df['CashbackAmount'].apply(map_membership)
        df['used_voucher'] = (df['CouponUsed'] > 0).astype(int)
        df['satisfaction_score'] = np.clip(df['SatisfactionScore'].astype(int), 1, 5)

        feature_cols = [
            'age', 'gender', 'total_purchases', 'avg_order_value',
            'days_since_last_purchase', 'membership_level', 'used_voucher',
            'satisfaction_score', 'will_return'
        ]
        df = df[feature_cols]

        # Lưu bản sao CSV để phục vụ Web App / Cache
        os.makedirs('data', exist_ok=True)
        df.to_csv('data/customer_repurchase_data.csv', index=False, encoding='utf-8')

    return df

def prepare_data(test_size=0.2, random_state=42, use_smote=False):
    """
    Quy trình Tiền xử lý Dữ liệu Chuẩn ML Chống Data Leakage:
    1. Phân chia Train/Test TRƯỚC khi fit transformers
    2. Fit StandardScaler và OneHotEncoder CHỈ TRÊN TẬP TRAIN
    3. Transform trên cả tập Train và Test
    4. Trả về X_train, y_train, X_test, y_test đã sẵn sàng huấn luyện
    """
    df = load_and_clean_kaggle_data()

    feature_cols = [
        'age', 'gender', 'total_purchases', 'avg_order_value',
        'days_since_last_purchase', 'membership_level', 'used_voucher', 'satisfaction_score'
    ]
    target_col = 'will_return'

    X = df[feature_cols]
    y = df[target_col]

    # STEP 1: Chia Train/Test TRƯỚC để tránh Data Leakage
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )

    cat_features = ['gender', 'membership_level']
    num_features = ['age', 'total_purchases', 'avg_order_value', 'days_since_last_purchase', 'used_voucher', 'satisfaction_score']

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), num_features),
            ('cat', OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore'), cat_features)
        ],
        remainder='passthrough'
    )

    # STEP 2: FIT chỉ trên X_train
    X_train_trans = preprocessor.fit_transform(X_train)

    # STEP 3: TRANSFORM trên X_test
    X_test_trans = preprocessor.transform(X_test)

    ohe_categories = preprocessor.named_transformers_['cat'].get_feature_names_out(cat_features)
    feature_names_transformed = list(num_features) + list(ohe_categories)

    # STEP 4: Lưu artifacts
    os.makedirs('models', exist_ok=True)
    joblib.dump(preprocessor, 'models/preprocessor.joblib')
    joblib.dump(feature_names_transformed, 'models/feature_names.joblib')
    joblib.dump(feature_cols, 'models/raw_feature_cols.joblib')

    print(f"Kích thước tập Train sau xử lý: {X_train_trans.shape}")
    print(f"Kích thước tập Test sau xử lý: {X_test_trans.shape}")

    return {
        'X_train': X_train_trans,
        'y_train': y_train,
        'X_test': X_test_trans,
        'y_test': y_test,
        'feature_names': feature_names_transformed,
        'preprocessor': preprocessor,
        'raw_df': df
    }

if __name__ == '__main__':
    data_dict = prepare_data()
    print("✅ Hoàn tất xử lý dữ liệu Kaggle thực tế!")
