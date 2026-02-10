from typing import List, Dict


def simple_backtest(ohlcv: List[Dict], strategy_fn) -> Dict:
    cash = 10000.0
    position = 0.0
    entry_price = None
    for row in ohlcv:
        signal = strategy_fn(row)
        price = row.get("close")
        if signal == "buy" and position == 0:
            # buy with all cash
            position = cash / price
            cash = 0.0
            entry_price = price
        elif signal == "sell" and position > 0:
            cash = position * price
            position = 0.0
            entry_price = None
    nav = cash + position * (ohlcv[-1]["close"] if ohlcv else 0)
    return {"final_nav": nav, "return_pct": (nav / 10000.0 - 1) * 100}
