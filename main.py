from data_loader import load_data
from feature_engineering import compute_features
from model import train_model
from signal_generator import generate_signal
from config import *

import numpy as np

df = load_data("data/gold_daily.csv")
df = compute_features(df)

features = ["return", "sma10", "sma50", "volatility", "rsi"]

split = int(len(df) * TRAIN_SPLIT)

X_train = df[features][:split]
y_train = df["target"][:split]

model = train_model(X_train, y_train)

latest_row = df[features].iloc[[-1]]

signal = generate_signal(model, latest_row, BUY_THRESHOLD, SELL_THRESHOLD)

print("Trading Signal:", signal)