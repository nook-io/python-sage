import pprint
import six
from sage.configuration import Configuration


class DefaultLedgerAccounts(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        "bank_charges_ledger_account": "Base",
        "bank_interest_received_ledger_account": "Base",
        "bank_interest_charges_paid_ledger_account": "Base",
        "exchange_rate_gains_ledger_account": "Base",
        "exchange_rate_losses_ledger_account": "Base",
        "sales_ledger_account": "Base",
        "sales_discount_ledger_account": "Base",
        "purchase_ledger_account": "Base",
        "purchase_discount_ledger_account": "Base",
        "product_sales_ledger_account": "Base",
        "product_purchase_ledger_account": "Base",
        "service_sales_ledger_account": "Base",
        "service_purchase_ledger_account": "Base",
        "stock_purchase_ledger_account": "Base",
        "other_receipt_ledger_account": "Base",
        "other_payment_ledger_account": "Base",
        "customer_receipt_discount_ledger_account": "Base",
        "vendor_payment_discount_ledger_account": "Base",
        "carriage_ledger_account": "Base",
    }
    attribute_map = {
        "bank_charges_ledger_account": "bank_charges_ledger_account",
        "bank_interest_received_ledger_account": "bank_interest_received_ledger_account",
        "bank_interest_charges_paid_ledger_account": "bank_interest_charges_paid_ledger_account",
        "exchange_rate_gains_ledger_account": "exchange_rate_gains_ledger_account",
        "exchange_rate_losses_ledger_account": "exchange_rate_losses_ledger_account",
        "sales_ledger_account": "sales_ledger_account",
        "sales_discount_ledger_account": "sales_discount_ledger_account",
        "purchase_ledger_account": "purchase_ledger_account",
        "purchase_discount_ledger_account": "purchase_discount_ledger_account",
        "product_sales_ledger_account": "product_sales_ledger_account",
        "product_purchase_ledger_account": "product_purchase_ledger_account",
        "service_sales_ledger_account": "service_sales_ledger_account",
        "service_purchase_ledger_account": "service_purchase_ledger_account",
        "stock_purchase_ledger_account": "stock_purchase_ledger_account",
        "other_receipt_ledger_account": "other_receipt_ledger_account",
        "other_payment_ledger_account": "other_payment_ledger_account",
        "customer_receipt_discount_ledger_account": "customer_receipt_discount_ledger_account",
        "vendor_payment_discount_ledger_account": "vendor_payment_discount_ledger_account",
        "carriage_ledger_account": "carriage_ledger_account",
    }

    def __init__(
        self,
        bank_charges_ledger_account=None,
        bank_interest_received_ledger_account=None,
        bank_interest_charges_paid_ledger_account=None,
        exchange_rate_gains_ledger_account=None,
        exchange_rate_losses_ledger_account=None,
        sales_ledger_account=None,
        sales_discount_ledger_account=None,
        purchase_ledger_account=None,
        purchase_discount_ledger_account=None,
        product_sales_ledger_account=None,
        product_purchase_ledger_account=None,
        service_sales_ledger_account=None,
        service_purchase_ledger_account=None,
        stock_purchase_ledger_account=None,
        other_receipt_ledger_account=None,
        other_payment_ledger_account=None,
        customer_receipt_discount_ledger_account=None,
        vendor_payment_discount_ledger_account=None,
        carriage_ledger_account=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._bank_charges_ledger_account = None
        self._bank_interest_received_ledger_account = None
        self._bank_interest_charges_paid_ledger_account = None
        self._exchange_rate_gains_ledger_account = None
        self._exchange_rate_losses_ledger_account = None
        self._sales_ledger_account = None
        self._sales_discount_ledger_account = None
        self._purchase_ledger_account = None
        self._purchase_discount_ledger_account = None
        self._product_sales_ledger_account = None
        self._product_purchase_ledger_account = None
        self._service_sales_ledger_account = None
        self._service_purchase_ledger_account = None
        self._stock_purchase_ledger_account = None
        self._other_receipt_ledger_account = None
        self._other_payment_ledger_account = None
        self._customer_receipt_discount_ledger_account = None
        self._vendor_payment_discount_ledger_account = None
        self._carriage_ledger_account = None
        self.discriminator = None
        if bank_charges_ledger_account is not None:
            self.bank_charges_ledger_account = bank_charges_ledger_account
        if bank_interest_received_ledger_account is not None:
            self.bank_interest_received_ledger_account = (
                bank_interest_received_ledger_account
            )
        if bank_interest_charges_paid_ledger_account is not None:
            self.bank_interest_charges_paid_ledger_account = (
                bank_interest_charges_paid_ledger_account
            )
        if exchange_rate_gains_ledger_account is not None:
            self.exchange_rate_gains_ledger_account = exchange_rate_gains_ledger_account
        if exchange_rate_losses_ledger_account is not None:
            self.exchange_rate_losses_ledger_account = (
                exchange_rate_losses_ledger_account
            )
        if sales_ledger_account is not None:
            self.sales_ledger_account = sales_ledger_account
        if sales_discount_ledger_account is not None:
            self.sales_discount_ledger_account = sales_discount_ledger_account
        if purchase_ledger_account is not None:
            self.purchase_ledger_account = purchase_ledger_account
        if purchase_discount_ledger_account is not None:
            self.purchase_discount_ledger_account = purchase_discount_ledger_account
        if product_sales_ledger_account is not None:
            self.product_sales_ledger_account = product_sales_ledger_account
        if product_purchase_ledger_account is not None:
            self.product_purchase_ledger_account = product_purchase_ledger_account
        if service_sales_ledger_account is not None:
            self.service_sales_ledger_account = service_sales_ledger_account
        if service_purchase_ledger_account is not None:
            self.service_purchase_ledger_account = service_purchase_ledger_account
        if stock_purchase_ledger_account is not None:
            self.stock_purchase_ledger_account = stock_purchase_ledger_account
        if other_receipt_ledger_account is not None:
            self.other_receipt_ledger_account = other_receipt_ledger_account
        if other_payment_ledger_account is not None:
            self.other_payment_ledger_account = other_payment_ledger_account
        if customer_receipt_discount_ledger_account is not None:
            self.customer_receipt_discount_ledger_account = (
                customer_receipt_discount_ledger_account
            )
        if vendor_payment_discount_ledger_account is not None:
            self.vendor_payment_discount_ledger_account = (
                vendor_payment_discount_ledger_account
            )
        if carriage_ledger_account is not None:
            self.carriage_ledger_account = carriage_ledger_account

    @property
    def bank_charges_ledger_account(self):
        return self._bank_charges_ledger_account

    @bank_charges_ledger_account.setter
    def bank_charges_ledger_account(self, bank_charges_ledger_account):
        self._bank_charges_ledger_account = bank_charges_ledger_account

    @property
    def bank_interest_received_ledger_account(self):
        return self._bank_interest_received_ledger_account

    @bank_interest_received_ledger_account.setter
    def bank_interest_received_ledger_account(
        self, bank_interest_received_ledger_account
    ):
        self._bank_interest_received_ledger_account = (
            bank_interest_received_ledger_account
        )

    @property
    def bank_interest_charges_paid_ledger_account(self):
        return self._bank_interest_charges_paid_ledger_account

    @bank_interest_charges_paid_ledger_account.setter
    def bank_interest_charges_paid_ledger_account(
        self, bank_interest_charges_paid_ledger_account
    ):
        self._bank_interest_charges_paid_ledger_account = (
            bank_interest_charges_paid_ledger_account
        )

    @property
    def exchange_rate_gains_ledger_account(self):
        return self._exchange_rate_gains_ledger_account

    @exchange_rate_gains_ledger_account.setter
    def exchange_rate_gains_ledger_account(self, exchange_rate_gains_ledger_account):
        self._exchange_rate_gains_ledger_account = exchange_rate_gains_ledger_account

    @property
    def exchange_rate_losses_ledger_account(self):
        return self._exchange_rate_losses_ledger_account

    @exchange_rate_losses_ledger_account.setter
    def exchange_rate_losses_ledger_account(self, exchange_rate_losses_ledger_account):
        self._exchange_rate_losses_ledger_account = exchange_rate_losses_ledger_account

    @property
    def sales_ledger_account(self):
        return self._sales_ledger_account

    @sales_ledger_account.setter
    def sales_ledger_account(self, sales_ledger_account):
        self._sales_ledger_account = sales_ledger_account

    @property
    def sales_discount_ledger_account(self):
        return self._sales_discount_ledger_account

    @sales_discount_ledger_account.setter
    def sales_discount_ledger_account(self, sales_discount_ledger_account):
        self._sales_discount_ledger_account = sales_discount_ledger_account

    @property
    def purchase_ledger_account(self):
        return self._purchase_ledger_account

    @purchase_ledger_account.setter
    def purchase_ledger_account(self, purchase_ledger_account):
        self._purchase_ledger_account = purchase_ledger_account

    @property
    def purchase_discount_ledger_account(self):
        return self._purchase_discount_ledger_account

    @purchase_discount_ledger_account.setter
    def purchase_discount_ledger_account(self, purchase_discount_ledger_account):
        self._purchase_discount_ledger_account = purchase_discount_ledger_account

    @property
    def product_sales_ledger_account(self):
        return self._product_sales_ledger_account

    @product_sales_ledger_account.setter
    def product_sales_ledger_account(self, product_sales_ledger_account):
        self._product_sales_ledger_account = product_sales_ledger_account

    @property
    def product_purchase_ledger_account(self):
        return self._product_purchase_ledger_account

    @product_purchase_ledger_account.setter
    def product_purchase_ledger_account(self, product_purchase_ledger_account):
        self._product_purchase_ledger_account = product_purchase_ledger_account

    @property
    def service_sales_ledger_account(self):
        return self._service_sales_ledger_account

    @service_sales_ledger_account.setter
    def service_sales_ledger_account(self, service_sales_ledger_account):
        self._service_sales_ledger_account = service_sales_ledger_account

    @property
    def service_purchase_ledger_account(self):
        return self._service_purchase_ledger_account

    @service_purchase_ledger_account.setter
    def service_purchase_ledger_account(self, service_purchase_ledger_account):
        self._service_purchase_ledger_account = service_purchase_ledger_account

    @property
    def stock_purchase_ledger_account(self):
        return self._stock_purchase_ledger_account

    @stock_purchase_ledger_account.setter
    def stock_purchase_ledger_account(self, stock_purchase_ledger_account):
        self._stock_purchase_ledger_account = stock_purchase_ledger_account

    @property
    def other_receipt_ledger_account(self):
        return self._other_receipt_ledger_account

    @other_receipt_ledger_account.setter
    def other_receipt_ledger_account(self, other_receipt_ledger_account):
        self._other_receipt_ledger_account = other_receipt_ledger_account

    @property
    def other_payment_ledger_account(self):
        return self._other_payment_ledger_account

    @other_payment_ledger_account.setter
    def other_payment_ledger_account(self, other_payment_ledger_account):
        self._other_payment_ledger_account = other_payment_ledger_account

    @property
    def customer_receipt_discount_ledger_account(self):
        return self._customer_receipt_discount_ledger_account

    @customer_receipt_discount_ledger_account.setter
    def customer_receipt_discount_ledger_account(
        self, customer_receipt_discount_ledger_account
    ):
        self._customer_receipt_discount_ledger_account = (
            customer_receipt_discount_ledger_account
        )

    @property
    def vendor_payment_discount_ledger_account(self):
        return self._vendor_payment_discount_ledger_account

    @vendor_payment_discount_ledger_account.setter
    def vendor_payment_discount_ledger_account(
        self, vendor_payment_discount_ledger_account
    ):
        self._vendor_payment_discount_ledger_account = (
            vendor_payment_discount_ledger_account
        )

    @property
    def carriage_ledger_account(self):
        return self._carriage_ledger_account

    @carriage_ledger_account.setter
    def carriage_ledger_account(self, carriage_ledger_account):
        self._carriage_ledger_account = carriage_ledger_account

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
        if not isinstance(other, DefaultLedgerAccounts):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, DefaultLedgerAccounts):
            return True
        return self.to_dict() != other.to_dict()
