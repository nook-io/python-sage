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


class PutInvoiceSettingsInvoiceSettingsLineItemTitles(object):
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
        'description': 'str',
        'unit_price': 'str',
        'quantity': 'str',
        'discount': 'str'
    }

    attribute_map = {
        'description': 'description',
        'unit_price': 'unit_price',
        'quantity': 'quantity',
        'discount': 'discount'
    }

    def __init__(self, description=None, unit_price=None, quantity=None, discount=None, local_vars_configuration=None):  # noqa: E501
        """PutInvoiceSettingsInvoiceSettingsLineItemTitles - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._unit_price = None
        self._quantity = None
        self._discount = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if unit_price is not None:
            self.unit_price = unit_price
        if quantity is not None:
            self.quantity = quantity
        if discount is not None:
            self.discount = discount

    @property
    def description(self):
        """Gets the description of this PutInvoiceSettingsInvoiceSettingsLineItemTitles.  # noqa: E501

        The user defined description column title  # noqa: E501

        :return: The description of this PutInvoiceSettingsInvoiceSettingsLineItemTitles.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PutInvoiceSettingsInvoiceSettingsLineItemTitles.

        The user defined description column title  # noqa: E501

        :param description: The description of this PutInvoiceSettingsInvoiceSettingsLineItemTitles.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def unit_price(self):
        """Gets the unit_price of this PutInvoiceSettingsInvoiceSettingsLineItemTitles.  # noqa: E501

        The user defined unit price column title  # noqa: E501

        :return: The unit_price of this PutInvoiceSettingsInvoiceSettingsLineItemTitles.  # noqa: E501
        :rtype: str
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """Sets the unit_price of this PutInvoiceSettingsInvoiceSettingsLineItemTitles.

        The user defined unit price column title  # noqa: E501

        :param unit_price: The unit_price of this PutInvoiceSettingsInvoiceSettingsLineItemTitles.  # noqa: E501
        :type: str
        """

        self._unit_price = unit_price

    @property
    def quantity(self):
        """Gets the quantity of this PutInvoiceSettingsInvoiceSettingsLineItemTitles.  # noqa: E501

        The user defined quantity column title  # noqa: E501

        :return: The quantity of this PutInvoiceSettingsInvoiceSettingsLineItemTitles.  # noqa: E501
        :rtype: str
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this PutInvoiceSettingsInvoiceSettingsLineItemTitles.

        The user defined quantity column title  # noqa: E501

        :param quantity: The quantity of this PutInvoiceSettingsInvoiceSettingsLineItemTitles.  # noqa: E501
        :type: str
        """

        self._quantity = quantity

    @property
    def discount(self):
        """Gets the discount of this PutInvoiceSettingsInvoiceSettingsLineItemTitles.  # noqa: E501

        The user defined discount column title  # noqa: E501

        :return: The discount of this PutInvoiceSettingsInvoiceSettingsLineItemTitles.  # noqa: E501
        :rtype: str
        """
        return self._discount

    @discount.setter
    def discount(self, discount):
        """Sets the discount of this PutInvoiceSettingsInvoiceSettingsLineItemTitles.

        The user defined discount column title  # noqa: E501

        :param discount: The discount of this PutInvoiceSettingsInvoiceSettingsLineItemTitles.  # noqa: E501
        :type: str
        """

        self._discount = discount

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
        if not isinstance(other, PutInvoiceSettingsInvoiceSettingsLineItemTitles):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PutInvoiceSettingsInvoiceSettingsLineItemTitles):
            return True

        return self.to_dict() != other.to_dict()
