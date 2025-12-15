import pprint
import six
from sage.configuration import Configuration


class PutContactOpeningBalancesContactOpeningBalance(object):
    openapi_types = {
        "contact_opening_balance_type_id": "str",
        "date": "date",
        "contact_id": "str",
        "reference": "str",
        "total_amount": "float",
        "transaction_type_id": "str",
        "details": "str",
        "net_amount": "float",
        "tax_rate_id": "str",
        "tax_amount": "float",
        "currency_id": "str",
        "exchange_rate": "float",
        "base_currency_net_amount": "float",
        "base_currency_tax_amount": "float",
        "base_currency_total_amount": "float",
    }
    attribute_map = {
        "contact_opening_balance_type_id": "contact_opening_balance_type_id",
        "date": "date",
        "contact_id": "contact_id",
        "reference": "reference",
        "total_amount": "total_amount",
        "transaction_type_id": "transaction_type_id",
        "details": "details",
        "net_amount": "net_amount",
        "tax_rate_id": "tax_rate_id",
        "tax_amount": "tax_amount",
        "currency_id": "currency_id",
        "exchange_rate": "exchange_rate",
        "base_currency_net_amount": "base_currency_net_amount",
        "base_currency_tax_amount": "base_currency_tax_amount",
        "base_currency_total_amount": "base_currency_total_amount",
    }

    def __init__(
        self,
        contact_opening_balance_type_id=None,
        date=None,
        contact_id=None,
        reference=None,
        total_amount=None,
        transaction_type_id=None,
        details=None,
        net_amount=None,
        tax_rate_id=None,
        tax_amount=None,
        currency_id=None,
        exchange_rate=None,
        base_currency_net_amount=None,
        base_currency_tax_amount=None,
        base_currency_total_amount=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._contact_opening_balance_type_id = None
        self._date = None
        self._contact_id = None
        self._reference = None
        self._total_amount = None
        self._transaction_type_id = None
        self._details = None
        self._net_amount = None
        self._tax_rate_id = None
        self._tax_amount = None
        self._currency_id = None
        self._exchange_rate = None
        self._base_currency_net_amount = None
        self._base_currency_tax_amount = None
        self._base_currency_total_amount = None
        self.discriminator = None
        if contact_opening_balance_type_id is not None:
            self.contact_opening_balance_type_id = contact_opening_balance_type_id
        if date is not None:
            self.date = date
        if contact_id is not None:
            self.contact_id = contact_id
        if reference is not None:
            self.reference = reference
        if total_amount is not None:
            self.total_amount = total_amount
        if transaction_type_id is not None:
            self.transaction_type_id = transaction_type_id
        if details is not None:
            self.details = details
        if net_amount is not None:
            self.net_amount = net_amount
        if tax_rate_id is not None:
            self.tax_rate_id = tax_rate_id
        if tax_amount is not None:
            self.tax_amount = tax_amount
        if currency_id is not None:
            self.currency_id = currency_id
        if exchange_rate is not None:
            self.exchange_rate = exchange_rate
        if base_currency_net_amount is not None:
            self.base_currency_net_amount = base_currency_net_amount
        if base_currency_tax_amount is not None:
            self.base_currency_tax_amount = base_currency_tax_amount
        if base_currency_total_amount is not None:
            self.base_currency_total_amount = base_currency_total_amount

    @property
    def contact_opening_balance_type_id(self):
        return self._contact_opening_balance_type_id

    @contact_opening_balance_type_id.setter
    def contact_opening_balance_type_id(self, contact_opening_balance_type_id):
        self._contact_opening_balance_type_id = contact_opening_balance_type_id

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

    @property
    def contact_id(self):
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        self._contact_id = contact_id

    @property
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, reference):
        self._reference = reference

    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        self._total_amount = total_amount

    @property
    def transaction_type_id(self):
        return self._transaction_type_id

    @transaction_type_id.setter
    def transaction_type_id(self, transaction_type_id):
        self._transaction_type_id = transaction_type_id

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
        if not isinstance(other, PutContactOpeningBalancesContactOpeningBalance):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PutContactOpeningBalancesContactOpeningBalance):
            return True
        return self.to_dict() != other.to_dict()
