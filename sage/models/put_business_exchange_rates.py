import pprint
import six
from sage.configuration import Configuration


class PutBusinessExchangeRates(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        "business_exchange_rate": "PutBusinessExchangeRatesBusinessExchangeRate"
    }
    attribute_map = {"business_exchange_rate": "business_exchange_rate"}

    def __init__(self, business_exchange_rate=None, local_vars_configuration=None):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._business_exchange_rate = None
        self.discriminator = None
        self.business_exchange_rate = business_exchange_rate

    @property
    def business_exchange_rate(self):
        return self._business_exchange_rate

    @business_exchange_rate.setter
    def business_exchange_rate(self, business_exchange_rate):
        if (
            self.local_vars_configuration.client_side_validation
            and business_exchange_rate is None
        ):
            raise ValueError(
                "Invalid value for `business_exchange_rate`, must not be `None`"
            )
        self._business_exchange_rate = business_exchange_rate

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
        if not isinstance(other, PutBusinessExchangeRates):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PutBusinessExchangeRates):
            return True
        return self.to_dict() != other.to_dict()
