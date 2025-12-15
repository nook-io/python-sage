import pprint
import six
from sage.configuration import Configuration


class PostSalesQuickEntries(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {"sales_quick_entry": "PostSalesQuickEntriesSalesQuickEntry"}
    attribute_map = {"sales_quick_entry": "sales_quick_entry"}

    def __init__(self, sales_quick_entry=None, local_vars_configuration=None):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._sales_quick_entry = None
        self.discriminator = None
        self.sales_quick_entry = sales_quick_entry

    @property
    def sales_quick_entry(self):
        return self._sales_quick_entry

    @sales_quick_entry.setter
    def sales_quick_entry(self, sales_quick_entry):
        if (
            self.local_vars_configuration.client_side_validation
            and sales_quick_entry is None
        ):
            raise ValueError(
                "Invalid value for `sales_quick_entry`, must not be `None`"
            )
        self._sales_quick_entry = sales_quick_entry

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
        if not isinstance(other, PostSalesQuickEntries):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PostSalesQuickEntries):
            return True
        return self.to_dict() != other.to_dict()
