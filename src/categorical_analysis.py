import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/sample.csv")

print("===== Categorical Analysis Engine =====")

# Select categorical columns
cat_cols = df.select_dtypes(include="object").columns

# Check if categorical columns exist
if len(cat_cols) == 0:
    print("No categorical columns found.")
else:
    for col in cat_cols:

        print(f"\nColumn: {col}")

        # Value Counts
        counts = df[col].value_counts()

        print(counts)

        # Save value counts
        counts.to_csv(f"reports/{col}_value_counts.csv")

        # Bar Chart
        plt.figure(figsize=(6,4))
        counts.plot(kind="bar")

        plt.title(col)
        plt.xlabel(col)
        plt.ylabel("Count")

        plt.tight_layout()

        plt.savefig(f"reports/{col}_distribution.png")

        plt.close()

print("\nTask Completed!")