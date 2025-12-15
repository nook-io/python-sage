import pprint
import six
from sage.configuration import Configuration


class TransactionOrigin(object):
    openapi_types = {
        "id": "str",
        "displayed_as": "str",
        "path": "str",
        "links": "list[Link]",
        "due_date": "date",
        "outstanding_amount": "float",
        "currency": "Base",
        "status": "Base",
        "sent": "bool",
    }
    attribute_map = {
        "id": "id",
        "displayed_as": "displayed_as",
        "path": "$path",
        "links": "links",
        "due_date": "due_date",
        "outstanding_amount": "outstanding_amount",
        "currency": "currency",
        "status": "status",
        "sent": "sent",
    }

    def __init__(
        self,
        id=None,
        displayed_as=None,
        path=None,
        links=None,
        due_date=None,
        outstanding_amount=None,
        currency=None,
        status=None,
        sent=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._id = None
        self._displayed_as = None
        self._path = None
        self._links = None
        self._due_date = None
        self._outstanding_amount = None
        self._currency = None
        self._status = None
        self._sent = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if displayed_as is not None:
            self.displayed_as = displayed_as
        if path is not None:
            self.path = path
        if links is not None:
            self.links = links
        if due_date is not None:
            self.due_date = due_date
        if outstanding_amount is not None:
            self.outstanding_amount = outstanding_amount
        if currency is not None:
            self.currency = currency
        if status is not None:
            self.status = status
        if sent is not None:
            self.sent = sent

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
    def links(self):
        return self._links

    @links.setter
    def links(self, links):
        self._links = links

    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        self._due_date = due_date

    @property
    def outstanding_amount(self):
        return self._outstanding_amount

    @outstanding_amount.setter
    def outstanding_amount(self, outstanding_amount):
        self._outstanding_amount = outstanding_amount

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, currency):
        self._currency = currency

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def sent(self):
        return self._sent

    @sent.setter
    def sent(self, sent):
        self._sent = sent

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
        if not isinstance(other, TransactionOrigin):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, TransactionOrigin):
            return True
        return self.to_dict() != other.to_dict()
