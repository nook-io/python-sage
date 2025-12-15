import pprint
import six
from sage.configuration import Configuration


class PostBankOpeningBalancesBankOpeningBalance(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        "bank_account_id": "str",
        "date": "date",
        "debit": "float",
        "credit": "float",
        "transaction_type_id": "str",
    }
    attribute_map = {
        "bank_account_id": "bank_account_id",
        "date": "date",
        "debit": "debit",
        "credit": "credit",
        "transaction_type_id": "transaction_type_id",
    }

    def __init__(
        self,
        bank_account_id=None,
        date=None,
        debit=None,
        credit=None,
        transaction_type_id=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._bank_account_id = None
        self._date = None
        self._debit = None
        self._credit = None
        self._transaction_type_id = None
        self.discriminator = None
        self.bank_account_id = bank_account_id
        self.date = date
        self.debit = debit
        self.credit = credit
        if transaction_type_id is not None:
            self.transaction_type_id = transaction_type_id

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
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if self.local_vars_configuration.client_side_validation and date is None:
            raise ValueError("Invalid value for `date`, must not be `None`")
        self._date = date

    @property
    def debit(self):
        return self._debit

    @debit.setter
    def debit(self, debit):
        if self.local_vars_configuration.client_side_validation and debit is None:
            raise ValueError("Invalid value for `debit`, must not be `None`")
        self._debit = debit

    @property
    def credit(self):
        return self._credit

    @credit.setter
    def credit(self, credit):
        if self.local_vars_configuration.client_side_validation and credit is None:
            raise ValueError("Invalid value for `credit`, must not be `None`")
        self._credit = credit

    @property
    def transaction_type_id(self):
        return self._transaction_type_id

    @transaction_type_id.setter
    def transaction_type_id(self, transaction_type_id):
        self._transaction_type_id = transaction_type_id

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
        if not isinstance(other, PostBankOpeningBalancesBankOpeningBalance):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PostBankOpeningBalancesBankOpeningBalance):
            return True
        return self.to_dict() != other.to_dict()
