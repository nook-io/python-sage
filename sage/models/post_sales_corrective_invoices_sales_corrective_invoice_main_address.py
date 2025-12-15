import pprint
import six
from sage.configuration import Configuration


class PostSalesCorrectiveInvoicesSalesCorrectiveInvoiceMainAddress(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        "address_line_1": "str",
        "address_line_2": "str",
        "city": "str",
        "postal_code": "str",
        "country_id": "str",
        "address_type_id": "str",
        "region": "str",
        "country_group_id": "str",
    }
    attribute_map = {
        "address_line_1": "address_line_1",
        "address_line_2": "address_line_2",
        "city": "city",
        "postal_code": "postal_code",
        "country_id": "country_id",
        "address_type_id": "address_type_id",
        "region": "region",
        "country_group_id": "country_group_id",
    }

    def __init__(
        self,
        address_line_1=None,
        address_line_2=None,
        city=None,
        postal_code=None,
        country_id=None,
        address_type_id=None,
        region=None,
        country_group_id=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._address_line_1 = None
        self._address_line_2 = None
        self._city = None
        self._postal_code = None
        self._country_id = None
        self._address_type_id = None
        self._region = None
        self._country_group_id = None
        self.discriminator = None
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
        if address_type_id is not None:
            self.address_type_id = address_type_id
        if region is not None:
            self.region = region
        if country_group_id is not None:
            self.country_group_id = country_group_id

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
    def address_type_id(self):
        return self._address_type_id

    @address_type_id.setter
    def address_type_id(self, address_type_id):
        self._address_type_id = address_type_id

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
        if not isinstance(
            other, PostSalesCorrectiveInvoicesSalesCorrectiveInvoiceMainAddress
        ):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(
            other, PostSalesCorrectiveInvoicesSalesCorrectiveInvoiceMainAddress
        ):
            return True
        return self.to_dict() != other.to_dict()
