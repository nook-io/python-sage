import pprint
import six
from sage.configuration import Configuration


class BankDeposit(object):
    openapi_types = {
        "id": "str",
        "displayed_as": "str",
        "path": "str",
        "created_at": "datetime",
        "updated_at": "datetime",
        "transaction": "Base",
        "transaction_type": "Base",
        "deleted_at": "datetime",
        "from_bank_account": "BankAccount",
        "to_bank_account": "BankAccount",
        "date": "date",
        "reference": "str",
        "cash_amount": "float",
        "cheque_amount": "float",
        "total_amount": "float",
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
        "from_bank_account": "from_bank_account",
        "to_bank_account": "to_bank_account",
        "date": "date",
        "reference": "reference",
        "cash_amount": "cash_amount",
        "cheque_amount": "cheque_amount",
        "total_amount": "total_amount",
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
        from_bank_account=None,
        to_bank_account=None,
        date=None,
        reference=None,
        cash_amount=None,
        cheque_amount=None,
        total_amount=None,
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
        self._from_bank_account = None
        self._to_bank_account = None
        self._date = None
        self._reference = None
        self._cash_amount = None
        self._cheque_amount = None
        self._total_amount = None
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
        if from_bank_account is not None:
            self.from_bank_account = from_bank_account
        if to_bank_account is not None:
            self.to_bank_account = to_bank_account
        if date is not None:
            self.date = date
        if reference is not None:
            self.reference = reference
        if cash_amount is not None:
            self.cash_amount = cash_amount
        if cheque_amount is not None:
            self.cheque_amount = cheque_amount
        if total_amount is not None:
            self.total_amount = total_amount

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
    def from_bank_account(self):
        return self._from_bank_account

    @from_bank_account.setter
    def from_bank_account(self, from_bank_account):
        self._from_bank_account = from_bank_account

    @property
    def to_bank_account(self):
        return self._to_bank_account

    @to_bank_account.setter
    def to_bank_account(self, to_bank_account):
        self._to_bank_account = to_bank_account

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
            and len(reference) > 255
        ):
            raise ValueError(
                "Invalid value for `reference`, length must be less than or equal to `255`"
            )
        self._reference = reference

    @property
    def cash_amount(self):
        return self._cash_amount

    @cash_amount.setter
    def cash_amount(self, cash_amount):
        self._cash_amount = cash_amount

    @property
    def cheque_amount(self):
        return self._cheque_amount

    @cheque_amount.setter
    def cheque_amount(self, cheque_amount):
        self._cheque_amount = cheque_amount

    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        self._total_amount = total_amount

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
        if not isinstance(other, BankDeposit):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, BankDeposit):
            return True
        return self.to_dict() != other.to_dict()
