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


class PutBankTransfersBankTransfer(object):
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
        'from_bank_account_id': 'str',
        'to_bank_account_id': 'str',
        'date': 'date',
        'amount': 'float',
        'reference': 'str',
        'description': 'str'
    }

    attribute_map = {
        'from_bank_account_id': 'from_bank_account_id',
        'to_bank_account_id': 'to_bank_account_id',
        'date': 'date',
        'amount': 'amount',
        'reference': 'reference',
        'description': 'description'
    }

    def __init__(self, from_bank_account_id=None, to_bank_account_id=None, date=None, amount=None, reference=None, description=None, local_vars_configuration=None):  # noqa: E501
        """PutBankTransfersBankTransfer - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._from_bank_account_id = None
        self._to_bank_account_id = None
        self._date = None
        self._amount = None
        self._reference = None
        self._description = None
        self.discriminator = None

        if from_bank_account_id is not None:
            self.from_bank_account_id = from_bank_account_id
        if to_bank_account_id is not None:
            self.to_bank_account_id = to_bank_account_id
        if date is not None:
            self.date = date
        if amount is not None:
            self.amount = amount
        if reference is not None:
            self.reference = reference
        if description is not None:
            self.description = description

    @property
    def from_bank_account_id(self):
        """Gets the from_bank_account_id of this PutBankTransfersBankTransfer.  # noqa: E501

        The bank account that the money was transfered from  # noqa: E501

        :return: The from_bank_account_id of this PutBankTransfersBankTransfer.  # noqa: E501
        :rtype: str
        """
        return self._from_bank_account_id

    @from_bank_account_id.setter
    def from_bank_account_id(self, from_bank_account_id):
        """Sets the from_bank_account_id of this PutBankTransfersBankTransfer.

        The bank account that the money was transfered from  # noqa: E501

        :param from_bank_account_id: The from_bank_account_id of this PutBankTransfersBankTransfer.  # noqa: E501
        :type: str
        """

        self._from_bank_account_id = from_bank_account_id

    @property
    def to_bank_account_id(self):
        """Gets the to_bank_account_id of this PutBankTransfersBankTransfer.  # noqa: E501

        The bank account that the money was transfered to  # noqa: E501

        :return: The to_bank_account_id of this PutBankTransfersBankTransfer.  # noqa: E501
        :rtype: str
        """
        return self._to_bank_account_id

    @to_bank_account_id.setter
    def to_bank_account_id(self, to_bank_account_id):
        """Sets the to_bank_account_id of this PutBankTransfersBankTransfer.

        The bank account that the money was transfered to  # noqa: E501

        :param to_bank_account_id: The to_bank_account_id of this PutBankTransfersBankTransfer.  # noqa: E501
        :type: str
        """

        self._to_bank_account_id = to_bank_account_id

    @property
    def date(self):
        """Gets the date of this PutBankTransfersBankTransfer.  # noqa: E501

        The date of the bank transfer  # noqa: E501

        :return: The date of this PutBankTransfersBankTransfer.  # noqa: E501
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this PutBankTransfersBankTransfer.

        The date of the bank transfer  # noqa: E501

        :param date: The date of this PutBankTransfersBankTransfer.  # noqa: E501
        :type: date
        """

        self._date = date

    @property
    def amount(self):
        """Gets the amount of this PutBankTransfersBankTransfer.  # noqa: E501

        The amount of the bank transfer  # noqa: E501

        :return: The amount of this PutBankTransfersBankTransfer.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PutBankTransfersBankTransfer.

        The amount of the bank transfer  # noqa: E501

        :param amount: The amount of this PutBankTransfersBankTransfer.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def reference(self):
        """Gets the reference of this PutBankTransfersBankTransfer.  # noqa: E501

        The reference for the bank transfer  # noqa: E501

        :return: The reference of this PutBankTransfersBankTransfer.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this PutBankTransfersBankTransfer.

        The reference for the bank transfer  # noqa: E501

        :param reference: The reference of this PutBankTransfersBankTransfer.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def description(self):
        """Gets the description of this PutBankTransfersBankTransfer.  # noqa: E501

        The description for the bank transfer  # noqa: E501

        :return: The description of this PutBankTransfersBankTransfer.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PutBankTransfersBankTransfer.

        The description for the bank transfer  # noqa: E501

        :param description: The description of this PutBankTransfersBankTransfer.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if not isinstance(other, PutBankTransfersBankTransfer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PutBankTransfersBankTransfer):
            return True

        return self.to_dict() != other.to_dict()
