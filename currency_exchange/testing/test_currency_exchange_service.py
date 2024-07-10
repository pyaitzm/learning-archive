from unittest import IsolatedAsyncioTestCase, main
from server.service.exchange_rate_service import ExchangeRateService
from server.service.currency_exchange_service import CurrencyExchangeService
from unittest.mock import Mock
from datetime import date
from server.domain.domain import CurrencyExchange


class TestCurrencyExchangeService(IsolatedAsyncioTestCase):
    def setUp(self):
        self.currency_exchange_service = CurrencyExchangeService(Mock(spec=ExchangeRateService))

    async def test_get_currency_exchange(self):
        # valid target currency
        self.currency_exchange_service.exchange_rate_service.get_exchange_rate.return_value = (date(2024, 7, 4),
                                                                                               float(2098.60161591))
        self.assertEqual(
            await self.currency_exchange_service.get_currency_exchange('mmk', float(1.23456789)),
            CurrencyExchange(
                date=date(2024, 7, 4),
                source_currency='usd',
                source_currency_amount=float(1.23456789),
                target_currency='mmk',
                target_currency_amount=float(1.23456789) * float(2098.60161591)
            )
        )


if __name__ == '__main__':
    main()
