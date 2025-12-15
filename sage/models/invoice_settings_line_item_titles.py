import pprint
import six
from sage.configuration import Configuration


class InvoiceSettingsLineItemTitles(object):
    openapi_types = {
        "description": "str",
        "unit_price": "str",
        "quantity": "str",
        "discount": "str",
    }
    attribute_map = {
        "description": "description",
        "unit_price": "unit_price",
        "quantity": "quantity",
        "discount": "discount",
    }

    def __init__(
        self,
        description=None,
        unit_price=None,
        quantity=None,
        discount=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._description = None
        self._unit_price = None
        self._quantity = None
        self._discount = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if unit_price is not None:
            self.unit_price = unit_price
        if quantity is not None:
            self.quantity = quantity
        if discount is not None:
            self.discount = discount

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def unit_price(self):
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        self._unit_price = unit_price

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount):
        self._discount = discount

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
        if not isinstance(other, InvoiceSettingsLineItemTitles):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, InvoiceSettingsLineItemTitles):
            return True
        return self.to_dict() != other.to_dict()
