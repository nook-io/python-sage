import pprint
import six
from sage.configuration import Configuration


class PutAddressesAddress(object):
    openapi_types = {
        "address_type_id": "str",
        "name": "str",
        "is_main_address": "bool",
        "address_line_1": "str",
        "address_line_2": "str",
        "city": "str",
        "postal_code": "str",
        "country_id": "str",
        "bank_account_id": "str",
        "contact_id": "str",
        "region": "str",
        "country_group_id": "str",
    }
    attribute_map = {
        "address_type_id": "address_type_id",
        "name": "name",
        "is_main_address": "is_main_address",
        "address_line_1": "address_line_1",
        "address_line_2": "address_line_2",
        "city": "city",
        "postal_code": "postal_code",
        "country_id": "country_id",
        "bank_account_id": "bank_account_id",
        "contact_id": "contact_id",
        "region": "region",
        "country_group_id": "country_group_id",
    }

    def __init__(
        self,
        address_type_id=None,
        name=None,
        is_main_address=None,
        address_line_1=None,
        address_line_2=None,
        city=None,
        postal_code=None,
        country_id=None,
        bank_account_id=None,
        contact_id=None,
        region=None,
        country_group_id=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._address_type_id = None
        self._name = None
        self._is_main_address = None
        self._address_line_1 = None
        self._address_line_2 = None
        self._city = None
        self._postal_code = None
        self._country_id = None
        self._bank_account_id = None
        self._contact_id = None
        self._region = None
        self._country_group_id = None
        self.discriminator = None
        if address_type_id is not None:
            self.address_type_id = address_type_id
        if name is not None:
            self.name = name
        if is_main_address is not None:
            self.is_main_address = is_main_address
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
        if bank_account_id is not None:
            self.bank_account_id = bank_account_id
        if contact_id is not None:
            self.contact_id = contact_id
        if region is not None:
            self.region = region
        if country_group_id is not None:
            self.country_group_id = country_group_id

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
        self._name = name

    @property
    def is_main_address(self):
        return self._is_main_address

    @is_main_address.setter
    def is_main_address(self, is_main_address):
        self._is_main_address = is_main_address

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
    def country_id(self):
        return self._country_id

    @country_id.setter
    def country_id(self, country_id):
        self._country_id = country_id

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
    def contact_id(self, contact_id):
        self._contact_id = contact_id

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, region):
        self._region = region

    @property
    def country_group_id(self):
        return self._country_group_id

    @country_group_id.setter
    def country_group_id(self, country_group_id):
        self._country_group_id = country_group_id

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
        if not isinstance(other, PutAddressesAddress):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PutAddressesAddress):
            return True
        return self.to_dict() != other.to_dict()
