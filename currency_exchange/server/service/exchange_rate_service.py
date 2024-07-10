from aiohttp import ClientSession
from typing import Tuple
from datetime import datetime

EXCHANGE_RATES_API_PATH = 'https://latest.currency-api.pages.dev/v1/currencies/usd.json'


class ExchangeRateServiceException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class ExchangeRateService:
    @staticmethod
    async def _fetch_exchange_rates_from_api():
        async with ClientSession(raise_for_status=True) as session:
            async with session.request('GET', EXCHANGE_RATES_API_PATH, ssl=False) as response:
                if 200 <= response.status <= 299:
                    return await response.json()

    async def get_exchange_rate(self, target_currency: str) -> Tuple[datetime.date, float]:
        data = await ExchangeRateService._fetch_exchange_rates_from_api()
        if target_currency not in data['usd']:
            raise ExchangeRateServiceException('target currency not found')
        return datetime.strptime(data['date'], '%Y-%m-%d').date(), float(data['usd'][target_currency])
