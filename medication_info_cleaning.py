import pandas as pd

# Load medication info
df = pd.read_csv("adhd_medications.csv")

# Clean duration field
def parse_duration(s: str) -> float:
    s = s.replace("hours", "").replace("hour", "").strip()
    if "-" in s:
        lo, hi = [float(x) for x in s.split("-")]
        return (lo + hi) / 2
    if "Up to" in s:
        return float(s.split()[-1])
    if s.startswith("~"):
        return float(s[1:])
    return float(s)

# Clean cost field
def parse_cost(s: str) -> float:
    s = s.replace("$", "")
    if "-" in s:
        lo, hi = [float(x) for x in s.split("-")]
        return (lo + hi) / 2
    return float(s)

df["Avg Duration (hrs)"] = df["Duration"].apply(parse_duration)
df["Avg Cost (USD)"] = df["Estimated Monthly Cost"].apply(parse_cost)

df.to_csv("cleaned_med_info.csv", index=False)
print("✅ Medication info cleaned and saved.")
