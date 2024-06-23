from fastapi import FastAPI
import joblib
import numpy as np
import pandas as pd

app = FastAPI()

# Load the trained model
model_file = joblib.load('model_endpoint/boston_reg.model')

@app.get("/")
def read_root():
    return {"message": f"Welcome to the {model_file['id']} model API"}

@app.post("/predict/")
def predict(data: dict):
    x_df = pd.DataFrame(data=data,index=[0]).loc[[[0]],model_file['features']]
    prediction = model_file['model_pipeline'].predict(x_df)
    return {"prediction": prediction[0]}