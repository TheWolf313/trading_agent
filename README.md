# trading_agent
Gold Trading Agent (Offline ML-Based Signal Engine)

Overview
This project implements a simple machine learning–based trading agent for Gold Futures using historical daily price data.

The system:

Loads offline historical gold data (CSV)

Engineers technical indicators

Trains a Logistic Regression model

Generates a BUY / SELL / HOLD signal based on prediction probabilities

This is an educational quantitative trading prototype demonstrating:

Time-series feature engineering

Supervised learning for direction prediction

Signal generation logic

Modular project structure

Data Source
Gold Futures historical data (GC=F) downloaded as CSV from Yahoo Finance or Kaggle.

Expected dataset columns:
Date, Open, High, Low, Close, Volume

Place the file in:
data/gold_daily.csv

Project Structure
trading_agent/
│
├── data/
│ └── gold_daily.csv
├── config.py
├── data_loader.py
├── feature_engineering.py
├── model.py
├── signal_generator.py
└── main.py

Features Engineered

Daily returns

10-day Simple Moving Average (SMA10)

50-day Simple Moving Average (SMA50)

10-day rolling volatility

14-day RSI

Target Variable
1 → Next day close > today close
0 → Otherwise

Model
Logistic Regression (scikit-learn)
Train/Test split: 80% / 20%

Signal Logic
If probability > 0.6 → BUY
If probability < 0.4 → SELL
Otherwise → HOLD

Installation
pip install pandas numpy scikit-learn

Run
python main.py

Important Notes

No transaction cost modeling

No slippage modeling

No macroeconomic inputs

No walk-forward validation

Not suitable for live trading

This is a structured educational prototype for experimentation and learning.
