import pandas as pd

def load_dataset():
    df = pd.read_csv("data/sample.csv")
    return df

def save_report(text, filename):
    report = open(filename, "w")
    report.write(text)
    report.close()