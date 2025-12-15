import pprint
import six
from sage.configuration import Configuration


class PutOtherPaymentsOtherPaymentPaymentLines(object):
    openapi_types = {
        "ledger_account_id": "str",
        "total_amount": "float",
        "details": "str",
        "tax_rate_id": "str",
        "net_amount": "float",
        "tax_amount": "float",
        "is_purchase_for_resale": "bool",
        "trade_of_asset": "bool",
        "gst_amount": "float",
        "pst_amount": "float",
        "tax_recoverable": "bool",
    }
    attribute_map = {
        "ledger_account_id": "ledger_account_id",
        "total_amount": "total_amount",
        "details": "details",
        "tax_rate_id": "tax_rate_id",
        "net_amount": "net_amount",
        "tax_amount": "tax_amount",
        "is_purchase_for_resale": "is_purchase_for_resale",
        "trade_of_asset": "trade_of_asset",
        "gst_amount": "gst_amount",
        "pst_amount": "pst_amount",
        "tax_recoverable": "tax_recoverable",
    }

    def __init__(
        self,
        ledger_account_id=None,
        total_amount=None,
        details=None,
        tax_rate_id=None,
        net_amount=None,
        tax_amount=None,
        is_purchase_for_resale=None,
        trade_of_asset=None,
        gst_amount=None,
        pst_amount=None,
        tax_recoverable=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._ledger_account_id = None
        self._total_amount = None
        self._details = None
        self._tax_rate_id = None
        self._net_amount = None
        self._tax_amount = None
        self._is_purchase_for_resale = None
        self._trade_of_asset = None
        self._gst_amount = None
        self._pst_amount = None
        self._tax_recoverable = None
        self.discriminator = None
        if ledger_account_id is not None:
            self.ledger_account_id = ledger_account_id
        if total_amount is not None:
            self.total_amount = total_amount
        if details is not None:
            self.details = details
        if tax_rate_id is not None:
            self.tax_rate_id = tax_rate_id
        if net_amount is not None:
            self.net_amount = net_amount
        if tax_amount is not None:
            self.tax_amount = tax_amount
        if is_purchase_for_resale is not None:
            self.is_purchase_for_resale = is_purchase_for_resale
        if trade_of_asset is not None:
            self.trade_of_asset = trade_of_asset
        if gst_amount is not None:
            self.gst_amount = gst_amount
        if pst_amount is not None:
            self.pst_amount = pst_amount
        if tax_recoverable is not None:
            self.tax_recoverable = tax_recoverable

    @property
    def ledger_account_id(self):
        return self._ledger_account_id

    @ledger_account_id.setter
    def ledger_account_id(self, ledger_account_id):
        self._ledger_account_id = ledger_account_id

    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        self._total_amount = total_amount

    @property
    def details(self):
        return self._details

    @details.setter
    def details(self, details):
        self._details = details

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
    def is_purchase_for_resale(self):
        return self._is_purchase_for_resale

    @is_purchase_for_resale.setter
    def is_purchase_for_resale(self, is_purchase_for_resale):
        self._is_purchase_for_resale = is_purchase_for_resale

    @property
    def trade_of_asset(self):
        return self._trade_of_asset

    @trade_of_asset.setter
    def trade_of_asset(self, trade_of_asset):
        self._trade_of_asset = trade_of_asset

    @property
    def gst_amount(self):
        return self._gst_amount

    @gst_amount.setter
    def gst_amount(self, gst_amount):
        self._gst_amount = gst_amount

    @property
    def pst_amount(self):
        return self._pst_amount

    @pst_amount.setter
    def pst_amount(self, pst_amount):
        self._pst_amount = pst_amount

    @property
    def tax_recoverable(self):
        return self._tax_recoverable

    @tax_recoverable.setter
    def tax_recoverable(self, tax_recoverable):
        self._tax_recoverable = tax_recoverable

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
        if not isinstance(other, PutOtherPaymentsOtherPaymentPaymentLines):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PutOtherPaymentsOtherPaymentPaymentLines):
            return True
        return self.to_dict() != other.to_dict()
