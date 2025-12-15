import pprint
import six
from sage.configuration import Configuration


class PutBusinessSettingsBusinessSettingsDefaultLedgerAccounts(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        "bank_charges_ledger_account_id": "str",
        "bank_interest_received_ledger_account_id": "str",
        "bank_interest_charges_paid_ledger_account_id": "str",
        "exchange_rate_gains_ledger_account_id": "str",
        "exchange_rate_losses_ledger_account_id": "str",
        "sales_ledger_account_id": "str",
        "sales_discount_ledger_account_id": "str",
        "purchase_ledger_account_id": "str",
        "purchase_discount_ledger_account_id": "str",
        "product_sales_ledger_account_id": "str",
        "product_purchase_ledger_account_id": "str",
        "service_sales_ledger_account_id": "str",
        "service_purchase_ledger_account_id": "str",
        "stock_purchase_ledger_account_id": "str",
        "other_receipt_ledger_account_id": "str",
        "other_payment_ledger_account_id": "str",
        "customer_receipt_discount_ledger_account_id": "str",
        "vendor_payment_discount_ledger_account_id": "str",
        "carriage_ledger_account_id": "str",
    }
    attribute_map = {
        "bank_charges_ledger_account_id": "bank_charges_ledger_account_id",
        "bank_interest_received_ledger_account_id": "bank_interest_received_ledger_account_id",
        "bank_interest_charges_paid_ledger_account_id": "bank_interest_charges_paid_ledger_account_id",
        "exchange_rate_gains_ledger_account_id": "exchange_rate_gains_ledger_account_id",
        "exchange_rate_losses_ledger_account_id": "exchange_rate_losses_ledger_account_id",
        "sales_ledger_account_id": "sales_ledger_account_id",
        "sales_discount_ledger_account_id": "sales_discount_ledger_account_id",
        "purchase_ledger_account_id": "purchase_ledger_account_id",
        "purchase_discount_ledger_account_id": "purchase_discount_ledger_account_id",
        "product_sales_ledger_account_id": "product_sales_ledger_account_id",
        "product_purchase_ledger_account_id": "product_purchase_ledger_account_id",
        "service_sales_ledger_account_id": "service_sales_ledger_account_id",
        "service_purchase_ledger_account_id": "service_purchase_ledger_account_id",
        "stock_purchase_ledger_account_id": "stock_purchase_ledger_account_id",
        "other_receipt_ledger_account_id": "other_receipt_ledger_account_id",
        "other_payment_ledger_account_id": "other_payment_ledger_account_id",
        "customer_receipt_discount_ledger_account_id": "customer_receipt_discount_ledger_account_id",
        "vendor_payment_discount_ledger_account_id": "vendor_payment_discount_ledger_account_id",
        "carriage_ledger_account_id": "carriage_ledger_account_id",
    }

    def __init__(
        self,
        bank_charges_ledger_account_id=None,
        bank_interest_received_ledger_account_id=None,
        bank_interest_charges_paid_ledger_account_id=None,
        exchange_rate_gains_ledger_account_id=None,
        exchange_rate_losses_ledger_account_id=None,
        sales_ledger_account_id=None,
        sales_discount_ledger_account_id=None,
        purchase_ledger_account_id=None,
        purchase_discount_ledger_account_id=None,
        product_sales_ledger_account_id=None,
        product_purchase_ledger_account_id=None,
        service_sales_ledger_account_id=None,
        service_purchase_ledger_account_id=None,
        stock_purchase_ledger_account_id=None,
        other_receipt_ledger_account_id=None,
        other_payment_ledger_account_id=None,
        customer_receipt_discount_ledger_account_id=None,
        vendor_payment_discount_ledger_account_id=None,
        carriage_ledger_account_id=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._bank_charges_ledger_account_id = None
        self._bank_interest_received_ledger_account_id = None
        self._bank_interest_charges_paid_ledger_account_id = None
        self._exchange_rate_gains_ledger_account_id = None
        self._exchange_rate_losses_ledger_account_id = None
        self._sales_ledger_account_id = None
        self._sales_discount_ledger_account_id = None
        self._purchase_ledger_account_id = None
        self._purchase_discount_ledger_account_id = None
        self._product_sales_ledger_account_id = None
        self._product_purchase_ledger_account_id = None
        self._service_sales_ledger_account_id = None
        self._service_purchase_ledger_account_id = None
        self._stock_purchase_ledger_account_id = None
        self._other_receipt_ledger_account_id = None
        self._other_payment_ledger_account_id = None
        self._customer_receipt_discount_ledger_account_id = None
        self._vendor_payment_discount_ledger_account_id = None
        self._carriage_ledger_account_id = None
        self.discriminator = None
        if bank_charges_ledger_account_id is not None:
            self.bank_charges_ledger_account_id = bank_charges_ledger_account_id
        if bank_interest_received_ledger_account_id is not None:
            self.bank_interest_received_ledger_account_id = (
                bank_interest_received_ledger_account_id
            )
        if bank_interest_charges_paid_ledger_account_id is not None:
            self.bank_interest_charges_paid_ledger_account_id = (
                bank_interest_charges_paid_ledger_account_id
            )
        if exchange_rate_gains_ledger_account_id is not None:
            self.exchange_rate_gains_ledger_account_id = (
                exchange_rate_gains_ledger_account_id
            )
        if exchange_rate_losses_ledger_account_id is not None:
            self.exchange_rate_losses_ledger_account_id = (
                exchange_rate_losses_ledger_account_id
            )
        if sales_ledger_account_id is not None:
            self.sales_ledger_account_id = sales_ledger_account_id
        if sales_discount_ledger_account_id is not None:
            self.sales_discount_ledger_account_id = sales_discount_ledger_account_id
        if purchase_ledger_account_id is not None:
            self.purchase_ledger_account_id = purchase_ledger_account_id
        if purchase_discount_ledger_account_id is not None:
            self.purchase_discount_ledger_account_id = (
                purchase_discount_ledger_account_id
            )
        if product_sales_ledger_account_id is not None:
            self.product_sales_ledger_account_id = product_sales_ledger_account_id
        if product_purchase_ledger_account_id is not None:
            self.product_purchase_ledger_account_id = product_purchase_ledger_account_id
        if service_sales_ledger_account_id is not None:
            self.service_sales_ledger_account_id = service_sales_ledger_account_id
        if service_purchase_ledger_account_id is not None:
            self.service_purchase_ledger_account_id = service_purchase_ledger_account_id
        if stock_purchase_ledger_account_id is not None:
            self.stock_purchase_ledger_account_id = stock_purchase_ledger_account_id
        if other_receipt_ledger_account_id is not None:
            self.other_receipt_ledger_account_id = other_receipt_ledger_account_id
        if other_payment_ledger_account_id is not None:
            self.other_payment_ledger_account_id = other_payment_ledger_account_id
        if customer_receipt_discount_ledger_account_id is not None:
            self.customer_receipt_discount_ledger_account_id = (
                customer_receipt_discount_ledger_account_id
            )
        if vendor_payment_discount_ledger_account_id is not None:
            self.vendor_payment_discount_ledger_account_id = (
                vendor_payment_discount_ledger_account_id
            )
        if carriage_ledger_account_id is not None:
            self.carriage_ledger_account_id = carriage_ledger_account_id

    @property
    def bank_charges_ledger_account_id(self):
        return self._bank_charges_ledger_account_id

    @bank_charges_ledger_account_id.setter
    def bank_charges_ledger_account_id(self, bank_charges_ledger_account_id):
        self._bank_charges_ledger_account_id = bank_charges_ledger_account_id

    @property
    def bank_interest_received_ledger_account_id(self):
        return self._bank_interest_received_ledger_account_id

    @bank_interest_received_ledger_account_id.setter
    def bank_interest_received_ledger_account_id(
        self, bank_interest_received_ledger_account_id
    ):
        self._bank_interest_received_ledger_account_id = (
            bank_interest_received_ledger_account_id
        )

    @property
    def bank_interest_charges_paid_ledger_account_id(self):
        return self._bank_interest_charges_paid_ledger_account_id

    @bank_interest_charges_paid_ledger_account_id.setter
    def bank_interest_charges_paid_ledger_account_id(
        self, bank_interest_charges_paid_ledger_account_id
    ):
        self._bank_interest_charges_paid_ledger_account_id = (
            bank_interest_charges_paid_ledger_account_id
        )

    @property
    def exchange_rate_gains_ledger_account_id(self):
        return self._exchange_rate_gains_ledger_account_id

    @exchange_rate_gains_ledger_account_id.setter
    def exchange_rate_gains_ledger_account_id(
        self, exchange_rate_gains_ledger_account_id
    ):
        self._exchange_rate_gains_ledger_account_id = (
            exchange_rate_gains_ledger_account_id
        )

    @property
    def exchange_rate_losses_ledger_account_id(self):
        return self._exchange_rate_losses_ledger_account_id

    @exchange_rate_losses_ledger_account_id.setter
    def exchange_rate_losses_ledger_account_id(
        self, exchange_rate_losses_ledger_account_id
    ):
        self._exchange_rate_losses_ledger_account_id = (
            exchange_rate_losses_ledger_account_id
        )

    @property
    def sales_ledger_account_id(self):
        return self._sales_ledger_account_id

    @sales_ledger_account_id.setter
    def sales_ledger_account_id(self, sales_ledger_account_id):
        self._sales_ledger_account_id = sales_ledger_account_id

    @property
    def sales_discount_ledger_account_id(self):
        return self._sales_discount_ledger_account_id

    @sales_discount_ledger_account_id.setter
    def sales_discount_ledger_account_id(self, sales_discount_ledger_account_id):
        self._sales_discount_ledger_account_id = sales_discount_ledger_account_id

    @property
    def purchase_ledger_account_id(self):
        return self._purchase_ledger_account_id

    @purchase_ledger_account_id.setter
    def purchase_ledger_account_id(self, purchase_ledger_account_id):
        self._purchase_ledger_account_id = purchase_ledger_account_id

    @property
    def purchase_discount_ledger_account_id(self):
        return self._purchase_discount_ledger_account_id

    @purchase_discount_ledger_account_id.setter
    def purchase_discount_ledger_account_id(self, purchase_discount_ledger_account_id):
        self._purchase_discount_ledger_account_id = purchase_discount_ledger_account_id

    @property
    def product_sales_ledger_account_id(self):
        return self._product_sales_ledger_account_id

    @product_sales_ledger_account_id.setter
    def product_sales_ledger_account_id(self, product_sales_ledger_account_id):
        self._product_sales_ledger_account_id = product_sales_ledger_account_id

    @property
    def product_purchase_ledger_account_id(self):
        return self._product_purchase_ledger_account_id

    @product_purchase_ledger_account_id.setter
    def product_purchase_ledger_account_id(self, product_purchase_ledger_account_id):
        self._product_purchase_ledger_account_id = product_purchase_ledger_account_id

    @property
    def service_sales_ledger_account_id(self):
        return self._service_sales_ledger_account_id

    @service_sales_ledger_account_id.setter
    def service_sales_ledger_account_id(self, service_sales_ledger_account_id):
        self._service_sales_ledger_account_id = service_sales_ledger_account_id

    @property
    def service_purchase_ledger_account_id(self):
        return self._service_purchase_ledger_account_id

    @service_purchase_ledger_account_id.setter
    def service_purchase_ledger_account_id(self, service_purchase_ledger_account_id):
        self._service_purchase_ledger_account_id = service_purchase_ledger_account_id

    @property
    def stock_purchase_ledger_account_id(self):
        return self._stock_purchase_ledger_account_id

    @stock_purchase_ledger_account_id.setter
    def stock_purchase_ledger_account_id(self, stock_purchase_ledger_account_id):
        self._stock_purchase_ledger_account_id = stock_purchase_ledger_account_id

    @property
    def other_receipt_ledger_account_id(self):
        return self._other_receipt_ledger_account_id

    @other_receipt_ledger_account_id.setter
    def other_receipt_ledger_account_id(self, other_receipt_ledger_account_id):
        self._other_receipt_ledger_account_id = other_receipt_ledger_account_id

    @property
    def other_payment_ledger_account_id(self):
        return self._other_payment_ledger_account_id

    @other_payment_ledger_account_id.setter
    def other_payment_ledger_account_id(self, other_payment_ledger_account_id):
        self._other_payment_ledger_account_id = other_payment_ledger_account_id

    @property
    def customer_receipt_discount_ledger_account_id(self):
        return self._customer_receipt_discount_ledger_account_id

    @customer_receipt_discount_ledger_account_id.setter
    def customer_receipt_discount_ledger_account_id(
        self, customer_receipt_discount_ledger_account_id
    ):
        self._customer_receipt_discount_ledger_account_id = (
            customer_receipt_discount_ledger_account_id
        )

    @property
    def vendor_payment_discount_ledger_account_id(self):
        return self._vendor_payment_discount_ledger_account_id

    @vendor_payment_discount_ledger_account_id.setter
    def vendor_payment_discount_ledger_account_id(
        self, vendor_payment_discount_ledger_account_id
    ):
        self._vendor_payment_discount_ledger_account_id = (
            vendor_payment_discount_ledger_account_id
        )

    @property
    def carriage_ledger_account_id(self):
        return self._carriage_ledger_account_id

    @carriage_ledger_account_id.setter
    def carriage_ledger_account_id(self, carriage_ledger_account_id):
        self._carriage_ledger_account_id = carriage_ledger_account_id

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
            other, PutBusinessSettingsBusinessSettingsDefaultLedgerAccounts
        ):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(
            other, PutBusinessSettingsBusinessSettingsDefaultLedgerAccounts
        ):
            return True
        return self.to_dict() != other.to_dict()
