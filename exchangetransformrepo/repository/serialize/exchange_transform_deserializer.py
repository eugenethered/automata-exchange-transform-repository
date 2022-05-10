from utility.json_utility import as_data

from exchangetransformrepo.ExchangeTransform import ExchangeTransform


def deserialize_exchange_transform(exchange_transform) -> ExchangeTransform:
    instrument = as_data(exchange_transform, 'instrument')
    transform = as_data(exchange_transform, 'transform')
    ignore = as_data(exchange_transform, 'ignore', False)
    deserialized = ExchangeTransform(instrument, transform)
    if ignore:
        deserialized.ignore = ignore
    return deserialized