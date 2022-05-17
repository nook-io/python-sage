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


class PutOtherPaymentsOtherPayment(object):
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
        'transaction_type_id': 'str',
        'date': 'date',
        'total_amount': 'float',
        'base_currency_total_itc_amount': 'float',
        'total_itc_amount': 'float',
        'base_currency_total_itr_amount': 'float',
        'total_itr_amount': 'float',
        'part_recoverable': 'bool',
        'payment_method_id': 'str',
        'contact_id': 'str',
        'bank_account_id': 'str',
        'tax_address_region_id': 'str',
        'net_amount': 'float',
        'tax_amount': 'float',
        'reference': 'str',
        'withholding_tax_rate': 'float',
        'withholding_tax_amount': 'float',
        'payment_lines': 'list[PutOtherPaymentsOtherPaymentPaymentLines]'
    }

    attribute_map = {
        'transaction_type_id': 'transaction_type_id',
        'date': 'date',
        'total_amount': 'total_amount',
        'base_currency_total_itc_amount': 'base_currency_total_itc_amount',
        'total_itc_amount': 'total_itc_amount',
        'base_currency_total_itr_amount': 'base_currency_total_itr_amount',
        'total_itr_amount': 'total_itr_amount',
        'part_recoverable': 'part_recoverable',
        'payment_method_id': 'payment_method_id',
        'contact_id': 'contact_id',
        'bank_account_id': 'bank_account_id',
        'tax_address_region_id': 'tax_address_region_id',
        'net_amount': 'net_amount',
        'tax_amount': 'tax_amount',
        'reference': 'reference',
        'withholding_tax_rate': 'withholding_tax_rate',
        'withholding_tax_amount': 'withholding_tax_amount',
        'payment_lines': 'payment_lines'
    }

    def __init__(self, transaction_type_id=None, date=None, total_amount=None, base_currency_total_itc_amount=None, total_itc_amount=None, base_currency_total_itr_amount=None, total_itr_amount=None, part_recoverable=None, payment_method_id=None, contact_id=None, bank_account_id=None, tax_address_region_id=None, net_amount=None, tax_amount=None, reference=None, withholding_tax_rate=None, withholding_tax_amount=None, payment_lines=None, local_vars_configuration=None):  # noqa: E501
        """PutOtherPaymentsOtherPayment - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._transaction_type_id = None
        self._date = None
        self._total_amount = None
        self._base_currency_total_itc_amount = None
        self._total_itc_amount = None
        self._base_currency_total_itr_amount = None
        self._total_itr_amount = None
        self._part_recoverable = None
        self._payment_method_id = None
        self._contact_id = None
        self._bank_account_id = None
        self._tax_address_region_id = None
        self._net_amount = None
        self._tax_amount = None
        self._reference = None
        self._withholding_tax_rate = None
        self._withholding_tax_amount = None
        self._payment_lines = None
        self.discriminator = None

        if transaction_type_id is not None:
            self.transaction_type_id = transaction_type_id
        if date is not None:
            self.date = date
        if total_amount is not None:
            self.total_amount = total_amount
        if base_currency_total_itc_amount is not None:
            self.base_currency_total_itc_amount = base_currency_total_itc_amount
        if total_itc_amount is not None:
            self.total_itc_amount = total_itc_amount
        if base_currency_total_itr_amount is not None:
            self.base_currency_total_itr_amount = base_currency_total_itr_amount
        if total_itr_amount is not None:
            self.total_itr_amount = total_itr_amount
        if part_recoverable is not None:
            self.part_recoverable = part_recoverable
        if payment_method_id is not None:
            self.payment_method_id = payment_method_id
        if contact_id is not None:
            self.contact_id = contact_id
        if bank_account_id is not None:
            self.bank_account_id = bank_account_id
        if tax_address_region_id is not None:
            self.tax_address_region_id = tax_address_region_id
        if net_amount is not None:
            self.net_amount = net_amount
        if tax_amount is not None:
            self.tax_amount = tax_amount
        if reference is not None:
            self.reference = reference
        if withholding_tax_rate is not None:
            self.withholding_tax_rate = withholding_tax_rate
        if withholding_tax_amount is not None:
            self.withholding_tax_amount = withholding_tax_amount
        if payment_lines is not None:
            self.payment_lines = payment_lines

    @property
    def transaction_type_id(self):
        """Gets the transaction_type_id of this PutOtherPaymentsOtherPayment.  # noqa: E501

        The transaction type of the payment  # noqa: E501

        :return: The transaction_type_id of this PutOtherPaymentsOtherPayment.  # noqa: E501
        :rtype: str
        """
        return self._transaction_type_id

    @transaction_type_id.setter
    def transaction_type_id(self, transaction_type_id):
        """Sets the transaction_type_id of this PutOtherPaymentsOtherPayment.

        The transaction type of the payment  # noqa: E501

        :param transaction_type_id: The transaction_type_id of this PutOtherPaymentsOtherPayment.  # noqa: E501
        :type: str
        """

        self._transaction_type_id = transaction_type_id

    @property
    def date(self):
        """Gets the date of this PutOtherPaymentsOtherPayment.  # noqa: E501

        The date of the payment  # noqa: E501

        :return: The date of this PutOtherPaymentsOtherPayment.  # noqa: E501
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this PutOtherPaymentsOtherPayment.

        The date of the payment  # noqa: E501

        :param date: The date of this PutOtherPaymentsOtherPayment.  # noqa: E501
        :type: date
        """

        self._date = date

    @property
    def total_amount(self):
        """Gets the total_amount of this PutOtherPaymentsOtherPayment.  # noqa: E501

        The total amount of the payment  # noqa: E501

        :return: The total_amount of this PutOtherPaymentsOtherPayment.  # noqa: E501
        :rtype: float
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """Sets the total_amount of this PutOtherPaymentsOtherPayment.

        The total amount of the payment  # noqa: E501

        :param total_amount: The total_amount of this PutOtherPaymentsOtherPayment.  # noqa: E501
        :type: float
        """

        self._total_amount = total_amount

    @property
    def base_currency_total_itc_amount(self):
        """Gets the base_currency_total_itc_amount of this PutOtherPaymentsOtherPayment.  # noqa: E501

        The total amount of input tax credit in base currency for the                      Other Payment (Canada only)  # noqa: E501

        :return: The base_currency_total_itc_amount of this PutOtherPaymentsOtherPayment.  # noqa: E501
        :rtype: float
        """
        return self._base_currency_total_itc_amount

    @base_currency_total_itc_amount.setter
    def base_currency_total_itc_amount(self, base_currency_total_itc_amount):
        """Sets the base_currency_total_itc_amount of this PutOtherPaymentsOtherPayment.

        The total amount of input tax credit in base currency for the                      Other Payment (Canada only)  # noqa: E501

        :param base_currency_total_itc_amount: The base_currency_total_itc_amount of this PutOtherPaymentsOtherPayment.  # noqa: E501
        :type: float
        """

        self._base_currency_total_itc_amount = base_currency_total_itc_amount

    @property
    def total_itc_amount(self):
        """Gets the total_itc_amount of this PutOtherPaymentsOtherPayment.  # noqa: E501

        The total amount of input tax credit for the Other Payment (Canada only)  # noqa: E501

        :return: The total_itc_amount of this PutOtherPaymentsOtherPayment.  # noqa: E501
        :rtype: float
        """
        return self._total_itc_amount

    @total_itc_amount.setter
    def total_itc_amount(self, total_itc_amount):
        """Sets the total_itc_amount of this PutOtherPaymentsOtherPayment.

        The total amount of input tax credit for the Other Payment (Canada only)  # noqa: E501

        :param total_itc_amount: The total_itc_amount of this PutOtherPaymentsOtherPayment.  # noqa: E501
        :type: float
        """

        self._total_itc_amount = total_itc_amount

    @property
    def base_currency_total_itr_amount(self):
        """Gets the base_currency_total_itr_amount of this PutOtherPaymentsOtherPayment.  # noqa: E501

        The total amount of input tax refund in base currency for the                      Other Payment (Canada only)  # noqa: E501

        :return: The base_currency_total_itr_amount of this PutOtherPaymentsOtherPayment.  # noqa: E501
        :rtype: float
        """
        return self._base_currency_total_itr_amount

    @base_currency_total_itr_amount.setter
    def base_currency_total_itr_amount(self, base_currency_total_itr_amount):
        """Sets the base_currency_total_itr_amount of this PutOtherPaymentsOtherPayment.

        The total amount of input tax refund in base currency for the                      Other Payment (Canada only)  # noqa: E501

        :param base_currency_total_itr_amount: The base_currency_total_itr_amount of this PutOtherPaymentsOtherPayment.  # noqa: E501
        :type: float
        """

        self._base_currency_total_itr_amount = base_currency_total_itr_amount

    @property
    def total_itr_amount(self):
        """Gets the total_itr_amount of this PutOtherPaymentsOtherPayment.  # noqa: E501

        The total amount of input tax refund for the Other Payment (Canada only)  # noqa: E501

        :return: The total_itr_amount of this PutOtherPaymentsOtherPayment.  # noqa: E501
        :rtype: float
        """
        return self._total_itr_amount

    @total_itr_amount.setter
    def total_itr_amount(self, total_itr_amount):
        """Sets the total_itr_amount of this PutOtherPaymentsOtherPayment.

        The total amount of input tax refund for the Other Payment (Canada only)  # noqa: E501

        :param total_itr_amount: The total_itr_amount of this PutOtherPaymentsOtherPayment.  # noqa: E501
        :type: float
        """

        self._total_itr_amount = total_itr_amount

    @property
    def part_recoverable(self):
        """Gets the part_recoverable of this PutOtherPaymentsOtherPayment.  # noqa: E501

        Indicates if the Other Payment is part recoverable or not (Canada only)  # noqa: E501

        :return: The part_recoverable of this PutOtherPaymentsOtherPayment.  # noqa: E501
        :rtype: bool
        """
        return self._part_recoverable

    @part_recoverable.setter
    def part_recoverable(self, part_recoverable):
        """Sets the part_recoverable of this PutOtherPaymentsOtherPayment.

        Indicates if the Other Payment is part recoverable or not (Canada only)  # noqa: E501

        :param part_recoverable: The part_recoverable of this PutOtherPaymentsOtherPayment.  # noqa: E501
        :type: bool
        """

        self._part_recoverable = part_recoverable

    @property
    def payment_method_id(self):
        """Gets the payment_method_id of this PutOtherPaymentsOtherPayment.  # noqa: E501

        The ID of the Payment Method.  # noqa: E501

        :return: The payment_method_id of this PutOtherPaymentsOtherPayment.  # noqa: E501
        :rtype: str
        """
        return self._payment_method_id

    @payment_method_id.setter
    def payment_method_id(self, payment_method_id):
        """Sets the payment_method_id of this PutOtherPaymentsOtherPayment.

        The ID of the Payment Method.  # noqa: E501

        :param payment_method_id: The payment_method_id of this PutOtherPaymentsOtherPayment.  # noqa: E501
        :type: str
        """

        self._payment_method_id = payment_method_id

    @property
    def contact_id(self):
        """Gets the contact_id of this PutOtherPaymentsOtherPayment.  # noqa: E501

        The ID of the Contact.  # noqa: E501

        :return: The contact_id of this PutOtherPaymentsOtherPayment.  # noqa: E501
        :rtype: str
        """
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        """Sets the contact_id of this PutOtherPaymentsOtherPayment.

        The ID of the Contact.  # noqa: E501

        :param contact_id: The contact_id of this PutOtherPaymentsOtherPayment.  # noqa: E501
        :type: str
        """

        self._contact_id = contact_id

    @property
    def bank_account_id(self):
        """Gets the bank_account_id of this PutOtherPaymentsOtherPayment.  # noqa: E501

        The ID of the Bank Account.  # noqa: E501

        :return: The bank_account_id of this PutOtherPaymentsOtherPayment.  # noqa: E501
        :rtype: str
        """
        return self._bank_account_id

    @bank_account_id.setter
    def bank_account_id(self, bank_account_id):
        """Sets the bank_account_id of this PutOtherPaymentsOtherPayment.

        The ID of the Bank Account.  # noqa: E501

        :param bank_account_id: The bank_account_id of this PutOtherPaymentsOtherPayment.  # noqa: E501
        :type: str
        """

        self._bank_account_id = bank_account_id

    @property
    def tax_address_region_id(self):
        """Gets the tax_address_region_id of this PutOtherPaymentsOtherPayment.  # noqa: E501

        The ID of the Tax Address Region. (Canada only)  # noqa: E501

        :return: The tax_address_region_id of this PutOtherPaymentsOtherPayment.  # noqa: E501
        :rtype: str
        """
        return self._tax_address_region_id

    @tax_address_region_id.setter
    def tax_address_region_id(self, tax_address_region_id):
        """Sets the tax_address_region_id of this PutOtherPaymentsOtherPayment.

        The ID of the Tax Address Region. (Canada only)  # noqa: E501

        :param tax_address_region_id: The tax_address_region_id of this PutOtherPaymentsOtherPayment.  # noqa: E501
        :type: str
        """

        self._tax_address_region_id = tax_address_region_id

    @property
    def net_amount(self):
        """Gets the net_amount of this PutOtherPaymentsOtherPayment.  # noqa: E501

        The net amount of the payment  # noqa: E501

        :return: The net_amount of this PutOtherPaymentsOtherPayment.  # noqa: E501
        :rtype: float
        """
        return self._net_amount

    @net_amount.setter
    def net_amount(self, net_amount):
        """Sets the net_amount of this PutOtherPaymentsOtherPayment.

        The net amount of the payment  # noqa: E501

        :param net_amount: The net_amount of this PutOtherPaymentsOtherPayment.  # noqa: E501
        :type: float
        """

        self._net_amount = net_amount

    @property
    def tax_amount(self):
        """Gets the tax_amount of this PutOtherPaymentsOtherPayment.  # noqa: E501

        The tax amount of the payment  # noqa: E501

        :return: The tax_amount of this PutOtherPaymentsOtherPayment.  # noqa: E501
        :rtype: float
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """Sets the tax_amount of this PutOtherPaymentsOtherPayment.

        The tax amount of the payment  # noqa: E501

        :param tax_amount: The tax_amount of this PutOtherPaymentsOtherPayment.  # noqa: E501
        :type: float
        """

        self._tax_amount = tax_amount

    @property
    def reference(self):
        """Gets the reference of this PutOtherPaymentsOtherPayment.  # noqa: E501

        A reference of the payment  # noqa: E501

        :return: The reference of this PutOtherPaymentsOtherPayment.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this PutOtherPaymentsOtherPayment.

        A reference of the payment  # noqa: E501

        :param reference: The reference of this PutOtherPaymentsOtherPayment.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def withholding_tax_rate(self):
        """Gets the withholding_tax_rate of this PutOtherPaymentsOtherPayment.  # noqa: E501

        IRPF withheld tax rate  # noqa: E501

        :return: The withholding_tax_rate of this PutOtherPaymentsOtherPayment.  # noqa: E501
        :rtype: float
        """
        return self._withholding_tax_rate

    @withholding_tax_rate.setter
    def withholding_tax_rate(self, withholding_tax_rate):
        """Sets the withholding_tax_rate of this PutOtherPaymentsOtherPayment.

        IRPF withheld tax rate  # noqa: E501

        :param withholding_tax_rate: The withholding_tax_rate of this PutOtherPaymentsOtherPayment.  # noqa: E501
        :type: float
        """

        self._withholding_tax_rate = withholding_tax_rate

    @property
    def withholding_tax_amount(self):
        """Gets the withholding_tax_amount of this PutOtherPaymentsOtherPayment.  # noqa: E501

        IRPF withheld tax amount  # noqa: E501

        :return: The withholding_tax_amount of this PutOtherPaymentsOtherPayment.  # noqa: E501
        :rtype: float
        """
        return self._withholding_tax_amount

    @withholding_tax_amount.setter
    def withholding_tax_amount(self, withholding_tax_amount):
        """Sets the withholding_tax_amount of this PutOtherPaymentsOtherPayment.

        IRPF withheld tax amount  # noqa: E501

        :param withholding_tax_amount: The withholding_tax_amount of this PutOtherPaymentsOtherPayment.  # noqa: E501
        :type: float
        """

        self._withholding_tax_amount = withholding_tax_amount

    @property
    def payment_lines(self):
        """Gets the payment_lines of this PutOtherPaymentsOtherPayment.  # noqa: E501


        :return: The payment_lines of this PutOtherPaymentsOtherPayment.  # noqa: E501
        :rtype: list[PutOtherPaymentsOtherPaymentPaymentLines]
        """
        return self._payment_lines

    @payment_lines.setter
    def payment_lines(self, payment_lines):
        """Sets the payment_lines of this PutOtherPaymentsOtherPayment.


        :param payment_lines: The payment_lines of this PutOtherPaymentsOtherPayment.  # noqa: E501
        :type: list[PutOtherPaymentsOtherPaymentPaymentLines]
        """

        self._payment_lines = payment_lines

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
        if not isinstance(other, PutOtherPaymentsOtherPayment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PutOtherPaymentsOtherPayment):
            return True

        return self.to_dict() != other.to_dict()
