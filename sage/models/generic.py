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


class Generic(object):
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
        'links': 'list[Link]'
    }

    attribute_map = {
        'id': 'id',
        'displayed_as': 'displayed_as',
        'path': '$path',
        'links': 'links'
    }

    def __init__(self, id=None, displayed_as=None, path=None, links=None, local_vars_configuration=None):  # noqa: E501
        """Generic - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._displayed_as = None
        self._path = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if displayed_as is not None:
            self.displayed_as = displayed_as
        if path is not None:
            self.path = path
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this Generic.  # noqa: E501

        The unique identifier for the item  # noqa: E501

        :return: The id of this Generic.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Generic.

        The unique identifier for the item  # noqa: E501

        :param id: The id of this Generic.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def displayed_as(self):
        """Gets the displayed_as of this Generic.  # noqa: E501

        The name of the resource  # noqa: E501

        :return: The displayed_as of this Generic.  # noqa: E501
        :rtype: str
        """
        return self._displayed_as

    @displayed_as.setter
    def displayed_as(self, displayed_as):
        """Sets the displayed_as of this Generic.

        The name of the resource  # noqa: E501

        :param displayed_as: The displayed_as of this Generic.  # noqa: E501
        :type: str
        """

        self._displayed_as = displayed_as

    @property
    def path(self):
        """Gets the path of this Generic.  # noqa: E501

        The API path for the resource  # noqa: E501

        :return: The path of this Generic.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this Generic.

        The API path for the resource  # noqa: E501

        :param path: The path of this Generic.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def links(self):
        """Gets the links of this Generic.  # noqa: E501

        Links for the resource  # noqa: E501

        :return: The links of this Generic.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Generic.

        Links for the resource  # noqa: E501

        :param links: The links of this Generic.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

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
        if not isinstance(other, Generic):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Generic):
            return True

        return self.to_dict() != other.to_dict()