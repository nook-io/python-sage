import pprint
import six
from sage.configuration import Configuration


class TaxType(object):
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
        "federal_tax": "bool",
        "country": "Base",
        "address_regions": "list[Base]",
        "tax_rates": "list[Base]",
    }
    attribute_map = {
        "id": "id",
        "displayed_as": "displayed_as",
        "path": "$path",
        "federal_tax": "federal_tax",
        "country": "country",
        "address_regions": "address_regions",
        "tax_rates": "tax_rates",
    }

    def __init__(
        self,
        id=None,
        displayed_as=None,
        path=None,
        federal_tax=None,
        country=None,
        address_regions=None,
        tax_rates=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._id = None
        self._displayed_as = None
        self._path = None
        self._federal_tax = None
        self._country = None
        self._address_regions = None
        self._tax_rates = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if displayed_as is not None:
            self.displayed_as = displayed_as
        if path is not None:
            self.path = path
        if federal_tax is not None:
            self.federal_tax = federal_tax
        if country is not None:
            self.country = country
        if address_regions is not None:
            self.address_regions = address_regions
        if tax_rates is not None:
            self.tax_rates = tax_rates

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        if (
            self.local_vars_configuration.client_side_validation
            and id is not None
            and len(id) > 15
        ):
            raise ValueError(
                "Invalid value for `id`, length must be less than or equal to `15`"
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
    def federal_tax(self):
        return self._federal_tax

    @federal_tax.setter
    def federal_tax(self, federal_tax):
        self._federal_tax = federal_tax

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country):
        self._country = country

    @property
    def address_regions(self):
        return self._address_regions

    @address_regions.setter
    def address_regions(self, address_regions):
        self._address_regions = address_regions

    @property
    def tax_rates(self):
        return self._tax_rates

    @tax_rates.setter
    def tax_rates(self, tax_rates):
        self._tax_rates = tax_rates

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
        if not isinstance(other, TaxType):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, TaxType):
            return True
        return self.to_dict() != other.to_dict()
