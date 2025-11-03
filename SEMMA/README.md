# SEMMA Project — Bank Marketing Campaign (UCI)

This project applies the **SEMMA** methodology (Sample, Explore, Modify, Model, Assess) using the *Bank Marketing* dataset.  
It demonstrates the data mining workflow for classification, interpretability, and business-focused evaluation.

---

## 📘 Project Overview
- **Goal:** Predict whether a client will subscribe to a term deposit after a marketing call.
- **Dataset:** [Bank Marketing (UCI / Kaggle)](https://www.kaggle.com/datasets/janiobachmann/bank-marketing-dataset)
- **Target Variable:** `y` (yes/no → 1/0)
- **Type:** Binary Classification

---

## 🚀 How to Run
1. **Open a terminal** in the project root:
   ```bash
   cd SEMMA
   jupyter notebook
2. Open notebook.ipynb in Jupyter Notebook.
3. Run all cells sequentially from top to bottom.
   - Each phase corresponds to one CRISP-DM stage.
   - Cells marked OLD CODE / BEFORE CRITIQUING show the original approach.
   - The following cells show the REVISED (GPT-5 critiqued) implementation

---

## 🔁 SEMMA Phases

### 1. Sample
- Loaded `bank-additional-full.csv` (~41K rows, 20+ features).
- Canonicalized target (`yes`→1, `no`→0).
- Stratified 60/20/20 split (Train/Valid/Test).
- Performed representativeness checks (Chi², KS).

### 2. Explore
- Conducted data audits (missingness, duplicates, drift).
- Detected policy-leakage variables (e.g., `duration`).
- Ranked signals using Mutual Information and point-biserial correlation.
- Built feature audit with suggested actions (drop/merge/bin).

### 3. Modify
- Dropped leakage & constant columns.
- Winsorized outliers, merged rare categorical levels.
- Applied version-safe OneHotEncoder + KFold TargetEncoder.
- Built unified preprocessing pipeline (`preproc`).

### 4. Model
- Trained calibrated **Logistic Regression** and **Random Forest**.
- Used 5-fold CV optimizing **PR-AUC**.
- Selected champion model by validation PR-AUC with bootstrap CI.
- Chose threshold by **cost** (FN:FP = 5:1).

### 5. Assess
- Evaluated champion on holdout test.
- Reported Accuracy, F1, ROC-AUC, PR-AUC, Brier, ECE, KS.
- Generated ROC, PR, Calibration, and Lift plots.
- Built decile table (response, capture, lift).
- Compared Validation→Test stability.

---

## 🧠 Key Learnings
- SEMMA emphasizes data refinement before modeling.
- Leakage prevention (dropping `duration`) drastically improved reliability.
- Rare-level merging reduced cardinality without hurting accuracy.
- Cost-based thresholds aligned predictions with business ROI.

---
