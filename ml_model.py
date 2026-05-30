import joblib

model = joblib.load("health_predictor.pkl")
encoder = joblib.load("label_encoder.pkl")

def predict_disease(glucose, haemoglobin, cholesterol):
    prediction = model.predict([[glucose, haemoglobin, cholesterol]])
    return encoder.inverse_transform(prediction)[0]
