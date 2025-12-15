import pprint
import six
from sage.configuration import Configuration


class LedgerAccountBalanceDetails(object):
    openapi_types = {
        "balance": "float",
        "credit_or_debit": "str",
        "credits": "float",
        "debits": "float",
        "from_date": "str",
        "to_date": "str",
    }
    attribute_map = {
        "balance": "balance",
        "credit_or_debit": "credit_or_debit",
        "credits": "credits",
        "debits": "debits",
        "from_date": "from_date",
        "to_date": "to_date",
    }

    def __init__(
        self,
        balance=None,
        credit_or_debit=None,
        credits=None,
        debits=None,
        from_date=None,
        to_date=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._balance = None
        self._credit_or_debit = None
        self._credits = None
        self._debits = None
        self._from_date = None
        self._to_date = None
        self.discriminator = None
        if balance is not None:
            self.balance = balance
        if credit_or_debit is not None:
            self.credit_or_debit = credit_or_debit
        if credits is not None:
            self.credits = credits
        if debits is not None:
            self.debits = debits
        if from_date is not None:
            self.from_date = from_date
        if to_date is not None:
            self.to_date = to_date

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        self._balance = balance

    @property
    def credit_or_debit(self):
        return self._credit_or_debit

    @credit_or_debit.setter
    def credit_or_debit(self, credit_or_debit):
        self._credit_or_debit = credit_or_debit

    @property
    def credits(self):
        return self._credits

    @credits.setter
    def credits(self, credits):
        self._credits = credits

    @property
    def debits(self):
        return self._debits

    @debits.setter
    def debits(self, debits):
        self._debits = debits

    @property
    def from_date(self):
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        self._from_date = from_date

    @property
    def to_date(self):
        return self._to_date

    @to_date.setter
    def to_date(self, to_date):
        self._to_date = to_date

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
        if not isinstance(other, LedgerAccountBalanceDetails):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, LedgerAccountBalanceDetails):
            return True
        return self.to_dict() != other.to_dict()
