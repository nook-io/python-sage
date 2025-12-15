import pprint
import six
from sage.configuration import Configuration


class PutFinancialSettingsFinancialSettings(object):
    openapi_types = {
        "year_end_date": "date",
        "year_end_lockdown_date": "date",
        "accounting_type": "str",
        "accounts_start_date": "date",
        "base_currency_id": "str",
        "multi_currency_enabled": "bool",
        "use_live_exchange_rates": "bool",
        "mtd_activation_status": "str",
        "mtd_connected": "bool",
        "mtd_authenticated_date": "date",
        "tax_scheme_id": "str",
        "tax_return_frequency_id": "str",
        "tax_number": "str",
        "general_tax_number": "str",
        "tax_office_id": "str",
        "default_irpf_rate": "float",
        "flat_rate_tax_percentage": "float",
        "recoverable_percentage": "float",
        "sales_tax_calculation": "str",
        "purchase_tax_calculation": "str",
    }
    attribute_map = {
        "year_end_date": "year_end_date",
        "year_end_lockdown_date": "year_end_lockdown_date",
        "accounting_type": "accounting_type",
        "accounts_start_date": "accounts_start_date",
        "base_currency_id": "base_currency_id",
        "multi_currency_enabled": "multi_currency_enabled",
        "use_live_exchange_rates": "use_live_exchange_rates",
        "mtd_activation_status": "mtd_activation_status",
        "mtd_connected": "mtd_connected",
        "mtd_authenticated_date": "mtd_authenticated_date",
        "tax_scheme_id": "tax_scheme_id",
        "tax_return_frequency_id": "tax_return_frequency_id",
        "tax_number": "tax_number",
        "general_tax_number": "general_tax_number",
        "tax_office_id": "tax_office_id",
        "default_irpf_rate": "default_irpf_rate",
        "flat_rate_tax_percentage": "flat_rate_tax_percentage",
        "recoverable_percentage": "recoverable_percentage",
        "sales_tax_calculation": "sales_tax_calculation",
        "purchase_tax_calculation": "purchase_tax_calculation",
    }

    def __init__(
        self,
        year_end_date=None,
        year_end_lockdown_date=None,
        accounting_type=None,
        accounts_start_date=None,
        base_currency_id=None,
        multi_currency_enabled=None,
        use_live_exchange_rates=None,
        mtd_activation_status=None,
        mtd_connected=None,
        mtd_authenticated_date=None,
        tax_scheme_id=None,
        tax_return_frequency_id=None,
        tax_number=None,
        general_tax_number=None,
        tax_office_id=None,
        default_irpf_rate=None,
        flat_rate_tax_percentage=None,
        recoverable_percentage=None,
        sales_tax_calculation=None,
        purchase_tax_calculation=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._year_end_date = None
        self._year_end_lockdown_date = None
        self._accounting_type = None
        self._accounts_start_date = None
        self._base_currency_id = None
        self._multi_currency_enabled = None
        self._use_live_exchange_rates = None
        self._mtd_activation_status = None
        self._mtd_connected = None
        self._mtd_authenticated_date = None
        self._tax_scheme_id = None
        self._tax_return_frequency_id = None
        self._tax_number = None
        self._general_tax_number = None
        self._tax_office_id = None
        self._default_irpf_rate = None
        self._flat_rate_tax_percentage = None
        self._recoverable_percentage = None
        self._sales_tax_calculation = None
        self._purchase_tax_calculation = None
        self.discriminator = None
        if year_end_date is not None:
            self.year_end_date = year_end_date
        if year_end_lockdown_date is not None:
            self.year_end_lockdown_date = year_end_lockdown_date
        if accounting_type is not None:
            self.accounting_type = accounting_type
        if accounts_start_date is not None:
            self.accounts_start_date = accounts_start_date
        if base_currency_id is not None:
            self.base_currency_id = base_currency_id
        if multi_currency_enabled is not None:
            self.multi_currency_enabled = multi_currency_enabled
        if use_live_exchange_rates is not None:
            self.use_live_exchange_rates = use_live_exchange_rates
        if mtd_activation_status is not None:
            self.mtd_activation_status = mtd_activation_status
        if mtd_connected is not None:
            self.mtd_connected = mtd_connected
        if mtd_authenticated_date is not None:
            self.mtd_authenticated_date = mtd_authenticated_date
        if tax_scheme_id is not None:
            self.tax_scheme_id = tax_scheme_id
        if tax_return_frequency_id is not None:
            self.tax_return_frequency_id = tax_return_frequency_id
        if tax_number is not None:
            self.tax_number = tax_number
        if general_tax_number is not None:
            self.general_tax_number = general_tax_number
        if tax_office_id is not None:
            self.tax_office_id = tax_office_id
        if default_irpf_rate is not None:
            self.default_irpf_rate = default_irpf_rate
        if flat_rate_tax_percentage is not None:
            self.flat_rate_tax_percentage = flat_rate_tax_percentage
        if recoverable_percentage is not None:
            self.recoverable_percentage = recoverable_percentage
        if sales_tax_calculation is not None:
            self.sales_tax_calculation = sales_tax_calculation
        if purchase_tax_calculation is not None:
            self.purchase_tax_calculation = purchase_tax_calculation

    @property
    def year_end_date(self):
        return self._year_end_date

    @year_end_date.setter
    def year_end_date(self, year_end_date):
        self._year_end_date = year_end_date

    @property
    def year_end_lockdown_date(self):
        return self._year_end_lockdown_date

    @year_end_lockdown_date.setter
    def year_end_lockdown_date(self, year_end_lockdown_date):
        self._year_end_lockdown_date = year_end_lockdown_date

    @property
    def accounting_type(self):
        return self._accounting_type

    @accounting_type.setter
    def accounting_type(self, accounting_type):
        self._accounting_type = accounting_type

    @property
    def accounts_start_date(self):
        return self._accounts_start_date

    @accounts_start_date.setter
    def accounts_start_date(self, accounts_start_date):
        self._accounts_start_date = accounts_start_date

    @property
    def base_currency_id(self):
        return self._base_currency_id

    @base_currency_id.setter
    def base_currency_id(self, base_currency_id):
        self._base_currency_id = base_currency_id

    @property
    def multi_currency_enabled(self):
        return self._multi_currency_enabled

    @multi_currency_enabled.setter
    def multi_currency_enabled(self, multi_currency_enabled):
        self._multi_currency_enabled = multi_currency_enabled

    @property
    def use_live_exchange_rates(self):
        return self._use_live_exchange_rates

    @use_live_exchange_rates.setter
    def use_live_exchange_rates(self, use_live_exchange_rates):
        self._use_live_exchange_rates = use_live_exchange_rates

    @property
    def mtd_activation_status(self):
        return self._mtd_activation_status

    @mtd_activation_status.setter
    def mtd_activation_status(self, mtd_activation_status):
        self._mtd_activation_status = mtd_activation_status

    @property
    def mtd_connected(self):
        return self._mtd_connected

    @mtd_connected.setter
    def mtd_connected(self, mtd_connected):
        self._mtd_connected = mtd_connected

    @property
    def mtd_authenticated_date(self):
        return self._mtd_authenticated_date

    @mtd_authenticated_date.setter
    def mtd_authenticated_date(self, mtd_authenticated_date):
        self._mtd_authenticated_date = mtd_authenticated_date

    @property
    def tax_scheme_id(self):
        return self._tax_scheme_id

    @tax_scheme_id.setter
    def tax_scheme_id(self, tax_scheme_id):
        self._tax_scheme_id = tax_scheme_id

    @property
    def tax_return_frequency_id(self):
        return self._tax_return_frequency_id

    @tax_return_frequency_id.setter
    def tax_return_frequency_id(self, tax_return_frequency_id):
        self._tax_return_frequency_id = tax_return_frequency_id

    @property
    def tax_number(self):
        return self._tax_number

    @tax_number.setter
    def tax_number(self, tax_number):
        self._tax_number = tax_number

    @property
    def general_tax_number(self):
        return self._general_tax_number

    @general_tax_number.setter
    def general_tax_number(self, general_tax_number):
        self._general_tax_number = general_tax_number

    @property
    def tax_office_id(self):
        return self._tax_office_id

    @tax_office_id.setter
    def tax_office_id(self, tax_office_id):
        self._tax_office_id = tax_office_id

    @property
    def default_irpf_rate(self):
        return self._default_irpf_rate

    @default_irpf_rate.setter
    def default_irpf_rate(self, default_irpf_rate):
        self._default_irpf_rate = default_irpf_rate

    @property
    def flat_rate_tax_percentage(self):
        return self._flat_rate_tax_percentage

    @flat_rate_tax_percentage.setter
    def flat_rate_tax_percentage(self, flat_rate_tax_percentage):
        self._flat_rate_tax_percentage = flat_rate_tax_percentage

    @property
    def recoverable_percentage(self):
        return self._recoverable_percentage

    @recoverable_percentage.setter
    def recoverable_percentage(self, recoverable_percentage):
        self._recoverable_percentage = recoverable_percentage

    @property
    def sales_tax_calculation(self):
        return self._sales_tax_calculation

    @sales_tax_calculation.setter
    def sales_tax_calculation(self, sales_tax_calculation):
        self._sales_tax_calculation = sales_tax_calculation

    @property
    def purchase_tax_calculation(self):
        return self._purchase_tax_calculation

    @purchase_tax_calculation.setter
    def purchase_tax_calculation(self, purchase_tax_calculation):
        self._purchase_tax_calculation = purchase_tax_calculation

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
        if not isinstance(other, PutFinancialSettingsFinancialSettings):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PutFinancialSettingsFinancialSettings):
            return True
        return self.to_dict() != other.to_dict()
