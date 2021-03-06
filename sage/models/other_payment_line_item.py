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


class OtherPaymentLineItem(object):
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
        'ledger_account': 'Base',
        'details': 'str',
        'tax_rate': 'Base',
        'net_amount': 'float',
        'tax_amount': 'float',
        'total_amount': 'float',
        'tax_breakdown': 'list[TaxBreakdown]',
        'is_purchase_for_resale': 'bool',
        'trade_of_asset': 'bool',
        'gst_amount': 'float',
        'pst_amount': 'float',
        'tax_recoverable': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'displayed_as': 'displayed_as',
        'ledger_account': 'ledger_account',
        'details': 'details',
        'tax_rate': 'tax_rate',
        'net_amount': 'net_amount',
        'tax_amount': 'tax_amount',
        'total_amount': 'total_amount',
        'tax_breakdown': 'tax_breakdown',
        'is_purchase_for_resale': 'is_purchase_for_resale',
        'trade_of_asset': 'trade_of_asset',
        'gst_amount': 'gst_amount',
        'pst_amount': 'pst_amount',
        'tax_recoverable': 'tax_recoverable'
    }

    def __init__(self, id=None, displayed_as=None, ledger_account=None, details=None, tax_rate=None, net_amount=None, tax_amount=None, total_amount=None, tax_breakdown=None, is_purchase_for_resale=None, trade_of_asset=None, gst_amount=None, pst_amount=None, tax_recoverable=None, local_vars_configuration=None):  # noqa: E501
        """OtherPaymentLineItem - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._displayed_as = None
        self._ledger_account = None
        self._details = None
        self._tax_rate = None
        self._net_amount = None
        self._tax_amount = None
        self._total_amount = None
        self._tax_breakdown = None
        self._is_purchase_for_resale = None
        self._trade_of_asset = None
        self._gst_amount = None
        self._pst_amount = None
        self._tax_recoverable = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if displayed_as is not None:
            self.displayed_as = displayed_as
        if ledger_account is not None:
            self.ledger_account = ledger_account
        if details is not None:
            self.details = details
        if tax_rate is not None:
            self.tax_rate = tax_rate
        if net_amount is not None:
            self.net_amount = net_amount
        if tax_amount is not None:
            self.tax_amount = tax_amount
        if total_amount is not None:
            self.total_amount = total_amount
        if tax_breakdown is not None:
            self.tax_breakdown = tax_breakdown
        if is_purchase_for_resale is not None:
            self.is_purchase_for_resale = is_purchase_for_resale
        if trade_of_asset is not None:
            self.trade_of_asset = trade_of_asset
        if gst_amount is not None:
            self.gst_amount = gst_amount
        if pst_amount is not None:
            self.pst_amount = pst_amount
        if tax_recoverable is not None:
            self.tax_recoverable = tax_recoverable

    @property
    def id(self):
        """Gets the id of this OtherPaymentLineItem.  # noqa: E501

        The unique identifier for the item  # noqa: E501

        :return: The id of this OtherPaymentLineItem.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OtherPaymentLineItem.

        The unique identifier for the item  # noqa: E501

        :param id: The id of this OtherPaymentLineItem.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def displayed_as(self):
        """Gets the displayed_as of this OtherPaymentLineItem.  # noqa: E501

        The name of the resource  # noqa: E501

        :return: The displayed_as of this OtherPaymentLineItem.  # noqa: E501
        :rtype: str
        """
        return self._displayed_as

    @displayed_as.setter
    def displayed_as(self, displayed_as):
        """Sets the displayed_as of this OtherPaymentLineItem.

        The name of the resource  # noqa: E501

        :param displayed_as: The displayed_as of this OtherPaymentLineItem.  # noqa: E501
        :type: str
        """

        self._displayed_as = displayed_as

    @property
    def ledger_account(self):
        """Gets the ledger_account of this OtherPaymentLineItem.  # noqa: E501


        :return: The ledger_account of this OtherPaymentLineItem.  # noqa: E501
        :rtype: Base
        """
        return self._ledger_account

    @ledger_account.setter
    def ledger_account(self, ledger_account):
        """Sets the ledger_account of this OtherPaymentLineItem.


        :param ledger_account: The ledger_account of this OtherPaymentLineItem.  # noqa: E501
        :type: Base
        """

        self._ledger_account = ledger_account

    @property
    def details(self):
        """Gets the details of this OtherPaymentLineItem.  # noqa: E501

        The details of the payment line  # noqa: E501

        :return: The details of this OtherPaymentLineItem.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this OtherPaymentLineItem.

        The details of the payment line  # noqa: E501

        :param details: The details of this OtherPaymentLineItem.  # noqa: E501
        :type: str
        """

        self._details = details

    @property
    def tax_rate(self):
        """Gets the tax_rate of this OtherPaymentLineItem.  # noqa: E501


        :return: The tax_rate of this OtherPaymentLineItem.  # noqa: E501
        :rtype: Base
        """
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, tax_rate):
        """Sets the tax_rate of this OtherPaymentLineItem.


        :param tax_rate: The tax_rate of this OtherPaymentLineItem.  # noqa: E501
        :type: Base
        """

        self._tax_rate = tax_rate

    @property
    def net_amount(self):
        """Gets the net_amount of this OtherPaymentLineItem.  # noqa: E501

        The net amount of the payment line  # noqa: E501

        :return: The net_amount of this OtherPaymentLineItem.  # noqa: E501
        :rtype: float
        """
        return self._net_amount

    @net_amount.setter
    def net_amount(self, net_amount):
        """Sets the net_amount of this OtherPaymentLineItem.

        The net amount of the payment line  # noqa: E501

        :param net_amount: The net_amount of this OtherPaymentLineItem.  # noqa: E501
        :type: float
        """

        self._net_amount = net_amount

    @property
    def tax_amount(self):
        """Gets the tax_amount of this OtherPaymentLineItem.  # noqa: E501

        The tax amount of the payment line  # noqa: E501

        :return: The tax_amount of this OtherPaymentLineItem.  # noqa: E501
        :rtype: float
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """Sets the tax_amount of this OtherPaymentLineItem.

        The tax amount of the payment line  # noqa: E501

        :param tax_amount: The tax_amount of this OtherPaymentLineItem.  # noqa: E501
        :type: float
        """

        self._tax_amount = tax_amount

    @property
    def total_amount(self):
        """Gets the total_amount of this OtherPaymentLineItem.  # noqa: E501

        The total amount of the payment line  # noqa: E501

        :return: The total_amount of this OtherPaymentLineItem.  # noqa: E501
        :rtype: float
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """Sets the total_amount of this OtherPaymentLineItem.

        The total amount of the payment line  # noqa: E501

        :param total_amount: The total_amount of this OtherPaymentLineItem.  # noqa: E501
        :type: float
        """

        self._total_amount = total_amount

    @property
    def tax_breakdown(self):
        """Gets the tax_breakdown of this OtherPaymentLineItem.  # noqa: E501

        The tax breakdown for the payment line  # noqa: E501

        :return: The tax_breakdown of this OtherPaymentLineItem.  # noqa: E501
        :rtype: list[TaxBreakdown]
        """
        return self._tax_breakdown

    @tax_breakdown.setter
    def tax_breakdown(self, tax_breakdown):
        """Sets the tax_breakdown of this OtherPaymentLineItem.

        The tax breakdown for the payment line  # noqa: E501

        :param tax_breakdown: The tax_breakdown of this OtherPaymentLineItem.  # noqa: E501
        :type: list[TaxBreakdown]
        """

        self._tax_breakdown = tax_breakdown

    @property
    def is_purchase_for_resale(self):
        """Gets the is_purchase_for_resale of this OtherPaymentLineItem.  # noqa: E501

        Identifies whether the line item is for resale. (Ireland only)  # noqa: E501

        :return: The is_purchase_for_resale of this OtherPaymentLineItem.  # noqa: E501
        :rtype: bool
        """
        return self._is_purchase_for_resale

    @is_purchase_for_resale.setter
    def is_purchase_for_resale(self, is_purchase_for_resale):
        """Sets the is_purchase_for_resale of this OtherPaymentLineItem.

        Identifies whether the line item is for resale. (Ireland only)  # noqa: E501

        :param is_purchase_for_resale: The is_purchase_for_resale of this OtherPaymentLineItem.  # noqa: E501
        :type: bool
        """

        self._is_purchase_for_resale = is_purchase_for_resale

    @property
    def trade_of_asset(self):
        """Gets the trade_of_asset of this OtherPaymentLineItem.  # noqa: E501

        Whether the line item is marked as trade of asset.  # noqa: E501

        :return: The trade_of_asset of this OtherPaymentLineItem.  # noqa: E501
        :rtype: bool
        """
        return self._trade_of_asset

    @trade_of_asset.setter
    def trade_of_asset(self, trade_of_asset):
        """Sets the trade_of_asset of this OtherPaymentLineItem.

        Whether the line item is marked as trade of asset.  # noqa: E501

        :param trade_of_asset: The trade_of_asset of this OtherPaymentLineItem.  # noqa: E501
        :type: bool
        """

        self._trade_of_asset = trade_of_asset

    @property
    def gst_amount(self):
        """Gets the gst_amount of this OtherPaymentLineItem.  # noqa: E501

        The gst or hst tax amount for the other payment  # noqa: E501

        :return: The gst_amount of this OtherPaymentLineItem.  # noqa: E501
        :rtype: float
        """
        return self._gst_amount

    @gst_amount.setter
    def gst_amount(self, gst_amount):
        """Sets the gst_amount of this OtherPaymentLineItem.

        The gst or hst tax amount for the other payment  # noqa: E501

        :param gst_amount: The gst_amount of this OtherPaymentLineItem.  # noqa: E501
        :type: float
        """

        self._gst_amount = gst_amount

    @property
    def pst_amount(self):
        """Gets the pst_amount of this OtherPaymentLineItem.  # noqa: E501

        The pst or qst tax amount for the other payment  # noqa: E501

        :return: The pst_amount of this OtherPaymentLineItem.  # noqa: E501
        :rtype: float
        """
        return self._pst_amount

    @pst_amount.setter
    def pst_amount(self, pst_amount):
        """Sets the pst_amount of this OtherPaymentLineItem.

        The pst or qst tax amount for the other payment  # noqa: E501

        :param pst_amount: The pst_amount of this OtherPaymentLineItem.  # noqa: E501
        :type: float
        """

        self._pst_amount = pst_amount

    @property
    def tax_recoverable(self):
        """Gets the tax_recoverable of this OtherPaymentLineItem.  # noqa: E501

        Indicates if the other payment is tax recoverable or not  # noqa: E501

        :return: The tax_recoverable of this OtherPaymentLineItem.  # noqa: E501
        :rtype: bool
        """
        return self._tax_recoverable

    @tax_recoverable.setter
    def tax_recoverable(self, tax_recoverable):
        """Sets the tax_recoverable of this OtherPaymentLineItem.

        Indicates if the other payment is tax recoverable or not  # noqa: E501

        :param tax_recoverable: The tax_recoverable of this OtherPaymentLineItem.  # noqa: E501
        :type: bool
        """

        self._tax_recoverable = tax_recoverable

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
        if not isinstance(other, OtherPaymentLineItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OtherPaymentLineItem):
            return True

        return self.to_dict() != other.to_dict()
