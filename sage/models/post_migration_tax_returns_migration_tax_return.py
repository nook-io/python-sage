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


class PostMigrationTaxReturnsMigrationTaxReturn(object):
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
        'from_date': 'date',
        'to_date': 'date',
        'total_amount': 'float',
        'tax_return_frequency_id': 'str',
        'gb': 'PostMigrationTaxReturnsMigrationTaxReturnGb',
        'ie': 'PostMigrationTaxReturnsMigrationTaxReturnIe'
    }

    attribute_map = {
        'from_date': 'from_date',
        'to_date': 'to_date',
        'total_amount': 'total_amount',
        'tax_return_frequency_id': 'tax_return_frequency_id',
        'gb': 'gb',
        'ie': 'ie'
    }

    def __init__(self, from_date=None, to_date=None, total_amount=None, tax_return_frequency_id=None, gb=None, ie=None, local_vars_configuration=None):  # noqa: E501
        """PostMigrationTaxReturnsMigrationTaxReturn - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._from_date = None
        self._to_date = None
        self._total_amount = None
        self._tax_return_frequency_id = None
        self._gb = None
        self._ie = None
        self.discriminator = None

        self.from_date = from_date
        self.to_date = to_date
        self.total_amount = total_amount
        self.tax_return_frequency_id = tax_return_frequency_id
        if gb is not None:
            self.gb = gb
        if ie is not None:
            self.ie = ie

    @property
    def from_date(self):
        """Gets the from_date of this PostMigrationTaxReturnsMigrationTaxReturn.  # noqa: E501

        The start date of the tax return  # noqa: E501

        :return: The from_date of this PostMigrationTaxReturnsMigrationTaxReturn.  # noqa: E501
        :rtype: date
        """
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        """Sets the from_date of this PostMigrationTaxReturnsMigrationTaxReturn.

        The start date of the tax return  # noqa: E501

        :param from_date: The from_date of this PostMigrationTaxReturnsMigrationTaxReturn.  # noqa: E501
        :type: date
        """
        if self.local_vars_configuration.client_side_validation and from_date is None:  # noqa: E501
            raise ValueError("Invalid value for `from_date`, must not be `None`")  # noqa: E501

        self._from_date = from_date

    @property
    def to_date(self):
        """Gets the to_date of this PostMigrationTaxReturnsMigrationTaxReturn.  # noqa: E501

        The end date of the tax return  # noqa: E501

        :return: The to_date of this PostMigrationTaxReturnsMigrationTaxReturn.  # noqa: E501
        :rtype: date
        """
        return self._to_date

    @to_date.setter
    def to_date(self, to_date):
        """Sets the to_date of this PostMigrationTaxReturnsMigrationTaxReturn.

        The end date of the tax return  # noqa: E501

        :param to_date: The to_date of this PostMigrationTaxReturnsMigrationTaxReturn.  # noqa: E501
        :type: date
        """
        if self.local_vars_configuration.client_side_validation and to_date is None:  # noqa: E501
            raise ValueError("Invalid value for `to_date`, must not be `None`")  # noqa: E501

        self._to_date = to_date

    @property
    def total_amount(self):
        """Gets the total_amount of this PostMigrationTaxReturnsMigrationTaxReturn.  # noqa: E501

        The total of the tax return  # noqa: E501

        :return: The total_amount of this PostMigrationTaxReturnsMigrationTaxReturn.  # noqa: E501
        :rtype: float
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """Sets the total_amount of this PostMigrationTaxReturnsMigrationTaxReturn.

        The total of the tax return  # noqa: E501

        :param total_amount: The total_amount of this PostMigrationTaxReturnsMigrationTaxReturn.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and total_amount is None:  # noqa: E501
            raise ValueError("Invalid value for `total_amount`, must not be `None`")  # noqa: E501

        self._total_amount = total_amount

    @property
    def tax_return_frequency_id(self):
        """Gets the tax_return_frequency_id of this PostMigrationTaxReturnsMigrationTaxReturn.  # noqa: E501

        The tax return submission frequency  # noqa: E501

        :return: The tax_return_frequency_id of this PostMigrationTaxReturnsMigrationTaxReturn.  # noqa: E501
        :rtype: str
        """
        return self._tax_return_frequency_id

    @tax_return_frequency_id.setter
    def tax_return_frequency_id(self, tax_return_frequency_id):
        """Sets the tax_return_frequency_id of this PostMigrationTaxReturnsMigrationTaxReturn.

        The tax return submission frequency  # noqa: E501

        :param tax_return_frequency_id: The tax_return_frequency_id of this PostMigrationTaxReturnsMigrationTaxReturn.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and tax_return_frequency_id is None:  # noqa: E501
            raise ValueError("Invalid value for `tax_return_frequency_id`, must not be `None`")  # noqa: E501

        self._tax_return_frequency_id = tax_return_frequency_id

    @property
    def gb(self):
        """Gets the gb of this PostMigrationTaxReturnsMigrationTaxReturn.  # noqa: E501


        :return: The gb of this PostMigrationTaxReturnsMigrationTaxReturn.  # noqa: E501
        :rtype: PostMigrationTaxReturnsMigrationTaxReturnGb
        """
        return self._gb

    @gb.setter
    def gb(self, gb):
        """Sets the gb of this PostMigrationTaxReturnsMigrationTaxReturn.


        :param gb: The gb of this PostMigrationTaxReturnsMigrationTaxReturn.  # noqa: E501
        :type: PostMigrationTaxReturnsMigrationTaxReturnGb
        """

        self._gb = gb

    @property
    def ie(self):
        """Gets the ie of this PostMigrationTaxReturnsMigrationTaxReturn.  # noqa: E501


        :return: The ie of this PostMigrationTaxReturnsMigrationTaxReturn.  # noqa: E501
        :rtype: PostMigrationTaxReturnsMigrationTaxReturnIe
        """
        return self._ie

    @ie.setter
    def ie(self, ie):
        """Sets the ie of this PostMigrationTaxReturnsMigrationTaxReturn.


        :param ie: The ie of this PostMigrationTaxReturnsMigrationTaxReturn.  # noqa: E501
        :type: PostMigrationTaxReturnsMigrationTaxReturnIe
        """

        self._ie = ie

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
        if not isinstance(other, PostMigrationTaxReturnsMigrationTaxReturn):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PostMigrationTaxReturnsMigrationTaxReturn):
            return True

        return self.to_dict() != other.to_dict()
