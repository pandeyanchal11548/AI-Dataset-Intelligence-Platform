import pandas as pd
import os

file_path = "data/sample.csv"

# Check if file exists
if not os.path.exists(file_path):
    print("Error: File not found!")

else:

    # CSV File
    if file_path.endswith(".csv"):
        df = pd.read_csv(file_path)

    # Excel File
    elif file_path.endswith(".xlsx"):
        df = pd.read_excel(file_path)

    else:
        print("Unsupported file format")
        exit()

    print("Dataset Loaded Successfully!\n")
    print(df)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)