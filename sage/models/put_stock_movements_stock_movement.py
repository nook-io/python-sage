import pprint
import six
from sage.configuration import Configuration


class PutStockMovementsStockMovement(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        "stock_item_id": "str",
        "date": "date",
        "quantity": "float",
        "cost_price": "float",
        "details": "str",
        "movement_number": "str",
        "reference": "str",
    }
    attribute_map = {
        "stock_item_id": "stock_item_id",
        "date": "date",
        "quantity": "quantity",
        "cost_price": "cost_price",
        "details": "details",
        "movement_number": "movement_number",
        "reference": "reference",
    }

    def __init__(
        self,
        stock_item_id=None,
        date=None,
        quantity=None,
        cost_price=None,
        details=None,
        movement_number=None,
        reference=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._stock_item_id = None
        self._date = None
        self._quantity = None
        self._cost_price = None
        self._details = None
        self._movement_number = None
        self._reference = None
        self.discriminator = None
        if stock_item_id is not None:
            self.stock_item_id = stock_item_id
        if date is not None:
            self.date = date
        if quantity is not None:
            self.quantity = quantity
        if cost_price is not None:
            self.cost_price = cost_price
        if details is not None:
            self.details = details
        if movement_number is not None:
            self.movement_number = movement_number
        if reference is not None:
            self.reference = reference

    @property
    def stock_item_id(self):
        return self._stock_item_id

    @stock_item_id.setter
    def stock_item_id(self, stock_item_id):
        self._stock_item_id = stock_item_id

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity

    @property
    def cost_price(self):
        return self._cost_price

    @cost_price.setter
    def cost_price(self, cost_price):
        self._cost_price = cost_price

    @property
    def details(self):
        return self._details

    @details.setter
    def details(self, details):
        self._details = details

    @property
    def movement_number(self):
        return self._movement_number

    @movement_number.setter
    def movement_number(self, movement_number):
        self._movement_number = movement_number

    @property
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, reference):
        self._reference = reference

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
        if not isinstance(other, PutStockMovementsStockMovement):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PutStockMovementsStockMovement):
            return True
        return self.to_dict() != other.to_dict()
