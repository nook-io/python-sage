import pprint
import six
from sage.configuration import Configuration


class LedgerAccount(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        "id": "str",
        "displayed_as": "str",
        "path": "str",
        "created_at": "datetime",
        "updated_at": "datetime",
        "ledger_account_group": "CoaGroupType",
        "name": "str",
        "display_name": "str",
        "visible_scopes": "list[str]",
        "included_in_chart": "bool",
        "nominal_code": "int",
        "ledger_account_type": "Base",
        "ledger_account_classification": "Base",
        "tax_rate": "Base",
        "fixed_tax_rate": "bool",
        "visible_in_banking": "bool",
        "visible_in_expenses": "bool",
        "visible_in_journals": "bool",
        "visible_in_other_payments": "bool",
        "visible_in_other_receipts": "bool",
        "visible_in_reporting": "bool",
        "visible_in_sales": "bool",
        "balance_details": "LedgerAccountBalanceDetails",
        "is_control_account": "bool",
        "control_name": "str",
        "display_formatted": "str",
        "tax_recoverable": "bool",
        "recoverable_percentage": "float",
        "non_recoverable_ledger_account": "LedgerAccount",
        "cis_materials": "bool",
        "tax_instalment": "bool",
        "cis_labour": "bool",
        "gifi_code": "int",
    }
    attribute_map = {
        "id": "id",
        "displayed_as": "displayed_as",
        "path": "$path",
        "created_at": "created_at",
        "updated_at": "updated_at",
        "ledger_account_group": "ledger_account_group",
        "name": "name",
        "display_name": "display_name",
        "visible_scopes": "visible_scopes",
        "included_in_chart": "included_in_chart",
        "nominal_code": "nominal_code",
        "ledger_account_type": "ledger_account_type",
        "ledger_account_classification": "ledger_account_classification",
        "tax_rate": "tax_rate",
        "fixed_tax_rate": "fixed_tax_rate",
        "visible_in_banking": "visible_in_banking",
        "visible_in_expenses": "visible_in_expenses",
        "visible_in_journals": "visible_in_journals",
        "visible_in_other_payments": "visible_in_other_payments",
        "visible_in_other_receipts": "visible_in_other_receipts",
        "visible_in_reporting": "visible_in_reporting",
        "visible_in_sales": "visible_in_sales",
        "balance_details": "balance_details",
        "is_control_account": "is_control_account",
        "control_name": "control_name",
        "display_formatted": "display_formatted",
        "tax_recoverable": "tax_recoverable",
        "recoverable_percentage": "recoverable_percentage",
        "non_recoverable_ledger_account": "non_recoverable_ledger_account",
        "cis_materials": "cis_materials",
        "tax_instalment": "tax_instalment",
        "cis_labour": "cis_labour",
        "gifi_code": "gifi_code",
    }

    def __init__(
        self,
        id=None,
        displayed_as=None,
        path=None,
        created_at=None,
        updated_at=None,
        ledger_account_group=None,
        name=None,
        display_name=None,
        visible_scopes=None,
        included_in_chart=None,
        nominal_code=None,
        ledger_account_type=None,
        ledger_account_classification=None,
        tax_rate=None,
        fixed_tax_rate=None,
        visible_in_banking=None,
        visible_in_expenses=None,
        visible_in_journals=None,
        visible_in_other_payments=None,
        visible_in_other_receipts=None,
        visible_in_reporting=None,
        visible_in_sales=None,
        balance_details=None,
        is_control_account=None,
        control_name=None,
        display_formatted=None,
        tax_recoverable=None,
        recoverable_percentage=None,
        non_recoverable_ledger_account=None,
        cis_materials=None,
        tax_instalment=None,
        cis_labour=None,
        gifi_code=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._id = None
        self._displayed_as = None
        self._path = None
        self._created_at = None
        self._updated_at = None
        self._ledger_account_group = None
        self._name = None
        self._display_name = None
        self._visible_scopes = None
        self._included_in_chart = None
        self._nominal_code = None
        self._ledger_account_type = None
        self._ledger_account_classification = None
        self._tax_rate = None
        self._fixed_tax_rate = None
        self._visible_in_banking = None
        self._visible_in_expenses = None
        self._visible_in_journals = None
        self._visible_in_other_payments = None
        self._visible_in_other_receipts = None
        self._visible_in_reporting = None
        self._visible_in_sales = None
        self._balance_details = None
        self._is_control_account = None
        self._control_name = None
        self._display_formatted = None
        self._tax_recoverable = None
        self._recoverable_percentage = None
        self._non_recoverable_ledger_account = None
        self._cis_materials = None
        self._tax_instalment = None
        self._cis_labour = None
        self._gifi_code = None
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
        if ledger_account_group is not None:
            self.ledger_account_group = ledger_account_group
        if name is not None:
            self.name = name
        if display_name is not None:
            self.display_name = display_name
        if visible_scopes is not None:
            self.visible_scopes = visible_scopes
        if included_in_chart is not None:
            self.included_in_chart = included_in_chart
        if nominal_code is not None:
            self.nominal_code = nominal_code
        if ledger_account_type is not None:
            self.ledger_account_type = ledger_account_type
        if ledger_account_classification is not None:
            self.ledger_account_classification = ledger_account_classification
        if tax_rate is not None:
            self.tax_rate = tax_rate
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
        if balance_details is not None:
            self.balance_details = balance_details
        if is_control_account is not None:
            self.is_control_account = is_control_account
        if control_name is not None:
            self.control_name = control_name
        if display_formatted is not None:
            self.display_formatted = display_formatted
        if tax_recoverable is not None:
            self.tax_recoverable = tax_recoverable
        if recoverable_percentage is not None:
            self.recoverable_percentage = recoverable_percentage
        if non_recoverable_ledger_account is not None:
            self.non_recoverable_ledger_account = non_recoverable_ledger_account
        if cis_materials is not None:
            self.cis_materials = cis_materials
        if tax_instalment is not None:
            self.tax_instalment = tax_instalment
        if cis_labour is not None:
            self.cis_labour = cis_labour
        if gifi_code is not None:
            self.gifi_code = gifi_code

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def displayed_as(self):
        return self._displayed_as

    @displayed_as.setter
    def displayed_as(self, displayed_as):
        self._displayed_as = displayed_as

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path):
        self._path = path

    @property
    def created_at(self):
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        self._created_at = created_at

    @property
    def updated_at(self):
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        self._updated_at = updated_at

    @property
    def ledger_account_group(self):
        return self._ledger_account_group

    @ledger_account_group.setter
    def ledger_account_group(self, ledger_account_group):
        self._ledger_account_group = ledger_account_group

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if (
            self.local_vars_configuration.client_side_validation
            and name is not None
            and len(name) > 200
        ):
            raise ValueError(
                "Invalid value for `name`, length must be less than or equal to `200`"
            )
        self._name = name

    @property
    def display_name(self):
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        if (
            self.local_vars_configuration.client_side_validation
            and display_name is not None
            and len(display_name) > 200
        ):
            raise ValueError(
                "Invalid value for `display_name`, length must be less than or equal to `200`"
            )
        self._display_name = display_name

    @property
    def visible_scopes(self):
        return self._visible_scopes

    @visible_scopes.setter
    def visible_scopes(self, visible_scopes):
        self._visible_scopes = visible_scopes

    @property
    def included_in_chart(self):
        return self._included_in_chart

    @included_in_chart.setter
    def included_in_chart(self, included_in_chart):
        self._included_in_chart = included_in_chart

    @property
    def nominal_code(self):
        return self._nominal_code

    @nominal_code.setter
    def nominal_code(self, nominal_code):
        self._nominal_code = nominal_code

    @property
    def ledger_account_type(self):
        return self._ledger_account_type

    @ledger_account_type.setter
    def ledger_account_type(self, ledger_account_type):
        self._ledger_account_type = ledger_account_type

    @property
    def ledger_account_classification(self):
        return self._ledger_account_classification

    @ledger_account_classification.setter
    def ledger_account_classification(self, ledger_account_classification):
        self._ledger_account_classification = ledger_account_classification

    @property
    def tax_rate(self):
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, tax_rate):
        self._tax_rate = tax_rate

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
    def balance_details(self):
        return self._balance_details

    @balance_details.setter
    def balance_details(self, balance_details):
        self._balance_details = balance_details

    @property
    def is_control_account(self):
        return self._is_control_account

    @is_control_account.setter
    def is_control_account(self, is_control_account):
        self._is_control_account = is_control_account

    @property
    def control_name(self):
        return self._control_name

    @control_name.setter
    def control_name(self, control_name):
        if (
            self.local_vars_configuration.client_side_validation
            and control_name is not None
            and len(control_name) > 255
        ):
            raise ValueError(
                "Invalid value for `control_name`, length must be less than or equal to `255`"
            )
        self._control_name = control_name

    @property
    def display_formatted(self):
        return self._display_formatted

    @display_formatted.setter
    def display_formatted(self, display_formatted):
        self._display_formatted = display_formatted

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
    def non_recoverable_ledger_account(self):
        return self._non_recoverable_ledger_account

    @non_recoverable_ledger_account.setter
    def non_recoverable_ledger_account(self, non_recoverable_ledger_account):
        self._non_recoverable_ledger_account = non_recoverable_ledger_account

    @property
    def cis_materials(self):
        return self._cis_materials

    @cis_materials.setter
    def cis_materials(self, cis_materials):
        self._cis_materials = cis_materials

    @property
    def tax_instalment(self):
        return self._tax_instalment

    @tax_instalment.setter
    def tax_instalment(self, tax_instalment):
        self._tax_instalment = tax_instalment

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
        if not isinstance(other, LedgerAccount):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, LedgerAccount):
            return True
        return self.to_dict() != other.to_dict()
