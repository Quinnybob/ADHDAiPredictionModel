import joblib

# Load model and encoder
model = joblib.load("adhd_model.pkl")
label_encoder = joblib.load("med_label_encoder.pkl")

# Predict a test sample
# Format: [age, sleep, activity, diet, anxiety, irritability, prior_stimulant_use, weight_kg]
sample = [[14, 1, 2, 0, 1, 0, 1, 40]]  # <-- these must be encoded values!

prediction = model.predict(sample)
decoded = label_encoder.inverse_transform(prediction)

print("🧠 Predicted medication:", decoded[0])
