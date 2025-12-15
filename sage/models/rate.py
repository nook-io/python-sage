import pprint
import six
from sage.configuration import Configuration


class Rate(object):
    openapi_types = {
        "id": "str",
        "displayed_as": "str",
        "created_at": "datetime",
        "updated_at": "datetime",
        "rate_name": "str",
        "rate": "float",
        "rate_includes_tax": "bool",
        "service_rate_type": "Base",
    }
    attribute_map = {
        "id": "id",
        "displayed_as": "displayed_as",
        "created_at": "created_at",
        "updated_at": "updated_at",
        "rate_name": "rate_name",
        "rate": "rate",
        "rate_includes_tax": "rate_includes_tax",
        "service_rate_type": "service_rate_type",
    }

    def __init__(
        self,
        id=None,
        displayed_as=None,
        created_at=None,
        updated_at=None,
        rate_name=None,
        rate=None,
        rate_includes_tax=None,
        service_rate_type=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._id = None
        self._displayed_as = None
        self._created_at = None
        self._updated_at = None
        self._rate_name = None
        self._rate = None
        self._rate_includes_tax = None
        self._service_rate_type = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if displayed_as is not None:
            self.displayed_as = displayed_as
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if rate_name is not None:
            self.rate_name = rate_name
        if rate is not None:
            self.rate = rate
        if rate_includes_tax is not None:
            self.rate_includes_tax = rate_includes_tax
        if service_rate_type is not None:
            self.service_rate_type = service_rate_type

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
    def rate_name(self):
        return self._rate_name

    @rate_name.setter
    def rate_name(self, rate_name):
        self._rate_name = rate_name

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, rate):
        self._rate = rate

    @property
    def rate_includes_tax(self):
        return self._rate_includes_tax

    @rate_includes_tax.setter
    def rate_includes_tax(self, rate_includes_tax):
        self._rate_includes_tax = rate_includes_tax

    @property
    def service_rate_type(self):
        return self._service_rate_type

    @service_rate_type.setter
    def service_rate_type(self, service_rate_type):
        self._service_rate_type = service_rate_type

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
        if not isinstance(other, Rate):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, Rate):
            return True
        return self.to_dict() != other.to_dict()
