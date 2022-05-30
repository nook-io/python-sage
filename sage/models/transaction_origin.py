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


class TransactionOrigin(object):
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
        'links': 'list[Link]',
        'due_date': 'date',
        'outstanding_amount': 'float',
        'currency': 'Base',
        'status': 'Base',
        'sent': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'displayed_as': 'displayed_as',
        'path': '$path',
        'links': 'links',
        'due_date': 'due_date',
        'outstanding_amount': 'outstanding_amount',
        'currency': 'currency',
        'status': 'status',
        'sent': 'sent'
    }

    def __init__(self, id=None, displayed_as=None, path=None, links=None, due_date=None, outstanding_amount=None, currency=None, status=None, sent=None, local_vars_configuration=None):  # noqa: E501
        """TransactionOrigin - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._displayed_as = None
        self._path = None
        self._links = None
        self._due_date = None
        self._outstanding_amount = None
        self._currency = None
        self._status = None
        self._sent = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if displayed_as is not None:
            self.displayed_as = displayed_as
        if path is not None:
            self.path = path
        if links is not None:
            self.links = links
        if due_date is not None:
            self.due_date = due_date
        if outstanding_amount is not None:
            self.outstanding_amount = outstanding_amount
        if currency is not None:
            self.currency = currency
        if status is not None:
            self.status = status
        if sent is not None:
            self.sent = sent

    @property
    def id(self):
        """Gets the id of this TransactionOrigin.  # noqa: E501

        The unique identifier for the item  # noqa: E501

        :return: The id of this TransactionOrigin.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TransactionOrigin.

        The unique identifier for the item  # noqa: E501

        :param id: The id of this TransactionOrigin.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def displayed_as(self):
        """Gets the displayed_as of this TransactionOrigin.  # noqa: E501

        The name of the resource  # noqa: E501

        :return: The displayed_as of this TransactionOrigin.  # noqa: E501
        :rtype: str
        """
        return self._displayed_as

    @displayed_as.setter
    def displayed_as(self, displayed_as):
        """Sets the displayed_as of this TransactionOrigin.

        The name of the resource  # noqa: E501

        :param displayed_as: The displayed_as of this TransactionOrigin.  # noqa: E501
        :type: str
        """

        self._displayed_as = displayed_as

    @property
    def path(self):
        """Gets the path of this TransactionOrigin.  # noqa: E501

        The API path for the resource  # noqa: E501

        :return: The path of this TransactionOrigin.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this TransactionOrigin.

        The API path for the resource  # noqa: E501

        :param path: The path of this TransactionOrigin.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def links(self):
        """Gets the links of this TransactionOrigin.  # noqa: E501

        Links for the resource  # noqa: E501

        :return: The links of this TransactionOrigin.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this TransactionOrigin.

        Links for the resource  # noqa: E501

        :param links: The links of this TransactionOrigin.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def due_date(self):
        """Gets the due_date of this TransactionOrigin.  # noqa: E501

        The due date of the associated item, e.g. an invoice This attribute is only part of the response when the GET paremeter `expand_origin=true` is set in the request URL. Even then, it is only available on transaction origins found at the following endpoints: [\"/contact_opening_balance\", \"/purchase_corrective_invoice\", \"/sales_corrective_invoice\", \"/purchase_credit_note\", \"/purchase_invoice\", \"/purchase_quick_entry\", \"/sales_credit_note\", \"/sales_estimate\", \"/sales_invoice\", \"/sales_quick_entry\", \"/sales_quote\"]. There are other resources, e.g. bank transfers, bank opening balances, or journals, which--though possibly origins of a transaction--can never have this attribute.  # noqa: E501

        :return: The due_date of this TransactionOrigin.  # noqa: E501
        :rtype: date
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this TransactionOrigin.

        The due date of the associated item, e.g. an invoice This attribute is only part of the response when the GET paremeter `expand_origin=true` is set in the request URL. Even then, it is only available on transaction origins found at the following endpoints: [\"/contact_opening_balance\", \"/purchase_corrective_invoice\", \"/sales_corrective_invoice\", \"/purchase_credit_note\", \"/purchase_invoice\", \"/purchase_quick_entry\", \"/sales_credit_note\", \"/sales_estimate\", \"/sales_invoice\", \"/sales_quick_entry\", \"/sales_quote\"]. There are other resources, e.g. bank transfers, bank opening balances, or journals, which--though possibly origins of a transaction--can never have this attribute.  # noqa: E501

        :param due_date: The due_date of this TransactionOrigin.  # noqa: E501
        :type: date
        """

        self._due_date = due_date

    @property
    def outstanding_amount(self):
        """Gets the outstanding_amount of this TransactionOrigin.  # noqa: E501

        The outstanding amount of the associated item, e.g. an invoice This attribute is only part of the response when the GET paremeter `expand_origin=true` is set in the request URL. Even then, it is only available on transaction origins found at the following endpoints: [\"/contact_opening_balance\", \"/purchase_corrective_invoice\", \"/sales_corrective_invoice\", \"/purchase_credit_note\", \"/purchase_invoice\", \"/purchase_quick_entry\", \"/sales_credit_note\", \"/sales_estimate\", \"/sales_invoice\", \"/sales_quick_entry\", \"/sales_quote\"]. There are other resources, e.g. bank transfers, bank opening balances, or journals, which--though possibly origins of a transaction--can never have this attribute.  # noqa: E501

        :return: The outstanding_amount of this TransactionOrigin.  # noqa: E501
        :rtype: float
        """
        return self._outstanding_amount

    @outstanding_amount.setter
    def outstanding_amount(self, outstanding_amount):
        """Sets the outstanding_amount of this TransactionOrigin.

        The outstanding amount of the associated item, e.g. an invoice This attribute is only part of the response when the GET paremeter `expand_origin=true` is set in the request URL. Even then, it is only available on transaction origins found at the following endpoints: [\"/contact_opening_balance\", \"/purchase_corrective_invoice\", \"/sales_corrective_invoice\", \"/purchase_credit_note\", \"/purchase_invoice\", \"/purchase_quick_entry\", \"/sales_credit_note\", \"/sales_estimate\", \"/sales_invoice\", \"/sales_quick_entry\", \"/sales_quote\"]. There are other resources, e.g. bank transfers, bank opening balances, or journals, which--though possibly origins of a transaction--can never have this attribute.  # noqa: E501

        :param outstanding_amount: The outstanding_amount of this TransactionOrigin.  # noqa: E501
        :type: float
        """

        self._outstanding_amount = outstanding_amount

    @property
    def currency(self):
        """Gets the currency of this TransactionOrigin.  # noqa: E501


        :return: The currency of this TransactionOrigin.  # noqa: E501
        :rtype: Base
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this TransactionOrigin.


        :param currency: The currency of this TransactionOrigin.  # noqa: E501
        :type: Base
        """

        self._currency = currency

    @property
    def status(self):
        """Gets the status of this TransactionOrigin.  # noqa: E501


        :return: The status of this TransactionOrigin.  # noqa: E501
        :rtype: Base
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TransactionOrigin.


        :param status: The status of this TransactionOrigin.  # noqa: E501
        :type: Base
        """

        self._status = status

    @property
    def sent(self):
        """Gets the sent of this TransactionOrigin.  # noqa: E501

        Indicates whether the associated item, e.g. an invoice, has been sent. This attribute is only present for sales items (not purchase) This attribute is only part of the response when the GET paremeter `expand_origin=true` is set in the request URL. Even then, it is only available on transaction origins found at the following endpoints: [\"/contact_opening_balance\", \"/purchase_corrective_invoice\", \"/sales_corrective_invoice\", \"/purchase_credit_note\", \"/purchase_invoice\", \"/purchase_quick_entry\", \"/sales_credit_note\", \"/sales_estimate\", \"/sales_invoice\", \"/sales_quick_entry\", \"/sales_quote\"]. There are other resources, e.g. bank transfers, bank opening balances, or journals, which--though possibly origins of a transaction--can never have this attribute.  # noqa: E501

        :return: The sent of this TransactionOrigin.  # noqa: E501
        :rtype: bool
        """
        return self._sent

    @sent.setter
    def sent(self, sent):
        """Sets the sent of this TransactionOrigin.

        Indicates whether the associated item, e.g. an invoice, has been sent. This attribute is only present for sales items (not purchase) This attribute is only part of the response when the GET paremeter `expand_origin=true` is set in the request URL. Even then, it is only available on transaction origins found at the following endpoints: [\"/contact_opening_balance\", \"/purchase_corrective_invoice\", \"/sales_corrective_invoice\", \"/purchase_credit_note\", \"/purchase_invoice\", \"/purchase_quick_entry\", \"/sales_credit_note\", \"/sales_estimate\", \"/sales_invoice\", \"/sales_quick_entry\", \"/sales_quote\"]. There are other resources, e.g. bank transfers, bank opening balances, or journals, which--though possibly origins of a transaction--can never have this attribute.  # noqa: E501

        :param sent: The sent of this TransactionOrigin.  # noqa: E501
        :type: bool
        """

        self._sent = sent

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
        if not isinstance(other, TransactionOrigin):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransactionOrigin):
            return True

        return self.to_dict() != other.to_dict()