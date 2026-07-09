import pandas as pd

# Load dataset
df = pd.read_csv("data/sample.csv")

print("===== Column Classification Engine =====\n")

# Check every column
for column in df.columns:

    # Get data type of the column
    dtype = df[column].dtype

    # Numerical Columns
    if pd.api.types.is_numeric_dtype(df[column]):
        column_type = "Numerical"

    # Date/Time Columns
    elif pd.api.types.is_datetime64_any_dtype(df[column]):
        column_type = "Date/Time"

    # Text or Categorical Columns
    else:
        # Count unique values
        unique_values = df[column].nunique()

        # If unique values are small, treat as categorical
        if unique_values <= 10:
            column_type = "Categorical"
        else:
            column_type = "Text"

    # Print result
    print(f"{column} --> {column_type}")