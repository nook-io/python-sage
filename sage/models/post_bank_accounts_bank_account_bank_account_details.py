import pprint
import six
from sage.configuration import Configuration


class PostBankAccountsBankAccountBankAccountDetails(object):
    openapi_types = {
        "account_name": "str",
        "account_number": "str",
        "sort_code": "str",
        "bic": "str",
        "iban": "str",
    }
    attribute_map = {
        "account_name": "account_name",
        "account_number": "account_number",
        "sort_code": "sort_code",
        "bic": "bic",
        "iban": "iban",
    }

    def __init__(
        self,
        account_name=None,
        account_number=None,
        sort_code=None,
        bic=None,
        iban=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._account_name = None
        self._account_number = None
        self._sort_code = None
        self._bic = None
        self._iban = None
        self.discriminator = None
        self.account_name = account_name
        if account_number is not None:
            self.account_number = account_number
        if sort_code is not None:
            self.sort_code = sort_code
        if bic is not None:
            self.bic = bic
        if iban is not None:
            self.iban = iban

    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        if (
            self.local_vars_configuration.client_side_validation
            and account_name is None
        ):
            raise ValueError("Invalid value for `account_name`, must not be `None`")
        self._account_name = account_name

    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        self._account_number = account_number

    @property
    def sort_code(self):
        return self._sort_code

    @sort_code.setter
    def sort_code(self, sort_code):
        self._sort_code = sort_code

    @property
    def bic(self):
        return self._bic

    @bic.setter
    def bic(self, bic):
        self._bic = bic

    @property
    def iban(self):
        return self._iban

    @iban.setter
    def iban(self, iban):
        self._iban = iban

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
        if not isinstance(other, PostBankAccountsBankAccountBankAccountDetails):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PostBankAccountsBankAccountBankAccountDetails):
            return True
        return self.to_dict() != other.to_dict()
