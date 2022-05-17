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


class PutAddressesAddress(object):
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
        'address_type_id': 'str',
        'name': 'str',
        'is_main_address': 'bool',
        'address_line_1': 'str',
        'address_line_2': 'str',
        'city': 'str',
        'postal_code': 'str',
        'country_id': 'str',
        'bank_account_id': 'str',
        'contact_id': 'str',
        'region': 'str',
        'country_group_id': 'str'
    }

    attribute_map = {
        'address_type_id': 'address_type_id',
        'name': 'name',
        'is_main_address': 'is_main_address',
        'address_line_1': 'address_line_1',
        'address_line_2': 'address_line_2',
        'city': 'city',
        'postal_code': 'postal_code',
        'country_id': 'country_id',
        'bank_account_id': 'bank_account_id',
        'contact_id': 'contact_id',
        'region': 'region',
        'country_group_id': 'country_group_id'
    }

    def __init__(self, address_type_id=None, name=None, is_main_address=None, address_line_1=None, address_line_2=None, city=None, postal_code=None, country_id=None, bank_account_id=None, contact_id=None, region=None, country_group_id=None, local_vars_configuration=None):  # noqa: E501
        """PutAddressesAddress - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._address_type_id = None
        self._name = None
        self._is_main_address = None
        self._address_line_1 = None
        self._address_line_2 = None
        self._city = None
        self._postal_code = None
        self._country_id = None
        self._bank_account_id = None
        self._contact_id = None
        self._region = None
        self._country_group_id = None
        self.discriminator = None

        if address_type_id is not None:
            self.address_type_id = address_type_id
        if name is not None:
            self.name = name
        if is_main_address is not None:
            self.is_main_address = is_main_address
        if address_line_1 is not None:
            self.address_line_1 = address_line_1
        if address_line_2 is not None:
            self.address_line_2 = address_line_2
        if city is not None:
            self.city = city
        if postal_code is not None:
            self.postal_code = postal_code
        if country_id is not None:
            self.country_id = country_id
        if bank_account_id is not None:
            self.bank_account_id = bank_account_id
        if contact_id is not None:
            self.contact_id = contact_id
        if region is not None:
            self.region = region
        if country_group_id is not None:
            self.country_group_id = country_group_id

    @property
    def address_type_id(self):
        """Gets the address_type_id of this PutAddressesAddress.  # noqa: E501

        Defines the nature of the address (Shipping, Billing, Head Office etc.).<br>Start defaults to \"Sales\" for Customers and \"Purchasing\" for Vendors  # noqa: E501

        :return: The address_type_id of this PutAddressesAddress.  # noqa: E501
        :rtype: str
        """
        return self._address_type_id

    @address_type_id.setter
    def address_type_id(self, address_type_id):
        """Sets the address_type_id of this PutAddressesAddress.

        Defines the nature of the address (Shipping, Billing, Head Office etc.).<br>Start defaults to \"Sales\" for Customers and \"Purchasing\" for Vendors  # noqa: E501

        :param address_type_id: The address_type_id of this PutAddressesAddress.  # noqa: E501
        :type: str
        """

        self._address_type_id = address_type_id

    @property
    def name(self):
        """Gets the name of this PutAddressesAddress.  # noqa: E501

        The custom name of the address  # noqa: E501

        :return: The name of this PutAddressesAddress.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PutAddressesAddress.

        The custom name of the address  # noqa: E501

        :param name: The name of this PutAddressesAddress.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def is_main_address(self):
        """Gets the is_main_address of this PutAddressesAddress.  # noqa: E501

        Specifies the address as the contact's main address. Only a single address can exist for a contact in Start so this is always true when returned by the API but cannot be seen in the UI  # noqa: E501

        :return: The is_main_address of this PutAddressesAddress.  # noqa: E501
        :rtype: bool
        """
        return self._is_main_address

    @is_main_address.setter
    def is_main_address(self, is_main_address):
        """Sets the is_main_address of this PutAddressesAddress.

        Specifies the address as the contact's main address. Only a single address can exist for a contact in Start so this is always true when returned by the API but cannot be seen in the UI  # noqa: E501

        :param is_main_address: The is_main_address of this PutAddressesAddress.  # noqa: E501
        :type: bool
        """

        self._is_main_address = is_main_address

    @property
    def address_line_1(self):
        """Gets the address_line_1 of this PutAddressesAddress.  # noqa: E501

        The first line of the address  # noqa: E501

        :return: The address_line_1 of this PutAddressesAddress.  # noqa: E501
        :rtype: str
        """
        return self._address_line_1

    @address_line_1.setter
    def address_line_1(self, address_line_1):
        """Sets the address_line_1 of this PutAddressesAddress.

        The first line of the address  # noqa: E501

        :param address_line_1: The address_line_1 of this PutAddressesAddress.  # noqa: E501
        :type: str
        """

        self._address_line_1 = address_line_1

    @property
    def address_line_2(self):
        """Gets the address_line_2 of this PutAddressesAddress.  # noqa: E501

        The second line of the address  # noqa: E501

        :return: The address_line_2 of this PutAddressesAddress.  # noqa: E501
        :rtype: str
        """
        return self._address_line_2

    @address_line_2.setter
    def address_line_2(self, address_line_2):
        """Sets the address_line_2 of this PutAddressesAddress.

        The second line of the address  # noqa: E501

        :param address_line_2: The address_line_2 of this PutAddressesAddress.  # noqa: E501
        :type: str
        """

        self._address_line_2 = address_line_2

    @property
    def city(self):
        """Gets the city of this PutAddressesAddress.  # noqa: E501

        The address town/city  # noqa: E501

        :return: The city of this PutAddressesAddress.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this PutAddressesAddress.

        The address town/city  # noqa: E501

        :param city: The city of this PutAddressesAddress.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def postal_code(self):
        """Gets the postal_code of this PutAddressesAddress.  # noqa: E501

        The address postal code/zipcode  # noqa: E501

        :return: The postal_code of this PutAddressesAddress.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this PutAddressesAddress.

        The address postal code/zipcode  # noqa: E501

        :param postal_code: The postal_code of this PutAddressesAddress.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def country_id(self):
        """Gets the country_id of this PutAddressesAddress.  # noqa: E501

        The ID of the Country.  # noqa: E501

        :return: The country_id of this PutAddressesAddress.  # noqa: E501
        :rtype: str
        """
        return self._country_id

    @country_id.setter
    def country_id(self, country_id):
        """Sets the country_id of this PutAddressesAddress.

        The ID of the Country.  # noqa: E501

        :param country_id: The country_id of this PutAddressesAddress.  # noqa: E501
        :type: str
        """

        self._country_id = country_id

    @property
    def bank_account_id(self):
        """Gets the bank_account_id of this PutAddressesAddress.  # noqa: E501

        The related bank account of the address, if the address belongs to a bank account.  # noqa: E501

        :return: The bank_account_id of this PutAddressesAddress.  # noqa: E501
        :rtype: str
        """
        return self._bank_account_id

    @bank_account_id.setter
    def bank_account_id(self, bank_account_id):
        """Sets the bank_account_id of this PutAddressesAddress.

        The related bank account of the address, if the address belongs to a bank account.  # noqa: E501

        :param bank_account_id: The bank_account_id of this PutAddressesAddress.  # noqa: E501
        :type: str
        """

        self._bank_account_id = bank_account_id

    @property
    def contact_id(self):
        """Gets the contact_id of this PutAddressesAddress.  # noqa: E501

        The related contact of the address, if the address belongs to a contact.  # noqa: E501

        :return: The contact_id of this PutAddressesAddress.  # noqa: E501
        :rtype: str
        """
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        """Sets the contact_id of this PutAddressesAddress.

        The related contact of the address, if the address belongs to a contact.  # noqa: E501

        :param contact_id: The contact_id of this PutAddressesAddress.  # noqa: E501
        :type: str
        """

        self._contact_id = contact_id

    @property
    def region(self):
        """Gets the region of this PutAddressesAddress.  # noqa: E501

        The address state/province/region  # noqa: E501

        :return: The region of this PutAddressesAddress.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this PutAddressesAddress.

        The address state/province/region  # noqa: E501

        :param region: The region of this PutAddressesAddress.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def country_group_id(self):
        """Gets the country_group_id of this PutAddressesAddress.  # noqa: E501

        The ID of the Country Group.  # noqa: E501

        :return: The country_group_id of this PutAddressesAddress.  # noqa: E501
        :rtype: str
        """
        return self._country_group_id

    @country_group_id.setter
    def country_group_id(self, country_group_id):
        """Sets the country_group_id of this PutAddressesAddress.

        The ID of the Country Group.  # noqa: E501

        :param country_group_id: The country_group_id of this PutAddressesAddress.  # noqa: E501
        :type: str
        """

        self._country_group_id = country_group_id

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
        if not isinstance(other, PutAddressesAddress):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PutAddressesAddress):
            return True

        return self.to_dict() != other.to_dict()
