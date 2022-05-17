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


class Transaction(object):
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
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'date': 'date',
        'deleted': 'bool',
        'reference': 'str',
        'total': 'float',
        'total_in_transaction_currency': 'float',
        'contact': 'Base',
        'transaction_type': 'Base',
        'origin': 'TransactionOrigin',
        'audit_trail_id': 'str',
        'number_of_attachments': 'str'
    }

    attribute_map = {
        'id': 'id',
        'displayed_as': 'displayed_as',
        'path': '$path',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'date': 'date',
        'deleted': 'deleted',
        'reference': 'reference',
        'total': 'total',
        'total_in_transaction_currency': 'total_in_transaction_currency',
        'contact': 'contact',
        'transaction_type': 'transaction_type',
        'origin': 'origin',
        'audit_trail_id': 'audit_trail_id',
        'number_of_attachments': 'number_of_attachments'
    }

    def __init__(self, id=None, displayed_as=None, path=None, created_at=None, updated_at=None, date=None, deleted=None, reference=None, total=None, total_in_transaction_currency=None, contact=None, transaction_type=None, origin=None, audit_trail_id=None, number_of_attachments=None, local_vars_configuration=None):  # noqa: E501
        """Transaction - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._displayed_as = None
        self._path = None
        self._created_at = None
        self._updated_at = None
        self._date = None
        self._deleted = None
        self._reference = None
        self._total = None
        self._total_in_transaction_currency = None
        self._contact = None
        self._transaction_type = None
        self._origin = None
        self._audit_trail_id = None
        self._number_of_attachments = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if displayed_as is not None:
            self.displayed_as = displayed_as
        if path is not None:
            self.path = path
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if date is not None:
            self.date = date
        if deleted is not None:
            self.deleted = deleted
        if reference is not None:
            self.reference = reference
        if total is not None:
            self.total = total
        if total_in_transaction_currency is not None:
            self.total_in_transaction_currency = total_in_transaction_currency
        if contact is not None:
            self.contact = contact
        if transaction_type is not None:
            self.transaction_type = transaction_type
        if origin is not None:
            self.origin = origin
        if audit_trail_id is not None:
            self.audit_trail_id = audit_trail_id
        if number_of_attachments is not None:
            self.number_of_attachments = number_of_attachments

    @property
    def id(self):
        """Gets the id of this Transaction.  # noqa: E501

        The unique identifier for the item  # noqa: E501

        :return: The id of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Transaction.

        The unique identifier for the item  # noqa: E501

        :param id: The id of this Transaction.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def displayed_as(self):
        """Gets the displayed_as of this Transaction.  # noqa: E501

        The name of the resource  # noqa: E501

        :return: The displayed_as of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._displayed_as

    @displayed_as.setter
    def displayed_as(self, displayed_as):
        """Sets the displayed_as of this Transaction.

        The name of the resource  # noqa: E501

        :param displayed_as: The displayed_as of this Transaction.  # noqa: E501
        :type: str
        """

        self._displayed_as = displayed_as

    @property
    def path(self):
        """Gets the path of this Transaction.  # noqa: E501

        The API path for the resource  # noqa: E501

        :return: The path of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this Transaction.

        The API path for the resource  # noqa: E501

        :param path: The path of this Transaction.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def created_at(self):
        """Gets the created_at of this Transaction.  # noqa: E501

        The datetime when the item was created  # noqa: E501

        :return: The created_at of this Transaction.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Transaction.

        The datetime when the item was created  # noqa: E501

        :param created_at: The created_at of this Transaction.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Transaction.  # noqa: E501

        The datetime when the item was last updated  # noqa: E501

        :return: The updated_at of this Transaction.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Transaction.

        The datetime when the item was last updated  # noqa: E501

        :param updated_at: The updated_at of this Transaction.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def date(self):
        """Gets the date of this Transaction.  # noqa: E501

        The date of the transaction  # noqa: E501

        :return: The date of this Transaction.  # noqa: E501
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this Transaction.

        The date of the transaction  # noqa: E501

        :param date: The date of this Transaction.  # noqa: E501
        :type: date
        """

        self._date = date

    @property
    def deleted(self):
        """Gets the deleted of this Transaction.  # noqa: E501

        Indicates whether the transaction has been deleted  # noqa: E501

        :return: The deleted of this Transaction.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this Transaction.

        Indicates whether the transaction has been deleted  # noqa: E501

        :param deleted: The deleted of this Transaction.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def reference(self):
        """Gets the reference of this Transaction.  # noqa: E501

        The transaction reference  # noqa: E501

        :return: The reference of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this Transaction.

        The transaction reference  # noqa: E501

        :param reference: The reference of this Transaction.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                reference is not None and len(reference) > 255):
            raise ValueError("Invalid value for `reference`, length must be less than or equal to `255`")  # noqa: E501

        self._reference = reference

    @property
    def total(self):
        """Gets the total of this Transaction.  # noqa: E501

        The transaction total in the base currency  # noqa: E501

        :return: The total of this Transaction.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this Transaction.

        The transaction total in the base currency  # noqa: E501

        :param total: The total of this Transaction.  # noqa: E501
        :type: float
        """

        self._total = total

    @property
    def total_in_transaction_currency(self):
        """Gets the total_in_transaction_currency of this Transaction.  # noqa: E501

        The transaction total in the transaction's origin's currency. This is null for some origin types.  # noqa: E501

        :return: The total_in_transaction_currency of this Transaction.  # noqa: E501
        :rtype: float
        """
        return self._total_in_transaction_currency

    @total_in_transaction_currency.setter
    def total_in_transaction_currency(self, total_in_transaction_currency):
        """Sets the total_in_transaction_currency of this Transaction.

        The transaction total in the transaction's origin's currency. This is null for some origin types.  # noqa: E501

        :param total_in_transaction_currency: The total_in_transaction_currency of this Transaction.  # noqa: E501
        :type: float
        """

        self._total_in_transaction_currency = total_in_transaction_currency

    @property
    def contact(self):
        """Gets the contact of this Transaction.  # noqa: E501


        :return: The contact of this Transaction.  # noqa: E501
        :rtype: Base
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this Transaction.


        :param contact: The contact of this Transaction.  # noqa: E501
        :type: Base
        """

        self._contact = contact

    @property
    def transaction_type(self):
        """Gets the transaction_type of this Transaction.  # noqa: E501


        :return: The transaction_type of this Transaction.  # noqa: E501
        :rtype: Base
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        """Sets the transaction_type of this Transaction.


        :param transaction_type: The transaction_type of this Transaction.  # noqa: E501
        :type: Base
        """

        self._transaction_type = transaction_type

    @property
    def origin(self):
        """Gets the origin of this Transaction.  # noqa: E501


        :return: The origin of this Transaction.  # noqa: E501
        :rtype: TransactionOrigin
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this Transaction.


        :param origin: The origin of this Transaction.  # noqa: E501
        :type: TransactionOrigin
        """

        self._origin = origin

    @property
    def audit_trail_id(self):
        """Gets the audit_trail_id of this Transaction.  # noqa: E501

        The original entity that generated the transaction  # noqa: E501

        :return: The audit_trail_id of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._audit_trail_id

    @audit_trail_id.setter
    def audit_trail_id(self, audit_trail_id):
        """Sets the audit_trail_id of this Transaction.

        The original entity that generated the transaction  # noqa: E501

        :param audit_trail_id: The audit_trail_id of this Transaction.  # noqa: E501
        :type: str
        """

        self._audit_trail_id = audit_trail_id

    @property
    def number_of_attachments(self):
        """Gets the number_of_attachments of this Transaction.  # noqa: E501

        The number of attachments related to the transaction  # noqa: E501

        :return: The number_of_attachments of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._number_of_attachments

    @number_of_attachments.setter
    def number_of_attachments(self, number_of_attachments):
        """Sets the number_of_attachments of this Transaction.

        The number of attachments related to the transaction  # noqa: E501

        :param number_of_attachments: The number_of_attachments of this Transaction.  # noqa: E501
        :type: str
        """

        self._number_of_attachments = number_of_attachments

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
        if not isinstance(other, Transaction):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Transaction):
            return True

        return self.to_dict() != other.to_dict()
