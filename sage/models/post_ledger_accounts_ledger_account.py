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


class PostLedgerAccountsLedgerAccount(object):
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
        'ledger_account_type_id': 'str',
        'included_in_chart': 'bool',
        'name': 'str',
        'display_name': 'str',
        'nominal_code': 'int',
        'ledger_account_classification_id': 'str',
        'tax_rate_id': 'str',
        'fixed_tax_rate': 'bool',
        'visible_in_banking': 'bool',
        'visible_in_expenses': 'bool',
        'visible_in_journals': 'bool',
        'visible_in_other_payments': 'bool',
        'visible_in_other_receipts': 'bool',
        'visible_in_reporting': 'bool',
        'visible_in_sales': 'bool',
        'control_name': 'str',
        'tax_recoverable': 'bool',
        'recoverable_percentage': 'float',
        'non_recoverable_ledger_account_id': 'str',
        'cis_materials': 'bool',
        'cis_labour': 'bool',
        'gifi_code': 'int'
    }

    attribute_map = {
        'ledger_account_type_id': 'ledger_account_type_id',
        'included_in_chart': 'included_in_chart',
        'name': 'name',
        'display_name': 'display_name',
        'nominal_code': 'nominal_code',
        'ledger_account_classification_id': 'ledger_account_classification_id',
        'tax_rate_id': 'tax_rate_id',
        'fixed_tax_rate': 'fixed_tax_rate',
        'visible_in_banking': 'visible_in_banking',
        'visible_in_expenses': 'visible_in_expenses',
        'visible_in_journals': 'visible_in_journals',
        'visible_in_other_payments': 'visible_in_other_payments',
        'visible_in_other_receipts': 'visible_in_other_receipts',
        'visible_in_reporting': 'visible_in_reporting',
        'visible_in_sales': 'visible_in_sales',
        'control_name': 'control_name',
        'tax_recoverable': 'tax_recoverable',
        'recoverable_percentage': 'recoverable_percentage',
        'non_recoverable_ledger_account_id': 'non_recoverable_ledger_account_id',
        'cis_materials': 'cis_materials',
        'cis_labour': 'cis_labour',
        'gifi_code': 'gifi_code'
    }

    def __init__(self, ledger_account_type_id=None, included_in_chart=None, name=None, display_name=None, nominal_code=None, ledger_account_classification_id=None, tax_rate_id=None, fixed_tax_rate=None, visible_in_banking=None, visible_in_expenses=None, visible_in_journals=None, visible_in_other_payments=None, visible_in_other_receipts=None, visible_in_reporting=None, visible_in_sales=None, control_name=None, tax_recoverable=None, recoverable_percentage=None, non_recoverable_ledger_account_id=None, cis_materials=None, cis_labour=None, gifi_code=None, local_vars_configuration=None):  # noqa: E501
        """PostLedgerAccountsLedgerAccount - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ledger_account_type_id = None
        self._included_in_chart = None
        self._name = None
        self._display_name = None
        self._nominal_code = None
        self._ledger_account_classification_id = None
        self._tax_rate_id = None
        self._fixed_tax_rate = None
        self._visible_in_banking = None
        self._visible_in_expenses = None
        self._visible_in_journals = None
        self._visible_in_other_payments = None
        self._visible_in_other_receipts = None
        self._visible_in_reporting = None
        self._visible_in_sales = None
        self._control_name = None
        self._tax_recoverable = None
        self._recoverable_percentage = None
        self._non_recoverable_ledger_account_id = None
        self._cis_materials = None
        self._cis_labour = None
        self._gifi_code = None
        self.discriminator = None

        self.ledger_account_type_id = ledger_account_type_id
        self.included_in_chart = included_in_chart
        self.name = name
        self.display_name = display_name
        self.nominal_code = nominal_code
        if ledger_account_classification_id is not None:
            self.ledger_account_classification_id = ledger_account_classification_id
        if tax_rate_id is not None:
            self.tax_rate_id = tax_rate_id
        if fixed_tax_rate is not None:
            self.fixed_tax_rate = fixed_tax_rate
        if visible_in_banking is not None:
            self.visible_in_banking = visible_in_banking
        if visible_in_expenses is not None:
            self.visible_in_expenses = visible_in_expenses
        if visible_in_journals is not None:
            self.visible_in_journals = visible_in_journals
        if visible_in_other_payments is not None:
            self.visible_in_other_payments = visible_in_other_payments
        if visible_in_other_receipts is not None:
            self.visible_in_other_receipts = visible_in_other_receipts
        if visible_in_reporting is not None:
            self.visible_in_reporting = visible_in_reporting
        if visible_in_sales is not None:
            self.visible_in_sales = visible_in_sales
        if control_name is not None:
            self.control_name = control_name
        if tax_recoverable is not None:
            self.tax_recoverable = tax_recoverable
        if recoverable_percentage is not None:
            self.recoverable_percentage = recoverable_percentage
        if non_recoverable_ledger_account_id is not None:
            self.non_recoverable_ledger_account_id = non_recoverable_ledger_account_id
        if cis_materials is not None:
            self.cis_materials = cis_materials
        if cis_labour is not None:
            self.cis_labour = cis_labour
        if gifi_code is not None:
            self.gifi_code = gifi_code

    @property
    def ledger_account_type_id(self):
        """Gets the ledger_account_type_id of this PostLedgerAccountsLedgerAccount.  # noqa: E501

        The ledger account type for the ledger account  # noqa: E501

        :return: The ledger_account_type_id of this PostLedgerAccountsLedgerAccount.  # noqa: E501
        :rtype: str
        """
        return self._ledger_account_type_id

    @ledger_account_type_id.setter
    def ledger_account_type_id(self, ledger_account_type_id):
        """Sets the ledger_account_type_id of this PostLedgerAccountsLedgerAccount.

        The ledger account type for the ledger account  # noqa: E501

        :param ledger_account_type_id: The ledger_account_type_id of this PostLedgerAccountsLedgerAccount.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and ledger_account_type_id is None:  # noqa: E501
            raise ValueError("Invalid value for `ledger_account_type_id`, must not be `None`")  # noqa: E501

        self._ledger_account_type_id = ledger_account_type_id

    @property
    def included_in_chart(self):
        """Gets the included_in_chart of this PostLedgerAccountsLedgerAccount.  # noqa: E501

        Indicates whether the ledger account is included in the chart of accounts  # noqa: E501

        :return: The included_in_chart of this PostLedgerAccountsLedgerAccount.  # noqa: E501
        :rtype: bool
        """
        return self._included_in_chart

    @included_in_chart.setter
    def included_in_chart(self, included_in_chart):
        """Sets the included_in_chart of this PostLedgerAccountsLedgerAccount.

        Indicates whether the ledger account is included in the chart of accounts  # noqa: E501

        :param included_in_chart: The included_in_chart of this PostLedgerAccountsLedgerAccount.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and included_in_chart is None:  # noqa: E501
            raise ValueError("Invalid value for `included_in_chart`, must not be `None`")  # noqa: E501

        self._included_in_chart = included_in_chart

    @property
    def name(self):
        """Gets the name of this PostLedgerAccountsLedgerAccount.  # noqa: E501

        The name for the ledger account.  Changes to this field do not propagate to other resources, namely not to the name of the associated bank_account (unlike the behaviour of the UI).   # noqa: E501

        :return: The name of this PostLedgerAccountsLedgerAccount.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PostLedgerAccountsLedgerAccount.

        The name for the ledger account.  Changes to this field do not propagate to other resources, namely not to the name of the associated bank_account (unlike the behaviour of the UI).   # noqa: E501

        :param name: The name of this PostLedgerAccountsLedgerAccount.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def display_name(self):
        """Gets the display_name of this PostLedgerAccountsLedgerAccount.  # noqa: E501

        The display name for the ledger account  # noqa: E501

        :return: The display_name of this PostLedgerAccountsLedgerAccount.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this PostLedgerAccountsLedgerAccount.

        The display name for the ledger account  # noqa: E501

        :param display_name: The display_name of this PostLedgerAccountsLedgerAccount.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def nominal_code(self):
        """Gets the nominal_code of this PostLedgerAccountsLedgerAccount.  # noqa: E501

        The nominal code of the ledger account  # noqa: E501

        :return: The nominal_code of this PostLedgerAccountsLedgerAccount.  # noqa: E501
        :rtype: int
        """
        return self._nominal_code

    @nominal_code.setter
    def nominal_code(self, nominal_code):
        """Sets the nominal_code of this PostLedgerAccountsLedgerAccount.

        The nominal code of the ledger account  # noqa: E501

        :param nominal_code: The nominal_code of this PostLedgerAccountsLedgerAccount.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and nominal_code is None:  # noqa: E501
            raise ValueError("Invalid value for `nominal_code`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                nominal_code is not None and nominal_code > 99999999):  # noqa: E501
            raise ValueError("Invalid value for `nominal_code`, must be a value less than or equal to `99999999`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                nominal_code is not None and nominal_code < 1):  # noqa: E501
            raise ValueError("Invalid value for `nominal_code`, must be a value greater than or equal to `1`")  # noqa: E501

        self._nominal_code = nominal_code

    @property
    def ledger_account_classification_id(self):
        """Gets the ledger_account_classification_id of this PostLedgerAccountsLedgerAccount.  # noqa: E501

        The ID of the Ledger Account Classification.  # noqa: E501

        :return: The ledger_account_classification_id of this PostLedgerAccountsLedgerAccount.  # noqa: E501
        :rtype: str
        """
        return self._ledger_account_classification_id

    @ledger_account_classification_id.setter
    def ledger_account_classification_id(self, ledger_account_classification_id):
        """Sets the ledger_account_classification_id of this PostLedgerAccountsLedgerAccount.

        The ID of the Ledger Account Classification.  # noqa: E501

        :param ledger_account_classification_id: The ledger_account_classification_id of this PostLedgerAccountsLedgerAccount.  # noqa: E501
        :type: str
        """

        self._ledger_account_classification_id = ledger_account_classification_id

    @property
    def tax_rate_id(self):
        """Gets the tax_rate_id of this PostLedgerAccountsLedgerAccount.  # noqa: E501

        The ID of the Tax Rate.  # noqa: E501

        :return: The tax_rate_id of this PostLedgerAccountsLedgerAccount.  # noqa: E501
        :rtype: str
        """
        return self._tax_rate_id

    @tax_rate_id.setter
    def tax_rate_id(self, tax_rate_id):
        """Sets the tax_rate_id of this PostLedgerAccountsLedgerAccount.

        The ID of the Tax Rate.  # noqa: E501

        :param tax_rate_id: The tax_rate_id of this PostLedgerAccountsLedgerAccount.  # noqa: E501
        :type: str
        """

        self._tax_rate_id = tax_rate_id

    @property
    def fixed_tax_rate(self):
        """Gets the fixed_tax_rate of this PostLedgerAccountsLedgerAccount.  # noqa: E501

        Indicates whether the default tax rate is fixed or may be changed per transaction  # noqa: E501

        :return: The fixed_tax_rate of this PostLedgerAccountsLedgerAccount.  # noqa: E501
        :rtype: bool
        """
        return self._fixed_tax_rate

    @fixed_tax_rate.setter
    def fixed_tax_rate(self, fixed_tax_rate):
        """Sets the fixed_tax_rate of this PostLedgerAccountsLedgerAccount.

        Indicates whether the default tax rate is fixed or may be changed per transaction  # noqa: E501

        :param fixed_tax_rate: The fixed_tax_rate of this PostLedgerAccountsLedgerAccount.  # noqa: E501
        :type: bool
        """

        self._fixed_tax_rate = fixed_tax_rate

    @property
    def visible_in_banking(self):
        """Gets the visible_in_banking of this PostLedgerAccountsLedgerAccount.  # noqa: E501

        Indicates whether the ledger account is displayed in the banking area of the application  # noqa: E501

        :return: The visible_in_banking of this PostLedgerAccountsLedgerAccount.  # noqa: E501
        :rtype: bool
        """
        return self._visible_in_banking

    @visible_in_banking.setter
    def visible_in_banking(self, visible_in_banking):
        """Sets the visible_in_banking of this PostLedgerAccountsLedgerAccount.

        Indicates whether the ledger account is displayed in the banking area of the application  # noqa: E501

        :param visible_in_banking: The visible_in_banking of this PostLedgerAccountsLedgerAccount.  # noqa: E501
        :type: bool
        """

        self._visible_in_banking = visible_in_banking

    @property
    def visible_in_expenses(self):
        """Gets the visible_in_expenses of this PostLedgerAccountsLedgerAccount.  # noqa: E501

        Indicates whether the ledger account is displayed in the purchases area of the application  # noqa: E501

        :return: The visible_in_expenses of this PostLedgerAccountsLedgerAccount.  # noqa: E501
        :rtype: bool
        """
        return self._visible_in_expenses

    @visible_in_expenses.setter
    def visible_in_expenses(self, visible_in_expenses):
        """Sets the visible_in_expenses of this PostLedgerAccountsLedgerAccount.

        Indicates whether the ledger account is displayed in the purchases area of the application  # noqa: E501

        :param visible_in_expenses: The visible_in_expenses of this PostLedgerAccountsLedgerAccount.  # noqa: E501
        :type: bool
        """

        self._visible_in_expenses = visible_in_expenses

    @property
    def visible_in_journals(self):
        """Gets the visible_in_journals of this PostLedgerAccountsLedgerAccount.  # noqa: E501

        Indicates whether the ledger account is displayed in the journals area of the application  # noqa: E501

        :return: The visible_in_journals of this PostLedgerAccountsLedgerAccount.  # noqa: E501
        :rtype: bool
        """
        return self._visible_in_journals

    @visible_in_journals.setter
    def visible_in_journals(self, visible_in_journals):
        """Sets the visible_in_journals of this PostLedgerAccountsLedgerAccount.

        Indicates whether the ledger account is displayed in the journals area of the application  # noqa: E501

        :param visible_in_journals: The visible_in_journals of this PostLedgerAccountsLedgerAccount.  # noqa: E501
        :type: bool
        """

        self._visible_in_journals = visible_in_journals

    @property
    def visible_in_other_payments(self):
        """Gets the visible_in_other_payments of this PostLedgerAccountsLedgerAccount.  # noqa: E501

        Indicates whether the ledger account is displayed in the other payments area of the application   # noqa: E501

        :return: The visible_in_other_payments of this PostLedgerAccountsLedgerAccount.  # noqa: E501
        :rtype: bool
        """
        return self._visible_in_other_payments

    @visible_in_other_payments.setter
    def visible_in_other_payments(self, visible_in_other_payments):
        """Sets the visible_in_other_payments of this PostLedgerAccountsLedgerAccount.

        Indicates whether the ledger account is displayed in the other payments area of the application   # noqa: E501

        :param visible_in_other_payments: The visible_in_other_payments of this PostLedgerAccountsLedgerAccount.  # noqa: E501
        :type: bool
        """

        self._visible_in_other_payments = visible_in_other_payments

    @property
    def visible_in_other_receipts(self):
        """Gets the visible_in_other_receipts of this PostLedgerAccountsLedgerAccount.  # noqa: E501

        Indicates whether the ledger account is displayed in the other receipts area of the application   # noqa: E501

        :return: The visible_in_other_receipts of this PostLedgerAccountsLedgerAccount.  # noqa: E501
        :rtype: bool
        """
        return self._visible_in_other_receipts

    @visible_in_other_receipts.setter
    def visible_in_other_receipts(self, visible_in_other_receipts):
        """Sets the visible_in_other_receipts of this PostLedgerAccountsLedgerAccount.

        Indicates whether the ledger account is displayed in the other receipts area of the application   # noqa: E501

        :param visible_in_other_receipts: The visible_in_other_receipts of this PostLedgerAccountsLedgerAccount.  # noqa: E501
        :type: bool
        """

        self._visible_in_other_receipts = visible_in_other_receipts

    @property
    def visible_in_reporting(self):
        """Gets the visible_in_reporting of this PostLedgerAccountsLedgerAccount.  # noqa: E501

        Indicates whether the ledger account is displayed in the reporting area of the application  # noqa: E501

        :return: The visible_in_reporting of this PostLedgerAccountsLedgerAccount.  # noqa: E501
        :rtype: bool
        """
        return self._visible_in_reporting

    @visible_in_reporting.setter
    def visible_in_reporting(self, visible_in_reporting):
        """Sets the visible_in_reporting of this PostLedgerAccountsLedgerAccount.

        Indicates whether the ledger account is displayed in the reporting area of the application  # noqa: E501

        :param visible_in_reporting: The visible_in_reporting of this PostLedgerAccountsLedgerAccount.  # noqa: E501
        :type: bool
        """

        self._visible_in_reporting = visible_in_reporting

    @property
    def visible_in_sales(self):
        """Gets the visible_in_sales of this PostLedgerAccountsLedgerAccount.  # noqa: E501

        Indicates whether the ledger account is displayed in the sales area of the application  # noqa: E501

        :return: The visible_in_sales of this PostLedgerAccountsLedgerAccount.  # noqa: E501
        :rtype: bool
        """
        return self._visible_in_sales

    @visible_in_sales.setter
    def visible_in_sales(self, visible_in_sales):
        """Sets the visible_in_sales of this PostLedgerAccountsLedgerAccount.

        Indicates whether the ledger account is displayed in the sales area of the application  # noqa: E501

        :param visible_in_sales: The visible_in_sales of this PostLedgerAccountsLedgerAccount.  # noqa: E501
        :type: bool
        """

        self._visible_in_sales = visible_in_sales

    @property
    def control_name(self):
        """Gets the control_name of this PostLedgerAccountsLedgerAccount.  # noqa: E501

        The control name for the ledger account.  This is used internally by Accounting to identify the correct ledger account for booking taxes etc. You cannot add ledger accounts with control name and you cannot modify the control name of existing ledger accounts.   # noqa: E501

        :return: The control_name of this PostLedgerAccountsLedgerAccount.  # noqa: E501
        :rtype: str
        """
        return self._control_name

    @control_name.setter
    def control_name(self, control_name):
        """Sets the control_name of this PostLedgerAccountsLedgerAccount.

        The control name for the ledger account.  This is used internally by Accounting to identify the correct ledger account for booking taxes etc. You cannot add ledger accounts with control name and you cannot modify the control name of existing ledger accounts.   # noqa: E501

        :param control_name: The control_name of this PostLedgerAccountsLedgerAccount.  # noqa: E501
        :type: str
        """

        self._control_name = control_name

    @property
    def tax_recoverable(self):
        """Gets the tax_recoverable of this PostLedgerAccountsLedgerAccount.  # noqa: E501

        Indicates that transactions posted to this ledger account have part recoverable taxes (Canada only)   # noqa: E501

        :return: The tax_recoverable of this PostLedgerAccountsLedgerAccount.  # noqa: E501
        :rtype: bool
        """
        return self._tax_recoverable

    @tax_recoverable.setter
    def tax_recoverable(self, tax_recoverable):
        """Sets the tax_recoverable of this PostLedgerAccountsLedgerAccount.

        Indicates that transactions posted to this ledger account have part recoverable taxes (Canada only)   # noqa: E501

        :param tax_recoverable: The tax_recoverable of this PostLedgerAccountsLedgerAccount.  # noqa: E501
        :type: bool
        """

        self._tax_recoverable = tax_recoverable

    @property
    def recoverable_percentage(self):
        """Gets the recoverable_percentage of this PostLedgerAccountsLedgerAccount.  # noqa: E501

        The partial recoverable tax rate (Canada only)  # noqa: E501

        :return: The recoverable_percentage of this PostLedgerAccountsLedgerAccount.  # noqa: E501
        :rtype: float
        """
        return self._recoverable_percentage

    @recoverable_percentage.setter
    def recoverable_percentage(self, recoverable_percentage):
        """Sets the recoverable_percentage of this PostLedgerAccountsLedgerAccount.

        The partial recoverable tax rate (Canada only)  # noqa: E501

        :param recoverable_percentage: The recoverable_percentage of this PostLedgerAccountsLedgerAccount.  # noqa: E501
        :type: float
        """

        self._recoverable_percentage = recoverable_percentage

    @property
    def non_recoverable_ledger_account_id(self):
        """Gets the non_recoverable_ledger_account_id of this PostLedgerAccountsLedgerAccount.  # noqa: E501

        The ID of the Non Recoverable Ledger Account.  # noqa: E501

        :return: The non_recoverable_ledger_account_id of this PostLedgerAccountsLedgerAccount.  # noqa: E501
        :rtype: str
        """
        return self._non_recoverable_ledger_account_id

    @non_recoverable_ledger_account_id.setter
    def non_recoverable_ledger_account_id(self, non_recoverable_ledger_account_id):
        """Sets the non_recoverable_ledger_account_id of this PostLedgerAccountsLedgerAccount.

        The ID of the Non Recoverable Ledger Account.  # noqa: E501

        :param non_recoverable_ledger_account_id: The non_recoverable_ledger_account_id of this PostLedgerAccountsLedgerAccount.  # noqa: E501
        :type: str
        """

        self._non_recoverable_ledger_account_id = non_recoverable_ledger_account_id

    @property
    def cis_materials(self):
        """Gets the cis_materials of this PostLedgerAccountsLedgerAccount.  # noqa: E501

        Indicates whether the ledger account is flagged for CIS Materials  # noqa: E501

        :return: The cis_materials of this PostLedgerAccountsLedgerAccount.  # noqa: E501
        :rtype: bool
        """
        return self._cis_materials

    @cis_materials.setter
    def cis_materials(self, cis_materials):
        """Sets the cis_materials of this PostLedgerAccountsLedgerAccount.

        Indicates whether the ledger account is flagged for CIS Materials  # noqa: E501

        :param cis_materials: The cis_materials of this PostLedgerAccountsLedgerAccount.  # noqa: E501
        :type: bool
        """

        self._cis_materials = cis_materials

    @property
    def cis_labour(self):
        """Gets the cis_labour of this PostLedgerAccountsLedgerAccount.  # noqa: E501

        Indicates whether the ledger account is flagged for CIS Labour  # noqa: E501

        :return: The cis_labour of this PostLedgerAccountsLedgerAccount.  # noqa: E501
        :rtype: bool
        """
        return self._cis_labour

    @cis_labour.setter
    def cis_labour(self, cis_labour):
        """Sets the cis_labour of this PostLedgerAccountsLedgerAccount.

        Indicates whether the ledger account is flagged for CIS Labour  # noqa: E501

        :param cis_labour: The cis_labour of this PostLedgerAccountsLedgerAccount.  # noqa: E501
        :type: bool
        """

        self._cis_labour = cis_labour

    @property
    def gifi_code(self):
        """Gets the gifi_code of this PostLedgerAccountsLedgerAccount.  # noqa: E501

        The GIFI code of the ledger account.  GIFI is short for The General Index of Financial Information and it lets the CRA validate tax information electronically instead of manually. Information from financial statements is categorized under the appropriate 4-digit-long GIFI code and entered on corporate income tax returns. GIFI is needed when filing a T2 income tax return.  _Canada only_   # noqa: E501

        :return: The gifi_code of this PostLedgerAccountsLedgerAccount.  # noqa: E501
        :rtype: int
        """
        return self._gifi_code

    @gifi_code.setter
    def gifi_code(self, gifi_code):
        """Sets the gifi_code of this PostLedgerAccountsLedgerAccount.

        The GIFI code of the ledger account.  GIFI is short for The General Index of Financial Information and it lets the CRA validate tax information electronically instead of manually. Information from financial statements is categorized under the appropriate 4-digit-long GIFI code and entered on corporate income tax returns. GIFI is needed when filing a T2 income tax return.  _Canada only_   # noqa: E501

        :param gifi_code: The gifi_code of this PostLedgerAccountsLedgerAccount.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                gifi_code is not None and gifi_code > 9999):  # noqa: E501
            raise ValueError("Invalid value for `gifi_code`, must be a value less than or equal to `9999`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                gifi_code is not None and gifi_code < 1000):  # noqa: E501
            raise ValueError("Invalid value for `gifi_code`, must be a value greater than or equal to `1000`")  # noqa: E501

        self._gifi_code = gifi_code

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
        if not isinstance(other, PostLedgerAccountsLedgerAccount):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PostLedgerAccountsLedgerAccount):
            return True

        return self.to_dict() != other.to_dict()
