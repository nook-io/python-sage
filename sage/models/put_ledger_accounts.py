import pprint
import six
from sage.configuration import Configuration


class PutLedgerAccounts(object):
    openapi_types = {"ledger_account": "PutLedgerAccountsLedgerAccount"}
    attribute_map = {"ledger_account": "ledger_account"}

    def __init__(self, ledger_account=None, local_vars_configuration=None):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._ledger_account = None
        self.discriminator = None
        self.ledger_account = ledger_account

    @property
    def ledger_account(self):
        return self._ledger_account

    @ledger_account.setter
    def ledger_account(self, ledger_account):
        if (
            self.local_vars_configuration.client_side_validation
            and ledger_account is None
        ):
            raise ValueError("Invalid value for `ledger_account`, must not be `None`")
        self._ledger_account = ledger_account

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
        if not isinstance(other, PutLedgerAccounts):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PutLedgerAccounts):
            return True
        return self.to_dict() != other.to_dict()
