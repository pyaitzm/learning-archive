from pydantic import BaseModel
from datetime import date
from server.domain.domain import CurrencyExchange
from fastapi import FastAPI
from server.service.currency_exchange_service import CurrencyExchangeService

BASE_PATH = '/usd'


class CurrencyExchangeModel(BaseModel):
    date: date
    source_currency_amount: float
    target_currency: str
    target_currency_amount: float
    source_currency: str = 'usd'


def _create_currency_exchange_model(currency_exchange: CurrencyExchange) -> CurrencyExchangeModel:
    return CurrencyExchangeModel(
        date=currency_exchange.date,
        source_currency=currency_exchange.source_currency,
        source_currency_amount=currency_exchange.source_currency_amount,
        target_currency=currency_exchange.target_currency,
        target_currency_amount=currency_exchange.target_currency_amount
    )


def init(app: FastAPI, service: CurrencyExchangeService):
    @app.get(BASE_PATH + '/{target_currency}', response_model=CurrencyExchangeModel)
    async def get_currency_exchange(target_currency: str, source_currency_amount: float = 1):
        currency_exchange = await service.get_currency_exchange(target_currency, source_currency_amount)
        return _create_currency_exchange_model(currency_exchange)
