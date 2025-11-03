from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import pandas as pd, joblib, json
from pathlib import Path

MODEL_PATH = Path("artifacts/model_rf_fast_pipeline.joblib")
SCHEMA_PATH = Path("artifacts/input_schema.json")

pipe = joblib.load(MODEL_PATH)
required = json.loads(SCHEMA_PATH.read_text())["required"]

class Item(BaseModel):
    __root__: dict

class Batch(BaseModel):
    items: List[Item]

app = FastAPI(title="Weekly Sales Predictor", version="1.0")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/v1/predict")
def predict(batch: Batch):
    recs = [i.__root__ for i in batch.items]
    df = pd.DataFrame.from_records(recs)
    miss = [c for c in required if c not in df.columns]
    if miss:
        return {"error": f"Missing required features: {miss}"}
    df = df.reindex(columns=required)
    preds = pipe.predict(df).tolist()
    return {"predictions": preds}
