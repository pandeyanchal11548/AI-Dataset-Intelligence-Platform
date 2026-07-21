import os

# Create output report
report = open("reports/final_report.txt", "w")

report.write("===== FINAL DATASET REPORT =====\n\n")

files = [
    "reports/summary.csv",
    "reports/data_quality_score.csv",
    "reports/eda_report.txt",
    "reports/feature_recommendation.txt",
    "reports/feature_correlation_report.txt",
    "reports/ml_readiness_report.txt"
]

for file in files:

    report.write("---------------------------------\n")
    report.write(file)
    report.write("\n")
    report.write("---------------------------------\n")

    if os.path.exists(file):

        f = open(file, "r")

        report.write(f.read())

        f.close()

    else:

        report.write("File not found.\n")

    report.write("\n\n")

report.close()

print("Final Structured Report Generated Successfully!")