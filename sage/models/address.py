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


class Address(object):
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
        'address_line_1': 'str',
        'address_line_2': 'str',
        'city': 'str',
        'postal_code': 'str',
        'country': 'Base',
        'deleted_at': 'datetime',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'bank_account': 'Base',
        'contact': 'Base',
        'address_type': 'Base',
        'name': 'str',
        'region': 'str',
        'country_group': 'Base',
        'is_main_address': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'displayed_as': 'displayed_as',
        'path': '$path',
        'address_line_1': 'address_line_1',
        'address_line_2': 'address_line_2',
        'city': 'city',
        'postal_code': 'postal_code',
        'country': 'country',
        'deleted_at': 'deleted_at',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'bank_account': 'bank_account',
        'contact': 'contact',
        'address_type': 'address_type',
        'name': 'name',
        'region': 'region',
        'country_group': 'country_group',
        'is_main_address': 'is_main_address'
    }

    def __init__(self, id=None, displayed_as=None, path=None, address_line_1=None, address_line_2=None, city=None, postal_code=None, country=None, deleted_at=None, created_at=None, updated_at=None, bank_account=None, contact=None, address_type=None, name=None, region=None, country_group=None, is_main_address=None, local_vars_configuration=None):  # noqa: E501
        """Address - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._displayed_as = None
        self._path = None
        self._address_line_1 = None
        self._address_line_2 = None
        self._city = None
        self._postal_code = None
        self._country = None
        self._deleted_at = None
        self._created_at = None
        self._updated_at = None
        self._bank_account = None
        self._contact = None
        self._address_type = None
        self._name = None
        self._region = None
        self._country_group = None
        self._is_main_address = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if displayed_as is not None:
            self.displayed_as = displayed_as
        if path is not None:
            self.path = path
        if address_line_1 is not None:
            self.address_line_1 = address_line_1
        if address_line_2 is not None:
            self.address_line_2 = address_line_2
        if city is not None:
            self.city = city
        if postal_code is not None:
            self.postal_code = postal_code
        if country is not None:
            self.country = country
        if deleted_at is not None:
            self.deleted_at = deleted_at
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if bank_account is not None:
            self.bank_account = bank_account
        if contact is not None:
            self.contact = contact
        if address_type is not None:
            self.address_type = address_type
        if name is not None:
            self.name = name
        if region is not None:
            self.region = region
        if country_group is not None:
            self.country_group = country_group
        if is_main_address is not None:
            self.is_main_address = is_main_address

    @property
    def id(self):
        """Gets the id of this Address.  # noqa: E501

        The unique identifier for the item  # noqa: E501

        :return: The id of this Address.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Address.

        The unique identifier for the item  # noqa: E501

        :param id: The id of this Address.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def displayed_as(self):
        """Gets the displayed_as of this Address.  # noqa: E501

        The name of the resource  # noqa: E501

        :return: The displayed_as of this Address.  # noqa: E501
        :rtype: str
        """
        return self._displayed_as

    @displayed_as.setter
    def displayed_as(self, displayed_as):
        """Sets the displayed_as of this Address.

        The name of the resource  # noqa: E501

        :param displayed_as: The displayed_as of this Address.  # noqa: E501
        :type: str
        """

        self._displayed_as = displayed_as

    @property
    def path(self):
        """Gets the path of this Address.  # noqa: E501

        The API path for the resource  # noqa: E501

        :return: The path of this Address.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this Address.

        The API path for the resource  # noqa: E501

        :param path: The path of this Address.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def address_line_1(self):
        """Gets the address_line_1 of this Address.  # noqa: E501

        The first line of the address  # noqa: E501

        :return: The address_line_1 of this Address.  # noqa: E501
        :rtype: str
        """
        return self._address_line_1

    @address_line_1.setter
    def address_line_1(self, address_line_1):
        """Sets the address_line_1 of this Address.

        The first line of the address  # noqa: E501

        :param address_line_1: The address_line_1 of this Address.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                address_line_1 is not None and len(address_line_1) > 50):
            raise ValueError("Invalid value for `address_line_1`, length must be less than or equal to `50`")  # noqa: E501

        self._address_line_1 = address_line_1

    @property
    def address_line_2(self):
        """Gets the address_line_2 of this Address.  # noqa: E501

        The second line of the address  # noqa: E501

        :return: The address_line_2 of this Address.  # noqa: E501
        :rtype: str
        """
        return self._address_line_2

    @address_line_2.setter
    def address_line_2(self, address_line_2):
        """Sets the address_line_2 of this Address.

        The second line of the address  # noqa: E501

        :param address_line_2: The address_line_2 of this Address.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                address_line_2 is not None and len(address_line_2) > 50):
            raise ValueError("Invalid value for `address_line_2`, length must be less than or equal to `50`")  # noqa: E501

        self._address_line_2 = address_line_2

    @property
    def city(self):
        """Gets the city of this Address.  # noqa: E501

        The address town/city  # noqa: E501

        :return: The city of this Address.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Address.

        The address town/city  # noqa: E501

        :param city: The city of this Address.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                city is not None and len(city) > 50):
            raise ValueError("Invalid value for `city`, length must be less than or equal to `50`")  # noqa: E501

        self._city = city

    @property
    def postal_code(self):
        """Gets the postal_code of this Address.  # noqa: E501

        The address postal code/zipcode  # noqa: E501

        :return: The postal_code of this Address.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this Address.

        The address postal code/zipcode  # noqa: E501

        :param postal_code: The postal_code of this Address.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                postal_code is not None and len(postal_code) > 10):
            raise ValueError("Invalid value for `postal_code`, length must be less than or equal to `10`")  # noqa: E501

        self._postal_code = postal_code

    @property
    def country(self):
        """Gets the country of this Address.  # noqa: E501


        :return: The country of this Address.  # noqa: E501
        :rtype: Base
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Address.


        :param country: The country of this Address.  # noqa: E501
        :type: Base
        """

        self._country = country

    @property
    def deleted_at(self):
        """Gets the deleted_at of this Address.  # noqa: E501

        The datetime when the item was deleted  # noqa: E501

        :return: The deleted_at of this Address.  # noqa: E501
        :rtype: datetime
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """Sets the deleted_at of this Address.

        The datetime when the item was deleted  # noqa: E501

        :param deleted_at: The deleted_at of this Address.  # noqa: E501
        :type: datetime
        """

        self._deleted_at = deleted_at

    @property
    def created_at(self):
        """Gets the created_at of this Address.  # noqa: E501

        The datetime when the item was created  # noqa: E501

        :return: The created_at of this Address.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Address.

        The datetime when the item was created  # noqa: E501

        :param created_at: The created_at of this Address.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Address.  # noqa: E501

        The datetime when the item was last updated  # noqa: E501

        :return: The updated_at of this Address.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Address.

        The datetime when the item was last updated  # noqa: E501

        :param updated_at: The updated_at of this Address.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def bank_account(self):
        """Gets the bank_account of this Address.  # noqa: E501


        :return: The bank_account of this Address.  # noqa: E501
        :rtype: Base
        """
        return self._bank_account

    @bank_account.setter
    def bank_account(self, bank_account):
        """Sets the bank_account of this Address.


        :param bank_account: The bank_account of this Address.  # noqa: E501
        :type: Base
        """

        self._bank_account = bank_account

    @property
    def contact(self):
        """Gets the contact of this Address.  # noqa: E501


        :return: The contact of this Address.  # noqa: E501
        :rtype: Base
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this Address.


        :param contact: The contact of this Address.  # noqa: E501
        :type: Base
        """

        self._contact = contact

    @property
    def address_type(self):
        """Gets the address_type of this Address.  # noqa: E501


        :return: The address_type of this Address.  # noqa: E501
        :rtype: Base
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        """Sets the address_type of this Address.


        :param address_type: The address_type of this Address.  # noqa: E501
        :type: Base
        """

        self._address_type = address_type

    @property
    def name(self):
        """Gets the name of this Address.  # noqa: E501

        The custom name of the address  # noqa: E501

        :return: The name of this Address.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Address.

        The custom name of the address  # noqa: E501

        :param name: The name of this Address.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 50):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `50`")  # noqa: E501

        self._name = name

    @property
    def region(self):
        """Gets the region of this Address.  # noqa: E501

        The address state/province/region  # noqa: E501

        :return: The region of this Address.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this Address.

        The address state/province/region  # noqa: E501

        :param region: The region of this Address.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                region is not None and len(region) > 50):
            raise ValueError("Invalid value for `region`, length must be less than or equal to `50`")  # noqa: E501

        self._region = region

    @property
    def country_group(self):
        """Gets the country_group of this Address.  # noqa: E501


        :return: The country_group of this Address.  # noqa: E501
        :rtype: Base
        """
        return self._country_group

    @country_group.setter
    def country_group(self, country_group):
        """Sets the country_group of this Address.


        :param country_group: The country_group of this Address.  # noqa: E501
        :type: Base
        """

        self._country_group = country_group

    @property
    def is_main_address(self):
        """Gets the is_main_address of this Address.  # noqa: E501

        Specifies the address as the contact's main address. Only a single address can exist for a contact in Start so this is always true when returned by the API but cannot be seen in the UI  # noqa: E501

        :return: The is_main_address of this Address.  # noqa: E501
        :rtype: bool
        """
        return self._is_main_address

    @is_main_address.setter
    def is_main_address(self, is_main_address):
        """Sets the is_main_address of this Address.

        Specifies the address as the contact's main address. Only a single address can exist for a contact in Start so this is always true when returned by the API but cannot be seen in the UI  # noqa: E501

        :param is_main_address: The is_main_address of this Address.  # noqa: E501
        :type: bool
        """

        self._is_main_address = is_main_address

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
        if not isinstance(other, Address):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Address):
            return True

        return self.to_dict() != other.to_dict()
