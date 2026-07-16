import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/sample.csv")

# Select only numeric columns
num_df = df.select_dtypes(include="number")

# Find correlation
corr = num_df.corr()

# Print correlation matrix
print("Correlation Matrix")
print(corr)

# Save correlation matrix
corr.to_csv("reports/correlation_matrix.csv")

# Create heatmap
plt.figure(figsize=(6,5))

plt.imshow(corr, cmap="coolwarm")

plt.colorbar()

plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
plt.yticks(range(len(corr.columns)), corr.columns)

plt.title("Correlation Heatmap")

plt.savefig("reports/correlation_heatmap.png")

plt.show()

print("Correlation matrix saved in reports/correlation_matrix.csv")
print("Heatmap saved in reports/correlation_heatmap.png")