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


class PostBusinessExchangeRatesBusinessExchangeRate(object):
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
        'currency_id': 'str',
        'rate': 'float',
        'inverse_rate': 'float',
        'base_currency_id': 'str'
    }

    attribute_map = {
        'currency_id': 'currency_id',
        'rate': 'rate',
        'inverse_rate': 'inverse_rate',
        'base_currency_id': 'base_currency_id'
    }

    def __init__(self, currency_id=None, rate=None, inverse_rate=None, base_currency_id=None, local_vars_configuration=None):  # noqa: E501
        """PostBusinessExchangeRatesBusinessExchangeRate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._currency_id = None
        self._rate = None
        self._inverse_rate = None
        self._base_currency_id = None
        self.discriminator = None

        self.currency_id = currency_id
        self.rate = rate
        if inverse_rate is not None:
            self.inverse_rate = inverse_rate
        if base_currency_id is not None:
            self.base_currency_id = base_currency_id

    @property
    def currency_id(self):
        """Gets the currency_id of this PostBusinessExchangeRatesBusinessExchangeRate.  # noqa: E501

        The foreign currency  # noqa: E501

        :return: The currency_id of this PostBusinessExchangeRatesBusinessExchangeRate.  # noqa: E501
        :rtype: str
        """
        return self._currency_id

    @currency_id.setter
    def currency_id(self, currency_id):
        """Sets the currency_id of this PostBusinessExchangeRatesBusinessExchangeRate.

        The foreign currency  # noqa: E501

        :param currency_id: The currency_id of this PostBusinessExchangeRatesBusinessExchangeRate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and currency_id is None:  # noqa: E501
            raise ValueError("Invalid value for `currency_id`, must not be `None`")  # noqa: E501

        self._currency_id = currency_id

    @property
    def rate(self):
        """Gets the rate of this PostBusinessExchangeRatesBusinessExchangeRate.  # noqa: E501

        The exchange rate  # noqa: E501

        :return: The rate of this PostBusinessExchangeRatesBusinessExchangeRate.  # noqa: E501
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this PostBusinessExchangeRatesBusinessExchangeRate.

        The exchange rate  # noqa: E501

        :param rate: The rate of this PostBusinessExchangeRatesBusinessExchangeRate.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and rate is None:  # noqa: E501
            raise ValueError("Invalid value for `rate`, must not be `None`")  # noqa: E501

        self._rate = rate

    @property
    def inverse_rate(self):
        """Gets the inverse_rate of this PostBusinessExchangeRatesBusinessExchangeRate.  # noqa: E501

        The inverse exchange rate  # noqa: E501

        :return: The inverse_rate of this PostBusinessExchangeRatesBusinessExchangeRate.  # noqa: E501
        :rtype: float
        """
        return self._inverse_rate

    @inverse_rate.setter
    def inverse_rate(self, inverse_rate):
        """Sets the inverse_rate of this PostBusinessExchangeRatesBusinessExchangeRate.

        The inverse exchange rate  # noqa: E501

        :param inverse_rate: The inverse_rate of this PostBusinessExchangeRatesBusinessExchangeRate.  # noqa: E501
        :type: float
        """

        self._inverse_rate = inverse_rate

    @property
    def base_currency_id(self):
        """Gets the base_currency_id of this PostBusinessExchangeRatesBusinessExchangeRate.  # noqa: E501

        The ID of the Base Currency.  # noqa: E501

        :return: The base_currency_id of this PostBusinessExchangeRatesBusinessExchangeRate.  # noqa: E501
        :rtype: str
        """
        return self._base_currency_id

    @base_currency_id.setter
    def base_currency_id(self, base_currency_id):
        """Sets the base_currency_id of this PostBusinessExchangeRatesBusinessExchangeRate.

        The ID of the Base Currency.  # noqa: E501

        :param base_currency_id: The base_currency_id of this PostBusinessExchangeRatesBusinessExchangeRate.  # noqa: E501
        :type: str
        """

        self._base_currency_id = base_currency_id

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
        if not isinstance(other, PostBusinessExchangeRatesBusinessExchangeRate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PostBusinessExchangeRatesBusinessExchangeRate):
            return True

        return self.to_dict() != other.to_dict()
