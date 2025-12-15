import pprint
import six
from sage.configuration import Configuration


class BaseJournalLine(object):
    openapi_types = {
        "id": "str",
        "ledger_account": "LedgerAccount",
        "details": "str",
        "debit": "float",
        "credit": "float",
    }
    attribute_map = {
        "id": "id",
        "ledger_account": "ledger_account",
        "details": "details",
        "debit": "debit",
        "credit": "credit",
    }

    def __init__(
        self,
        id=None,
        ledger_account=None,
        details=None,
        debit=None,
        credit=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._id = None
        self._ledger_account = None
        self._details = None
        self._debit = None
        self._credit = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if ledger_account is not None:
            self.ledger_account = ledger_account
        if details is not None:
            self.details = details
        if debit is not None:
            self.debit = debit
        if credit is not None:
            self.credit = credit

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

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
        self._details = details

    @property
    def debit(self):
        return self._debit

    @debit.setter
    def debit(self, debit):
        self._debit = debit

    @property
    def credit(self):
        return self._credit

    @credit.setter
    def credit(self, credit):
        self._credit = credit

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
        if not isinstance(other, BaseJournalLine):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, BaseJournalLine):
            return True
        return self.to_dict() != other.to_dict()
