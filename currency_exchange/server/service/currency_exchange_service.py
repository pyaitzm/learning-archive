from server.service.exchange_rate_service import ExchangeRateService
from server.domain.domain import CurrencyExchange


class CurrencyExchangeService:
    def __init__(self, exchange_rate_service: ExchangeRateService):
        self.exchange_rate_service = exchange_rate_service

    async def get_currency_exchange(self, target_currency: str, source_currency_amount: float) -> CurrencyExchange:
        date, exchange_rate = await self.exchange_rate_service.get_exchange_rate(target_currency)
        return CurrencyExchange(
            date=date,
            source_currency_amount=source_currency_amount,
            target_currency=target_currency,
            target_currency_amount=source_currency_amount * exchange_rate
        )
