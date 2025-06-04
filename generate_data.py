import pandas as pd
import random

medications = ["Adderall XR", "Vyvanse", "Strattera", "Intuniv", "Kapvay", "Ritalin"]

def generate_patient():
    age = random.randint(6, 18)
    weight_kg = random.randint(20, 70)
    sleep = random.choice(["good", "moderate", "poor"])
    activity = random.choice(["low", "medium", "high"])
    diet = random.choice(["low_protein", "balanced", "high_protein"])
    anxiety = random.choice([True, False])
    irritability = random.choice([True, False])
    prior_stimulant_use = random.choice([True, False])

    # --- Medication matching logic ---
    if anxiety or sleep == "poor":
        if age < 10 or weight_kg < 30:
            med = "Kapvay"
        elif irritability:
            med = "Strattera"
        else:
            med = "Intuniv"
    elif activity == "high":
        if diet == "high_protein" and not irritability:
            med = "Vyvanse"
        else:
            med = "Adderall XR"
    else:
        med = "Ritalin"

    # --- Inject noise (10-15% chance of wrong med) ---
    if random.random() < 0.1:
        med = random.choice([m for m in medications if m != med])

    # --- Dosage logic ---
    if med == "Strattera":
        dose_mg = round(weight_kg * 1.0)
    elif med == "Intuniv":
        dose_mg = 1 if age < 12 else 2
    elif med == "Vyvanse":
        dose_mg = 30 if weight_kg < 40 else 50
    else:
        dose_mg = 10

    return {
        "age": age,
        "weight_kg": weight_kg,
        "sleep": sleep,
        "activity": activity,
        "diet": diet,
        "anxiety": anxiety,
        "irritability": irritability,
        "prior_stimulant_use": prior_stimulant_use,
        "recommended_med": med,
        "recommended_dose_mg": dose_mg
    }

# Generate dataset
patients = [generate_patient() for _ in range(300)]
df = pd.DataFrame(patients)
df.to_csv("adhd_dataset.csv", index=False)
print(df.head())
