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


class Service(object):
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
        'deleted_at': 'datetime',
        'deletable': 'bool',
        'deactivatable': 'bool',
        'used_on_recurring_invoice': 'bool',
        'item_code': 'str',
        'description': 'str',
        'notes': 'str',
        'sales_ledger_account': 'Base',
        'purchase_ledger_account': 'Base',
        'sales_tax_rate': 'Base',
        'purchase_tax_rate': 'Base',
        'sales_rates': 'list[Rate]',
        'source_guid': 'str',
        'purchase_description': 'str',
        'usual_supplier': 'Contact',
        'active': 'bool',
        'cost_price': 'float'
    }

    attribute_map = {
        'id': 'id',
        'displayed_as': 'displayed_as',
        'path': '$path',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'deleted_at': 'deleted_at',
        'deletable': 'deletable',
        'deactivatable': 'deactivatable',
        'used_on_recurring_invoice': 'used_on_recurring_invoice',
        'item_code': 'item_code',
        'description': 'description',
        'notes': 'notes',
        'sales_ledger_account': 'sales_ledger_account',
        'purchase_ledger_account': 'purchase_ledger_account',
        'sales_tax_rate': 'sales_tax_rate',
        'purchase_tax_rate': 'purchase_tax_rate',
        'sales_rates': 'sales_rates',
        'source_guid': 'source_guid',
        'purchase_description': 'purchase_description',
        'usual_supplier': 'usual_supplier',
        'active': 'active',
        'cost_price': 'cost_price'
    }

    def __init__(self, id=None, displayed_as=None, path=None, created_at=None, updated_at=None, deleted_at=None, deletable=None, deactivatable=None, used_on_recurring_invoice=None, item_code=None, description=None, notes=None, sales_ledger_account=None, purchase_ledger_account=None, sales_tax_rate=None, purchase_tax_rate=None, sales_rates=None, source_guid=None, purchase_description=None, usual_supplier=None, active=None, cost_price=None, local_vars_configuration=None):  # noqa: E501
        """Service - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._displayed_as = None
        self._path = None
        self._created_at = None
        self._updated_at = None
        self._deleted_at = None
        self._deletable = None
        self._deactivatable = None
        self._used_on_recurring_invoice = None
        self._item_code = None
        self._description = None
        self._notes = None
        self._sales_ledger_account = None
        self._purchase_ledger_account = None
        self._sales_tax_rate = None
        self._purchase_tax_rate = None
        self._sales_rates = None
        self._source_guid = None
        self._purchase_description = None
        self._usual_supplier = None
        self._active = None
        self._cost_price = None
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
        if deleted_at is not None:
            self.deleted_at = deleted_at
        if deletable is not None:
            self.deletable = deletable
        if deactivatable is not None:
            self.deactivatable = deactivatable
        if used_on_recurring_invoice is not None:
            self.used_on_recurring_invoice = used_on_recurring_invoice
        if item_code is not None:
            self.item_code = item_code
        if description is not None:
            self.description = description
        if notes is not None:
            self.notes = notes
        if sales_ledger_account is not None:
            self.sales_ledger_account = sales_ledger_account
        if purchase_ledger_account is not None:
            self.purchase_ledger_account = purchase_ledger_account
        if sales_tax_rate is not None:
            self.sales_tax_rate = sales_tax_rate
        if purchase_tax_rate is not None:
            self.purchase_tax_rate = purchase_tax_rate
        if sales_rates is not None:
            self.sales_rates = sales_rates
        if source_guid is not None:
            self.source_guid = source_guid
        if purchase_description is not None:
            self.purchase_description = purchase_description
        if usual_supplier is not None:
            self.usual_supplier = usual_supplier
        if active is not None:
            self.active = active
        if cost_price is not None:
            self.cost_price = cost_price

    @property
    def id(self):
        """Gets the id of this Service.  # noqa: E501

        The unique identifier for the item  # noqa: E501

        :return: The id of this Service.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Service.

        The unique identifier for the item  # noqa: E501

        :param id: The id of this Service.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def displayed_as(self):
        """Gets the displayed_as of this Service.  # noqa: E501

        The name of the resource  # noqa: E501

        :return: The displayed_as of this Service.  # noqa: E501
        :rtype: str
        """
        return self._displayed_as

    @displayed_as.setter
    def displayed_as(self, displayed_as):
        """Sets the displayed_as of this Service.

        The name of the resource  # noqa: E501

        :param displayed_as: The displayed_as of this Service.  # noqa: E501
        :type: str
        """

        self._displayed_as = displayed_as

    @property
    def path(self):
        """Gets the path of this Service.  # noqa: E501

        The API path for the resource  # noqa: E501

        :return: The path of this Service.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this Service.

        The API path for the resource  # noqa: E501

        :param path: The path of this Service.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def created_at(self):
        """Gets the created_at of this Service.  # noqa: E501

        The datetime when the item was created  # noqa: E501

        :return: The created_at of this Service.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Service.

        The datetime when the item was created  # noqa: E501

        :param created_at: The created_at of this Service.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Service.  # noqa: E501

        The datetime when the item was last updated  # noqa: E501

        :return: The updated_at of this Service.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Service.

        The datetime when the item was last updated  # noqa: E501

        :param updated_at: The updated_at of this Service.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def deleted_at(self):
        """Gets the deleted_at of this Service.  # noqa: E501

        The datetime when the item was deleted  # noqa: E501

        :return: The deleted_at of this Service.  # noqa: E501
        :rtype: datetime
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """Sets the deleted_at of this Service.

        The datetime when the item was deleted  # noqa: E501

        :param deleted_at: The deleted_at of this Service.  # noqa: E501
        :type: datetime
        """

        self._deleted_at = deleted_at

    @property
    def deletable(self):
        """Gets the deletable of this Service.  # noqa: E501

        Indicates whether the service can be deleted  # noqa: E501

        :return: The deletable of this Service.  # noqa: E501
        :rtype: bool
        """
        return self._deletable

    @deletable.setter
    def deletable(self, deletable):
        """Sets the deletable of this Service.

        Indicates whether the service can be deleted  # noqa: E501

        :param deletable: The deletable of this Service.  # noqa: E501
        :type: bool
        """

        self._deletable = deletable

    @property
    def deactivatable(self):
        """Gets the deactivatable of this Service.  # noqa: E501

        Indicates whether the service can be deactivated  # noqa: E501

        :return: The deactivatable of this Service.  # noqa: E501
        :rtype: bool
        """
        return self._deactivatable

    @deactivatable.setter
    def deactivatable(self, deactivatable):
        """Sets the deactivatable of this Service.

        Indicates whether the service can be deactivated  # noqa: E501

        :param deactivatable: The deactivatable of this Service.  # noqa: E501
        :type: bool
        """

        self._deactivatable = deactivatable

    @property
    def used_on_recurring_invoice(self):
        """Gets the used_on_recurring_invoice of this Service.  # noqa: E501

        Indicates whether the service has been used on a recurring invoice  # noqa: E501

        :return: The used_on_recurring_invoice of this Service.  # noqa: E501
        :rtype: bool
        """
        return self._used_on_recurring_invoice

    @used_on_recurring_invoice.setter
    def used_on_recurring_invoice(self, used_on_recurring_invoice):
        """Sets the used_on_recurring_invoice of this Service.

        Indicates whether the service has been used on a recurring invoice  # noqa: E501

        :param used_on_recurring_invoice: The used_on_recurring_invoice of this Service.  # noqa: E501
        :type: bool
        """

        self._used_on_recurring_invoice = used_on_recurring_invoice

    @property
    def item_code(self):
        """Gets the item_code of this Service.  # noqa: E501

        The item code for the service  # noqa: E501

        :return: The item_code of this Service.  # noqa: E501
        :rtype: str
        """
        return self._item_code

    @item_code.setter
    def item_code(self, item_code):
        """Sets the item_code of this Service.

        The item code for the service  # noqa: E501

        :param item_code: The item_code of this Service.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                item_code is not None and len(item_code) > 255):
            raise ValueError("Invalid value for `item_code`, length must be less than or equal to `255`")  # noqa: E501

        self._item_code = item_code

    @property
    def description(self):
        """Gets the description of this Service.  # noqa: E501

        The service description  # noqa: E501

        :return: The description of this Service.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Service.

        The service description  # noqa: E501

        :param description: The description of this Service.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 255):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")  # noqa: E501

        self._description = description

    @property
    def notes(self):
        """Gets the notes of this Service.  # noqa: E501

        The notes for the service  # noqa: E501

        :return: The notes of this Service.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this Service.

        The notes for the service  # noqa: E501

        :param notes: The notes of this Service.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                notes is not None and len(notes) > 500):
            raise ValueError("Invalid value for `notes`, length must be less than or equal to `500`")  # noqa: E501

        self._notes = notes

    @property
    def sales_ledger_account(self):
        """Gets the sales_ledger_account of this Service.  # noqa: E501


        :return: The sales_ledger_account of this Service.  # noqa: E501
        :rtype: Base
        """
        return self._sales_ledger_account

    @sales_ledger_account.setter
    def sales_ledger_account(self, sales_ledger_account):
        """Sets the sales_ledger_account of this Service.


        :param sales_ledger_account: The sales_ledger_account of this Service.  # noqa: E501
        :type: Base
        """

        self._sales_ledger_account = sales_ledger_account

    @property
    def purchase_ledger_account(self):
        """Gets the purchase_ledger_account of this Service.  # noqa: E501


        :return: The purchase_ledger_account of this Service.  # noqa: E501
        :rtype: Base
        """
        return self._purchase_ledger_account

    @purchase_ledger_account.setter
    def purchase_ledger_account(self, purchase_ledger_account):
        """Sets the purchase_ledger_account of this Service.


        :param purchase_ledger_account: The purchase_ledger_account of this Service.  # noqa: E501
        :type: Base
        """

        self._purchase_ledger_account = purchase_ledger_account

    @property
    def sales_tax_rate(self):
        """Gets the sales_tax_rate of this Service.  # noqa: E501


        :return: The sales_tax_rate of this Service.  # noqa: E501
        :rtype: Base
        """
        return self._sales_tax_rate

    @sales_tax_rate.setter
    def sales_tax_rate(self, sales_tax_rate):
        """Sets the sales_tax_rate of this Service.


        :param sales_tax_rate: The sales_tax_rate of this Service.  # noqa: E501
        :type: Base
        """

        self._sales_tax_rate = sales_tax_rate

    @property
    def purchase_tax_rate(self):
        """Gets the purchase_tax_rate of this Service.  # noqa: E501


        :return: The purchase_tax_rate of this Service.  # noqa: E501
        :rtype: Base
        """
        return self._purchase_tax_rate

    @purchase_tax_rate.setter
    def purchase_tax_rate(self, purchase_tax_rate):
        """Sets the purchase_tax_rate of this Service.


        :param purchase_tax_rate: The purchase_tax_rate of this Service.  # noqa: E501
        :type: Base
        """

        self._purchase_tax_rate = purchase_tax_rate

    @property
    def sales_rates(self):
        """Gets the sales_rates of this Service.  # noqa: E501

        The sales rates for the service  # noqa: E501

        :return: The sales_rates of this Service.  # noqa: E501
        :rtype: list[Rate]
        """
        return self._sales_rates

    @sales_rates.setter
    def sales_rates(self, sales_rates):
        """Sets the sales_rates of this Service.

        The sales rates for the service  # noqa: E501

        :param sales_rates: The sales_rates of this Service.  # noqa: E501
        :type: list[Rate]
        """

        self._sales_rates = sales_rates

    @property
    def source_guid(self):
        """Gets the source_guid of this Service.  # noqa: E501

        Used when importing services from external sources  # noqa: E501

        :return: The source_guid of this Service.  # noqa: E501
        :rtype: str
        """
        return self._source_guid

    @source_guid.setter
    def source_guid(self, source_guid):
        """Sets the source_guid of this Service.

        Used when importing services from external sources  # noqa: E501

        :param source_guid: The source_guid of this Service.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                source_guid is not None and len(source_guid) > 255):
            raise ValueError("Invalid value for `source_guid`, length must be less than or equal to `255`")  # noqa: E501

        self._source_guid = source_guid

    @property
    def purchase_description(self):
        """Gets the purchase_description of this Service.  # noqa: E501

        The service purchase description  # noqa: E501

        :return: The purchase_description of this Service.  # noqa: E501
        :rtype: str
        """
        return self._purchase_description

    @purchase_description.setter
    def purchase_description(self, purchase_description):
        """Sets the purchase_description of this Service.

        The service purchase description  # noqa: E501

        :param purchase_description: The purchase_description of this Service.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                purchase_description is not None and len(purchase_description) > 250):
            raise ValueError("Invalid value for `purchase_description`, length must be less than or equal to `250`")  # noqa: E501

        self._purchase_description = purchase_description

    @property
    def usual_supplier(self):
        """Gets the usual_supplier of this Service.  # noqa: E501


        :return: The usual_supplier of this Service.  # noqa: E501
        :rtype: Contact
        """
        return self._usual_supplier

    @usual_supplier.setter
    def usual_supplier(self, usual_supplier):
        """Sets the usual_supplier of this Service.


        :param usual_supplier: The usual_supplier of this Service.  # noqa: E501
        :type: Contact
        """

        self._usual_supplier = usual_supplier

    @property
    def active(self):
        """Gets the active of this Service.  # noqa: E501

        Indicates whether the service is active  # noqa: E501

        :return: The active of this Service.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this Service.

        Indicates whether the service is active  # noqa: E501

        :param active: The active of this Service.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def cost_price(self):
        """Gets the cost_price of this Service.  # noqa: E501

        The cost price of the service  # noqa: E501

        :return: The cost_price of this Service.  # noqa: E501
        :rtype: float
        """
        return self._cost_price

    @cost_price.setter
    def cost_price(self, cost_price):
        """Sets the cost_price of this Service.

        The cost price of the service  # noqa: E501

        :param cost_price: The cost_price of this Service.  # noqa: E501
        :type: float
        """

        self._cost_price = cost_price

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
        if not isinstance(other, Service):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Service):
            return True

        return self.to_dict() != other.to_dict()