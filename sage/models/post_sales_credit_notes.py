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


class PostSalesCreditNotes(object):
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
        'sales_credit_note': 'PostSalesCreditNotesSalesCreditNote'
    }

    attribute_map = {
        'sales_credit_note': 'sales_credit_note'
    }

    def __init__(self, sales_credit_note=None, local_vars_configuration=None):  # noqa: E501
        """PostSalesCreditNotes - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._sales_credit_note = None
        self.discriminator = None

        self.sales_credit_note = sales_credit_note

    @property
    def sales_credit_note(self):
        """Gets the sales_credit_note of this PostSalesCreditNotes.  # noqa: E501


        :return: The sales_credit_note of this PostSalesCreditNotes.  # noqa: E501
        :rtype: PostSalesCreditNotesSalesCreditNote
        """
        return self._sales_credit_note

    @sales_credit_note.setter
    def sales_credit_note(self, sales_credit_note):
        """Sets the sales_credit_note of this PostSalesCreditNotes.


        :param sales_credit_note: The sales_credit_note of this PostSalesCreditNotes.  # noqa: E501
        :type: PostSalesCreditNotesSalesCreditNote
        """
        if self.local_vars_configuration.client_side_validation and sales_credit_note is None:  # noqa: E501
            raise ValueError("Invalid value for `sales_credit_note`, must not be `None`")  # noqa: E501

        self._sales_credit_note = sales_credit_note

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
        if not isinstance(other, PostSalesCreditNotes):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PostSalesCreditNotes):
            return True

        return self.to_dict() != other.to_dict()