import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/sample.csv")

print("===== Correlation Analyzer =====\n")

# Select only numeric columns
numeric_df = df.select_dtypes(include=["number"])

# Generate correlation matrix
correlation_matrix = numeric_df.corr()

print("Correlation Matrix:\n")
print(correlation_matrix)

# Save correlation matrix
correlation_matrix.to_csv("reports/correlation_matrix.csv")

# Create heatmap
plt.figure(figsize=(8,6))

plt.imshow(correlation_matrix, cmap="coolwarm")

plt.colorbar()

plt.xticks(
    range(len(correlation_matrix.columns)),
    correlation_matrix.columns,
    rotation=90
)

plt.yticks(
    range(len(correlation_matrix.columns)),
    correlation_matrix.columns
)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig("reports/correlation_heatmap.png")

plt.show()

print("\nFiles saved successfully!")