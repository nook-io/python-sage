import pprint
import six
from sage.configuration import Configuration


class Business(object):
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
        "name": "str",
        "address_line_1": "str",
        "address_line_2": "str",
        "city": "str",
        "postal_code": "str",
        "country": "Country",
        "region": "str",
        "telephone": "str",
        "mobile": "str",
        "website": "str",
        "is_demo": "bool",
        "ni_based": "bool",
        "subscriptions": "list[Subscription]",
    }
    attribute_map = {
        "created_at": "created_at",
        "updated_at": "updated_at",
        "displayed_as": "displayed_as",
        "id": "id",
        "name": "name",
        "address_line_1": "address_line_1",
        "address_line_2": "address_line_2",
        "city": "city",
        "postal_code": "postal_code",
        "country": "country",
        "region": "region",
        "telephone": "telephone",
        "mobile": "mobile",
        "website": "website",
        "is_demo": "is_demo",
        "ni_based": "ni_based",
        "subscriptions": "subscriptions",
    }

    def __init__(
        self,
        created_at=None,
        updated_at=None,
        displayed_as=None,
        id=None,
        name=None,
        address_line_1=None,
        address_line_2=None,
        city=None,
        postal_code=None,
        country=None,
        region=None,
        telephone=None,
        mobile=None,
        website=None,
        is_demo=None,
        ni_based=None,
        subscriptions=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._created_at = None
        self._updated_at = None
        self._displayed_as = None
        self._id = None
        self._name = None
        self._address_line_1 = None
        self._address_line_2 = None
        self._city = None
        self._postal_code = None
        self._country = None
        self._region = None
        self._telephone = None
        self._mobile = None
        self._website = None
        self._is_demo = None
        self._ni_based = None
        self._subscriptions = None
        self.discriminator = None
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if displayed_as is not None:
            self.displayed_as = displayed_as
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
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
        if region is not None:
            self.region = region
        if telephone is not None:
            self.telephone = telephone
        if mobile is not None:
            self.mobile = mobile
        if website is not None:
            self.website = website
        if is_demo is not None:
            self.is_demo = is_demo
        if ni_based is not None:
            self.ni_based = ni_based
        if subscriptions is not None:
            self.subscriptions = subscriptions

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
    def region(self):
        return self._region

    @region.setter
    def region(self, region):
        self._region = region

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

    @property
    def is_demo(self):
        return self._is_demo

    @is_demo.setter
    def is_demo(self, is_demo):
        self._is_demo = is_demo

    @property
    def ni_based(self):
        return self._ni_based

    @ni_based.setter
    def ni_based(self, ni_based):
        self._ni_based = ni_based

    @property
    def subscriptions(self):
        return self._subscriptions

    @subscriptions.setter
    def subscriptions(self, subscriptions):
        self._subscriptions = subscriptions

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
        if not isinstance(other, Business):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, Business):
            return True
        return self.to_dict() != other.to_dict()
