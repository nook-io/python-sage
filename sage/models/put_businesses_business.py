import pprint
import six
from sage.configuration import Configuration


class PutBusinessesBusiness(object):
    openapi_types = {
        "name": "str",
        "address_line_1": "str",
        "address_line_2": "str",
        "city": "str",
        "region": "str",
        "postal_code": "str",
        "telephone": "str",
        "mobile": "str",
        "website": "str",
    }
    attribute_map = {
        "name": "name",
        "address_line_1": "address_line_1",
        "address_line_2": "address_line_2",
        "city": "city",
        "region": "region",
        "postal_code": "postal_code",
        "telephone": "telephone",
        "mobile": "mobile",
        "website": "website",
    }

    def __init__(
        self,
        name=None,
        address_line_1=None,
        address_line_2=None,
        city=None,
        region=None,
        postal_code=None,
        telephone=None,
        mobile=None,
        website=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._name = None
        self._address_line_1 = None
        self._address_line_2 = None
        self._city = None
        self._region = None
        self._postal_code = None
        self._telephone = None
        self._mobile = None
        self._website = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if address_line_1 is not None:
            self.address_line_1 = address_line_1
        if address_line_2 is not None:
            self.address_line_2 = address_line_2
        if city is not None:
            self.city = city
        if region is not None:
            self.region = region
        if postal_code is not None:
            self.postal_code = postal_code
        if telephone is not None:
            self.telephone = telephone
        if mobile is not None:
            self.mobile = mobile
        if website is not None:
            self.website = website

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

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
    def region(self):
        return self._region

    @region.setter
    def region(self, region):
        self._region = region

    @property
    def postal_code(self):
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        self._postal_code = postal_code

    @property
    def telephone(self):
        return self._telephone

    @telephone.setter
    def telephone(self, telephone):
        self._telephone = telephone

    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        self._mobile = mobile

    @property
    def website(self):
        return self._website

    @website.setter
    def website(self, website):
        self._website = website

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
        if not isinstance(other, PutBusinessesBusiness):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PutBusinessesBusiness):
            return True
        return self.to_dict() != other.to_dict()
