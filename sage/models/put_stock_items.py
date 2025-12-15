import pprint
import six
from sage.configuration import Configuration


class PutStockItems(object):
    openapi_types = {"stock_item": "PutStockItemsStockItem"}
    attribute_map = {"stock_item": "stock_item"}

    def __init__(self, stock_item=None, local_vars_configuration=None):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._stock_item = None
        self.discriminator = None
        self.stock_item = stock_item

    @property
    def stock_item(self):
        return self._stock_item

    @stock_item.setter
    def stock_item(self, stock_item):
        if self.local_vars_configuration.client_side_validation and stock_item is None:
            raise ValueError("Invalid value for `stock_item`, must not be `None`")
        self._stock_item = stock_item

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
        if not isinstance(other, PutStockItems):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PutStockItems):
            return True
        return self.to_dict() != other.to_dict()
