import pprint
import six
from sage.configuration import Configuration


class PutLedgerAccountOpeningBalancesLedgerAccountOpeningBalance(object):
    openapi_types = {
        "ledger_account_id": "str",
        "debit": "float",
        "credit": "float",
        "details": "str",
    }
    attribute_map = {
        "ledger_account_id": "ledger_account_id",
        "debit": "debit",
        "credit": "credit",
        "details": "details",
    }

    def __init__(
        self,
        ledger_account_id=None,
        debit=None,
        credit=None,
        details=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._ledger_account_id = None
        self._debit = None
        self._credit = None
        self._details = None
        self.discriminator = None
        if ledger_account_id is not None:
            self.ledger_account_id = ledger_account_id
        if debit is not None:
            self.debit = debit
        if credit is not None:
            self.credit = credit
        if details is not None:
            self.details = details

    @property
    def ledger_account_id(self):
        return self._ledger_account_id

    @ledger_account_id.setter
    def ledger_account_id(self, ledger_account_id):
        self._ledger_account_id = ledger_account_id

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

    @property
    def details(self):
        return self._details

    @details.setter
    def details(self, details):
        self._details = details

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
        if not isinstance(
            other, PutLedgerAccountOpeningBalancesLedgerAccountOpeningBalance
        ):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(
            other, PutLedgerAccountOpeningBalancesLedgerAccountOpeningBalance
        ):
            return True
        return self.to_dict() != other.to_dict()
