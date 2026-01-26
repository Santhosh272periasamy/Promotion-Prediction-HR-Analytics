from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os
import pandas as pd

# Load model

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "..",
    "model",
    "promotion_voting_pipeline.pkl"
)

model = joblib.load(MODEL_PATH)

app = FastAPI(title="Employee Promotion Prediction API")

class EmployeeFeatures(BaseModel):
    department: str
    region: str
    education: str
    gender: str
    recruitment_channel: str
    no_of_trainings: int
    age: int
    previous_year_rating: float
    length_of_service: int
    awards_won: int
    avg_training_score: float


@app.post("/predict")


def predict_promotion(data: EmployeeFeatures):

    # df = pd.DataFrame([data.dict()])
    # print("Incoming columns:", df.columns.tolist())
    # print("Expected columns:", model.named_steps["preprocessing"].feature_names_in_)

    
    input_df = pd.DataFrame([data.dict()])
    
    prediction = model.predict(input_df)[0]

    if hasattr(model, "predict_proba"):
        probability = model.predict_proba(input_df)[0][1]
    else:
        probability = None
    
    return {
        #"is_promoted": int(prediction)
        "promotion_prediction": int(prediction),
        "promotion_probability": float(probability) if probability is not None else None

    }


