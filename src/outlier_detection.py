import pandas as pd
from scipy.stats import zscore

# Load dataset
df = pd.read_csv("data/sample.csv")

print("===== Outlier Detection Engine =====\n")

# Find numeric columns
numeric_columns = df.select_dtypes(include=["number"]).columns

print("Numeric Columns:")
print(numeric_columns)

print("\n==============================")
print("IQR METHOD")
print("==============================")

iqr_results = []

# IQR Method
for column in numeric_columns:

    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = df[
        (df[column] < lower_bound) |
        (df[column] > upper_bound)
    ]

    outlier_count = len(outliers)

    print(f"\nColumn : {column}")
    print(f"Lower Bound : {lower_bound}")
    print(f"Upper Bound : {upper_bound}")
    print(f"Outliers Found : {outlier_count}")

    iqr_results.append({
        "Column": column,
        "Lower Bound": round(lower_bound, 2),
        "Upper Bound": round(upper_bound, 2),
        "Outlier Count": outlier_count
    })

# Save IQR Report
iqr_report = pd.DataFrame(iqr_results)

print("\n===== IQR Report =====")
print(iqr_report)

iqr_report.to_csv("reports/iqr_outlier_report.csv", index=False)
iqr_report.to_json(
    "reports/iqr_outlier_report.json",
    orient="records",
    indent=4
)

print("\n==============================")
print("Z-SCORE METHOD")
print("==============================")

zscore_results = []

# Z-Score Method
for column in numeric_columns:

    z_scores = zscore(df[column])

    outliers = df[abs(z_scores) > 3]

    outlier_count = len(outliers)

    print(f"\nColumn : {column}")
    print(f"Outliers Found : {outlier_count}")

    zscore_results.append({
        "Column": column,
        "Outlier Count": outlier_count
    })

# Save Z-Score Report
zscore_report = pd.DataFrame(zscore_results)

print("\n===== Z-Score Report =====")
print(zscore_report)

zscore_report.to_csv("reports/zscore_outlier_report.csv", index=False)
zscore_report.to_json(
    "reports/zscore_outlier_report.json",
    orient="records",
    indent=4
)

print("\nReports Generated Successfully!")
