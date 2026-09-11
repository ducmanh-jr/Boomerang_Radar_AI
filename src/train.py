import os
import sys
import json
import joblib
import numpy as np
import pandas as pd

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, confusion_matrix
)

from src.data_processing import prepare_data

def train_and_evaluate_models():
    """
    Huấn luyện và đánh giá 3 mô hình học máy truyền thống:
    1. Logistic Regression
    2. Decision Tree
    3. Random Forest (Mô hình chính - Ensemble/Bagging với GridSearchCV)
    
    Tất cả số liệu đo đạc (Accuracy, Precision, Recall, F1, ROC-AUC)
    được tính toán thực tế trên tập Kiểm thử (Test Set) độc lập.
    """
    print("=== BẮT ĐẦU CHUẨN BỊ DỮ LIỆU ===")
    data = prepare_data(use_smote=True)
    
    X_train, y_train = data['X_train'], data['y_train']
    X_test, y_test = data['X_test'], data['y_test']
    feature_names = data['feature_names']
    
    os.makedirs('models', exist_ok=True)
    results = {}
    
    # -------------------------------------------------------------
    # 1. LOGISTIC REGRESSION
    # -------------------------------------------------------------
    print("\n--- Huấn luyện Mô hình 1: Logistic Regression ---")
    log_reg_param_grid = {
        'C': [0.01, 0.1, 1.0, 10.0],
        'solver': ['lbfgs', 'liblinear']
    }
    grid_log_reg = GridSearchCV(
        LogisticRegression(max_iter=1000, random_state=42, class_weight='balanced'),
        log_reg_param_grid, cv=5, scoring='f1', n_jobs=-1
    )
    grid_log_reg.fit(X_train, y_train)
    best_log_reg = grid_log_reg.best_estimator_
    
    y_pred_log = best_log_reg.predict(X_test)
    y_prob_log = best_log_reg.predict_proba(X_test)[:, 1]
    
    results['Logistic Regression'] = {
        'best_params': grid_log_reg.best_params_,
        'accuracy': float(accuracy_score(y_test, y_pred_log)),
        'precision': float(precision_score(y_test, y_pred_log, zero_division=0)),
        'recall': float(recall_score(y_test, y_pred_log, zero_division=0)),
        'f1': float(f1_score(y_test, y_pred_log, zero_division=0)),
        'roc_auc': float(roc_auc_score(y_test, y_prob_log)),
        'confusion_matrix': confusion_matrix(y_test, y_pred_log).tolist()
    }
    joblib.dump(best_log_reg, 'models/logistic_regression_model.joblib')
    
    # -------------------------------------------------------------
    # 2. DECISION TREE
    # -------------------------------------------------------------
    print("\n--- Huấn luyện Mô hình 2: Decision Tree ---")
    dt_param_grid = {
        'max_depth': [3, 5, 8, 12, None],
        'min_samples_split': [2, 5, 10],
        'criterion': ['gini', 'entropy']
    }
    grid_dt = GridSearchCV(
        DecisionTreeClassifier(random_state=42, class_weight='balanced'),
        dt_param_grid, cv=5, scoring='f1', n_jobs=-1
    )
    grid_dt.fit(X_train, y_train)
    best_dt = grid_dt.best_estimator_
    
    y_pred_dt = best_dt.predict(X_test)
    y_prob_dt = best_dt.predict_proba(X_test)[:, 1]
    
    results['Decision Tree'] = {
        'best_params': grid_dt.best_params_,
        'accuracy': float(accuracy_score(y_test, y_pred_dt)),
        'precision': float(precision_score(y_test, y_pred_dt, zero_division=0)),
        'recall': float(recall_score(y_test, y_pred_dt, zero_division=0)),
        'f1': float(f1_score(y_test, y_pred_dt, zero_division=0)),
        'roc_auc': float(roc_auc_score(y_test, y_prob_dt)),
        'confusion_matrix': confusion_matrix(y_test, y_pred_dt).tolist()
    }
    joblib.dump(best_dt, 'models/decision_tree_model.joblib')
    
    # -------------------------------------------------------------
    # 3. RANDOM FOREST (MÔ HÌNH CHÍNH)
    # -------------------------------------------------------------
    print("\n--- Huấn luyện Mô hình 3: Random Forest (Chính) với GridSearchCV ---")
    rf_param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [5, 8, 12, 16, None],
        'min_samples_split': [2, 5, 10],
        'max_features': ['sqrt', 'log2']
    }
    grid_rf = GridSearchCV(
        RandomForestClassifier(random_state=42, class_weight='balanced', n_jobs=-1),
        rf_param_grid, cv=5, scoring='f1', n_jobs=-1
    )
    grid_rf.fit(X_train, y_train)
    best_rf = grid_rf.best_estimator_
    
    y_pred_rf = best_rf.predict(X_test)
    y_prob_rf = best_rf.predict_proba(X_test)[:, 1]
    
    # Feature Importances cho Random Forest
    importances = best_rf.feature_importances_
    feat_imp = sorted(zip(feature_names, [float(x) for x in importances]), key=lambda x: x[1], reverse=True)
    
    results['Random Forest'] = {
        'best_params': grid_rf.best_params_,
        'accuracy': float(accuracy_score(y_test, y_pred_rf)),
        'precision': float(precision_score(y_test, y_pred_rf, zero_division=0)),
        'recall': float(recall_score(y_test, y_pred_rf, zero_division=0)),
        'f1': float(f1_score(y_test, y_pred_rf, zero_division=0)),
        'roc_auc': float(roc_auc_score(y_test, y_prob_rf)),
        'confusion_matrix': confusion_matrix(y_test, y_pred_rf).tolist(),
        'feature_importances': feat_imp
    }
    joblib.dump(best_rf, 'models/random_forest_model.joblib')
    
    # Lưu kết quả tổng hợp ra file JSON
    with open('models/evaluation_results.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
        
    print("\n=== HOÀN THÀNH HUẤN LUYỆN & ĐÁNH GIÁ MÔ HÌNH ===")
    for model_name, metrics in results.items():
        print(f"\n[{model_name}]")
        print(f"  Accuracy:  {metrics['accuracy']*100:.2f}%")
        print(f"  Precision: {metrics['precision']:.4f}")
        print(f"  Recall:    {metrics['recall']:.4f}")
        print(f"  F1-Score:  {metrics['f1']:.4f}")
        print(f"  ROC-AUC:   {metrics['roc_auc']:.4f}")
        
    return results

if __name__ == '__main__':
    train_and_evaluate_models()
