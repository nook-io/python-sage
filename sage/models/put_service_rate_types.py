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


class PutServiceRateTypes(object):
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
        'service_rate_type': 'PutServiceRateTypesServiceRateType'
    }

    attribute_map = {
        'service_rate_type': 'service_rate_type'
    }

    def __init__(self, service_rate_type=None, local_vars_configuration=None):  # noqa: E501
        """PutServiceRateTypes - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._service_rate_type = None
        self.discriminator = None

        self.service_rate_type = service_rate_type

    @property
    def service_rate_type(self):
        """Gets the service_rate_type of this PutServiceRateTypes.  # noqa: E501


        :return: The service_rate_type of this PutServiceRateTypes.  # noqa: E501
        :rtype: PutServiceRateTypesServiceRateType
        """
        return self._service_rate_type

    @service_rate_type.setter
    def service_rate_type(self, service_rate_type):
        """Sets the service_rate_type of this PutServiceRateTypes.


        :param service_rate_type: The service_rate_type of this PutServiceRateTypes.  # noqa: E501
        :type: PutServiceRateTypesServiceRateType
        """
        if self.local_vars_configuration.client_side_validation and service_rate_type is None:  # noqa: E501
            raise ValueError("Invalid value for `service_rate_type`, must not be `None`")  # noqa: E501

        self._service_rate_type = service_rate_type

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
        if not isinstance(other, PutServiceRateTypes):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PutServiceRateTypes):
            return True

        return self.to_dict() != other.to_dict()
