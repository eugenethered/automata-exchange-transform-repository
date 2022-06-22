from cache.holder.RedisCacheHolder import RedisCacheHolder
from cache.provider.RedisCacheProviderWithHash import RedisCacheProviderWithHash

from exchangetransformrepo.ExchangeTransform import ExchangeTransform
from exchangetransformrepo.repository.ExchangeTransformRepository import ExchangeTransformRepository


class ExchangeTransformationsStoreHandler:

    def __init__(self, options):
        RedisCacheHolder(options, held_type=RedisCacheProviderWithHash)
        self.repository = ExchangeTransformRepository(options)

    @staticmethod
    def obtain_exchange_transformations():
        return [
            ExchangeTransform('BTCOTC', {
                    'instruments': 'BTC/OTC'
            }),
            ExchangeTransform('OTCBTC', {
                    'instruments': 'OTC/BTC'
            }),
            ExchangeTransform('OTCUSDT', ignore=True)
        ]

    def store_exchange_transformations(self):
        exchange_transformations = self.obtain_exchange_transformations()
        self.repository.store(exchange_transformations)
        print(f'Stored [{len(exchange_transformations)}] exchange transformation')
