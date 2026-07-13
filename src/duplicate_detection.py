import pandas as pd

df = pd.read_csv("data/sample.csv")

print("===== Duplicate Detection Module =====\n")

# Detect full row duplicates
full_duplicates = df[df.duplicated()]

print("Full Row Duplicates:")
print(full_duplicates)

duplicate_count = full_duplicates.shape[0]

print("\nTotal Full Row Duplicates:", duplicate_count)


print("\n===== Partial Duplicate Detection =====")

partial_duplicates = df[df.duplicated(subset=["Name"], keep=False)]

print(partial_duplicates)