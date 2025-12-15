import pprint
import six
from sage.configuration import Configuration


class TaxOffice(object):
    openapi_types = {
        "id": "str",
        "displayed_as": "str",
        "path": "str",
        "office_number": "str",
        "name": "str",
    }
    attribute_map = {
        "id": "id",
        "displayed_as": "displayed_as",
        "path": "$path",
        "office_number": "office_number",
        "name": "name",
    }

    def __init__(
        self,
        id=None,
        displayed_as=None,
        path=None,
        office_number=None,
        name=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._id = None
        self._displayed_as = None
        self._path = None
        self._office_number = None
        self._name = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if displayed_as is not None:
            self.displayed_as = displayed_as
        if path is not None:
            self.path = path
        if office_number is not None:
            self.office_number = office_number
        if name is not None:
            self.name = name

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        if (
            self.local_vars_configuration.client_side_validation
            and id is not None
            and len(id) > 17
        ):
            raise ValueError(
                "Invalid value for `id`, length must be less than or equal to `17`"
            )
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
    def office_number(self):
        return self._office_number

    @office_number.setter
    def office_number(self, office_number):
        if (
            self.local_vars_configuration.client_side_validation
            and office_number is not None
            and len(office_number) > 4
        ):
            raise ValueError(
                "Invalid value for `office_number`, length must be less than or equal to `4`"
            )
        self._office_number = office_number

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
        if not isinstance(other, TaxOffice):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, TaxOffice):
            return True
        return self.to_dict() != other.to_dict()
