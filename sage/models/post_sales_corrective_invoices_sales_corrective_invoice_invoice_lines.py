import pprint
import six
from sage.configuration import Configuration


class PostSalesCorrectiveInvoicesSalesCorrectiveInvoiceInvoiceLines(object):
    openapi_types = {
        "description": "str",
        "product_id": "str",
        "service_id": "str",
        "ledger_account_id": "str",
        "trade_of_asset": "bool",
        "quantity": "float",
        "unit_price": "float",
        "net_amount": "float",
        "tax_rate_id": "str",
        "tax_amount": "float",
        "total_amount": "float",
        "base_currency_unit_price": "float",
        "unit_price_includes_tax": "bool",
        "base_currency_net_amount": "float",
        "base_currency_tax_amount": "float",
        "base_currency_total_amount": "float",
        "eu_goods_services_type_id": "str",
        "discount_amount": "float",
        "base_currency_discount_amount": "float",
        "discount_percentage": "float",
        "eu_sales_description_id": "str",
    }
    attribute_map = {
        "description": "description",
        "product_id": "product_id",
        "service_id": "service_id",
        "ledger_account_id": "ledger_account_id",
        "trade_of_asset": "trade_of_asset",
        "quantity": "quantity",
        "unit_price": "unit_price",
        "net_amount": "net_amount",
        "tax_rate_id": "tax_rate_id",
        "tax_amount": "tax_amount",
        "total_amount": "total_amount",
        "base_currency_unit_price": "base_currency_unit_price",
        "unit_price_includes_tax": "unit_price_includes_tax",
        "base_currency_net_amount": "base_currency_net_amount",
        "base_currency_tax_amount": "base_currency_tax_amount",
        "base_currency_total_amount": "base_currency_total_amount",
        "eu_goods_services_type_id": "eu_goods_services_type_id",
        "discount_amount": "discount_amount",
        "base_currency_discount_amount": "base_currency_discount_amount",
        "discount_percentage": "discount_percentage",
        "eu_sales_description_id": "eu_sales_description_id",
    }

    def __init__(
        self,
        description=None,
        product_id=None,
        service_id=None,
        ledger_account_id=None,
        trade_of_asset=None,
        quantity=None,
        unit_price=None,
        net_amount=None,
        tax_rate_id=None,
        tax_amount=None,
        total_amount=None,
        base_currency_unit_price=None,
        unit_price_includes_tax=None,
        base_currency_net_amount=None,
        base_currency_tax_amount=None,
        base_currency_total_amount=None,
        eu_goods_services_type_id=None,
        discount_amount=None,
        base_currency_discount_amount=None,
        discount_percentage=None,
        eu_sales_description_id=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._description = None
        self._product_id = None
        self._service_id = None
        self._ledger_account_id = None
        self._trade_of_asset = None
        self._quantity = None
        self._unit_price = None
        self._net_amount = None
        self._tax_rate_id = None
        self._tax_amount = None
        self._total_amount = None
        self._base_currency_unit_price = None
        self._unit_price_includes_tax = None
        self._base_currency_net_amount = None
        self._base_currency_tax_amount = None
        self._base_currency_total_amount = None
        self._eu_goods_services_type_id = None
        self._discount_amount = None
        self._base_currency_discount_amount = None
        self._discount_percentage = None
        self._eu_sales_description_id = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if product_id is not None:
            self.product_id = product_id
        if service_id is not None:
            self.service_id = service_id
        if ledger_account_id is not None:
            self.ledger_account_id = ledger_account_id
        if trade_of_asset is not None:
            self.trade_of_asset = trade_of_asset
        if quantity is not None:
            self.quantity = quantity
        if unit_price is not None:
            self.unit_price = unit_price
        if net_amount is not None:
            self.net_amount = net_amount
        if tax_rate_id is not None:
            self.tax_rate_id = tax_rate_id
        if tax_amount is not None:
            self.tax_amount = tax_amount
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
        if base_currency_total_amount is not None:
            self.base_currency_total_amount = base_currency_total_amount
        if eu_goods_services_type_id is not None:
            self.eu_goods_services_type_id = eu_goods_services_type_id
        if discount_amount is not None:
            self.discount_amount = discount_amount
        if base_currency_discount_amount is not None:
            self.base_currency_discount_amount = base_currency_discount_amount
        if discount_percentage is not None:
            self.discount_percentage = discount_percentage
        if eu_sales_description_id is not None:
            self.eu_sales_description_id = eu_sales_description_id

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        self._product_id = product_id

    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        self._service_id = service_id

    @property
    def ledger_account_id(self):
        return self._ledger_account_id

    @ledger_account_id.setter
    def ledger_account_id(self, ledger_account_id):
        self._ledger_account_id = ledger_account_id

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
    def tax_rate_id(self):
        return self._tax_rate_id

    @tax_rate_id.setter
    def tax_rate_id(self, tax_rate_id):
        self._tax_rate_id = tax_rate_id

    @property
    def tax_amount(self):
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        self._tax_amount = tax_amount

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
    def base_currency_total_amount(self):
        return self._base_currency_total_amount

    @base_currency_total_amount.setter
    def base_currency_total_amount(self, base_currency_total_amount):
        self._base_currency_total_amount = base_currency_total_amount

    @property
    def eu_goods_services_type_id(self):
        return self._eu_goods_services_type_id

    @eu_goods_services_type_id.setter
    def eu_goods_services_type_id(self, eu_goods_services_type_id):
        self._eu_goods_services_type_id = eu_goods_services_type_id

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
    def eu_sales_description_id(self):
        return self._eu_sales_description_id

    @eu_sales_description_id.setter
    def eu_sales_description_id(self, eu_sales_description_id):
        self._eu_sales_description_id = eu_sales_description_id

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
        if not isinstance(
            other, PostSalesCorrectiveInvoicesSalesCorrectiveInvoiceInvoiceLines
        ):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(
            other, PostSalesCorrectiveInvoicesSalesCorrectiveInvoiceInvoiceLines
        ):
            return True
        return self.to_dict() != other.to_dict()
