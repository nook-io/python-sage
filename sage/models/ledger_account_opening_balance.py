import pprint
import six
from sage.configuration import Configuration


class LedgerAccountOpeningBalance(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        "id": "str",
        "displayed_as": "str",
        "path": "str",
        "created_at": "datetime",
        "updated_at": "datetime",
        "ledger_account": "Base",
        "details": "str",
        "debit": "float",
        "credit": "float",
    }
    attribute_map = {
        "id": "id",
        "displayed_as": "displayed_as",
        "path": "$path",
        "created_at": "created_at",
        "updated_at": "updated_at",
        "ledger_account": "ledger_account",
        "details": "details",
        "debit": "debit",
        "credit": "credit",
    }

    def __init__(
        self,
        id=None,
        displayed_as=None,
        path=None,
        created_at=None,
        updated_at=None,
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
        self._displayed_as = None
        self._path = None
        self._created_at = None
        self._updated_at = None
        self._ledger_account = None
        self._details = None
        self._debit = None
        self._credit = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if displayed_as is not None:
            self.displayed_as = displayed_as
        if path is not None:
            self.path = path
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
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
    def displayed_as(self):
        return self._displayed_as

    @displayed_as.setter
    def displayed_as(self, displayed_as):
        self._displayed_as = displayed_as

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path):
        self._path = path

    @property
    def created_at(self):
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        self._created_at = created_at

    @property
    def updated_at(self):
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        self._updated_at = updated_at

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
        if (
            self.local_vars_configuration.client_side_validation
            and details is not None
            and len(details) > 255
        ):
            raise ValueError(
                "Invalid value for `details`, length must be less than or equal to `255`"
            )
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
        if not isinstance(other, LedgerAccountOpeningBalance):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, LedgerAccountOpeningBalance):
            return True
        return self.to_dict() != other.to_dict()
