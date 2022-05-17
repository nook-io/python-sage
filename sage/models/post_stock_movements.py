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


class PostStockMovements(object):
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
        'stock_movement': 'PostStockMovementsStockMovement'
    }

    attribute_map = {
        'stock_movement': 'stock_movement'
    }

    def __init__(self, stock_movement=None, local_vars_configuration=None):  # noqa: E501
        """PostStockMovements - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._stock_movement = None
        self.discriminator = None

        self.stock_movement = stock_movement

    @property
    def stock_movement(self):
        """Gets the stock_movement of this PostStockMovements.  # noqa: E501


        :return: The stock_movement of this PostStockMovements.  # noqa: E501
        :rtype: PostStockMovementsStockMovement
        """
        return self._stock_movement

    @stock_movement.setter
    def stock_movement(self, stock_movement):
        """Sets the stock_movement of this PostStockMovements.


        :param stock_movement: The stock_movement of this PostStockMovements.  # noqa: E501
        :type: PostStockMovementsStockMovement
        """
        if self.local_vars_configuration.client_side_validation and stock_movement is None:  # noqa: E501
            raise ValueError("Invalid value for `stock_movement`, must not be `None`")  # noqa: E501

        self._stock_movement = stock_movement

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
        if not isinstance(other, PostStockMovements):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PostStockMovements):
            return True

        return self.to_dict() != other.to_dict()
