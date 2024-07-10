from fastapi import FastAPI
from server.service.exchange_rate_service import ExchangeRateService
from server.service.currency_exchange_service import CurrencyExchangeService
from server.api import api


class App:
    app: FastAPI
    exchange_rate_service: ExchangeRateService
    currency_exchange_service: CurrencyExchangeService

    def __init__(self):
        self.app = FastAPI()
        self.exchange_rate_service = ExchangeRateService()
        self.currency_exchange_service = CurrencyExchangeService(self.exchange_rate_service)
        api.init(self.app, self.currency_exchange_service)
