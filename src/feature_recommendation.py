import pandas as pd

# Load dataset
df = pd.read_csv("data/sample.csv")

# Create report
report = open("reports/feature_recommendation.txt", "w")

report.write("===== FEATURE RECOMMENDATION ENGINE =====\n\n")

# Drop Columns
report.write("DROP COLUMN SUGGESTIONS\n")
report.write("--------------------------\n")

for col in df.columns:
    if df[col].isnull().sum() > len(df) / 2:
        report.write(col)
        report.write(" -> Too many missing values\n")

report.write("\n")

# Encode Columns
report.write("ENCODE COLUMN SUGGESTIONS\n")
report.write("--------------------------\n")

for col in df.select_dtypes(include="object").columns:
    report.write(col)
    report.write(" -> Encode this column\n")

report.write("\n")

# Scale Columns
report.write("SCALE COLUMN SUGGESTIONS\n")
report.write("--------------------------\n")

for col in df.select_dtypes(include="number").columns:
    report.write(col)
    report.write(" -> Scale this column\n")

report.write("\n")

# High Importance Features
report.write("HIGH IMPORTANCE FEATURES\n")
report.write("--------------------------\n")

for col in df.columns:
    report.write(col)
    report.write("\n")

report.close()

print("Feature Recommendation Report Generated Successfully!")
