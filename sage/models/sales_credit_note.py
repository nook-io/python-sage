import pprint

import six

from sage.configuration import Configuration


class SalesCreditNote(object):
    openapi_types = {
        "id": "str",
        "displayed_as": "str",
        "path": "str",
        "created_at": "datetime",
        "updated_at": "datetime",
        "links": "list[Link]",
        "editable": "bool",
        "tax_calculation_method": "str",
        "transaction": "Transaction",
        "transaction_type": "Base",
        "deleted_at": "datetime",
        "is_cis": "bool",
        "cis_applicable_amount": "float",
        "base_currency_cis_applicable_amount": "float",
        "total_after_cis_deduction": "float",
        "base_currency_total_after_cis_deduction": "float",
        "has_cis_labour": "bool",
        "has_cis_materials": "bool",
        "contact": "Contact",
        "credit_note_number_prefix": "str",
        "credit_note_number": "str",
        "contact_name": "str",
        "contact_reference": "str",
        "date": "date",
        "original_invoice_date": "date",
        "reference": "str",
        "main_address_free_form": "str",
        "main_address": "SalesArtefactAddress",
        "delivery_address_free_form": "str",
        "delivery_address": "SalesArtefactAddress",
        "notes": "str",
        "terms_and_conditions": "str",
        "shipping_net_amount": "float",
        "shipping_tax_rate": "Base",
        "shipping_tax_amount": "float",
        "shipping_tax_breakdown": "list[TaxBreakdown]",
        "total_quantity": "float",
        "shipping_total_amount": "float",
        "net_amount": "float",
        "tax_amount": "float",
        "total_amount": "float",
        "payments_allocations_total_amount": "float",
        "payments_allocations_total_discount": "float",
        "total_paid": "float",
        "outstanding_amount": "float",
        "currency": "Base",
        "exchange_rate": "float",
        "inverse_exchange_rate": "float",
        "base_currency_shipping_net_amount": "float",
        "base_currency_shipping_tax_amount": "float",
        "base_currency_shipping_tax_breakdown": "list[TaxBreakdown]",
        "base_currency_shipping_total_amount": "float",
        "total_discount_amount": "float",
        "base_currency_total_discount_amount": "float",
        "base_currency_net_amount": "float",
        "base_currency_tax_amount": "float",
        "base_currency_total_amount": "float",
        "base_currency_outstanding_amount": "float",
        "status": "Base",
        "sent": "bool",
        "sent_by_email": "bool",
        "void_reason": "str",
        "credit_note_lines": "list[SalesCreditNoteLineItem]",
        "tax_analysis": "list[ArtefactTaxAnalysis]",
        "detailed_tax_analysis": "ArtefactDetailedTaxAnalysis",
        "payments_allocations": "list[PaymentAllocation]",
        "last_paid": "date",
        "tax_address_region": "Base",
        "tax_reconciled": "bool",
        "migrated": "bool",
        "withholding_tax_rate": "float",
        "withholding_tax_amount": "float",
        "base_currency_withholding_tax_amount": "float",
    }
    attribute_map = {
        "id": "id",
        "displayed_as": "displayed_as",
        "path": "$path",
        "created_at": "created_at",
        "updated_at": "updated_at",
        "links": "links",
        "editable": "editable",
        "tax_calculation_method": "tax_calculation_method",
        "transaction": "transaction",
        "transaction_type": "transaction_type",
        "deleted_at": "deleted_at",
        "is_cis": "is_cis",
        "cis_applicable_amount": "cis_applicable_amount",
        "base_currency_cis_applicable_amount": "base_currency_cis_applicable_amount",
        "total_after_cis_deduction": "total_after_cis_deduction",
        "base_currency_total_after_cis_deduction": "base_currency_total_after_cis_deduction",
        "has_cis_labour": "has_cis_labour",
        "has_cis_materials": "has_cis_materials",
        "contact": "contact",
        "credit_note_number_prefix": "credit_note_number_prefix",
        "credit_note_number": "credit_note_number",
        "contact_name": "contact_name",
        "contact_reference": "contact_reference",
        "date": "date",
        "original_invoice_date": "original_invoice_date",
        "reference": "reference",
        "main_address_free_form": "main_address_free_form",
        "main_address": "main_address",
        "delivery_address_free_form": "delivery_address_free_form",
        "delivery_address": "delivery_address",
        "notes": "notes",
        "terms_and_conditions": "terms_and_conditions",
        "shipping_net_amount": "shipping_net_amount",
        "shipping_tax_rate": "shipping_tax_rate",
        "shipping_tax_amount": "shipping_tax_amount",
        "shipping_tax_breakdown": "shipping_tax_breakdown",
        "total_quantity": "total_quantity",
        "shipping_total_amount": "shipping_total_amount",
        "net_amount": "net_amount",
        "tax_amount": "tax_amount",
        "total_amount": "total_amount",
        "payments_allocations_total_amount": "payments_allocations_total_amount",
        "payments_allocations_total_discount": "payments_allocations_total_discount",
        "total_paid": "total_paid",
        "outstanding_amount": "outstanding_amount",
        "currency": "currency",
        "exchange_rate": "exchange_rate",
        "inverse_exchange_rate": "inverse_exchange_rate",
        "base_currency_shipping_net_amount": "base_currency_shipping_net_amount",
        "base_currency_shipping_tax_amount": "base_currency_shipping_tax_amount",
        "base_currency_shipping_tax_breakdown": "base_currency_shipping_tax_breakdown",
        "base_currency_shipping_total_amount": "base_currency_shipping_total_amount",
        "total_discount_amount": "total_discount_amount",
        "base_currency_total_discount_amount": "base_currency_total_discount_amount",
        "base_currency_net_amount": "base_currency_net_amount",
        "base_currency_tax_amount": "base_currency_tax_amount",
        "base_currency_total_amount": "base_currency_total_amount",
        "base_currency_outstanding_amount": "base_currency_outstanding_amount",
        "status": "status",
        "sent": "sent",
        "sent_by_email": "sent_by_email",
        "void_reason": "void_reason",
        "credit_note_lines": "credit_note_lines",
        "tax_analysis": "tax_analysis",
        "detailed_tax_analysis": "detailed_tax_analysis",
        "payments_allocations": "payments_allocations",
        "last_paid": "last_paid",
        "tax_address_region": "tax_address_region",
        "tax_reconciled": "tax_reconciled",
        "migrated": "migrated",
        "withholding_tax_rate": "withholding_tax_rate",
        "withholding_tax_amount": "withholding_tax_amount",
        "base_currency_withholding_tax_amount": "base_currency_withholding_tax_amount",
    }

    def __init__(
        self,
        id=None,
        displayed_as=None,
        path=None,
        created_at=None,
        updated_at=None,
        links=None,
        editable=None,
        tax_calculation_method=None,
        transaction=None,
        transaction_type=None,
        deleted_at=None,
        is_cis=None,
        cis_applicable_amount=None,
        base_currency_cis_applicable_amount=None,
        total_after_cis_deduction=None,
        base_currency_total_after_cis_deduction=None,
        has_cis_labour=None,
        has_cis_materials=None,
        contact=None,
        credit_note_number_prefix=None,
        credit_note_number=None,
        contact_name=None,
        contact_reference=None,
        date=None,
        original_invoice_date=None,
        reference=None,
        main_address_free_form=None,
        main_address=None,
        delivery_address_free_form=None,
        delivery_address=None,
        notes=None,
        terms_and_conditions=None,
        shipping_net_amount=None,
        shipping_tax_rate=None,
        shipping_tax_amount=None,
        shipping_tax_breakdown=None,
        total_quantity=None,
        shipping_total_amount=None,
        net_amount=None,
        tax_amount=None,
        total_amount=None,
        payments_allocations_total_amount=None,
        payments_allocations_total_discount=None,
        total_paid=None,
        outstanding_amount=None,
        currency=None,
        exchange_rate=None,
        inverse_exchange_rate=None,
        base_currency_shipping_net_amount=None,
        base_currency_shipping_tax_amount=None,
        base_currency_shipping_tax_breakdown=None,
        base_currency_shipping_total_amount=None,
        total_discount_amount=None,
        base_currency_total_discount_amount=None,
        base_currency_net_amount=None,
        base_currency_tax_amount=None,
        base_currency_total_amount=None,
        base_currency_outstanding_amount=None,
        status=None,
        sent=None,
        sent_by_email=None,
        void_reason=None,
        credit_note_lines=None,
        tax_analysis=None,
        detailed_tax_analysis=None,
        payments_allocations=None,
        last_paid=None,
        tax_address_region=None,
        tax_reconciled=None,
        migrated=None,
        withholding_tax_rate=None,
        withholding_tax_amount=None,
        base_currency_withholding_tax_amount=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._id = None
        self._displayed_as = None
        self._path = None
        self._created_at = None
        self._updated_at = None
        self._links = None
        self._editable = None
        self._tax_calculation_method = None
        self._transaction = None
        self._transaction_type = None
        self._deleted_at = None
        self._is_cis = None
        self._cis_applicable_amount = None
        self._base_currency_cis_applicable_amount = None
        self._total_after_cis_deduction = None
        self._base_currency_total_after_cis_deduction = None
        self._has_cis_labour = None
        self._has_cis_materials = None
        self._contact = None
        self._credit_note_number_prefix = None
        self._credit_note_number = None
        self._contact_name = None
        self._contact_reference = None
        self._date = None
        self._original_invoice_date = None
        self._reference = None
        self._main_address_free_form = None
        self._main_address = None
        self._delivery_address_free_form = None
        self._delivery_address = None
        self._notes = None
        self._terms_and_conditions = None
        self._shipping_net_amount = None
        self._shipping_tax_rate = None
        self._shipping_tax_amount = None
        self._shipping_tax_breakdown = None
        self._total_quantity = None
        self._shipping_total_amount = None
        self._net_amount = None
        self._tax_amount = None
        self._total_amount = None
        self._payments_allocations_total_amount = None
        self._payments_allocations_total_discount = None
        self._total_paid = None
        self._outstanding_amount = None
        self._currency = None
        self._exchange_rate = None
        self._inverse_exchange_rate = None
        self._base_currency_shipping_net_amount = None
        self._base_currency_shipping_tax_amount = None
        self._base_currency_shipping_tax_breakdown = None
        self._base_currency_shipping_total_amount = None
        self._total_discount_amount = None
        self._base_currency_total_discount_amount = None
        self._base_currency_net_amount = None
        self._base_currency_tax_amount = None
        self._base_currency_total_amount = None
        self._base_currency_outstanding_amount = None
        self._status = None
        self._sent = None
        self._sent_by_email = None
        self._void_reason = None
        self._credit_note_lines = None
        self._tax_analysis = None
        self._detailed_tax_analysis = None
        self._payments_allocations = None
        self._last_paid = None
        self._tax_address_region = None
        self._tax_reconciled = None
        self._migrated = None
        self._withholding_tax_rate = None
        self._withholding_tax_amount = None
        self._base_currency_withholding_tax_amount = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if displayed_as is not None:
            self.displayed_as = displayed_as
        if path is not None:
            self.path = path
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if links is not None:
            self.links = links
        if editable is not None:
            self.editable = editable
        if tax_calculation_method is not None:
            self.tax_calculation_method = tax_calculation_method
        if transaction is not None:
            self.transaction = transaction
        if transaction_type is not None:
            self.transaction_type = transaction_type
        if deleted_at is not None:
            self.deleted_at = deleted_at
        if is_cis is not None:
            self.is_cis = is_cis
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
        if has_cis_labour is not None:
            self.has_cis_labour = has_cis_labour
        if has_cis_materials is not None:
            self.has_cis_materials = has_cis_materials
        if contact is not None:
            self.contact = contact
        if credit_note_number_prefix is not None:
            self.credit_note_number_prefix = credit_note_number_prefix
        if credit_note_number is not None:
            self.credit_note_number = credit_note_number
        if contact_name is not None:
            self.contact_name = contact_name
        if contact_reference is not None:
            self.contact_reference = contact_reference
        if date is not None:
            self.date = date
        if original_invoice_date is not None:
            self.original_invoice_date = original_invoice_date
        if reference is not None:
            self.reference = reference
        if main_address_free_form is not None:
            self.main_address_free_form = main_address_free_form
        if main_address is not None:
            self.main_address = main_address
        if delivery_address_free_form is not None:
            self.delivery_address_free_form = delivery_address_free_form
        if delivery_address is not None:
            self.delivery_address = delivery_address
        if notes is not None:
            self.notes = notes
        if terms_and_conditions is not None:
            self.terms_and_conditions = terms_and_conditions
        if shipping_net_amount is not None:
            self.shipping_net_amount = shipping_net_amount
        if shipping_tax_rate is not None:
            self.shipping_tax_rate = shipping_tax_rate
        if shipping_tax_amount is not None:
            self.shipping_tax_amount = shipping_tax_amount
        if shipping_tax_breakdown is not None:
            self.shipping_tax_breakdown = shipping_tax_breakdown
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
        if payments_allocations_total_amount is not None:
            self.payments_allocations_total_amount = payments_allocations_total_amount
        if payments_allocations_total_discount is not None:
            self.payments_allocations_total_discount = (
                payments_allocations_total_discount
            )
        if total_paid is not None:
            self.total_paid = total_paid
        if outstanding_amount is not None:
            self.outstanding_amount = outstanding_amount
        if currency is not None:
            self.currency = currency
        if exchange_rate is not None:
            self.exchange_rate = exchange_rate
        if inverse_exchange_rate is not None:
            self.inverse_exchange_rate = inverse_exchange_rate
        if base_currency_shipping_net_amount is not None:
            self.base_currency_shipping_net_amount = base_currency_shipping_net_amount
        if base_currency_shipping_tax_amount is not None:
            self.base_currency_shipping_tax_amount = base_currency_shipping_tax_amount
        if base_currency_shipping_tax_breakdown is not None:
            self.base_currency_shipping_tax_breakdown = (
                base_currency_shipping_tax_breakdown
            )
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
        if base_currency_outstanding_amount is not None:
            self.base_currency_outstanding_amount = base_currency_outstanding_amount
        if status is not None:
            self.status = status
        if sent is not None:
            self.sent = sent
        if sent_by_email is not None:
            self.sent_by_email = sent_by_email
        if void_reason is not None:
            self.void_reason = void_reason
        if credit_note_lines is not None:
            self.credit_note_lines = credit_note_lines
        if tax_analysis is not None:
            self.tax_analysis = tax_analysis
        if detailed_tax_analysis is not None:
            self.detailed_tax_analysis = detailed_tax_analysis
        if payments_allocations is not None:
            self.payments_allocations = payments_allocations
        if last_paid is not None:
            self.last_paid = last_paid
        if tax_address_region is not None:
            self.tax_address_region = tax_address_region
        if tax_reconciled is not None:
            self.tax_reconciled = tax_reconciled
        if migrated is not None:
            self.migrated = migrated
        if withholding_tax_rate is not None:
            self.withholding_tax_rate = withholding_tax_rate
        if withholding_tax_amount is not None:
            self.withholding_tax_amount = withholding_tax_amount
        if base_currency_withholding_tax_amount is not None:
            self.base_currency_withholding_tax_amount = (
                base_currency_withholding_tax_amount
            )

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
    def path(self):
        return self._path

    @path.setter
    def path(self, path):
        self._path = path

    @property
    def created_at(self):
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        self._created_at = created_at

    @property
    def updated_at(self):
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        self._updated_at = updated_at

    @property
    def links(self):
        return self._links

    @links.setter
    def links(self, links):
        self._links = links

    @property
    def editable(self):
        return self._editable

    @editable.setter
    def editable(self, editable):
        self._editable = editable

    @property
    def tax_calculation_method(self):
        return self._tax_calculation_method

    @tax_calculation_method.setter
    def tax_calculation_method(self, tax_calculation_method):
        self._tax_calculation_method = tax_calculation_method

    @property
    def transaction(self):
        return self._transaction

    @transaction.setter
    def transaction(self, transaction):
        self._transaction = transaction

    @property
    def transaction_type(self):
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        self._transaction_type = transaction_type

    @property
    def deleted_at(self):
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        self._deleted_at = deleted_at

    @property
    def is_cis(self):
        return self._is_cis

    @is_cis.setter
    def is_cis(self, is_cis):
        self._is_cis = is_cis

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
    def has_cis_labour(self):
        return self._has_cis_labour

    @has_cis_labour.setter
    def has_cis_labour(self, has_cis_labour):
        self._has_cis_labour = has_cis_labour

    @property
    def has_cis_materials(self):
        return self._has_cis_materials

    @has_cis_materials.setter
    def has_cis_materials(self, has_cis_materials):
        self._has_cis_materials = has_cis_materials

    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, contact):
        self._contact = contact

    @property
    def credit_note_number_prefix(self):
        return self._credit_note_number_prefix

    @credit_note_number_prefix.setter
    def credit_note_number_prefix(self, credit_note_number_prefix):
        if (
            self.local_vars_configuration.client_side_validation
            and credit_note_number_prefix is not None
            and len(credit_note_number_prefix) > 6
        ):
            raise ValueError(
                "Invalid value for `credit_note_number_prefix`, length must be less than or equal to `6`"
            )
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
        if (
            self.local_vars_configuration.client_side_validation
            and contact_name is not None
            and len(contact_name) > 255
        ):
            raise ValueError(
                "Invalid value for `contact_name`, length must be less than or equal to `255`"
            )
        self._contact_name = contact_name

    @property
    def contact_reference(self):
        return self._contact_reference

    @contact_reference.setter
    def contact_reference(self, contact_reference):
        if (
            self.local_vars_configuration.client_side_validation
            and contact_reference is not None
            and len(contact_reference) > 255
        ):
            raise ValueError(
                "Invalid value for `contact_reference`, length must be less than or equal to `255`"
            )
        self._contact_reference = contact_reference

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

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
    def main_address_free_form(self):
        return self._main_address_free_form

    @main_address_free_form.setter
    def main_address_free_form(self, main_address_free_form):
        if (
            self.local_vars_configuration.client_side_validation
            and main_address_free_form is not None
            and len(main_address_free_form) > 500
        ):
            raise ValueError(
                "Invalid value for `main_address_free_form`, length must be less than or equal to `500`"
            )
        self._main_address_free_form = main_address_free_form

    @property
    def main_address(self):
        return self._main_address

    @main_address.setter
    def main_address(self, main_address):
        self._main_address = main_address

    @property
    def delivery_address_free_form(self):
        return self._delivery_address_free_form

    @delivery_address_free_form.setter
    def delivery_address_free_form(self, delivery_address_free_form):
        if (
            self.local_vars_configuration.client_side_validation
            and delivery_address_free_form is not None
            and len(delivery_address_free_form) > 500
        ):
            raise ValueError(
                "Invalid value for `delivery_address_free_form`, length must be less than or equal to `500`"
            )
        self._delivery_address_free_form = delivery_address_free_form

    @property
    def delivery_address(self):
        return self._delivery_address

    @delivery_address.setter
    def delivery_address(self, delivery_address):
        self._delivery_address = delivery_address

    @property
    def notes(self):
        return self._notes

    @notes.setter
    def notes(self, notes):
        if (
            self.local_vars_configuration.client_side_validation
            and notes is not None
            and len(notes) > 2000
        ):
            raise ValueError(
                "Invalid value for `notes`, length must be less than or equal to `2000`"
            )
        self._notes = notes

    @property
    def terms_and_conditions(self):
        return self._terms_and_conditions

    @terms_and_conditions.setter
    def terms_and_conditions(self, terms_and_conditions):
        if (
            self.local_vars_configuration.client_side_validation
            and terms_and_conditions is not None
            and len(terms_and_conditions) > 65535
        ):
            raise ValueError(
                "Invalid value for `terms_and_conditions`, length must be less than or equal to `65535`"
            )
        self._terms_and_conditions = terms_and_conditions

    @property
    def shipping_net_amount(self):
        return self._shipping_net_amount

    @shipping_net_amount.setter
    def shipping_net_amount(self, shipping_net_amount):
        self._shipping_net_amount = shipping_net_amount

    @property
    def shipping_tax_rate(self):
        return self._shipping_tax_rate

    @shipping_tax_rate.setter
    def shipping_tax_rate(self, shipping_tax_rate):
        self._shipping_tax_rate = shipping_tax_rate

    @property
    def shipping_tax_amount(self):
        return self._shipping_tax_amount

    @shipping_tax_amount.setter
    def shipping_tax_amount(self, shipping_tax_amount):
        self._shipping_tax_amount = shipping_tax_amount

    @property
    def shipping_tax_breakdown(self):
        return self._shipping_tax_breakdown

    @shipping_tax_breakdown.setter
    def shipping_tax_breakdown(self, shipping_tax_breakdown):
        self._shipping_tax_breakdown = shipping_tax_breakdown

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
    def payments_allocations_total_amount(self):
        return self._payments_allocations_total_amount

    @payments_allocations_total_amount.setter
    def payments_allocations_total_amount(self, payments_allocations_total_amount):
        self._payments_allocations_total_amount = payments_allocations_total_amount

    @property
    def payments_allocations_total_discount(self):
        return self._payments_allocations_total_discount

    @payments_allocations_total_discount.setter
    def payments_allocations_total_discount(self, payments_allocations_total_discount):
        self._payments_allocations_total_discount = payments_allocations_total_discount

    @property
    def total_paid(self):
        return self._total_paid

    @total_paid.setter
    def total_paid(self, total_paid):
        self._total_paid = total_paid

    @property
    def outstanding_amount(self):
        return self._outstanding_amount

    @outstanding_amount.setter
    def outstanding_amount(self, outstanding_amount):
        self._outstanding_amount = outstanding_amount

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, currency):
        self._currency = currency

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
    def base_currency_shipping_tax_breakdown(self):
        return self._base_currency_shipping_tax_breakdown

    @base_currency_shipping_tax_breakdown.setter
    def base_currency_shipping_tax_breakdown(
        self, base_currency_shipping_tax_breakdown
    ):
        self._base_currency_shipping_tax_breakdown = (
            base_currency_shipping_tax_breakdown
        )

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
    def base_currency_outstanding_amount(self):
        return self._base_currency_outstanding_amount

    @base_currency_outstanding_amount.setter
    def base_currency_outstanding_amount(self, base_currency_outstanding_amount):
        self._base_currency_outstanding_amount = base_currency_outstanding_amount

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def sent(self):
        return self._sent

    @sent.setter
    def sent(self, sent):
        self._sent = sent

    @property
    def sent_by_email(self):
        return self._sent_by_email

    @sent_by_email.setter
    def sent_by_email(self, sent_by_email):
        self._sent_by_email = sent_by_email

    @property
    def void_reason(self):
        return self._void_reason

    @void_reason.setter
    def void_reason(self, void_reason):
        if (
            self.local_vars_configuration.client_side_validation
            and void_reason is not None
            and len(void_reason) > 200
        ):
            raise ValueError(
                "Invalid value for `void_reason`, length must be less than or equal to `200`"
            )
        self._void_reason = void_reason

    @property
    def credit_note_lines(self):
        return self._credit_note_lines

    @credit_note_lines.setter
    def credit_note_lines(self, credit_note_lines):
        self._credit_note_lines = credit_note_lines

    @property
    def tax_analysis(self):
        return self._tax_analysis

    @tax_analysis.setter
    def tax_analysis(self, tax_analysis):
        self._tax_analysis = tax_analysis

    @property
    def detailed_tax_analysis(self):
        return self._detailed_tax_analysis

    @detailed_tax_analysis.setter
    def detailed_tax_analysis(self, detailed_tax_analysis):
        self._detailed_tax_analysis = detailed_tax_analysis

    @property
    def payments_allocations(self):
        return self._payments_allocations

    @payments_allocations.setter
    def payments_allocations(self, payments_allocations):
        self._payments_allocations = payments_allocations

    @property
    def last_paid(self):
        return self._last_paid

    @last_paid.setter
    def last_paid(self, last_paid):
        self._last_paid = last_paid

    @property
    def tax_address_region(self):
        return self._tax_address_region

    @tax_address_region.setter
    def tax_address_region(self, tax_address_region):
        self._tax_address_region = tax_address_region

    @property
    def tax_reconciled(self):
        return self._tax_reconciled

    @tax_reconciled.setter
    def tax_reconciled(self, tax_reconciled):
        self._tax_reconciled = tax_reconciled

    @property
    def migrated(self):
        return self._migrated

    @migrated.setter
    def migrated(self, migrated):
        self._migrated = migrated

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
        if not isinstance(other, SalesCreditNote):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, SalesCreditNote):
            return True
        return self.to_dict() != other.to_dict()
