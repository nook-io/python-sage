import pprint
import six
from sage.configuration import Configuration


class TaxRatePercentage(object):
    openapi_types = {"percentage": "float", "from_date": "date", "to_date": "date"}
    attribute_map = {
        "percentage": "percentage",
        "from_date": "from_date",
        "to_date": "to_date",
    }

    def __init__(
        self,
        percentage=None,
        from_date=None,
        to_date=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._percentage = None
        self._from_date = None
        self._to_date = None
        self.discriminator = None
        if percentage is not None:
            self.percentage = percentage
        if from_date is not None:
            self.from_date = from_date
        if to_date is not None:
            self.to_date = to_date

    @property
    def percentage(self):
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        self._percentage = percentage

    @property
    def from_date(self):
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        self._from_date = from_date

    @property
    def to_date(self):
        return self._to_date

    @to_date.setter
    def to_date(self, to_date):
        self._to_date = to_date

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
        if not isinstance(other, TaxRatePercentage):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, TaxRatePercentage):
            return True
        return self.to_dict() != other.to_dict()
