import pprint
import six
from sage.configuration import Configuration


class PutTaxRatesTaxRate(object):
    openapi_types = {
        "name": "str",
        "from_date": "datetime",
        "agency": "str",
        "percentage": "float",
        "is_visible": "bool",
    }
    attribute_map = {
        "name": "name",
        "from_date": "from_date",
        "agency": "agency",
        "percentage": "percentage",
        "is_visible": "is_visible",
    }

    def __init__(
        self,
        name=None,
        from_date=None,
        agency=None,
        percentage=None,
        is_visible=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._name = None
        self._from_date = None
        self._agency = None
        self._percentage = None
        self._is_visible = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if from_date is not None:
            self.from_date = from_date
        if agency is not None:
            self.agency = agency
        if percentage is not None:
            self.percentage = percentage
        if is_visible is not None:
            self.is_visible = is_visible

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def from_date(self):
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        self._from_date = from_date

    @property
    def agency(self):
        return self._agency

    @agency.setter
    def agency(self, agency):
        self._agency = agency

    @property
    def percentage(self):
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        self._percentage = percentage

    @property
    def is_visible(self):
        return self._is_visible

    @is_visible.setter
    def is_visible(self, is_visible):
        self._is_visible = is_visible

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
        if not isinstance(other, PutTaxRatesTaxRate):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PutTaxRatesTaxRate):
            return True
        return self.to_dict() != other.to_dict()
