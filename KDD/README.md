# KDD Project — Telco Customer Churn Prediction

This project follows the **KDD (Knowledge Discovery in Databases)** methodology using the *Telco Customer Churn* dataset from Kaggle.

It implements all KDD phases — from selection and preprocessing to data mining and interpretation — and uses AI-assisted critique prompts for iterative refinement.

---

## 📘 Project Overview
- **Goal:** Predict whether a customer will churn based on service usage and contract features.
- **Dataset:** [Telco Customer Churn (Kaggle)](https://www.kaggle.com/blastchar/telco-customer-churn)
- **Target Variable:** `Churn` (Yes/No → 1/0)
- **Type:** Binary Classification

---

## 🔁 KDD Process

### 1. Plan & Define
- Defined business goal: *Reduce churn rate by targeting high-risk customers.*
- KPIs: ROC-AUC ≥ 0.82, PR-AUC ≥ 0.60.

### 2. Data Understanding / Selection
- Cleaned and profiled 7,043 rows, 21 features.
- Identified and corrected inconsistent `TotalCharges` values.
- Selected relevant features, excluded IDs and post-churn indicators.

### 3. Data Preparation
- Mapped `Churn` to binary 1/0.
- Handled missing values, scaled numerics, one-hot encoded categoricals.
- Managed imbalance using `class_weight` and optional SMOTE.

### 4. Modeling
- Benchmarked **Logistic Regression** and **Random Forest**.
- Used `RandomizedSearchCV` for hyperparameter tuning.
- Evaluated with ROC-AUC, PR-AUC, and F1 metrics.

### 5. Evaluation / Interpretation
- Assessed feature importance (SHAP, permutation).
- Compared model performance with cost-based thresholds.
- Visualized ROC, PR, and calibration curves.

### 6. Deployment / Delivery
- Saved best calibrated model (`model.joblib`).
- Created `deploy_config.json` and `model_card.md`.
- Built optional Streamlit demo for batch predictions.

---

## 🧠 Key Insights
- Contract type, tenure, and payment method are top churn drivers.
- Calibration improved probability reliability.
- Cost-based thresholding achieved better business alignment.

---

## 📦 Repository Structure
KDD/
│
├── notebook.ipynb # Full code (KDD end-to-end)
├── critique_prompts.md # Expert review prompts
├── medium_draft.md # Medium article draft
├── data/ 
├── artifacts/ 
└── README.md
