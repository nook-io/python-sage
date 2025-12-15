import pprint
import six
from sage.configuration import Configuration


class PostTaxRatesTaxRate(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        "name": "str",
        "agency": "str",
        "is_visible": "bool",
        "component_tax_rate": "list[PostTaxRatesTaxRateComponentTaxRate]",
    }
    attribute_map = {
        "name": "name",
        "agency": "agency",
        "is_visible": "is_visible",
        "component_tax_rate": "component_tax_rate",
    }

    def __init__(
        self,
        name=None,
        agency=None,
        is_visible=None,
        component_tax_rate=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._name = None
        self._agency = None
        self._is_visible = None
        self._component_tax_rate = None
        self.discriminator = None
        self.name = name
        if agency is not None:
            self.agency = agency
        if is_visible is not None:
            self.is_visible = is_visible
        if component_tax_rate is not None:
            self.component_tax_rate = component_tax_rate

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
    def is_visible(self):
        return self._is_visible

    @is_visible.setter
    def is_visible(self, is_visible):
        self._is_visible = is_visible

    @property
    def component_tax_rate(self):
        return self._component_tax_rate

    @component_tax_rate.setter
    def component_tax_rate(self, component_tax_rate):
        self._component_tax_rate = component_tax_rate

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
        if not isinstance(other, PostTaxRatesTaxRate):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PostTaxRatesTaxRate):
            return True
        return self.to_dict() != other.to_dict()
