import pprint
import six
from sage.configuration import Configuration


class PostBankReconciliationsBankReconciliation(object):
    openapi_types = {
        "bank_account_id": "str",
        "statement_date": "date",
        "statement_end_balance": "float",
        "reference": "str",
        "total_received": "float",
        "total_paid": "float",
        "starting_balance": "float",
        "closing_balance": "float",
        "reconciled_balance": "float",
        "balance_difference": "float",
        "status_id": "str",
    }
    attribute_map = {
        "bank_account_id": "bank_account_id",
        "statement_date": "statement_date",
        "statement_end_balance": "statement_end_balance",
        "reference": "reference",
        "total_received": "total_received",
        "total_paid": "total_paid",
        "starting_balance": "starting_balance",
        "closing_balance": "closing_balance",
        "reconciled_balance": "reconciled_balance",
        "balance_difference": "balance_difference",
        "status_id": "status_id",
    }

    def __init__(
        self,
        bank_account_id=None,
        statement_date=None,
        statement_end_balance=None,
        reference=None,
        total_received=None,
        total_paid=None,
        starting_balance=None,
        closing_balance=None,
        reconciled_balance=None,
        balance_difference=None,
        status_id=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._bank_account_id = None
        self._statement_date = None
        self._statement_end_balance = None
        self._reference = None
        self._total_received = None
        self._total_paid = None
        self._starting_balance = None
        self._closing_balance = None
        self._reconciled_balance = None
        self._balance_difference = None
        self._status_id = None
        self.discriminator = None
        self.bank_account_id = bank_account_id
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
        if status_id is not None:
            self.status_id = status_id

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
    def status_id(self):
        return self._status_id

    @status_id.setter
    def status_id(self, status_id):
        self._status_id = status_id

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
        if not isinstance(other, PostBankReconciliationsBankReconciliation):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PostBankReconciliationsBankReconciliation):
            return True
        return self.to_dict() != other.to_dict()
