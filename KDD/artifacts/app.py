
import streamlit as st
import pandas as pd, json, joblib
import numpy as np
from pathlib import Path

ART_DIR = Path("artifacts")
MODEL_F = ART_DIR/"model.joblib"
CONF_F  = ART_DIR/"deploy_config.json"

st.set_page_config(page_title="Telco Churn Predictor", layout="centered")

@st.cache_resource
def load_model():
    return joblib.load(MODEL_F)

@st.cache_resource
def load_conf():
    with open(CONF_F) as f:
        return json.load(f)

model = load_model()
conf  = load_conf()
raw_cols = conf["raw_feature_columns"]
threshold = conf["threshold"]

st.title("📞 Telco Churn Predictor")
st.write("Upload a CSV with these columns:")
st.code(", ".join(raw_cols), language="text")

file = st.file_uploader("Upload CSV", type=["csv"])
if file is not None:
    df = pd.read_csv(file)
    # add missing cols
    for c in raw_cols:
        if c not in df.columns:
            df[c] = np.nan
    df = df[raw_cols]
    proba = model.predict_proba(df)[:,1]
    pred  = (proba >= threshold).astype(int)
    out = df.copy()
    out["churn_score"] = proba
    out["churn_pred"]  = pred
    st.write("Preview (first 20 rows):")
    st.dataframe(out.head(20))
    st.download_button("Download Scored CSV", out.to_csv(index=False), "scored.csv", "text/csv")
else:
    st.info("Upload a CSV to score churn probabilities.")
