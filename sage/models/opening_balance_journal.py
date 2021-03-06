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


class OpeningBalanceJournal(object):
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
        'transaction': 'Base',
        'transaction_type': 'Base',
        'deleted_at': 'datetime',
        'date': 'date',
        'reference': 'str',
        'journal_lines': 'list[BaseJournalLine]'
    }

    attribute_map = {
        'id': 'id',
        'displayed_as': 'displayed_as',
        'path': '$path',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'transaction': 'transaction',
        'transaction_type': 'transaction_type',
        'deleted_at': 'deleted_at',
        'date': 'date',
        'reference': 'reference',
        'journal_lines': 'journal_lines'
    }

    def __init__(self, id=None, displayed_as=None, path=None, created_at=None, updated_at=None, transaction=None, transaction_type=None, deleted_at=None, date=None, reference=None, journal_lines=None, local_vars_configuration=None):  # noqa: E501
        """OpeningBalanceJournal - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._displayed_as = None
        self._path = None
        self._created_at = None
        self._updated_at = None
        self._transaction = None
        self._transaction_type = None
        self._deleted_at = None
        self._date = None
        self._reference = None
        self._journal_lines = None
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
        if transaction is not None:
            self.transaction = transaction
        if transaction_type is not None:
            self.transaction_type = transaction_type
        if deleted_at is not None:
            self.deleted_at = deleted_at
        if date is not None:
            self.date = date
        if reference is not None:
            self.reference = reference
        if journal_lines is not None:
            self.journal_lines = journal_lines

    @property
    def id(self):
        """Gets the id of this OpeningBalanceJournal.  # noqa: E501

        The unique identifier for the item  # noqa: E501

        :return: The id of this OpeningBalanceJournal.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OpeningBalanceJournal.

        The unique identifier for the item  # noqa: E501

        :param id: The id of this OpeningBalanceJournal.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def displayed_as(self):
        """Gets the displayed_as of this OpeningBalanceJournal.  # noqa: E501

        The name of the resource  # noqa: E501

        :return: The displayed_as of this OpeningBalanceJournal.  # noqa: E501
        :rtype: str
        """
        return self._displayed_as

    @displayed_as.setter
    def displayed_as(self, displayed_as):
        """Sets the displayed_as of this OpeningBalanceJournal.

        The name of the resource  # noqa: E501

        :param displayed_as: The displayed_as of this OpeningBalanceJournal.  # noqa: E501
        :type: str
        """

        self._displayed_as = displayed_as

    @property
    def path(self):
        """Gets the path of this OpeningBalanceJournal.  # noqa: E501

        The API path for the resource  # noqa: E501

        :return: The path of this OpeningBalanceJournal.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this OpeningBalanceJournal.

        The API path for the resource  # noqa: E501

        :param path: The path of this OpeningBalanceJournal.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def created_at(self):
        """Gets the created_at of this OpeningBalanceJournal.  # noqa: E501

        The datetime when the item was created  # noqa: E501

        :return: The created_at of this OpeningBalanceJournal.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this OpeningBalanceJournal.

        The datetime when the item was created  # noqa: E501

        :param created_at: The created_at of this OpeningBalanceJournal.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this OpeningBalanceJournal.  # noqa: E501

        The datetime when the item was last updated  # noqa: E501

        :return: The updated_at of this OpeningBalanceJournal.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this OpeningBalanceJournal.

        The datetime when the item was last updated  # noqa: E501

        :param updated_at: The updated_at of this OpeningBalanceJournal.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def transaction(self):
        """Gets the transaction of this OpeningBalanceJournal.  # noqa: E501


        :return: The transaction of this OpeningBalanceJournal.  # noqa: E501
        :rtype: Base
        """
        return self._transaction

    @transaction.setter
    def transaction(self, transaction):
        """Sets the transaction of this OpeningBalanceJournal.


        :param transaction: The transaction of this OpeningBalanceJournal.  # noqa: E501
        :type: Base
        """

        self._transaction = transaction

    @property
    def transaction_type(self):
        """Gets the transaction_type of this OpeningBalanceJournal.  # noqa: E501


        :return: The transaction_type of this OpeningBalanceJournal.  # noqa: E501
        :rtype: Base
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        """Sets the transaction_type of this OpeningBalanceJournal.


        :param transaction_type: The transaction_type of this OpeningBalanceJournal.  # noqa: E501
        :type: Base
        """

        self._transaction_type = transaction_type

    @property
    def deleted_at(self):
        """Gets the deleted_at of this OpeningBalanceJournal.  # noqa: E501

        The datetime when the item was deleted  # noqa: E501

        :return: The deleted_at of this OpeningBalanceJournal.  # noqa: E501
        :rtype: datetime
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """Sets the deleted_at of this OpeningBalanceJournal.

        The datetime when the item was deleted  # noqa: E501

        :param deleted_at: The deleted_at of this OpeningBalanceJournal.  # noqa: E501
        :type: datetime
        """

        self._deleted_at = deleted_at

    @property
    def date(self):
        """Gets the date of this OpeningBalanceJournal.  # noqa: E501

        The date of the opening balance journal  # noqa: E501

        :return: The date of this OpeningBalanceJournal.  # noqa: E501
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this OpeningBalanceJournal.

        The date of the opening balance journal  # noqa: E501

        :param date: The date of this OpeningBalanceJournal.  # noqa: E501
        :type: date
        """

        self._date = date

    @property
    def reference(self):
        """Gets the reference of this OpeningBalanceJournal.  # noqa: E501

        A reference for the opening balance journal  # noqa: E501

        :return: The reference of this OpeningBalanceJournal.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this OpeningBalanceJournal.

        A reference for the opening balance journal  # noqa: E501

        :param reference: The reference of this OpeningBalanceJournal.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                reference is not None and len(reference) > 25):
            raise ValueError("Invalid value for `reference`, length must be less than or equal to `25`")  # noqa: E501

        self._reference = reference

    @property
    def journal_lines(self):
        """Gets the journal_lines of this OpeningBalanceJournal.  # noqa: E501

        The journal lines  # noqa: E501

        :return: The journal_lines of this OpeningBalanceJournal.  # noqa: E501
        :rtype: list[BaseJournalLine]
        """
        return self._journal_lines

    @journal_lines.setter
    def journal_lines(self, journal_lines):
        """Sets the journal_lines of this OpeningBalanceJournal.

        The journal lines  # noqa: E501

        :param journal_lines: The journal_lines of this OpeningBalanceJournal.  # noqa: E501
        :type: list[BaseJournalLine]
        """

        self._journal_lines = journal_lines

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
        if not isinstance(other, OpeningBalanceJournal):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OpeningBalanceJournal):
            return True

        return self.to_dict() != other.to_dict()
