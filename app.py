import os
import sys
import json
import pandas as pd
import numpy as np
from flask import Flask, render_template, jsonify, request

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

app = Flask(__name__, template_folder='templates')

from src.predict import predict_single_customer, predict_batch_df

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/stats', methods=['GET'])
def get_stats():
    data_path = 'data/customer_repurchase_data.csv'
    if not os.path.exists(data_path):
        from src.data_processing import load_and_clean_kaggle_data
        df = load_and_clean_kaggle_data()
    else:
        df = pd.read_csv(data_path)
        
    total_cust = len(df)
    returns = int(df['will_return'].sum())
    churns = total_cust - returns
    return_rate = round((returns / total_cust) * 100, 1)
    churn_rate = round(100 - return_rate, 1)
    avg_aov = int(df['avg_order_value'].mean())
    
    preview = df.head(15).to_dict(orient='records')
    
    return jsonify({
        'total_customers': total_cust,
        'return_rate': return_rate,
        'churn_rate': churn_rate,
        'avg_aov': avg_aov,
        'preview': preview
    })

@app.route('/api/models', methods=['GET'])
def get_models_eval():
    eval_path = 'models/evaluation_results.json'
    if not os.path.exists(eval_path):
        from src.train import train_and_evaluate_models
        train_and_evaluate_models()
        
    with open(eval_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/api/predict', methods=['POST'])
def handle_predict_single():
    req_data = request.get_json()
    threshold = float(req_data.get('threshold', 0.50))
    model_name = req_data.get('model_name', 'Random Forest')
    
    cust_dict = {
        'age': int(req_data.get('age', 32)),
        'gender': req_data.get('gender', 'Nữ'),
        'total_purchases': int(req_data.get('total_purchases', 5)),
        'avg_order_value': float(req_data.get('avg_order_value', 500000)),
        'days_since_last_purchase': int(req_data.get('days_since_last_purchase', 15)),
        'membership_level': req_data.get('membership_level', 'Bạc'),
        'used_voucher': int(req_data.get('used_voucher', 1)),
        'satisfaction_score': int(req_data.get('satisfaction_score', 4))
    }
    
    res = predict_single_customer(cust_dict, threshold=threshold, model_name=model_name)
    return jsonify(res)

@app.route('/api/predict-batch', methods=['POST'])
def handle_predict_batch():
    try:
        # Nếu có file CSV tải lên
        if 'file' in request.files and request.files['file'].filename != '':
            file = request.files['file']
            df = pd.read_csv(file)
        else:
            data_path = 'data/customer_repurchase_data.csv'
            if not os.path.exists(data_path):
                from src.data_processing import load_and_clean_kaggle_data
                df = load_and_clean_kaggle_data().head(30)
            else:
                df = pd.read_csv(data_path).head(30)
                
        df_res = predict_batch_df(df, threshold=0.50, model_name='Random Forest')
        df_res = df_res.fillna('')
        return jsonify(df_res.to_dict(orient='records'))
    except Exception as e:
        print(f"Lỗi predict-batch: {e}")
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    print("=== KHỞI CHẠY DMC CUSTOMER REPURCHASE PREDICTION WEB APP ===")
    print("Truy cập Web Dashboard tại: http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=False)
