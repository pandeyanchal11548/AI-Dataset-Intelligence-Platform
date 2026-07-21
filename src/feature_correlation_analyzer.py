import pandas as pd

# Load dataset
df = pd.read_csv("data/sample.csv")

# Select numeric columns
num_df = df.select_dtypes(include="number")

# Correlation matrix
corr = num_df.corr()

# Create report
report = open("reports/feature_correlation_report.txt", "w")

report.write("===== FEATURE CORRELATION ANALYZER =====\n\n")

report.write("HIGHLY CORRELATED FEATURES\n")
report.write("----------------------------\n")

for i in range(len(corr.columns)):
    for j in range(i + 1, len(corr.columns)):

        value = corr.iloc[i, j]

        if abs(value) > 0.8:
            report.write(corr.columns[i])
            report.write(" and ")
            report.write(corr.columns[j])
            report.write(" : ")
            report.write(str(value))
            report.write("\n")

report.write("\n")

report.write("REDUNDANT COLUMNS\n")
report.write("----------------------------\n")

found = False

for i in range(len(corr.columns)):
    for j in range(i + 1, len(corr.columns)):

        value = corr.iloc[i, j]

        if abs(value) > 0.8:
            report.write(corr.columns[j])
            report.write("\n")
            found = True

if found == False:
    report.write("No redundant columns found.\n")

report.close()

print("Feature Correlation Report Generated Successfully!")