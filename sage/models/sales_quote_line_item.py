import pprint
import six
from sage.configuration import Configuration


class SalesQuoteLineItem(object):
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
        "description": "str",
        "product": "Product",
        "service": "Service",
        "ledger_account": "Base",
        "trade_of_asset": "bool",
        "quantity": "float",
        "unit_price": "float",
        "net_amount": "float",
        "tax_rate": "Base",
        "tax_amount": "float",
        "tax_breakdown": "list[TaxBreakdown]",
        "total_amount": "float",
        "base_currency_unit_price": "float",
        "unit_price_includes_tax": "bool",
        "base_currency_net_amount": "float",
        "base_currency_tax_amount": "float",
        "base_currency_tax_breakdown": "list[TaxBreakdown]",
        "base_currency_total_amount": "float",
        "eu_goods_services_type": "Base",
        "discount_amount": "float",
        "base_currency_discount_amount": "float",
        "discount_percentage": "float",
        "eu_sales_description": "EuSalesDescription",
    }
    attribute_map = {
        "id": "id",
        "displayed_as": "displayed_as",
        "description": "description",
        "product": "product",
        "service": "service",
        "ledger_account": "ledger_account",
        "trade_of_asset": "trade_of_asset",
        "quantity": "quantity",
        "unit_price": "unit_price",
        "net_amount": "net_amount",
        "tax_rate": "tax_rate",
        "tax_amount": "tax_amount",
        "tax_breakdown": "tax_breakdown",
        "total_amount": "total_amount",
        "base_currency_unit_price": "base_currency_unit_price",
        "unit_price_includes_tax": "unit_price_includes_tax",
        "base_currency_net_amount": "base_currency_net_amount",
        "base_currency_tax_amount": "base_currency_tax_amount",
        "base_currency_tax_breakdown": "base_currency_tax_breakdown",
        "base_currency_total_amount": "base_currency_total_amount",
        "eu_goods_services_type": "eu_goods_services_type",
        "discount_amount": "discount_amount",
        "base_currency_discount_amount": "base_currency_discount_amount",
        "discount_percentage": "discount_percentage",
        "eu_sales_description": "eu_sales_description",
    }

    def __init__(
        self,
        id=None,
        displayed_as=None,
        description=None,
        product=None,
        service=None,
        ledger_account=None,
        trade_of_asset=None,
        quantity=None,
        unit_price=None,
        net_amount=None,
        tax_rate=None,
        tax_amount=None,
        tax_breakdown=None,
        total_amount=None,
        base_currency_unit_price=None,
        unit_price_includes_tax=None,
        base_currency_net_amount=None,
        base_currency_tax_amount=None,
        base_currency_tax_breakdown=None,
        base_currency_total_amount=None,
        eu_goods_services_type=None,
        discount_amount=None,
        base_currency_discount_amount=None,
        discount_percentage=None,
        eu_sales_description=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._id = None
        self._displayed_as = None
        self._description = None
        self._product = None
        self._service = None
        self._ledger_account = None
        self._trade_of_asset = None
        self._quantity = None
        self._unit_price = None
        self._net_amount = None
        self._tax_rate = None
        self._tax_amount = None
        self._tax_breakdown = None
        self._total_amount = None
        self._base_currency_unit_price = None
        self._unit_price_includes_tax = None
        self._base_currency_net_amount = None
        self._base_currency_tax_amount = None
        self._base_currency_tax_breakdown = None
        self._base_currency_total_amount = None
        self._eu_goods_services_type = None
        self._discount_amount = None
        self._base_currency_discount_amount = None
        self._discount_percentage = None
        self._eu_sales_description = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if displayed_as is not None:
            self.displayed_as = displayed_as
        if description is not None:
            self.description = description
        if product is not None:
            self.product = product
        if service is not None:
            self.service = service
        if ledger_account is not None:
            self.ledger_account = ledger_account
        if trade_of_asset is not None:
            self.trade_of_asset = trade_of_asset
        if quantity is not None:
            self.quantity = quantity
        if unit_price is not None:
            self.unit_price = unit_price
        if net_amount is not None:
            self.net_amount = net_amount
        if tax_rate is not None:
            self.tax_rate = tax_rate
        if tax_amount is not None:
            self.tax_amount = tax_amount
        if tax_breakdown is not None:
            self.tax_breakdown = tax_breakdown
        if total_amount is not None:
            self.total_amount = total_amount
        if base_currency_unit_price is not None:
            self.base_currency_unit_price = base_currency_unit_price
        if unit_price_includes_tax is not None:
            self.unit_price_includes_tax = unit_price_includes_tax
        if base_currency_net_amount is not None:
            self.base_currency_net_amount = base_currency_net_amount
        if base_currency_tax_amount is not None:
            self.base_currency_tax_amount = base_currency_tax_amount
        if base_currency_tax_breakdown is not None:
            self.base_currency_tax_breakdown = base_currency_tax_breakdown
        if base_currency_total_amount is not None:
            self.base_currency_total_amount = base_currency_total_amount
        if eu_goods_services_type is not None:
            self.eu_goods_services_type = eu_goods_services_type
        if discount_amount is not None:
            self.discount_amount = discount_amount
        if base_currency_discount_amount is not None:
            self.base_currency_discount_amount = base_currency_discount_amount
        if discount_percentage is not None:
            self.discount_percentage = discount_percentage
        if eu_sales_description is not None:
            self.eu_sales_description = eu_sales_description

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
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, product):
        self._product = product

    @property
    def service(self):
        return self._service

    @service.setter
    def service(self, service):
        self._service = service

    @property
    def ledger_account(self):
        return self._ledger_account

    @ledger_account.setter
    def ledger_account(self, ledger_account):
        self._ledger_account = ledger_account

    @property
    def trade_of_asset(self):
        return self._trade_of_asset

    @trade_of_asset.setter
    def trade_of_asset(self, trade_of_asset):
        self._trade_of_asset = trade_of_asset

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity

    @property
    def unit_price(self):
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        self._unit_price = unit_price

    @property
    def net_amount(self):
        return self._net_amount

    @net_amount.setter
    def net_amount(self, net_amount):
        self._net_amount = net_amount

    @property
    def tax_rate(self):
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, tax_rate):
        self._tax_rate = tax_rate

    @property
    def tax_amount(self):
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        self._tax_amount = tax_amount

    @property
    def tax_breakdown(self):
        return self._tax_breakdown

    @tax_breakdown.setter
    def tax_breakdown(self, tax_breakdown):
        self._tax_breakdown = tax_breakdown

    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        self._total_amount = total_amount

    @property
    def base_currency_unit_price(self):
        return self._base_currency_unit_price

    @base_currency_unit_price.setter
    def base_currency_unit_price(self, base_currency_unit_price):
        self._base_currency_unit_price = base_currency_unit_price

    @property
    def unit_price_includes_tax(self):
        return self._unit_price_includes_tax

    @unit_price_includes_tax.setter
    def unit_price_includes_tax(self, unit_price_includes_tax):
        self._unit_price_includes_tax = unit_price_includes_tax

    @property
    def base_currency_net_amount(self):
        return self._base_currency_net_amount

    @base_currency_net_amount.setter
    def base_currency_net_amount(self, base_currency_net_amount):
        self._base_currency_net_amount = base_currency_net_amount

    @property
    def base_currency_tax_amount(self):
        return self._base_currency_tax_amount

    @base_currency_tax_amount.setter
    def base_currency_tax_amount(self, base_currency_tax_amount):
        self._base_currency_tax_amount = base_currency_tax_amount

    @property
    def base_currency_tax_breakdown(self):
        return self._base_currency_tax_breakdown

    @base_currency_tax_breakdown.setter
    def base_currency_tax_breakdown(self, base_currency_tax_breakdown):
        self._base_currency_tax_breakdown = base_currency_tax_breakdown

    @property
    def base_currency_total_amount(self):
        return self._base_currency_total_amount

    @base_currency_total_amount.setter
    def base_currency_total_amount(self, base_currency_total_amount):
        self._base_currency_total_amount = base_currency_total_amount

    @property
    def eu_goods_services_type(self):
        return self._eu_goods_services_type

    @eu_goods_services_type.setter
    def eu_goods_services_type(self, eu_goods_services_type):
        self._eu_goods_services_type = eu_goods_services_type

    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        self._discount_amount = discount_amount

    @property
    def base_currency_discount_amount(self):
        return self._base_currency_discount_amount

    @base_currency_discount_amount.setter
    def base_currency_discount_amount(self, base_currency_discount_amount):
        self._base_currency_discount_amount = base_currency_discount_amount

    @property
    def discount_percentage(self):
        return self._discount_percentage

    @discount_percentage.setter
    def discount_percentage(self, discount_percentage):
        self._discount_percentage = discount_percentage

    @property
    def eu_sales_description(self):
        return self._eu_sales_description

    @eu_sales_description.setter
    def eu_sales_description(self, eu_sales_description):
        self._eu_sales_description = eu_sales_description

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
        if not isinstance(other, SalesQuoteLineItem):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, SalesQuoteLineItem):
            return True
        return self.to_dict() != other.to_dict()
