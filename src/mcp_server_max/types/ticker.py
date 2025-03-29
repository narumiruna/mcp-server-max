from datetime import datetime

from pydantic import BaseModel
from pydantic import Field
from pydantic import field_validator

# {
# "market": "ethtwd",
# "at": 1531905257,
# "buy": "200000.0",
# "buy_vol": "0.01",
# "sell": "200000.0",
# "sell_vol": "0.02",
# "open": "200000.0",
# "low": "200000.0",
# "high": "200000.0",
# "last": "200000.0",
# "vol": "10.0",
# "vol_in_btc": "10.0"
# }


class Ticker(BaseModel):
    market: str | None = Field(default=None)
    at: datetime | None = Field(default=None)
    buy: float | None = Field(default=None)
    buy_vol: float | None = Field(default=None)
    sell: float | None = Field(default=None)
    sell_vol: float | None = Field(default=None)
    open: float | None = Field(default=None)
    low: float | None = Field(default=None)
    high: float | None = Field(default=None)
    last: float | None = Field(default=None)
    vol: float | None = Field(default=None)
    vol_in_btc: float | None = Field(default=None)

    @field_validator(
        "buy",
        "buy_vol",
        "sell",
        "sell_vol",
        "open",
        "low",
        "high",
        "last",
        "vol",
        "vol_in_btc",
        mode="before",
    )
    @classmethod
    def convert_float(cls, value: str | float | None) -> float | None:
        if value is None:
            return None
        elif isinstance(value, float):
            return value
        elif value == "":
            return None
        else:
            return float(value)

    @field_validator("at", mode="before")
    @classmethod
    def convert_datetime(cls, value: int) -> datetime:
        return datetime.fromtimestamp(int(value))
