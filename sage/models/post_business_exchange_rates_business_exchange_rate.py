import pprint
import six
from sage.configuration import Configuration


class PostBusinessExchangeRatesBusinessExchangeRate(object):
    openapi_types = {
        "currency_id": "str",
        "rate": "float",
        "inverse_rate": "float",
        "base_currency_id": "str",
    }
    attribute_map = {
        "currency_id": "currency_id",
        "rate": "rate",
        "inverse_rate": "inverse_rate",
        "base_currency_id": "base_currency_id",
    }

    def __init__(
        self,
        currency_id=None,
        rate=None,
        inverse_rate=None,
        base_currency_id=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._currency_id = None
        self._rate = None
        self._inverse_rate = None
        self._base_currency_id = None
        self.discriminator = None
        self.currency_id = currency_id
        self.rate = rate
        if inverse_rate is not None:
            self.inverse_rate = inverse_rate
        if base_currency_id is not None:
            self.base_currency_id = base_currency_id

    @property
    def currency_id(self):
        return self._currency_id

    @currency_id.setter
    def currency_id(self, currency_id):
        if self.local_vars_configuration.client_side_validation and currency_id is None:
            raise ValueError("Invalid value for `currency_id`, must not be `None`")
        self._currency_id = currency_id

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, rate):
        if self.local_vars_configuration.client_side_validation and rate is None:
            raise ValueError("Invalid value for `rate`, must not be `None`")
        self._rate = rate

    @property
    def inverse_rate(self):
        return self._inverse_rate

    @inverse_rate.setter
    def inverse_rate(self, inverse_rate):
        self._inverse_rate = inverse_rate

    @property
    def base_currency_id(self):
        return self._base_currency_id

    @base_currency_id.setter
    def base_currency_id(self, base_currency_id):
        self._base_currency_id = base_currency_id

    def to_dict(self):
        result = {}
        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, PostBusinessExchangeRatesBusinessExchangeRate):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PostBusinessExchangeRatesBusinessExchangeRate):
            return True
        return self.to_dict() != other.to_dict()
