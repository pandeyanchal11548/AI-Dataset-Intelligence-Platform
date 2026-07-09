import pandas as pd

# Load the dataset
df = pd.read_csv("data/sample.csv")

# Row count
print("Row Count:", len(df))

# Column count
print("Column Count:", len(df.columns))

# Data types
print("\nData Types:")
print(df.dtypes)

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate rows
print("\nDuplicate Rows:", df.duplicated().sum())