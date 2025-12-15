import pprint
import six
from sage.configuration import Configuration


class PostSalesCreditNotesSalesCreditNote(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        "contact_id": "str",
        "date": "date",
        "cis_applicable_amount": "float",
        "base_currency_cis_applicable_amount": "float",
        "total_after_cis_deduction": "float",
        "base_currency_total_after_cis_deduction": "float",
        "credit_note_number_prefix": "str",
        "credit_note_number": "str",
        "contact_name": "str",
        "contact_reference": "str",
        "original_invoice_date": "date",
        "reference": "str",
        "notes": "str",
        "terms_and_conditions": "str",
        "shipping_net_amount": "float",
        "shipping_tax_rate_id": "str",
        "shipping_tax_amount": "float",
        "total_quantity": "float",
        "shipping_total_amount": "float",
        "net_amount": "float",
        "tax_amount": "float",
        "total_amount": "float",
        "currency_id": "str",
        "exchange_rate": "float",
        "inverse_exchange_rate": "float",
        "base_currency_shipping_net_amount": "float",
        "base_currency_shipping_tax_amount": "float",
        "base_currency_shipping_total_amount": "float",
        "total_discount_amount": "float",
        "base_currency_total_discount_amount": "float",
        "base_currency_net_amount": "float",
        "base_currency_tax_amount": "float",
        "base_currency_total_amount": "float",
        "status_id": "str",
        "sent": "bool",
        "tax_address_region_id": "str",
        "withholding_tax_rate": "float",
        "withholding_tax_amount": "float",
        "base_currency_withholding_tax_amount": "float",
        "main_address": "PostSalesCorrectiveInvoicesSalesCorrectiveInvoiceMainAddress",
        "delivery_address": "PostSalesCorrectiveInvoicesSalesCorrectiveInvoiceMainAddress",
        "credit_note_lines": "list[PostSalesCreditNotesSalesCreditNoteCreditNoteLines]",
        "tax_analysis": "list[PostPurchaseCorrectiveInvoicesPurchaseCorrectiveInvoiceTaxAnalysis]",
    }
    attribute_map = {
        "contact_id": "contact_id",
        "date": "date",
        "cis_applicable_amount": "cis_applicable_amount",
        "base_currency_cis_applicable_amount": "base_currency_cis_applicable_amount",
        "total_after_cis_deduction": "total_after_cis_deduction",
        "base_currency_total_after_cis_deduction": "base_currency_total_after_cis_deduction",
        "credit_note_number_prefix": "credit_note_number_prefix",
        "credit_note_number": "credit_note_number",
        "contact_name": "contact_name",
        "contact_reference": "contact_reference",
        "original_invoice_date": "original_invoice_date",
        "reference": "reference",
        "notes": "notes",
        "terms_and_conditions": "terms_and_conditions",
        "shipping_net_amount": "shipping_net_amount",
        "shipping_tax_rate_id": "shipping_tax_rate_id",
        "shipping_tax_amount": "shipping_tax_amount",
        "total_quantity": "total_quantity",
        "shipping_total_amount": "shipping_total_amount",
        "net_amount": "net_amount",
        "tax_amount": "tax_amount",
        "total_amount": "total_amount",
        "currency_id": "currency_id",
        "exchange_rate": "exchange_rate",
        "inverse_exchange_rate": "inverse_exchange_rate",
        "base_currency_shipping_net_amount": "base_currency_shipping_net_amount",
        "base_currency_shipping_tax_amount": "base_currency_shipping_tax_amount",
        "base_currency_shipping_total_amount": "base_currency_shipping_total_amount",
        "total_discount_amount": "total_discount_amount",
        "base_currency_total_discount_amount": "base_currency_total_discount_amount",
        "base_currency_net_amount": "base_currency_net_amount",
        "base_currency_tax_amount": "base_currency_tax_amount",
        "base_currency_total_amount": "base_currency_total_amount",
        "status_id": "status_id",
        "sent": "sent",
        "tax_address_region_id": "tax_address_region_id",
        "withholding_tax_rate": "withholding_tax_rate",
        "withholding_tax_amount": "withholding_tax_amount",
        "base_currency_withholding_tax_amount": "base_currency_withholding_tax_amount",
        "main_address": "main_address",
        "delivery_address": "delivery_address",
        "credit_note_lines": "credit_note_lines",
        "tax_analysis": "tax_analysis",
    }

    def __init__(
        self,
        contact_id=None,
        date=None,
        cis_applicable_amount=None,
        base_currency_cis_applicable_amount=None,
        total_after_cis_deduction=None,
        base_currency_total_after_cis_deduction=None,
        credit_note_number_prefix=None,
        credit_note_number=None,
        contact_name=None,
        contact_reference=None,
        original_invoice_date=None,
        reference=None,
        notes=None,
        terms_and_conditions=None,
        shipping_net_amount=None,
        shipping_tax_rate_id=None,
        shipping_tax_amount=None,
        total_quantity=None,
        shipping_total_amount=None,
        net_amount=None,
        tax_amount=None,
        total_amount=None,
        currency_id=None,
        exchange_rate=None,
        inverse_exchange_rate=None,
        base_currency_shipping_net_amount=None,
        base_currency_shipping_tax_amount=None,
        base_currency_shipping_total_amount=None,
        total_discount_amount=None,
        base_currency_total_discount_amount=None,
        base_currency_net_amount=None,
        base_currency_tax_amount=None,
        base_currency_total_amount=None,
        status_id=None,
        sent=None,
        tax_address_region_id=None,
        withholding_tax_rate=None,
        withholding_tax_amount=None,
        base_currency_withholding_tax_amount=None,
        main_address=None,
        delivery_address=None,
        credit_note_lines=None,
        tax_analysis=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._contact_id = None
        self._date = None
        self._cis_applicable_amount = None
        self._base_currency_cis_applicable_amount = None
        self._total_after_cis_deduction = None
        self._base_currency_total_after_cis_deduction = None
        self._credit_note_number_prefix = None
        self._credit_note_number = None
        self._contact_name = None
        self._contact_reference = None
        self._original_invoice_date = None
        self._reference = None
        self._notes = None
        self._terms_and_conditions = None
        self._shipping_net_amount = None
        self._shipping_tax_rate_id = None
        self._shipping_tax_amount = None
        self._total_quantity = None
        self._shipping_total_amount = None
        self._net_amount = None
        self._tax_amount = None
        self._total_amount = None
        self._currency_id = None
        self._exchange_rate = None
        self._inverse_exchange_rate = None
        self._base_currency_shipping_net_amount = None
        self._base_currency_shipping_tax_amount = None
        self._base_currency_shipping_total_amount = None
        self._total_discount_amount = None
        self._base_currency_total_discount_amount = None
        self._base_currency_net_amount = None
        self._base_currency_tax_amount = None
        self._base_currency_total_amount = None
        self._status_id = None
        self._sent = None
        self._tax_address_region_id = None
        self._withholding_tax_rate = None
        self._withholding_tax_amount = None
        self._base_currency_withholding_tax_amount = None
        self._main_address = None
        self._delivery_address = None
        self._credit_note_lines = None
        self._tax_analysis = None
        self.discriminator = None
        self.contact_id = contact_id
        self.date = date
        if cis_applicable_amount is not None:
            self.cis_applicable_amount = cis_applicable_amount
        if base_currency_cis_applicable_amount is not None:
            self.base_currency_cis_applicable_amount = (
                base_currency_cis_applicable_amount
            )
        if total_after_cis_deduction is not None:
            self.total_after_cis_deduction = total_after_cis_deduction
        if base_currency_total_after_cis_deduction is not None:
            self.base_currency_total_after_cis_deduction = (
                base_currency_total_after_cis_deduction
            )
        if credit_note_number_prefix is not None:
            self.credit_note_number_prefix = credit_note_number_prefix
        if credit_note_number is not None:
            self.credit_note_number = credit_note_number
        if contact_name is not None:
            self.contact_name = contact_name
        if contact_reference is not None:
            self.contact_reference = contact_reference
        if original_invoice_date is not None:
            self.original_invoice_date = original_invoice_date
        if reference is not None:
            self.reference = reference
        if notes is not None:
            self.notes = notes
        if terms_and_conditions is not None:
            self.terms_and_conditions = terms_and_conditions
        if shipping_net_amount is not None:
            self.shipping_net_amount = shipping_net_amount
        if shipping_tax_rate_id is not None:
            self.shipping_tax_rate_id = shipping_tax_rate_id
        if shipping_tax_amount is not None:
            self.shipping_tax_amount = shipping_tax_amount
        if total_quantity is not None:
            self.total_quantity = total_quantity
        if shipping_total_amount is not None:
            self.shipping_total_amount = shipping_total_amount
        if net_amount is not None:
            self.net_amount = net_amount
        if tax_amount is not None:
            self.tax_amount = tax_amount
        if total_amount is not None:
            self.total_amount = total_amount
        if currency_id is not None:
            self.currency_id = currency_id
        if exchange_rate is not None:
            self.exchange_rate = exchange_rate
        if inverse_exchange_rate is not None:
            self.inverse_exchange_rate = inverse_exchange_rate
        if base_currency_shipping_net_amount is not None:
            self.base_currency_shipping_net_amount = base_currency_shipping_net_amount
        if base_currency_shipping_tax_amount is not None:
            self.base_currency_shipping_tax_amount = base_currency_shipping_tax_amount
        if base_currency_shipping_total_amount is not None:
            self.base_currency_shipping_total_amount = (
                base_currency_shipping_total_amount
            )
        if total_discount_amount is not None:
            self.total_discount_amount = total_discount_amount
        if base_currency_total_discount_amount is not None:
            self.base_currency_total_discount_amount = (
                base_currency_total_discount_amount
            )
        if base_currency_net_amount is not None:
            self.base_currency_net_amount = base_currency_net_amount
        if base_currency_tax_amount is not None:
            self.base_currency_tax_amount = base_currency_tax_amount
        if base_currency_total_amount is not None:
            self.base_currency_total_amount = base_currency_total_amount
        if status_id is not None:
            self.status_id = status_id
        if sent is not None:
            self.sent = sent
        if tax_address_region_id is not None:
            self.tax_address_region_id = tax_address_region_id
        if withholding_tax_rate is not None:
            self.withholding_tax_rate = withholding_tax_rate
        if withholding_tax_amount is not None:
            self.withholding_tax_amount = withholding_tax_amount
        if base_currency_withholding_tax_amount is not None:
            self.base_currency_withholding_tax_amount = (
                base_currency_withholding_tax_amount
            )
        if main_address is not None:
            self.main_address = main_address
        if delivery_address is not None:
            self.delivery_address = delivery_address
        self.credit_note_lines = credit_note_lines
        if tax_analysis is not None:
            self.tax_analysis = tax_analysis

    @property
    def contact_id(self):
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        if self.local_vars_configuration.client_side_validation and contact_id is None:
            raise ValueError("Invalid value for `contact_id`, must not be `None`")
        self._contact_id = contact_id

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if self.local_vars_configuration.client_side_validation and date is None:
            raise ValueError("Invalid value for `date`, must not be `None`")
        self._date = date

    @property
    def cis_applicable_amount(self):
        return self._cis_applicable_amount

    @cis_applicable_amount.setter
    def cis_applicable_amount(self, cis_applicable_amount):
        self._cis_applicable_amount = cis_applicable_amount

    @property
    def base_currency_cis_applicable_amount(self):
        return self._base_currency_cis_applicable_amount

    @base_currency_cis_applicable_amount.setter
    def base_currency_cis_applicable_amount(self, base_currency_cis_applicable_amount):
        self._base_currency_cis_applicable_amount = base_currency_cis_applicable_amount

    @property
    def total_after_cis_deduction(self):
        return self._total_after_cis_deduction

    @total_after_cis_deduction.setter
    def total_after_cis_deduction(self, total_after_cis_deduction):
        self._total_after_cis_deduction = total_after_cis_deduction

    @property
    def base_currency_total_after_cis_deduction(self):
        return self._base_currency_total_after_cis_deduction

    @base_currency_total_after_cis_deduction.setter
    def base_currency_total_after_cis_deduction(
        self, base_currency_total_after_cis_deduction
    ):
        self._base_currency_total_after_cis_deduction = (
            base_currency_total_after_cis_deduction
        )

    @property
    def credit_note_number_prefix(self):
        return self._credit_note_number_prefix

    @credit_note_number_prefix.setter
    def credit_note_number_prefix(self, credit_note_number_prefix):
        self._credit_note_number_prefix = credit_note_number_prefix

    @property
    def credit_note_number(self):
        return self._credit_note_number

    @credit_note_number.setter
    def credit_note_number(self, credit_note_number):
        self._credit_note_number = credit_note_number

    @property
    def contact_name(self):
        return self._contact_name

    @contact_name.setter
    def contact_name(self, contact_name):
        self._contact_name = contact_name

    @property
    def contact_reference(self):
        return self._contact_reference

    @contact_reference.setter
    def contact_reference(self, contact_reference):
        self._contact_reference = contact_reference

    @property
    def original_invoice_date(self):
        return self._original_invoice_date

    @original_invoice_date.setter
    def original_invoice_date(self, original_invoice_date):
        self._original_invoice_date = original_invoice_date

    @property
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, reference):
        self._reference = reference

    @property
    def notes(self):
        return self._notes

    @notes.setter
    def notes(self, notes):
        self._notes = notes

    @property
    def terms_and_conditions(self):
        return self._terms_and_conditions

    @terms_and_conditions.setter
    def terms_and_conditions(self, terms_and_conditions):
        self._terms_and_conditions = terms_and_conditions

    @property
    def shipping_net_amount(self):
        return self._shipping_net_amount

    @shipping_net_amount.setter
    def shipping_net_amount(self, shipping_net_amount):
        self._shipping_net_amount = shipping_net_amount

    @property
    def shipping_tax_rate_id(self):
        return self._shipping_tax_rate_id

    @shipping_tax_rate_id.setter
    def shipping_tax_rate_id(self, shipping_tax_rate_id):
        self._shipping_tax_rate_id = shipping_tax_rate_id

    @property
    def shipping_tax_amount(self):
        return self._shipping_tax_amount

    @shipping_tax_amount.setter
    def shipping_tax_amount(self, shipping_tax_amount):
        self._shipping_tax_amount = shipping_tax_amount

    @property
    def total_quantity(self):
        return self._total_quantity

    @total_quantity.setter
    def total_quantity(self, total_quantity):
        self._total_quantity = total_quantity

    @property
    def shipping_total_amount(self):
        return self._shipping_total_amount

    @shipping_total_amount.setter
    def shipping_total_amount(self, shipping_total_amount):
        self._shipping_total_amount = shipping_total_amount

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
    def currency_id(self):
        return self._currency_id

    @currency_id.setter
    def currency_id(self, currency_id):
        self._currency_id = currency_id

    @property
    def exchange_rate(self):
        return self._exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, exchange_rate):
        self._exchange_rate = exchange_rate

    @property
    def inverse_exchange_rate(self):
        return self._inverse_exchange_rate

    @inverse_exchange_rate.setter
    def inverse_exchange_rate(self, inverse_exchange_rate):
        self._inverse_exchange_rate = inverse_exchange_rate

    @property
    def base_currency_shipping_net_amount(self):
        return self._base_currency_shipping_net_amount

    @base_currency_shipping_net_amount.setter
    def base_currency_shipping_net_amount(self, base_currency_shipping_net_amount):
        self._base_currency_shipping_net_amount = base_currency_shipping_net_amount

    @property
    def base_currency_shipping_tax_amount(self):
        return self._base_currency_shipping_tax_amount

    @base_currency_shipping_tax_amount.setter
    def base_currency_shipping_tax_amount(self, base_currency_shipping_tax_amount):
        self._base_currency_shipping_tax_amount = base_currency_shipping_tax_amount

    @property
    def base_currency_shipping_total_amount(self):
        return self._base_currency_shipping_total_amount

    @base_currency_shipping_total_amount.setter
    def base_currency_shipping_total_amount(self, base_currency_shipping_total_amount):
        self._base_currency_shipping_total_amount = base_currency_shipping_total_amount

    @property
    def total_discount_amount(self):
        return self._total_discount_amount

    @total_discount_amount.setter
    def total_discount_amount(self, total_discount_amount):
        self._total_discount_amount = total_discount_amount

    @property
    def base_currency_total_discount_amount(self):
        return self._base_currency_total_discount_amount

    @base_currency_total_discount_amount.setter
    def base_currency_total_discount_amount(self, base_currency_total_discount_amount):
        self._base_currency_total_discount_amount = base_currency_total_discount_amount

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
    def status_id(self):
        return self._status_id

    @status_id.setter
    def status_id(self, status_id):
        self._status_id = status_id

    @property
    def sent(self):
        return self._sent

    @sent.setter
    def sent(self, sent):
        self._sent = sent

    @property
    def tax_address_region_id(self):
        return self._tax_address_region_id

    @tax_address_region_id.setter
    def tax_address_region_id(self, tax_address_region_id):
        self._tax_address_region_id = tax_address_region_id

    @property
    def withholding_tax_rate(self):
        return self._withholding_tax_rate

    @withholding_tax_rate.setter
    def withholding_tax_rate(self, withholding_tax_rate):
        self._withholding_tax_rate = withholding_tax_rate

    @property
    def withholding_tax_amount(self):
        return self._withholding_tax_amount

    @withholding_tax_amount.setter
    def withholding_tax_amount(self, withholding_tax_amount):
        self._withholding_tax_amount = withholding_tax_amount

    @property
    def base_currency_withholding_tax_amount(self):
        return self._base_currency_withholding_tax_amount

    @base_currency_withholding_tax_amount.setter
    def base_currency_withholding_tax_amount(
        self, base_currency_withholding_tax_amount
    ):
        self._base_currency_withholding_tax_amount = (
            base_currency_withholding_tax_amount
        )

    @property
    def main_address(self):
        return self._main_address

    @main_address.setter
    def main_address(self, main_address):
        self._main_address = main_address

    @property
    def delivery_address(self):
        return self._delivery_address

    @delivery_address.setter
    def delivery_address(self, delivery_address):
        self._delivery_address = delivery_address

    @property
    def credit_note_lines(self):
        return self._credit_note_lines

    @credit_note_lines.setter
    def credit_note_lines(self, credit_note_lines):
        if (
            self.local_vars_configuration.client_side_validation
            and credit_note_lines is None
        ):
            raise ValueError(
                "Invalid value for `credit_note_lines`, must not be `None`"
            )
        self._credit_note_lines = credit_note_lines

    @property
    def tax_analysis(self):
        return self._tax_analysis

    @tax_analysis.setter
    def tax_analysis(self, tax_analysis):
        self._tax_analysis = tax_analysis

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
        if not isinstance(other, PostSalesCreditNotesSalesCreditNote):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PostSalesCreditNotesSalesCreditNote):
            return True
        return self.to_dict() != other.to_dict()
