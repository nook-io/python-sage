import pprint
import six
from sage.configuration import Configuration


class PostProductsProductSalesPrices(object):
    openapi_types = {
        "price_name": "str",
        "price": "float",
        "price_includes_tax": "bool",
        "product_sales_price_type_id": "str",
    }
    attribute_map = {
        "price_name": "price_name",
        "price": "price",
        "price_includes_tax": "price_includes_tax",
        "product_sales_price_type_id": "product_sales_price_type_id",
    }

    def __init__(
        self,
        price_name=None,
        price=None,
        price_includes_tax=None,
        product_sales_price_type_id=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._price_name = None
        self._price = None
        self._price_includes_tax = None
        self._product_sales_price_type_id = None
        self.discriminator = None
        if price_name is not None:
            self.price_name = price_name
        if price is not None:
            self.price = price
        if price_includes_tax is not None:
            self.price_includes_tax = price_includes_tax
        if product_sales_price_type_id is not None:
            self.product_sales_price_type_id = product_sales_price_type_id

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
    def product_sales_price_type_id(self):
        return self._product_sales_price_type_id

    @product_sales_price_type_id.setter
    def product_sales_price_type_id(self, product_sales_price_type_id):
        self._product_sales_price_type_id = product_sales_price_type_id

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
        if not isinstance(other, PostProductsProductSalesPrices):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PostProductsProductSalesPrices):
            return True
        return self.to_dict() != other.to_dict()
