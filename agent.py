from typing import List
from .config import load_config
from .data_fetcher import fetch_ohlcv
from .feature_engine import add_features
from .strategy import decide


class Agent:
    def __init__(self, config=None):
        self.config = config or load_config()

    def run_once(self):
        for sym in self.config.symbols:
            data = fetch_ohlcv(sym, interval=self.config.interval)
            feats = add_features(data)
            latest = feats[-1]
            action = decide(latest)
            print(f"{sym} -> action: {action} (price={latest.get('close')} sma10={latest.get('sma10')})")
