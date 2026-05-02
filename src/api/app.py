from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pandas as pd
import joblib
import mlflow.pyfunc
import os
from dotenv import load_dotenv
load_dotenv()

app = FastAPI(title="Apartments Price Prediction API", version="1.0")
mlflow.set_tracking_uri(os.environ.get("MLFLOW_TRACKING_URI"))
model = mlflow.pyfunc.load_model(
    model_uri="models:/apartments-price-model/Production"
)

class ApartmentFeatures(BaseModel):
    Area: float
    Payment: str
    Ownership: str
    Status: str
    Bedrooms: float
    Bathrooms: float
    Location: str
    Pool: int
    Electricity_Meter: int
    Water_Meter: int
    Natural_Gas: int
    PrivateGarden: int
    Landline: int
    Covered_Parking: int
    Security: int
    Balcony: int



@app.post("/predict")
def predict(data: ApartmentFeatures):
    df = pd.DataFrame([data.dict()])
    prediction = model.predict(df)
    return {"predicted_price": float(prediction[0])}