import pprint
import six
from sage.configuration import Configuration


class PostSalesInvoicesSalesInvoiceRecurringInvoice(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        "frequency": "int",
        "on_week_day": "int",
        "on_day_number": "int",
        "recurrence_type": "str",
        "recurrence_status_identifier": "str",
    }
    attribute_map = {
        "frequency": "frequency",
        "on_week_day": "on_week_day",
        "on_day_number": "on_day_number",
        "recurrence_type": "recurrence_type",
        "recurrence_status_identifier": "recurrence_status_identifier",
    }

    def __init__(
        self,
        frequency=None,
        on_week_day=None,
        on_day_number=None,
        recurrence_type=None,
        recurrence_status_identifier=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._frequency = None
        self._on_week_day = None
        self._on_day_number = None
        self._recurrence_type = None
        self._recurrence_status_identifier = None
        self.discriminator = None
        if frequency is not None:
            self.frequency = frequency
        if on_week_day is not None:
            self.on_week_day = on_week_day
        if on_day_number is not None:
            self.on_day_number = on_day_number
        if recurrence_type is not None:
            self.recurrence_type = recurrence_type
        if recurrence_status_identifier is not None:
            self.recurrence_status_identifier = recurrence_status_identifier

    @property
    def frequency(self):
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        self._frequency = frequency

    @property
    def on_week_day(self):
        return self._on_week_day

    @on_week_day.setter
    def on_week_day(self, on_week_day):
        self._on_week_day = on_week_day

    @property
    def on_day_number(self):
        return self._on_day_number

    @on_day_number.setter
    def on_day_number(self, on_day_number):
        self._on_day_number = on_day_number

    @property
    def recurrence_type(self):
        return self._recurrence_type

    @recurrence_type.setter
    def recurrence_type(self, recurrence_type):
        self._recurrence_type = recurrence_type

    @property
    def recurrence_status_identifier(self):
        return self._recurrence_status_identifier

    @recurrence_status_identifier.setter
    def recurrence_status_identifier(self, recurrence_status_identifier):
        self._recurrence_status_identifier = recurrence_status_identifier

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
        if not isinstance(other, PostSalesInvoicesSalesInvoiceRecurringInvoice):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PostSalesInvoicesSalesInvoiceRecurringInvoice):
            return True
        return self.to_dict() != other.to_dict()
