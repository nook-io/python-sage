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


class PrintContactDetails(object):
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
        'business_name': 'bool',
        'website': 'bool',
        'telephone': 'bool',
        'mobile': 'bool',
        'email_address': 'bool',
        'due_date': 'bool',
        'default_delivery_address': 'str'
    }

    attribute_map = {
        'business_name': 'business_name',
        'website': 'website',
        'telephone': 'telephone',
        'mobile': 'mobile',
        'email_address': 'email_address',
        'due_date': 'due_date',
        'default_delivery_address': 'default_delivery_address'
    }

    def __init__(self, business_name=None, website=None, telephone=None, mobile=None, email_address=None, due_date=None, default_delivery_address=None, local_vars_configuration=None):  # noqa: E501
        """PrintContactDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._business_name = None
        self._website = None
        self._telephone = None
        self._mobile = None
        self._email_address = None
        self._due_date = None
        self._default_delivery_address = None
        self.discriminator = None

        if business_name is not None:
            self.business_name = business_name
        if website is not None:
            self.website = website
        if telephone is not None:
            self.telephone = telephone
        if mobile is not None:
            self.mobile = mobile
        if email_address is not None:
            self.email_address = email_address
        if due_date is not None:
            self.due_date = due_date
        if default_delivery_address is not None:
            self.default_delivery_address = default_delivery_address

    @property
    def business_name(self):
        """Gets the business_name of this PrintContactDetails.  # noqa: E501

        Indicates whether business name is printed on the invoice  # noqa: E501

        :return: The business_name of this PrintContactDetails.  # noqa: E501
        :rtype: bool
        """
        return self._business_name

    @business_name.setter
    def business_name(self, business_name):
        """Sets the business_name of this PrintContactDetails.

        Indicates whether business name is printed on the invoice  # noqa: E501

        :param business_name: The business_name of this PrintContactDetails.  # noqa: E501
        :type: bool
        """

        self._business_name = business_name

    @property
    def website(self):
        """Gets the website of this PrintContactDetails.  # noqa: E501

        Indicates whether website is printed on the invoice  # noqa: E501

        :return: The website of this PrintContactDetails.  # noqa: E501
        :rtype: bool
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this PrintContactDetails.

        Indicates whether website is printed on the invoice  # noqa: E501

        :param website: The website of this PrintContactDetails.  # noqa: E501
        :type: bool
        """

        self._website = website

    @property
    def telephone(self):
        """Gets the telephone of this PrintContactDetails.  # noqa: E501

        Indicates whether telephone is printed on the invoice  # noqa: E501

        :return: The telephone of this PrintContactDetails.  # noqa: E501
        :rtype: bool
        """
        return self._telephone

    @telephone.setter
    def telephone(self, telephone):
        """Sets the telephone of this PrintContactDetails.

        Indicates whether telephone is printed on the invoice  # noqa: E501

        :param telephone: The telephone of this PrintContactDetails.  # noqa: E501
        :type: bool
        """

        self._telephone = telephone

    @property
    def mobile(self):
        """Gets the mobile of this PrintContactDetails.  # noqa: E501

        Indicates whether mobile is printed on the invoice  # noqa: E501

        :return: The mobile of this PrintContactDetails.  # noqa: E501
        :rtype: bool
        """
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        """Sets the mobile of this PrintContactDetails.

        Indicates whether mobile is printed on the invoice  # noqa: E501

        :param mobile: The mobile of this PrintContactDetails.  # noqa: E501
        :type: bool
        """

        self._mobile = mobile

    @property
    def email_address(self):
        """Gets the email_address of this PrintContactDetails.  # noqa: E501

        Indicates whether email address is printed on the invoice  # noqa: E501

        :return: The email_address of this PrintContactDetails.  # noqa: E501
        :rtype: bool
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this PrintContactDetails.

        Indicates whether email address is printed on the invoice  # noqa: E501

        :param email_address: The email_address of this PrintContactDetails.  # noqa: E501
        :type: bool
        """

        self._email_address = email_address

    @property
    def due_date(self):
        """Gets the due_date of this PrintContactDetails.  # noqa: E501

        Indicates whether due date is printed on the invoice  # noqa: E501

        :return: The due_date of this PrintContactDetails.  # noqa: E501
        :rtype: bool
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this PrintContactDetails.

        Indicates whether due date is printed on the invoice  # noqa: E501

        :param due_date: The due_date of this PrintContactDetails.  # noqa: E501
        :type: bool
        """

        self._due_date = due_date

    @property
    def default_delivery_address(self):
        """Gets the default_delivery_address of this PrintContactDetails.  # noqa: E501

        Indicates which contact address is used for the delivery address of the invoice. Valid options are: INVOICE_ADDRESS, CONTACT_DELIVERY_ADDRESS, NONE.  # noqa: E501

        :return: The default_delivery_address of this PrintContactDetails.  # noqa: E501
        :rtype: str
        """
        return self._default_delivery_address

    @default_delivery_address.setter
    def default_delivery_address(self, default_delivery_address):
        """Sets the default_delivery_address of this PrintContactDetails.

        Indicates which contact address is used for the delivery address of the invoice. Valid options are: INVOICE_ADDRESS, CONTACT_DELIVERY_ADDRESS, NONE.  # noqa: E501

        :param default_delivery_address: The default_delivery_address of this PrintContactDetails.  # noqa: E501
        :type: str
        """

        self._default_delivery_address = default_delivery_address

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
        if not isinstance(other, PrintContactDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PrintContactDetails):
            return True

        return self.to_dict() != other.to_dict()
