import pandas as pd
import numpy as np

def compute_features(df):
    df["return"] = df["Close"].pct_change()
    df["sma10"] = df["Close"].rolling(10).mean()
    df["sma50"] = df["Close"].rolling(50).mean()
    df["volatility"] = df["return"].rolling(10).std()

    delta = df["Close"].diff()
    gain = delta.clip(lower=0).rolling(14).mean()
    loss = -delta.clip(upper=0).rolling(14).mean()
    rs = gain / loss
    df["rsi"] = 100 - (100 / (1 + rs))

    df["target"] = (df["Close"].shift(-1) > df["Close"]).astype(int)

    df = df.dropna()
    return df