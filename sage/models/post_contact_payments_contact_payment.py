import pprint
import six
from sage.configuration import Configuration


class PostContactPaymentsContactPayment(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        "transaction_type_id": "str",
        "contact_id": "str",
        "bank_account_id": "str",
        "date": "date",
        "total_amount": "float",
        "payment_method_id": "str",
        "net_amount": "float",
        "tax_amount": "float",
        "currency_id": "str",
        "exchange_rate": "float",
        "base_currency_net_amount": "float",
        "base_currency_tax_amount": "float",
        "base_currency_total_amount": "float",
        "base_currency_currency_charge": "float",
        "reference": "str",
        "tax_rate_id": "str",
        "allocated_artefacts": "list[PostContactPaymentsContactPaymentAllocatedArtefacts]",
        "payment_on_account": "PostContactPaymentsContactPaymentPaymentOnAccount",
    }
    attribute_map = {
        "transaction_type_id": "transaction_type_id",
        "contact_id": "contact_id",
        "bank_account_id": "bank_account_id",
        "date": "date",
        "total_amount": "total_amount",
        "payment_method_id": "payment_method_id",
        "net_amount": "net_amount",
        "tax_amount": "tax_amount",
        "currency_id": "currency_id",
        "exchange_rate": "exchange_rate",
        "base_currency_net_amount": "base_currency_net_amount",
        "base_currency_tax_amount": "base_currency_tax_amount",
        "base_currency_total_amount": "base_currency_total_amount",
        "base_currency_currency_charge": "base_currency_currency_charge",
        "reference": "reference",
        "tax_rate_id": "tax_rate_id",
        "allocated_artefacts": "allocated_artefacts",
        "payment_on_account": "payment_on_account",
    }

    def __init__(
        self,
        transaction_type_id=None,
        contact_id=None,
        bank_account_id=None,
        date=None,
        total_amount=None,
        payment_method_id=None,
        net_amount=None,
        tax_amount=None,
        currency_id=None,
        exchange_rate=None,
        base_currency_net_amount=None,
        base_currency_tax_amount=None,
        base_currency_total_amount=None,
        base_currency_currency_charge=None,
        reference=None,
        tax_rate_id=None,
        allocated_artefacts=None,
        payment_on_account=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._transaction_type_id = None
        self._contact_id = None
        self._bank_account_id = None
        self._date = None
        self._total_amount = None
        self._payment_method_id = None
        self._net_amount = None
        self._tax_amount = None
        self._currency_id = None
        self._exchange_rate = None
        self._base_currency_net_amount = None
        self._base_currency_tax_amount = None
        self._base_currency_total_amount = None
        self._base_currency_currency_charge = None
        self._reference = None
        self._tax_rate_id = None
        self._allocated_artefacts = None
        self._payment_on_account = None
        self.discriminator = None
        self.transaction_type_id = transaction_type_id
        self.contact_id = contact_id
        self.bank_account_id = bank_account_id
        self.date = date
        self.total_amount = total_amount
        if payment_method_id is not None:
            self.payment_method_id = payment_method_id
        if net_amount is not None:
            self.net_amount = net_amount
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
        if base_currency_currency_charge is not None:
            self.base_currency_currency_charge = base_currency_currency_charge
        if reference is not None:
            self.reference = reference
        if tax_rate_id is not None:
            self.tax_rate_id = tax_rate_id
        if allocated_artefacts is not None:
            self.allocated_artefacts = allocated_artefacts
        if payment_on_account is not None:
            self.payment_on_account = payment_on_account

    @property
    def transaction_type_id(self):
        return self._transaction_type_id

    @transaction_type_id.setter
    def transaction_type_id(self, transaction_type_id):
        if (
            self.local_vars_configuration.client_side_validation
            and transaction_type_id is None
        ):
            raise ValueError(
                "Invalid value for `transaction_type_id`, must not be `None`"
            )
        self._transaction_type_id = transaction_type_id

    @property
    def contact_id(self):
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        if self.local_vars_configuration.client_side_validation and contact_id is None:
            raise ValueError("Invalid value for `contact_id`, must not be `None`")
        self._contact_id = contact_id

    @property
    def bank_account_id(self):
        return self._bank_account_id

    @bank_account_id.setter
    def bank_account_id(self, bank_account_id):
        if (
            self.local_vars_configuration.client_side_validation
            and bank_account_id is None
        ):
            raise ValueError("Invalid value for `bank_account_id`, must not be `None`")
        self._bank_account_id = bank_account_id

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if self.local_vars_configuration.client_side_validation and date is None:
            raise ValueError("Invalid value for `date`, must not be `None`")
        self._date = date

    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        if (
            self.local_vars_configuration.client_side_validation
            and total_amount is None
        ):
            raise ValueError("Invalid value for `total_amount`, must not be `None`")
        self._total_amount = total_amount

    @property
    def payment_method_id(self):
        return self._payment_method_id

    @payment_method_id.setter
    def payment_method_id(self, payment_method_id):
        self._payment_method_id = payment_method_id

    @property
    def net_amount(self):
        return self._net_amount

    @net_amount.setter
    def net_amount(self, net_amount):
        self._net_amount = net_amount

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

    @property
    def base_currency_currency_charge(self):
        return self._base_currency_currency_charge

    @base_currency_currency_charge.setter
    def base_currency_currency_charge(self, base_currency_currency_charge):
        self._base_currency_currency_charge = base_currency_currency_charge

    @property
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, reference):
        self._reference = reference

    @property
    def tax_rate_id(self):
        return self._tax_rate_id

    @tax_rate_id.setter
    def tax_rate_id(self, tax_rate_id):
        self._tax_rate_id = tax_rate_id

    @property
    def allocated_artefacts(self):
        return self._allocated_artefacts

    @allocated_artefacts.setter
    def allocated_artefacts(self, allocated_artefacts):
        self._allocated_artefacts = allocated_artefacts

    @property
    def payment_on_account(self):
        return self._payment_on_account

    @payment_on_account.setter
    def payment_on_account(self, payment_on_account):
        self._payment_on_account = payment_on_account

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
        if not isinstance(other, PostContactPaymentsContactPayment):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PostContactPaymentsContactPayment):
            return True
        return self.to_dict() != other.to_dict()
