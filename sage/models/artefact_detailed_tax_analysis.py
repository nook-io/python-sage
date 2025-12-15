import pprint
import six
from sage.configuration import Configuration


class ArtefactDetailedTaxAnalysis(object):
    openapi_types = {
        "tax_rates_breakdown": "ArtefactDetailedTaxAnalysisBreakdown",
        "total_net": "float",
        "total_tax": "float",
        "total": "float",
        "total_goods_amount": "float",
        "total_services_amount": "float",
        "base_currency_total_net": "float",
        "base_currency_total_tax": "float",
        "base_currency_total": "float",
        "base_currency_total_goods_amount": "float",
        "base_currency_total_services_amount": "float",
        "total_retailer_tax": "float",
    }
    attribute_map = {
        "tax_rates_breakdown": "tax_rates_breakdown",
        "total_net": "total_net",
        "total_tax": "total_tax",
        "total": "total",
        "total_goods_amount": "total_goods_amount",
        "total_services_amount": "total_services_amount",
        "base_currency_total_net": "base_currency_total_net",
        "base_currency_total_tax": "base_currency_total_tax",
        "base_currency_total": "base_currency_total",
        "base_currency_total_goods_amount": "base_currency_total_goods_amount",
        "base_currency_total_services_amount": "base_currency_total_services_amount",
        "total_retailer_tax": "total_retailer_tax",
    }

    def __init__(
        self,
        tax_rates_breakdown=None,
        total_net=None,
        total_tax=None,
        total=None,
        total_goods_amount=None,
        total_services_amount=None,
        base_currency_total_net=None,
        base_currency_total_tax=None,
        base_currency_total=None,
        base_currency_total_goods_amount=None,
        base_currency_total_services_amount=None,
        total_retailer_tax=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._tax_rates_breakdown = None
        self._total_net = None
        self._total_tax = None
        self._total = None
        self._total_goods_amount = None
        self._total_services_amount = None
        self._base_currency_total_net = None
        self._base_currency_total_tax = None
        self._base_currency_total = None
        self._base_currency_total_goods_amount = None
        self._base_currency_total_services_amount = None
        self._total_retailer_tax = None
        self.discriminator = None
        if tax_rates_breakdown is not None:
            self.tax_rates_breakdown = tax_rates_breakdown
        if total_net is not None:
            self.total_net = total_net
        if total_tax is not None:
            self.total_tax = total_tax
        if total is not None:
            self.total = total
        if total_goods_amount is not None:
            self.total_goods_amount = total_goods_amount
        if total_services_amount is not None:
            self.total_services_amount = total_services_amount
        if base_currency_total_net is not None:
            self.base_currency_total_net = base_currency_total_net
        if base_currency_total_tax is not None:
            self.base_currency_total_tax = base_currency_total_tax
        if base_currency_total is not None:
            self.base_currency_total = base_currency_total
        if base_currency_total_goods_amount is not None:
            self.base_currency_total_goods_amount = base_currency_total_goods_amount
        if base_currency_total_services_amount is not None:
            self.base_currency_total_services_amount = (
                base_currency_total_services_amount
            )
        if total_retailer_tax is not None:
            self.total_retailer_tax = total_retailer_tax

    @property
    def tax_rates_breakdown(self):
        return self._tax_rates_breakdown

    @tax_rates_breakdown.setter
    def tax_rates_breakdown(self, tax_rates_breakdown):
        self._tax_rates_breakdown = tax_rates_breakdown

    @property
    def total_net(self):
        return self._total_net

    @total_net.setter
    def total_net(self, total_net):
        self._total_net = total_net

    @property
    def total_tax(self):
        return self._total_tax

    @total_tax.setter
    def total_tax(self, total_tax):
        self._total_tax = total_tax

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, total):
        self._total = total

    @property
    def total_goods_amount(self):
        return self._total_goods_amount

    @total_goods_amount.setter
    def total_goods_amount(self, total_goods_amount):
        self._total_goods_amount = total_goods_amount

    @property
    def total_services_amount(self):
        return self._total_services_amount

    @total_services_amount.setter
    def total_services_amount(self, total_services_amount):
        self._total_services_amount = total_services_amount

    @property
    def base_currency_total_net(self):
        return self._base_currency_total_net

    @base_currency_total_net.setter
    def base_currency_total_net(self, base_currency_total_net):
        self._base_currency_total_net = base_currency_total_net

    @property
    def base_currency_total_tax(self):
        return self._base_currency_total_tax

    @base_currency_total_tax.setter
    def base_currency_total_tax(self, base_currency_total_tax):
        self._base_currency_total_tax = base_currency_total_tax

    @property
    def base_currency_total(self):
        return self._base_currency_total

    @base_currency_total.setter
    def base_currency_total(self, base_currency_total):
        self._base_currency_total = base_currency_total

    @property
    def base_currency_total_goods_amount(self):
        return self._base_currency_total_goods_amount

    @base_currency_total_goods_amount.setter
    def base_currency_total_goods_amount(self, base_currency_total_goods_amount):
        self._base_currency_total_goods_amount = base_currency_total_goods_amount

    @property
    def base_currency_total_services_amount(self):
        return self._base_currency_total_services_amount

    @base_currency_total_services_amount.setter
    def base_currency_total_services_amount(self, base_currency_total_services_amount):
        self._base_currency_total_services_amount = base_currency_total_services_amount

    @property
    def total_retailer_tax(self):
        return self._total_retailer_tax

    @total_retailer_tax.setter
    def total_retailer_tax(self, total_retailer_tax):
        self._total_retailer_tax = total_retailer_tax

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
        if not isinstance(other, ArtefactDetailedTaxAnalysis):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, ArtefactDetailedTaxAnalysis):
            return True
        return self.to_dict() != other.to_dict()
