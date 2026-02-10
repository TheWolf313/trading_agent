import json
from pathlib import Path
from typing import List, Dict, Any
import time

CACHE_DIR = Path("storage")
CACHE_DIR.mkdir(exist_ok=True)


def _cache_path(symbol: str) -> Path:
    return CACHE_DIR / f"{symbol}.json"


def save_cache(symbol: str, data: List[Dict[str, Any]]):
    p = _cache_path(symbol)
    with p.open("w", encoding="utf-8") as f:
        json.dump({"ts": time.time(), "data": data}, f)


def load_cache(symbol: str, max_age_seconds: int = 3600) -> List[Dict[str, Any]]:
    p = _cache_path(symbol)
    if not p.exists():
        return []
    payload = json.loads(p.read_text(encoding="utf-8"))
    if time.time() - payload.get("ts", 0) > max_age_seconds:
        return []
    return payload.get("data", [])


def fetch_ohlcv(symbol: str, interval: str = "1h", use_cache: bool = True) -> List[Dict[str, Any]]:
    """Stub: replace with real exchange/api calls. Returns list of dicts with at least 'ts' and 'close'."""
    if use_cache:
        data = load_cache(symbol)
        if data:
            return data
    # Placeholder synthetic data for now
    now = int(time.time())
    data = [{"ts": now - i * 3600, "close": 1000 + i} for i in range(100)][::-1]
    save_cache(symbol, data)
    return data
