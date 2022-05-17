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


class BankAccount(object):
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
        'deleted_at': 'datetime',
        'bank_account_details': 'BankAccountDetails',
        'ledger_account': 'Base',
        'bank_account_type': 'Base',
        'balance': 'float',
        'main_address': 'Address',
        'main_contact_person': 'BankAccountContact',
        'nominal_code': 'int',
        'editable': 'bool',
        'deletable': 'bool',
        'journal_code': 'JournalCode',
        'default_payment_method': 'Base',
        'gifi_code': 'int'
    }

    attribute_map = {
        'id': 'id',
        'displayed_as': 'displayed_as',
        'path': '$path',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'deleted_at': 'deleted_at',
        'bank_account_details': 'bank_account_details',
        'ledger_account': 'ledger_account',
        'bank_account_type': 'bank_account_type',
        'balance': 'balance',
        'main_address': 'main_address',
        'main_contact_person': 'main_contact_person',
        'nominal_code': 'nominal_code',
        'editable': 'editable',
        'deletable': 'deletable',
        'journal_code': 'journal_code',
        'default_payment_method': 'default_payment_method',
        'gifi_code': 'gifi_code'
    }

    def __init__(self, id=None, displayed_as=None, path=None, created_at=None, updated_at=None, deleted_at=None, bank_account_details=None, ledger_account=None, bank_account_type=None, balance=None, main_address=None, main_contact_person=None, nominal_code=None, editable=None, deletable=None, journal_code=None, default_payment_method=None, gifi_code=None, local_vars_configuration=None):  # noqa: E501
        """BankAccount - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._displayed_as = None
        self._path = None
        self._created_at = None
        self._updated_at = None
        self._deleted_at = None
        self._bank_account_details = None
        self._ledger_account = None
        self._bank_account_type = None
        self._balance = None
        self._main_address = None
        self._main_contact_person = None
        self._nominal_code = None
        self._editable = None
        self._deletable = None
        self._journal_code = None
        self._default_payment_method = None
        self._gifi_code = None
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
        if deleted_at is not None:
            self.deleted_at = deleted_at
        if bank_account_details is not None:
            self.bank_account_details = bank_account_details
        if ledger_account is not None:
            self.ledger_account = ledger_account
        if bank_account_type is not None:
            self.bank_account_type = bank_account_type
        if balance is not None:
            self.balance = balance
        if main_address is not None:
            self.main_address = main_address
        if main_contact_person is not None:
            self.main_contact_person = main_contact_person
        if nominal_code is not None:
            self.nominal_code = nominal_code
        if editable is not None:
            self.editable = editable
        if deletable is not None:
            self.deletable = deletable
        if journal_code is not None:
            self.journal_code = journal_code
        if default_payment_method is not None:
            self.default_payment_method = default_payment_method
        if gifi_code is not None:
            self.gifi_code = gifi_code

    @property
    def id(self):
        """Gets the id of this BankAccount.  # noqa: E501

        The unique identifier for the item  # noqa: E501

        :return: The id of this BankAccount.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BankAccount.

        The unique identifier for the item  # noqa: E501

        :param id: The id of this BankAccount.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def displayed_as(self):
        """Gets the displayed_as of this BankAccount.  # noqa: E501

        The name of the resource  # noqa: E501

        :return: The displayed_as of this BankAccount.  # noqa: E501
        :rtype: str
        """
        return self._displayed_as

    @displayed_as.setter
    def displayed_as(self, displayed_as):
        """Sets the displayed_as of this BankAccount.

        The name of the resource  # noqa: E501

        :param displayed_as: The displayed_as of this BankAccount.  # noqa: E501
        :type: str
        """

        self._displayed_as = displayed_as

    @property
    def path(self):
        """Gets the path of this BankAccount.  # noqa: E501

        The API path for the resource  # noqa: E501

        :return: The path of this BankAccount.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this BankAccount.

        The API path for the resource  # noqa: E501

        :param path: The path of this BankAccount.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def created_at(self):
        """Gets the created_at of this BankAccount.  # noqa: E501

        The datetime when the item was created  # noqa: E501

        :return: The created_at of this BankAccount.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this BankAccount.

        The datetime when the item was created  # noqa: E501

        :param created_at: The created_at of this BankAccount.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this BankAccount.  # noqa: E501

        The datetime when the item was last updated  # noqa: E501

        :return: The updated_at of this BankAccount.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this BankAccount.

        The datetime when the item was last updated  # noqa: E501

        :param updated_at: The updated_at of this BankAccount.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def deleted_at(self):
        """Gets the deleted_at of this BankAccount.  # noqa: E501

        The datetime when the item was deleted  # noqa: E501

        :return: The deleted_at of this BankAccount.  # noqa: E501
        :rtype: datetime
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """Sets the deleted_at of this BankAccount.

        The datetime when the item was deleted  # noqa: E501

        :param deleted_at: The deleted_at of this BankAccount.  # noqa: E501
        :type: datetime
        """

        self._deleted_at = deleted_at

    @property
    def bank_account_details(self):
        """Gets the bank_account_details of this BankAccount.  # noqa: E501


        :return: The bank_account_details of this BankAccount.  # noqa: E501
        :rtype: BankAccountDetails
        """
        return self._bank_account_details

    @bank_account_details.setter
    def bank_account_details(self, bank_account_details):
        """Sets the bank_account_details of this BankAccount.


        :param bank_account_details: The bank_account_details of this BankAccount.  # noqa: E501
        :type: BankAccountDetails
        """

        self._bank_account_details = bank_account_details

    @property
    def ledger_account(self):
        """Gets the ledger_account of this BankAccount.  # noqa: E501


        :return: The ledger_account of this BankAccount.  # noqa: E501
        :rtype: Base
        """
        return self._ledger_account

    @ledger_account.setter
    def ledger_account(self, ledger_account):
        """Sets the ledger_account of this BankAccount.


        :param ledger_account: The ledger_account of this BankAccount.  # noqa: E501
        :type: Base
        """

        self._ledger_account = ledger_account

    @property
    def bank_account_type(self):
        """Gets the bank_account_type of this BankAccount.  # noqa: E501


        :return: The bank_account_type of this BankAccount.  # noqa: E501
        :rtype: Base
        """
        return self._bank_account_type

    @bank_account_type.setter
    def bank_account_type(self, bank_account_type):
        """Sets the bank_account_type of this BankAccount.


        :param bank_account_type: The bank_account_type of this BankAccount.  # noqa: E501
        :type: Base
        """

        self._bank_account_type = bank_account_type

    @property
    def balance(self):
        """Gets the balance of this BankAccount.  # noqa: E501

        The bank account balance  # noqa: E501

        :return: The balance of this BankAccount.  # noqa: E501
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this BankAccount.

        The bank account balance  # noqa: E501

        :param balance: The balance of this BankAccount.  # noqa: E501
        :type: float
        """

        self._balance = balance

    @property
    def main_address(self):
        """Gets the main_address of this BankAccount.  # noqa: E501


        :return: The main_address of this BankAccount.  # noqa: E501
        :rtype: Address
        """
        return self._main_address

    @main_address.setter
    def main_address(self, main_address):
        """Sets the main_address of this BankAccount.


        :param main_address: The main_address of this BankAccount.  # noqa: E501
        :type: Address
        """

        self._main_address = main_address

    @property
    def main_contact_person(self):
        """Gets the main_contact_person of this BankAccount.  # noqa: E501


        :return: The main_contact_person of this BankAccount.  # noqa: E501
        :rtype: BankAccountContact
        """
        return self._main_contact_person

    @main_contact_person.setter
    def main_contact_person(self, main_contact_person):
        """Sets the main_contact_person of this BankAccount.


        :param main_contact_person: The main_contact_person of this BankAccount.  # noqa: E501
        :type: BankAccountContact
        """

        self._main_contact_person = main_contact_person

    @property
    def nominal_code(self):
        """Gets the nominal_code of this BankAccount.  # noqa: E501

        The nominal code of the bank account  # noqa: E501

        :return: The nominal_code of this BankAccount.  # noqa: E501
        :rtype: int
        """
        return self._nominal_code

    @nominal_code.setter
    def nominal_code(self, nominal_code):
        """Sets the nominal_code of this BankAccount.

        The nominal code of the bank account  # noqa: E501

        :param nominal_code: The nominal_code of this BankAccount.  # noqa: E501
        :type: int
        """

        self._nominal_code = nominal_code

    @property
    def editable(self):
        """Gets the editable of this BankAccount.  # noqa: E501

        Indicates whether or not the bank account can be edited  # noqa: E501

        :return: The editable of this BankAccount.  # noqa: E501
        :rtype: bool
        """
        return self._editable

    @editable.setter
    def editable(self, editable):
        """Sets the editable of this BankAccount.

        Indicates whether or not the bank account can be edited  # noqa: E501

        :param editable: The editable of this BankAccount.  # noqa: E501
        :type: bool
        """

        self._editable = editable

    @property
    def deletable(self):
        """Gets the deletable of this BankAccount.  # noqa: E501

        Indicates whether or not the bank account can be deleted  # noqa: E501

        :return: The deletable of this BankAccount.  # noqa: E501
        :rtype: bool
        """
        return self._deletable

    @deletable.setter
    def deletable(self, deletable):
        """Sets the deletable of this BankAccount.

        Indicates whether or not the bank account can be deleted  # noqa: E501

        :param deletable: The deletable of this BankAccount.  # noqa: E501
        :type: bool
        """

        self._deletable = deletable

    @property
    def journal_code(self):
        """Gets the journal_code of this BankAccount.  # noqa: E501


        :return: The journal_code of this BankAccount.  # noqa: E501
        :rtype: JournalCode
        """
        return self._journal_code

    @journal_code.setter
    def journal_code(self, journal_code):
        """Sets the journal_code of this BankAccount.


        :param journal_code: The journal_code of this BankAccount.  # noqa: E501
        :type: JournalCode
        """

        self._journal_code = journal_code

    @property
    def default_payment_method(self):
        """Gets the default_payment_method of this BankAccount.  # noqa: E501


        :return: The default_payment_method of this BankAccount.  # noqa: E501
        :rtype: Base
        """
        return self._default_payment_method

    @default_payment_method.setter
    def default_payment_method(self, default_payment_method):
        """Sets the default_payment_method of this BankAccount.


        :param default_payment_method: The default_payment_method of this BankAccount.  # noqa: E501
        :type: Base
        """

        self._default_payment_method = default_payment_method

    @property
    def gifi_code(self):
        """Gets the gifi_code of this BankAccount.  # noqa: E501

        The GIFI code of the bank ledger account'  GIFI is short for The General Index of Financial Information and it lets the CRA validate tax information electronically instead of manually. Information from financial statements is categorized under the appropriate 4-digit-long GIFI code and entered on corporate income tax returns. GIFI is needed when filing a T2 income tax return.  _Canada only_   # noqa: E501

        :return: The gifi_code of this BankAccount.  # noqa: E501
        :rtype: int
        """
        return self._gifi_code

    @gifi_code.setter
    def gifi_code(self, gifi_code):
        """Sets the gifi_code of this BankAccount.

        The GIFI code of the bank ledger account'  GIFI is short for The General Index of Financial Information and it lets the CRA validate tax information electronically instead of manually. Information from financial statements is categorized under the appropriate 4-digit-long GIFI code and entered on corporate income tax returns. GIFI is needed when filing a T2 income tax return.  _Canada only_   # noqa: E501

        :param gifi_code: The gifi_code of this BankAccount.  # noqa: E501
        :type: int
        """

        self._gifi_code = gifi_code

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
        if not isinstance(other, BankAccount):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BankAccount):
            return True

        return self.to_dict() != other.to_dict()
