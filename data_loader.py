import pandas as pd

def load_data(path):
    df = pd.read_csv(path, parse_dates=["Date"])

    # Remove ticker column 
    df = df.drop(columns=["ticker"])

    # Ensure sorted by time
    df = df.sort_values("Date")

    # Ensure numeric types 
    numeric_cols = ["Open", "High", "Low", "Close", "Volume"]
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")

    df = df.dropna()

    return df