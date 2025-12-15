import pprint
import six
from sage.configuration import Configuration


class QuickEntry(object):
    openapi_types = {
        "id": "str",
        "displayed_as": "str",
        "path": "str",
        "created_at": "datetime",
        "updated_at": "datetime",
        "transaction": "Base",
        "transaction_type": "Base",
        "deleted_at": "datetime",
        "quick_entry_type": "Base",
        "contact_name": "str",
        "contact_reference": "str",
        "contact": "Base",
        "date": "date",
        "reference": "str",
        "ledger_account": "Base",
        "details": "str",
        "net_amount": "float",
        "tax_rate": "Base",
        "tax_amount": "float",
        "tax_breakdown": "list[TaxBreakdown]",
        "total_amount": "float",
        "outstanding_amount": "float",
        "currency": "Base",
        "exchange_rate": "float",
        "inverse_exchange_rate": "float",
        "base_currency_net_amount": "float",
        "base_currency_tax_amount": "float",
        "base_currency_tax_breakdown": "list[TaxBreakdown]",
        "base_currency_total_amount": "float",
        "base_currency_outstanding_amount": "float",
        "status": "Base",
        "payments_allocations": "list[PaymentAllocation]",
        "tax_address_region": "Base",
        "migrated": "bool",
        "trade_of_asset": "bool",
    }
    attribute_map = {
        "id": "id",
        "displayed_as": "displayed_as",
        "path": "$path",
        "created_at": "created_at",
        "updated_at": "updated_at",
        "transaction": "transaction",
        "transaction_type": "transaction_type",
        "deleted_at": "deleted_at",
        "quick_entry_type": "quick_entry_type",
        "contact_name": "contact_name",
        "contact_reference": "contact_reference",
        "contact": "contact",
        "date": "date",
        "reference": "reference",
        "ledger_account": "ledger_account",
        "details": "details",
        "net_amount": "net_amount",
        "tax_rate": "tax_rate",
        "tax_amount": "tax_amount",
        "tax_breakdown": "tax_breakdown",
        "total_amount": "total_amount",
        "outstanding_amount": "outstanding_amount",
        "currency": "currency",
        "exchange_rate": "exchange_rate",
        "inverse_exchange_rate": "inverse_exchange_rate",
        "base_currency_net_amount": "base_currency_net_amount",
        "base_currency_tax_amount": "base_currency_tax_amount",
        "base_currency_tax_breakdown": "base_currency_tax_breakdown",
        "base_currency_total_amount": "base_currency_total_amount",
        "base_currency_outstanding_amount": "base_currency_outstanding_amount",
        "status": "status",
        "payments_allocations": "payments_allocations",
        "tax_address_region": "tax_address_region",
        "migrated": "migrated",
        "trade_of_asset": "trade_of_asset",
    }

    def __init__(
        self,
        id=None,
        displayed_as=None,
        path=None,
        created_at=None,
        updated_at=None,
        transaction=None,
        transaction_type=None,
        deleted_at=None,
        quick_entry_type=None,
        contact_name=None,
        contact_reference=None,
        contact=None,
        date=None,
        reference=None,
        ledger_account=None,
        details=None,
        net_amount=None,
        tax_rate=None,
        tax_amount=None,
        tax_breakdown=None,
        total_amount=None,
        outstanding_amount=None,
        currency=None,
        exchange_rate=None,
        inverse_exchange_rate=None,
        base_currency_net_amount=None,
        base_currency_tax_amount=None,
        base_currency_tax_breakdown=None,
        base_currency_total_amount=None,
        base_currency_outstanding_amount=None,
        status=None,
        payments_allocations=None,
        tax_address_region=None,
        migrated=None,
        trade_of_asset=None,
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
        self._transaction = None
        self._transaction_type = None
        self._deleted_at = None
        self._quick_entry_type = None
        self._contact_name = None
        self._contact_reference = None
        self._contact = None
        self._date = None
        self._reference = None
        self._ledger_account = None
        self._details = None
        self._net_amount = None
        self._tax_rate = None
        self._tax_amount = None
        self._tax_breakdown = None
        self._total_amount = None
        self._outstanding_amount = None
        self._currency = None
        self._exchange_rate = None
        self._inverse_exchange_rate = None
        self._base_currency_net_amount = None
        self._base_currency_tax_amount = None
        self._base_currency_tax_breakdown = None
        self._base_currency_total_amount = None
        self._base_currency_outstanding_amount = None
        self._status = None
        self._payments_allocations = None
        self._tax_address_region = None
        self._migrated = None
        self._trade_of_asset = None
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
        if transaction is not None:
            self.transaction = transaction
        if transaction_type is not None:
            self.transaction_type = transaction_type
        if deleted_at is not None:
            self.deleted_at = deleted_at
        if quick_entry_type is not None:
            self.quick_entry_type = quick_entry_type
        if contact_name is not None:
            self.contact_name = contact_name
        if contact_reference is not None:
            self.contact_reference = contact_reference
        if contact is not None:
            self.contact = contact
        if date is not None:
            self.date = date
        if reference is not None:
            self.reference = reference
        if ledger_account is not None:
            self.ledger_account = ledger_account
        if details is not None:
            self.details = details
        if net_amount is not None:
            self.net_amount = net_amount
        if tax_rate is not None:
            self.tax_rate = tax_rate
        if tax_amount is not None:
            self.tax_amount = tax_amount
        if tax_breakdown is not None:
            self.tax_breakdown = tax_breakdown
        if total_amount is not None:
            self.total_amount = total_amount
        if outstanding_amount is not None:
            self.outstanding_amount = outstanding_amount
        if currency is not None:
            self.currency = currency
        if exchange_rate is not None:
            self.exchange_rate = exchange_rate
        if inverse_exchange_rate is not None:
            self.inverse_exchange_rate = inverse_exchange_rate
        if base_currency_net_amount is not None:
            self.base_currency_net_amount = base_currency_net_amount
        if base_currency_tax_amount is not None:
            self.base_currency_tax_amount = base_currency_tax_amount
        if base_currency_tax_breakdown is not None:
            self.base_currency_tax_breakdown = base_currency_tax_breakdown
        if base_currency_total_amount is not None:
            self.base_currency_total_amount = base_currency_total_amount
        if base_currency_outstanding_amount is not None:
            self.base_currency_outstanding_amount = base_currency_outstanding_amount
        if status is not None:
            self.status = status
        if payments_allocations is not None:
            self.payments_allocations = payments_allocations
        if tax_address_region is not None:
            self.tax_address_region = tax_address_region
        if migrated is not None:
            self.migrated = migrated
        if trade_of_asset is not None:
            self.trade_of_asset = trade_of_asset

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
    def transaction(self):
        return self._transaction

    @transaction.setter
    def transaction(self, transaction):
        self._transaction = transaction

    @property
    def transaction_type(self):
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        self._transaction_type = transaction_type

    @property
    def deleted_at(self):
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        self._deleted_at = deleted_at

    @property
    def quick_entry_type(self):
        return self._quick_entry_type

    @quick_entry_type.setter
    def quick_entry_type(self, quick_entry_type):
        self._quick_entry_type = quick_entry_type

    @property
    def contact_name(self):
        return self._contact_name

    @contact_name.setter
    def contact_name(self, contact_name):
        if (
            self.local_vars_configuration.client_side_validation
            and contact_name is not None
            and len(contact_name) > 255
        ):
            raise ValueError(
                "Invalid value for `contact_name`, length must be less than or equal to `255`"
            )
        self._contact_name = contact_name

    @property
    def contact_reference(self):
        return self._contact_reference

    @contact_reference.setter
    def contact_reference(self, contact_reference):
        if (
            self.local_vars_configuration.client_side_validation
            and contact_reference is not None
            and len(contact_reference) > 255
        ):
            raise ValueError(
                "Invalid value for `contact_reference`, length must be less than or equal to `255`"
            )
        self._contact_reference = contact_reference

    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, contact):
        self._contact = contact

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

    @property
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, reference):
        if (
            self.local_vars_configuration.client_side_validation
            and reference is not None
            and len(reference) > 25
        ):
            raise ValueError(
                "Invalid value for `reference`, length must be less than or equal to `25`"
            )
        self._reference = reference

    @property
    def ledger_account(self):
        return self._ledger_account

    @ledger_account.setter
    def ledger_account(self, ledger_account):
        self._ledger_account = ledger_account

    @property
    def details(self):
        return self._details

    @details.setter
    def details(self, details):
        if (
            self.local_vars_configuration.client_side_validation
            and details is not None
            and len(details) > 255
        ):
            raise ValueError(
                "Invalid value for `details`, length must be less than or equal to `255`"
            )
        self._details = details

    @property
    def net_amount(self):
        return self._net_amount

    @net_amount.setter
    def net_amount(self, net_amount):
        self._net_amount = net_amount

    @property
    def tax_rate(self):
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, tax_rate):
        self._tax_rate = tax_rate

    @property
    def tax_amount(self):
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        self._tax_amount = tax_amount

    @property
    def tax_breakdown(self):
        return self._tax_breakdown

    @tax_breakdown.setter
    def tax_breakdown(self, tax_breakdown):
        self._tax_breakdown = tax_breakdown

    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        self._total_amount = total_amount

    @property
    def outstanding_amount(self):
        return self._outstanding_amount

    @outstanding_amount.setter
    def outstanding_amount(self, outstanding_amount):
        self._outstanding_amount = outstanding_amount

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, currency):
        self._currency = currency

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
    def base_currency_tax_breakdown(self):
        return self._base_currency_tax_breakdown

    @base_currency_tax_breakdown.setter
    def base_currency_tax_breakdown(self, base_currency_tax_breakdown):
        self._base_currency_tax_breakdown = base_currency_tax_breakdown

    @property
    def base_currency_total_amount(self):
        return self._base_currency_total_amount

    @base_currency_total_amount.setter
    def base_currency_total_amount(self, base_currency_total_amount):
        self._base_currency_total_amount = base_currency_total_amount

    @property
    def base_currency_outstanding_amount(self):
        return self._base_currency_outstanding_amount

    @base_currency_outstanding_amount.setter
    def base_currency_outstanding_amount(self, base_currency_outstanding_amount):
        self._base_currency_outstanding_amount = base_currency_outstanding_amount

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def payments_allocations(self):
        return self._payments_allocations

    @payments_allocations.setter
    def payments_allocations(self, payments_allocations):
        self._payments_allocations = payments_allocations

    @property
    def tax_address_region(self):
        return self._tax_address_region

    @tax_address_region.setter
    def tax_address_region(self, tax_address_region):
        self._tax_address_region = tax_address_region

    @property
    def migrated(self):
        return self._migrated

    @migrated.setter
    def migrated(self, migrated):
        self._migrated = migrated

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
        if not isinstance(other, QuickEntry):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, QuickEntry):
            return True
        return self.to_dict() != other.to_dict()
