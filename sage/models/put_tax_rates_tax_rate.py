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


class PutTaxRatesTaxRate(object):
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
        'from_date': 'datetime',
        'agency': 'str',
        'percentage': 'float',
        'is_visible': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'from_date': 'from_date',
        'agency': 'agency',
        'percentage': 'percentage',
        'is_visible': 'is_visible'
    }

    def __init__(self, name=None, from_date=None, agency=None, percentage=None, is_visible=None, local_vars_configuration=None):  # noqa: E501
        """PutTaxRatesTaxRate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._from_date = None
        self._agency = None
        self._percentage = None
        self._is_visible = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if from_date is not None:
            self.from_date = from_date
        if agency is not None:
            self.agency = agency
        if percentage is not None:
            self.percentage = percentage
        if is_visible is not None:
            self.is_visible = is_visible

    @property
    def name(self):
        """Gets the name of this PutTaxRatesTaxRate.  # noqa: E501

        The name of the tax rate  # noqa: E501

        :return: The name of this PutTaxRatesTaxRate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PutTaxRatesTaxRate.

        The name of the tax rate  # noqa: E501

        :param name: The name of this PutTaxRatesTaxRate.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def from_date(self):
        """Gets the from_date of this PutTaxRatesTaxRate.  # noqa: E501

        The date from which the tax rate applies  # noqa: E501

        :return: The from_date of this PutTaxRatesTaxRate.  # noqa: E501
        :rtype: datetime
        """
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        """Sets the from_date of this PutTaxRatesTaxRate.

        The date from which the tax rate applies  # noqa: E501

        :param from_date: The from_date of this PutTaxRatesTaxRate.  # noqa: E501
        :type: datetime
        """

        self._from_date = from_date

    @property
    def agency(self):
        """Gets the agency of this PutTaxRatesTaxRate.  # noqa: E501

        The agency name (US Only)  # noqa: E501

        :return: The agency of this PutTaxRatesTaxRate.  # noqa: E501
        :rtype: str
        """
        return self._agency

    @agency.setter
    def agency(self, agency):
        """Sets the agency of this PutTaxRatesTaxRate.

        The agency name (US Only)  # noqa: E501

        :param agency: The agency of this PutTaxRatesTaxRate.  # noqa: E501
        :type: str
        """

        self._agency = agency

    @property
    def percentage(self):
        """Gets the percentage of this PutTaxRatesTaxRate.  # noqa: E501

        The tax rate percentage  # noqa: E501

        :return: The percentage of this PutTaxRatesTaxRate.  # noqa: E501
        :rtype: float
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this PutTaxRatesTaxRate.

        The tax rate percentage  # noqa: E501

        :param percentage: The percentage of this PutTaxRatesTaxRate.  # noqa: E501
        :type: float
        """

        self._percentage = percentage

    @property
    def is_visible(self):
        """Gets the is_visible of this PutTaxRatesTaxRate.  # noqa: E501

        Indicates whether the tax rate is visible in the application  # noqa: E501

        :return: The is_visible of this PutTaxRatesTaxRate.  # noqa: E501
        :rtype: bool
        """
        return self._is_visible

    @is_visible.setter
    def is_visible(self, is_visible):
        """Sets the is_visible of this PutTaxRatesTaxRate.

        Indicates whether the tax rate is visible in the application  # noqa: E501

        :param is_visible: The is_visible of this PutTaxRatesTaxRate.  # noqa: E501
        :type: bool
        """

        self._is_visible = is_visible

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
        if not isinstance(other, PutTaxRatesTaxRate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PutTaxRatesTaxRate):
            return True

        return self.to_dict() != other.to_dict()
