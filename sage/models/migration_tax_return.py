import pprint
import six
from sage.configuration import Configuration


class MigrationTaxReturn(object):
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
        "from_date": "date",
        "to_date": "date",
        "tax_return_frequency": "Base",
        "total_amount": "float",
        "gb": "GBBoxData",
        "ie": "IEBoxData",
    }
    attribute_map = {
        "id": "id",
        "displayed_as": "displayed_as",
        "path": "$path",
        "created_at": "created_at",
        "updated_at": "updated_at",
        "from_date": "from_date",
        "to_date": "to_date",
        "tax_return_frequency": "tax_return_frequency",
        "total_amount": "total_amount",
        "gb": "gb",
        "ie": "ie",
    }

    def __init__(
        self,
        id=None,
        displayed_as=None,
        path=None,
        created_at=None,
        updated_at=None,
        from_date=None,
        to_date=None,
        tax_return_frequency=None,
        total_amount=None,
        gb=None,
        ie=None,
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
        self._from_date = None
        self._to_date = None
        self._tax_return_frequency = None
        self._total_amount = None
        self._gb = None
        self._ie = None
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
        if from_date is not None:
            self.from_date = from_date
        if to_date is not None:
            self.to_date = to_date
        if tax_return_frequency is not None:
            self.tax_return_frequency = tax_return_frequency
        if total_amount is not None:
            self.total_amount = total_amount
        if gb is not None:
            self.gb = gb
        if ie is not None:
            self.ie = ie

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
    def from_date(self):
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        self._from_date = from_date

    @property
    def to_date(self):
        return self._to_date

    @to_date.setter
    def to_date(self, to_date):
        self._to_date = to_date

    @property
    def tax_return_frequency(self):
        return self._tax_return_frequency

    @tax_return_frequency.setter
    def tax_return_frequency(self, tax_return_frequency):
        self._tax_return_frequency = tax_return_frequency

    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        self._total_amount = total_amount

    @property
    def gb(self):
        return self._gb

    @gb.setter
    def gb(self, gb):
        self._gb = gb

    @property
    def ie(self):
        return self._ie

    @ie.setter
    def ie(self, ie):
        self._ie = ie

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
        if not isinstance(other, MigrationTaxReturn):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, MigrationTaxReturn):
            return True
        return self.to_dict() != other.to_dict()
