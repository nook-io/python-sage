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


class TaxRate(object):
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
        'name': 'str',
        'agency': 'str',
        'percentage': 'float',
        'percentages': 'list[TaxRatePercentage]',
        'is_visible': 'bool',
        'retailer': 'bool',
        'editable': 'bool',
        'deletable': 'bool',
        'is_combined_rate': 'bool',
        'component_tax_rates': 'list[ComponentTaxRate]'
    }

    attribute_map = {
        'id': 'id',
        'displayed_as': 'displayed_as',
        'path': '$path',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'name': 'name',
        'agency': 'agency',
        'percentage': 'percentage',
        'percentages': 'percentages',
        'is_visible': 'is_visible',
        'retailer': 'retailer',
        'editable': 'editable',
        'deletable': 'deletable',
        'is_combined_rate': 'is_combined_rate',
        'component_tax_rates': 'component_tax_rates'
    }

    def __init__(self, id=None, displayed_as=None, path=None, created_at=None, updated_at=None, name=None, agency=None, percentage=None, percentages=None, is_visible=None, retailer=None, editable=None, deletable=None, is_combined_rate=None, component_tax_rates=None, local_vars_configuration=None):  # noqa: E501
        """TaxRate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._displayed_as = None
        self._path = None
        self._created_at = None
        self._updated_at = None
        self._name = None
        self._agency = None
        self._percentage = None
        self._percentages = None
        self._is_visible = None
        self._retailer = None
        self._editable = None
        self._deletable = None
        self._is_combined_rate = None
        self._component_tax_rates = None
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
        if name is not None:
            self.name = name
        if agency is not None:
            self.agency = agency
        if percentage is not None:
            self.percentage = percentage
        if percentages is not None:
            self.percentages = percentages
        if is_visible is not None:
            self.is_visible = is_visible
        if retailer is not None:
            self.retailer = retailer
        if editable is not None:
            self.editable = editable
        if deletable is not None:
            self.deletable = deletable
        if is_combined_rate is not None:
            self.is_combined_rate = is_combined_rate
        if component_tax_rates is not None:
            self.component_tax_rates = component_tax_rates

    @property
    def id(self):
        """Gets the id of this TaxRate.  # noqa: E501

        The unique identifier for the item  # noqa: E501

        :return: The id of this TaxRate.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TaxRate.

        The unique identifier for the item  # noqa: E501

        :param id: The id of this TaxRate.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def displayed_as(self):
        """Gets the displayed_as of this TaxRate.  # noqa: E501

        The name of the resource  # noqa: E501

        :return: The displayed_as of this TaxRate.  # noqa: E501
        :rtype: str
        """
        return self._displayed_as

    @displayed_as.setter
    def displayed_as(self, displayed_as):
        """Sets the displayed_as of this TaxRate.

        The name of the resource  # noqa: E501

        :param displayed_as: The displayed_as of this TaxRate.  # noqa: E501
        :type: str
        """

        self._displayed_as = displayed_as

    @property
    def path(self):
        """Gets the path of this TaxRate.  # noqa: E501

        The API path for the resource  # noqa: E501

        :return: The path of this TaxRate.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this TaxRate.

        The API path for the resource  # noqa: E501

        :param path: The path of this TaxRate.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def created_at(self):
        """Gets the created_at of this TaxRate.  # noqa: E501

        The datetime when the item was created  # noqa: E501

        :return: The created_at of this TaxRate.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this TaxRate.

        The datetime when the item was created  # noqa: E501

        :param created_at: The created_at of this TaxRate.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this TaxRate.  # noqa: E501

        The datetime when the item was last updated  # noqa: E501

        :return: The updated_at of this TaxRate.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this TaxRate.

        The datetime when the item was last updated  # noqa: E501

        :param updated_at: The updated_at of this TaxRate.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def name(self):
        """Gets the name of this TaxRate.  # noqa: E501

        The name of the tax rate  # noqa: E501

        :return: The name of this TaxRate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TaxRate.

        The name of the tax rate  # noqa: E501

        :param name: The name of this TaxRate.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501

        self._name = name

    @property
    def agency(self):
        """Gets the agency of this TaxRate.  # noqa: E501

        The agency name (US Only)  # noqa: E501

        :return: The agency of this TaxRate.  # noqa: E501
        :rtype: str
        """
        return self._agency

    @agency.setter
    def agency(self, agency):
        """Sets the agency of this TaxRate.

        The agency name (US Only)  # noqa: E501

        :param agency: The agency of this TaxRate.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                agency is not None and len(agency) > 255):
            raise ValueError("Invalid value for `agency`, length must be less than or equal to `255`")  # noqa: E501

        self._agency = agency

    @property
    def percentage(self):
        """Gets the percentage of this TaxRate.  # noqa: E501

        The current tax rate percentage  # noqa: E501

        :return: The percentage of this TaxRate.  # noqa: E501
        :rtype: float
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this TaxRate.

        The current tax rate percentage  # noqa: E501

        :param percentage: The percentage of this TaxRate.  # noqa: E501
        :type: float
        """

        self._percentage = percentage

    @property
    def percentages(self):
        """Gets the percentages of this TaxRate.  # noqa: E501

        The tax rate percentage and date ranges they apply to  # noqa: E501

        :return: The percentages of this TaxRate.  # noqa: E501
        :rtype: list[TaxRatePercentage]
        """
        return self._percentages

    @percentages.setter
    def percentages(self, percentages):
        """Sets the percentages of this TaxRate.

        The tax rate percentage and date ranges they apply to  # noqa: E501

        :param percentages: The percentages of this TaxRate.  # noqa: E501
        :type: list[TaxRatePercentage]
        """

        self._percentages = percentages

    @property
    def is_visible(self):
        """Gets the is_visible of this TaxRate.  # noqa: E501

        Indicates whether the tax rate is displayed in the application  # noqa: E501

        :return: The is_visible of this TaxRate.  # noqa: E501
        :rtype: bool
        """
        return self._is_visible

    @is_visible.setter
    def is_visible(self, is_visible):
        """Sets the is_visible of this TaxRate.

        Indicates whether the tax rate is displayed in the application  # noqa: E501

        :param is_visible: The is_visible of this TaxRate.  # noqa: E501
        :type: bool
        """

        self._is_visible = is_visible

    @property
    def retailer(self):
        """Gets the retailer of this TaxRate.  # noqa: E501

        Indicates if tax rate is a retailer rate or not  # noqa: E501

        :return: The retailer of this TaxRate.  # noqa: E501
        :rtype: bool
        """
        return self._retailer

    @retailer.setter
    def retailer(self, retailer):
        """Sets the retailer of this TaxRate.

        Indicates if tax rate is a retailer rate or not  # noqa: E501

        :param retailer: The retailer of this TaxRate.  # noqa: E501
        :type: bool
        """

        self._retailer = retailer

    @property
    def editable(self):
        """Gets the editable of this TaxRate.  # noqa: E501

        Indicates whether a tax rate can be edited  # noqa: E501

        :return: The editable of this TaxRate.  # noqa: E501
        :rtype: bool
        """
        return self._editable

    @editable.setter
    def editable(self, editable):
        """Sets the editable of this TaxRate.

        Indicates whether a tax rate can be edited  # noqa: E501

        :param editable: The editable of this TaxRate.  # noqa: E501
        :type: bool
        """

        self._editable = editable

    @property
    def deletable(self):
        """Gets the deletable of this TaxRate.  # noqa: E501

        Indicates whether a tax rate can be deleted  # noqa: E501

        :return: The deletable of this TaxRate.  # noqa: E501
        :rtype: bool
        """
        return self._deletable

    @deletable.setter
    def deletable(self, deletable):
        """Sets the deletable of this TaxRate.

        Indicates whether a tax rate can be deleted  # noqa: E501

        :param deletable: The deletable of this TaxRate.  # noqa: E501
        :type: bool
        """

        self._deletable = deletable

    @property
    def is_combined_rate(self):
        """Gets the is_combined_rate of this TaxRate.  # noqa: E501

        Indicates whether the tax rate is made up of component tax rates  # noqa: E501

        :return: The is_combined_rate of this TaxRate.  # noqa: E501
        :rtype: bool
        """
        return self._is_combined_rate

    @is_combined_rate.setter
    def is_combined_rate(self, is_combined_rate):
        """Sets the is_combined_rate of this TaxRate.

        Indicates whether the tax rate is made up of component tax rates  # noqa: E501

        :param is_combined_rate: The is_combined_rate of this TaxRate.  # noqa: E501
        :type: bool
        """

        self._is_combined_rate = is_combined_rate

    @property
    def component_tax_rates(self):
        """Gets the component_tax_rates of this TaxRate.  # noqa: E501

        The component tax rates which make up a combined rate  # noqa: E501

        :return: The component_tax_rates of this TaxRate.  # noqa: E501
        :rtype: list[ComponentTaxRate]
        """
        return self._component_tax_rates

    @component_tax_rates.setter
    def component_tax_rates(self, component_tax_rates):
        """Sets the component_tax_rates of this TaxRate.

        The component tax rates which make up a combined rate  # noqa: E501

        :param component_tax_rates: The component_tax_rates of this TaxRate.  # noqa: E501
        :type: list[ComponentTaxRate]
        """

        self._component_tax_rates = component_tax_rates

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
        if not isinstance(other, TaxRate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TaxRate):
            return True

        return self.to_dict() != other.to_dict()