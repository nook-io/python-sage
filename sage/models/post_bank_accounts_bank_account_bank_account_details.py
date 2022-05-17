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


class PostBankAccountsBankAccountBankAccountDetails(object):
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
        'account_name': 'str',
        'account_number': 'str',
        'sort_code': 'str',
        'bic': 'str',
        'iban': 'str'
    }

    attribute_map = {
        'account_name': 'account_name',
        'account_number': 'account_number',
        'sort_code': 'sort_code',
        'bic': 'bic',
        'iban': 'iban'
    }

    def __init__(self, account_name=None, account_number=None, sort_code=None, bic=None, iban=None, local_vars_configuration=None):  # noqa: E501
        """PostBankAccountsBankAccountBankAccountDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_name = None
        self._account_number = None
        self._sort_code = None
        self._bic = None
        self._iban = None
        self.discriminator = None

        self.account_name = account_name
        if account_number is not None:
            self.account_number = account_number
        if sort_code is not None:
            self.sort_code = sort_code
        if bic is not None:
            self.bic = bic
        if iban is not None:
            self.iban = iban

    @property
    def account_name(self):
        """Gets the account_name of this PostBankAccountsBankAccountBankAccountDetails.  # noqa: E501

        The account name  # noqa: E501

        :return: The account_name of this PostBankAccountsBankAccountBankAccountDetails.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this PostBankAccountsBankAccountBankAccountDetails.

        The account name  # noqa: E501

        :param account_name: The account_name of this PostBankAccountsBankAccountBankAccountDetails.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and account_name is None:  # noqa: E501
            raise ValueError("Invalid value for `account_name`, must not be `None`")  # noqa: E501

        self._account_name = account_name

    @property
    def account_number(self):
        """Gets the account_number of this PostBankAccountsBankAccountBankAccountDetails.  # noqa: E501

        The account number  # noqa: E501

        :return: The account_number of this PostBankAccountsBankAccountBankAccountDetails.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this PostBankAccountsBankAccountBankAccountDetails.

        The account number  # noqa: E501

        :param account_number: The account_number of this PostBankAccountsBankAccountBankAccountDetails.  # noqa: E501
        :type: str
        """

        self._account_number = account_number

    @property
    def sort_code(self):
        """Gets the sort_code of this PostBankAccountsBankAccountBankAccountDetails.  # noqa: E501

        The sort code  # noqa: E501

        :return: The sort_code of this PostBankAccountsBankAccountBankAccountDetails.  # noqa: E501
        :rtype: str
        """
        return self._sort_code

    @sort_code.setter
    def sort_code(self, sort_code):
        """Sets the sort_code of this PostBankAccountsBankAccountBankAccountDetails.

        The sort code  # noqa: E501

        :param sort_code: The sort_code of this PostBankAccountsBankAccountBankAccountDetails.  # noqa: E501
        :type: str
        """

        self._sort_code = sort_code

    @property
    def bic(self):
        """Gets the bic of this PostBankAccountsBankAccountBankAccountDetails.  # noqa: E501

        The bic  # noqa: E501

        :return: The bic of this PostBankAccountsBankAccountBankAccountDetails.  # noqa: E501
        :rtype: str
        """
        return self._bic

    @bic.setter
    def bic(self, bic):
        """Sets the bic of this PostBankAccountsBankAccountBankAccountDetails.

        The bic  # noqa: E501

        :param bic: The bic of this PostBankAccountsBankAccountBankAccountDetails.  # noqa: E501
        :type: str
        """

        self._bic = bic

    @property
    def iban(self):
        """Gets the iban of this PostBankAccountsBankAccountBankAccountDetails.  # noqa: E501

        The iban  # noqa: E501

        :return: The iban of this PostBankAccountsBankAccountBankAccountDetails.  # noqa: E501
        :rtype: str
        """
        return self._iban

    @iban.setter
    def iban(self, iban):
        """Sets the iban of this PostBankAccountsBankAccountBankAccountDetails.

        The iban  # noqa: E501

        :param iban: The iban of this PostBankAccountsBankAccountBankAccountDetails.  # noqa: E501
        :type: str
        """

        self._iban = iban

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
        if not isinstance(other, PostBankAccountsBankAccountBankAccountDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PostBankAccountsBankAccountBankAccountDetails):
            return True

        return self.to_dict() != other.to_dict()
