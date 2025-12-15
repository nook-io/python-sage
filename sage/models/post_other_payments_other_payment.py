import pprint
import six
from sage.configuration import Configuration


class PostOtherPaymentsOtherPayment(object):
    openapi_types = {
        "transaction_type_id": "str",
        "date": "date",
        "total_amount": "float",
        "base_currency_total_itc_amount": "float",
        "total_itc_amount": "float",
        "base_currency_total_itr_amount": "float",
        "total_itr_amount": "float",
        "part_recoverable": "bool",
        "payment_method_id": "str",
        "contact_id": "str",
        "bank_account_id": "str",
        "tax_address_region_id": "str",
        "net_amount": "float",
        "tax_amount": "float",
        "reference": "str",
        "withholding_tax_rate": "float",
        "withholding_tax_amount": "float",
        "payment_lines": "list[PostOtherPaymentsOtherPaymentPaymentLines]",
    }
    attribute_map = {
        "transaction_type_id": "transaction_type_id",
        "date": "date",
        "total_amount": "total_amount",
        "base_currency_total_itc_amount": "base_currency_total_itc_amount",
        "total_itc_amount": "total_itc_amount",
        "base_currency_total_itr_amount": "base_currency_total_itr_amount",
        "total_itr_amount": "total_itr_amount",
        "part_recoverable": "part_recoverable",
        "payment_method_id": "payment_method_id",
        "contact_id": "contact_id",
        "bank_account_id": "bank_account_id",
        "tax_address_region_id": "tax_address_region_id",
        "net_amount": "net_amount",
        "tax_amount": "tax_amount",
        "reference": "reference",
        "withholding_tax_rate": "withholding_tax_rate",
        "withholding_tax_amount": "withholding_tax_amount",
        "payment_lines": "payment_lines",
    }

    def __init__(
        self,
        transaction_type_id=None,
        date=None,
        total_amount=None,
        base_currency_total_itc_amount=None,
        total_itc_amount=None,
        base_currency_total_itr_amount=None,
        total_itr_amount=None,
        part_recoverable=None,
        payment_method_id=None,
        contact_id=None,
        bank_account_id=None,
        tax_address_region_id=None,
        net_amount=None,
        tax_amount=None,
        reference=None,
        withholding_tax_rate=None,
        withholding_tax_amount=None,
        payment_lines=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._transaction_type_id = None
        self._date = None
        self._total_amount = None
        self._base_currency_total_itc_amount = None
        self._total_itc_amount = None
        self._base_currency_total_itr_amount = None
        self._total_itr_amount = None
        self._part_recoverable = None
        self._payment_method_id = None
        self._contact_id = None
        self._bank_account_id = None
        self._tax_address_region_id = None
        self._net_amount = None
        self._tax_amount = None
        self._reference = None
        self._withholding_tax_rate = None
        self._withholding_tax_amount = None
        self._payment_lines = None
        self.discriminator = None
        self.transaction_type_id = transaction_type_id
        self.date = date
        self.total_amount = total_amount
        if base_currency_total_itc_amount is not None:
            self.base_currency_total_itc_amount = base_currency_total_itc_amount
        if total_itc_amount is not None:
            self.total_itc_amount = total_itc_amount
        if base_currency_total_itr_amount is not None:
            self.base_currency_total_itr_amount = base_currency_total_itr_amount
        if total_itr_amount is not None:
            self.total_itr_amount = total_itr_amount
        if part_recoverable is not None:
            self.part_recoverable = part_recoverable
        if payment_method_id is not None:
            self.payment_method_id = payment_method_id
        if contact_id is not None:
            self.contact_id = contact_id
        if bank_account_id is not None:
            self.bank_account_id = bank_account_id
        if tax_address_region_id is not None:
            self.tax_address_region_id = tax_address_region_id
        if net_amount is not None:
            self.net_amount = net_amount
        if tax_amount is not None:
            self.tax_amount = tax_amount
        if reference is not None:
            self.reference = reference
        if withholding_tax_rate is not None:
            self.withholding_tax_rate = withholding_tax_rate
        if withholding_tax_amount is not None:
            self.withholding_tax_amount = withholding_tax_amount
        self.payment_lines = payment_lines

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
    def base_currency_total_itc_amount(self):
        return self._base_currency_total_itc_amount

    @base_currency_total_itc_amount.setter
    def base_currency_total_itc_amount(self, base_currency_total_itc_amount):
        self._base_currency_total_itc_amount = base_currency_total_itc_amount

    @property
    def total_itc_amount(self):
        return self._total_itc_amount

    @total_itc_amount.setter
    def total_itc_amount(self, total_itc_amount):
        self._total_itc_amount = total_itc_amount

    @property
    def base_currency_total_itr_amount(self):
        return self._base_currency_total_itr_amount

    @base_currency_total_itr_amount.setter
    def base_currency_total_itr_amount(self, base_currency_total_itr_amount):
        self._base_currency_total_itr_amount = base_currency_total_itr_amount

    @property
    def total_itr_amount(self):
        return self._total_itr_amount

    @total_itr_amount.setter
    def total_itr_amount(self, total_itr_amount):
        self._total_itr_amount = total_itr_amount

    @property
    def part_recoverable(self):
        return self._part_recoverable

    @part_recoverable.setter
    def part_recoverable(self, part_recoverable):
        self._part_recoverable = part_recoverable

    @property
    def payment_method_id(self):
        return self._payment_method_id

    @payment_method_id.setter
    def payment_method_id(self, payment_method_id):
        self._payment_method_id = payment_method_id

    @property
    def contact_id(self):
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        self._contact_id = contact_id

    @property
    def bank_account_id(self):
        return self._bank_account_id

    @bank_account_id.setter
    def bank_account_id(self, bank_account_id):
        self._bank_account_id = bank_account_id

    @property
    def tax_address_region_id(self):
        return self._tax_address_region_id

    @tax_address_region_id.setter
    def tax_address_region_id(self, tax_address_region_id):
        self._tax_address_region_id = tax_address_region_id

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
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, reference):
        self._reference = reference

    @property
    def withholding_tax_rate(self):
        return self._withholding_tax_rate

    @withholding_tax_rate.setter
    def withholding_tax_rate(self, withholding_tax_rate):
        self._withholding_tax_rate = withholding_tax_rate

    @property
    def withholding_tax_amount(self):
        return self._withholding_tax_amount

    @withholding_tax_amount.setter
    def withholding_tax_amount(self, withholding_tax_amount):
        self._withholding_tax_amount = withholding_tax_amount

    @property
    def payment_lines(self):
        return self._payment_lines

    @payment_lines.setter
    def payment_lines(self, payment_lines):
        if (
            self.local_vars_configuration.client_side_validation
            and payment_lines is None
        ):
            raise ValueError("Invalid value for `payment_lines`, must not be `None`")
        self._payment_lines = payment_lines

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
        if not isinstance(other, PostOtherPaymentsOtherPayment):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PostOtherPaymentsOtherPayment):
            return True
        return self.to_dict() != other.to_dict()
