# coding: utf-8

"""
    Sage Business Cloud Accounting - Accounts

    Documentation of the Sage Business Cloud Accounting API.  # noqa: E501

    The version of the OpenAPI document: 3.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from sage.configuration import Configuration


class PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'description': 'str',
        'ledger_account_id': 'str',
        'quantity': 'float',
        'unit_price': 'float',
        'is_purchase_for_resale': 'bool',
        'product_id': 'str',
        'service_id': 'str',
        'trade_of_asset': 'bool',
        'net_amount': 'float',
        'tax_rate_id': 'str',
        'tax_amount': 'float',
        'total_amount': 'float',
        'base_currency_unit_price': 'float',
        'unit_price_includes_tax': 'bool',
        'base_currency_net_amount': 'float',
        'base_currency_tax_amount': 'float',
        'base_currency_total_amount': 'float',
        'eu_goods_services_type_id': 'str',
        'gst_amount': 'float',
        'pst_amount': 'float',
        'tax_recoverable': 'bool'
    }

    attribute_map = {
        'description': 'description',
        'ledger_account_id': 'ledger_account_id',
        'quantity': 'quantity',
        'unit_price': 'unit_price',
        'is_purchase_for_resale': 'is_purchase_for_resale',
        'product_id': 'product_id',
        'service_id': 'service_id',
        'trade_of_asset': 'trade_of_asset',
        'net_amount': 'net_amount',
        'tax_rate_id': 'tax_rate_id',
        'tax_amount': 'tax_amount',
        'total_amount': 'total_amount',
        'base_currency_unit_price': 'base_currency_unit_price',
        'unit_price_includes_tax': 'unit_price_includes_tax',
        'base_currency_net_amount': 'base_currency_net_amount',
        'base_currency_tax_amount': 'base_currency_tax_amount',
        'base_currency_total_amount': 'base_currency_total_amount',
        'eu_goods_services_type_id': 'eu_goods_services_type_id',
        'gst_amount': 'gst_amount',
        'pst_amount': 'pst_amount',
        'tax_recoverable': 'tax_recoverable'
    }

    def __init__(self, description=None, ledger_account_id=None, quantity=None, unit_price=None, is_purchase_for_resale=None, product_id=None, service_id=None, trade_of_asset=None, net_amount=None, tax_rate_id=None, tax_amount=None, total_amount=None, base_currency_unit_price=None, unit_price_includes_tax=None, base_currency_net_amount=None, base_currency_tax_amount=None, base_currency_total_amount=None, eu_goods_services_type_id=None, gst_amount=None, pst_amount=None, tax_recoverable=None, local_vars_configuration=None):  # noqa: E501
        """PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines - a model defined in OpenAPI"""  # noqa: E501
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
        """Gets the description of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501

        The description for the credit note line  # noqa: E501

        :return: The description of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.

        The description for the credit note line  # noqa: E501

        :param description: The description of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def ledger_account_id(self):
        """Gets the ledger_account_id of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501

        The ID of the Ledger Account.  # noqa: E501

        :return: The ledger_account_id of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501
        :rtype: str
        """
        return self._ledger_account_id

    @ledger_account_id.setter
    def ledger_account_id(self, ledger_account_id):
        """Sets the ledger_account_id of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.

        The ID of the Ledger Account.  # noqa: E501

        :param ledger_account_id: The ledger_account_id of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501
        :type: str
        """

        self._ledger_account_id = ledger_account_id

    @property
    def quantity(self):
        """Gets the quantity of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501

        The quantity for the credit note line  # noqa: E501

        :return: The quantity of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.

        The quantity for the credit note line  # noqa: E501

        :param quantity: The quantity of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501
        :type: float
        """

        self._quantity = quantity

    @property
    def unit_price(self):
        """Gets the unit_price of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501

        The unit price for the credit note line  # noqa: E501

        :return: The unit_price of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501
        :rtype: float
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """Sets the unit_price of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.

        The unit price for the credit note line  # noqa: E501

        :param unit_price: The unit_price of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501
        :type: float
        """

        self._unit_price = unit_price

    @property
    def is_purchase_for_resale(self):
        """Gets the is_purchase_for_resale of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501

        Identifies whether the line item is for resale. (Ireland Only)  # noqa: E501

        :return: The is_purchase_for_resale of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501
        :rtype: bool
        """
        return self._is_purchase_for_resale

    @is_purchase_for_resale.setter
    def is_purchase_for_resale(self, is_purchase_for_resale):
        """Sets the is_purchase_for_resale of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.

        Identifies whether the line item is for resale. (Ireland Only)  # noqa: E501

        :param is_purchase_for_resale: The is_purchase_for_resale of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501
        :type: bool
        """

        self._is_purchase_for_resale = is_purchase_for_resale

    @property
    def product_id(self):
        """Gets the product_id of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501

        The ID of the Product.  # noqa: E501

        :return: The product_id of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.

        The ID of the Product.  # noqa: E501

        :param product_id: The product_id of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501
        :type: str
        """

        self._product_id = product_id

    @property
    def service_id(self):
        """Gets the service_id of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501

        The ID of the Service.  # noqa: E501

        :return: The service_id of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.

        The ID of the Service.  # noqa: E501

        :param service_id: The service_id of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501
        :type: str
        """

        self._service_id = service_id

    @property
    def trade_of_asset(self):
        """Gets the trade_of_asset of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501

        Whether the line item is marked as trade of asset.  # noqa: E501

        :return: The trade_of_asset of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501
        :rtype: bool
        """
        return self._trade_of_asset

    @trade_of_asset.setter
    def trade_of_asset(self, trade_of_asset):
        """Sets the trade_of_asset of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.

        Whether the line item is marked as trade of asset.  # noqa: E501

        :param trade_of_asset: The trade_of_asset of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501
        :type: bool
        """

        self._trade_of_asset = trade_of_asset

    @property
    def net_amount(self):
        """Gets the net_amount of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501

        The net amount for the credit note line  # noqa: E501

        :return: The net_amount of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501
        :rtype: float
        """
        return self._net_amount

    @net_amount.setter
    def net_amount(self, net_amount):
        """Sets the net_amount of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.

        The net amount for the credit note line  # noqa: E501

        :param net_amount: The net_amount of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501
        :type: float
        """

        self._net_amount = net_amount

    @property
    def tax_rate_id(self):
        """Gets the tax_rate_id of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501

        The ID of the Tax Rate.  # noqa: E501

        :return: The tax_rate_id of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501
        :rtype: str
        """
        return self._tax_rate_id

    @tax_rate_id.setter
    def tax_rate_id(self, tax_rate_id):
        """Sets the tax_rate_id of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.

        The ID of the Tax Rate.  # noqa: E501

        :param tax_rate_id: The tax_rate_id of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501
        :type: str
        """

        self._tax_rate_id = tax_rate_id

    @property
    def tax_amount(self):
        """Gets the tax_amount of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501

        The tax amount for the credit note line\". This attribute is required in v3.1, unless the tax rate is of a \"zero\", \"exempt\" or \"no_tax\" type. Then the tax_amount is infered as 0.0. In v3, this attribute is optional, but you should still set, as it defaults to 0.0 in any case. This is not what you want for tax rates with a percentage > 0.0.  # noqa: E501

        :return: The tax_amount of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501
        :rtype: float
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """Sets the tax_amount of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.

        The tax amount for the credit note line\". This attribute is required in v3.1, unless the tax rate is of a \"zero\", \"exempt\" or \"no_tax\" type. Then the tax_amount is infered as 0.0. In v3, this attribute is optional, but you should still set, as it defaults to 0.0 in any case. This is not what you want for tax rates with a percentage > 0.0.  # noqa: E501

        :param tax_amount: The tax_amount of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501
        :type: float
        """

        self._tax_amount = tax_amount

    @property
    def total_amount(self):
        """Gets the total_amount of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501

        The total amount for the credit note line  # noqa: E501

        :return: The total_amount of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501
        :rtype: float
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """Sets the total_amount of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.

        The total amount for the credit note line  # noqa: E501

        :param total_amount: The total_amount of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501
        :type: float
        """

        self._total_amount = total_amount

    @property
    def base_currency_unit_price(self):
        """Gets the base_currency_unit_price of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501

        The unit price for the credit note line in base currency  # noqa: E501

        :return: The base_currency_unit_price of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501
        :rtype: float
        """
        return self._base_currency_unit_price

    @base_currency_unit_price.setter
    def base_currency_unit_price(self, base_currency_unit_price):
        """Sets the base_currency_unit_price of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.

        The unit price for the credit note line in base currency  # noqa: E501

        :param base_currency_unit_price: The base_currency_unit_price of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501
        :type: float
        """

        self._base_currency_unit_price = base_currency_unit_price

    @property
    def unit_price_includes_tax(self):
        """Gets the unit_price_includes_tax of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501

        Defines whether the unit price includes tax  # noqa: E501

        :return: The unit_price_includes_tax of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501
        :rtype: bool
        """
        return self._unit_price_includes_tax

    @unit_price_includes_tax.setter
    def unit_price_includes_tax(self, unit_price_includes_tax):
        """Sets the unit_price_includes_tax of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.

        Defines whether the unit price includes tax  # noqa: E501

        :param unit_price_includes_tax: The unit_price_includes_tax of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501
        :type: bool
        """

        self._unit_price_includes_tax = unit_price_includes_tax

    @property
    def base_currency_net_amount(self):
        """Gets the base_currency_net_amount of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501

        The net amount for the credit note line in base currency  # noqa: E501

        :return: The base_currency_net_amount of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501
        :rtype: float
        """
        return self._base_currency_net_amount

    @base_currency_net_amount.setter
    def base_currency_net_amount(self, base_currency_net_amount):
        """Sets the base_currency_net_amount of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.

        The net amount for the credit note line in base currency  # noqa: E501

        :param base_currency_net_amount: The base_currency_net_amount of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501
        :type: float
        """

        self._base_currency_net_amount = base_currency_net_amount

    @property
    def base_currency_tax_amount(self):
        """Gets the base_currency_tax_amount of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501

        The tax amount for the credit note line in base currency  # noqa: E501

        :return: The base_currency_tax_amount of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501
        :rtype: float
        """
        return self._base_currency_tax_amount

    @base_currency_tax_amount.setter
    def base_currency_tax_amount(self, base_currency_tax_amount):
        """Sets the base_currency_tax_amount of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.

        The tax amount for the credit note line in base currency  # noqa: E501

        :param base_currency_tax_amount: The base_currency_tax_amount of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501
        :type: float
        """

        self._base_currency_tax_amount = base_currency_tax_amount

    @property
    def base_currency_total_amount(self):
        """Gets the base_currency_total_amount of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501

        The total amount for the credit note line in base currency  # noqa: E501

        :return: The base_currency_total_amount of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501
        :rtype: float
        """
        return self._base_currency_total_amount

    @base_currency_total_amount.setter
    def base_currency_total_amount(self, base_currency_total_amount):
        """Sets the base_currency_total_amount of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.

        The total amount for the credit note line in base currency  # noqa: E501

        :param base_currency_total_amount: The base_currency_total_amount of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501
        :type: float
        """

        self._base_currency_total_amount = base_currency_total_amount

    @property
    def eu_goods_services_type_id(self):
        """Gets the eu_goods_services_type_id of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501

        The ID of the EU Goods Services Type.  # noqa: E501

        :return: The eu_goods_services_type_id of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501
        :rtype: str
        """
        return self._eu_goods_services_type_id

    @eu_goods_services_type_id.setter
    def eu_goods_services_type_id(self, eu_goods_services_type_id):
        """Sets the eu_goods_services_type_id of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.

        The ID of the EU Goods Services Type.  # noqa: E501

        :param eu_goods_services_type_id: The eu_goods_services_type_id of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501
        :type: str
        """

        self._eu_goods_services_type_id = eu_goods_services_type_id

    @property
    def gst_amount(self):
        """Gets the gst_amount of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501

        The gst or hst tax amount for the credit note line  # noqa: E501

        :return: The gst_amount of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501
        :rtype: float
        """
        return self._gst_amount

    @gst_amount.setter
    def gst_amount(self, gst_amount):
        """Sets the gst_amount of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.

        The gst or hst tax amount for the credit note line  # noqa: E501

        :param gst_amount: The gst_amount of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501
        :type: float
        """

        self._gst_amount = gst_amount

    @property
    def pst_amount(self):
        """Gets the pst_amount of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501

        The pst or qst tax amount for the credit note line  # noqa: E501

        :return: The pst_amount of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501
        :rtype: float
        """
        return self._pst_amount

    @pst_amount.setter
    def pst_amount(self, pst_amount):
        """Sets the pst_amount of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.

        The pst or qst tax amount for the credit note line  # noqa: E501

        :param pst_amount: The pst_amount of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501
        :type: float
        """

        self._pst_amount = pst_amount

    @property
    def tax_recoverable(self):
        """Gets the tax_recoverable of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501

        Indicates if the credit note line is tax recoverable or not  # noqa: E501

        :return: The tax_recoverable of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501
        :rtype: bool
        """
        return self._tax_recoverable

    @tax_recoverable.setter
    def tax_recoverable(self, tax_recoverable):
        """Sets the tax_recoverable of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.

        Indicates if the credit note line is tax recoverable or not  # noqa: E501

        :param tax_recoverable: The tax_recoverable of this PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.  # noqa: E501
        :type: bool
        """

        self._tax_recoverable = tax_recoverable

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines):
            return True

        return self.to_dict() != other.to_dict()
