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


class PutBankAccountsBankAccount(object):
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
        'bank_account_type_id': 'str',
        'ledger_account_id': 'str',
        'nominal_code': 'int',
        'default_payment_method_id': 'str',
        'gifi_code': 'int',
        'bank_account_details': 'PutBankAccountsBankAccountBankAccountDetails',
        'main_address': 'PostBankAccountsBankAccountMainAddress',
        'main_contact_person': 'PostBankAccountsBankAccountMainContactPerson',
        'journal_code': 'PostJournalsJournalJournalCode'
    }

    attribute_map = {
        'bank_account_type_id': 'bank_account_type_id',
        'ledger_account_id': 'ledger_account_id',
        'nominal_code': 'nominal_code',
        'default_payment_method_id': 'default_payment_method_id',
        'gifi_code': 'gifi_code',
        'bank_account_details': 'bank_account_details',
        'main_address': 'main_address',
        'main_contact_person': 'main_contact_person',
        'journal_code': 'journal_code'
    }

    def __init__(self, bank_account_type_id=None, ledger_account_id=None, nominal_code=None, default_payment_method_id=None, gifi_code=None, bank_account_details=None, main_address=None, main_contact_person=None, journal_code=None, local_vars_configuration=None):  # noqa: E501
        """PutBankAccountsBankAccount - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._bank_account_type_id = None
        self._ledger_account_id = None
        self._nominal_code = None
        self._default_payment_method_id = None
        self._gifi_code = None
        self._bank_account_details = None
        self._main_address = None
        self._main_contact_person = None
        self._journal_code = None
        self.discriminator = None

        if bank_account_type_id is not None:
            self.bank_account_type_id = bank_account_type_id
        if ledger_account_id is not None:
            self.ledger_account_id = ledger_account_id
        if nominal_code is not None:
            self.nominal_code = nominal_code
        if default_payment_method_id is not None:
            self.default_payment_method_id = default_payment_method_id
        if gifi_code is not None:
            self.gifi_code = gifi_code
        if bank_account_details is not None:
            self.bank_account_details = bank_account_details
        if main_address is not None:
            self.main_address = main_address
        if main_contact_person is not None:
            self.main_contact_person = main_contact_person
        if journal_code is not None:
            self.journal_code = journal_code

    @property
    def bank_account_type_id(self):
        """Gets the bank_account_type_id of this PutBankAccountsBankAccount.  # noqa: E501

        The bank account type for the bank account  # noqa: E501

        :return: The bank_account_type_id of this PutBankAccountsBankAccount.  # noqa: E501
        :rtype: str
        """
        return self._bank_account_type_id

    @bank_account_type_id.setter
    def bank_account_type_id(self, bank_account_type_id):
        """Sets the bank_account_type_id of this PutBankAccountsBankAccount.

        The bank account type for the bank account  # noqa: E501

        :param bank_account_type_id: The bank_account_type_id of this PutBankAccountsBankAccount.  # noqa: E501
        :type: str
        """

        self._bank_account_type_id = bank_account_type_id

    @property
    def ledger_account_id(self):
        """Gets the ledger_account_id of this PutBankAccountsBankAccount.  # noqa: E501

        The ID of the Ledger Account.  # noqa: E501

        :return: The ledger_account_id of this PutBankAccountsBankAccount.  # noqa: E501
        :rtype: str
        """
        return self._ledger_account_id

    @ledger_account_id.setter
    def ledger_account_id(self, ledger_account_id):
        """Sets the ledger_account_id of this PutBankAccountsBankAccount.

        The ID of the Ledger Account.  # noqa: E501

        :param ledger_account_id: The ledger_account_id of this PutBankAccountsBankAccount.  # noqa: E501
        :type: str
        """

        self._ledger_account_id = ledger_account_id

    @property
    def nominal_code(self):
        """Gets the nominal_code of this PutBankAccountsBankAccount.  # noqa: E501

        The nominal code of the bank account  # noqa: E501

        :return: The nominal_code of this PutBankAccountsBankAccount.  # noqa: E501
        :rtype: int
        """
        return self._nominal_code

    @nominal_code.setter
    def nominal_code(self, nominal_code):
        """Sets the nominal_code of this PutBankAccountsBankAccount.

        The nominal code of the bank account  # noqa: E501

        :param nominal_code: The nominal_code of this PutBankAccountsBankAccount.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                nominal_code is not None and nominal_code > 99999999):  # noqa: E501
            raise ValueError("Invalid value for `nominal_code`, must be a value less than or equal to `99999999`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                nominal_code is not None and nominal_code < 1):  # noqa: E501
            raise ValueError("Invalid value for `nominal_code`, must be a value greater than or equal to `1`")  # noqa: E501

        self._nominal_code = nominal_code

    @property
    def default_payment_method_id(self):
        """Gets the default_payment_method_id of this PutBankAccountsBankAccount.  # noqa: E501

        The ID of the Default Payment Method.  # noqa: E501

        :return: The default_payment_method_id of this PutBankAccountsBankAccount.  # noqa: E501
        :rtype: str
        """
        return self._default_payment_method_id

    @default_payment_method_id.setter
    def default_payment_method_id(self, default_payment_method_id):
        """Sets the default_payment_method_id of this PutBankAccountsBankAccount.

        The ID of the Default Payment Method.  # noqa: E501

        :param default_payment_method_id: The default_payment_method_id of this PutBankAccountsBankAccount.  # noqa: E501
        :type: str
        """

        self._default_payment_method_id = default_payment_method_id

    @property
    def gifi_code(self):
        """Gets the gifi_code of this PutBankAccountsBankAccount.  # noqa: E501

        The GIFI code of the bank ledger account'  GIFI is short for The General Index of Financial Information and it lets the CRA validate tax information electronically instead of manually. Information from financial statements is categorized under the appropriate 4-digit-long GIFI code and entered on corporate income tax returns. GIFI is needed when filing a T2 income tax return.  _Canada only_   # noqa: E501

        :return: The gifi_code of this PutBankAccountsBankAccount.  # noqa: E501
        :rtype: int
        """
        return self._gifi_code

    @gifi_code.setter
    def gifi_code(self, gifi_code):
        """Sets the gifi_code of this PutBankAccountsBankAccount.

        The GIFI code of the bank ledger account'  GIFI is short for The General Index of Financial Information and it lets the CRA validate tax information electronically instead of manually. Information from financial statements is categorized under the appropriate 4-digit-long GIFI code and entered on corporate income tax returns. GIFI is needed when filing a T2 income tax return.  _Canada only_   # noqa: E501

        :param gifi_code: The gifi_code of this PutBankAccountsBankAccount.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                gifi_code is not None and gifi_code > 9999):  # noqa: E501
            raise ValueError("Invalid value for `gifi_code`, must be a value less than or equal to `9999`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                gifi_code is not None and gifi_code < 1000):  # noqa: E501
            raise ValueError("Invalid value for `gifi_code`, must be a value greater than or equal to `1000`")  # noqa: E501

        self._gifi_code = gifi_code

    @property
    def bank_account_details(self):
        """Gets the bank_account_details of this PutBankAccountsBankAccount.  # noqa: E501


        :return: The bank_account_details of this PutBankAccountsBankAccount.  # noqa: E501
        :rtype: PutBankAccountsBankAccountBankAccountDetails
        """
        return self._bank_account_details

    @bank_account_details.setter
    def bank_account_details(self, bank_account_details):
        """Sets the bank_account_details of this PutBankAccountsBankAccount.


        :param bank_account_details: The bank_account_details of this PutBankAccountsBankAccount.  # noqa: E501
        :type: PutBankAccountsBankAccountBankAccountDetails
        """

        self._bank_account_details = bank_account_details

    @property
    def main_address(self):
        """Gets the main_address of this PutBankAccountsBankAccount.  # noqa: E501


        :return: The main_address of this PutBankAccountsBankAccount.  # noqa: E501
        :rtype: PostBankAccountsBankAccountMainAddress
        """
        return self._main_address

    @main_address.setter
    def main_address(self, main_address):
        """Sets the main_address of this PutBankAccountsBankAccount.


        :param main_address: The main_address of this PutBankAccountsBankAccount.  # noqa: E501
        :type: PostBankAccountsBankAccountMainAddress
        """

        self._main_address = main_address

    @property
    def main_contact_person(self):
        """Gets the main_contact_person of this PutBankAccountsBankAccount.  # noqa: E501


        :return: The main_contact_person of this PutBankAccountsBankAccount.  # noqa: E501
        :rtype: PostBankAccountsBankAccountMainContactPerson
        """
        return self._main_contact_person

    @main_contact_person.setter
    def main_contact_person(self, main_contact_person):
        """Sets the main_contact_person of this PutBankAccountsBankAccount.


        :param main_contact_person: The main_contact_person of this PutBankAccountsBankAccount.  # noqa: E501
        :type: PostBankAccountsBankAccountMainContactPerson
        """

        self._main_contact_person = main_contact_person

    @property
    def journal_code(self):
        """Gets the journal_code of this PutBankAccountsBankAccount.  # noqa: E501


        :return: The journal_code of this PutBankAccountsBankAccount.  # noqa: E501
        :rtype: PostJournalsJournalJournalCode
        """
        return self._journal_code

    @journal_code.setter
    def journal_code(self, journal_code):
        """Sets the journal_code of this PutBankAccountsBankAccount.


        :param journal_code: The journal_code of this PutBankAccountsBankAccount.  # noqa: E501
        :type: PostJournalsJournalJournalCode
        """

        self._journal_code = journal_code

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
        if not isinstance(other, PutBankAccountsBankAccount):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PutBankAccountsBankAccount):
            return True

        return self.to_dict() != other.to_dict()
