import pprint
import six
from sage.configuration import Configuration


class User(object):
    openapi_types = {
        "created_at": "datetime",
        "updated_at": "datetime",
        "displayed_as": "str",
        "id": "str",
        "first_name": "str",
        "last_name": "str",
        "initials": "str",
        "email": "str",
        "locale": "str",
    }
    attribute_map = {
        "created_at": "created_at",
        "updated_at": "updated_at",
        "displayed_as": "displayed_as",
        "id": "id",
        "first_name": "first_name",
        "last_name": "last_name",
        "initials": "initials",
        "email": "email",
        "locale": "locale",
    }

    def __init__(
        self,
        created_at=None,
        updated_at=None,
        displayed_as=None,
        id=None,
        first_name=None,
        last_name=None,
        initials=None,
        email=None,
        locale=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._created_at = None
        self._updated_at = None
        self._displayed_as = None
        self._id = None
        self._first_name = None
        self._last_name = None
        self._initials = None
        self._email = None
        self._locale = None
        self.discriminator = None
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if displayed_as is not None:
            self.displayed_as = displayed_as
        if id is not None:
            self.id = id
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if initials is not None:
            self.initials = initials
        if email is not None:
            self.email = email
        if locale is not None:
            self.locale = locale

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
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def initials(self):
        return self._initials

    @initials.setter
    def initials(self, initials):
        self._initials = initials

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def locale(self):
        return self._locale

    @locale.setter
    def locale(self, locale):
        self._locale = locale

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
        if not isinstance(other, User):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, User):
            return True
        return self.to_dict() != other.to_dict()
