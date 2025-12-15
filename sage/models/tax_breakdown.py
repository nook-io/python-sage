import pprint
import six
from sage.configuration import Configuration


class TaxBreakdown(object):
    openapi_types = {"tax_rate": "Base", "percentage": "float", "amount": "float"}
    attribute_map = {
        "tax_rate": "tax_rate",
        "percentage": "percentage",
        "amount": "amount",
    }

    def __init__(
        self, tax_rate=None, percentage=None, amount=None, local_vars_configuration=None
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._tax_rate = None
        self._percentage = None
        self._amount = None
        self.discriminator = None
        if tax_rate is not None:
            self.tax_rate = tax_rate
        if percentage is not None:
            self.percentage = percentage
        if amount is not None:
            self.amount = amount

    @property
    def tax_rate(self):
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, tax_rate):
        self._tax_rate = tax_rate

    @property
    def percentage(self):
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        self._percentage = percentage

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

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
        if not isinstance(other, TaxBreakdown):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, TaxBreakdown):
            return True
        return self.to_dict() != other.to_dict()
