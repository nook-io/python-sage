import pprint
import six
from sage.configuration import Configuration


class PurchaseInvoicePush(object):
    openapi_types = {
        "id": "str",
        "displayed_as": "str",
        "path": "str",
        "created_at": "datetime",
        "updated_at": "datetime",
        "links": "list[Link]",
        "editable": "bool",
        "transaction": "Transaction",
        "transaction_type": "Base",
        "postponed_accounting": "bool",
        "_import": "bool",
        "deleted_at": "datetime",
        "is_cis": "bool",
        "cis_applicable_amount": "float",
        "base_currency_cis_applicable_amount": "float",
        "total_after_cis_deduction": "float",
        "base_currency_total_after_cis_deduction": "float",
        "has_cis_labour": "bool",
        "has_cis_materials": "bool",
        "contact_id": "str",
        "base_currency_total_itc_amount": "float",
        "total_itc_amount": "float",
        "base_currency_total_itr_amount": "float",
        "total_itr_amount": "float",
        "part_recoverable": "bool",
        "contact_name": "str",
        "contact_reference": "str",
        "date": "date",
        "due_date": "date",
        "reference": "str",
        "vendor_reference": "str",
        "notes": "str",
        "total_quantity": "float",
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
        "base_currency_net_amount": "float",
        "base_currency_tax_amount": "float",
        "base_currency_total_amount": "float",
        "base_currency_outstanding_amount": "float",
        "status_id": "str",
        "void_reason": "str",
        "invoice_lines": "list[PurchaseInvoiceLineItem]",
        "tax_analysis": "list[ArtefactTaxAnalysis]",
        "detailed_tax_analysis": "ArtefactDetailedTaxAnalysis",
        "payments_allocations": "list[PaymentAllocation]",
        "last_paid": "date",
        "tax_address_region": "Base",
        "withholding_tax_rate": "float",
        "withholding_tax_amount": "float",
        "base_currency_withholding_tax_amount": "float",
        "corrections": "list[PurchaseCorrectiveInvoice]",
        "tax_reconciled": "bool",
        "migrated": "bool",
        "tax_calculation_method": "str",
    }
    attribute_map = {
        "id": "id",
        "displayed_as": "displayed_as",
        "path": "$path",
        "created_at": "created_at",
        "updated_at": "updated_at",
        "links": "links",
        "editable": "editable",
        "transaction": "transaction",
        "transaction_type": "transaction_type",
        "postponed_accounting": "postponed_accounting",
        "_import": "import",
        "deleted_at": "deleted_at",
        "is_cis": "is_cis",
        "cis_applicable_amount": "cis_applicable_amount",
        "base_currency_cis_applicable_amount": "base_currency_cis_applicable_amount",
        "total_after_cis_deduction": "total_after_cis_deduction",
        "base_currency_total_after_cis_deduction": "base_currency_total_after_cis_deduction",
        "has_cis_labour": "has_cis_labour",
        "has_cis_materials": "has_cis_materials",
        "contact_id": "contact_id",
        "base_currency_total_itc_amount": "base_currency_total_itc_amount",
        "total_itc_amount": "total_itc_amount",
        "base_currency_total_itr_amount": "base_currency_total_itr_amount",
        "total_itr_amount": "total_itr_amount",
        "part_recoverable": "part_recoverable",
        "contact_name": "contact_name",
        "contact_reference": "contact_reference",
        "date": "date",
        "due_date": "due_date",
        "reference": "reference",
        "vendor_reference": "vendor_reference",
        "notes": "notes",
        "total_quantity": "total_quantity",
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
        "base_currency_net_amount": "base_currency_net_amount",
        "base_currency_tax_amount": "base_currency_tax_amount",
        "base_currency_total_amount": "base_currency_total_amount",
        "base_currency_outstanding_amount": "base_currency_outstanding_amount",
        "status_id": "status_id",
        "void_reason": "void_reason",
        "invoice_lines": "invoice_lines",
        "tax_analysis": "tax_analysis",
        "detailed_tax_analysis": "detailed_tax_analysis",
        "payments_allocations": "payments_allocations",
        "last_paid": "last_paid",
        "tax_address_region": "tax_address_region",
        "withholding_tax_rate": "withholding_tax_rate",
        "withholding_tax_amount": "withholding_tax_amount",
        "base_currency_withholding_tax_amount": "base_currency_withholding_tax_amount",
        "corrections": "corrections",
        "tax_reconciled": "tax_reconciled",
        "migrated": "migrated",
        "tax_calculation_method": "tax_calculation_method",
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
        transaction=None,
        transaction_type=None,
        postponed_accounting=None,
        _import=None,
        deleted_at=None,
        is_cis=None,
        cis_applicable_amount=None,
        base_currency_cis_applicable_amount=None,
        total_after_cis_deduction=None,
        base_currency_total_after_cis_deduction=None,
        has_cis_labour=None,
        has_cis_materials=None,
        contact_id=None,
        base_currency_total_itc_amount=None,
        total_itc_amount=None,
        base_currency_total_itr_amount=None,
        total_itr_amount=None,
        part_recoverable=None,
        contact_name=None,
        contact_reference=None,
        date=None,
        due_date=None,
        reference=None,
        vendor_reference=None,
        notes=None,
        total_quantity=None,
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
        base_currency_net_amount=None,
        base_currency_tax_amount=None,
        base_currency_total_amount=None,
        base_currency_outstanding_amount=None,
        status_id=None,
        void_reason=None,
        invoice_lines=None,
        tax_analysis=None,
        detailed_tax_analysis=None,
        payments_allocations=None,
        last_paid=None,
        tax_address_region=None,
        withholding_tax_rate=None,
        withholding_tax_amount=None,
        base_currency_withholding_tax_amount=None,
        corrections=None,
        tax_reconciled=None,
        migrated=None,
        tax_calculation_method=None,
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
        self._transaction = None
        self._transaction_type = None
        self._postponed_accounting = None
        self.__import = None
        self._deleted_at = None
        self._is_cis = None
        self._cis_applicable_amount = None
        self._base_currency_cis_applicable_amount = None
        self._total_after_cis_deduction = None
        self._base_currency_total_after_cis_deduction = None
        self._has_cis_labour = None
        self._has_cis_materials = None
        self._contact_id = None
        self._base_currency_total_itc_amount = None
        self._total_itc_amount = None
        self._base_currency_total_itr_amount = None
        self._total_itr_amount = None
        self._part_recoverable = None
        self._contact_name = None
        self._contact_reference = None
        self._date = None
        self._due_date = None
        self._reference = None
        self._vendor_reference = None
        self._notes = None
        self._total_quantity = None
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
        self._base_currency_net_amount = None
        self._base_currency_tax_amount = None
        self._base_currency_total_amount = None
        self._base_currency_outstanding_amount = None
        self._status_id = None
        self._void_reason = None
        self._invoice_lines = None
        self._tax_analysis = None
        self._detailed_tax_analysis = None
        self._payments_allocations = None
        self._last_paid = None
        self._tax_address_region = None
        self._withholding_tax_rate = None
        self._withholding_tax_amount = None
        self._base_currency_withholding_tax_amount = None
        self._corrections = None
        self._tax_reconciled = None
        self._migrated = None
        self._tax_calculation_method = None
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
        if transaction is not None:
            self.transaction = transaction
        if transaction_type is not None:
            self.transaction_type = transaction_type
        if postponed_accounting is not None:
            self.postponed_accounting = postponed_accounting
        if _import is not None:
            self._import = _import
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
        if contact_id is not None:
            self.contact_id = contact_id
        if base_currency_total_itc_amount is not None:
            self.base_currency_total_itc_amount = base_currency_total_itc_amount
        if total_itc_amount is not None:
            self.total_itc_amount = total_itc_amount
        if base_currency_total_itr_amount is not None:
            self.base_currency_total_itr_amount = base_currency_total_itr_amount
        if total_itr_amount is not None:
            self.total_itr_amount = total_itr_amount
        if part_recoverable is not None:
            self.part_recoverable = part_recoverable
        if contact_name is not None:
            self.contact_name = contact_name
        if contact_reference is not None:
            self.contact_reference = contact_reference
        if date is not None:
            self.date = date
        if due_date is not None:
            self.due_date = due_date
        if reference is not None:
            self.reference = reference
        if vendor_reference is not None:
            self.vendor_reference = vendor_reference
        if notes is not None:
            self.notes = notes
        if total_quantity is not None:
            self.total_quantity = total_quantity
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
        if base_currency_net_amount is not None:
            self.base_currency_net_amount = base_currency_net_amount
        if base_currency_tax_amount is not None:
            self.base_currency_tax_amount = base_currency_tax_amount
        if base_currency_total_amount is not None:
            self.base_currency_total_amount = base_currency_total_amount
        if base_currency_outstanding_amount is not None:
            self.base_currency_outstanding_amount = base_currency_outstanding_amount
        if status_id is not None:
            self.status_id = status_id
        if void_reason is not None:
            self.void_reason = void_reason
        if invoice_lines is not None:
            self.invoice_lines = invoice_lines
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
        if withholding_tax_rate is not None:
            self.withholding_tax_rate = withholding_tax_rate
        if withholding_tax_amount is not None:
            self.withholding_tax_amount = withholding_tax_amount
        if base_currency_withholding_tax_amount is not None:
            self.base_currency_withholding_tax_amount = (
                base_currency_withholding_tax_amount
            )
        if corrections is not None:
            self.corrections = corrections
        if tax_reconciled is not None:
            self.tax_reconciled = tax_reconciled
        if migrated is not None:
            self.migrated = migrated
        if tax_calculation_method is not None:
            self.tax_calculation_method = tax_calculation_method

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
    def postponed_accounting(self):
        return self._postponed_accounting

    @postponed_accounting.setter
    def postponed_accounting(self, postponed_accounting):
        self._postponed_accounting = postponed_accounting

    @property
    def _import(self):
        return self.__import

    @_import.setter
    def _import(self, _import):
        self.__import = _import

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
    def contact_id(self):
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        self._contact_id = contact_id

    @property
    def base_currency_total_itc_amount(self):
        return self._base_currency_total_itc_amount

    @base_currency_total_itc_amount.setter
    def base_currency_total_itc_amount(self, base_currency_total_itc_amount):
        self._base_currency_total_itc_amount = base_currency_total_itc_amount

    @property
    def total_itc_amount(self):
        return self._total_itc_amount

    @total_itc_amount.setter
    def total_itc_amount(self, total_itc_amount):
        self._total_itc_amount = total_itc_amount

    @property
    def base_currency_total_itr_amount(self):
        return self._base_currency_total_itr_amount

    @base_currency_total_itr_amount.setter
    def base_currency_total_itr_amount(self, base_currency_total_itr_amount):
        self._base_currency_total_itr_amount = base_currency_total_itr_amount

    @property
    def total_itr_amount(self):
        return self._total_itr_amount

    @total_itr_amount.setter
    def total_itr_amount(self, total_itr_amount):
        self._total_itr_amount = total_itr_amount

    @property
    def part_recoverable(self):
        return self._part_recoverable

    @part_recoverable.setter
    def part_recoverable(self, part_recoverable):
        self._part_recoverable = part_recoverable

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
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        self._due_date = due_date

    @property
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, reference):
        if (
            self.local_vars_configuration.client_side_validation
            and reference is not None
            and len(reference) > 25
        ):
            raise ValueError(
                "Invalid value for `reference`, length must be less than or equal to `25`"
            )
        self._reference = reference

    @property
    def vendor_reference(self):
        return self._vendor_reference

    @vendor_reference.setter
    def vendor_reference(self, vendor_reference):
        if (
            self.local_vars_configuration.client_side_validation
            and vendor_reference is not None
            and len(vendor_reference) > 31
        ):
            raise ValueError(
                "Invalid value for `vendor_reference`, length must be less than or equal to `31`"
            )
        self._vendor_reference = vendor_reference

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
    def total_quantity(self):
        return self._total_quantity

    @total_quantity.setter
    def total_quantity(self, total_quantity):
        self._total_quantity = total_quantity

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
    def status_id(self):
        return self._status_id

    @status_id.setter
    def status_id(self, status_id):
        self._status_id = status_id

    @property
    def void_reason(self):
        return self._void_reason

    @void_reason.setter
    def void_reason(self, void_reason):
        if (
            self.local_vars_configuration.client_side_validation
            and void_reason is not None
            and len(void_reason) > 255
        ):
            raise ValueError(
                "Invalid value for `void_reason`, length must be less than or equal to `255`"
            )
        self._void_reason = void_reason

    @property
    def invoice_lines(self):
        return self._invoice_lines

    @invoice_lines.setter
    def invoice_lines(self, invoice_lines):
        self._invoice_lines = invoice_lines

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
    def corrections(self):
        return self._corrections

    @corrections.setter
    def corrections(self, corrections):
        self._corrections = corrections

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
    def tax_calculation_method(self):
        return self._tax_calculation_method

    @tax_calculation_method.setter
    def tax_calculation_method(self, tax_calculation_method):
        self._tax_calculation_method = tax_calculation_method

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
        if not isinstance(other, PurchaseInvoice):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PurchaseInvoice):
            return True
        return self.to_dict() != other.to_dict()
