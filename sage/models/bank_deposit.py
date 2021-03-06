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


class BankDeposit(object):
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
        'from_bank_account': 'BankAccount',
        'to_bank_account': 'BankAccount',
        'date': 'date',
        'reference': 'str',
        'cash_amount': 'float',
        'cheque_amount': 'float',
        'total_amount': 'float'
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
        'from_bank_account': 'from_bank_account',
        'to_bank_account': 'to_bank_account',
        'date': 'date',
        'reference': 'reference',
        'cash_amount': 'cash_amount',
        'cheque_amount': 'cheque_amount',
        'total_amount': 'total_amount'
    }

    def __init__(self, id=None, displayed_as=None, path=None, created_at=None, updated_at=None, transaction=None, transaction_type=None, deleted_at=None, from_bank_account=None, to_bank_account=None, date=None, reference=None, cash_amount=None, cheque_amount=None, total_amount=None, local_vars_configuration=None):  # noqa: E501
        """BankDeposit - a model defined in OpenAPI"""  # noqa: E501
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
        self._from_bank_account = None
        self._to_bank_account = None
        self._date = None
        self._reference = None
        self._cash_amount = None
        self._cheque_amount = None
        self._total_amount = None
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
        if from_bank_account is not None:
            self.from_bank_account = from_bank_account
        if to_bank_account is not None:
            self.to_bank_account = to_bank_account
        if date is not None:
            self.date = date
        if reference is not None:
            self.reference = reference
        if cash_amount is not None:
            self.cash_amount = cash_amount
        if cheque_amount is not None:
            self.cheque_amount = cheque_amount
        if total_amount is not None:
            self.total_amount = total_amount

    @property
    def id(self):
        """Gets the id of this BankDeposit.  # noqa: E501

        The unique identifier for the item  # noqa: E501

        :return: The id of this BankDeposit.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BankDeposit.

        The unique identifier for the item  # noqa: E501

        :param id: The id of this BankDeposit.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def displayed_as(self):
        """Gets the displayed_as of this BankDeposit.  # noqa: E501

        The name of the resource  # noqa: E501

        :return: The displayed_as of this BankDeposit.  # noqa: E501
        :rtype: str
        """
        return self._displayed_as

    @displayed_as.setter
    def displayed_as(self, displayed_as):
        """Sets the displayed_as of this BankDeposit.

        The name of the resource  # noqa: E501

        :param displayed_as: The displayed_as of this BankDeposit.  # noqa: E501
        :type: str
        """

        self._displayed_as = displayed_as

    @property
    def path(self):
        """Gets the path of this BankDeposit.  # noqa: E501

        The API path for the resource  # noqa: E501

        :return: The path of this BankDeposit.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this BankDeposit.

        The API path for the resource  # noqa: E501

        :param path: The path of this BankDeposit.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def created_at(self):
        """Gets the created_at of this BankDeposit.  # noqa: E501

        The datetime when the item was created  # noqa: E501

        :return: The created_at of this BankDeposit.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this BankDeposit.

        The datetime when the item was created  # noqa: E501

        :param created_at: The created_at of this BankDeposit.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this BankDeposit.  # noqa: E501

        The datetime when the item was last updated  # noqa: E501

        :return: The updated_at of this BankDeposit.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this BankDeposit.

        The datetime when the item was last updated  # noqa: E501

        :param updated_at: The updated_at of this BankDeposit.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def transaction(self):
        """Gets the transaction of this BankDeposit.  # noqa: E501


        :return: The transaction of this BankDeposit.  # noqa: E501
        :rtype: Base
        """
        return self._transaction

    @transaction.setter
    def transaction(self, transaction):
        """Sets the transaction of this BankDeposit.


        :param transaction: The transaction of this BankDeposit.  # noqa: E501
        :type: Base
        """

        self._transaction = transaction

    @property
    def transaction_type(self):
        """Gets the transaction_type of this BankDeposit.  # noqa: E501


        :return: The transaction_type of this BankDeposit.  # noqa: E501
        :rtype: Base
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        """Sets the transaction_type of this BankDeposit.


        :param transaction_type: The transaction_type of this BankDeposit.  # noqa: E501
        :type: Base
        """

        self._transaction_type = transaction_type

    @property
    def deleted_at(self):
        """Gets the deleted_at of this BankDeposit.  # noqa: E501

        The datetime when the item was deleted  # noqa: E501

        :return: The deleted_at of this BankDeposit.  # noqa: E501
        :rtype: datetime
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """Sets the deleted_at of this BankDeposit.

        The datetime when the item was deleted  # noqa: E501

        :param deleted_at: The deleted_at of this BankDeposit.  # noqa: E501
        :type: datetime
        """

        self._deleted_at = deleted_at

    @property
    def from_bank_account(self):
        """Gets the from_bank_account of this BankDeposit.  # noqa: E501


        :return: The from_bank_account of this BankDeposit.  # noqa: E501
        :rtype: BankAccount
        """
        return self._from_bank_account

    @from_bank_account.setter
    def from_bank_account(self, from_bank_account):
        """Sets the from_bank_account of this BankDeposit.


        :param from_bank_account: The from_bank_account of this BankDeposit.  # noqa: E501
        :type: BankAccount
        """

        self._from_bank_account = from_bank_account

    @property
    def to_bank_account(self):
        """Gets the to_bank_account of this BankDeposit.  # noqa: E501


        :return: The to_bank_account of this BankDeposit.  # noqa: E501
        :rtype: BankAccount
        """
        return self._to_bank_account

    @to_bank_account.setter
    def to_bank_account(self, to_bank_account):
        """Sets the to_bank_account of this BankDeposit.


        :param to_bank_account: The to_bank_account of this BankDeposit.  # noqa: E501
        :type: BankAccount
        """

        self._to_bank_account = to_bank_account

    @property
    def date(self):
        """Gets the date of this BankDeposit.  # noqa: E501

        User generated date of transaction, not necessarily when it was created  # noqa: E501

        :return: The date of this BankDeposit.  # noqa: E501
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this BankDeposit.

        User generated date of transaction, not necessarily when it was created  # noqa: E501

        :param date: The date of this BankDeposit.  # noqa: E501
        :type: date
        """

        self._date = date

    @property
    def reference(self):
        """Gets the reference of this BankDeposit.  # noqa: E501

        Reference  # noqa: E501

        :return: The reference of this BankDeposit.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this BankDeposit.

        Reference  # noqa: E501

        :param reference: The reference of this BankDeposit.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                reference is not None and len(reference) > 255):
            raise ValueError("Invalid value for `reference`, length must be less than or equal to `255`")  # noqa: E501

        self._reference = reference

    @property
    def cash_amount(self):
        """Gets the cash_amount of this BankDeposit.  # noqa: E501

        Cash total in the deposit  # noqa: E501

        :return: The cash_amount of this BankDeposit.  # noqa: E501
        :rtype: float
        """
        return self._cash_amount

    @cash_amount.setter
    def cash_amount(self, cash_amount):
        """Sets the cash_amount of this BankDeposit.

        Cash total in the deposit  # noqa: E501

        :param cash_amount: The cash_amount of this BankDeposit.  # noqa: E501
        :type: float
        """

        self._cash_amount = cash_amount

    @property
    def cheque_amount(self):
        """Gets the cheque_amount of this BankDeposit.  # noqa: E501

        Cheque total in the deposit  # noqa: E501

        :return: The cheque_amount of this BankDeposit.  # noqa: E501
        :rtype: float
        """
        return self._cheque_amount

    @cheque_amount.setter
    def cheque_amount(self, cheque_amount):
        """Sets the cheque_amount of this BankDeposit.

        Cheque total in the deposit  # noqa: E501

        :param cheque_amount: The cheque_amount of this BankDeposit.  # noqa: E501
        :type: float
        """

        self._cheque_amount = cheque_amount

    @property
    def total_amount(self):
        """Gets the total_amount of this BankDeposit.  # noqa: E501

        Total of cash and cheques in the deposit  # noqa: E501

        :return: The total_amount of this BankDeposit.  # noqa: E501
        :rtype: float
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """Sets the total_amount of this BankDeposit.

        Total of cash and cheques in the deposit  # noqa: E501

        :param total_amount: The total_amount of this BankDeposit.  # noqa: E501
        :type: float
        """

        self._total_amount = total_amount

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
        if not isinstance(other, BankDeposit):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BankDeposit):
            return True

        return self.to_dict() != other.to_dict()
