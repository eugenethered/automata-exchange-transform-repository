import logging
import unittest

from cache.holder.RedisCacheHolder import RedisCacheHolder
from cache.provider.RedisCacheProviderWithHash import RedisCacheProviderWithHash

from exchangetransformrepo.ExchangeTransform import ExchangeTransform
from exchangetransformrepo.repository.ExchangeTransformRepository import ExchangeTransformRepository


class ExchangeTransformRepositoryTestCase(unittest.TestCase):

    def setUp(self) -> None:
        logging.basicConfig(level=logging.INFO)
        logging.getLogger('ExchangeTransformRepository').setLevel(logging.DEBUG)

        options = {
            'REDIS_SERVER_ADDRESS': '192.168.1.90',
            'REDIS_SERVER_PORT': 6379,
            'EXCHANGE_TRANSFORMATIONS_KEY': 'test:transformation:exchange'
        }
        self.cache = RedisCacheHolder(options, held_type=RedisCacheProviderWithHash)
        self.repository = ExchangeTransformRepository(options)

    def tearDown(self):
        self.cache.delete('test:transformation:exchange')

    def test_should_store_and_retrieve_exchange_transform(self):
        exchange_transform = ExchangeTransform('BTCOTC', {
            'instruments': 'BTC/OTC'
        })
        self.repository.create(exchange_transform)
        stored_exchange_transformations = self.repository.retrieve()
        self.assertEqual(exchange_transform, stored_exchange_transformations[0])

    def test_should_store_and_retrieve_exchange_ignore_transform(self):
        exchange_transform = ExchangeTransform('BTCOTC')
        exchange_transform.ignore = True
        self.repository.create(exchange_transform)
        stored_exchange_transformations = self.repository.retrieve()
        self.assertEqual(exchange_transform, stored_exchange_transformations[0])

    def test_should_store_and_retrieve_multiple_exchange_transformations(self):
        exchange_transform_1 = ExchangeTransform('BTCOTC', {
            'instruments': 'BTC/OTC'
        })
        exchange_transform_2 = ExchangeTransform('ETHOTC', {
            'instruments': 'ETH/OTC'
        })
        exchange_transform_2.ignore = True
        exchange_transform_3 = ExchangeTransform('GBPOTC')
        exchange_transform_3.ignore = True
        exchange_transformations = [exchange_transform_1, exchange_transform_2, exchange_transform_3]
        self.repository.store(exchange_transformations)
        stored_exchange_transformations = self.repository.retrieve()
        # sort to compare
        exchange_transformations.sort(key=lambda e: e.instrument)
        stored_exchange_transformations.sort(key=lambda e: e.instrument)
        self.assertEqual(exchange_transformations, stored_exchange_transformations)


if __name__ == '__main__':
    unittest.main()
