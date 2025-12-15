import pprint
import six
from sage.configuration import Configuration


class SalesPrice(object):
    openapi_types = {
        "id": "str",
        "displayed_as": "str",
        "created_at": "datetime",
        "updated_at": "datetime",
        "price_name": "str",
        "price": "float",
        "price_includes_tax": "bool",
        "product_sales_price_type": "Base",
    }
    attribute_map = {
        "id": "id",
        "displayed_as": "displayed_as",
        "created_at": "created_at",
        "updated_at": "updated_at",
        "price_name": "price_name",
        "price": "price",
        "price_includes_tax": "price_includes_tax",
        "product_sales_price_type": "product_sales_price_type",
    }

    def __init__(
        self,
        id=None,
        displayed_as=None,
        created_at=None,
        updated_at=None,
        price_name=None,
        price=None,
        price_includes_tax=None,
        product_sales_price_type=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._id = None
        self._displayed_as = None
        self._created_at = None
        self._updated_at = None
        self._price_name = None
        self._price = None
        self._price_includes_tax = None
        self._product_sales_price_type = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if displayed_as is not None:
            self.displayed_as = displayed_as
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if price_name is not None:
            self.price_name = price_name
        if price is not None:
            self.price = price
        if price_includes_tax is not None:
            self.price_includes_tax = price_includes_tax
        if product_sales_price_type is not None:
            self.product_sales_price_type = product_sales_price_type

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
    def price_name(self):
        return self._price_name

    @price_name.setter
    def price_name(self, price_name):
        self._price_name = price_name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    @property
    def price_includes_tax(self):
        return self._price_includes_tax

    @price_includes_tax.setter
    def price_includes_tax(self, price_includes_tax):
        self._price_includes_tax = price_includes_tax

    @property
    def product_sales_price_type(self):
        return self._product_sales_price_type

    @product_sales_price_type.setter
    def product_sales_price_type(self, product_sales_price_type):
        self._product_sales_price_type = product_sales_price_type

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
        if not isinstance(other, SalesPrice):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, SalesPrice):
            return True
        return self.to_dict() != other.to_dict()
