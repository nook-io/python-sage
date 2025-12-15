import pprint
import six
from sage.configuration import Configuration


class SalesArtefactAddress(object):
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
        "address_line_1": "str",
        "address_line_2": "str",
        "city": "str",
        "postal_code": "str",
        "country": "Base",
        "deleted_at": "datetime",
        "address_type": "Base",
        "region": "str",
        "country_group": "Base",
    }
    attribute_map = {
        "id": "id",
        "displayed_as": "displayed_as",
        "path": "$path",
        "address_line_1": "address_line_1",
        "address_line_2": "address_line_2",
        "city": "city",
        "postal_code": "postal_code",
        "country": "country",
        "deleted_at": "deleted_at",
        "address_type": "address_type",
        "region": "region",
        "country_group": "country_group",
    }

    def __init__(
        self,
        id=None,
        displayed_as=None,
        path=None,
        address_line_1=None,
        address_line_2=None,
        city=None,
        postal_code=None,
        country=None,
        deleted_at=None,
        address_type=None,
        region=None,
        country_group=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._id = None
        self._displayed_as = None
        self._path = None
        self._address_line_1 = None
        self._address_line_2 = None
        self._city = None
        self._postal_code = None
        self._country = None
        self._deleted_at = None
        self._address_type = None
        self._region = None
        self._country_group = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if displayed_as is not None:
            self.displayed_as = displayed_as
        if path is not None:
            self.path = path
        if address_line_1 is not None:
            self.address_line_1 = address_line_1
        if address_line_2 is not None:
            self.address_line_2 = address_line_2
        if city is not None:
            self.city = city
        if postal_code is not None:
            self.postal_code = postal_code
        if country is not None:
            self.country = country
        if deleted_at is not None:
            self.deleted_at = deleted_at
        if address_type is not None:
            self.address_type = address_type
        if region is not None:
            self.region = region
        if country_group is not None:
            self.country_group = country_group

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
    def address_line_1(self):
        return self._address_line_1

    @address_line_1.setter
    def address_line_1(self, address_line_1):
        self._address_line_1 = address_line_1

    @property
    def address_line_2(self):
        return self._address_line_2

    @address_line_2.setter
    def address_line_2(self, address_line_2):
        self._address_line_2 = address_line_2

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        self._city = city

    @property
    def postal_code(self):
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        self._postal_code = postal_code

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country):
        self._country = country

    @property
    def deleted_at(self):
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        self._deleted_at = deleted_at

    @property
    def address_type(self):
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        self._address_type = address_type

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, region):
        self._region = region

    @property
    def country_group(self):
        return self._country_group

    @country_group.setter
    def country_group(self, country_group):
        self._country_group = country_group

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
        if not isinstance(other, SalesArtefactAddress):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, SalesArtefactAddress):
            return True
        return self.to_dict() != other.to_dict()
