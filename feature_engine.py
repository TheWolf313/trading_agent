from typing import List, Dict


def simple_sma(series: List[float], window: int) -> List[float]:
    if window <= 0:
        raise ValueError("window must be > 0")
    out = []
    cum = 0.0
    for i, v in enumerate(series):
        cum += v
        if i >= window:
            cum -= series[i - window]
        if i >= window - 1:
            out.append(cum / window)
        else:
            out.append(None)
    return out


def add_features(ohlcv: List[Dict]) -> List[Dict]:
    closes = [c["close"] for c in ohlcv]
    sma10 = simple_sma(closes, 10)
    out = []
    for i, row in enumerate(ohlcv):
        r = dict(row)
        r["sma10"] = sma10[i]
        out.append(r)
    return out
