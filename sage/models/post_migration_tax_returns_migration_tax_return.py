import pprint
import six
from sage.configuration import Configuration


class PostMigrationTaxReturnsMigrationTaxReturn(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        "from_date": "date",
        "to_date": "date",
        "total_amount": "float",
        "tax_return_frequency_id": "str",
        "gb": "PostMigrationTaxReturnsMigrationTaxReturnGb",
        "ie": "PostMigrationTaxReturnsMigrationTaxReturnIe",
    }
    attribute_map = {
        "from_date": "from_date",
        "to_date": "to_date",
        "total_amount": "total_amount",
        "tax_return_frequency_id": "tax_return_frequency_id",
        "gb": "gb",
        "ie": "ie",
    }

    def __init__(
        self,
        from_date=None,
        to_date=None,
        total_amount=None,
        tax_return_frequency_id=None,
        gb=None,
        ie=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._from_date = None
        self._to_date = None
        self._total_amount = None
        self._tax_return_frequency_id = None
        self._gb = None
        self._ie = None
        self.discriminator = None
        self.from_date = from_date
        self.to_date = to_date
        self.total_amount = total_amount
        self.tax_return_frequency_id = tax_return_frequency_id
        if gb is not None:
            self.gb = gb
        if ie is not None:
            self.ie = ie

    @property
    def from_date(self):
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        if self.local_vars_configuration.client_side_validation and from_date is None:
            raise ValueError("Invalid value for `from_date`, must not be `None`")
        self._from_date = from_date

    @property
    def to_date(self):
        return self._to_date

    @to_date.setter
    def to_date(self, to_date):
        if self.local_vars_configuration.client_side_validation and to_date is None:
            raise ValueError("Invalid value for `to_date`, must not be `None`")
        self._to_date = to_date

    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        if (
            self.local_vars_configuration.client_side_validation
            and total_amount is None
        ):
            raise ValueError("Invalid value for `total_amount`, must not be `None`")
        self._total_amount = total_amount

    @property
    def tax_return_frequency_id(self):
        return self._tax_return_frequency_id

    @tax_return_frequency_id.setter
    def tax_return_frequency_id(self, tax_return_frequency_id):
        if (
            self.local_vars_configuration.client_side_validation
            and tax_return_frequency_id is None
        ):
            raise ValueError(
                "Invalid value for `tax_return_frequency_id`, must not be `None`"
            )
        self._tax_return_frequency_id = tax_return_frequency_id

    @property
    def gb(self):
        return self._gb

    @gb.setter
    def gb(self, gb):
        self._gb = gb

    @property
    def ie(self):
        return self._ie

    @ie.setter
    def ie(self, ie):
        self._ie = ie

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
        if not isinstance(other, PostMigrationTaxReturnsMigrationTaxReturn):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PostMigrationTaxReturnsMigrationTaxReturn):
            return True
        return self.to_dict() != other.to_dict()
