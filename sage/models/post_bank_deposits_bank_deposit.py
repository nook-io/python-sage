import pprint
import six
from sage.configuration import Configuration


class PostBankDepositsBankDeposit(object):
    openapi_types = {
        "from_bank_account_id": "str",
        "to_bank_account_id": "str",
        "date": "date",
        "reference": "str",
        "cash_amount": "float",
        "cheque_amount": "float",
        "total_amount": "float",
    }
    attribute_map = {
        "from_bank_account_id": "from_bank_account_id",
        "to_bank_account_id": "to_bank_account_id",
        "date": "date",
        "reference": "reference",
        "cash_amount": "cash_amount",
        "cheque_amount": "cheque_amount",
        "total_amount": "total_amount",
    }

    def __init__(
        self,
        from_bank_account_id=None,
        to_bank_account_id=None,
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
        self._from_bank_account_id = None
        self._to_bank_account_id = None
        self._date = None
        self._reference = None
        self._cash_amount = None
        self._cheque_amount = None
        self._total_amount = None
        self.discriminator = None
        self.from_bank_account_id = from_bank_account_id
        self.to_bank_account_id = to_bank_account_id
        self.date = date
        self.reference = reference
        self.cash_amount = cash_amount
        if cheque_amount is not None:
            self.cheque_amount = cheque_amount
        if total_amount is not None:
            self.total_amount = total_amount

    @property
    def from_bank_account_id(self):
        return self._from_bank_account_id

    @from_bank_account_id.setter
    def from_bank_account_id(self, from_bank_account_id):
        if (
            self.local_vars_configuration.client_side_validation
            and from_bank_account_id is None
        ):
            raise ValueError(
                "Invalid value for `from_bank_account_id`, must not be `None`"
            )
        self._from_bank_account_id = from_bank_account_id

    @property
    def to_bank_account_id(self):
        return self._to_bank_account_id

    @to_bank_account_id.setter
    def to_bank_account_id(self, to_bank_account_id):
        if (
            self.local_vars_configuration.client_side_validation
            and to_bank_account_id is None
        ):
            raise ValueError(
                "Invalid value for `to_bank_account_id`, must not be `None`"
            )
        self._to_bank_account_id = to_bank_account_id

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if self.local_vars_configuration.client_side_validation and date is None:
            raise ValueError("Invalid value for `date`, must not be `None`")
        self._date = date

    @property
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, reference):
        if self.local_vars_configuration.client_side_validation and reference is None:
            raise ValueError("Invalid value for `reference`, must not be `None`")
        self._reference = reference

    @property
    def cash_amount(self):
        return self._cash_amount

    @cash_amount.setter
    def cash_amount(self, cash_amount):
        if self.local_vars_configuration.client_side_validation and cash_amount is None:
            raise ValueError("Invalid value for `cash_amount`, must not be `None`")
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
        if not isinstance(other, PostBankDepositsBankDeposit):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PostBankDepositsBankDeposit):
            return True
        return self.to_dict() != other.to_dict()
