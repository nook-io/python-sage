import pprint
import six
from sage.configuration import Configuration


class BankAccountPush(object):
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
        "deleted_at": "datetime",
        "bank_account_details": "BankAccountDetails",
        "ledger_account_id": "str",
        "bank_account_type_id": "str",
        "balance": "float",
        "main_address": "Address",
        "main_contact_person": "BankAccountContact",
        "nominal_code": "int",
        "editable": "bool",
        "deletable": "bool",
        "journal_code": "JournalCode",
        "default_payment_method_id": "str",
        "gifi_code": "int",
    }
    attribute_map = {
        "id": "id",
        "displayed_as": "displayed_as",
        "path": "$path",
        "created_at": "created_at",
        "updated_at": "updated_at",
        "deleted_at": "deleted_at",
        "bank_account_details": "bank_account_details",
        "ledger_account_id": "ledger_account_id",
        "bank_account_type_id": "bank_account_type_id",
        "balance": "balance",
        "main_address": "main_address",
        "main_contact_person": "main_contact_person",
        "nominal_code": "nominal_code",
        "editable": "editable",
        "deletable": "deletable",
        "journal_code": "journal_code",
        "default_payment_method_id": "default_payment_method_id",
        "gifi_code": "gifi_code",
    }

    def __init__(
        self,
        id=None,
        displayed_as=None,
        path=None,
        created_at=None,
        updated_at=None,
        deleted_at=None,
        bank_account_details=None,
        ledger_account_id=None,
        bank_account_type_id=None,
        balance=None,
        main_address=None,
        main_contact_person=None,
        nominal_code=None,
        editable=None,
        deletable=None,
        journal_code=None,
        default_payment_method_id=None,
        gifi_code=None,
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
        self._deleted_at = None
        self._bank_account_details = None
        self._ledger_account_id = None
        self._bank_account_type_id = None
        self._balance = None
        self._main_address = None
        self._main_contact_person = None
        self._nominal_code = None
        self._editable = None
        self._deletable = None
        self._journal_code = None
        self._default_payment_method_id = None
        self._gifi_code = None
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
        if deleted_at is not None:
            self.deleted_at = deleted_at
        if bank_account_details is not None:
            self.bank_account_details = bank_account_details
        if ledger_account_id is not None:
            self.ledger_account_id = ledger_account_id
        if bank_account_type_id is not None:
            self.bank_account_type_id = bank_account_type_id
        if balance is not None:
            self.balance = balance
        if main_address is not None:
            self.main_address = main_address
        if main_contact_person is not None:
            self.main_contact_person = main_contact_person
        if nominal_code is not None:
            self.nominal_code = nominal_code
        if editable is not None:
            self.editable = editable
        if deletable is not None:
            self.deletable = deletable
        if journal_code is not None:
            self.journal_code = journal_code
        if default_payment_method_id is not None:
            self.default_payment_method_id = default_payment_method_id
        if gifi_code is not None:
            self.gifi_code = gifi_code

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
    def deleted_at(self):
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        self._deleted_at = deleted_at

    @property
    def bank_account_details(self):
        return self._bank_account_details

    @bank_account_details.setter
    def bank_account_details(self, bank_account_details):
        self._bank_account_details = bank_account_details

    @property
    def ledger_account_id(self):
        return self._ledger_account_id

    @ledger_account_id.setter
    def ledger_account_id(self, ledger_account_id):
        self._ledger_account_id = ledger_account_id

    @property
    def bank_account_type_id(self):
        return self._bank_account_type_id

    @bank_account_type_id.setter
    def bank_account_type_id(self, bank_account_type_id):
        self._bank_account_type_id = bank_account_type_id

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        self._balance = balance

    @property
    def main_address(self):
        return self._main_address

    @main_address.setter
    def main_address(self, main_address):
        self._main_address = main_address

    @property
    def main_contact_person(self):
        return self._main_contact_person

    @main_contact_person.setter
    def main_contact_person(self, main_contact_person):
        self._main_contact_person = main_contact_person

    @property
    def nominal_code(self):
        return self._nominal_code

    @nominal_code.setter
    def nominal_code(self, nominal_code):
        self._nominal_code = nominal_code

    @property
    def editable(self):
        return self._editable

    @editable.setter
    def editable(self, editable):
        self._editable = editable

    @property
    def deletable(self):
        return self._deletable

    @deletable.setter
    def deletable(self, deletable):
        self._deletable = deletable

    @property
    def journal_code(self):
        return self._journal_code

    @journal_code.setter
    def journal_code(self, journal_code):
        self._journal_code = journal_code

    @property
    def default_payment_method_id(self):
        return self._default_payment_method_id

    @default_payment_method_id.setter
    def default_payment_method_id(self, default_payment_method_id):
        self._default_payment_method_id = default_payment_method_id

    @property
    def gifi_code(self):
        return self._gifi_code

    @gifi_code.setter
    def gifi_code(self, gifi_code):
        self._gifi_code = gifi_code

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
        if not isinstance(other, BankAccount):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, BankAccount):
            return True
        return self.to_dict() != other.to_dict()
