import pprint
import six
from sage.configuration import Configuration


class PostPurchaseCorrectiveInvoicesPurchaseCorrectiveInvoiceTaxAnalysis(object):
    openapi_types = {
        "tax_rate_id": "str",
        "net_amount": "float",
        "tax_amount": "float",
        "total_amount": "float",
        "goods_amount": "float",
        "service_amount": "float",
    }
    attribute_map = {
        "tax_rate_id": "tax_rate_id",
        "net_amount": "net_amount",
        "tax_amount": "tax_amount",
        "total_amount": "total_amount",
        "goods_amount": "goods_amount",
        "service_amount": "service_amount",
    }

    def __init__(
        self,
        tax_rate_id=None,
        net_amount=None,
        tax_amount=None,
        total_amount=None,
        goods_amount=None,
        service_amount=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._tax_rate_id = None
        self._net_amount = None
        self._tax_amount = None
        self._total_amount = None
        self._goods_amount = None
        self._service_amount = None
        self.discriminator = None
        if tax_rate_id is not None:
            self.tax_rate_id = tax_rate_id
        if net_amount is not None:
            self.net_amount = net_amount
        if tax_amount is not None:
            self.tax_amount = tax_amount
        if total_amount is not None:
            self.total_amount = total_amount
        if goods_amount is not None:
            self.goods_amount = goods_amount
        if service_amount is not None:
            self.service_amount = service_amount

    @property
    def tax_rate_id(self):
        return self._tax_rate_id

    @tax_rate_id.setter
    def tax_rate_id(self, tax_rate_id):
        self._tax_rate_id = tax_rate_id

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
    def service_amount(self):
        return self._service_amount

    @service_amount.setter
    def service_amount(self, service_amount):
        self._service_amount = service_amount

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
        if not isinstance(
            other, PostPurchaseCorrectiveInvoicesPurchaseCorrectiveInvoiceTaxAnalysis
        ):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(
            other, PostPurchaseCorrectiveInvoicesPurchaseCorrectiveInvoiceTaxAnalysis
        ):
            return True
        return self.to_dict() != other.to_dict()
