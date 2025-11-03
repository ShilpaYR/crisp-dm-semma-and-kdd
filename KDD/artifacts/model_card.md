# Model Card — Telco Churn

**Model:** Champion  
**Created:** 2025-11-03T04:45:34.098102Z  
**scikit-learn:** 1.6.1

## Intended Use
Predict customer churn probability to prioritize retention outreach.

## Data
Telco customer dataset (train/test split 80/20, stratified by Churn).  
Raw columns used (preprocessor handles missing values & one-hot encoding):
gender, SeniorCitizen, Partner, Dependents, tenure, PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies, Contract, PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges

## Metrics (Test)
- Accuracy:  0.4968
- F1:        0.5080
- ROC-AUC:   0.8430
- PR-AUC:    0.6496
- Brier:     0.1586

## Threshold
Deployment threshold: **0.120** (cost-optimized(from Evaluation))  
Predicted label = 1 if probability ≥ threshold, else 0.

## Risks & Ethics
- Possible bias by tenure/contract type; monitor subgroup metrics (e.g., SeniorCitizen).
- Calibrate periodically; watch for drift.

## Maintenance
- Retrain monthly/quarterly or after significant plan changes.
- Log predictions + outcomes to re-evaluate calibration.

