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


class PutBusinessSettingsBusinessSettings(object):
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
        'siret': 'str',
        'management_centre_member': 'bool',
        'rcs_number': 'str',
        'share_capital': 'float',
        'business_activity_type_id': 'str',
        'legal_form_type_id': 'str',
        'auxiliary_accounts_visible': 'bool',
        'business_type_id': 'str',
        'country_of_registration_id': 'str',
        'default_ledger_accounts': 'PutBusinessSettingsBusinessSettingsDefaultLedgerAccounts'
    }

    attribute_map = {
        'siret': 'siret',
        'management_centre_member': 'management_centre_member',
        'rcs_number': 'rcs_number',
        'share_capital': 'share_capital',
        'business_activity_type_id': 'business_activity_type_id',
        'legal_form_type_id': 'legal_form_type_id',
        'auxiliary_accounts_visible': 'auxiliary_accounts_visible',
        'business_type_id': 'business_type_id',
        'country_of_registration_id': 'country_of_registration_id',
        'default_ledger_accounts': 'default_ledger_accounts'
    }

    def __init__(self, siret=None, management_centre_member=None, rcs_number=None, share_capital=None, business_activity_type_id=None, legal_form_type_id=None, auxiliary_accounts_visible=None, business_type_id=None, country_of_registration_id=None, default_ledger_accounts=None, local_vars_configuration=None):  # noqa: E501
        """PutBusinessSettingsBusinessSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._siret = None
        self._management_centre_member = None
        self._rcs_number = None
        self._share_capital = None
        self._business_activity_type_id = None
        self._legal_form_type_id = None
        self._auxiliary_accounts_visible = None
        self._business_type_id = None
        self._country_of_registration_id = None
        self._default_ledger_accounts = None
        self.discriminator = None

        if siret is not None:
            self.siret = siret
        if management_centre_member is not None:
            self.management_centre_member = management_centre_member
        if rcs_number is not None:
            self.rcs_number = rcs_number
        if share_capital is not None:
            self.share_capital = share_capital
        if business_activity_type_id is not None:
            self.business_activity_type_id = business_activity_type_id
        if legal_form_type_id is not None:
            self.legal_form_type_id = legal_form_type_id
        if auxiliary_accounts_visible is not None:
            self.auxiliary_accounts_visible = auxiliary_accounts_visible
        if business_type_id is not None:
            self.business_type_id = business_type_id
        if country_of_registration_id is not None:
            self.country_of_registration_id = country_of_registration_id
        if default_ledger_accounts is not None:
            self.default_ledger_accounts = default_ledger_accounts

    @property
    def siret(self):
        """Gets the siret of this PutBusinessSettingsBusinessSettings.  # noqa: E501

        SIRET Number (France only)  # noqa: E501

        :return: The siret of this PutBusinessSettingsBusinessSettings.  # noqa: E501
        :rtype: str
        """
        return self._siret

    @siret.setter
    def siret(self, siret):
        """Sets the siret of this PutBusinessSettingsBusinessSettings.

        SIRET Number (France only)  # noqa: E501

        :param siret: The siret of this PutBusinessSettingsBusinessSettings.  # noqa: E501
        :type: str
        """

        self._siret = siret

    @property
    def management_centre_member(self):
        """Gets the management_centre_member of this PutBusinessSettingsBusinessSettings.  # noqa: E501

        Member of Approved Management Centres (France only)  # noqa: E501

        :return: The management_centre_member of this PutBusinessSettingsBusinessSettings.  # noqa: E501
        :rtype: bool
        """
        return self._management_centre_member

    @management_centre_member.setter
    def management_centre_member(self, management_centre_member):
        """Sets the management_centre_member of this PutBusinessSettingsBusinessSettings.

        Member of Approved Management Centres (France only)  # noqa: E501

        :param management_centre_member: The management_centre_member of this PutBusinessSettingsBusinessSettings.  # noqa: E501
        :type: bool
        """

        self._management_centre_member = management_centre_member

    @property
    def rcs_number(self):
        """Gets the rcs_number of this PutBusinessSettingsBusinessSettings.  # noqa: E501

        RCS Number (France only)  # noqa: E501

        :return: The rcs_number of this PutBusinessSettingsBusinessSettings.  # noqa: E501
        :rtype: str
        """
        return self._rcs_number

    @rcs_number.setter
    def rcs_number(self, rcs_number):
        """Sets the rcs_number of this PutBusinessSettingsBusinessSettings.

        RCS Number (France only)  # noqa: E501

        :param rcs_number: The rcs_number of this PutBusinessSettingsBusinessSettings.  # noqa: E501
        :type: str
        """

        self._rcs_number = rcs_number

    @property
    def share_capital(self):
        """Gets the share_capital of this PutBusinessSettingsBusinessSettings.  # noqa: E501

        Share Capital (France only)  # noqa: E501

        :return: The share_capital of this PutBusinessSettingsBusinessSettings.  # noqa: E501
        :rtype: float
        """
        return self._share_capital

    @share_capital.setter
    def share_capital(self, share_capital):
        """Sets the share_capital of this PutBusinessSettingsBusinessSettings.

        Share Capital (France only)  # noqa: E501

        :param share_capital: The share_capital of this PutBusinessSettingsBusinessSettings.  # noqa: E501
        :type: float
        """

        self._share_capital = share_capital

    @property
    def business_activity_type_id(self):
        """Gets the business_activity_type_id of this PutBusinessSettingsBusinessSettings.  # noqa: E501

        The ID of the Business Activity Type.  # noqa: E501

        :return: The business_activity_type_id of this PutBusinessSettingsBusinessSettings.  # noqa: E501
        :rtype: str
        """
        return self._business_activity_type_id

    @business_activity_type_id.setter
    def business_activity_type_id(self, business_activity_type_id):
        """Sets the business_activity_type_id of this PutBusinessSettingsBusinessSettings.

        The ID of the Business Activity Type.  # noqa: E501

        :param business_activity_type_id: The business_activity_type_id of this PutBusinessSettingsBusinessSettings.  # noqa: E501
        :type: str
        """

        self._business_activity_type_id = business_activity_type_id

    @property
    def legal_form_type_id(self):
        """Gets the legal_form_type_id of this PutBusinessSettingsBusinessSettings.  # noqa: E501

        The ID of the Legal Form Type.  # noqa: E501

        :return: The legal_form_type_id of this PutBusinessSettingsBusinessSettings.  # noqa: E501
        :rtype: str
        """
        return self._legal_form_type_id

    @legal_form_type_id.setter
    def legal_form_type_id(self, legal_form_type_id):
        """Sets the legal_form_type_id of this PutBusinessSettingsBusinessSettings.

        The ID of the Legal Form Type.  # noqa: E501

        :param legal_form_type_id: The legal_form_type_id of this PutBusinessSettingsBusinessSettings.  # noqa: E501
        :type: str
        """

        self._legal_form_type_id = legal_form_type_id

    @property
    def auxiliary_accounts_visible(self):
        """Gets the auxiliary_accounts_visible of this PutBusinessSettingsBusinessSettings.  # noqa: E501

        Auxiliary Accounts Visible (France & Spain only)  # noqa: E501

        :return: The auxiliary_accounts_visible of this PutBusinessSettingsBusinessSettings.  # noqa: E501
        :rtype: bool
        """
        return self._auxiliary_accounts_visible

    @auxiliary_accounts_visible.setter
    def auxiliary_accounts_visible(self, auxiliary_accounts_visible):
        """Sets the auxiliary_accounts_visible of this PutBusinessSettingsBusinessSettings.

        Auxiliary Accounts Visible (France & Spain only)  # noqa: E501

        :param auxiliary_accounts_visible: The auxiliary_accounts_visible of this PutBusinessSettingsBusinessSettings.  # noqa: E501
        :type: bool
        """

        self._auxiliary_accounts_visible = auxiliary_accounts_visible

    @property
    def business_type_id(self):
        """Gets the business_type_id of this PutBusinessSettingsBusinessSettings.  # noqa: E501

        The ID of the Business Type.  # noqa: E501

        :return: The business_type_id of this PutBusinessSettingsBusinessSettings.  # noqa: E501
        :rtype: str
        """
        return self._business_type_id

    @business_type_id.setter
    def business_type_id(self, business_type_id):
        """Sets the business_type_id of this PutBusinessSettingsBusinessSettings.

        The ID of the Business Type.  # noqa: E501

        :param business_type_id: The business_type_id of this PutBusinessSettingsBusinessSettings.  # noqa: E501
        :type: str
        """

        self._business_type_id = business_type_id

    @property
    def country_of_registration_id(self):
        """Gets the country_of_registration_id of this PutBusinessSettingsBusinessSettings.  # noqa: E501

        The ID of the Country Of Registration.  # noqa: E501

        :return: The country_of_registration_id of this PutBusinessSettingsBusinessSettings.  # noqa: E501
        :rtype: str
        """
        return self._country_of_registration_id

    @country_of_registration_id.setter
    def country_of_registration_id(self, country_of_registration_id):
        """Sets the country_of_registration_id of this PutBusinessSettingsBusinessSettings.

        The ID of the Country Of Registration.  # noqa: E501

        :param country_of_registration_id: The country_of_registration_id of this PutBusinessSettingsBusinessSettings.  # noqa: E501
        :type: str
        """

        self._country_of_registration_id = country_of_registration_id

    @property
    def default_ledger_accounts(self):
        """Gets the default_ledger_accounts of this PutBusinessSettingsBusinessSettings.  # noqa: E501


        :return: The default_ledger_accounts of this PutBusinessSettingsBusinessSettings.  # noqa: E501
        :rtype: PutBusinessSettingsBusinessSettingsDefaultLedgerAccounts
        """
        return self._default_ledger_accounts

    @default_ledger_accounts.setter
    def default_ledger_accounts(self, default_ledger_accounts):
        """Sets the default_ledger_accounts of this PutBusinessSettingsBusinessSettings.


        :param default_ledger_accounts: The default_ledger_accounts of this PutBusinessSettingsBusinessSettings.  # noqa: E501
        :type: PutBusinessSettingsBusinessSettingsDefaultLedgerAccounts
        """

        self._default_ledger_accounts = default_ledger_accounts

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
        if not isinstance(other, PutBusinessSettingsBusinessSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PutBusinessSettingsBusinessSettings):
            return True

        return self.to_dict() != other.to_dict()
