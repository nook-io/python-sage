import pprint
import six
from sage.configuration import Configuration


class PutTaxProfilesTaxProfile(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        "tax_type_id": "str",
        "tax_number": "str",
        "tax_number_suffix": "str",
        "collect_tax": "bool",
        "tax_return_frequency_id": "str",
        "address_region": "PutTaxProfilesTaxProfileAddressRegion",
    }
    attribute_map = {
        "tax_type_id": "tax_type_id",
        "tax_number": "tax_number",
        "tax_number_suffix": "tax_number_suffix",
        "collect_tax": "collect_tax",
        "tax_return_frequency_id": "tax_return_frequency_id",
        "address_region": "address_region",
    }

    def __init__(
        self,
        tax_type_id=None,
        tax_number=None,
        tax_number_suffix=None,
        collect_tax=None,
        tax_return_frequency_id=None,
        address_region=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._tax_type_id = None
        self._tax_number = None
        self._tax_number_suffix = None
        self._collect_tax = None
        self._tax_return_frequency_id = None
        self._address_region = None
        self.discriminator = None
        if tax_type_id is not None:
            self.tax_type_id = tax_type_id
        if tax_number is not None:
            self.tax_number = tax_number
        if tax_number_suffix is not None:
            self.tax_number_suffix = tax_number_suffix
        if collect_tax is not None:
            self.collect_tax = collect_tax
        if tax_return_frequency_id is not None:
            self.tax_return_frequency_id = tax_return_frequency_id
        if address_region is not None:
            self.address_region = address_region

    @property
    def tax_type_id(self):
        return self._tax_type_id

    @tax_type_id.setter
    def tax_type_id(self, tax_type_id):
        self._tax_type_id = tax_type_id

    @property
    def tax_number(self):
        return self._tax_number

    @tax_number.setter
    def tax_number(self, tax_number):
        self._tax_number = tax_number

    @property
    def tax_number_suffix(self):
        return self._tax_number_suffix

    @tax_number_suffix.setter
    def tax_number_suffix(self, tax_number_suffix):
        self._tax_number_suffix = tax_number_suffix

    @property
    def collect_tax(self):
        return self._collect_tax

    @collect_tax.setter
    def collect_tax(self, collect_tax):
        self._collect_tax = collect_tax

    @property
    def tax_return_frequency_id(self):
        return self._tax_return_frequency_id

    @tax_return_frequency_id.setter
    def tax_return_frequency_id(self, tax_return_frequency_id):
        self._tax_return_frequency_id = tax_return_frequency_id

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
        if not isinstance(other, PutTaxProfilesTaxProfile):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PutTaxProfilesTaxProfile):
            return True
        return self.to_dict() != other.to_dict()
