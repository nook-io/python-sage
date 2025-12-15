import pprint
import six
from sage.configuration import Configuration


class PutInvoiceSettingsInvoiceSettingsPrintStatements(object):
    openapi_types = {"days_overdue": "bool", "table_of_balances": "bool"}
    attribute_map = {
        "days_overdue": "days_overdue",
        "table_of_balances": "table_of_balances",
    }

    def __init__(
        self, days_overdue=None, table_of_balances=None, local_vars_configuration=None
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._days_overdue = None
        self._table_of_balances = None
        self.discriminator = None
        if days_overdue is not None:
            self.days_overdue = days_overdue
        if table_of_balances is not None:
            self.table_of_balances = table_of_balances

    @property
    def days_overdue(self):
        return self._days_overdue

    @days_overdue.setter
    def days_overdue(self, days_overdue):
        self._days_overdue = days_overdue

    @property
    def table_of_balances(self):
        return self._table_of_balances

    @table_of_balances.setter
    def table_of_balances(self, table_of_balances):
        self._table_of_balances = table_of_balances

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
        if not isinstance(other, PutInvoiceSettingsInvoiceSettingsPrintStatements):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PutInvoiceSettingsInvoiceSettingsPrintStatements):
            return True
        return self.to_dict() != other.to_dict()
