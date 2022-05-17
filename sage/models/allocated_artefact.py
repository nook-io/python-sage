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


class AllocatedArtefact(object):
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
        'artefact': 'Generic',
        'amount': 'float'
    }

    attribute_map = {
        'id': 'id',
        'artefact': 'artefact',
        'amount': 'amount'
    }

    def __init__(self, id=None, artefact=None, amount=None, local_vars_configuration=None):  # noqa: E501
        """AllocatedArtefact - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._artefact = None
        self._amount = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if artefact is not None:
            self.artefact = artefact
        if amount is not None:
            self.amount = amount

    @property
    def id(self):
        """Gets the id of this AllocatedArtefact.  # noqa: E501

        The unique identifier for the item  # noqa: E501

        :return: The id of this AllocatedArtefact.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AllocatedArtefact.

        The unique identifier for the item  # noqa: E501

        :param id: The id of this AllocatedArtefact.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def artefact(self):
        """Gets the artefact of this AllocatedArtefact.  # noqa: E501


        :return: The artefact of this AllocatedArtefact.  # noqa: E501
        :rtype: Generic
        """
        return self._artefact

    @artefact.setter
    def artefact(self, artefact):
        """Sets the artefact of this AllocatedArtefact.


        :param artefact: The artefact of this AllocatedArtefact.  # noqa: E501
        :type: Generic
        """

        self._artefact = artefact

    @property
    def amount(self):
        """Gets the amount of this AllocatedArtefact.  # noqa: E501

        The allocated amount  # noqa: E501

        :return: The amount of this AllocatedArtefact.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this AllocatedArtefact.

        The allocated amount  # noqa: E501

        :param amount: The amount of this AllocatedArtefact.  # noqa: E501
        :type: float
        """

        self._amount = amount

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
        if not isinstance(other, AllocatedArtefact):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AllocatedArtefact):
            return True

        return self.to_dict() != other.to_dict()
