import pprint
import six
from sage.configuration import Configuration


class Subscription(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        "created_at": "datetime",
        "updated_at": "datetime",
        "displayed_as": "str",
        "id": "str",
        "active": "bool",
        "status": "str",
    }
    attribute_map = {
        "created_at": "created_at",
        "updated_at": "updated_at",
        "displayed_as": "displayed_as",
        "id": "id",
        "active": "active",
        "status": "status",
    }

    def __init__(
        self,
        created_at=None,
        updated_at=None,
        displayed_as=None,
        id=None,
        active=None,
        status=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._created_at = None
        self._updated_at = None
        self._displayed_as = None
        self._id = None
        self._active = None
        self._status = None
        self.discriminator = None
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if displayed_as is not None:
            self.displayed_as = displayed_as
        if id is not None:
            self.id = id
        if active is not None:
            self.active = active
        if status is not None:
            self.status = status

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
    def displayed_as(self):
        return self._displayed_as

    @displayed_as.setter
    def displayed_as(self, displayed_as):
        self._displayed_as = displayed_as

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, active):
        self._active = active

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

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
        if not isinstance(other, Subscription):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, Subscription):
            return True
        return self.to_dict() != other.to_dict()
