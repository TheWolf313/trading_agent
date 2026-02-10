from dataclasses import dataclass, field
import os
from typing import List

@dataclass
class Config:
    api_key: str = field(default_factory=lambda: os.getenv("API_KEY", ""))
    symbols: List[str] = field(default_factory=lambda: os.getenv("SYMBOLS", "BTC-USD").split(","))
    interval: str = field(default_factory=lambda: os.getenv("INTERVAL", "1h"))


def load_config() -> Config:
    return Config()
