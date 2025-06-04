import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib

# 1. Load the synthetic dataset
df = pd.read_csv("adhd_dataset.csv")

# 2. Encode categorical features
df_encoded = df.copy()
label_encoders = {}

categorical_cols = ["sleep", "activity", "diet", "recommended_med"]
for col in categorical_cols:
    le = LabelEncoder()
    df_encoded[col] = le.fit_transform(df_encoded[col])
    label_encoders[col] = le

# 3. Split into features (X) and target (y)
X = df_encoded.drop(["recommended_med"], axis=1)
y = df_encoded["recommended_med"]

# 4. Split into train/test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Train a model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 6. Save model and encoder
joblib.dump(model, "adhd_model.pkl")
joblib.dump(label_encoders["recommended_med"], "med_label_encoder.pkl")

print("✅ Model trained and saved.")
