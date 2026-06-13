from pydantic import BaseModel
from typing import Optional, List


class SupportZone(BaseModel):
    symbol: str
    upper: float
    lower: float
    confidence: float
    timeframe: str
    atr: float


class RiskModel(BaseModel):
    account_size: float
    risk_per_trade_pct: float = 1.0
    max_position_value: Optional[float] = None


class Strategy(BaseModel):
    name: str
    direction: str  # long only for now
    timeframe: str

    entry_rules: List[str]
    exit_rules: List[str]

    risk: RiskModel


class Trade(BaseModel):
    symbol: str
    strategy_name: str

    entry_price: float
    stop_loss: float
    take_profit: Optional[float]

    position_size: float
    capital_used: float

    support_zone: SupportZone
