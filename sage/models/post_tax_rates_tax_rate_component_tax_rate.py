import pprint
import six
from sage.configuration import Configuration


class PostTaxRatesTaxRateComponentTaxRate(object):
    openapi_types = {"name": "str", "agency": "str", "percentage": "float"}
    attribute_map = {"name": "name", "agency": "agency", "percentage": "percentage"}

    def __init__(
        self, name=None, agency=None, percentage=None, local_vars_configuration=None
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._name = None
        self._agency = None
        self._percentage = None
        self.discriminator = None
        self.name = name
        if agency is not None:
            self.agency = agency
        if percentage is not None:
            self.percentage = percentage

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if self.local_vars_configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        self._name = name

    @property
    def agency(self):
        return self._agency

    @agency.setter
    def agency(self, agency):
        self._agency = agency

    @property
    def percentage(self):
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        self._percentage = percentage

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
        if not isinstance(other, PostTaxRatesTaxRateComponentTaxRate):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PostTaxRatesTaxRateComponentTaxRate):
            return True
        return self.to_dict() != other.to_dict()
