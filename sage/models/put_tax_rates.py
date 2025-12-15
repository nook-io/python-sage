import pprint
import six
from sage.configuration import Configuration


class PutTaxRates(object):
    openapi_types = {"tax_rate": "PutTaxRatesTaxRate"}
    attribute_map = {"tax_rate": "tax_rate"}

    def __init__(self, tax_rate=None, local_vars_configuration=None):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._tax_rate = None
        self.discriminator = None
        self.tax_rate = tax_rate

    @property
    def tax_rate(self):
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, tax_rate):
        if self.local_vars_configuration.client_side_validation and tax_rate is None:
            raise ValueError("Invalid value for `tax_rate`, must not be `None`")
        self._tax_rate = tax_rate

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
        if not isinstance(other, PutTaxRates):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PutTaxRates):
            return True
        return self.to_dict() != other.to_dict()
