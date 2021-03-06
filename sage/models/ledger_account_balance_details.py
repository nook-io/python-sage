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


class LedgerAccountBalanceDetails(object):
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
        'balance': 'float',
        'credit_or_debit': 'str',
        'credits': 'float',
        'debits': 'float',
        'from_date': 'str',
        'to_date': 'str'
    }

    attribute_map = {
        'balance': 'balance',
        'credit_or_debit': 'credit_or_debit',
        'credits': 'credits',
        'debits': 'debits',
        'from_date': 'from_date',
        'to_date': 'to_date'
    }

    def __init__(self, balance=None, credit_or_debit=None, credits=None, debits=None, from_date=None, to_date=None, local_vars_configuration=None):  # noqa: E501
        """LedgerAccountBalanceDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._balance = None
        self._credit_or_debit = None
        self._credits = None
        self._debits = None
        self._from_date = None
        self._to_date = None
        self.discriminator = None

        if balance is not None:
            self.balance = balance
        if credit_or_debit is not None:
            self.credit_or_debit = credit_or_debit
        if credits is not None:
            self.credits = credits
        if debits is not None:
            self.debits = debits
        if from_date is not None:
            self.from_date = from_date
        if to_date is not None:
            self.to_date = to_date

    @property
    def balance(self):
        """Gets the balance of this LedgerAccountBalanceDetails.  # noqa: E501

        The account balance  # noqa: E501

        :return: The balance of this LedgerAccountBalanceDetails.  # noqa: E501
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this LedgerAccountBalanceDetails.

        The account balance  # noqa: E501

        :param balance: The balance of this LedgerAccountBalanceDetails.  # noqa: E501
        :type: float
        """

        self._balance = balance

    @property
    def credit_or_debit(self):
        """Gets the credit_or_debit of this LedgerAccountBalanceDetails.  # noqa: E501

        Is the balance a debit or credit  # noqa: E501

        :return: The credit_or_debit of this LedgerAccountBalanceDetails.  # noqa: E501
        :rtype: str
        """
        return self._credit_or_debit

    @credit_or_debit.setter
    def credit_or_debit(self, credit_or_debit):
        """Sets the credit_or_debit of this LedgerAccountBalanceDetails.

        Is the balance a debit or credit  # noqa: E501

        :param credit_or_debit: The credit_or_debit of this LedgerAccountBalanceDetails.  # noqa: E501
        :type: str
        """

        self._credit_or_debit = credit_or_debit

    @property
    def credits(self):
        """Gets the credits of this LedgerAccountBalanceDetails.  # noqa: E501

        The credit balance  # noqa: E501

        :return: The credits of this LedgerAccountBalanceDetails.  # noqa: E501
        :rtype: float
        """
        return self._credits

    @credits.setter
    def credits(self, credits):
        """Sets the credits of this LedgerAccountBalanceDetails.

        The credit balance  # noqa: E501

        :param credits: The credits of this LedgerAccountBalanceDetails.  # noqa: E501
        :type: float
        """

        self._credits = credits

    @property
    def debits(self):
        """Gets the debits of this LedgerAccountBalanceDetails.  # noqa: E501

        The debit balance  # noqa: E501

        :return: The debits of this LedgerAccountBalanceDetails.  # noqa: E501
        :rtype: float
        """
        return self._debits

    @debits.setter
    def debits(self, debits):
        """Sets the debits of this LedgerAccountBalanceDetails.

        The debit balance  # noqa: E501

        :param debits: The debits of this LedgerAccountBalanceDetails.  # noqa: E501
        :type: float
        """

        self._debits = debits

    @property
    def from_date(self):
        """Gets the from_date of this LedgerAccountBalanceDetails.  # noqa: E501

        The from date filter  # noqa: E501

        :return: The from_date of this LedgerAccountBalanceDetails.  # noqa: E501
        :rtype: str
        """
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        """Sets the from_date of this LedgerAccountBalanceDetails.

        The from date filter  # noqa: E501

        :param from_date: The from_date of this LedgerAccountBalanceDetails.  # noqa: E501
        :type: str
        """

        self._from_date = from_date

    @property
    def to_date(self):
        """Gets the to_date of this LedgerAccountBalanceDetails.  # noqa: E501

        The to date filter  # noqa: E501

        :return: The to_date of this LedgerAccountBalanceDetails.  # noqa: E501
        :rtype: str
        """
        return self._to_date

    @to_date.setter
    def to_date(self, to_date):
        """Sets the to_date of this LedgerAccountBalanceDetails.

        The to date filter  # noqa: E501

        :param to_date: The to_date of this LedgerAccountBalanceDetails.  # noqa: E501
        :type: str
        """

        self._to_date = to_date

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
        if not isinstance(other, LedgerAccountBalanceDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LedgerAccountBalanceDetails):
            return True

        return self.to_dict() != other.to_dict()
