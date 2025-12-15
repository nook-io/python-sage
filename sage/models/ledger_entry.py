import pprint
import six
from sage.configuration import Configuration


class LedgerEntry(object):
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
        "date": "date",
        "credit": "float",
        "debit": "float",
        "ledger_account": "LedgerAccount",
        "transaction": "Transaction",
        "contact": "Contact",
        "deleted": "bool",
        "tax_rate": "TaxRate",
        "description": "str",
        "journal_code": "JournalCode",
    }
    attribute_map = {
        "id": "id",
        "displayed_as": "displayed_as",
        "path": "$path",
        "created_at": "created_at",
        "updated_at": "updated_at",
        "date": "date",
        "credit": "credit",
        "debit": "debit",
        "ledger_account": "ledger_account",
        "transaction": "transaction",
        "contact": "contact",
        "deleted": "deleted",
        "tax_rate": "tax_rate",
        "description": "description",
        "journal_code": "journal_code",
    }

    def __init__(
        self,
        id=None,
        displayed_as=None,
        path=None,
        created_at=None,
        updated_at=None,
        date=None,
        credit=None,
        debit=None,
        ledger_account=None,
        transaction=None,
        contact=None,
        deleted=None,
        tax_rate=None,
        description=None,
        journal_code=None,
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
        self._date = None
        self._credit = None
        self._debit = None
        self._ledger_account = None
        self._transaction = None
        self._contact = None
        self._deleted = None
        self._tax_rate = None
        self._description = None
        self._journal_code = None
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
        if date is not None:
            self.date = date
        if credit is not None:
            self.credit = credit
        if debit is not None:
            self.debit = debit
        if ledger_account is not None:
            self.ledger_account = ledger_account
        if transaction is not None:
            self.transaction = transaction
        if contact is not None:
            self.contact = contact
        if deleted is not None:
            self.deleted = deleted
        if tax_rate is not None:
            self.tax_rate = tax_rate
        if description is not None:
            self.description = description
        if journal_code is not None:
            self.journal_code = journal_code

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
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

    @property
    def credit(self):
        return self._credit

    @credit.setter
    def credit(self, credit):
        self._credit = credit

    @property
    def debit(self):
        return self._debit

    @debit.setter
    def debit(self, debit):
        self._debit = debit

    @property
    def ledger_account(self):
        return self._ledger_account

    @ledger_account.setter
    def ledger_account(self, ledger_account):
        self._ledger_account = ledger_account

    @property
    def transaction(self):
        return self._transaction

    @transaction.setter
    def transaction(self, transaction):
        self._transaction = transaction

    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, contact):
        self._contact = contact

    @property
    def deleted(self):
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        self._deleted = deleted

    @property
    def tax_rate(self):
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, tax_rate):
        self._tax_rate = tax_rate

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def journal_code(self):
        return self._journal_code

    @journal_code.setter
    def journal_code(self, journal_code):
        self._journal_code = journal_code

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
        if not isinstance(other, LedgerEntry):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, LedgerEntry):
            return True
        return self.to_dict() != other.to_dict()
