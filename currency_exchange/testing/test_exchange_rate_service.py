from unittest import IsolatedAsyncioTestCase, main
from server.service.exchange_rate_service import ExchangeRateService, ExchangeRateServiceException
from unittest.mock import patch
from datetime import date


class TestExchangeRateService(IsolatedAsyncioTestCase):
    def setUp(self):
        self.exchange_rate_service = ExchangeRateService()

    async def test_get_exchange_rate(self):
        with patch('server.service.exchange_rate_service.ExchangeRateService._fetch_exchange_rates_from_api') as m:
            m.return_value = {
                'date': '2024-07-04',
                'usd': {
                    'jpy': 161.42251688,
                    'mmk': 2098.60161591
                }
            }

            # valid target currency
            self.assertEqual(
                await self.exchange_rate_service.get_exchange_rate('mmk'),
                (date(2024, 7, 4), float(2098.60161591))
            )

            # invalid target currency
            with self.assertRaises(ExchangeRateServiceException) as e:
                await self.exchange_rate_service.get_exchange_rate('unsupported_currency')
                self.assertEqual(
                    e.exception.message,
                    'target currency not found'
                )


if __name__ == '__main__':
    main()
