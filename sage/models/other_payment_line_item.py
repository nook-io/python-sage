import pprint
import six
from sage.configuration import Configuration


class OtherPaymentLineItem(object):
    openapi_types = {
        "id": "str",
        "displayed_as": "str",
        "ledger_account": "Base",
        "details": "str",
        "tax_rate": "Base",
        "net_amount": "float",
        "tax_amount": "float",
        "total_amount": "float",
        "tax_breakdown": "list[TaxBreakdown]",
        "is_purchase_for_resale": "bool",
        "trade_of_asset": "bool",
        "gst_amount": "float",
        "pst_amount": "float",
        "tax_recoverable": "bool",
    }
    attribute_map = {
        "id": "id",
        "displayed_as": "displayed_as",
        "ledger_account": "ledger_account",
        "details": "details",
        "tax_rate": "tax_rate",
        "net_amount": "net_amount",
        "tax_amount": "tax_amount",
        "total_amount": "total_amount",
        "tax_breakdown": "tax_breakdown",
        "is_purchase_for_resale": "is_purchase_for_resale",
        "trade_of_asset": "trade_of_asset",
        "gst_amount": "gst_amount",
        "pst_amount": "pst_amount",
        "tax_recoverable": "tax_recoverable",
    }

    def __init__(
        self,
        id=None,
        displayed_as=None,
        ledger_account=None,
        details=None,
        tax_rate=None,
        net_amount=None,
        tax_amount=None,
        total_amount=None,
        tax_breakdown=None,
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
        self._id = None
        self._displayed_as = None
        self._ledger_account = None
        self._details = None
        self._tax_rate = None
        self._net_amount = None
        self._tax_amount = None
        self._total_amount = None
        self._tax_breakdown = None
        self._is_purchase_for_resale = None
        self._trade_of_asset = None
        self._gst_amount = None
        self._pst_amount = None
        self._tax_recoverable = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if displayed_as is not None:
            self.displayed_as = displayed_as
        if ledger_account is not None:
            self.ledger_account = ledger_account
        if details is not None:
            self.details = details
        if tax_rate is not None:
            self.tax_rate = tax_rate
        if net_amount is not None:
            self.net_amount = net_amount
        if tax_amount is not None:
            self.tax_amount = tax_amount
        if total_amount is not None:
            self.total_amount = total_amount
        if tax_breakdown is not None:
            self.tax_breakdown = tax_breakdown
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
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def displayed_as(self):
        return self._displayed_as

    @displayed_as.setter
    def displayed_as(self, displayed_as):
        self._displayed_as = displayed_as

    @property
    def ledger_account(self):
        return self._ledger_account

    @ledger_account.setter
    def ledger_account(self, ledger_account):
        self._ledger_account = ledger_account

    @property
    def details(self):
        return self._details

    @details.setter
    def details(self, details):
        self._details = details

    @property
    def tax_rate(self):
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, tax_rate):
        self._tax_rate = tax_rate

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
    def tax_breakdown(self):
        return self._tax_breakdown

    @tax_breakdown.setter
    def tax_breakdown(self, tax_breakdown):
        self._tax_breakdown = tax_breakdown

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
        if not isinstance(other, OtherPaymentLineItem):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, OtherPaymentLineItem):
            return True
        return self.to_dict() != other.to_dict()
