import pprint
import six
from sage.configuration import Configuration


class PostPurchaseQuickEntries(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        "purchase_quick_entry": "PostPurchaseQuickEntriesPurchaseQuickEntry"
    }
    attribute_map = {"purchase_quick_entry": "purchase_quick_entry"}

    def __init__(self, purchase_quick_entry=None, local_vars_configuration=None):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._purchase_quick_entry = None
        self.discriminator = None
        self.purchase_quick_entry = purchase_quick_entry

    @property
    def purchase_quick_entry(self):
        return self._purchase_quick_entry

    @purchase_quick_entry.setter
    def purchase_quick_entry(self, purchase_quick_entry):
        if (
            self.local_vars_configuration.client_side_validation
            and purchase_quick_entry is None
        ):
            raise ValueError(
                "Invalid value for `purchase_quick_entry`, must not be `None`"
            )
        self._purchase_quick_entry = purchase_quick_entry

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
        if not isinstance(other, PostPurchaseQuickEntries):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PostPurchaseQuickEntries):
            return True
        return self.to_dict() != other.to_dict()
