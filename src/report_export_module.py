import pandas as pd

# Load dataset
df = pd.read_csv("data/sample.csv")

# Export CSV
df.to_csv("reports/export_report.csv", index=False)

# Export JSON
df.to_json("reports/export_report.json", orient="records", indent=4)

# Export HTML
df.to_html("reports/export_report.html", index=False)

print("Reports exported successfully!")