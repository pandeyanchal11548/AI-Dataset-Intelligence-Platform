import pandas as pd

# Load dataset
df = pd.read_csv("data/sample.csv")

print("===== Missing Value Analyzer =====\n")

# Store results
results = []

# Loop through each column
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

    # Save results
    results.append({
        "Column": column,
        "Null Count": null_count,
        "Null Percentage": round(null_percentage, 2),
        "Severity": severity
    })

    # Display results for each column
    print(f"Column: {column}")
    print(f"Null Count: {null_count}")
    print(f"Null Percentage: {null_percentage:.2f}%")
    print(f"Severity: {severity}")
    print("----------------------------")

# Create DataFrame
report = pd.DataFrame(results)

# Display final report
print("\n===== Missing Value Report =====\n")
print(report)

# Save report as CSV
report.to_csv("reports/missing_value_report.csv", index=False)

# Save report as JSON
report.to_json(
    "reports/missing_value_report.json",
    orient="records",
    indent=4
)

print("\nReports saved successfully!")