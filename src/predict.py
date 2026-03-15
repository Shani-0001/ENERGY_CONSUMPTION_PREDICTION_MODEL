import joblib
import pandas as pd

model = joblib.load("../models/energy_model.pkl")

def predict_energy(data):

    df = pd.DataFrame([data])

    prediction = model.predict(df)

    return prediction[0]
