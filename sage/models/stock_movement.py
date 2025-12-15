import pprint
import six
from sage.configuration import Configuration


class StockMovement(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        "id": "str",
        "displayed_as": "str",
        "path": "str",
        "links": "list[Link]",
        "created_at": "datetime",
        "updated_at": "datetime",
        "movement_number": "str",
        "date": "date",
        "cost_price": "float",
        "quantity": "float",
        "details": "str",
        "reference": "str",
        "stock_item": "StockItem",
    }
    attribute_map = {
        "id": "id",
        "displayed_as": "displayed_as",
        "path": "$path",
        "links": "links",
        "created_at": "created_at",
        "updated_at": "updated_at",
        "movement_number": "movement_number",
        "date": "date",
        "cost_price": "cost_price",
        "quantity": "quantity",
        "details": "details",
        "reference": "reference",
        "stock_item": "stock_item",
    }

    def __init__(
        self,
        id=None,
        displayed_as=None,
        path=None,
        links=None,
        created_at=None,
        updated_at=None,
        movement_number=None,
        date=None,
        cost_price=None,
        quantity=None,
        details=None,
        reference=None,
        stock_item=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._id = None
        self._displayed_as = None
        self._path = None
        self._links = None
        self._created_at = None
        self._updated_at = None
        self._movement_number = None
        self._date = None
        self._cost_price = None
        self._quantity = None
        self._details = None
        self._reference = None
        self._stock_item = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if displayed_as is not None:
            self.displayed_as = displayed_as
        if path is not None:
            self.path = path
        if links is not None:
            self.links = links
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if movement_number is not None:
            self.movement_number = movement_number
        if date is not None:
            self.date = date
        if cost_price is not None:
            self.cost_price = cost_price
        if quantity is not None:
            self.quantity = quantity
        if details is not None:
            self.details = details
        if reference is not None:
            self.reference = reference
        if stock_item is not None:
            self.stock_item = stock_item

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

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
    def links(self):
        return self._links

    @links.setter
    def links(self, links):
        self._links = links

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
    def movement_number(self):
        return self._movement_number

    @movement_number.setter
    def movement_number(self, movement_number):
        if (
            self.local_vars_configuration.client_side_validation
            and movement_number is not None
            and len(movement_number) > 4
        ):
            raise ValueError(
                "Invalid value for `movement_number`, length must be less than or equal to `4`"
            )
        self._movement_number = movement_number

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

    @property
    def cost_price(self):
        return self._cost_price

    @cost_price.setter
    def cost_price(self, cost_price):
        self._cost_price = cost_price

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity

    @property
    def details(self):
        return self._details

    @details.setter
    def details(self, details):
        if (
            self.local_vars_configuration.client_side_validation
            and details is not None
            and len(details) > 50
        ):
            raise ValueError(
                "Invalid value for `details`, length must be less than or equal to `50`"
            )
        self._details = details

    @property
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, reference):
        if (
            self.local_vars_configuration.client_side_validation
            and reference is not None
            and len(reference) > 31
        ):
            raise ValueError(
                "Invalid value for `reference`, length must be less than or equal to `31`"
            )
        self._reference = reference

    @property
    def stock_item(self):
        return self._stock_item

    @stock_item.setter
    def stock_item(self, stock_item):
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
        if not isinstance(other, StockMovement):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, StockMovement):
            return True
        return self.to_dict() != other.to_dict()
