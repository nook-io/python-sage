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


class PostProductsProduct(object):
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
        'description': 'str',
        'sales_ledger_account_id': 'str',
        'purchase_ledger_account_id': 'str',
        'item_code': 'str',
        'notes': 'str',
        'sales_tax_rate_id': 'str',
        'usual_supplier_id': 'str',
        'purchase_tax_rate_id': 'str',
        'cost_price': 'float',
        'source_guid': 'str',
        'purchase_description': 'str',
        'active': 'bool',
        'catalog_item_type_id': 'str',
        'sales_prices': 'list[PostProductsProductSalesPrices]'
    }

    attribute_map = {
        'description': 'description',
        'sales_ledger_account_id': 'sales_ledger_account_id',
        'purchase_ledger_account_id': 'purchase_ledger_account_id',
        'item_code': 'item_code',
        'notes': 'notes',
        'sales_tax_rate_id': 'sales_tax_rate_id',
        'usual_supplier_id': 'usual_supplier_id',
        'purchase_tax_rate_id': 'purchase_tax_rate_id',
        'cost_price': 'cost_price',
        'source_guid': 'source_guid',
        'purchase_description': 'purchase_description',
        'active': 'active',
        'catalog_item_type_id': 'catalog_item_type_id',
        'sales_prices': 'sales_prices'
    }

    def __init__(self, description=None, sales_ledger_account_id=None, purchase_ledger_account_id=None, item_code=None, notes=None, sales_tax_rate_id=None, usual_supplier_id=None, purchase_tax_rate_id=None, cost_price=None, source_guid=None, purchase_description=None, active=None, catalog_item_type_id=None, sales_prices=None, local_vars_configuration=None):  # noqa: E501
        """PostProductsProduct - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._sales_ledger_account_id = None
        self._purchase_ledger_account_id = None
        self._item_code = None
        self._notes = None
        self._sales_tax_rate_id = None
        self._usual_supplier_id = None
        self._purchase_tax_rate_id = None
        self._cost_price = None
        self._source_guid = None
        self._purchase_description = None
        self._active = None
        self._catalog_item_type_id = None
        self._sales_prices = None
        self.discriminator = None

        self.description = description
        self.sales_ledger_account_id = sales_ledger_account_id
        self.purchase_ledger_account_id = purchase_ledger_account_id
        if item_code is not None:
            self.item_code = item_code
        if notes is not None:
            self.notes = notes
        if sales_tax_rate_id is not None:
            self.sales_tax_rate_id = sales_tax_rate_id
        if usual_supplier_id is not None:
            self.usual_supplier_id = usual_supplier_id
        if purchase_tax_rate_id is not None:
            self.purchase_tax_rate_id = purchase_tax_rate_id
        if cost_price is not None:
            self.cost_price = cost_price
        if source_guid is not None:
            self.source_guid = source_guid
        if purchase_description is not None:
            self.purchase_description = purchase_description
        if active is not None:
            self.active = active
        if catalog_item_type_id is not None:
            self.catalog_item_type_id = catalog_item_type_id
        if sales_prices is not None:
            self.sales_prices = sales_prices

    @property
    def description(self):
        """Gets the description of this PostProductsProduct.  # noqa: E501

        The product description  # noqa: E501

        :return: The description of this PostProductsProduct.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PostProductsProduct.

        The product description  # noqa: E501

        :param description: The description of this PostProductsProduct.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def sales_ledger_account_id(self):
        """Gets the sales_ledger_account_id of this PostProductsProduct.  # noqa: E501

        The sales ledger account for the product  # noqa: E501

        :return: The sales_ledger_account_id of this PostProductsProduct.  # noqa: E501
        :rtype: str
        """
        return self._sales_ledger_account_id

    @sales_ledger_account_id.setter
    def sales_ledger_account_id(self, sales_ledger_account_id):
        """Sets the sales_ledger_account_id of this PostProductsProduct.

        The sales ledger account for the product  # noqa: E501

        :param sales_ledger_account_id: The sales_ledger_account_id of this PostProductsProduct.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and sales_ledger_account_id is None:  # noqa: E501
            raise ValueError("Invalid value for `sales_ledger_account_id`, must not be `None`")  # noqa: E501

        self._sales_ledger_account_id = sales_ledger_account_id

    @property
    def purchase_ledger_account_id(self):
        """Gets the purchase_ledger_account_id of this PostProductsProduct.  # noqa: E501

        The purchase ledger account for the product  # noqa: E501

        :return: The purchase_ledger_account_id of this PostProductsProduct.  # noqa: E501
        :rtype: str
        """
        return self._purchase_ledger_account_id

    @purchase_ledger_account_id.setter
    def purchase_ledger_account_id(self, purchase_ledger_account_id):
        """Sets the purchase_ledger_account_id of this PostProductsProduct.

        The purchase ledger account for the product  # noqa: E501

        :param purchase_ledger_account_id: The purchase_ledger_account_id of this PostProductsProduct.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and purchase_ledger_account_id is None:  # noqa: E501
            raise ValueError("Invalid value for `purchase_ledger_account_id`, must not be `None`")  # noqa: E501

        self._purchase_ledger_account_id = purchase_ledger_account_id

    @property
    def item_code(self):
        """Gets the item_code of this PostProductsProduct.  # noqa: E501

        The item code for the product  # noqa: E501

        :return: The item_code of this PostProductsProduct.  # noqa: E501
        :rtype: str
        """
        return self._item_code

    @item_code.setter
    def item_code(self, item_code):
        """Sets the item_code of this PostProductsProduct.

        The item code for the product  # noqa: E501

        :param item_code: The item_code of this PostProductsProduct.  # noqa: E501
        :type: str
        """

        self._item_code = item_code

    @property
    def notes(self):
        """Gets the notes of this PostProductsProduct.  # noqa: E501

        The notes for the product  # noqa: E501

        :return: The notes of this PostProductsProduct.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this PostProductsProduct.

        The notes for the product  # noqa: E501

        :param notes: The notes of this PostProductsProduct.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def sales_tax_rate_id(self):
        """Gets the sales_tax_rate_id of this PostProductsProduct.  # noqa: E501

        The ID of the Sales Tax Rate.  # noqa: E501

        :return: The sales_tax_rate_id of this PostProductsProduct.  # noqa: E501
        :rtype: str
        """
        return self._sales_tax_rate_id

    @sales_tax_rate_id.setter
    def sales_tax_rate_id(self, sales_tax_rate_id):
        """Sets the sales_tax_rate_id of this PostProductsProduct.

        The ID of the Sales Tax Rate.  # noqa: E501

        :param sales_tax_rate_id: The sales_tax_rate_id of this PostProductsProduct.  # noqa: E501
        :type: str
        """

        self._sales_tax_rate_id = sales_tax_rate_id

    @property
    def usual_supplier_id(self):
        """Gets the usual_supplier_id of this PostProductsProduct.  # noqa: E501

        The ID of the Usual Supplier.  # noqa: E501

        :return: The usual_supplier_id of this PostProductsProduct.  # noqa: E501
        :rtype: str
        """
        return self._usual_supplier_id

    @usual_supplier_id.setter
    def usual_supplier_id(self, usual_supplier_id):
        """Sets the usual_supplier_id of this PostProductsProduct.

        The ID of the Usual Supplier.  # noqa: E501

        :param usual_supplier_id: The usual_supplier_id of this PostProductsProduct.  # noqa: E501
        :type: str
        """

        self._usual_supplier_id = usual_supplier_id

    @property
    def purchase_tax_rate_id(self):
        """Gets the purchase_tax_rate_id of this PostProductsProduct.  # noqa: E501

        The ID of the Purchase Tax Rate.  # noqa: E501

        :return: The purchase_tax_rate_id of this PostProductsProduct.  # noqa: E501
        :rtype: str
        """
        return self._purchase_tax_rate_id

    @purchase_tax_rate_id.setter
    def purchase_tax_rate_id(self, purchase_tax_rate_id):
        """Sets the purchase_tax_rate_id of this PostProductsProduct.

        The ID of the Purchase Tax Rate.  # noqa: E501

        :param purchase_tax_rate_id: The purchase_tax_rate_id of this PostProductsProduct.  # noqa: E501
        :type: str
        """

        self._purchase_tax_rate_id = purchase_tax_rate_id

    @property
    def cost_price(self):
        """Gets the cost_price of this PostProductsProduct.  # noqa: E501

        The cost price of the product  # noqa: E501

        :return: The cost_price of this PostProductsProduct.  # noqa: E501
        :rtype: float
        """
        return self._cost_price

    @cost_price.setter
    def cost_price(self, cost_price):
        """Sets the cost_price of this PostProductsProduct.

        The cost price of the product  # noqa: E501

        :param cost_price: The cost_price of this PostProductsProduct.  # noqa: E501
        :type: float
        """

        self._cost_price = cost_price

    @property
    def source_guid(self):
        """Gets the source_guid of this PostProductsProduct.  # noqa: E501

        Used when importing products from external sources  # noqa: E501

        :return: The source_guid of this PostProductsProduct.  # noqa: E501
        :rtype: str
        """
        return self._source_guid

    @source_guid.setter
    def source_guid(self, source_guid):
        """Sets the source_guid of this PostProductsProduct.

        Used when importing products from external sources  # noqa: E501

        :param source_guid: The source_guid of this PostProductsProduct.  # noqa: E501
        :type: str
        """

        self._source_guid = source_guid

    @property
    def purchase_description(self):
        """Gets the purchase_description of this PostProductsProduct.  # noqa: E501

        The product purchase description  # noqa: E501

        :return: The purchase_description of this PostProductsProduct.  # noqa: E501
        :rtype: str
        """
        return self._purchase_description

    @purchase_description.setter
    def purchase_description(self, purchase_description):
        """Sets the purchase_description of this PostProductsProduct.

        The product purchase description  # noqa: E501

        :param purchase_description: The purchase_description of this PostProductsProduct.  # noqa: E501
        :type: str
        """

        self._purchase_description = purchase_description

    @property
    def active(self):
        """Gets the active of this PostProductsProduct.  # noqa: E501

        Indicates whether the product is active  # noqa: E501

        :return: The active of this PostProductsProduct.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this PostProductsProduct.

        Indicates whether the product is active  # noqa: E501

        :param active: The active of this PostProductsProduct.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def catalog_item_type_id(self):
        """Gets the catalog_item_type_id of this PostProductsProduct.  # noqa: E501

        The ID of the Catalog Item Type.  # noqa: E501

        :return: The catalog_item_type_id of this PostProductsProduct.  # noqa: E501
        :rtype: str
        """
        return self._catalog_item_type_id

    @catalog_item_type_id.setter
    def catalog_item_type_id(self, catalog_item_type_id):
        """Sets the catalog_item_type_id of this PostProductsProduct.

        The ID of the Catalog Item Type.  # noqa: E501

        :param catalog_item_type_id: The catalog_item_type_id of this PostProductsProduct.  # noqa: E501
        :type: str
        """

        self._catalog_item_type_id = catalog_item_type_id

    @property
    def sales_prices(self):
        """Gets the sales_prices of this PostProductsProduct.  # noqa: E501


        :return: The sales_prices of this PostProductsProduct.  # noqa: E501
        :rtype: list[PostProductsProductSalesPrices]
        """
        return self._sales_prices

    @sales_prices.setter
    def sales_prices(self, sales_prices):
        """Sets the sales_prices of this PostProductsProduct.


        :param sales_prices: The sales_prices of this PostProductsProduct.  # noqa: E501
        :type: list[PostProductsProductSalesPrices]
        """

        self._sales_prices = sales_prices

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
        if not isinstance(other, PostProductsProduct):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PostProductsProduct):
            return True

        return self.to_dict() != other.to_dict()