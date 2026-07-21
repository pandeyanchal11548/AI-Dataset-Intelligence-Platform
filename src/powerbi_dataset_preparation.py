import pandas as pd

# Load dataset
df = pd.read_csv("data/sample.csv")

print("Preparing dataset for Power BI...")

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing values
for col in df.columns:

    if pd.api.types.is_numeric_dtype(df[col]):
        df[col] = df[col].fillna(df[col].mean())

    else:
        df[col] = df[col].fillna("Unknown")

# Save cleaned dataset
df.to_csv("reports/powerbi_dataset.csv", index=False)

print("Power BI dataset created successfully!")