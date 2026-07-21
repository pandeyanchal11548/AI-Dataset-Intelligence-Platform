import pandas as pd

# Load dataset
df = pd.read_csv("data/sample.csv")

# Create report
report = open("reports/ml_readiness_report.txt", "w")

report.write("===== ML READINESS SCORE =====\n\n")

# Data Completeness
total_cells = df.shape[0] * df.shape[1]
missing_cells = df.isnull().sum().sum()

completeness = ((total_cells - missing_cells) / total_cells) * 100

report.write("Data Completeness : ")
report.write(str(round(completeness, 2)))
report.write("%\n\n")

# Feature Quality
numeric_columns = len(df.select_dtypes(include="number").columns)
total_columns = len(df.columns)

feature_quality = (numeric_columns / total_columns) * 100

report.write("Feature Quality : ")
report.write(str(round(feature_quality, 2)))
report.write("%\n\n")

# Noise Level
duplicate_rows = df.duplicated().sum()

noise = (duplicate_rows / len(df)) * 100

report.write("Noise Level : ")
report.write(str(round(noise, 2)))
report.write("%\n\n")

# Final Score
score = (completeness + feature_quality + (100 - noise)) / 3

report.write("Final ML Readiness Score : ")
report.write(str(round(score, 2)))
report.write("/100\n")

report.close()

print("ML Readiness Report Generated Successfully!")