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


class PutPurchaseQuickEntriesPurchaseQuickEntry(object):
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
        'quick_entry_type_id': 'str',
        'date': 'date',
        'contact_id': 'str',
        'reference': 'str',
        'ledger_account_id': 'str',
        'contact_name': 'str',
        'contact_reference': 'str',
        'details': 'str',
        'net_amount': 'float',
        'tax_rate_id': 'str',
        'tax_amount': 'float',
        'total_amount': 'float',
        'currency_id': 'str',
        'exchange_rate': 'float',
        'inverse_exchange_rate': 'float',
        'base_currency_net_amount': 'float',
        'base_currency_tax_amount': 'float',
        'base_currency_total_amount': 'float',
        'status_id': 'str',
        'tax_address_region_id': 'str',
        'trade_of_asset': 'bool',
        'gst_amount': 'float',
        'pst_amount': 'float',
        'tax_recoverable': 'bool'
    }

    attribute_map = {
        'quick_entry_type_id': 'quick_entry_type_id',
        'date': 'date',
        'contact_id': 'contact_id',
        'reference': 'reference',
        'ledger_account_id': 'ledger_account_id',
        'contact_name': 'contact_name',
        'contact_reference': 'contact_reference',
        'details': 'details',
        'net_amount': 'net_amount',
        'tax_rate_id': 'tax_rate_id',
        'tax_amount': 'tax_amount',
        'total_amount': 'total_amount',
        'currency_id': 'currency_id',
        'exchange_rate': 'exchange_rate',
        'inverse_exchange_rate': 'inverse_exchange_rate',
        'base_currency_net_amount': 'base_currency_net_amount',
        'base_currency_tax_amount': 'base_currency_tax_amount',
        'base_currency_total_amount': 'base_currency_total_amount',
        'status_id': 'status_id',
        'tax_address_region_id': 'tax_address_region_id',
        'trade_of_asset': 'trade_of_asset',
        'gst_amount': 'gst_amount',
        'pst_amount': 'pst_amount',
        'tax_recoverable': 'tax_recoverable'
    }

    def __init__(self, quick_entry_type_id=None, date=None, contact_id=None, reference=None, ledger_account_id=None, contact_name=None, contact_reference=None, details=None, net_amount=None, tax_rate_id=None, tax_amount=None, total_amount=None, currency_id=None, exchange_rate=None, inverse_exchange_rate=None, base_currency_net_amount=None, base_currency_tax_amount=None, base_currency_total_amount=None, status_id=None, tax_address_region_id=None, trade_of_asset=None, gst_amount=None, pst_amount=None, tax_recoverable=None, local_vars_configuration=None):  # noqa: E501
        """PutPurchaseQuickEntriesPurchaseQuickEntry - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._quick_entry_type_id = None
        self._date = None
        self._contact_id = None
        self._reference = None
        self._ledger_account_id = None
        self._contact_name = None
        self._contact_reference = None
        self._details = None
        self._net_amount = None
        self._tax_rate_id = None
        self._tax_amount = None
        self._total_amount = None
        self._currency_id = None
        self._exchange_rate = None
        self._inverse_exchange_rate = None
        self._base_currency_net_amount = None
        self._base_currency_tax_amount = None
        self._base_currency_total_amount = None
        self._status_id = None
        self._tax_address_region_id = None
        self._trade_of_asset = None
        self._gst_amount = None
        self._pst_amount = None
        self._tax_recoverable = None
        self.discriminator = None

        if quick_entry_type_id is not None:
            self.quick_entry_type_id = quick_entry_type_id
        if date is not None:
            self.date = date
        if contact_id is not None:
            self.contact_id = contact_id
        if reference is not None:
            self.reference = reference
        if ledger_account_id is not None:
            self.ledger_account_id = ledger_account_id
        if contact_name is not None:
            self.contact_name = contact_name
        if contact_reference is not None:
            self.contact_reference = contact_reference
        if details is not None:
            self.details = details
        if net_amount is not None:
            self.net_amount = net_amount
        if tax_rate_id is not None:
            self.tax_rate_id = tax_rate_id
        if tax_amount is not None:
            self.tax_amount = tax_amount
        if total_amount is not None:
            self.total_amount = total_amount
        if currency_id is not None:
            self.currency_id = currency_id
        if exchange_rate is not None:
            self.exchange_rate = exchange_rate
        if inverse_exchange_rate is not None:
            self.inverse_exchange_rate = inverse_exchange_rate
        if base_currency_net_amount is not None:
            self.base_currency_net_amount = base_currency_net_amount
        if base_currency_tax_amount is not None:
            self.base_currency_tax_amount = base_currency_tax_amount
        if base_currency_total_amount is not None:
            self.base_currency_total_amount = base_currency_total_amount
        if status_id is not None:
            self.status_id = status_id
        if tax_address_region_id is not None:
            self.tax_address_region_id = tax_address_region_id
        if trade_of_asset is not None:
            self.trade_of_asset = trade_of_asset
        if gst_amount is not None:
            self.gst_amount = gst_amount
        if pst_amount is not None:
            self.pst_amount = pst_amount
        if tax_recoverable is not None:
            self.tax_recoverable = tax_recoverable

    @property
    def quick_entry_type_id(self):
        """Gets the quick_entry_type_id of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501

        The type of quick entry e.g. invoice or credit note  # noqa: E501

        :return: The quick_entry_type_id of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501
        :rtype: str
        """
        return self._quick_entry_type_id

    @quick_entry_type_id.setter
    def quick_entry_type_id(self, quick_entry_type_id):
        """Sets the quick_entry_type_id of this PutPurchaseQuickEntriesPurchaseQuickEntry.

        The type of quick entry e.g. invoice or credit note  # noqa: E501

        :param quick_entry_type_id: The quick_entry_type_id of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501
        :type: str
        """

        self._quick_entry_type_id = quick_entry_type_id

    @property
    def date(self):
        """Gets the date of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501

        The date of the quick entry  # noqa: E501

        :return: The date of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this PutPurchaseQuickEntriesPurchaseQuickEntry.

        The date of the quick entry  # noqa: E501

        :param date: The date of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501
        :type: date
        """

        self._date = date

    @property
    def contact_id(self):
        """Gets the contact_id of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501

        The contact the quick entry relates to  # noqa: E501

        :return: The contact_id of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501
        :rtype: str
        """
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        """Sets the contact_id of this PutPurchaseQuickEntriesPurchaseQuickEntry.

        The contact the quick entry relates to  # noqa: E501

        :param contact_id: The contact_id of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501
        :type: str
        """

        self._contact_id = contact_id

    @property
    def reference(self):
        """Gets the reference of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501

        The reference for the quick entry  # noqa: E501

        :return: The reference of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this PutPurchaseQuickEntriesPurchaseQuickEntry.

        The reference for the quick entry  # noqa: E501

        :param reference: The reference of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def ledger_account_id(self):
        """Gets the ledger_account_id of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501

        The associated ledger account  # noqa: E501

        :return: The ledger_account_id of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501
        :rtype: str
        """
        return self._ledger_account_id

    @ledger_account_id.setter
    def ledger_account_id(self, ledger_account_id):
        """Sets the ledger_account_id of this PutPurchaseQuickEntriesPurchaseQuickEntry.

        The associated ledger account  # noqa: E501

        :param ledger_account_id: The ledger_account_id of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501
        :type: str
        """

        self._ledger_account_id = ledger_account_id

    @property
    def contact_name(self):
        """Gets the contact_name of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501

        The name of the contact when the quick entry was created  # noqa: E501

        :return: The contact_name of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501
        :rtype: str
        """
        return self._contact_name

    @contact_name.setter
    def contact_name(self, contact_name):
        """Sets the contact_name of this PutPurchaseQuickEntriesPurchaseQuickEntry.

        The name of the contact when the quick entry was created  # noqa: E501

        :param contact_name: The contact_name of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501
        :type: str
        """

        self._contact_name = contact_name

    @property
    def contact_reference(self):
        """Gets the contact_reference of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501

        The reference of the contact when the quick entry was created  # noqa: E501

        :return: The contact_reference of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501
        :rtype: str
        """
        return self._contact_reference

    @contact_reference.setter
    def contact_reference(self, contact_reference):
        """Sets the contact_reference of this PutPurchaseQuickEntriesPurchaseQuickEntry.

        The reference of the contact when the quick entry was created  # noqa: E501

        :param contact_reference: The contact_reference of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501
        :type: str
        """

        self._contact_reference = contact_reference

    @property
    def details(self):
        """Gets the details of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501

        A description of the quick entry  # noqa: E501

        :return: The details of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this PutPurchaseQuickEntriesPurchaseQuickEntry.

        A description of the quick entry  # noqa: E501

        :param details: The details of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501
        :type: str
        """

        self._details = details

    @property
    def net_amount(self):
        """Gets the net_amount of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501

        The net amount of the quick entry  # noqa: E501

        :return: The net_amount of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501
        :rtype: float
        """
        return self._net_amount

    @net_amount.setter
    def net_amount(self, net_amount):
        """Sets the net_amount of this PutPurchaseQuickEntriesPurchaseQuickEntry.

        The net amount of the quick entry  # noqa: E501

        :param net_amount: The net_amount of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501
        :type: float
        """

        self._net_amount = net_amount

    @property
    def tax_rate_id(self):
        """Gets the tax_rate_id of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501

        The ID of the Tax Rate.  # noqa: E501

        :return: The tax_rate_id of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501
        :rtype: str
        """
        return self._tax_rate_id

    @tax_rate_id.setter
    def tax_rate_id(self, tax_rate_id):
        """Sets the tax_rate_id of this PutPurchaseQuickEntriesPurchaseQuickEntry.

        The ID of the Tax Rate.  # noqa: E501

        :param tax_rate_id: The tax_rate_id of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501
        :type: str
        """

        self._tax_rate_id = tax_rate_id

    @property
    def tax_amount(self):
        """Gets the tax_amount of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501

        The tax amount of the quick entry  # noqa: E501

        :return: The tax_amount of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501
        :rtype: float
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """Sets the tax_amount of this PutPurchaseQuickEntriesPurchaseQuickEntry.

        The tax amount of the quick entry  # noqa: E501

        :param tax_amount: The tax_amount of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501
        :type: float
        """

        self._tax_amount = tax_amount

    @property
    def total_amount(self):
        """Gets the total_amount of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501

        The total amount of the quick entry  # noqa: E501

        :return: The total_amount of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501
        :rtype: float
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """Sets the total_amount of this PutPurchaseQuickEntriesPurchaseQuickEntry.

        The total amount of the quick entry  # noqa: E501

        :param total_amount: The total_amount of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501
        :type: float
        """

        self._total_amount = total_amount

    @property
    def currency_id(self):
        """Gets the currency_id of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501

        The ID of the Currency.  # noqa: E501

        :return: The currency_id of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501
        :rtype: str
        """
        return self._currency_id

    @currency_id.setter
    def currency_id(self, currency_id):
        """Sets the currency_id of this PutPurchaseQuickEntriesPurchaseQuickEntry.

        The ID of the Currency.  # noqa: E501

        :param currency_id: The currency_id of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501
        :type: str
        """

        self._currency_id = currency_id

    @property
    def exchange_rate(self):
        """Gets the exchange_rate of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501

        The exchange rate for the quick entry  # noqa: E501

        :return: The exchange_rate of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501
        :rtype: float
        """
        return self._exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, exchange_rate):
        """Sets the exchange_rate of this PutPurchaseQuickEntriesPurchaseQuickEntry.

        The exchange rate for the quick entry  # noqa: E501

        :param exchange_rate: The exchange_rate of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501
        :type: float
        """

        self._exchange_rate = exchange_rate

    @property
    def inverse_exchange_rate(self):
        """Gets the inverse_exchange_rate of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501

        The inverse exchange rate for the quick entry  # noqa: E501

        :return: The inverse_exchange_rate of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501
        :rtype: float
        """
        return self._inverse_exchange_rate

    @inverse_exchange_rate.setter
    def inverse_exchange_rate(self, inverse_exchange_rate):
        """Sets the inverse_exchange_rate of this PutPurchaseQuickEntriesPurchaseQuickEntry.

        The inverse exchange rate for the quick entry  # noqa: E501

        :param inverse_exchange_rate: The inverse_exchange_rate of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501
        :type: float
        """

        self._inverse_exchange_rate = inverse_exchange_rate

    @property
    def base_currency_net_amount(self):
        """Gets the base_currency_net_amount of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501

        The net amount of the quick entry in base currency  # noqa: E501

        :return: The base_currency_net_amount of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501
        :rtype: float
        """
        return self._base_currency_net_amount

    @base_currency_net_amount.setter
    def base_currency_net_amount(self, base_currency_net_amount):
        """Sets the base_currency_net_amount of this PutPurchaseQuickEntriesPurchaseQuickEntry.

        The net amount of the quick entry in base currency  # noqa: E501

        :param base_currency_net_amount: The base_currency_net_amount of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501
        :type: float
        """

        self._base_currency_net_amount = base_currency_net_amount

    @property
    def base_currency_tax_amount(self):
        """Gets the base_currency_tax_amount of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501

        The tax amount of the quick entry in base currency  # noqa: E501

        :return: The base_currency_tax_amount of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501
        :rtype: float
        """
        return self._base_currency_tax_amount

    @base_currency_tax_amount.setter
    def base_currency_tax_amount(self, base_currency_tax_amount):
        """Sets the base_currency_tax_amount of this PutPurchaseQuickEntriesPurchaseQuickEntry.

        The tax amount of the quick entry in base currency  # noqa: E501

        :param base_currency_tax_amount: The base_currency_tax_amount of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501
        :type: float
        """

        self._base_currency_tax_amount = base_currency_tax_amount

    @property
    def base_currency_total_amount(self):
        """Gets the base_currency_total_amount of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501

        The total amount of the quick entry in base currency  # noqa: E501

        :return: The base_currency_total_amount of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501
        :rtype: float
        """
        return self._base_currency_total_amount

    @base_currency_total_amount.setter
    def base_currency_total_amount(self, base_currency_total_amount):
        """Sets the base_currency_total_amount of this PutPurchaseQuickEntriesPurchaseQuickEntry.

        The total amount of the quick entry in base currency  # noqa: E501

        :param base_currency_total_amount: The base_currency_total_amount of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501
        :type: float
        """

        self._base_currency_total_amount = base_currency_total_amount

    @property
    def status_id(self):
        """Gets the status_id of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501

        The ID of the Status.  # noqa: E501

        :return: The status_id of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501
        :rtype: str
        """
        return self._status_id

    @status_id.setter
    def status_id(self, status_id):
        """Sets the status_id of this PutPurchaseQuickEntriesPurchaseQuickEntry.

        The ID of the Status.  # noqa: E501

        :param status_id: The status_id of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501
        :type: str
        """

        self._status_id = status_id

    @property
    def tax_address_region_id(self):
        """Gets the tax_address_region_id of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501

        The ID of the Tax Address Region. (Canada only)  # noqa: E501

        :return: The tax_address_region_id of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501
        :rtype: str
        """
        return self._tax_address_region_id

    @tax_address_region_id.setter
    def tax_address_region_id(self, tax_address_region_id):
        """Sets the tax_address_region_id of this PutPurchaseQuickEntriesPurchaseQuickEntry.

        The ID of the Tax Address Region. (Canada only)  # noqa: E501

        :param tax_address_region_id: The tax_address_region_id of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501
        :type: str
        """

        self._tax_address_region_id = tax_address_region_id

    @property
    def trade_of_asset(self):
        """Gets the trade_of_asset of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501

        Whether the quick entry is marked as trade of asset.  # noqa: E501

        :return: The trade_of_asset of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501
        :rtype: bool
        """
        return self._trade_of_asset

    @trade_of_asset.setter
    def trade_of_asset(self, trade_of_asset):
        """Sets the trade_of_asset of this PutPurchaseQuickEntriesPurchaseQuickEntry.

        Whether the quick entry is marked as trade of asset.  # noqa: E501

        :param trade_of_asset: The trade_of_asset of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501
        :type: bool
        """

        self._trade_of_asset = trade_of_asset

    @property
    def gst_amount(self):
        """Gets the gst_amount of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501

        The gst or hst tax amount for the purchase quick entry  # noqa: E501

        :return: The gst_amount of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501
        :rtype: float
        """
        return self._gst_amount

    @gst_amount.setter
    def gst_amount(self, gst_amount):
        """Sets the gst_amount of this PutPurchaseQuickEntriesPurchaseQuickEntry.

        The gst or hst tax amount for the purchase quick entry  # noqa: E501

        :param gst_amount: The gst_amount of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501
        :type: float
        """

        self._gst_amount = gst_amount

    @property
    def pst_amount(self):
        """Gets the pst_amount of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501

        The pst or qst tax amount for the purchase quick entry  # noqa: E501

        :return: The pst_amount of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501
        :rtype: float
        """
        return self._pst_amount

    @pst_amount.setter
    def pst_amount(self, pst_amount):
        """Sets the pst_amount of this PutPurchaseQuickEntriesPurchaseQuickEntry.

        The pst or qst tax amount for the purchase quick entry  # noqa: E501

        :param pst_amount: The pst_amount of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501
        :type: float
        """

        self._pst_amount = pst_amount

    @property
    def tax_recoverable(self):
        """Gets the tax_recoverable of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501

        Indicates if the purchase quick entry is tax recoverable or not  # noqa: E501

        :return: The tax_recoverable of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501
        :rtype: bool
        """
        return self._tax_recoverable

    @tax_recoverable.setter
    def tax_recoverable(self, tax_recoverable):
        """Sets the tax_recoverable of this PutPurchaseQuickEntriesPurchaseQuickEntry.

        Indicates if the purchase quick entry is tax recoverable or not  # noqa: E501

        :param tax_recoverable: The tax_recoverable of this PutPurchaseQuickEntriesPurchaseQuickEntry.  # noqa: E501
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
        if not isinstance(other, PutPurchaseQuickEntriesPurchaseQuickEntry):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PutPurchaseQuickEntriesPurchaseQuickEntry):
            return True

        return self.to_dict() != other.to_dict()
