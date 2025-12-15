import pprint
import six
from sage.configuration import Configuration


class PostLedgerAccountsLedgerAccount(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        "ledger_account_type_id": "str",
        "included_in_chart": "bool",
        "name": "str",
        "display_name": "str",
        "nominal_code": "int",
        "ledger_account_classification_id": "str",
        "tax_rate_id": "str",
        "fixed_tax_rate": "bool",
        "visible_in_banking": "bool",
        "visible_in_expenses": "bool",
        "visible_in_journals": "bool",
        "visible_in_other_payments": "bool",
        "visible_in_other_receipts": "bool",
        "visible_in_reporting": "bool",
        "visible_in_sales": "bool",
        "control_name": "str",
        "tax_recoverable": "bool",
        "recoverable_percentage": "float",
        "non_recoverable_ledger_account_id": "str",
        "cis_materials": "bool",
        "cis_labour": "bool",
        "gifi_code": "int",
    }
    attribute_map = {
        "ledger_account_type_id": "ledger_account_type_id",
        "included_in_chart": "included_in_chart",
        "name": "name",
        "display_name": "display_name",
        "nominal_code": "nominal_code",
        "ledger_account_classification_id": "ledger_account_classification_id",
        "tax_rate_id": "tax_rate_id",
        "fixed_tax_rate": "fixed_tax_rate",
        "visible_in_banking": "visible_in_banking",
        "visible_in_expenses": "visible_in_expenses",
        "visible_in_journals": "visible_in_journals",
        "visible_in_other_payments": "visible_in_other_payments",
        "visible_in_other_receipts": "visible_in_other_receipts",
        "visible_in_reporting": "visible_in_reporting",
        "visible_in_sales": "visible_in_sales",
        "control_name": "control_name",
        "tax_recoverable": "tax_recoverable",
        "recoverable_percentage": "recoverable_percentage",
        "non_recoverable_ledger_account_id": "non_recoverable_ledger_account_id",
        "cis_materials": "cis_materials",
        "cis_labour": "cis_labour",
        "gifi_code": "gifi_code",
    }

    def __init__(
        self,
        ledger_account_type_id=None,
        included_in_chart=None,
        name=None,
        display_name=None,
        nominal_code=None,
        ledger_account_classification_id=None,
        tax_rate_id=None,
        fixed_tax_rate=None,
        visible_in_banking=None,
        visible_in_expenses=None,
        visible_in_journals=None,
        visible_in_other_payments=None,
        visible_in_other_receipts=None,
        visible_in_reporting=None,
        visible_in_sales=None,
        control_name=None,
        tax_recoverable=None,
        recoverable_percentage=None,
        non_recoverable_ledger_account_id=None,
        cis_materials=None,
        cis_labour=None,
        gifi_code=None,
        local_vars_configuration=None,
    ):
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
        return self._ledger_account_type_id

    @ledger_account_type_id.setter
    def ledger_account_type_id(self, ledger_account_type_id):
        if (
            self.local_vars_configuration.client_side_validation
            and ledger_account_type_id is None
        ):
            raise ValueError(
                "Invalid value for `ledger_account_type_id`, must not be `None`"
            )
        self._ledger_account_type_id = ledger_account_type_id

    @property
    def included_in_chart(self):
        return self._included_in_chart

    @included_in_chart.setter
    def included_in_chart(self, included_in_chart):
        if (
            self.local_vars_configuration.client_side_validation
            and included_in_chart is None
        ):
            raise ValueError(
                "Invalid value for `included_in_chart`, must not be `None`"
            )
        self._included_in_chart = included_in_chart

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if self.local_vars_configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        self._name = name

    @property
    def display_name(self):
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        if (
            self.local_vars_configuration.client_side_validation
            and display_name is None
        ):
            raise ValueError("Invalid value for `display_name`, must not be `None`")
        self._display_name = display_name

    @property
    def nominal_code(self):
        return self._nominal_code

    @nominal_code.setter
    def nominal_code(self, nominal_code):
        if (
            self.local_vars_configuration.client_side_validation
            and nominal_code is None
        ):
            raise ValueError("Invalid value for `nominal_code`, must not be `None`")
        if (
            self.local_vars_configuration.client_side_validation
            and nominal_code is not None
            and nominal_code > 99999999
        ):
            raise ValueError(
                "Invalid value for `nominal_code`, must be a value less than or equal to `99999999`"
            )
        if (
            self.local_vars_configuration.client_side_validation
            and nominal_code is not None
            and nominal_code < 1
        ):
            raise ValueError(
                "Invalid value for `nominal_code`, must be a value greater than or equal to `1`"
            )
        self._nominal_code = nominal_code

    @property
    def ledger_account_classification_id(self):
        return self._ledger_account_classification_id

    @ledger_account_classification_id.setter
    def ledger_account_classification_id(self, ledger_account_classification_id):
        self._ledger_account_classification_id = ledger_account_classification_id

    @property
    def tax_rate_id(self):
        return self._tax_rate_id

    @tax_rate_id.setter
    def tax_rate_id(self, tax_rate_id):
        self._tax_rate_id = tax_rate_id

    @property
    def fixed_tax_rate(self):
        return self._fixed_tax_rate

    @fixed_tax_rate.setter
    def fixed_tax_rate(self, fixed_tax_rate):
        self._fixed_tax_rate = fixed_tax_rate

    @property
    def visible_in_banking(self):
        return self._visible_in_banking

    @visible_in_banking.setter
    def visible_in_banking(self, visible_in_banking):
        self._visible_in_banking = visible_in_banking

    @property
    def visible_in_expenses(self):
        return self._visible_in_expenses

    @visible_in_expenses.setter
    def visible_in_expenses(self, visible_in_expenses):
        self._visible_in_expenses = visible_in_expenses

    @property
    def visible_in_journals(self):
        return self._visible_in_journals

    @visible_in_journals.setter
    def visible_in_journals(self, visible_in_journals):
        self._visible_in_journals = visible_in_journals

    @property
    def visible_in_other_payments(self):
        return self._visible_in_other_payments

    @visible_in_other_payments.setter
    def visible_in_other_payments(self, visible_in_other_payments):
        self._visible_in_other_payments = visible_in_other_payments

    @property
    def visible_in_other_receipts(self):
        return self._visible_in_other_receipts

    @visible_in_other_receipts.setter
    def visible_in_other_receipts(self, visible_in_other_receipts):
        self._visible_in_other_receipts = visible_in_other_receipts

    @property
    def visible_in_reporting(self):
        return self._visible_in_reporting

    @visible_in_reporting.setter
    def visible_in_reporting(self, visible_in_reporting):
        self._visible_in_reporting = visible_in_reporting

    @property
    def visible_in_sales(self):
        return self._visible_in_sales

    @visible_in_sales.setter
    def visible_in_sales(self, visible_in_sales):
        self._visible_in_sales = visible_in_sales

    @property
    def control_name(self):
        return self._control_name

    @control_name.setter
    def control_name(self, control_name):
        self._control_name = control_name

    @property
    def tax_recoverable(self):
        return self._tax_recoverable

    @tax_recoverable.setter
    def tax_recoverable(self, tax_recoverable):
        self._tax_recoverable = tax_recoverable

    @property
    def recoverable_percentage(self):
        return self._recoverable_percentage

    @recoverable_percentage.setter
    def recoverable_percentage(self, recoverable_percentage):
        self._recoverable_percentage = recoverable_percentage

    @property
    def non_recoverable_ledger_account_id(self):
        return self._non_recoverable_ledger_account_id

    @non_recoverable_ledger_account_id.setter
    def non_recoverable_ledger_account_id(self, non_recoverable_ledger_account_id):
        self._non_recoverable_ledger_account_id = non_recoverable_ledger_account_id

    @property
    def cis_materials(self):
        return self._cis_materials

    @cis_materials.setter
    def cis_materials(self, cis_materials):
        self._cis_materials = cis_materials

    @property
    def cis_labour(self):
        return self._cis_labour

    @cis_labour.setter
    def cis_labour(self, cis_labour):
        self._cis_labour = cis_labour

    @property
    def gifi_code(self):
        return self._gifi_code

    @gifi_code.setter
    def gifi_code(self, gifi_code):
        if (
            self.local_vars_configuration.client_side_validation
            and gifi_code is not None
            and gifi_code > 9999
        ):
            raise ValueError(
                "Invalid value for `gifi_code`, must be a value less than or equal to `9999`"
            )
        if (
            self.local_vars_configuration.client_side_validation
            and gifi_code is not None
            and gifi_code < 1000
        ):
            raise ValueError(
                "Invalid value for `gifi_code`, must be a value greater than or equal to `1000`"
            )
        self._gifi_code = gifi_code

    def to_dict(self):
        result = {}
        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, PostLedgerAccountsLedgerAccount):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PostLedgerAccountsLedgerAccount):
            return True
        return self.to_dict() != other.to_dict()
