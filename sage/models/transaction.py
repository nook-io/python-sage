import pprint
import six
from sage.configuration import Configuration


class Transaction(object):
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
        "deleted": "bool",
        "reference": "str",
        "total": "float",
        "total_in_transaction_currency": "float",
        "contact": "Base",
        "transaction_type": "Base",
        "origin": "TransactionOrigin",
        "audit_trail_id": "str",
        "number_of_attachments": "str",
    }
    attribute_map = {
        "id": "id",
        "displayed_as": "displayed_as",
        "path": "$path",
        "created_at": "created_at",
        "updated_at": "updated_at",
        "date": "date",
        "deleted": "deleted",
        "reference": "reference",
        "total": "total",
        "total_in_transaction_currency": "total_in_transaction_currency",
        "contact": "contact",
        "transaction_type": "transaction_type",
        "origin": "origin",
        "audit_trail_id": "audit_trail_id",
        "number_of_attachments": "number_of_attachments",
    }

    def __init__(
        self,
        id=None,
        displayed_as=None,
        path=None,
        created_at=None,
        updated_at=None,
        date=None,
        deleted=None,
        reference=None,
        total=None,
        total_in_transaction_currency=None,
        contact=None,
        transaction_type=None,
        origin=None,
        audit_trail_id=None,
        number_of_attachments=None,
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
        self._deleted = None
        self._reference = None
        self._total = None
        self._total_in_transaction_currency = None
        self._contact = None
        self._transaction_type = None
        self._origin = None
        self._audit_trail_id = None
        self._number_of_attachments = None
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
        if deleted is not None:
            self.deleted = deleted
        if reference is not None:
            self.reference = reference
        if total is not None:
            self.total = total
        if total_in_transaction_currency is not None:
            self.total_in_transaction_currency = total_in_transaction_currency
        if contact is not None:
            self.contact = contact
        if transaction_type is not None:
            self.transaction_type = transaction_type
        if origin is not None:
            self.origin = origin
        if audit_trail_id is not None:
            self.audit_trail_id = audit_trail_id
        if number_of_attachments is not None:
            self.number_of_attachments = number_of_attachments

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
    def deleted(self):
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        self._deleted = deleted

    @property
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, reference):
        if (
            self.local_vars_configuration.client_side_validation
            and reference is not None
            and len(reference) > 255
        ):
            raise ValueError(
                "Invalid value for `reference`, length must be less than or equal to `255`"
            )
        self._reference = reference

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, total):
        self._total = total

    @property
    def total_in_transaction_currency(self):
        return self._total_in_transaction_currency

    @total_in_transaction_currency.setter
    def total_in_transaction_currency(self, total_in_transaction_currency):
        self._total_in_transaction_currency = total_in_transaction_currency

    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, contact):
        self._contact = contact

    @property
    def transaction_type(self):
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        self._transaction_type = transaction_type

    @property
    def origin(self):
        return self._origin

    @origin.setter
    def origin(self, origin):
        self._origin = origin

    @property
    def audit_trail_id(self):
        return self._audit_trail_id

    @audit_trail_id.setter
    def audit_trail_id(self, audit_trail_id):
        self._audit_trail_id = audit_trail_id

    @property
    def number_of_attachments(self):
        return self._number_of_attachments

    @number_of_attachments.setter
    def number_of_attachments(self, number_of_attachments):
        self._number_of_attachments = number_of_attachments

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
        if not isinstance(other, Transaction):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, Transaction):
            return True
        return self.to_dict() != other.to_dict()
