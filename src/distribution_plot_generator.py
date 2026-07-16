import pandas as pd
import matplotlib.pyplot as plt
import os

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("data/sample.csv")

# -----------------------------
# Create reports folder if needed
# -----------------------------
os.makedirs("reports", exist_ok=True)

print("\n===== Distribution Plot Generator =====\n")

# -----------------------------
# Select Numeric Columns
# -----------------------------
numeric_columns = df.select_dtypes(include=["int64", "float64"]).columns

if len(numeric_columns) == 0:
    print("No numeric columns found in dataset.")
else:

    for column in numeric_columns:

        # -------------------------
        # Histogram
        # -------------------------
        plt.figure(figsize=(8,5))

        plt.hist(
            df[column].dropna(),
            bins=20,
            edgecolor="black"
        )

        plt.title(f"Histogram - {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")

        histogram_path = f"reports/{column}_histogram.png"

        plt.savefig(histogram_path)

        plt.close()

        print(f"Histogram Saved : {histogram_path}")

        # -------------------------
        # Density Plot
        # -------------------------
        plt.figure(figsize=(8,5))

        df[column].dropna().plot(
            kind="density"
        )

        plt.title(f"Density Plot - {column}")
        plt.xlabel(column)

        density_path = f"reports/{column}_density.png"

        plt.savefig(density_path)

        plt.close()

        print(f"Density Plot Saved : {density_path}")

print("\nDistribution plots generated successfully!")