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


class PutBankOpeningBalancesBankOpeningBalance(object):
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
        'bank_account_id': 'str',
        'date': 'date',
        'debit': 'float',
        'credit': 'float',
        'transaction_type_id': 'str'
    }

    attribute_map = {
        'bank_account_id': 'bank_account_id',
        'date': 'date',
        'debit': 'debit',
        'credit': 'credit',
        'transaction_type_id': 'transaction_type_id'
    }

    def __init__(self, bank_account_id=None, date=None, debit=None, credit=None, transaction_type_id=None, local_vars_configuration=None):  # noqa: E501
        """PutBankOpeningBalancesBankOpeningBalance - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._bank_account_id = None
        self._date = None
        self._debit = None
        self._credit = None
        self._transaction_type_id = None
        self.discriminator = None

        if bank_account_id is not None:
            self.bank_account_id = bank_account_id
        if date is not None:
            self.date = date
        if debit is not None:
            self.debit = debit
        if credit is not None:
            self.credit = credit
        if transaction_type_id is not None:
            self.transaction_type_id = transaction_type_id

    @property
    def bank_account_id(self):
        """Gets the bank_account_id of this PutBankOpeningBalancesBankOpeningBalance.  # noqa: E501

        The bank account the opening balance relates to  # noqa: E501

        :return: The bank_account_id of this PutBankOpeningBalancesBankOpeningBalance.  # noqa: E501
        :rtype: str
        """
        return self._bank_account_id

    @bank_account_id.setter
    def bank_account_id(self, bank_account_id):
        """Sets the bank_account_id of this PutBankOpeningBalancesBankOpeningBalance.

        The bank account the opening balance relates to  # noqa: E501

        :param bank_account_id: The bank_account_id of this PutBankOpeningBalancesBankOpeningBalance.  # noqa: E501
        :type: str
        """

        self._bank_account_id = bank_account_id

    @property
    def date(self):
        """Gets the date of this PutBankOpeningBalancesBankOpeningBalance.  # noqa: E501

        The date of the opening balance  # noqa: E501

        :return: The date of this PutBankOpeningBalancesBankOpeningBalance.  # noqa: E501
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this PutBankOpeningBalancesBankOpeningBalance.

        The date of the opening balance  # noqa: E501

        :param date: The date of this PutBankOpeningBalancesBankOpeningBalance.  # noqa: E501
        :type: date
        """

        self._date = date

    @property
    def debit(self):
        """Gets the debit of this PutBankOpeningBalancesBankOpeningBalance.  # noqa: E501

        The debit amount of the opening balance  # noqa: E501

        :return: The debit of this PutBankOpeningBalancesBankOpeningBalance.  # noqa: E501
        :rtype: float
        """
        return self._debit

    @debit.setter
    def debit(self, debit):
        """Sets the debit of this PutBankOpeningBalancesBankOpeningBalance.

        The debit amount of the opening balance  # noqa: E501

        :param debit: The debit of this PutBankOpeningBalancesBankOpeningBalance.  # noqa: E501
        :type: float
        """

        self._debit = debit

    @property
    def credit(self):
        """Gets the credit of this PutBankOpeningBalancesBankOpeningBalance.  # noqa: E501

        The credit amount of the opening balance  # noqa: E501

        :return: The credit of this PutBankOpeningBalancesBankOpeningBalance.  # noqa: E501
        :rtype: float
        """
        return self._credit

    @credit.setter
    def credit(self, credit):
        """Sets the credit of this PutBankOpeningBalancesBankOpeningBalance.

        The credit amount of the opening balance  # noqa: E501

        :param credit: The credit of this PutBankOpeningBalancesBankOpeningBalance.  # noqa: E501
        :type: float
        """

        self._credit = credit

    @property
    def transaction_type_id(self):
        """Gets the transaction_type_id of this PutBankOpeningBalancesBankOpeningBalance.  # noqa: E501

        The ID of the Transaction Type.  # noqa: E501

        :return: The transaction_type_id of this PutBankOpeningBalancesBankOpeningBalance.  # noqa: E501
        :rtype: str
        """
        return self._transaction_type_id

    @transaction_type_id.setter
    def transaction_type_id(self, transaction_type_id):
        """Sets the transaction_type_id of this PutBankOpeningBalancesBankOpeningBalance.

        The ID of the Transaction Type.  # noqa: E501

        :param transaction_type_id: The transaction_type_id of this PutBankOpeningBalancesBankOpeningBalance.  # noqa: E501
        :type: str
        """

        self._transaction_type_id = transaction_type_id

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
        if not isinstance(other, PutBankOpeningBalancesBankOpeningBalance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PutBankOpeningBalancesBankOpeningBalance):
            return True

        return self.to_dict() != other.to_dict()
