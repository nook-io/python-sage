import pprint
import six
from sage.configuration import Configuration


class PostServicesServiceSalesRates(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        "rate_name": "str",
        "rate": "float",
        "rate_includes_tax": "bool",
        "service_rate_type_id": "str",
    }
    attribute_map = {
        "rate_name": "rate_name",
        "rate": "rate",
        "rate_includes_tax": "rate_includes_tax",
        "service_rate_type_id": "service_rate_type_id",
    }

    def __init__(
        self,
        rate_name=None,
        rate=None,
        rate_includes_tax=None,
        service_rate_type_id=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._rate_name = None
        self._rate = None
        self._rate_includes_tax = None
        self._service_rate_type_id = None
        self.discriminator = None
        if rate_name is not None:
            self.rate_name = rate_name
        if rate is not None:
            self.rate = rate
        if rate_includes_tax is not None:
            self.rate_includes_tax = rate_includes_tax
        if service_rate_type_id is not None:
            self.service_rate_type_id = service_rate_type_id

    @property
    def rate_name(self):
        return self._rate_name

    @rate_name.setter
    def rate_name(self, rate_name):
        self._rate_name = rate_name

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, rate):
        self._rate = rate

    @property
    def rate_includes_tax(self):
        return self._rate_includes_tax

    @rate_includes_tax.setter
    def rate_includes_tax(self, rate_includes_tax):
        self._rate_includes_tax = rate_includes_tax

    @property
    def service_rate_type_id(self):
        return self._service_rate_type_id

    @service_rate_type_id.setter
    def service_rate_type_id(self, service_rate_type_id):
        self._service_rate_type_id = service_rate_type_id

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
        if not isinstance(other, PostServicesServiceSalesRates):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PostServicesServiceSalesRates):
            return True
        return self.to_dict() != other.to_dict()
