import pprint
import six
from sage.configuration import Configuration


class PutBankAccounts(object):
    openapi_types = {"bank_account": "PutBankAccountsBankAccount"}
    attribute_map = {"bank_account": "bank_account"}

    def __init__(self, bank_account=None, local_vars_configuration=None):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._bank_account = None
        self.discriminator = None
        self.bank_account = bank_account

    @property
    def bank_account(self):
        return self._bank_account

    @bank_account.setter
    def bank_account(self, bank_account):
        if (
            self.local_vars_configuration.client_side_validation
            and bank_account is None
        ):
            raise ValueError("Invalid value for `bank_account`, must not be `None`")
        self._bank_account = bank_account

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
        if not isinstance(other, PutBankAccounts):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PutBankAccounts):
            return True
        return self.to_dict() != other.to_dict()
