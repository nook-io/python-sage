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


class ContactPaymentPush(object):
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
        'links': 'list[Link]',
        'transaction': 'Base',
        'transaction_type_id': 'str',
        'deleted_at': 'datetime',
        'payment_method_id': 'str',
        'contact_id': 'str',
        'bank_account_id': 'str',
        'date': 'date',
        'net_amount': 'float',
        'tax_amount': 'float',
        'total_amount': 'float',
        'currency_id': 'str',
        'exchange_rate': 'float',
        'base_currency_net_amount': 'float',
        'base_currency_tax_amount': 'float',
        'base_currency_total_amount': 'float',
        'base_currency_currency_charge': 'float',
        'reference': 'str',
        'allocated_artefacts': 'list[AllocatedPaymentArtefact]',
        'tax_rate_id': 'str',
        'payment_on_account': 'PaymentOnAccount',
        'editable': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'displayed_as': 'displayed_as',
        'path': '$path',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'links': 'links',
        'transaction': 'transaction',
        'transaction_type_id': 'transaction_type_id',
        'deleted_at': 'deleted_at',
        'payment_method_id': 'payment_method_id',
        'contact_id': 'contact_id',
        'bank_account_id': 'bank_account_id',
        'date': 'date',
        'net_amount': 'net_amount',
        'tax_amount': 'tax_amount',
        'total_amount': 'total_amount',
        'currency_id': 'currency_id',
        'exchange_rate': 'exchange_rate',
        'base_currency_net_amount': 'base_currency_net_amount',
        'base_currency_tax_amount': 'base_currency_tax_amount',
        'base_currency_total_amount': 'base_currency_total_amount',
        'base_currency_currency_charge': 'base_currency_currency_charge',
        'reference': 'reference',
        'allocated_artefacts': 'allocated_artefacts',
        'tax_rate_id': 'tax_rate_id',
        'payment_on_account': 'payment_on_account',
        'editable': 'editable'
    }

    def __init__(self, id=None, displayed_as=None, path=None, created_at=None, updated_at=None, links=None, transaction=None, transaction_type_id=None, deleted_at=None, payment_method_id=None, contact_id=None, bank_account_id=None, date=None, net_amount=None, tax_amount=None, total_amount=None, currency_id=None, exchange_rate=None, base_currency_net_amount=None, base_currency_tax_amount=None, base_currency_total_amount=None, base_currency_currency_charge=None, reference=None, allocated_artefacts=None, tax_rate_id=None, payment_on_account=None, editable=None, local_vars_configuration=None):  # noqa: E501
        """ContactPayment - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._displayed_as = None
        self._path = None
        self._created_at = None
        self._updated_at = None
        self._links = None
        self._transaction = None
        self._transaction_type_id = None
        self._deleted_at = None
        self._payment_method_id = None
        self._contact_id = None
        self._bank_account_id = None
        self._date = None
        self._net_amount = None
        self._tax_amount = None
        self._total_amount = None
        self._currency_id = None
        self._exchange_rate = None
        self._base_currency_net_amount = None
        self._base_currency_tax_amount = None
        self._base_currency_total_amount = None
        self._base_currency_currency_charge = None
        self._reference = None
        self._allocated_artefacts = None
        self._tax_rate_id = None
        self._payment_on_account = None
        self._editable = None
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
        if links is not None:
            self.links = links
        if transaction is not None:
            self.transaction = transaction
        if transaction_type_id is not None:
            self.transaction_type_id = transaction_type_id
        if deleted_at is not None:
            self.deleted_at = deleted_at
        if payment_method_id is not None:
            self.payment_method_id = payment_method_id
        if contact_id is not None:
            self.contact_id = contact_id
        if bank_account_id is not None:
            self.bank_account_id = bank_account_id
        if date is not None:
            self.date = date
        if net_amount is not None:
            self.net_amount = net_amount
        if tax_amount is not None:
            self.tax_amount = tax_amount
        if total_amount is not None:
            self.total_amount = total_amount
        if currency_id is not None:
            self.currency_id = currency_id
        if exchange_rate is not None:
            self.exchange_rate = exchange_rate
        if base_currency_net_amount is not None:
            self.base_currency_net_amount = base_currency_net_amount
        if base_currency_tax_amount is not None:
            self.base_currency_tax_amount = base_currency_tax_amount
        if base_currency_total_amount is not None:
            self.base_currency_total_amount = base_currency_total_amount
        if base_currency_currency_charge is not None:
            self.base_currency_currency_charge = base_currency_currency_charge
        if reference is not None:
            self.reference = reference
        if allocated_artefacts is not None:
            self.allocated_artefacts = allocated_artefacts
        if tax_rate_id is not None:
            self.tax_rate_id = tax_rate_id
        if payment_on_account is not None:
            self.payment_on_account = payment_on_account
        if editable is not None:
            self.editable = editable

    @property
    def id(self):
        """Gets the id of this ContactPayment.  # noqa: E501

        The unique identifier for the item  # noqa: E501

        :return: The id of this ContactPayment.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ContactPayment.

        The unique identifier for the item  # noqa: E501

        :param id: The id of this ContactPayment.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def displayed_as(self):
        """Gets the displayed_as of this ContactPayment.  # noqa: E501

        The name of the resource  # noqa: E501

        :return: The displayed_as of this ContactPayment.  # noqa: E501
        :rtype: str
        """
        return self._displayed_as

    @displayed_as.setter
    def displayed_as(self, displayed_as):
        """Sets the displayed_as of this ContactPayment.

        The name of the resource  # noqa: E501

        :param displayed_as: The displayed_as of this ContactPayment.  # noqa: E501
        :type: str
        """

        self._displayed_as = displayed_as

    @property
    def path(self):
        """Gets the path of this ContactPayment.  # noqa: E501

        The API path for the resource  # noqa: E501

        :return: The path of this ContactPayment.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ContactPayment.

        The API path for the resource  # noqa: E501

        :param path: The path of this ContactPayment.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def created_at(self):
        """Gets the created_at of this ContactPayment.  # noqa: E501

        The datetime when the item was created  # noqa: E501

        :return: The created_at of this ContactPayment.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ContactPayment.

        The datetime when the item was created  # noqa: E501

        :param created_at: The created_at of this ContactPayment.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ContactPayment.  # noqa: E501

        The datetime when the item was last updated  # noqa: E501

        :return: The updated_at of this ContactPayment.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ContactPayment.

        The datetime when the item was last updated  # noqa: E501

        :param updated_at: The updated_at of this ContactPayment.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def links(self):
        """Gets the links of this ContactPayment.  # noqa: E501

        Links for the resource  # noqa: E501

        :return: The links of this ContactPayment.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ContactPayment.

        Links for the resource  # noqa: E501

        :param links: The links of this ContactPayment.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def transaction(self):
        """Gets the transaction of this ContactPayment.  # noqa: E501


        :return: The transaction of this ContactPayment.  # noqa: E501
        :rtype: Base
        """
        return self._transaction

    @transaction.setter
    def transaction(self, transaction):
        """Sets the transaction of this ContactPayment.


        :param transaction: The transaction of this ContactPayment.  # noqa: E501
        :type: Base
        """

        self._transaction = transaction

    @property
    def transaction_type_id(self):
        """Gets the transaction_type_id of this ContactPayment.  # noqa: E501


        :return: The transaction_type_id of this ContactPayment.  # noqa: E501
        :rtype: Base
        """
        return self._transaction_type_id

    @transaction_type_id.setter
    def transaction_type_id(self, transaction_type_id):
        """Sets the transaction_type_id of this ContactPayment.


        :param transaction_type_id: The transaction_type_id of this ContactPayment.  # noqa: E501
        :type: Base
        """

        self._transaction_type_id = transaction_type_id

    @property
    def deleted_at(self):
        """Gets the deleted_at of this ContactPayment.  # noqa: E501

        The datetime when the item was deleted  # noqa: E501

        :return: The deleted_at of this ContactPayment.  # noqa: E501
        :rtype: datetime
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """Sets the deleted_at of this ContactPayment.

        The datetime when the item was deleted  # noqa: E501

        :param deleted_at: The deleted_at of this ContactPayment.  # noqa: E501
        :type: datetime
        """

        self._deleted_at = deleted_at

    @property
    def payment_method_id(self):
        """Gets the payment_method_id of this ContactPayment.  # noqa: E501


        :return: The payment_method_id of this ContactPayment.  # noqa: E501
        :rtype: Base
        """
        return self._payment_method_id

    @payment_method_id.setter
    def payment_method_id(self, payment_method_id):
        """Sets the payment_method_id of this ContactPayment.


        :param payment_method_id: The payment_method_id of this ContactPayment.  # noqa: E501
        :type: Base
        """

        self._payment_method_id = payment_method_id

    @property
    def contact_id(self):
        """Gets the contact_id of this ContactPayment.  # noqa: E501


        :return: The contact_id of this ContactPayment.  # noqa: E501
        :rtype: Base
        """
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        """Sets the contact_id of this ContactPayment.


        :param contact_id: The contact_id of this ContactPayment.  # noqa: E501
        :type: Base
        """

        self._contact_id = contact_id

    @property
    def bank_account_id(self):
        """Gets the bank_account_id of this ContactPayment.  # noqa: E501


        :return: The bank_account_id of this ContactPayment.  # noqa: E501
        :rtype: Base
        """
        return self._bank_account_id

    @bank_account_id.setter
    def bank_account_id(self, bank_account_id):
        """Sets the bank_account_id of this ContactPayment.


        :param bank_account_id: The bank_account_id of this ContactPayment.  # noqa: E501
        :type: Base
        """

        self._bank_account_id = bank_account_id

    @property
    def date(self):
        """Gets the date of this ContactPayment.  # noqa: E501

        The date the payment was made  # noqa: E501

        :return: The date of this ContactPayment.  # noqa: E501
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this ContactPayment.

        The date the payment was made  # noqa: E501

        :param date: The date of this ContactPayment.  # noqa: E501
        :type: date
        """

        self._date = date

    @property
    def net_amount(self):
        """Gets the net_amount of this ContactPayment.  # noqa: E501

        The net amount of the payment  # noqa: E501

        :return: The net_amount of this ContactPayment.  # noqa: E501
        :rtype: float
        """
        return self._net_amount

    @net_amount.setter
    def net_amount(self, net_amount):
        """Sets the net_amount of this ContactPayment.

        The net amount of the payment  # noqa: E501

        :param net_amount: The net_amount of this ContactPayment.  # noqa: E501
        :type: float
        """

        self._net_amount = net_amount

    @property
    def tax_amount(self):
        """Gets the tax_amount of this ContactPayment.  # noqa: E501

        The tax amount of the payment  # noqa: E501

        :return: The tax_amount of this ContactPayment.  # noqa: E501
        :rtype: float
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """Sets the tax_amount of this ContactPayment.

        The tax amount of the payment  # noqa: E501

        :param tax_amount: The tax_amount of this ContactPayment.  # noqa: E501
        :type: float
        """

        self._tax_amount = tax_amount

    @property
    def total_amount(self):
        """Gets the total_amount of this ContactPayment.  # noqa: E501

        The total amount of the payment  # noqa: E501

        :return: The total_amount of this ContactPayment.  # noqa: E501
        :rtype: float
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """Sets the total_amount of this ContactPayment.

        The total amount of the payment  # noqa: E501

        :param total_amount: The total_amount of this ContactPayment.  # noqa: E501
        :type: float
        """

        self._total_amount = total_amount

    @property
    def currency_id(self):
        """Gets the currency_id of this ContactPayment.  # noqa: E501


        :return: The currency_id of this ContactPayment.  # noqa: E501
        :rtype: Base
        """
        return self._currency_id

    @currency_id.setter
    def currency_id(self, currency_id):
        """Sets the currency_id of this ContactPayment.


        :param currency_id: The currency_id of this ContactPayment.  # noqa: E501
        :type: Base
        """

        self._currency_id = currency_id

    @property
    def exchange_rate(self):
        """Gets the exchange_rate of this ContactPayment.  # noqa: E501

        The exchange rate of the payment  # noqa: E501

        :return: The exchange_rate of this ContactPayment.  # noqa: E501
        :rtype: float
        """
        return self._exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, exchange_rate):
        """Sets the exchange_rate of this ContactPayment.

        The exchange rate of the payment  # noqa: E501

        :param exchange_rate: The exchange_rate of this ContactPayment.  # noqa: E501
        :type: float
        """

        self._exchange_rate = exchange_rate

    @property
    def base_currency_net_amount(self):
        """Gets the base_currency_net_amount of this ContactPayment.  # noqa: E501

        The net amount of the payment in base currency  # noqa: E501

        :return: The base_currency_net_amount of this ContactPayment.  # noqa: E501
        :rtype: float
        """
        return self._base_currency_net_amount

    @base_currency_net_amount.setter
    def base_currency_net_amount(self, base_currency_net_amount):
        """Sets the base_currency_net_amount of this ContactPayment.

        The net amount of the payment in base currency  # noqa: E501

        :param base_currency_net_amount: The base_currency_net_amount of this ContactPayment.  # noqa: E501
        :type: float
        """

        self._base_currency_net_amount = base_currency_net_amount

    @property
    def base_currency_tax_amount(self):
        """Gets the base_currency_tax_amount of this ContactPayment.  # noqa: E501

        The tax amount of the payment in base currency  # noqa: E501

        :return: The base_currency_tax_amount of this ContactPayment.  # noqa: E501
        :rtype: float
        """
        return self._base_currency_tax_amount

    @base_currency_tax_amount.setter
    def base_currency_tax_amount(self, base_currency_tax_amount):
        """Sets the base_currency_tax_amount of this ContactPayment.

        The tax amount of the payment in base currency  # noqa: E501

        :param base_currency_tax_amount: The base_currency_tax_amount of this ContactPayment.  # noqa: E501
        :type: float
        """

        self._base_currency_tax_amount = base_currency_tax_amount

    @property
    def base_currency_total_amount(self):
        """Gets the base_currency_total_amount of this ContactPayment.  # noqa: E501

        The total amount of the payment in base currency  # noqa: E501

        :return: The base_currency_total_amount of this ContactPayment.  # noqa: E501
        :rtype: float
        """
        return self._base_currency_total_amount

    @base_currency_total_amount.setter
    def base_currency_total_amount(self, base_currency_total_amount):
        """Sets the base_currency_total_amount of this ContactPayment.

        The total amount of the payment in base currency  # noqa: E501

        :param base_currency_total_amount: The base_currency_total_amount of this ContactPayment.  # noqa: E501
        :type: float
        """

        self._base_currency_total_amount = base_currency_total_amount

    @property
    def base_currency_currency_charge(self):
        """Gets the base_currency_currency_charge of this ContactPayment.  # noqa: E501

        The currency conversion charges in base currency  # noqa: E501

        :return: The base_currency_currency_charge of this ContactPayment.  # noqa: E501
        :rtype: float
        """
        return self._base_currency_currency_charge

    @base_currency_currency_charge.setter
    def base_currency_currency_charge(self, base_currency_currency_charge):
        """Sets the base_currency_currency_charge of this ContactPayment.

        The currency conversion charges in base currency  # noqa: E501

        :param base_currency_currency_charge: The base_currency_currency_charge of this ContactPayment.  # noqa: E501
        :type: float
        """

        self._base_currency_currency_charge = base_currency_currency_charge

    @property
    def reference(self):
        """Gets the reference of this ContactPayment.  # noqa: E501

        A reference for the payment Note: An upper length limit of 25 or 40 characters is imposed conditionally and may not apply in every request. A hard upper limit of 255 characters is imposed by the storage layer, though.  # noqa: E501

        :return: The reference of this ContactPayment.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this ContactPayment.

        A reference for the payment Note: An upper length limit of 25 or 40 characters is imposed conditionally and may not apply in every request. A hard upper limit of 255 characters is imposed by the storage layer, though.  # noqa: E501

        :param reference: The reference of this ContactPayment.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                reference is not None and len(reference) > 25):
            raise ValueError("Invalid value for `reference`, length must be less than or equal to `25`")  # noqa: E501

        self._reference = reference

    @property
    def allocated_artefacts(self):
        """Gets the allocated_artefacts of this ContactPayment.  # noqa: E501

        The allocated artefacts  # noqa: E501

        :return: The allocated_artefacts of this ContactPayment.  # noqa: E501
        :rtype: list[AllocatedPaymentArtefact]
        """
        return self._allocated_artefacts

    @allocated_artefacts.setter
    def allocated_artefacts(self, allocated_artefacts):
        """Sets the allocated_artefacts of this ContactPayment.

        The allocated artefacts  # noqa: E501

        :param allocated_artefacts: The allocated_artefacts of this ContactPayment.  # noqa: E501
        :type: list[AllocatedPaymentArtefact]
        """

        self._allocated_artefacts = allocated_artefacts

    @property
    def tax_rate_id(self):
        """Gets the tax_rate_id of this ContactPayment.  # noqa: E501


        :return: The tax_rate_id of this ContactPayment.  # noqa: E501
        :rtype: Base
        """
        return self._tax_rate_id

    @tax_rate_id.setter
    def tax_rate_id(self, tax_rate_id):
        """Sets the tax_rate_id of this ContactPayment.


        :param tax_rate_id: The tax_rate_id of this ContactPayment.  # noqa: E501
        :type: Base
        """

        self._tax_rate_id = tax_rate_id

    @property
    def payment_on_account(self):
        """Gets the payment_on_account of this ContactPayment.  # noqa: E501


        :return: The payment_on_account of this ContactPayment.  # noqa: E501
        :rtype: PaymentOnAccount
        """
        return self._payment_on_account

    @payment_on_account.setter
    def payment_on_account(self, payment_on_account):
        """Sets the payment_on_account of this ContactPayment.


        :param payment_on_account: The payment_on_account of this ContactPayment.  # noqa: E501
        :type: PaymentOnAccount
        """

        self._payment_on_account = payment_on_account

    @property
    def editable(self):
        """Gets the editable of this ContactPayment.  # noqa: E501

        Indicates whether payment can be edited  # noqa: E501

        :return: The editable of this ContactPayment.  # noqa: E501
        :rtype: bool
        """
        return self._editable

    @editable.setter
    def editable(self, editable):
        """Sets the editable of this ContactPayment.

        Indicates whether payment can be edited  # noqa: E501

        :param editable: The editable of this ContactPayment.  # noqa: E501
        :type: bool
        """

        self._editable = editable

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
        if not isinstance(other, ContactPayment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ContactPayment):
            return True

        return self.to_dict() != other.to_dict()