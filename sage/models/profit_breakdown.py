import pprint
import six
from sage.configuration import Configuration


class ProfitBreakdown(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        "description": "str",
        "total_cost": "float",
        "total_sale": "float",
        "profit": "float",
        "profit_percentage": "float",
    }
    attribute_map = {
        "description": "description",
        "total_cost": "total_cost",
        "total_sale": "total_sale",
        "profit": "profit",
        "profit_percentage": "profit_percentage",
    }

    def __init__(
        self,
        description=None,
        total_cost=None,
        total_sale=None,
        profit=None,
        profit_percentage=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._description = None
        self._total_cost = None
        self._total_sale = None
        self._profit = None
        self._profit_percentage = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if total_cost is not None:
            self.total_cost = total_cost
        if total_sale is not None:
            self.total_sale = total_sale
        if profit is not None:
            self.profit = profit
        if profit_percentage is not None:
            self.profit_percentage = profit_percentage

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def total_cost(self):
        return self._total_cost

    @total_cost.setter
    def total_cost(self, total_cost):
        self._total_cost = total_cost

    @property
    def total_sale(self):
        return self._total_sale

    @total_sale.setter
    def total_sale(self, total_sale):
        self._total_sale = total_sale

    @property
    def profit(self):
        return self._profit

    @profit.setter
    def profit(self, profit):
        self._profit = profit

    @property
    def profit_percentage(self):
        return self._profit_percentage

    @profit_percentage.setter
    def profit_percentage(self, profit_percentage):
        self._profit_percentage = profit_percentage

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
        if not isinstance(other, ProfitBreakdown):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, ProfitBreakdown):
            return True
        return self.to_dict() != other.to_dict()
