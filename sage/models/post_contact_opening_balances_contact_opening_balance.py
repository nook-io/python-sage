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


class PostContactOpeningBalancesContactOpeningBalance(object):
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
        'contact_opening_balance_type_id': 'str',
        'date': 'date',
        'contact_id': 'str',
        'reference': 'str',
        'total_amount': 'float',
        'transaction_type_id': 'str',
        'details': 'str',
        'net_amount': 'float',
        'tax_rate_id': 'str',
        'tax_amount': 'float',
        'currency_id': 'str',
        'exchange_rate': 'float',
        'base_currency_net_amount': 'float',
        'base_currency_tax_amount': 'float',
        'base_currency_total_amount': 'float'
    }

    attribute_map = {
        'contact_opening_balance_type_id': 'contact_opening_balance_type_id',
        'date': 'date',
        'contact_id': 'contact_id',
        'reference': 'reference',
        'total_amount': 'total_amount',
        'transaction_type_id': 'transaction_type_id',
        'details': 'details',
        'net_amount': 'net_amount',
        'tax_rate_id': 'tax_rate_id',
        'tax_amount': 'tax_amount',
        'currency_id': 'currency_id',
        'exchange_rate': 'exchange_rate',
        'base_currency_net_amount': 'base_currency_net_amount',
        'base_currency_tax_amount': 'base_currency_tax_amount',
        'base_currency_total_amount': 'base_currency_total_amount'
    }

    def __init__(self, contact_opening_balance_type_id=None, date=None, contact_id=None, reference=None, total_amount=None, transaction_type_id=None, details=None, net_amount=None, tax_rate_id=None, tax_amount=None, currency_id=None, exchange_rate=None, base_currency_net_amount=None, base_currency_tax_amount=None, base_currency_total_amount=None, local_vars_configuration=None):  # noqa: E501
        """PostContactOpeningBalancesContactOpeningBalance - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._contact_opening_balance_type_id = None
        self._date = None
        self._contact_id = None
        self._reference = None
        self._total_amount = None
        self._transaction_type_id = None
        self._details = None
        self._net_amount = None
        self._tax_rate_id = None
        self._tax_amount = None
        self._currency_id = None
        self._exchange_rate = None
        self._base_currency_net_amount = None
        self._base_currency_tax_amount = None
        self._base_currency_total_amount = None
        self.discriminator = None

        self.contact_opening_balance_type_id = contact_opening_balance_type_id
        self.date = date
        self.contact_id = contact_id
        self.reference = reference
        self.total_amount = total_amount
        if transaction_type_id is not None:
            self.transaction_type_id = transaction_type_id
        if details is not None:
            self.details = details
        if net_amount is not None:
            self.net_amount = net_amount
        if tax_rate_id is not None:
            self.tax_rate_id = tax_rate_id
        if tax_amount is not None:
            self.tax_amount = tax_amount
        if currency_id is not None:
            self.currency_id = currency_id
        if exchange_rate is not None:
            self.exchange_rate = exchange_rate
        if base_currency_net_amount is not None:
            self.base_currency_net_amount = base_currency_net_amount
        if base_currency_tax_amount is not None:
            self.base_currency_tax_amount = base_currency_tax_amount
        if base_currency_total_amount is not None:
            self.base_currency_total_amount = base_currency_total_amount

    @property
    def contact_opening_balance_type_id(self):
        """Gets the contact_opening_balance_type_id of this PostContactOpeningBalancesContactOpeningBalance.  # noqa: E501

        The type of contact opening balance e.g. invoice or credit note  # noqa: E501

        :return: The contact_opening_balance_type_id of this PostContactOpeningBalancesContactOpeningBalance.  # noqa: E501
        :rtype: str
        """
        return self._contact_opening_balance_type_id

    @contact_opening_balance_type_id.setter
    def contact_opening_balance_type_id(self, contact_opening_balance_type_id):
        """Sets the contact_opening_balance_type_id of this PostContactOpeningBalancesContactOpeningBalance.

        The type of contact opening balance e.g. invoice or credit note  # noqa: E501

        :param contact_opening_balance_type_id: The contact_opening_balance_type_id of this PostContactOpeningBalancesContactOpeningBalance.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and contact_opening_balance_type_id is None:  # noqa: E501
            raise ValueError("Invalid value for `contact_opening_balance_type_id`, must not be `None`")  # noqa: E501

        self._contact_opening_balance_type_id = contact_opening_balance_type_id

    @property
    def date(self):
        """Gets the date of this PostContactOpeningBalancesContactOpeningBalance.  # noqa: E501

        The date of the opening balance  # noqa: E501

        :return: The date of this PostContactOpeningBalancesContactOpeningBalance.  # noqa: E501
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this PostContactOpeningBalancesContactOpeningBalance.

        The date of the opening balance  # noqa: E501

        :param date: The date of this PostContactOpeningBalancesContactOpeningBalance.  # noqa: E501
        :type: date
        """
        if self.local_vars_configuration.client_side_validation and date is None:  # noqa: E501
            raise ValueError("Invalid value for `date`, must not be `None`")  # noqa: E501

        self._date = date

    @property
    def contact_id(self):
        """Gets the contact_id of this PostContactOpeningBalancesContactOpeningBalance.  # noqa: E501

        The contact the opening balance relates to  # noqa: E501

        :return: The contact_id of this PostContactOpeningBalancesContactOpeningBalance.  # noqa: E501
        :rtype: str
        """
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        """Sets the contact_id of this PostContactOpeningBalancesContactOpeningBalance.

        The contact the opening balance relates to  # noqa: E501

        :param contact_id: The contact_id of this PostContactOpeningBalancesContactOpeningBalance.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and contact_id is None:  # noqa: E501
            raise ValueError("Invalid value for `contact_id`, must not be `None`")  # noqa: E501

        self._contact_id = contact_id

    @property
    def reference(self):
        """Gets the reference of this PostContactOpeningBalancesContactOpeningBalance.  # noqa: E501

        The reference for the opening balance  # noqa: E501

        :return: The reference of this PostContactOpeningBalancesContactOpeningBalance.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this PostContactOpeningBalancesContactOpeningBalance.

        The reference for the opening balance  # noqa: E501

        :param reference: The reference of this PostContactOpeningBalancesContactOpeningBalance.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and reference is None:  # noqa: E501
            raise ValueError("Invalid value for `reference`, must not be `None`")  # noqa: E501

        self._reference = reference

    @property
    def total_amount(self):
        """Gets the total_amount of this PostContactOpeningBalancesContactOpeningBalance.  # noqa: E501

        The total amount of the opening balance  # noqa: E501

        :return: The total_amount of this PostContactOpeningBalancesContactOpeningBalance.  # noqa: E501
        :rtype: float
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """Sets the total_amount of this PostContactOpeningBalancesContactOpeningBalance.

        The total amount of the opening balance  # noqa: E501

        :param total_amount: The total_amount of this PostContactOpeningBalancesContactOpeningBalance.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and total_amount is None:  # noqa: E501
            raise ValueError("Invalid value for `total_amount`, must not be `None`")  # noqa: E501

        self._total_amount = total_amount

    @property
    def transaction_type_id(self):
        """Gets the transaction_type_id of this PostContactOpeningBalancesContactOpeningBalance.  # noqa: E501

        The ID of the Transaction Type.  # noqa: E501

        :return: The transaction_type_id of this PostContactOpeningBalancesContactOpeningBalance.  # noqa: E501
        :rtype: str
        """
        return self._transaction_type_id

    @transaction_type_id.setter
    def transaction_type_id(self, transaction_type_id):
        """Sets the transaction_type_id of this PostContactOpeningBalancesContactOpeningBalance.

        The ID of the Transaction Type.  # noqa: E501

        :param transaction_type_id: The transaction_type_id of this PostContactOpeningBalancesContactOpeningBalance.  # noqa: E501
        :type: str
        """

        self._transaction_type_id = transaction_type_id

    @property
    def details(self):
        """Gets the details of this PostContactOpeningBalancesContactOpeningBalance.  # noqa: E501

        A description of the opening balance  # noqa: E501

        :return: The details of this PostContactOpeningBalancesContactOpeningBalance.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this PostContactOpeningBalancesContactOpeningBalance.

        A description of the opening balance  # noqa: E501

        :param details: The details of this PostContactOpeningBalancesContactOpeningBalance.  # noqa: E501
        :type: str
        """

        self._details = details

    @property
    def net_amount(self):
        """Gets the net_amount of this PostContactOpeningBalancesContactOpeningBalance.  # noqa: E501

        The net amount of the opening balance  # noqa: E501

        :return: The net_amount of this PostContactOpeningBalancesContactOpeningBalance.  # noqa: E501
        :rtype: float
        """
        return self._net_amount

    @net_amount.setter
    def net_amount(self, net_amount):
        """Sets the net_amount of this PostContactOpeningBalancesContactOpeningBalance.

        The net amount of the opening balance  # noqa: E501

        :param net_amount: The net_amount of this PostContactOpeningBalancesContactOpeningBalance.  # noqa: E501
        :type: float
        """

        self._net_amount = net_amount

    @property
    def tax_rate_id(self):
        """Gets the tax_rate_id of this PostContactOpeningBalancesContactOpeningBalance.  # noqa: E501

        The ID of the Tax Rate.  # noqa: E501

        :return: The tax_rate_id of this PostContactOpeningBalancesContactOpeningBalance.  # noqa: E501
        :rtype: str
        """
        return self._tax_rate_id

    @tax_rate_id.setter
    def tax_rate_id(self, tax_rate_id):
        """Sets the tax_rate_id of this PostContactOpeningBalancesContactOpeningBalance.

        The ID of the Tax Rate.  # noqa: E501

        :param tax_rate_id: The tax_rate_id of this PostContactOpeningBalancesContactOpeningBalance.  # noqa: E501
        :type: str
        """

        self._tax_rate_id = tax_rate_id

    @property
    def tax_amount(self):
        """Gets the tax_amount of this PostContactOpeningBalancesContactOpeningBalance.  # noqa: E501

        The tax amount of the opening balance  # noqa: E501

        :return: The tax_amount of this PostContactOpeningBalancesContactOpeningBalance.  # noqa: E501
        :rtype: float
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """Sets the tax_amount of this PostContactOpeningBalancesContactOpeningBalance.

        The tax amount of the opening balance  # noqa: E501

        :param tax_amount: The tax_amount of this PostContactOpeningBalancesContactOpeningBalance.  # noqa: E501
        :type: float
        """

        self._tax_amount = tax_amount

    @property
    def currency_id(self):
        """Gets the currency_id of this PostContactOpeningBalancesContactOpeningBalance.  # noqa: E501

        The ID of the Currency.  # noqa: E501

        :return: The currency_id of this PostContactOpeningBalancesContactOpeningBalance.  # noqa: E501
        :rtype: str
        """
        return self._currency_id

    @currency_id.setter
    def currency_id(self, currency_id):
        """Sets the currency_id of this PostContactOpeningBalancesContactOpeningBalance.

        The ID of the Currency.  # noqa: E501

        :param currency_id: The currency_id of this PostContactOpeningBalancesContactOpeningBalance.  # noqa: E501
        :type: str
        """

        self._currency_id = currency_id

    @property
    def exchange_rate(self):
        """Gets the exchange_rate of this PostContactOpeningBalancesContactOpeningBalance.  # noqa: E501

        The exchange rate for the opening balance  # noqa: E501

        :return: The exchange_rate of this PostContactOpeningBalancesContactOpeningBalance.  # noqa: E501
        :rtype: float
        """
        return self._exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, exchange_rate):
        """Sets the exchange_rate of this PostContactOpeningBalancesContactOpeningBalance.

        The exchange rate for the opening balance  # noqa: E501

        :param exchange_rate: The exchange_rate of this PostContactOpeningBalancesContactOpeningBalance.  # noqa: E501
        :type: float
        """

        self._exchange_rate = exchange_rate

    @property
    def base_currency_net_amount(self):
        """Gets the base_currency_net_amount of this PostContactOpeningBalancesContactOpeningBalance.  # noqa: E501

        The net amount of the opening balance in base currency  # noqa: E501

        :return: The base_currency_net_amount of this PostContactOpeningBalancesContactOpeningBalance.  # noqa: E501
        :rtype: float
        """
        return self._base_currency_net_amount

    @base_currency_net_amount.setter
    def base_currency_net_amount(self, base_currency_net_amount):
        """Sets the base_currency_net_amount of this PostContactOpeningBalancesContactOpeningBalance.

        The net amount of the opening balance in base currency  # noqa: E501

        :param base_currency_net_amount: The base_currency_net_amount of this PostContactOpeningBalancesContactOpeningBalance.  # noqa: E501
        :type: float
        """

        self._base_currency_net_amount = base_currency_net_amount

    @property
    def base_currency_tax_amount(self):
        """Gets the base_currency_tax_amount of this PostContactOpeningBalancesContactOpeningBalance.  # noqa: E501

        The tax amount of the opening balance in base currency  # noqa: E501

        :return: The base_currency_tax_amount of this PostContactOpeningBalancesContactOpeningBalance.  # noqa: E501
        :rtype: float
        """
        return self._base_currency_tax_amount

    @base_currency_tax_amount.setter
    def base_currency_tax_amount(self, base_currency_tax_amount):
        """Sets the base_currency_tax_amount of this PostContactOpeningBalancesContactOpeningBalance.

        The tax amount of the opening balance in base currency  # noqa: E501

        :param base_currency_tax_amount: The base_currency_tax_amount of this PostContactOpeningBalancesContactOpeningBalance.  # noqa: E501
        :type: float
        """

        self._base_currency_tax_amount = base_currency_tax_amount

    @property
    def base_currency_total_amount(self):
        """Gets the base_currency_total_amount of this PostContactOpeningBalancesContactOpeningBalance.  # noqa: E501

        The total amount of the opening balance in base currency  # noqa: E501

        :return: The base_currency_total_amount of this PostContactOpeningBalancesContactOpeningBalance.  # noqa: E501
        :rtype: float
        """
        return self._base_currency_total_amount

    @base_currency_total_amount.setter
    def base_currency_total_amount(self, base_currency_total_amount):
        """Sets the base_currency_total_amount of this PostContactOpeningBalancesContactOpeningBalance.

        The total amount of the opening balance in base currency  # noqa: E501

        :param base_currency_total_amount: The base_currency_total_amount of this PostContactOpeningBalancesContactOpeningBalance.  # noqa: E501
        :type: float
        """

        self._base_currency_total_amount = base_currency_total_amount

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
        if not isinstance(other, PostContactOpeningBalancesContactOpeningBalance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PostContactOpeningBalancesContactOpeningBalance):
            return True

        return self.to_dict() != other.to_dict()
