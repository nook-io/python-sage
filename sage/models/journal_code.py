import pprint
import six
from sage.configuration import Configuration


class JournalCode(object):
    openapi_types = {
        "id": "str",
        "displayed_as": "str",
        "path": "str",
        "created_at": "datetime",
        "updated_at": "datetime",
        "name": "str",
        "code": "str",
        "journal_code_type": "JournalCodeType",
        "control_name": "str",
        "reserved": "bool",
    }
    attribute_map = {
        "id": "id",
        "displayed_as": "displayed_as",
        "path": "$path",
        "created_at": "created_at",
        "updated_at": "updated_at",
        "name": "name",
        "code": "code",
        "journal_code_type": "journal_code_type",
        "control_name": "control_name",
        "reserved": "reserved",
    }

    def __init__(
        self,
        id=None,
        displayed_as=None,
        path=None,
        created_at=None,
        updated_at=None,
        name=None,
        code=None,
        journal_code_type=None,
        control_name=None,
        reserved=None,
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
        self._name = None
        self._code = None
        self._journal_code_type = None
        self._control_name = None
        self._reserved = None
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
        if name is not None:
            self.name = name
        if code is not None:
            self.code = code
        if journal_code_type is not None:
            self.journal_code_type = journal_code_type
        if control_name is not None:
            self.control_name = control_name
        if reserved is not None:
            self.reserved = reserved

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
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if (
            self.local_vars_configuration.client_side_validation
            and name is not None
            and len(name) > 255
        ):
            raise ValueError(
                "Invalid value for `name`, length must be less than or equal to `255`"
            )
        self._name = name

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        if (
            self.local_vars_configuration.client_side_validation
            and code is not None
            and len(code) > 255
        ):
            raise ValueError(
                "Invalid value for `code`, length must be less than or equal to `255`"
            )
        self._code = code

    @property
    def journal_code_type(self):
        return self._journal_code_type

    @journal_code_type.setter
    def journal_code_type(self, journal_code_type):
        self._journal_code_type = journal_code_type

    @property
    def control_name(self):
        return self._control_name

    @control_name.setter
    def control_name(self, control_name):
        if (
            self.local_vars_configuration.client_side_validation
            and control_name is not None
            and len(control_name) > 255
        ):
            raise ValueError(
                "Invalid value for `control_name`, length must be less than or equal to `255`"
            )
        self._control_name = control_name

    @property
    def reserved(self):
        return self._reserved

    @reserved.setter
    def reserved(self, reserved):
        self._reserved = reserved

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
        if not isinstance(other, JournalCode):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, JournalCode):
            return True
        return self.to_dict() != other.to_dict()
