from simulation.create.ExchangeTransformationsStoreHandler import ExchangeTransformationsStoreHandler

if __name__ == '__main__':

    options = {
        'REDIS_SERVER_ADDRESS': '192.168.1.90',
        'REDIS_SERVER_PORT': 6379,
        'EXCHANGE_TRANSFORMATIONS_KEY': 'test:mv:transformation:exchange'
    }

    handler = ExchangeTransformationsStoreHandler(options)
    handler.store_exchange_transformations()
