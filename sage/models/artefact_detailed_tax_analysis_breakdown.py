import pprint
import six
from sage.configuration import Configuration


class ArtefactDetailedTaxAnalysisBreakdown(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        "tax_rate": "TaxRate",
        "name": "str",
        "percentage": "float",
        "net_amount": "float",
        "tax_amount": "float",
        "retail_tax_amount": "float",
        "total_amount": "float",
        "goods_amount": "float",
        "services_amount": "float",
        "base_currency_net_amount": "float",
        "base_currency_tax_amount": "float",
        "base_currency_total_amount": "float",
        "base_currency_goods_amount": "float",
        "base_currency_services_amount": "float",
    }
    attribute_map = {
        "tax_rate": "tax_rate",
        "name": "name",
        "percentage": "percentage",
        "net_amount": "net_amount",
        "tax_amount": "tax_amount",
        "retail_tax_amount": "retail_tax_amount",
        "total_amount": "total_amount",
        "goods_amount": "goods_amount",
        "services_amount": "services_amount",
        "base_currency_net_amount": "base_currency_net_amount",
        "base_currency_tax_amount": "base_currency_tax_amount",
        "base_currency_total_amount": "base_currency_total_amount",
        "base_currency_goods_amount": "base_currency_goods_amount",
        "base_currency_services_amount": "base_currency_services_amount",
    }

    def __init__(
        self,
        tax_rate=None,
        name=None,
        percentage=None,
        net_amount=None,
        tax_amount=None,
        retail_tax_amount=None,
        total_amount=None,
        goods_amount=None,
        services_amount=None,
        base_currency_net_amount=None,
        base_currency_tax_amount=None,
        base_currency_total_amount=None,
        base_currency_goods_amount=None,
        base_currency_services_amount=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._tax_rate = None
        self._name = None
        self._percentage = None
        self._net_amount = None
        self._tax_amount = None
        self._retail_tax_amount = None
        self._total_amount = None
        self._goods_amount = None
        self._services_amount = None
        self._base_currency_net_amount = None
        self._base_currency_tax_amount = None
        self._base_currency_total_amount = None
        self._base_currency_goods_amount = None
        self._base_currency_services_amount = None
        self.discriminator = None
        if tax_rate is not None:
            self.tax_rate = tax_rate
        if name is not None:
            self.name = name
        if percentage is not None:
            self.percentage = percentage
        if net_amount is not None:
            self.net_amount = net_amount
        if tax_amount is not None:
            self.tax_amount = tax_amount
        if retail_tax_amount is not None:
            self.retail_tax_amount = retail_tax_amount
        if total_amount is not None:
            self.total_amount = total_amount
        if goods_amount is not None:
            self.goods_amount = goods_amount
        if services_amount is not None:
            self.services_amount = services_amount
        if base_currency_net_amount is not None:
            self.base_currency_net_amount = base_currency_net_amount
        if base_currency_tax_amount is not None:
            self.base_currency_tax_amount = base_currency_tax_amount
        if base_currency_total_amount is not None:
            self.base_currency_total_amount = base_currency_total_amount
        if base_currency_goods_amount is not None:
            self.base_currency_goods_amount = base_currency_goods_amount
        if base_currency_services_amount is not None:
            self.base_currency_services_amount = base_currency_services_amount

    @property
    def tax_rate(self):
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, tax_rate):
        self._tax_rate = tax_rate

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def percentage(self):
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        self._percentage = percentage

    @property
    def net_amount(self):
        return self._net_amount

    @net_amount.setter
    def net_amount(self, net_amount):
        self._net_amount = net_amount

    @property
    def tax_amount(self):
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        self._tax_amount = tax_amount

    @property
    def retail_tax_amount(self):
        return self._retail_tax_amount

    @retail_tax_amount.setter
    def retail_tax_amount(self, retail_tax_amount):
        self._retail_tax_amount = retail_tax_amount

    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        self._total_amount = total_amount

    @property
    def goods_amount(self):
        return self._goods_amount

    @goods_amount.setter
    def goods_amount(self, goods_amount):
        self._goods_amount = goods_amount

    @property
    def services_amount(self):
        return self._services_amount

    @services_amount.setter
    def services_amount(self, services_amount):
        self._services_amount = services_amount

    @property
    def base_currency_net_amount(self):
        return self._base_currency_net_amount

    @base_currency_net_amount.setter
    def base_currency_net_amount(self, base_currency_net_amount):
        self._base_currency_net_amount = base_currency_net_amount

    @property
    def base_currency_tax_amount(self):
        return self._base_currency_tax_amount

    @base_currency_tax_amount.setter
    def base_currency_tax_amount(self, base_currency_tax_amount):
        self._base_currency_tax_amount = base_currency_tax_amount

    @property
    def base_currency_total_amount(self):
        return self._base_currency_total_amount

    @base_currency_total_amount.setter
    def base_currency_total_amount(self, base_currency_total_amount):
        self._base_currency_total_amount = base_currency_total_amount

    @property
    def base_currency_goods_amount(self):
        return self._base_currency_goods_amount

    @base_currency_goods_amount.setter
    def base_currency_goods_amount(self, base_currency_goods_amount):
        self._base_currency_goods_amount = base_currency_goods_amount

    @property
    def base_currency_services_amount(self):
        return self._base_currency_services_amount

    @base_currency_services_amount.setter
    def base_currency_services_amount(self, base_currency_services_amount):
        self._base_currency_services_amount = base_currency_services_amount

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
        if not isinstance(other, ArtefactDetailedTaxAnalysisBreakdown):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, ArtefactDetailedTaxAnalysisBreakdown):
            return True
        return self.to_dict() != other.to_dict()
