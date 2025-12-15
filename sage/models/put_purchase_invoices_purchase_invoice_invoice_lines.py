import pprint
import six
from sage.configuration import Configuration


class PutPurchaseInvoicesPurchaseInvoiceInvoiceLines(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        "description": "str",
        "ledger_account_id": "str",
        "quantity": "float",
        "unit_price": "float",
        "is_purchase_for_resale": "bool",
        "product_id": "str",
        "service_id": "str",
        "trade_of_asset": "bool",
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
        "gst_amount": "float",
        "pst_amount": "float",
        "tax_recoverable": "bool",
    }
    attribute_map = {
        "description": "description",
        "ledger_account_id": "ledger_account_id",
        "quantity": "quantity",
        "unit_price": "unit_price",
        "is_purchase_for_resale": "is_purchase_for_resale",
        "product_id": "product_id",
        "service_id": "service_id",
        "trade_of_asset": "trade_of_asset",
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
        "gst_amount": "gst_amount",
        "pst_amount": "pst_amount",
        "tax_recoverable": "tax_recoverable",
    }

    def __init__(
        self,
        description=None,
        ledger_account_id=None,
        quantity=None,
        unit_price=None,
        is_purchase_for_resale=None,
        product_id=None,
        service_id=None,
        trade_of_asset=None,
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
        gst_amount=None,
        pst_amount=None,
        tax_recoverable=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._description = None
        self._ledger_account_id = None
        self._quantity = None
        self._unit_price = None
        self._is_purchase_for_resale = None
        self._product_id = None
        self._service_id = None
        self._trade_of_asset = None
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
        self._gst_amount = None
        self._pst_amount = None
        self._tax_recoverable = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if ledger_account_id is not None:
            self.ledger_account_id = ledger_account_id
        if quantity is not None:
            self.quantity = quantity
        if unit_price is not None:
            self.unit_price = unit_price
        if is_purchase_for_resale is not None:
            self.is_purchase_for_resale = is_purchase_for_resale
        if product_id is not None:
            self.product_id = product_id
        if service_id is not None:
            self.service_id = service_id
        if trade_of_asset is not None:
            self.trade_of_asset = trade_of_asset
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
        if gst_amount is not None:
            self.gst_amount = gst_amount
        if pst_amount is not None:
            self.pst_amount = pst_amount
        if tax_recoverable is not None:
            self.tax_recoverable = tax_recoverable

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def ledger_account_id(self):
        return self._ledger_account_id

    @ledger_account_id.setter
    def ledger_account_id(self, ledger_account_id):
        self._ledger_account_id = ledger_account_id

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
    def is_purchase_for_resale(self):
        return self._is_purchase_for_resale

    @is_purchase_for_resale.setter
    def is_purchase_for_resale(self, is_purchase_for_resale):
        self._is_purchase_for_resale = is_purchase_for_resale

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
    def trade_of_asset(self):
        return self._trade_of_asset

    @trade_of_asset.setter
    def trade_of_asset(self, trade_of_asset):
        self._trade_of_asset = trade_of_asset

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
    def gst_amount(self):
        return self._gst_amount

    @gst_amount.setter
    def gst_amount(self, gst_amount):
        self._gst_amount = gst_amount

    @property
    def pst_amount(self):
        return self._pst_amount

    @pst_amount.setter
    def pst_amount(self, pst_amount):
        self._pst_amount = pst_amount

    @property
    def tax_recoverable(self):
        return self._tax_recoverable

    @tax_recoverable.setter
    def tax_recoverable(self, tax_recoverable):
        self._tax_recoverable = tax_recoverable

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
        if not isinstance(other, PutPurchaseInvoicesPurchaseInvoiceInvoiceLines):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PutPurchaseInvoicesPurchaseInvoiceInvoiceLines):
            return True
        return self.to_dict() != other.to_dict()
