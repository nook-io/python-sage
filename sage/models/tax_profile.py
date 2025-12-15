import pprint
import six
from sage.configuration import Configuration


class TaxProfile(object):
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
        "created_at": "datetime",
        "updated_at": "datetime",
        "tax_type": "Base",
        "tax_number": "str",
        "tax_number_suffix": "str",
        "collect_tax": "bool",
        "tax_return_frequency": "Base",
        "address_region": "AddressRegion",
    }
    attribute_map = {
        "id": "id",
        "displayed_as": "displayed_as",
        "path": "$path",
        "created_at": "created_at",
        "updated_at": "updated_at",
        "tax_type": "tax_type",
        "tax_number": "tax_number",
        "tax_number_suffix": "tax_number_suffix",
        "collect_tax": "collect_tax",
        "tax_return_frequency": "tax_return_frequency",
        "address_region": "address_region",
    }

    def __init__(
        self,
        id=None,
        displayed_as=None,
        path=None,
        created_at=None,
        updated_at=None,
        tax_type=None,
        tax_number=None,
        tax_number_suffix=None,
        collect_tax=None,
        tax_return_frequency=None,
        address_region=None,
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
        self._tax_type = None
        self._tax_number = None
        self._tax_number_suffix = None
        self._collect_tax = None
        self._tax_return_frequency = None
        self._address_region = None
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
        if tax_type is not None:
            self.tax_type = tax_type
        if tax_number is not None:
            self.tax_number = tax_number
        if tax_number_suffix is not None:
            self.tax_number_suffix = tax_number_suffix
        if collect_tax is not None:
            self.collect_tax = collect_tax
        if tax_return_frequency is not None:
            self.tax_return_frequency = tax_return_frequency
        if address_region is not None:
            self.address_region = address_region

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
    def tax_type(self):
        return self._tax_type

    @tax_type.setter
    def tax_type(self, tax_type):
        self._tax_type = tax_type

    @property
    def tax_number(self):
        return self._tax_number

    @tax_number.setter
    def tax_number(self, tax_number):
        if (
            self.local_vars_configuration.client_side_validation
            and tax_number is not None
            and len(tax_number) > 255
        ):
            raise ValueError(
                "Invalid value for `tax_number`, length must be less than or equal to `255`"
            )
        self._tax_number = tax_number

    @property
    def tax_number_suffix(self):
        return self._tax_number_suffix

    @tax_number_suffix.setter
    def tax_number_suffix(self, tax_number_suffix):
        if (
            self.local_vars_configuration.client_side_validation
            and tax_number_suffix is not None
            and len(tax_number_suffix) > 255
        ):
            raise ValueError(
                "Invalid value for `tax_number_suffix`, length must be less than or equal to `255`"
            )
        self._tax_number_suffix = tax_number_suffix

    @property
    def collect_tax(self):
        return self._collect_tax

    @collect_tax.setter
    def collect_tax(self, collect_tax):
        self._collect_tax = collect_tax

    @property
    def tax_return_frequency(self):
        return self._tax_return_frequency

    @tax_return_frequency.setter
    def tax_return_frequency(self, tax_return_frequency):
        self._tax_return_frequency = tax_return_frequency

    @property
    def address_region(self):
        return self._address_region

    @address_region.setter
    def address_region(self, address_region):
        self._address_region = address_region

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
        if not isinstance(other, TaxProfile):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, TaxProfile):
            return True
        return self.to_dict() != other.to_dict()
