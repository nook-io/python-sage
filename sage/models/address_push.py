import pprint
import six
from sage.configuration import Configuration


class AddressPush(object):
    openapi_types = {
        "id": "str",
        "displayed_as": "str",
        "path": "str",
        "address_line_1": "str",
        "address_line_2": "str",
        "city": "str",
        "postal_code": "str",
        "country_id": "str",
        "deleted_at": "datetime",
        "created_at": "datetime",
        "updated_at": "datetime",
        "bank_account_id": "str",
        "contact_id": "str",
        "address_type_id": "str",
        "name": "str",
        "region": "str",
        "country_group_id": "str",
        "is_main_address": "bool",
    }
    attribute_map = {
        "id": "id",
        "displayed_as": "displayed_as",
        "path": "$path",
        "address_line_1": "address_line_1",
        "address_line_2": "address_line_2",
        "city": "city",
        "postal_code": "postal_code",
        "country_id": "country_id",
        "deleted_at": "deleted_at",
        "created_at": "created_at",
        "updated_at": "updated_at",
        "bank_account_id": "bank_account_id",
        "contact_id": "contact_id",
        "address_type_id": "address_type_id",
        "name": "name",
        "region": "region",
        "country_group_id": "country_group_id",
        "is_main_address": "is_main_address",
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
        country_id=None,
        deleted_at=None,
        created_at=None,
        updated_at=None,
        bank_account_id=None,
        contact_id=None,
        address_type_id=None,
        name=None,
        region=None,
        country_group_id=None,
        is_main_address=None,
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
        self._country_id = None
        self._deleted_at = None
        self._created_at = None
        self._updated_at = None
        self._bank_account_id = None
        self._contact_id = None
        self._address_type_id = None
        self._name = None
        self._region = None
        self._country_group_id = None
        self._is_main_address = None
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
        if country_id is not None:
            self.country_id = country_id
        if deleted_at is not None:
            self.deleted_at = deleted_at
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if bank_account_id is not None:
            self.bank_account_id = bank_account_id
        if contact_id is not None:
            self.contact_id = contact_id
        if address_type_id is not None:
            self.address_type_id = address_type_id
        if name is not None:
            self.name = name
        if region is not None:
            self.region = region
        if country_group_id is not None:
            self.country_group_id = country_group_id
        if is_main_address is not None:
            self.is_main_address = is_main_address

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
        if (
            self.local_vars_configuration.client_side_validation
            and address_line_1 is not None
            and len(address_line_1) > 50
        ):
            raise ValueError(
                "Invalid value for `address_line_1`, length must be less than or equal to `50`"
            )
        self._address_line_1 = address_line_1

    @property
    def address_line_2(self):
        return self._address_line_2

    @address_line_2.setter
    def address_line_2(self, address_line_2):
        if (
            self.local_vars_configuration.client_side_validation
            and address_line_2 is not None
            and len(address_line_2) > 50
        ):
            raise ValueError(
                "Invalid value for `address_line_2`, length must be less than or equal to `50`"
            )
        self._address_line_2 = address_line_2

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        if (
            self.local_vars_configuration.client_side_validation
            and city is not None
            and len(city) > 50
        ):
            raise ValueError(
                "Invalid value for `city`, length must be less than or equal to `50`"
            )
        self._city = city

    @property
    def postal_code(self):
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        if (
            self.local_vars_configuration.client_side_validation
            and postal_code is not None
            and len(postal_code) > 10
        ):
            raise ValueError(
                "Invalid value for `postal_code`, length must be less than or equal to `10`"
            )
        self._postal_code = postal_code

    @property
    def country_id(self):
        return self._country_id

    @country_id.setter
    def country_id(self, country_id):
        self._country_id = country_id

    @property
    def deleted_at(self):
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        self._deleted_at = deleted_at

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
    def bank_account_id(self):
        return self._bank_account_id

    @bank_account_id.setter
    def bank_account_id(self, bank_account_id):
        self._bank_account_id = bank_account_id

    @property
    def contact_id(self):
        return self._contact_id

    @contact_id.setter
    def contact(self, contact_id):
        self._contact_id = contact_id

    @property
    def address_type_id(self):
        return self._address_type_id

    @address_type_id.setter
    def address_type_id(self, address_type_id):
        self._address_type_id = address_type_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if (
            self.local_vars_configuration.client_side_validation
            and name is not None
            and len(name) > 50
        ):
            raise ValueError(
                "Invalid value for `name`, length must be less than or equal to `50`"
            )
        self._name = name

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, region):
        if (
            self.local_vars_configuration.client_side_validation
            and region is not None
            and len(region) > 50
        ):
            raise ValueError(
                "Invalid value for `region`, length must be less than or equal to `50`"
            )
        self._region = region

    @property
    def country_group_id(self):
        return self._country_group_id

    @country_group_id.setter
    def country_group_id(self, country_group_id):
        self._country_group_id = country_group_id

    @property
    def is_main_address(self):
        return self._is_main_address

    @is_main_address.setter
    def is_main_address(self, is_main_address):
        self._is_main_address = is_main_address

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
        if not isinstance(other, Address):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, Address):
            return True
        return self.to_dict() != other.to_dict()
