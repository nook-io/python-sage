import pprint
import six
from sage.configuration import Configuration


class PostBankTransfersBankTransfer(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        "from_bank_account_id": "str",
        "to_bank_account_id": "str",
        "date": "date",
        "amount": "float",
        "reference": "str",
        "description": "str",
    }
    attribute_map = {
        "from_bank_account_id": "from_bank_account_id",
        "to_bank_account_id": "to_bank_account_id",
        "date": "date",
        "amount": "amount",
        "reference": "reference",
        "description": "description",
    }

    def __init__(
        self,
        from_bank_account_id=None,
        to_bank_account_id=None,
        date=None,
        amount=None,
        reference=None,
        description=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._from_bank_account_id = None
        self._to_bank_account_id = None
        self._date = None
        self._amount = None
        self._reference = None
        self._description = None
        self.discriminator = None
        self.from_bank_account_id = from_bank_account_id
        self.to_bank_account_id = to_bank_account_id
        self.date = date
        self.amount = amount
        if reference is not None:
            self.reference = reference
        if description is not None:
            self.description = description

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
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        if self.local_vars_configuration.client_side_validation and amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")
        self._amount = amount

    @property
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, reference):
        self._reference = reference

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

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
        if not isinstance(other, PostBankTransfersBankTransfer):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PostBankTransfersBankTransfer):
            return True
        return self.to_dict() != other.to_dict()
