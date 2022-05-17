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


class PutTaxProfilesTaxProfile(object):
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
        'tax_type_id': 'str',
        'tax_number': 'str',
        'tax_number_suffix': 'str',
        'collect_tax': 'bool',
        'tax_return_frequency_id': 'str',
        'address_region': 'PutTaxProfilesTaxProfileAddressRegion'
    }

    attribute_map = {
        'tax_type_id': 'tax_type_id',
        'tax_number': 'tax_number',
        'tax_number_suffix': 'tax_number_suffix',
        'collect_tax': 'collect_tax',
        'tax_return_frequency_id': 'tax_return_frequency_id',
        'address_region': 'address_region'
    }

    def __init__(self, tax_type_id=None, tax_number=None, tax_number_suffix=None, collect_tax=None, tax_return_frequency_id=None, address_region=None, local_vars_configuration=None):  # noqa: E501
        """PutTaxProfilesTaxProfile - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._tax_type_id = None
        self._tax_number = None
        self._tax_number_suffix = None
        self._collect_tax = None
        self._tax_return_frequency_id = None
        self._address_region = None
        self.discriminator = None

        if tax_type_id is not None:
            self.tax_type_id = tax_type_id
        if tax_number is not None:
            self.tax_number = tax_number
        if tax_number_suffix is not None:
            self.tax_number_suffix = tax_number_suffix
        if collect_tax is not None:
            self.collect_tax = collect_tax
        if tax_return_frequency_id is not None:
            self.tax_return_frequency_id = tax_return_frequency_id
        if address_region is not None:
            self.address_region = address_region

    @property
    def tax_type_id(self):
        """Gets the tax_type_id of this PutTaxProfilesTaxProfile.  # noqa: E501

        The ID of the Tax Type.  # noqa: E501

        :return: The tax_type_id of this PutTaxProfilesTaxProfile.  # noqa: E501
        :rtype: str
        """
        return self._tax_type_id

    @tax_type_id.setter
    def tax_type_id(self, tax_type_id):
        """Sets the tax_type_id of this PutTaxProfilesTaxProfile.

        The ID of the Tax Type.  # noqa: E501

        :param tax_type_id: The tax_type_id of this PutTaxProfilesTaxProfile.  # noqa: E501
        :type: str
        """

        self._tax_type_id = tax_type_id

    @property
    def tax_number(self):
        """Gets the tax_number of this PutTaxProfilesTaxProfile.  # noqa: E501

        The tax number  # noqa: E501

        :return: The tax_number of this PutTaxProfilesTaxProfile.  # noqa: E501
        :rtype: str
        """
        return self._tax_number

    @tax_number.setter
    def tax_number(self, tax_number):
        """Sets the tax_number of this PutTaxProfilesTaxProfile.

        The tax number  # noqa: E501

        :param tax_number: The tax_number of this PutTaxProfilesTaxProfile.  # noqa: E501
        :type: str
        """

        self._tax_number = tax_number

    @property
    def tax_number_suffix(self):
        """Gets the tax_number_suffix of this PutTaxProfilesTaxProfile.  # noqa: E501

        The tax number suffix  # noqa: E501

        :return: The tax_number_suffix of this PutTaxProfilesTaxProfile.  # noqa: E501
        :rtype: str
        """
        return self._tax_number_suffix

    @tax_number_suffix.setter
    def tax_number_suffix(self, tax_number_suffix):
        """Sets the tax_number_suffix of this PutTaxProfilesTaxProfile.

        The tax number suffix  # noqa: E501

        :param tax_number_suffix: The tax_number_suffix of this PutTaxProfilesTaxProfile.  # noqa: E501
        :type: str
        """

        self._tax_number_suffix = tax_number_suffix

    @property
    def collect_tax(self):
        """Gets the collect_tax of this PutTaxProfilesTaxProfile.  # noqa: E501

        Indicates whether tax is collected for this tax type  # noqa: E501

        :return: The collect_tax of this PutTaxProfilesTaxProfile.  # noqa: E501
        :rtype: bool
        """
        return self._collect_tax

    @collect_tax.setter
    def collect_tax(self, collect_tax):
        """Sets the collect_tax of this PutTaxProfilesTaxProfile.

        Indicates whether tax is collected for this tax type  # noqa: E501

        :param collect_tax: The collect_tax of this PutTaxProfilesTaxProfile.  # noqa: E501
        :type: bool
        """

        self._collect_tax = collect_tax

    @property
    def tax_return_frequency_id(self):
        """Gets the tax_return_frequency_id of this PutTaxProfilesTaxProfile.  # noqa: E501

        The ID of the Tax Return Frequency.  # noqa: E501

        :return: The tax_return_frequency_id of this PutTaxProfilesTaxProfile.  # noqa: E501
        :rtype: str
        """
        return self._tax_return_frequency_id

    @tax_return_frequency_id.setter
    def tax_return_frequency_id(self, tax_return_frequency_id):
        """Sets the tax_return_frequency_id of this PutTaxProfilesTaxProfile.

        The ID of the Tax Return Frequency.  # noqa: E501

        :param tax_return_frequency_id: The tax_return_frequency_id of this PutTaxProfilesTaxProfile.  # noqa: E501
        :type: str
        """

        self._tax_return_frequency_id = tax_return_frequency_id

    @property
    def address_region(self):
        """Gets the address_region of this PutTaxProfilesTaxProfile.  # noqa: E501


        :return: The address_region of this PutTaxProfilesTaxProfile.  # noqa: E501
        :rtype: PutTaxProfilesTaxProfileAddressRegion
        """
        return self._address_region

    @address_region.setter
    def address_region(self, address_region):
        """Sets the address_region of this PutTaxProfilesTaxProfile.


        :param address_region: The address_region of this PutTaxProfilesTaxProfile.  # noqa: E501
        :type: PutTaxProfilesTaxProfileAddressRegion
        """

        self._address_region = address_region

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
        if not isinstance(other, PutTaxProfilesTaxProfile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PutTaxProfilesTaxProfile):
            return True

        return self.to_dict() != other.to_dict()
