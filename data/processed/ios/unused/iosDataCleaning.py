import pandas as pd
from pathlib import Path


# Load data

here = Path.cwd()
root = next(p for p in [here, *here.parents] if (p / "data" / "raw").exists())

df = pd.read_csv(root / "data" / "raw" / "ios_turns.csv", header=0)


# KEEP ALL COLUMNS

raw_df = df.copy()
print(f"[INFO] Loaded rows/cols: {raw_df.shape}")


# Sanity checks on speed and duration

before = df.shape
df = df[df["eventStartSpeed"] >= 0]
print(f"[FILTER] eventStartSpeed >= 0: {before} -> {df.shape}")

before = df.shape
df = df[(df["eventEndSpeed"] >= 0) & (df["eventEndSpeed"] <= 120)]
print(f"[FILTER] 0 <= eventEndSpeed <= 120: {before} -> {df.shape}")

before = df.shape
df = df[df["eventDurationSeconds"] <= 15]
print(f"[FILTER] eventDurationSeconds <= 15: {before} -> {df.shape}")


# Duration & miles sanity

before = df.shape
df = df[df["eventMilesDriven"] < 0.3]
print(f"[FILTER] eventMilesDriven < 0.3: {before} -> {df.shape}")


# Speed-gap “impossible jump” gate

df["speed_gap"] = (df["eventEndSpeed"] - df["eventStartSpeed"]).abs()

before = df.shape
df = df[~((df["speed_gap"] > 10) & (df["eventDurationSeconds"] < 2))]
print(f"[FILTER] remove |Δspeed|>10 in <2s: {before} -> {df.shape}")

# Save cleaned output & keep raw

out_dir = root / "data" / "processed" / "ios"
out_dir.mkdir(parents=True, exist_ok=True)

clean_path = out_dir / "parent_cleanV2.csv"
df.to_csv(clean_path, index=False)
print(f"[SAVE] Cleaned file written to: {clean_path}")

# quick check
df_check = pd.read_csv(clean_path, nrows=5)
print(f"[CHECK] Preview saved columns: {list(df_check.columns)}")