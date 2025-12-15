import pprint
import six
from sage.configuration import Configuration


class OtherPayment(object):
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
        "transaction": "Base",
        "transaction_type": "Base",
        "deleted_at": "datetime",
        "base_currency_total_itc_amount": "float",
        "total_itc_amount": "float",
        "base_currency_total_itr_amount": "float",
        "total_itr_amount": "float",
        "part_recoverable": "bool",
        "payment_method": "Base",
        "contact": "Base",
        "bank_account": "Base",
        "tax_address_region": "Base",
        "date": "date",
        "net_amount": "float",
        "tax_amount": "float",
        "total_amount": "float",
        "reference": "str",
        "payment_lines": "list[OtherPaymentLineItem]",
        "editable": "bool",
        "deletable": "bool",
        "withholding_tax_rate": "float",
        "withholding_tax_amount": "float",
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
        "base_currency_total_itc_amount": "base_currency_total_itc_amount",
        "total_itc_amount": "total_itc_amount",
        "base_currency_total_itr_amount": "base_currency_total_itr_amount",
        "total_itr_amount": "total_itr_amount",
        "part_recoverable": "part_recoverable",
        "payment_method": "payment_method",
        "contact": "contact",
        "bank_account": "bank_account",
        "tax_address_region": "tax_address_region",
        "date": "date",
        "net_amount": "net_amount",
        "tax_amount": "tax_amount",
        "total_amount": "total_amount",
        "reference": "reference",
        "payment_lines": "payment_lines",
        "editable": "editable",
        "deletable": "deletable",
        "withholding_tax_rate": "withholding_tax_rate",
        "withholding_tax_amount": "withholding_tax_amount",
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
        base_currency_total_itc_amount=None,
        total_itc_amount=None,
        base_currency_total_itr_amount=None,
        total_itr_amount=None,
        part_recoverable=None,
        payment_method=None,
        contact=None,
        bank_account=None,
        tax_address_region=None,
        date=None,
        net_amount=None,
        tax_amount=None,
        total_amount=None,
        reference=None,
        payment_lines=None,
        editable=None,
        deletable=None,
        withholding_tax_rate=None,
        withholding_tax_amount=None,
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
        self._base_currency_total_itc_amount = None
        self._total_itc_amount = None
        self._base_currency_total_itr_amount = None
        self._total_itr_amount = None
        self._part_recoverable = None
        self._payment_method = None
        self._contact = None
        self._bank_account = None
        self._tax_address_region = None
        self._date = None
        self._net_amount = None
        self._tax_amount = None
        self._total_amount = None
        self._reference = None
        self._payment_lines = None
        self._editable = None
        self._deletable = None
        self._withholding_tax_rate = None
        self._withholding_tax_amount = None
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
        if payment_method is not None:
            self.payment_method = payment_method
        if contact is not None:
            self.contact = contact
        if bank_account is not None:
            self.bank_account = bank_account
        if tax_address_region is not None:
            self.tax_address_region = tax_address_region
        if date is not None:
            self.date = date
        if net_amount is not None:
            self.net_amount = net_amount
        if tax_amount is not None:
            self.tax_amount = tax_amount
        if total_amount is not None:
            self.total_amount = total_amount
        if reference is not None:
            self.reference = reference
        if payment_lines is not None:
            self.payment_lines = payment_lines
        if editable is not None:
            self.editable = editable
        if deletable is not None:
            self.deletable = deletable
        if withholding_tax_rate is not None:
            self.withholding_tax_rate = withholding_tax_rate
        if withholding_tax_amount is not None:
            self.withholding_tax_amount = withholding_tax_amount

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
    def payment_method(self):
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        self._payment_method = payment_method

    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, contact):
        self._contact = contact

    @property
    def bank_account(self):
        return self._bank_account

    @bank_account.setter
    def bank_account(self, bank_account):
        self._bank_account = bank_account

    @property
    def tax_address_region(self):
        return self._tax_address_region

    @tax_address_region.setter
    def tax_address_region(self, tax_address_region):
        self._tax_address_region = tax_address_region

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

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
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        self._total_amount = total_amount

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
    def payment_lines(self):
        return self._payment_lines

    @payment_lines.setter
    def payment_lines(self, payment_lines):
        self._payment_lines = payment_lines

    @property
    def editable(self):
        return self._editable

    @editable.setter
    def editable(self, editable):
        self._editable = editable

    @property
    def deletable(self):
        return self._deletable

    @deletable.setter
    def deletable(self, deletable):
        self._deletable = deletable

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
        if not isinstance(other, OtherPayment):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, OtherPayment):
            return True
        return self.to_dict() != other.to_dict()
