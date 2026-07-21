
import numpy as np
import pandas as pd

# -----------------------------
# Load Dataset
# -----------------------------


df = pd.read_csv("data/sample.csv")
print("\n========== DATA QUALITY SCORING SYSTEM ==========\n")

# -----------------------------
# Missing Values
# -----------------------------
total_cells = df.shape[0] * df.shape[1]

missing_values = df.isnull().sum().sum()

missing_percentage = (missing_values / total_cells) * 100

# -----------------------------
# Duplicate Rows
# -----------------------------
duplicate_rows = df.duplicated().sum()

duplicate_percentage = (duplicate_rows / len(df)) * 100

# -----------------------------
# Outlier Detection (IQR)
# -----------------------------
numeric_columns = df.select_dtypes(include=np.number)

total_outliers = 0

for column in numeric_columns.columns:

    Q1 = numeric_columns[column].quantile(0.25)
    Q3 = numeric_columns[column].quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    outliers = ((numeric_columns[column] < lower) |
                (numeric_columns[column] > upper)).sum()

    total_outliers += outliers

outlier_percentage = (total_outliers / total_cells) * 100

# -----------------------------
# Data Consistency
# -----------------------------
consistency_issues = 0

for column in df.select_dtypes(include="object").columns:

    consistency_issues += (
        df[column]
        .astype(str)
        .str.strip()
        .eq("")
        .sum()
    )

consistency_percentage = (consistency_issues / total_cells) * 100

# -----------------------------
# Quality Score
# -----------------------------
score = 100

score -= missing_percentage * 0.30
score -= duplicate_percentage * 0.20
score -= outlier_percentage * 0.30
score -= consistency_percentage * 0.20

score = round(score, 2)

if score < 0:
    score = 0

# -----------------------------
# Grade
# -----------------------------
if score >= 90:
    grade = "Excellent"

elif score >= 75:
    grade = "Good"

elif score >= 60:
    grade = "Average"

else:
    grade = "Poor"

# -----------------------------
# Print Report
# -----------------------------
print("========== DATA QUALITY REPORT ==========\n")

print(f"Missing Values        : {missing_values}")
print(f"Missing Percentage    : {missing_percentage:.2f}%")

print(f"\nDuplicate Rows        : {duplicate_rows}")
print(f"Duplicate Percentage  : {duplicate_percentage:.2f}%")

print(f"\nTotal Outliers        : {total_outliers}")
print(f"Outlier Percentage    : {outlier_percentage:.2f}%")

print(f"\nConsistency Issues    : {consistency_issues}")
print(f"Consistency Percentage: {consistency_percentage:.2f}%")

print("\n-----------------------------------------")

print(f"Dataset Score         : {score}/100")
print(f"Grade                 : {grade}")

print("-----------------------------------------")

# -----------------------------
# Save CSV Report
# -----------------------------
report = pd.DataFrame({
    "Metric": [
        "Missing Values",
        "Missing Percentage",
        "Duplicate Rows",
        "Duplicate Percentage",
        "Outliers",
        "Outlier Percentage",
        "Consistency Issues",
        "Consistency Percentage",
        "Final Score",
        "Grade"
    ],
    "Value": [
        missing_values,
        round(missing_percentage, 2),
        duplicate_rows,
        round(duplicate_percentage, 2),
        total_outliers,
        round(outlier_percentage, 2),
        consistency_issues,
        round(consistency_percentage, 2),
        score,
        grade
    ]
})

report.to_csv(
    "reports/data_quality_score.csv",
    index=False
)

print("\nCSV Report Saved Successfully!")