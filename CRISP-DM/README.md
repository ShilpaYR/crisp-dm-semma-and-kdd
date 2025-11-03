# CRISP-DM Project — Retail Sales Forecasting (Walmart)

This project demonstrates the full **CRISP-DM** lifecycle using the *Walmart Sales Forecasting* dataset from Kaggle.  
It walks through every phase — from business understanding to deployment — with clear documentation and reproducible code.

---

## 📊 Project Overview
- **Goal:** Predict future weekly sales per store and department to help optimize inventory and staffing.
- **Dataset:** [Walmart Sales Forecasting (Kaggle)](https://www.kaggle.com/c/walmart-recruiting-store-sales-forecasting)
- **Target Variable:** `Weekly_Sales`
- **Type:** Regression (time series–like tabular data)

---

## 🔁 CRISP-DM Phases

### 1. Business Understanding
- Defined business goal: *Reduce forecast error by 15% vs. last year’s baseline.*
- Identified success metrics (RMSE, MAPE).
- Captured constraints (data lag, weekly cadence).

### 2. Data Understanding
- Loaded and explored 421,570 rows, 5 columns.
- Identified trends, outliers, and missing values.
- Visualized seasonal sales patterns and store-level variability.

### 3. Data Preparation
- Engineered features: lag and rolling averages per (Store, Dept).
- Encoded categorical variables and scaled numerics.
- Built reproducible preprocessing pipelines (using `ColumnTransformer`).

### 4. Modeling
- Benchmarked **Linear Regression** vs. **Random Forest**.
- Cross-validated RMSE and tuned hyperparameters with `GridSearchCV`.

### 5. Evaluation
- Compared validation/test RMSE, plotted residuals.
- Analyzed feature importances and error patterns.
- Documented model strengths, limitations, and possible improvements.

### 6. Deployment
- Saved best model (`model.joblib`) and preprocessing pipeline.
- Created example inference notebook for new data.
- Outlined options for lightweight Streamlit/Flask deployment.

---

## 🧠 Key Learnings
- CRISP-DM encourages structured thinking before modeling.
- Feature engineering had a larger impact than model complexity.
- Reproducible preprocessing ensures consistent inference results.

---

## 📦 Repository Structure
CRISP-DM/
│
├── notebook.ipynb # Full pipeline implementation
├── critique_prompts.md # Prompts for GPT-5/Claude expert review
├── medium_draft.md # Medium article draft outline
├── data/
├── model.joblib
└── README.md
