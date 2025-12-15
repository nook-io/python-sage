import pprint
import six
from sage.configuration import Configuration


class ContactTaxTreatment(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        "home_tax": "bool",
        "eu_tax_registered": "bool",
        "eu_not_tax_registered": "bool",
        "rest_of_world_tax": "bool",
        "is_importer": "bool",
    }
    attribute_map = {
        "home_tax": "home_tax",
        "eu_tax_registered": "eu_tax_registered",
        "eu_not_tax_registered": "eu_not_tax_registered",
        "rest_of_world_tax": "rest_of_world_tax",
        "is_importer": "is_importer",
    }

    def __init__(
        self,
        home_tax=None,
        eu_tax_registered=None,
        eu_not_tax_registered=None,
        rest_of_world_tax=None,
        is_importer=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._home_tax = None
        self._eu_tax_registered = None
        self._eu_not_tax_registered = None
        self._rest_of_world_tax = None
        self._is_importer = None
        self.discriminator = None
        if home_tax is not None:
            self.home_tax = home_tax
        if eu_tax_registered is not None:
            self.eu_tax_registered = eu_tax_registered
        if eu_not_tax_registered is not None:
            self.eu_not_tax_registered = eu_not_tax_registered
        if rest_of_world_tax is not None:
            self.rest_of_world_tax = rest_of_world_tax
        if is_importer is not None:
            self.is_importer = is_importer

    @property
    def home_tax(self):
        return self._home_tax

    @home_tax.setter
    def home_tax(self, home_tax):
        self._home_tax = home_tax

    @property
    def eu_tax_registered(self):
        return self._eu_tax_registered

    @eu_tax_registered.setter
    def eu_tax_registered(self, eu_tax_registered):
        self._eu_tax_registered = eu_tax_registered

    @property
    def eu_not_tax_registered(self):
        return self._eu_not_tax_registered

    @eu_not_tax_registered.setter
    def eu_not_tax_registered(self, eu_not_tax_registered):
        self._eu_not_tax_registered = eu_not_tax_registered

    @property
    def rest_of_world_tax(self):
        return self._rest_of_world_tax

    @rest_of_world_tax.setter
    def rest_of_world_tax(self, rest_of_world_tax):
        self._rest_of_world_tax = rest_of_world_tax

    @property
    def is_importer(self):
        return self._is_importer

    @is_importer.setter
    def is_importer(self, is_importer):
        self._is_importer = is_importer

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
        if not isinstance(other, ContactTaxTreatment):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, ContactTaxTreatment):
            return True
        return self.to_dict() != other.to_dict()
