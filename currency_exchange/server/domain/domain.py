from dataclasses import dataclass
from datetime import date


@dataclass
class CurrencyExchange:
    date: date
    source_currency_amount: float
    target_currency: str
    target_currency_amount: float
    source_currency: str = 'usd'
