import pandas as pd

df = pd.read_csv("C:\\Users\\apues\\Downloads\\archive (28)\\us-shein-office_and_school_supplies-4233.csv", header=None)

for col in df.columns:
    print(f"\n--- COLUMN {col} ---")
    print(df[col].head(5))