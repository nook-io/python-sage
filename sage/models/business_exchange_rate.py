import pprint
import six
from sage.configuration import Configuration


class BusinessExchangeRate(object):
    openapi_types = {
        "displayed_as": "str",
        "path": "str",
        "created_at": "datetime",
        "updated_at": "datetime",
        "rate": "float",
        "inverse_rate": "float",
        "base_currency": "Base",
        "currency": "Base",
    }
    attribute_map = {
        "displayed_as": "displayed_as",
        "path": "$path",
        "created_at": "created_at",
        "updated_at": "updated_at",
        "rate": "rate",
        "inverse_rate": "inverse_rate",
        "base_currency": "base_currency",
        "currency": "currency",
    }

    def __init__(
        self,
        displayed_as=None,
        path=None,
        created_at=None,
        updated_at=None,
        rate=None,
        inverse_rate=None,
        base_currency=None,
        currency=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._displayed_as = None
        self._path = None
        self._created_at = None
        self._updated_at = None
        self._rate = None
        self._inverse_rate = None
        self._base_currency = None
        self._currency = None
        self.discriminator = None
        if displayed_as is not None:
            self.displayed_as = displayed_as
        if path is not None:
            self.path = path
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if rate is not None:
            self.rate = rate
        if inverse_rate is not None:
            self.inverse_rate = inverse_rate
        if base_currency is not None:
            self.base_currency = base_currency
        if currency is not None:
            self.currency = currency

    @property
    def displayed_as(self):
        return self._displayed_as

    @displayed_as.setter
    def displayed_as(self, displayed_as):
        self._displayed_as = displayed_as

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path):
        self._path = path

    @property
    def created_at(self):
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        self._created_at = created_at

    @property
    def updated_at(self):
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        self._updated_at = updated_at

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, rate):
        self._rate = rate

    @property
    def inverse_rate(self):
        return self._inverse_rate

    @inverse_rate.setter
    def inverse_rate(self, inverse_rate):
        self._inverse_rate = inverse_rate

    @property
    def base_currency(self):
        return self._base_currency

    @base_currency.setter
    def base_currency(self, base_currency):
        self._base_currency = base_currency

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, currency):
        self._currency = currency

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
        if not isinstance(other, BusinessExchangeRate):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, BusinessExchangeRate):
            return True
        return self.to_dict() != other.to_dict()
