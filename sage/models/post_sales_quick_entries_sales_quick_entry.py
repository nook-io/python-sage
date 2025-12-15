import pprint
import six
from sage.configuration import Configuration


class PostSalesQuickEntriesSalesQuickEntry(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        "quick_entry_type_id": "str",
        "date": "date",
        "contact_id": "str",
        "reference": "str",
        "ledger_account_id": "str",
        "contact_name": "str",
        "contact_reference": "str",
        "details": "str",
        "net_amount": "float",
        "tax_rate_id": "str",
        "tax_amount": "float",
        "total_amount": "float",
        "currency_id": "str",
        "exchange_rate": "float",
        "inverse_exchange_rate": "float",
        "base_currency_net_amount": "float",
        "base_currency_tax_amount": "float",
        "base_currency_total_amount": "float",
        "status_id": "str",
        "tax_address_region_id": "str",
        "trade_of_asset": "bool",
    }
    attribute_map = {
        "quick_entry_type_id": "quick_entry_type_id",
        "date": "date",
        "contact_id": "contact_id",
        "reference": "reference",
        "ledger_account_id": "ledger_account_id",
        "contact_name": "contact_name",
        "contact_reference": "contact_reference",
        "details": "details",
        "net_amount": "net_amount",
        "tax_rate_id": "tax_rate_id",
        "tax_amount": "tax_amount",
        "total_amount": "total_amount",
        "currency_id": "currency_id",
        "exchange_rate": "exchange_rate",
        "inverse_exchange_rate": "inverse_exchange_rate",
        "base_currency_net_amount": "base_currency_net_amount",
        "base_currency_tax_amount": "base_currency_tax_amount",
        "base_currency_total_amount": "base_currency_total_amount",
        "status_id": "status_id",
        "tax_address_region_id": "tax_address_region_id",
        "trade_of_asset": "trade_of_asset",
    }

    def __init__(
        self,
        quick_entry_type_id=None,
        date=None,
        contact_id=None,
        reference=None,
        ledger_account_id=None,
        contact_name=None,
        contact_reference=None,
        details=None,
        net_amount=None,
        tax_rate_id=None,
        tax_amount=None,
        total_amount=None,
        currency_id=None,
        exchange_rate=None,
        inverse_exchange_rate=None,
        base_currency_net_amount=None,
        base_currency_tax_amount=None,
        base_currency_total_amount=None,
        status_id=None,
        tax_address_region_id=None,
        trade_of_asset=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._quick_entry_type_id = None
        self._date = None
        self._contact_id = None
        self._reference = None
        self._ledger_account_id = None
        self._contact_name = None
        self._contact_reference = None
        self._details = None
        self._net_amount = None
        self._tax_rate_id = None
        self._tax_amount = None
        self._total_amount = None
        self._currency_id = None
        self._exchange_rate = None
        self._inverse_exchange_rate = None
        self._base_currency_net_amount = None
        self._base_currency_tax_amount = None
        self._base_currency_total_amount = None
        self._status_id = None
        self._tax_address_region_id = None
        self._trade_of_asset = None
        self.discriminator = None
        self.quick_entry_type_id = quick_entry_type_id
        self.date = date
        self.contact_id = contact_id
        self.reference = reference
        self.ledger_account_id = ledger_account_id
        if contact_name is not None:
            self.contact_name = contact_name
        if contact_reference is not None:
            self.contact_reference = contact_reference
        if details is not None:
            self.details = details
        if net_amount is not None:
            self.net_amount = net_amount
        if tax_rate_id is not None:
            self.tax_rate_id = tax_rate_id
        if tax_amount is not None:
            self.tax_amount = tax_amount
        if total_amount is not None:
            self.total_amount = total_amount
        if currency_id is not None:
            self.currency_id = currency_id
        if exchange_rate is not None:
            self.exchange_rate = exchange_rate
        if inverse_exchange_rate is not None:
            self.inverse_exchange_rate = inverse_exchange_rate
        if base_currency_net_amount is not None:
            self.base_currency_net_amount = base_currency_net_amount
        if base_currency_tax_amount is not None:
            self.base_currency_tax_amount = base_currency_tax_amount
        if base_currency_total_amount is not None:
            self.base_currency_total_amount = base_currency_total_amount
        if status_id is not None:
            self.status_id = status_id
        if tax_address_region_id is not None:
            self.tax_address_region_id = tax_address_region_id
        if trade_of_asset is not None:
            self.trade_of_asset = trade_of_asset

    @property
    def quick_entry_type_id(self):
        return self._quick_entry_type_id

    @quick_entry_type_id.setter
    def quick_entry_type_id(self, quick_entry_type_id):
        if (
            self.local_vars_configuration.client_side_validation
            and quick_entry_type_id is None
        ):
            raise ValueError(
                "Invalid value for `quick_entry_type_id`, must not be `None`"
            )
        self._quick_entry_type_id = quick_entry_type_id

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if self.local_vars_configuration.client_side_validation and date is None:
            raise ValueError("Invalid value for `date`, must not be `None`")
        self._date = date

    @property
    def contact_id(self):
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        if self.local_vars_configuration.client_side_validation and contact_id is None:
            raise ValueError("Invalid value for `contact_id`, must not be `None`")
        self._contact_id = contact_id

    @property
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, reference):
        if self.local_vars_configuration.client_side_validation and reference is None:
            raise ValueError("Invalid value for `reference`, must not be `None`")
        self._reference = reference

    @property
    def ledger_account_id(self):
        return self._ledger_account_id

    @ledger_account_id.setter
    def ledger_account_id(self, ledger_account_id):
        if (
            self.local_vars_configuration.client_side_validation
            and ledger_account_id is None
        ):
            raise ValueError(
                "Invalid value for `ledger_account_id`, must not be `None`"
            )
        self._ledger_account_id = ledger_account_id

    @property
    def contact_name(self):
        return self._contact_name

    @contact_name.setter
    def contact_name(self, contact_name):
        self._contact_name = contact_name

    @property
    def contact_reference(self):
        return self._contact_reference

    @contact_reference.setter
    def contact_reference(self, contact_reference):
        self._contact_reference = contact_reference

    @property
    def details(self):
        return self._details

    @details.setter
    def details(self, details):
        self._details = details

    @property
    def net_amount(self):
        return self._net_amount

    @net_amount.setter
    def net_amount(self, net_amount):
        self._net_amount = net_amount

    @property
    def tax_rate_id(self):
        return self._tax_rate_id

    @tax_rate_id.setter
    def tax_rate_id(self, tax_rate_id):
        self._tax_rate_id = tax_rate_id

    @property
    def tax_amount(self):
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        self._tax_amount = tax_amount

    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        self._total_amount = total_amount

    @property
    def currency_id(self):
        return self._currency_id

    @currency_id.setter
    def currency_id(self, currency_id):
        self._currency_id = currency_id

    @property
    def exchange_rate(self):
        return self._exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, exchange_rate):
        self._exchange_rate = exchange_rate

    @property
    def inverse_exchange_rate(self):
        return self._inverse_exchange_rate

    @inverse_exchange_rate.setter
    def inverse_exchange_rate(self, inverse_exchange_rate):
        self._inverse_exchange_rate = inverse_exchange_rate

    @property
    def base_currency_net_amount(self):
        return self._base_currency_net_amount

    @base_currency_net_amount.setter
    def base_currency_net_amount(self, base_currency_net_amount):
        self._base_currency_net_amount = base_currency_net_amount

    @property
    def base_currency_tax_amount(self):
        return self._base_currency_tax_amount

    @base_currency_tax_amount.setter
    def base_currency_tax_amount(self, base_currency_tax_amount):
        self._base_currency_tax_amount = base_currency_tax_amount

    @property
    def base_currency_total_amount(self):
        return self._base_currency_total_amount

    @base_currency_total_amount.setter
    def base_currency_total_amount(self, base_currency_total_amount):
        self._base_currency_total_amount = base_currency_total_amount

    @property
    def status_id(self):
        return self._status_id

    @status_id.setter
    def status_id(self, status_id):
        self._status_id = status_id

    @property
    def tax_address_region_id(self):
        return self._tax_address_region_id

    @tax_address_region_id.setter
    def tax_address_region_id(self, tax_address_region_id):
        self._tax_address_region_id = tax_address_region_id

    @property
    def trade_of_asset(self):
        return self._trade_of_asset

    @trade_of_asset.setter
    def trade_of_asset(self, trade_of_asset):
        self._trade_of_asset = trade_of_asset

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
        if not isinstance(other, PostSalesQuickEntriesSalesQuickEntry):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PostSalesQuickEntriesSalesQuickEntry):
            return True
        return self.to_dict() != other.to_dict()
