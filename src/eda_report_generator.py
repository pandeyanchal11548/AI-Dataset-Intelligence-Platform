import pandas as pd

# Load dataset
df = pd.read_csv("data/sample.csv")

# Create report file
report = open("reports/eda_report.txt", "w")

report.write("===== AUTOMATED EDA REPORT =====\n\n")

# Dataset Summary
report.write("DATASET SUMMARY\n")
report.write("----------------------\n")

report.write("Rows : ")
report.write(str(df.shape[0]))
report.write("\n")

report.write("Columns : ")
report.write(str(df.shape[1]))
report.write("\n\n")

# Column Names
report.write("COLUMN NAMES\n")
report.write("----------------------\n")

for col in df.columns:
    report.write(col)
    report.write("\n")

report.write("\n")

# Missing Values
report.write("MISSING VALUES\n")
report.write("----------------------\n")
report.write(str(df.isnull().sum()))
report.write("\n\n")

# Numerical Summary
report.write("NUMERICAL SUMMARY\n")
report.write("----------------------\n")
report.write(str(df.describe()))
report.write("\n\n")

# Insights
report.write("INSIGHTS\n")
report.write("----------------------\n")

if df.isnull().sum().sum() == 0:
    report.write("No missing values found.\n")
else:
    report.write("Missing values found.\n")

report.write("Charts are available in the reports folder.\n")
report.write("Correlation heatmap is available in the reports folder.\n")

report.close()

print("EDA Report Generated Successfully!")