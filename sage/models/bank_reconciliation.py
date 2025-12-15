import pprint
import six
from sage.configuration import Configuration


class BankReconciliation(object):
    openapi_types = {
        "id": "str",
        "displayed_as": "str",
        "path": "str",
        "created_at": "datetime",
        "updated_at": "datetime",
        "bank_account": "Base",
        "statement_date": "date",
        "statement_end_balance": "float",
        "reference": "str",
        "total_received": "float",
        "total_paid": "float",
        "starting_balance": "float",
        "closing_balance": "float",
        "reconciled_balance": "float",
        "balance_difference": "float",
        "status": "BankReconciliationStatus",
    }
    attribute_map = {
        "id": "id",
        "displayed_as": "displayed_as",
        "path": "$path",
        "created_at": "created_at",
        "updated_at": "updated_at",
        "bank_account": "bank_account",
        "statement_date": "statement_date",
        "statement_end_balance": "statement_end_balance",
        "reference": "reference",
        "total_received": "total_received",
        "total_paid": "total_paid",
        "starting_balance": "starting_balance",
        "closing_balance": "closing_balance",
        "reconciled_balance": "reconciled_balance",
        "balance_difference": "balance_difference",
        "status": "status",
    }

    def __init__(
        self,
        id=None,
        displayed_as=None,
        path=None,
        created_at=None,
        updated_at=None,
        bank_account=None,
        statement_date=None,
        statement_end_balance=None,
        reference=None,
        total_received=None,
        total_paid=None,
        starting_balance=None,
        closing_balance=None,
        reconciled_balance=None,
        balance_difference=None,
        status=None,
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
        self._bank_account = None
        self._statement_date = None
        self._statement_end_balance = None
        self._reference = None
        self._total_received = None
        self._total_paid = None
        self._starting_balance = None
        self._closing_balance = None
        self._reconciled_balance = None
        self._balance_difference = None
        self._status = None
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
        if bank_account is not None:
            self.bank_account = bank_account
        if statement_date is not None:
            self.statement_date = statement_date
        if statement_end_balance is not None:
            self.statement_end_balance = statement_end_balance
        if reference is not None:
            self.reference = reference
        if total_received is not None:
            self.total_received = total_received
        if total_paid is not None:
            self.total_paid = total_paid
        if starting_balance is not None:
            self.starting_balance = starting_balance
        if closing_balance is not None:
            self.closing_balance = closing_balance
        if reconciled_balance is not None:
            self.reconciled_balance = reconciled_balance
        if balance_difference is not None:
            self.balance_difference = balance_difference
        if status is not None:
            self.status = status

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
    def bank_account(self):
        return self._bank_account

    @bank_account.setter
    def bank_account(self, bank_account):
        self._bank_account = bank_account

    @property
    def statement_date(self):
        return self._statement_date

    @statement_date.setter
    def statement_date(self, statement_date):
        self._statement_date = statement_date

    @property
    def statement_end_balance(self):
        return self._statement_end_balance

    @statement_end_balance.setter
    def statement_end_balance(self, statement_end_balance):
        self._statement_end_balance = statement_end_balance

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
    def total_received(self):
        return self._total_received

    @total_received.setter
    def total_received(self, total_received):
        self._total_received = total_received

    @property
    def total_paid(self):
        return self._total_paid

    @total_paid.setter
    def total_paid(self, total_paid):
        self._total_paid = total_paid

    @property
    def starting_balance(self):
        return self._starting_balance

    @starting_balance.setter
    def starting_balance(self, starting_balance):
        self._starting_balance = starting_balance

    @property
    def closing_balance(self):
        return self._closing_balance

    @closing_balance.setter
    def closing_balance(self, closing_balance):
        self._closing_balance = closing_balance

    @property
    def reconciled_balance(self):
        return self._reconciled_balance

    @reconciled_balance.setter
    def reconciled_balance(self, reconciled_balance):
        self._reconciled_balance = reconciled_balance

    @property
    def balance_difference(self):
        return self._balance_difference

    @balance_difference.setter
    def balance_difference(self, balance_difference):
        self._balance_difference = balance_difference

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

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
        if not isinstance(other, BankReconciliation):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, BankReconciliation):
            return True
        return self.to_dict() != other.to_dict()
