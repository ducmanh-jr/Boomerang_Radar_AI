import os
import sys
import pandas as pd
import numpy as np

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def process_real_kaggle_dataset(raw_excel_path='data/raw/E Commerce Dataset.xlsx', output_path='data/customer_repurchase_data.csv'):
    """
    Tải và xử lý Bộ Dữ Liệu Thực Tế Kaggle (Ecommerce Customer Churn Analysis and Prediction):
    - Đọc file Excel từ Kaggle (5,630 bản ghi)
    - Xử lý giá trị khuyết (Missing value imputation)
    - Ánh xạ & Chuyển đổi các cột Kaggle sang đúng 8 thuộc tính RFM+ của đề tài:
        1. age: Mẫu tính từ Tenure + baseline 22 tuổi
        2. gender: Male/Female -> Nam/Nữ
        3. total_purchases: OrderCount
        4. avg_order_value: Tính từ CashbackAmount & OrderCount (chuyển đổi sang VNĐ)
        5. days_since_last_purchase: DaySinceLastOrder
        6. membership_level: Phân hạng Đồng/Bạc/Vàng/Kim Cương dựa trên CashbackAmount
        7. used_voucher: CouponUsed (> 0 -> 1, ngược lại 0)
        8. satisfaction_score: SatisfactionScore (1-5)
        Nhãn target y: will_return = 1 - Churn (1: Quay lại, 0: Churn)
    """
    if not os.path.exists(raw_excel_path):
        raise FileNotFoundError(f"Chưa tìm thấy file Kaggle tại {raw_excel_path}")

    print(f"--- BẮT ĐẦU ĐỌC VÀ XỬ LÝ BỘ DỮ LIỆU THỰC TẾ KAGGLE ---")
    df_raw = pd.read_excel(raw_excel_path, sheet_name='E Comm')
    print(f"Tổng số bản ghi dữ liệu thực tế: {len(df_raw):,} dòng x {len(df_raw.columns)} cột")

    # Xử lý giá trị khuyết (Imputation)
    df = df_raw.copy()
    num_cols = ['Tenure', 'OrderCount', 'DaySinceLastOrder', 'CouponUsed', 'OrderAmountHikeFromlastYear', 'CashbackAmount', 'SatisfactionScore']
    for c in num_cols:
        if c in df.columns:
            df[c] = df[c].fillna(df[c].median())

    # 1. Target Label (will_return = 1 - Churn)
    # Churn = 1 (Rời bỏ) -> will_return = 0; Churn = 0 (Quay lại) -> will_return = 1
    df['will_return'] = (df['Churn'] == 0).astype(int)

    # 2. Gender (Male/Female -> Nam/Nữ)
    df['gender'] = df['Gender'].replace({'Male': 'Nam', 'Female': 'Nữ'}).fillna('Nữ')

    # 3. Age (Ước tính từ Tenure + 22)
    df['age'] = np.clip((22 + df['Tenure'] * 0.8 + np.random.normal(0, 2, size=len(df))).astype(int), 18, 70)

    # 4. Total Purchases (OrderCount)
    df['total_purchases'] = np.clip(df['OrderCount'].astype(int), 1, 60)

    # 5. Avg Order Value (VNĐ - chuyển đổi từ Cashback/Ratio)
    df['avg_order_value'] = np.round(np.clip(df['CashbackAmount'] * 3200 + df['OrderAmountHikeFromlastYear'] * 15000, 150000, 4500000), -3)

    # 6. Days Since Last Purchase (DaySinceLastOrder)
    df['days_since_last_purchase'] = np.clip(df['DaySinceLastOrder'].astype(int), 1, 180)

    # 7. Membership Level (Phân loại theo CashbackAmount)
    cashback_q = df['CashbackAmount'].quantile([0.35, 0.70, 0.90])
    def map_membership(cb):
        if cb <= cashback_q[0.35]:
            return 'Đồng'
        elif cb <= cashback_q[0.70]:
            return 'Bạc'
        elif cb <= cashback_q[0.90]:
            return 'Vàng'
        else:
            return 'Kim Cương'
            
    df['membership_level'] = df['CashbackAmount'].apply(map_membership)

    # 8. Used Voucher (CouponUsed > 0 -> 1, 0 -> 0)
    df['used_voucher'] = (df['CouponUsed'] > 0).astype(int)

    # 9. Satisfaction Score (1-5)
    df['satisfaction_score'] = np.clip(df['SatisfactionScore'].astype(int), 1, 5)

    # Lọc đúng 8 thuộc tính + 1 nhãn
    final_cols = [
        'age', 'gender', 'total_purchases', 'avg_order_value',
        'days_since_last_purchase', 'membership_level', 'used_voucher',
        'satisfaction_score', 'will_return'
    ]
    df_final = df[final_cols].copy()

    # Lưu file CSV
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df_final.to_csv(output_path, index=False, encoding='utf-8')

    print(f"\n✅ Đã tiền xử lý và ánh xạ thành công bộ dữ liệu thực tế!")
    print(f"Lưu file tại: {output_path}")
    print("Phân bố nhãn thực tế (`will_return`):")
    print(df_final['will_return'].value_counts(normalize=True))
    print(df_final.head(5))

    return df_final

if __name__ == '__main__':
    process_real_kaggle_dataset()
