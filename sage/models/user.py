# coding: utf-8

"""
    Sage Accounting API - User Accounts

    Documentation of the Sage Business Cloud Accounting API.  # noqa: E501

    The version of the OpenAPI document: 3.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from sage.configuration import Configuration


class User(object):
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
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'displayed_as': 'str',
        'id': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'initials': 'str',
        'email': 'str',
        'locale': 'str'
    }

    attribute_map = {
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'displayed_as': 'displayed_as',
        'id': 'id',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'initials': 'initials',
        'email': 'email',
        'locale': 'locale'
    }

    def __init__(self, created_at=None, updated_at=None, displayed_as=None, id=None, first_name=None, last_name=None, initials=None, email=None, locale=None, local_vars_configuration=None):  # noqa: E501
        """User - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._created_at = None
        self._updated_at = None
        self._displayed_as = None
        self._id = None
        self._first_name = None
        self._last_name = None
        self._initials = None
        self._email = None
        self._locale = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if displayed_as is not None:
            self.displayed_as = displayed_as
        if id is not None:
            self.id = id
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if initials is not None:
            self.initials = initials
        if email is not None:
            self.email = email
        if locale is not None:
            self.locale = locale

    @property
    def created_at(self):
        """Gets the created_at of this User.  # noqa: E501

        The datetime when the item was created  # noqa: E501

        :return: The created_at of this User.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this User.

        The datetime when the item was created  # noqa: E501

        :param created_at: The created_at of this User.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this User.  # noqa: E501

        The datetime when the item was last updated  # noqa: E501

        :return: The updated_at of this User.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this User.

        The datetime when the item was last updated  # noqa: E501

        :param updated_at: The updated_at of this User.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def displayed_as(self):
        """Gets the displayed_as of this User.  # noqa: E501

        Display text for the item  # noqa: E501

        :return: The displayed_as of this User.  # noqa: E501
        :rtype: str
        """
        return self._displayed_as

    @displayed_as.setter
    def displayed_as(self, displayed_as):
        """Sets the displayed_as of this User.

        Display text for the item  # noqa: E501

        :param displayed_as: The displayed_as of this User.  # noqa: E501
        :type: str
        """

        self._displayed_as = displayed_as

    @property
    def id(self):
        """Gets the id of this User.  # noqa: E501

        The unique identifier for the user  # noqa: E501

        :return: The id of this User.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this User.

        The unique identifier for the user  # noqa: E501

        :param id: The id of this User.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def first_name(self):
        """Gets the first_name of this User.  # noqa: E501

        The first name of the user  # noqa: E501

        :return: The first_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this User.

        The first name of the user  # noqa: E501

        :param first_name: The first_name of this User.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this User.  # noqa: E501

        The last name of the user  # noqa: E501

        :return: The last_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this User.

        The last name of the user  # noqa: E501

        :param last_name: The last_name of this User.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def initials(self):
        """Gets the initials of this User.  # noqa: E501

        The initials of the user  # noqa: E501

        :return: The initials of this User.  # noqa: E501
        :rtype: str
        """
        return self._initials

    @initials.setter
    def initials(self, initials):
        """Sets the initials of this User.

        The initials of the user  # noqa: E501

        :param initials: The initials of this User.  # noqa: E501
        :type: str
        """

        self._initials = initials

    @property
    def email(self):
        """Gets the email of this User.  # noqa: E501

        The email address of the user  # noqa: E501

        :return: The email of this User.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this User.

        The email address of the user  # noqa: E501

        :param email: The email of this User.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def locale(self):
        """Gets the locale of this User.  # noqa: E501

        The locale of the user  # noqa: E501

        :return: The locale of this User.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this User.

        The locale of the user  # noqa: E501

        :param locale: The locale of this User.  # noqa: E501
        :type: str
        """

        self._locale = locale

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
        if not isinstance(other, User):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, User):
            return True

        return self.to_dict() != other.to_dict()
