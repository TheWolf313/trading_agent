from typing import Dict, List


def decide(latest: Dict) -> str:
    """Very simple strategy:
    - If price > sma10 -> 'sell'
    - If price < sma10 -> 'buy'
    - Else 'hold'
    """
    price = latest.get("close")
    sma = latest.get("sma10")
    if sma is None:
        return "hold"
    if price > sma:
        return "sell"
    if price < sma:
        return "buy"
    return "hold"
