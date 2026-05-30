import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

df = pd.read_csv("health_data.csv")
X = df[['Glucose','Haemoglobin','Cholesterol']]
y = df['Disease']

encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y_encoded)

joblib.dump(model, "health_predictor.pkl")
joblib.dump(encoder, "label_encoder.pkl")

print("Model trained and saved.")
