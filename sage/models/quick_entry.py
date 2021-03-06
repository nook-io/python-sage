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


class QuickEntry(object):
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
        'id': 'str',
        'displayed_as': 'str',
        'path': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'transaction': 'Base',
        'transaction_type': 'Base',
        'deleted_at': 'datetime',
        'quick_entry_type': 'Base',
        'contact_name': 'str',
        'contact_reference': 'str',
        'contact': 'Base',
        'date': 'date',
        'reference': 'str',
        'ledger_account': 'Base',
        'details': 'str',
        'net_amount': 'float',
        'tax_rate': 'Base',
        'tax_amount': 'float',
        'tax_breakdown': 'list[TaxBreakdown]',
        'total_amount': 'float',
        'outstanding_amount': 'float',
        'currency': 'Base',
        'exchange_rate': 'float',
        'inverse_exchange_rate': 'float',
        'base_currency_net_amount': 'float',
        'base_currency_tax_amount': 'float',
        'base_currency_tax_breakdown': 'list[TaxBreakdown]',
        'base_currency_total_amount': 'float',
        'base_currency_outstanding_amount': 'float',
        'status': 'Base',
        'payments_allocations': 'list[PaymentAllocation]',
        'tax_address_region': 'Base',
        'migrated': 'bool',
        'trade_of_asset': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'displayed_as': 'displayed_as',
        'path': '$path',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'transaction': 'transaction',
        'transaction_type': 'transaction_type',
        'deleted_at': 'deleted_at',
        'quick_entry_type': 'quick_entry_type',
        'contact_name': 'contact_name',
        'contact_reference': 'contact_reference',
        'contact': 'contact',
        'date': 'date',
        'reference': 'reference',
        'ledger_account': 'ledger_account',
        'details': 'details',
        'net_amount': 'net_amount',
        'tax_rate': 'tax_rate',
        'tax_amount': 'tax_amount',
        'tax_breakdown': 'tax_breakdown',
        'total_amount': 'total_amount',
        'outstanding_amount': 'outstanding_amount',
        'currency': 'currency',
        'exchange_rate': 'exchange_rate',
        'inverse_exchange_rate': 'inverse_exchange_rate',
        'base_currency_net_amount': 'base_currency_net_amount',
        'base_currency_tax_amount': 'base_currency_tax_amount',
        'base_currency_tax_breakdown': 'base_currency_tax_breakdown',
        'base_currency_total_amount': 'base_currency_total_amount',
        'base_currency_outstanding_amount': 'base_currency_outstanding_amount',
        'status': 'status',
        'payments_allocations': 'payments_allocations',
        'tax_address_region': 'tax_address_region',
        'migrated': 'migrated',
        'trade_of_asset': 'trade_of_asset'
    }

    def __init__(self, id=None, displayed_as=None, path=None, created_at=None, updated_at=None, transaction=None, transaction_type=None, deleted_at=None, quick_entry_type=None, contact_name=None, contact_reference=None, contact=None, date=None, reference=None, ledger_account=None, details=None, net_amount=None, tax_rate=None, tax_amount=None, tax_breakdown=None, total_amount=None, outstanding_amount=None, currency=None, exchange_rate=None, inverse_exchange_rate=None, base_currency_net_amount=None, base_currency_tax_amount=None, base_currency_tax_breakdown=None, base_currency_total_amount=None, base_currency_outstanding_amount=None, status=None, payments_allocations=None, tax_address_region=None, migrated=None, trade_of_asset=None, local_vars_configuration=None):  # noqa: E501
        """QuickEntry - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._displayed_as = None
        self._path = None
        self._created_at = None
        self._updated_at = None
        self._transaction = None
        self._transaction_type = None
        self._deleted_at = None
        self._quick_entry_type = None
        self._contact_name = None
        self._contact_reference = None
        self._contact = None
        self._date = None
        self._reference = None
        self._ledger_account = None
        self._details = None
        self._net_amount = None
        self._tax_rate = None
        self._tax_amount = None
        self._tax_breakdown = None
        self._total_amount = None
        self._outstanding_amount = None
        self._currency = None
        self._exchange_rate = None
        self._inverse_exchange_rate = None
        self._base_currency_net_amount = None
        self._base_currency_tax_amount = None
        self._base_currency_tax_breakdown = None
        self._base_currency_total_amount = None
        self._base_currency_outstanding_amount = None
        self._status = None
        self._payments_allocations = None
        self._tax_address_region = None
        self._migrated = None
        self._trade_of_asset = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if displayed_as is not None:
            self.displayed_as = displayed_as
        if path is not None:
            self.path = path
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if transaction is not None:
            self.transaction = transaction
        if transaction_type is not None:
            self.transaction_type = transaction_type
        if deleted_at is not None:
            self.deleted_at = deleted_at
        if quick_entry_type is not None:
            self.quick_entry_type = quick_entry_type
        if contact_name is not None:
            self.contact_name = contact_name
        if contact_reference is not None:
            self.contact_reference = contact_reference
        if contact is not None:
            self.contact = contact
        if date is not None:
            self.date = date
        if reference is not None:
            self.reference = reference
        if ledger_account is not None:
            self.ledger_account = ledger_account
        if details is not None:
            self.details = details
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
        if outstanding_amount is not None:
            self.outstanding_amount = outstanding_amount
        if currency is not None:
            self.currency = currency
        if exchange_rate is not None:
            self.exchange_rate = exchange_rate
        if inverse_exchange_rate is not None:
            self.inverse_exchange_rate = inverse_exchange_rate
        if base_currency_net_amount is not None:
            self.base_currency_net_amount = base_currency_net_amount
        if base_currency_tax_amount is not None:
            self.base_currency_tax_amount = base_currency_tax_amount
        if base_currency_tax_breakdown is not None:
            self.base_currency_tax_breakdown = base_currency_tax_breakdown
        if base_currency_total_amount is not None:
            self.base_currency_total_amount = base_currency_total_amount
        if base_currency_outstanding_amount is not None:
            self.base_currency_outstanding_amount = base_currency_outstanding_amount
        if status is not None:
            self.status = status
        if payments_allocations is not None:
            self.payments_allocations = payments_allocations
        if tax_address_region is not None:
            self.tax_address_region = tax_address_region
        if migrated is not None:
            self.migrated = migrated
        if trade_of_asset is not None:
            self.trade_of_asset = trade_of_asset

    @property
    def id(self):
        """Gets the id of this QuickEntry.  # noqa: E501

        The unique identifier for the item  # noqa: E501

        :return: The id of this QuickEntry.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QuickEntry.

        The unique identifier for the item  # noqa: E501

        :param id: The id of this QuickEntry.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def displayed_as(self):
        """Gets the displayed_as of this QuickEntry.  # noqa: E501

        The name of the resource  # noqa: E501

        :return: The displayed_as of this QuickEntry.  # noqa: E501
        :rtype: str
        """
        return self._displayed_as

    @displayed_as.setter
    def displayed_as(self, displayed_as):
        """Sets the displayed_as of this QuickEntry.

        The name of the resource  # noqa: E501

        :param displayed_as: The displayed_as of this QuickEntry.  # noqa: E501
        :type: str
        """

        self._displayed_as = displayed_as

    @property
    def path(self):
        """Gets the path of this QuickEntry.  # noqa: E501

        The API path for the resource  # noqa: E501

        :return: The path of this QuickEntry.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this QuickEntry.

        The API path for the resource  # noqa: E501

        :param path: The path of this QuickEntry.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def created_at(self):
        """Gets the created_at of this QuickEntry.  # noqa: E501

        The datetime when the item was created  # noqa: E501

        :return: The created_at of this QuickEntry.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this QuickEntry.

        The datetime when the item was created  # noqa: E501

        :param created_at: The created_at of this QuickEntry.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this QuickEntry.  # noqa: E501

        The datetime when the item was last updated  # noqa: E501

        :return: The updated_at of this QuickEntry.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this QuickEntry.

        The datetime when the item was last updated  # noqa: E501

        :param updated_at: The updated_at of this QuickEntry.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def transaction(self):
        """Gets the transaction of this QuickEntry.  # noqa: E501


        :return: The transaction of this QuickEntry.  # noqa: E501
        :rtype: Base
        """
        return self._transaction

    @transaction.setter
    def transaction(self, transaction):
        """Sets the transaction of this QuickEntry.


        :param transaction: The transaction of this QuickEntry.  # noqa: E501
        :type: Base
        """

        self._transaction = transaction

    @property
    def transaction_type(self):
        """Gets the transaction_type of this QuickEntry.  # noqa: E501


        :return: The transaction_type of this QuickEntry.  # noqa: E501
        :rtype: Base
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        """Sets the transaction_type of this QuickEntry.


        :param transaction_type: The transaction_type of this QuickEntry.  # noqa: E501
        :type: Base
        """

        self._transaction_type = transaction_type

    @property
    def deleted_at(self):
        """Gets the deleted_at of this QuickEntry.  # noqa: E501

        The datetime when the item was deleted  # noqa: E501

        :return: The deleted_at of this QuickEntry.  # noqa: E501
        :rtype: datetime
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """Sets the deleted_at of this QuickEntry.

        The datetime when the item was deleted  # noqa: E501

        :param deleted_at: The deleted_at of this QuickEntry.  # noqa: E501
        :type: datetime
        """

        self._deleted_at = deleted_at

    @property
    def quick_entry_type(self):
        """Gets the quick_entry_type of this QuickEntry.  # noqa: E501


        :return: The quick_entry_type of this QuickEntry.  # noqa: E501
        :rtype: Base
        """
        return self._quick_entry_type

    @quick_entry_type.setter
    def quick_entry_type(self, quick_entry_type):
        """Sets the quick_entry_type of this QuickEntry.


        :param quick_entry_type: The quick_entry_type of this QuickEntry.  # noqa: E501
        :type: Base
        """

        self._quick_entry_type = quick_entry_type

    @property
    def contact_name(self):
        """Gets the contact_name of this QuickEntry.  # noqa: E501

        The name of the contact when the quick entry was created  # noqa: E501

        :return: The contact_name of this QuickEntry.  # noqa: E501
        :rtype: str
        """
        return self._contact_name

    @contact_name.setter
    def contact_name(self, contact_name):
        """Sets the contact_name of this QuickEntry.

        The name of the contact when the quick entry was created  # noqa: E501

        :param contact_name: The contact_name of this QuickEntry.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                contact_name is not None and len(contact_name) > 255):
            raise ValueError("Invalid value for `contact_name`, length must be less than or equal to `255`")  # noqa: E501

        self._contact_name = contact_name

    @property
    def contact_reference(self):
        """Gets the contact_reference of this QuickEntry.  # noqa: E501

        The reference of the contact when the quick entry was created  # noqa: E501

        :return: The contact_reference of this QuickEntry.  # noqa: E501
        :rtype: str
        """
        return self._contact_reference

    @contact_reference.setter
    def contact_reference(self, contact_reference):
        """Sets the contact_reference of this QuickEntry.

        The reference of the contact when the quick entry was created  # noqa: E501

        :param contact_reference: The contact_reference of this QuickEntry.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                contact_reference is not None and len(contact_reference) > 255):
            raise ValueError("Invalid value for `contact_reference`, length must be less than or equal to `255`")  # noqa: E501

        self._contact_reference = contact_reference

    @property
    def contact(self):
        """Gets the contact of this QuickEntry.  # noqa: E501


        :return: The contact of this QuickEntry.  # noqa: E501
        :rtype: Base
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this QuickEntry.


        :param contact: The contact of this QuickEntry.  # noqa: E501
        :type: Base
        """

        self._contact = contact

    @property
    def date(self):
        """Gets the date of this QuickEntry.  # noqa: E501

        The date of the quick entry  # noqa: E501

        :return: The date of this QuickEntry.  # noqa: E501
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this QuickEntry.

        The date of the quick entry  # noqa: E501

        :param date: The date of this QuickEntry.  # noqa: E501
        :type: date
        """

        self._date = date

    @property
    def reference(self):
        """Gets the reference of this QuickEntry.  # noqa: E501

        The reference for the quick entry  # noqa: E501

        :return: The reference of this QuickEntry.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this QuickEntry.

        The reference for the quick entry  # noqa: E501

        :param reference: The reference of this QuickEntry.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                reference is not None and len(reference) > 25):
            raise ValueError("Invalid value for `reference`, length must be less than or equal to `25`")  # noqa: E501

        self._reference = reference

    @property
    def ledger_account(self):
        """Gets the ledger_account of this QuickEntry.  # noqa: E501


        :return: The ledger_account of this QuickEntry.  # noqa: E501
        :rtype: Base
        """
        return self._ledger_account

    @ledger_account.setter
    def ledger_account(self, ledger_account):
        """Sets the ledger_account of this QuickEntry.


        :param ledger_account: The ledger_account of this QuickEntry.  # noqa: E501
        :type: Base
        """

        self._ledger_account = ledger_account

    @property
    def details(self):
        """Gets the details of this QuickEntry.  # noqa: E501

        A description of the quick entry  # noqa: E501

        :return: The details of this QuickEntry.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this QuickEntry.

        A description of the quick entry  # noqa: E501

        :param details: The details of this QuickEntry.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                details is not None and len(details) > 255):
            raise ValueError("Invalid value for `details`, length must be less than or equal to `255`")  # noqa: E501

        self._details = details

    @property
    def net_amount(self):
        """Gets the net_amount of this QuickEntry.  # noqa: E501

        The net amount of the quick entry  # noqa: E501

        :return: The net_amount of this QuickEntry.  # noqa: E501
        :rtype: float
        """
        return self._net_amount

    @net_amount.setter
    def net_amount(self, net_amount):
        """Sets the net_amount of this QuickEntry.

        The net amount of the quick entry  # noqa: E501

        :param net_amount: The net_amount of this QuickEntry.  # noqa: E501
        :type: float
        """

        self._net_amount = net_amount

    @property
    def tax_rate(self):
        """Gets the tax_rate of this QuickEntry.  # noqa: E501


        :return: The tax_rate of this QuickEntry.  # noqa: E501
        :rtype: Base
        """
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, tax_rate):
        """Sets the tax_rate of this QuickEntry.


        :param tax_rate: The tax_rate of this QuickEntry.  # noqa: E501
        :type: Base
        """

        self._tax_rate = tax_rate

    @property
    def tax_amount(self):
        """Gets the tax_amount of this QuickEntry.  # noqa: E501

        The tax amount of the quick entry  # noqa: E501

        :return: The tax_amount of this QuickEntry.  # noqa: E501
        :rtype: float
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """Sets the tax_amount of this QuickEntry.

        The tax amount of the quick entry  # noqa: E501

        :param tax_amount: The tax_amount of this QuickEntry.  # noqa: E501
        :type: float
        """

        self._tax_amount = tax_amount

    @property
    def tax_breakdown(self):
        """Gets the tax_breakdown of this QuickEntry.  # noqa: E501

        The tax breakdown for the quick entry  # noqa: E501

        :return: The tax_breakdown of this QuickEntry.  # noqa: E501
        :rtype: list[TaxBreakdown]
        """
        return self._tax_breakdown

    @tax_breakdown.setter
    def tax_breakdown(self, tax_breakdown):
        """Sets the tax_breakdown of this QuickEntry.

        The tax breakdown for the quick entry  # noqa: E501

        :param tax_breakdown: The tax_breakdown of this QuickEntry.  # noqa: E501
        :type: list[TaxBreakdown]
        """

        self._tax_breakdown = tax_breakdown

    @property
    def total_amount(self):
        """Gets the total_amount of this QuickEntry.  # noqa: E501

        The total amount of the quick entry  # noqa: E501

        :return: The total_amount of this QuickEntry.  # noqa: E501
        :rtype: float
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """Sets the total_amount of this QuickEntry.

        The total amount of the quick entry  # noqa: E501

        :param total_amount: The total_amount of this QuickEntry.  # noqa: E501
        :type: float
        """

        self._total_amount = total_amount

    @property
    def outstanding_amount(self):
        """Gets the outstanding_amount of this QuickEntry.  # noqa: E501

        The outstanding amount of the quick entry  # noqa: E501

        :return: The outstanding_amount of this QuickEntry.  # noqa: E501
        :rtype: float
        """
        return self._outstanding_amount

    @outstanding_amount.setter
    def outstanding_amount(self, outstanding_amount):
        """Sets the outstanding_amount of this QuickEntry.

        The outstanding amount of the quick entry  # noqa: E501

        :param outstanding_amount: The outstanding_amount of this QuickEntry.  # noqa: E501
        :type: float
        """

        self._outstanding_amount = outstanding_amount

    @property
    def currency(self):
        """Gets the currency of this QuickEntry.  # noqa: E501


        :return: The currency of this QuickEntry.  # noqa: E501
        :rtype: Base
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this QuickEntry.


        :param currency: The currency of this QuickEntry.  # noqa: E501
        :type: Base
        """

        self._currency = currency

    @property
    def exchange_rate(self):
        """Gets the exchange_rate of this QuickEntry.  # noqa: E501

        The exchange rate for the quick entry  # noqa: E501

        :return: The exchange_rate of this QuickEntry.  # noqa: E501
        :rtype: float
        """
        return self._exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, exchange_rate):
        """Sets the exchange_rate of this QuickEntry.

        The exchange rate for the quick entry  # noqa: E501

        :param exchange_rate: The exchange_rate of this QuickEntry.  # noqa: E501
        :type: float
        """

        self._exchange_rate = exchange_rate

    @property
    def inverse_exchange_rate(self):
        """Gets the inverse_exchange_rate of this QuickEntry.  # noqa: E501

        The inverse exchange rate for the quick entry  # noqa: E501

        :return: The inverse_exchange_rate of this QuickEntry.  # noqa: E501
        :rtype: float
        """
        return self._inverse_exchange_rate

    @inverse_exchange_rate.setter
    def inverse_exchange_rate(self, inverse_exchange_rate):
        """Sets the inverse_exchange_rate of this QuickEntry.

        The inverse exchange rate for the quick entry  # noqa: E501

        :param inverse_exchange_rate: The inverse_exchange_rate of this QuickEntry.  # noqa: E501
        :type: float
        """

        self._inverse_exchange_rate = inverse_exchange_rate

    @property
    def base_currency_net_amount(self):
        """Gets the base_currency_net_amount of this QuickEntry.  # noqa: E501

        The net amount of the quick entry in base currency  # noqa: E501

        :return: The base_currency_net_amount of this QuickEntry.  # noqa: E501
        :rtype: float
        """
        return self._base_currency_net_amount

    @base_currency_net_amount.setter
    def base_currency_net_amount(self, base_currency_net_amount):
        """Sets the base_currency_net_amount of this QuickEntry.

        The net amount of the quick entry in base currency  # noqa: E501

        :param base_currency_net_amount: The base_currency_net_amount of this QuickEntry.  # noqa: E501
        :type: float
        """

        self._base_currency_net_amount = base_currency_net_amount

    @property
    def base_currency_tax_amount(self):
        """Gets the base_currency_tax_amount of this QuickEntry.  # noqa: E501

        The tax amount of the quick entry in base currency  # noqa: E501

        :return: The base_currency_tax_amount of this QuickEntry.  # noqa: E501
        :rtype: float
        """
        return self._base_currency_tax_amount

    @base_currency_tax_amount.setter
    def base_currency_tax_amount(self, base_currency_tax_amount):
        """Sets the base_currency_tax_amount of this QuickEntry.

        The tax amount of the quick entry in base currency  # noqa: E501

        :param base_currency_tax_amount: The base_currency_tax_amount of this QuickEntry.  # noqa: E501
        :type: float
        """

        self._base_currency_tax_amount = base_currency_tax_amount

    @property
    def base_currency_tax_breakdown(self):
        """Gets the base_currency_tax_breakdown of this QuickEntry.  # noqa: E501

        The tax breakdown for the quick entry in base currency  # noqa: E501

        :return: The base_currency_tax_breakdown of this QuickEntry.  # noqa: E501
        :rtype: list[TaxBreakdown]
        """
        return self._base_currency_tax_breakdown

    @base_currency_tax_breakdown.setter
    def base_currency_tax_breakdown(self, base_currency_tax_breakdown):
        """Sets the base_currency_tax_breakdown of this QuickEntry.

        The tax breakdown for the quick entry in base currency  # noqa: E501

        :param base_currency_tax_breakdown: The base_currency_tax_breakdown of this QuickEntry.  # noqa: E501
        :type: list[TaxBreakdown]
        """

        self._base_currency_tax_breakdown = base_currency_tax_breakdown

    @property
    def base_currency_total_amount(self):
        """Gets the base_currency_total_amount of this QuickEntry.  # noqa: E501

        The total amount of the quick entry in base currency  # noqa: E501

        :return: The base_currency_total_amount of this QuickEntry.  # noqa: E501
        :rtype: float
        """
        return self._base_currency_total_amount

    @base_currency_total_amount.setter
    def base_currency_total_amount(self, base_currency_total_amount):
        """Sets the base_currency_total_amount of this QuickEntry.

        The total amount of the quick entry in base currency  # noqa: E501

        :param base_currency_total_amount: The base_currency_total_amount of this QuickEntry.  # noqa: E501
        :type: float
        """

        self._base_currency_total_amount = base_currency_total_amount

    @property
    def base_currency_outstanding_amount(self):
        """Gets the base_currency_outstanding_amount of this QuickEntry.  # noqa: E501

        The outstanding amount of the quick entry in base currency  # noqa: E501

        :return: The base_currency_outstanding_amount of this QuickEntry.  # noqa: E501
        :rtype: float
        """
        return self._base_currency_outstanding_amount

    @base_currency_outstanding_amount.setter
    def base_currency_outstanding_amount(self, base_currency_outstanding_amount):
        """Sets the base_currency_outstanding_amount of this QuickEntry.

        The outstanding amount of the quick entry in base currency  # noqa: E501

        :param base_currency_outstanding_amount: The base_currency_outstanding_amount of this QuickEntry.  # noqa: E501
        :type: float
        """

        self._base_currency_outstanding_amount = base_currency_outstanding_amount

    @property
    def status(self):
        """Gets the status of this QuickEntry.  # noqa: E501


        :return: The status of this QuickEntry.  # noqa: E501
        :rtype: Base
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this QuickEntry.


        :param status: The status of this QuickEntry.  # noqa: E501
        :type: Base
        """

        self._status = status

    @property
    def payments_allocations(self):
        """Gets the payments_allocations of this QuickEntry.  # noqa: E501

        The associated payments and allocations  # noqa: E501

        :return: The payments_allocations of this QuickEntry.  # noqa: E501
        :rtype: list[PaymentAllocation]
        """
        return self._payments_allocations

    @payments_allocations.setter
    def payments_allocations(self, payments_allocations):
        """Sets the payments_allocations of this QuickEntry.

        The associated payments and allocations  # noqa: E501

        :param payments_allocations: The payments_allocations of this QuickEntry.  # noqa: E501
        :type: list[PaymentAllocation]
        """

        self._payments_allocations = payments_allocations

    @property
    def tax_address_region(self):
        """Gets the tax_address_region of this QuickEntry.  # noqa: E501


        :return: The tax_address_region of this QuickEntry.  # noqa: E501
        :rtype: Base
        """
        return self._tax_address_region

    @tax_address_region.setter
    def tax_address_region(self, tax_address_region):
        """Sets the tax_address_region of this QuickEntry.


        :param tax_address_region: The tax_address_region of this QuickEntry.  # noqa: E501
        :type: Base
        """

        self._tax_address_region = tax_address_region

    @property
    def migrated(self):
        """Gets the migrated of this QuickEntry.  # noqa: E501

        Indicates if the quick entry was migrated from another system.  # noqa: E501

        :return: The migrated of this QuickEntry.  # noqa: E501
        :rtype: bool
        """
        return self._migrated

    @migrated.setter
    def migrated(self, migrated):
        """Sets the migrated of this QuickEntry.

        Indicates if the quick entry was migrated from another system.  # noqa: E501

        :param migrated: The migrated of this QuickEntry.  # noqa: E501
        :type: bool
        """

        self._migrated = migrated

    @property
    def trade_of_asset(self):
        """Gets the trade_of_asset of this QuickEntry.  # noqa: E501

        Whether the quick entry is marked as trade of asset.  # noqa: E501

        :return: The trade_of_asset of this QuickEntry.  # noqa: E501
        :rtype: bool
        """
        return self._trade_of_asset

    @trade_of_asset.setter
    def trade_of_asset(self, trade_of_asset):
        """Sets the trade_of_asset of this QuickEntry.

        Whether the quick entry is marked as trade of asset.  # noqa: E501

        :param trade_of_asset: The trade_of_asset of this QuickEntry.  # noqa: E501
        :type: bool
        """

        self._trade_of_asset = trade_of_asset

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
        if not isinstance(other, QuickEntry):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QuickEntry):
            return True

        return self.to_dict() != other.to_dict()
