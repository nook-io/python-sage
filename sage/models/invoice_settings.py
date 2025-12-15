import pprint
import six
from sage.configuration import Configuration


class InvoiceSettings(object):
    openapi_types = {
        "path": "str",
        "next_invoice_number": "int",
        "next_credit_note_number": "int",
        "separate_invoice_credit_note_numbering": "bool",
        "sales_invoice_number_prefix": "str",
        "sales_credit_note_number_prefix": "str",
        "invoice_terms_and_conditions": "str",
        "default_note_on_invoice": "str",
        "default_note_on_credit_note": "str",
        "next_quote_number": "int",
        "quote_number_prefix": "str",
        "estimate_number_prefix": "str",
        "quote_default_days_to_expiry": "int",
        "estimate_default_days_to_expiry": "int",
        "quote_terms_and_conditions": "str",
        "estimate_terms_and_conditions": "str",
        "delivery_note_terms_and_conditions": "str",
        "delivery_note_show_signature": "bool",
        "delivery_note_show_picked": "bool",
        "delivery_note_show_notes": "bool",
        "delivery_note_show_contact_details": "bool",
        "quick_entry_prefix": "str",
        "late_payment_percentage": "float",
        "prompt_payment_percentage": "float",
        "show_auto_entrepreneur": "bool",
        "show_insurance": "bool",
        "insurer": "Contact",
        "insurance_area": "str",
        "insurance_type": "str",
        "insurance_text": "str",
        "payment_bank_account": "Base",
        "sales_corrective_invoice_number_prefix": "str",
        "next_sales_corrective_invoice_number": "int",
        "document_headings": "InvoiceSettingsDocumentHeadings",
        "line_item_titles": "InvoiceSettingsLineItemTitles",
        "footer_details": "FooterDetails",
        "print_contact_details": "PrintContactDetails",
        "print_statements": "PrintStatements",
        "customer_credit_days": "int",
        "vendor_credit_days": "int",
        "updated_at": "datetime",
    }
    attribute_map = {
        "path": "$path",
        "next_invoice_number": "next_invoice_number",
        "next_credit_note_number": "next_credit_note_number",
        "separate_invoice_credit_note_numbering": "separate_invoice_credit_note_numbering",
        "sales_invoice_number_prefix": "sales_invoice_number_prefix",
        "sales_credit_note_number_prefix": "sales_credit_note_number_prefix",
        "invoice_terms_and_conditions": "invoice_terms_and_conditions",
        "default_note_on_invoice": "default_note_on_invoice",
        "default_note_on_credit_note": "default_note_on_credit_note",
        "next_quote_number": "next_quote_number",
        "quote_number_prefix": "quote_number_prefix",
        "estimate_number_prefix": "estimate_number_prefix",
        "quote_default_days_to_expiry": "quote_default_days_to_expiry",
        "estimate_default_days_to_expiry": "estimate_default_days_to_expiry",
        "quote_terms_and_conditions": "quote_terms_and_conditions",
        "estimate_terms_and_conditions": "estimate_terms_and_conditions",
        "delivery_note_terms_and_conditions": "delivery_note_terms_and_conditions",
        "delivery_note_show_signature": "delivery_note_show_signature",
        "delivery_note_show_picked": "delivery_note_show_picked",
        "delivery_note_show_notes": "delivery_note_show_notes",
        "delivery_note_show_contact_details": "delivery_note_show_contact_details",
        "quick_entry_prefix": "quick_entry_prefix",
        "late_payment_percentage": "late_payment_percentage",
        "prompt_payment_percentage": "prompt_payment_percentage",
        "show_auto_entrepreneur": "show_auto_entrepreneur",
        "show_insurance": "show_insurance",
        "insurer": "insurer",
        "insurance_area": "insurance_area",
        "insurance_type": "insurance_type",
        "insurance_text": "insurance_text",
        "payment_bank_account": "payment_bank_account",
        "sales_corrective_invoice_number_prefix": "sales_corrective_invoice_number_prefix",
        "next_sales_corrective_invoice_number": "next_sales_corrective_invoice_number",
        "document_headings": "document_headings",
        "line_item_titles": "line_item_titles",
        "footer_details": "footer_details",
        "print_contact_details": "print_contact_details",
        "print_statements": "print_statements",
        "customer_credit_days": "customer_credit_days",
        "vendor_credit_days": "vendor_credit_days",
        "updated_at": "updated_at",
    }

    def __init__(
        self,
        path=None,
        next_invoice_number=None,
        next_credit_note_number=None,
        separate_invoice_credit_note_numbering=None,
        sales_invoice_number_prefix=None,
        sales_credit_note_number_prefix=None,
        invoice_terms_and_conditions=None,
        default_note_on_invoice=None,
        default_note_on_credit_note=None,
        next_quote_number=None,
        quote_number_prefix=None,
        estimate_number_prefix=None,
        quote_default_days_to_expiry=None,
        estimate_default_days_to_expiry=None,
        quote_terms_and_conditions=None,
        estimate_terms_and_conditions=None,
        delivery_note_terms_and_conditions=None,
        delivery_note_show_signature=None,
        delivery_note_show_picked=None,
        delivery_note_show_notes=None,
        delivery_note_show_contact_details=None,
        quick_entry_prefix=None,
        late_payment_percentage=None,
        prompt_payment_percentage=None,
        show_auto_entrepreneur=None,
        show_insurance=None,
        insurer=None,
        insurance_area=None,
        insurance_type=None,
        insurance_text=None,
        payment_bank_account=None,
        sales_corrective_invoice_number_prefix=None,
        next_sales_corrective_invoice_number=None,
        document_headings=None,
        line_item_titles=None,
        footer_details=None,
        print_contact_details=None,
        print_statements=None,
        customer_credit_days=None,
        vendor_credit_days=None,
        updated_at=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._path = None
        self._next_invoice_number = None
        self._next_credit_note_number = None
        self._separate_invoice_credit_note_numbering = None
        self._sales_invoice_number_prefix = None
        self._sales_credit_note_number_prefix = None
        self._invoice_terms_and_conditions = None
        self._default_note_on_invoice = None
        self._default_note_on_credit_note = None
        self._next_quote_number = None
        self._quote_number_prefix = None
        self._estimate_number_prefix = None
        self._quote_default_days_to_expiry = None
        self._estimate_default_days_to_expiry = None
        self._quote_terms_and_conditions = None
        self._estimate_terms_and_conditions = None
        self._delivery_note_terms_and_conditions = None
        self._delivery_note_show_signature = None
        self._delivery_note_show_picked = None
        self._delivery_note_show_notes = None
        self._delivery_note_show_contact_details = None
        self._quick_entry_prefix = None
        self._late_payment_percentage = None
        self._prompt_payment_percentage = None
        self._show_auto_entrepreneur = None
        self._show_insurance = None
        self._insurer = None
        self._insurance_area = None
        self._insurance_type = None
        self._insurance_text = None
        self._payment_bank_account = None
        self._sales_corrective_invoice_number_prefix = None
        self._next_sales_corrective_invoice_number = None
        self._document_headings = None
        self._line_item_titles = None
        self._footer_details = None
        self._print_contact_details = None
        self._print_statements = None
        self._customer_credit_days = None
        self._vendor_credit_days = None
        self._updated_at = None
        self.discriminator = None
        if path is not None:
            self.path = path
        if next_invoice_number is not None:
            self.next_invoice_number = next_invoice_number
        if next_credit_note_number is not None:
            self.next_credit_note_number = next_credit_note_number
        if separate_invoice_credit_note_numbering is not None:
            self.separate_invoice_credit_note_numbering = (
                separate_invoice_credit_note_numbering
            )
        if sales_invoice_number_prefix is not None:
            self.sales_invoice_number_prefix = sales_invoice_number_prefix
        if sales_credit_note_number_prefix is not None:
            self.sales_credit_note_number_prefix = sales_credit_note_number_prefix
        if invoice_terms_and_conditions is not None:
            self.invoice_terms_and_conditions = invoice_terms_and_conditions
        if default_note_on_invoice is not None:
            self.default_note_on_invoice = default_note_on_invoice
        if default_note_on_credit_note is not None:
            self.default_note_on_credit_note = default_note_on_credit_note
        if next_quote_number is not None:
            self.next_quote_number = next_quote_number
        if quote_number_prefix is not None:
            self.quote_number_prefix = quote_number_prefix
        if estimate_number_prefix is not None:
            self.estimate_number_prefix = estimate_number_prefix
        if quote_default_days_to_expiry is not None:
            self.quote_default_days_to_expiry = quote_default_days_to_expiry
        if estimate_default_days_to_expiry is not None:
            self.estimate_default_days_to_expiry = estimate_default_days_to_expiry
        if quote_terms_and_conditions is not None:
            self.quote_terms_and_conditions = quote_terms_and_conditions
        if estimate_terms_and_conditions is not None:
            self.estimate_terms_and_conditions = estimate_terms_and_conditions
        if delivery_note_terms_and_conditions is not None:
            self.delivery_note_terms_and_conditions = delivery_note_terms_and_conditions
        if delivery_note_show_signature is not None:
            self.delivery_note_show_signature = delivery_note_show_signature
        if delivery_note_show_picked is not None:
            self.delivery_note_show_picked = delivery_note_show_picked
        if delivery_note_show_notes is not None:
            self.delivery_note_show_notes = delivery_note_show_notes
        if delivery_note_show_contact_details is not None:
            self.delivery_note_show_contact_details = delivery_note_show_contact_details
        if quick_entry_prefix is not None:
            self.quick_entry_prefix = quick_entry_prefix
        if late_payment_percentage is not None:
            self.late_payment_percentage = late_payment_percentage
        if prompt_payment_percentage is not None:
            self.prompt_payment_percentage = prompt_payment_percentage
        if show_auto_entrepreneur is not None:
            self.show_auto_entrepreneur = show_auto_entrepreneur
        if show_insurance is not None:
            self.show_insurance = show_insurance
        if insurer is not None:
            self.insurer = insurer
        if insurance_area is not None:
            self.insurance_area = insurance_area
        if insurance_type is not None:
            self.insurance_type = insurance_type
        if insurance_text is not None:
            self.insurance_text = insurance_text
        if payment_bank_account is not None:
            self.payment_bank_account = payment_bank_account
        if sales_corrective_invoice_number_prefix is not None:
            self.sales_corrective_invoice_number_prefix = (
                sales_corrective_invoice_number_prefix
            )
        if next_sales_corrective_invoice_number is not None:
            self.next_sales_corrective_invoice_number = (
                next_sales_corrective_invoice_number
            )
        if document_headings is not None:
            self.document_headings = document_headings
        if line_item_titles is not None:
            self.line_item_titles = line_item_titles
        if footer_details is not None:
            self.footer_details = footer_details
        if print_contact_details is not None:
            self.print_contact_details = print_contact_details
        if print_statements is not None:
            self.print_statements = print_statements
        if customer_credit_days is not None:
            self.customer_credit_days = customer_credit_days
        if vendor_credit_days is not None:
            self.vendor_credit_days = vendor_credit_days
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path):
        self._path = path

    @property
    def next_invoice_number(self):
        return self._next_invoice_number

    @next_invoice_number.setter
    def next_invoice_number(self, next_invoice_number):
        self._next_invoice_number = next_invoice_number

    @property
    def next_credit_note_number(self):
        return self._next_credit_note_number

    @next_credit_note_number.setter
    def next_credit_note_number(self, next_credit_note_number):
        self._next_credit_note_number = next_credit_note_number

    @property
    def separate_invoice_credit_note_numbering(self):
        return self._separate_invoice_credit_note_numbering

    @separate_invoice_credit_note_numbering.setter
    def separate_invoice_credit_note_numbering(
        self, separate_invoice_credit_note_numbering
    ):
        self._separate_invoice_credit_note_numbering = (
            separate_invoice_credit_note_numbering
        )

    @property
    def sales_invoice_number_prefix(self):
        return self._sales_invoice_number_prefix

    @sales_invoice_number_prefix.setter
    def sales_invoice_number_prefix(self, sales_invoice_number_prefix):
        if (
            self.local_vars_configuration.client_side_validation
            and sales_invoice_number_prefix is not None
            and len(sales_invoice_number_prefix) > 6
        ):
            raise ValueError(
                "Invalid value for `sales_invoice_number_prefix`, length must be less than or equal to `6`"
            )
        self._sales_invoice_number_prefix = sales_invoice_number_prefix

    @property
    def sales_credit_note_number_prefix(self):
        return self._sales_credit_note_number_prefix

    @sales_credit_note_number_prefix.setter
    def sales_credit_note_number_prefix(self, sales_credit_note_number_prefix):
        if (
            self.local_vars_configuration.client_side_validation
            and sales_credit_note_number_prefix is not None
            and len(sales_credit_note_number_prefix) > 6
        ):
            raise ValueError(
                "Invalid value for `sales_credit_note_number_prefix`, length must be less than or equal to `6`"
            )
        self._sales_credit_note_number_prefix = sales_credit_note_number_prefix

    @property
    def invoice_terms_and_conditions(self):
        return self._invoice_terms_and_conditions

    @invoice_terms_and_conditions.setter
    def invoice_terms_and_conditions(self, invoice_terms_and_conditions):
        if (
            self.local_vars_configuration.client_side_validation
            and invoice_terms_and_conditions is not None
            and len(invoice_terms_and_conditions) > 2000
        ):
            raise ValueError(
                "Invalid value for `invoice_terms_and_conditions`, length must be less than or equal to `2000`"
            )
        self._invoice_terms_and_conditions = invoice_terms_and_conditions

    @property
    def default_note_on_invoice(self):
        return self._default_note_on_invoice

    @default_note_on_invoice.setter
    def default_note_on_invoice(self, default_note_on_invoice):
        if (
            self.local_vars_configuration.client_side_validation
            and default_note_on_invoice is not None
            and len(default_note_on_invoice) > 2000
        ):
            raise ValueError(
                "Invalid value for `default_note_on_invoice`, length must be less than or equal to `2000`"
            )
        self._default_note_on_invoice = default_note_on_invoice

    @property
    def default_note_on_credit_note(self):
        return self._default_note_on_credit_note

    @default_note_on_credit_note.setter
    def default_note_on_credit_note(self, default_note_on_credit_note):
        if (
            self.local_vars_configuration.client_side_validation
            and default_note_on_credit_note is not None
            and len(default_note_on_credit_note) > 2000
        ):
            raise ValueError(
                "Invalid value for `default_note_on_credit_note`, length must be less than or equal to `2000`"
            )
        self._default_note_on_credit_note = default_note_on_credit_note

    @property
    def next_quote_number(self):
        return self._next_quote_number

    @next_quote_number.setter
    def next_quote_number(self, next_quote_number):
        self._next_quote_number = next_quote_number

    @property
    def quote_number_prefix(self):
        return self._quote_number_prefix

    @quote_number_prefix.setter
    def quote_number_prefix(self, quote_number_prefix):
        if (
            self.local_vars_configuration.client_side_validation
            and quote_number_prefix is not None
            and len(quote_number_prefix) > 6
        ):
            raise ValueError(
                "Invalid value for `quote_number_prefix`, length must be less than or equal to `6`"
            )
        self._quote_number_prefix = quote_number_prefix

    @property
    def estimate_number_prefix(self):
        return self._estimate_number_prefix

    @estimate_number_prefix.setter
    def estimate_number_prefix(self, estimate_number_prefix):
        if (
            self.local_vars_configuration.client_side_validation
            and estimate_number_prefix is not None
            and len(estimate_number_prefix) > 6
        ):
            raise ValueError(
                "Invalid value for `estimate_number_prefix`, length must be less than or equal to `6`"
            )
        self._estimate_number_prefix = estimate_number_prefix

    @property
    def quote_default_days_to_expiry(self):
        return self._quote_default_days_to_expiry

    @quote_default_days_to_expiry.setter
    def quote_default_days_to_expiry(self, quote_default_days_to_expiry):
        self._quote_default_days_to_expiry = quote_default_days_to_expiry

    @property
    def estimate_default_days_to_expiry(self):
        return self._estimate_default_days_to_expiry

    @estimate_default_days_to_expiry.setter
    def estimate_default_days_to_expiry(self, estimate_default_days_to_expiry):
        self._estimate_default_days_to_expiry = estimate_default_days_to_expiry

    @property
    def quote_terms_and_conditions(self):
        return self._quote_terms_and_conditions

    @quote_terms_and_conditions.setter
    def quote_terms_and_conditions(self, quote_terms_and_conditions):
        if (
            self.local_vars_configuration.client_side_validation
            and quote_terms_and_conditions is not None
            and len(quote_terms_and_conditions) > 2000
        ):
            raise ValueError(
                "Invalid value for `quote_terms_and_conditions`, length must be less than or equal to `2000`"
            )
        self._quote_terms_and_conditions = quote_terms_and_conditions

    @property
    def estimate_terms_and_conditions(self):
        return self._estimate_terms_and_conditions

    @estimate_terms_and_conditions.setter
    def estimate_terms_and_conditions(self, estimate_terms_and_conditions):
        if (
            self.local_vars_configuration.client_side_validation
            and estimate_terms_and_conditions is not None
            and len(estimate_terms_and_conditions) > 2000
        ):
            raise ValueError(
                "Invalid value for `estimate_terms_and_conditions`, length must be less than or equal to `2000`"
            )
        self._estimate_terms_and_conditions = estimate_terms_and_conditions

    @property
    def delivery_note_terms_and_conditions(self):
        return self._delivery_note_terms_and_conditions

    @delivery_note_terms_and_conditions.setter
    def delivery_note_terms_and_conditions(self, delivery_note_terms_and_conditions):
        if (
            self.local_vars_configuration.client_side_validation
            and delivery_note_terms_and_conditions is not None
            and len(delivery_note_terms_and_conditions) > 2000
        ):
            raise ValueError(
                "Invalid value for `delivery_note_terms_and_conditions`, length must be less than or equal to `2000`"
            )
        self._delivery_note_terms_and_conditions = delivery_note_terms_and_conditions

    @property
    def delivery_note_show_signature(self):
        return self._delivery_note_show_signature

    @delivery_note_show_signature.setter
    def delivery_note_show_signature(self, delivery_note_show_signature):
        self._delivery_note_show_signature = delivery_note_show_signature

    @property
    def delivery_note_show_picked(self):
        return self._delivery_note_show_picked

    @delivery_note_show_picked.setter
    def delivery_note_show_picked(self, delivery_note_show_picked):
        self._delivery_note_show_picked = delivery_note_show_picked

    @property
    def delivery_note_show_notes(self):
        return self._delivery_note_show_notes

    @delivery_note_show_notes.setter
    def delivery_note_show_notes(self, delivery_note_show_notes):
        self._delivery_note_show_notes = delivery_note_show_notes

    @property
    def delivery_note_show_contact_details(self):
        return self._delivery_note_show_contact_details

    @delivery_note_show_contact_details.setter
    def delivery_note_show_contact_details(self, delivery_note_show_contact_details):
        self._delivery_note_show_contact_details = delivery_note_show_contact_details

    @property
    def quick_entry_prefix(self):
        return self._quick_entry_prefix

    @quick_entry_prefix.setter
    def quick_entry_prefix(self, quick_entry_prefix):
        if (
            self.local_vars_configuration.client_side_validation
            and quick_entry_prefix is not None
            and len(quick_entry_prefix) > 6
        ):
            raise ValueError(
                "Invalid value for `quick_entry_prefix`, length must be less than or equal to `6`"
            )
        self._quick_entry_prefix = quick_entry_prefix

    @property
    def late_payment_percentage(self):
        return self._late_payment_percentage

    @late_payment_percentage.setter
    def late_payment_percentage(self, late_payment_percentage):
        self._late_payment_percentage = late_payment_percentage

    @property
    def prompt_payment_percentage(self):
        return self._prompt_payment_percentage

    @prompt_payment_percentage.setter
    def prompt_payment_percentage(self, prompt_payment_percentage):
        self._prompt_payment_percentage = prompt_payment_percentage

    @property
    def show_auto_entrepreneur(self):
        return self._show_auto_entrepreneur

    @show_auto_entrepreneur.setter
    def show_auto_entrepreneur(self, show_auto_entrepreneur):
        self._show_auto_entrepreneur = show_auto_entrepreneur

    @property
    def show_insurance(self):
        return self._show_insurance

    @show_insurance.setter
    def show_insurance(self, show_insurance):
        self._show_insurance = show_insurance

    @property
    def insurer(self):
        return self._insurer

    @insurer.setter
    def insurer(self, insurer):
        self._insurer = insurer

    @property
    def insurance_area(self):
        return self._insurance_area

    @insurance_area.setter
    def insurance_area(self, insurance_area):
        self._insurance_area = insurance_area

    @property
    def insurance_type(self):
        return self._insurance_type

    @insurance_type.setter
    def insurance_type(self, insurance_type):
        self._insurance_type = insurance_type

    @property
    def insurance_text(self):
        return self._insurance_text

    @insurance_text.setter
    def insurance_text(self, insurance_text):
        self._insurance_text = insurance_text

    @property
    def payment_bank_account(self):
        return self._payment_bank_account

    @payment_bank_account.setter
    def payment_bank_account(self, payment_bank_account):
        self._payment_bank_account = payment_bank_account

    @property
    def sales_corrective_invoice_number_prefix(self):
        return self._sales_corrective_invoice_number_prefix

    @sales_corrective_invoice_number_prefix.setter
    def sales_corrective_invoice_number_prefix(
        self, sales_corrective_invoice_number_prefix
    ):
        if (
            self.local_vars_configuration.client_side_validation
            and sales_corrective_invoice_number_prefix is not None
            and len(sales_corrective_invoice_number_prefix) > 255
        ):
            raise ValueError(
                "Invalid value for `sales_corrective_invoice_number_prefix`, length must be less than or equal to `255`"
            )
        self._sales_corrective_invoice_number_prefix = (
            sales_corrective_invoice_number_prefix
        )

    @property
    def next_sales_corrective_invoice_number(self):
        return self._next_sales_corrective_invoice_number

    @next_sales_corrective_invoice_number.setter
    def next_sales_corrective_invoice_number(
        self, next_sales_corrective_invoice_number
    ):
        self._next_sales_corrective_invoice_number = (
            next_sales_corrective_invoice_number
        )

    @property
    def document_headings(self):
        return self._document_headings

    @document_headings.setter
    def document_headings(self, document_headings):
        self._document_headings = document_headings

    @property
    def line_item_titles(self):
        return self._line_item_titles

    @line_item_titles.setter
    def line_item_titles(self, line_item_titles):
        self._line_item_titles = line_item_titles

    @property
    def footer_details(self):
        return self._footer_details

    @footer_details.setter
    def footer_details(self, footer_details):
        self._footer_details = footer_details

    @property
    def print_contact_details(self):
        return self._print_contact_details

    @print_contact_details.setter
    def print_contact_details(self, print_contact_details):
        self._print_contact_details = print_contact_details

    @property
    def print_statements(self):
        return self._print_statements

    @print_statements.setter
    def print_statements(self, print_statements):
        self._print_statements = print_statements

    @property
    def customer_credit_days(self):
        return self._customer_credit_days

    @customer_credit_days.setter
    def customer_credit_days(self, customer_credit_days):
        self._customer_credit_days = customer_credit_days

    @property
    def vendor_credit_days(self):
        return self._vendor_credit_days

    @vendor_credit_days.setter
    def vendor_credit_days(self, vendor_credit_days):
        self._vendor_credit_days = vendor_credit_days

    @property
    def updated_at(self):
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        self._updated_at = updated_at

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
        if not isinstance(other, InvoiceSettings):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, InvoiceSettings):
            return True
        return self.to_dict() != other.to_dict()
