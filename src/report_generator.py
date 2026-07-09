import pandas as pd
import json

df = pd.read_csv("data/sample.csv")

summary = {
    "Row Count": int(len(df)),
    "Column Count": int(len(df.columns)),
    "Missing Values": int(df.isnull().sum().sum()),
    "Duplicate Rows": int(df.duplicated().sum())
}

with open("reports/summary.json", "w") as file:
    json.dump(summary, file, indent=4)
    
# Save CSV report
summary_df = pd.DataFrame(
    summary.items(),
    columns=["Metric", "Value"]
)

summary_df.to_csv(
    "reports/summary.csv",
    index=False
)

print("Summary reports generated successfully!")