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


class PostProductSalesPriceTypesProductSalesPriceType(object):
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
        'name': 'str',
        'active': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'active': 'active'
    }

    def __init__(self, name=None, active=None, local_vars_configuration=None):  # noqa: E501
        """PostProductSalesPriceTypesProductSalesPriceType - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._active = None
        self.discriminator = None

        self.name = name
        self.active = active

    @property
    def name(self):
        """Gets the name of this PostProductSalesPriceTypesProductSalesPriceType.  # noqa: E501

        The name of the product sales price type  # noqa: E501

        :return: The name of this PostProductSalesPriceTypesProductSalesPriceType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PostProductSalesPriceTypesProductSalesPriceType.

        The name of the product sales price type  # noqa: E501

        :param name: The name of this PostProductSalesPriceTypesProductSalesPriceType.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def active(self):
        """Gets the active of this PostProductSalesPriceTypesProductSalesPriceType.  # noqa: E501

        Indicates whether the price type is displayed in the application  # noqa: E501

        :return: The active of this PostProductSalesPriceTypesProductSalesPriceType.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this PostProductSalesPriceTypesProductSalesPriceType.

        Indicates whether the price type is displayed in the application  # noqa: E501

        :param active: The active of this PostProductSalesPriceTypesProductSalesPriceType.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and active is None:  # noqa: E501
            raise ValueError("Invalid value for `active`, must not be `None`")  # noqa: E501

        self._active = active

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
        if not isinstance(other, PostProductSalesPriceTypesProductSalesPriceType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PostProductSalesPriceTypesProductSalesPriceType):
            return True

        return self.to_dict() != other.to_dict()
