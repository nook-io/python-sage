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


class ProfitAnalysis(object):
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
        'total': 'ProfitBreakdown',
        'line_breakdown': 'list[ProfitBreakdown]'
    }

    attribute_map = {
        'total': 'total',
        'line_breakdown': 'line_breakdown'
    }

    def __init__(self, total=None, line_breakdown=None, local_vars_configuration=None):  # noqa: E501
        """ProfitAnalysis - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._total = None
        self._line_breakdown = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if line_breakdown is not None:
            self.line_breakdown = line_breakdown

    @property
    def total(self):
        """Gets the total of this ProfitAnalysis.  # noqa: E501


        :return: The total of this ProfitAnalysis.  # noqa: E501
        :rtype: ProfitBreakdown
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ProfitAnalysis.


        :param total: The total of this ProfitAnalysis.  # noqa: E501
        :type: ProfitBreakdown
        """

        self._total = total

    @property
    def line_breakdown(self):
        """Gets the line_breakdown of this ProfitAnalysis.  # noqa: E501

        The breakdown of profit per line  # noqa: E501

        :return: The line_breakdown of this ProfitAnalysis.  # noqa: E501
        :rtype: list[ProfitBreakdown]
        """
        return self._line_breakdown

    @line_breakdown.setter
    def line_breakdown(self, line_breakdown):
        """Sets the line_breakdown of this ProfitAnalysis.

        The breakdown of profit per line  # noqa: E501

        :param line_breakdown: The line_breakdown of this ProfitAnalysis.  # noqa: E501
        :type: list[ProfitBreakdown]
        """

        self._line_breakdown = line_breakdown

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
        if not isinstance(other, ProfitAnalysis):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProfitAnalysis):
            return True

        return self.to_dict() != other.to_dict()
