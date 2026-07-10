import pandas as pd

# Load dataset
df = pd.read_csv("data/sample.csv")

print("===== Missing Value Analyzer =====\n")

for column in df.columns:

    # Count missing values
    null_count = df[column].isnull().sum()

    # Calculate percentage
    null_percentage = (null_count / len(df)) * 100

    # Classify severity
    if null_percentage == 0:
        severity = "No Missing"

    elif null_percentage <= 20:
        severity = "Low"

    elif null_percentage <= 50:
        severity = "Medium"

    else:
        severity = "High"

    # Display results
    print(f"Column: {column}")
    print(f"Null Count: {null_count}")
    print(f"Null Percentage: {null_percentage:.2f}%")
    print(f"Severity: {severity}")
    print("----------------------------")