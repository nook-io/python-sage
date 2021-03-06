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


class LiveExchangeRate(object):
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
        'displayed_as': 'str',
        'path': 'str',
        'rate': 'float',
        'inverse_rate': 'float',
        'base_currency': 'Base',
        'currency': 'Base',
        'retrieved_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'displayed_as': 'displayed_as',
        'path': '$path',
        'rate': 'rate',
        'inverse_rate': 'inverse_rate',
        'base_currency': 'base_currency',
        'currency': 'currency',
        'retrieved_at': 'retrieved_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, displayed_as=None, path=None, rate=None, inverse_rate=None, base_currency=None, currency=None, retrieved_at=None, updated_at=None, local_vars_configuration=None):  # noqa: E501
        """LiveExchangeRate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._displayed_as = None
        self._path = None
        self._rate = None
        self._inverse_rate = None
        self._base_currency = None
        self._currency = None
        self._retrieved_at = None
        self._updated_at = None
        self.discriminator = None

        if displayed_as is not None:
            self.displayed_as = displayed_as
        if path is not None:
            self.path = path
        if rate is not None:
            self.rate = rate
        if inverse_rate is not None:
            self.inverse_rate = inverse_rate
        if base_currency is not None:
            self.base_currency = base_currency
        if currency is not None:
            self.currency = currency
        if retrieved_at is not None:
            self.retrieved_at = retrieved_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def displayed_as(self):
        """Gets the displayed_as of this LiveExchangeRate.  # noqa: E501

        Display text for the item  # noqa: E501

        :return: The displayed_as of this LiveExchangeRate.  # noqa: E501
        :rtype: str
        """
        return self._displayed_as

    @displayed_as.setter
    def displayed_as(self, displayed_as):
        """Sets the displayed_as of this LiveExchangeRate.

        Display text for the item  # noqa: E501

        :param displayed_as: The displayed_as of this LiveExchangeRate.  # noqa: E501
        :type: str
        """

        self._displayed_as = displayed_as

    @property
    def path(self):
        """Gets the path of this LiveExchangeRate.  # noqa: E501

        The API path for the resource  # noqa: E501

        :return: The path of this LiveExchangeRate.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this LiveExchangeRate.

        The API path for the resource  # noqa: E501

        :param path: The path of this LiveExchangeRate.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def rate(self):
        """Gets the rate of this LiveExchangeRate.  # noqa: E501

        The exchange rate  # noqa: E501

        :return: The rate of this LiveExchangeRate.  # noqa: E501
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this LiveExchangeRate.

        The exchange rate  # noqa: E501

        :param rate: The rate of this LiveExchangeRate.  # noqa: E501
        :type: float
        """

        self._rate = rate

    @property
    def inverse_rate(self):
        """Gets the inverse_rate of this LiveExchangeRate.  # noqa: E501

        The inverse exchange rate  # noqa: E501

        :return: The inverse_rate of this LiveExchangeRate.  # noqa: E501
        :rtype: float
        """
        return self._inverse_rate

    @inverse_rate.setter
    def inverse_rate(self, inverse_rate):
        """Sets the inverse_rate of this LiveExchangeRate.

        The inverse exchange rate  # noqa: E501

        :param inverse_rate: The inverse_rate of this LiveExchangeRate.  # noqa: E501
        :type: float
        """

        self._inverse_rate = inverse_rate

    @property
    def base_currency(self):
        """Gets the base_currency of this LiveExchangeRate.  # noqa: E501


        :return: The base_currency of this LiveExchangeRate.  # noqa: E501
        :rtype: Base
        """
        return self._base_currency

    @base_currency.setter
    def base_currency(self, base_currency):
        """Sets the base_currency of this LiveExchangeRate.


        :param base_currency: The base_currency of this LiveExchangeRate.  # noqa: E501
        :type: Base
        """

        self._base_currency = base_currency

    @property
    def currency(self):
        """Gets the currency of this LiveExchangeRate.  # noqa: E501


        :return: The currency of this LiveExchangeRate.  # noqa: E501
        :rtype: Base
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this LiveExchangeRate.


        :param currency: The currency of this LiveExchangeRate.  # noqa: E501
        :type: Base
        """

        self._currency = currency

    @property
    def retrieved_at(self):
        """Gets the retrieved_at of this LiveExchangeRate.  # noqa: E501


        :return: The retrieved_at of this LiveExchangeRate.  # noqa: E501
        :rtype: datetime
        """
        return self._retrieved_at

    @retrieved_at.setter
    def retrieved_at(self, retrieved_at):
        """Sets the retrieved_at of this LiveExchangeRate.


        :param retrieved_at: The retrieved_at of this LiveExchangeRate.  # noqa: E501
        :type: datetime
        """

        self._retrieved_at = retrieved_at

    @property
    def updated_at(self):
        """Gets the updated_at of this LiveExchangeRate.  # noqa: E501


        :return: The updated_at of this LiveExchangeRate.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this LiveExchangeRate.


        :param updated_at: The updated_at of this LiveExchangeRate.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

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
        if not isinstance(other, LiveExchangeRate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LiveExchangeRate):
            return True

        return self.to_dict() != other.to_dict()
