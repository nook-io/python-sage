import pprint
import six
from sage.configuration import Configuration


class Contact(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        "id": "str",
        "displayed_as": "str",
        "path": "str",
        "created_at": "datetime",
        "updated_at": "datetime",
        "links": "list[Link]",
        "deleted_at": "datetime",
        "balance": "float",
        "contact_types": "list[Base]",
        "name": "str",
        "reference": "str",
        "default_sales_ledger_account": "LedgerAccount",
        "default_sales_tax_rate": "Base",
        "default_purchase_ledger_account": "LedgerAccount",
        "tax_number": "str",
        "notes": "str",
        "locale": "str",
        "main_address": "Address",
        "delivery_address": "Address",
        "main_contact_person": "ContactPerson",
        "bank_account_details": "BankAccountDetails",
        "credit_limit": "float",
        "credit_days": "int",
        "credit_terms_and_conditions": "str",
        "product_sales_price_type": "Base",
        "source_guid": "str",
        "currency": "Base",
        "aux_reference": "str",
        "registered_number": "str",
        "deletable": "bool",
        "tax_treatment": "ContactTaxTreatment",
        "email": "str",
        "tax_calculation": "str",
        "auxiliary_account": "str",
        "gdpr_obfuscated": "bool",
        "system": "bool",
        "has_unfinished_recurring_invoices": "bool",
        "cis_registered": "bool",
        "ni_based": "bool",
        "cis_settings": "ContactCisSettings",
    }
    attribute_map = {
        "id": "id",
        "displayed_as": "displayed_as",
        "path": "$path",
        "created_at": "created_at",
        "updated_at": "updated_at",
        "links": "links",
        "deleted_at": "deleted_at",
        "balance": "balance",
        "contact_type_ids": "contact_type_ids",
        "contact_types": "contact_types",
        "name": "name",
        "reference": "reference",
        "default_sales_ledger_account": "default_sales_ledger_account",
        "default_sales_tax_rate": "default_sales_tax_rate",
        "default_purchase_ledger_account": "default_purchase_ledger_account",
        "tax_number": "tax_number",
        "notes": "notes",
        "locale": "locale",
        "main_address": "main_address",
        "delivery_address": "delivery_address",
        "main_contact_person": "main_contact_person",
        "bank_account_details": "bank_account_details",
        "credit_limit": "credit_limit",
        "credit_days": "credit_days",
        "credit_terms_and_conditions": "credit_terms_and_conditions",
        "product_sales_price_type": "product_sales_price_type",
        "source_guid": "source_guid",
        "currency": "currency",
        "aux_reference": "aux_reference",
        "registered_number": "registered_number",
        "deletable": "deletable",
        "tax_treatment": "tax_treatment",
        "email": "email",
        "tax_calculation": "tax_calculation",
        "auxiliary_account": "auxiliary_account",
        "gdpr_obfuscated": "gdpr_obfuscated",
        "system": "system",
        "has_unfinished_recurring_invoices": "has_unfinished_recurring_invoices",
        "cis_registered": "cis_registered",
        "ni_based": "ni_based",
        "cis_settings": "cis_settings",
    }

    def __init__(
        self,
        id=None,
        displayed_as=None,
        path=None,
        created_at=None,
        updated_at=None,
        links=None,
        deleted_at=None,
        balance=None,
        contact_types=None,
        name=None,
        reference=None,
        default_sales_ledger_account=None,
        default_sales_tax_rate=None,
        default_purchase_ledger_account=None,
        tax_number=None,
        notes=None,
        locale=None,
        main_address=None,
        delivery_address=None,
        main_contact_person=None,
        bank_account_details=None,
        credit_limit=None,
        credit_days=None,
        credit_terms_and_conditions=None,
        product_sales_price_type=None,
        source_guid=None,
        currency=None,
        aux_reference=None,
        registered_number=None,
        deletable=None,
        tax_treatment=None,
        email=None,
        tax_calculation=None,
        auxiliary_account=None,
        gdpr_obfuscated=None,
        system=None,
        has_unfinished_recurring_invoices=None,
        cis_registered=None,
        ni_based=None,
        cis_settings=None,
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
        self._deleted_at = None
        self._balance = None
        self._contact_types = None
        self._name = None
        self._reference = None
        self._default_sales_ledger_account = None
        self._default_sales_tax_rate = None
        self._default_purchase_ledger_account = None
        self._tax_number = None
        self._notes = None
        self._locale = None
        self._main_address = None
        self._delivery_address = None
        self._main_contact_person = None
        self._bank_account_details = None
        self._credit_limit = None
        self._credit_days = None
        self._credit_terms_and_conditions = None
        self._product_sales_price_type = None
        self._source_guid = None
        self._currency = None
        self._aux_reference = None
        self._registered_number = None
        self._deletable = None
        self._tax_treatment = None
        self._email = None
        self._tax_calculation = None
        self._auxiliary_account = None
        self._gdpr_obfuscated = None
        self._system = None
        self._has_unfinished_recurring_invoices = None
        self._cis_registered = None
        self._ni_based = None
        self._cis_settings = None
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
        if deleted_at is not None:
            self.deleted_at = deleted_at
        if balance is not None:
            self.balance = balance
        if contact_types is not None:
            self.contact_types = contact_types
        if name is not None:
            self.name = name
        if reference is not None:
            self.reference = reference
        if default_sales_ledger_account is not None:
            self.default_sales_ledger_account = default_sales_ledger_account
        if default_sales_tax_rate is not None:
            self.default_sales_tax_rate = default_sales_tax_rate
        if default_purchase_ledger_account is not None:
            self.default_purchase_ledger_account = default_purchase_ledger_account
        if tax_number is not None:
            self.tax_number = tax_number
        if notes is not None:
            self.notes = notes
        if locale is not None:
            self.locale = locale
        if main_address is not None:
            self.main_address = main_address
        if delivery_address is not None:
            self.delivery_address = delivery_address
        if main_contact_person is not None:
            self.main_contact_person = main_contact_person
        if bank_account_details is not None:
            self.bank_account_details = bank_account_details
        if credit_limit is not None:
            self.credit_limit = credit_limit
        if credit_days is not None:
            self.credit_days = credit_days
        if credit_terms_and_conditions is not None:
            self.credit_terms_and_conditions = credit_terms_and_conditions
        if product_sales_price_type is not None:
            self.product_sales_price_type = product_sales_price_type
        if source_guid is not None:
            self.source_guid = source_guid
        if currency is not None:
            self.currency = currency
        if aux_reference is not None:
            self.aux_reference = aux_reference
        if registered_number is not None:
            self.registered_number = registered_number
        if deletable is not None:
            self.deletable = deletable
        if tax_treatment is not None:
            self.tax_treatment = tax_treatment
        if email is not None:
            self.email = email
        if tax_calculation is not None:
            self.tax_calculation = tax_calculation
        if auxiliary_account is not None:
            self.auxiliary_account = auxiliary_account
        if gdpr_obfuscated is not None:
            self.gdpr_obfuscated = gdpr_obfuscated
        if system is not None:
            self.system = system
        if has_unfinished_recurring_invoices is not None:
            self.has_unfinished_recurring_invoices = has_unfinished_recurring_invoices
        if cis_registered is not None:
            self.cis_registered = cis_registered
        if ni_based is not None:
            self.ni_based = ni_based
        if cis_settings is not None:
            self.cis_settings = cis_settings

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
    def deleted_at(self):
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        self._deleted_at = deleted_at

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        self._balance = balance

    @property
    def contact_types(self):
        return self._contact_types

    @contact_types.setter
    def contact_types(self, contact_types):
        self._contact_types = contact_types

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if (
            self.local_vars_configuration.client_side_validation
            and name is not None
            and len(name) > 100
        ):
            raise ValueError(
                "Invalid value for `name`, length must be less than or equal to `100`"
            )
        self._name = name

    @property
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, reference):
        if (
            self.local_vars_configuration.client_side_validation
            and reference is not None
            and len(reference) > 10
        ):
            raise ValueError(
                "Invalid value for `reference`, length must be less than or equal to `10`"
            )
        self._reference = reference

    @property
    def default_sales_ledger_account(self):
        return self._default_sales_ledger_account

    @default_sales_ledger_account.setter
    def default_sales_ledger_account(self, default_sales_ledger_account):
        self._default_sales_ledger_account = default_sales_ledger_account

    @property
    def default_sales_tax_rate(self):
        return self._default_sales_tax_rate

    @default_sales_tax_rate.setter
    def default_sales_tax_rate(self, default_sales_tax_rate):
        self._default_sales_tax_rate = default_sales_tax_rate

    @property
    def default_purchase_ledger_account(self):
        return self._default_purchase_ledger_account

    @default_purchase_ledger_account.setter
    def default_purchase_ledger_account(self, default_purchase_ledger_account):
        self._default_purchase_ledger_account = default_purchase_ledger_account

    @property
    def tax_number(self):
        return self._tax_number

    @tax_number.setter
    def tax_number(self, tax_number):
        if (
            self.local_vars_configuration.client_side_validation
            and tax_number is not None
            and len(tax_number) > 255
        ):
            raise ValueError(
                "Invalid value for `tax_number`, length must be less than or equal to `255`"
            )
        self._tax_number = tax_number

    @property
    def notes(self):
        return self._notes

    @notes.setter
    def notes(self, notes):
        if (
            self.local_vars_configuration.client_side_validation
            and notes is not None
            and len(notes) > 4000
        ):
            raise ValueError(
                "Invalid value for `notes`, length must be less than or equal to `4000`"
            )
        self._notes = notes

    @property
    def locale(self):
        return self._locale

    @locale.setter
    def locale(self, locale):
        if (
            self.local_vars_configuration.client_side_validation
            and locale is not None
            and len(locale) > 10
        ):
            raise ValueError(
                "Invalid value for `locale`, length must be less than or equal to `10`"
            )
        self._locale = locale

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
    def main_contact_person(self):
        return self._main_contact_person

    @main_contact_person.setter
    def main_contact_person(self, main_contact_person):
        self._main_contact_person = main_contact_person

    @property
    def bank_account_details(self):
        return self._bank_account_details

    @bank_account_details.setter
    def bank_account_details(self, bank_account_details):
        self._bank_account_details = bank_account_details

    @property
    def credit_limit(self):
        return self._credit_limit

    @credit_limit.setter
    def credit_limit(self, credit_limit):
        self._credit_limit = credit_limit

    @property
    def credit_days(self):
        return self._credit_days

    @credit_days.setter
    def credit_days(self, credit_days):
        self._credit_days = credit_days

    @property
    def credit_terms_and_conditions(self):
        return self._credit_terms_and_conditions

    @credit_terms_and_conditions.setter
    def credit_terms_and_conditions(self, credit_terms_and_conditions):
        if (
            self.local_vars_configuration.client_side_validation
            and credit_terms_and_conditions is not None
            and len(credit_terms_and_conditions) > 2000
        ):
            raise ValueError(
                "Invalid value for `credit_terms_and_conditions`, length must be less than or equal to `2000`"
            )
        self._credit_terms_and_conditions = credit_terms_and_conditions

    @property
    def product_sales_price_type(self):
        return self._product_sales_price_type

    @product_sales_price_type.setter
    def product_sales_price_type(self, product_sales_price_type):
        self._product_sales_price_type = product_sales_price_type

    @property
    def source_guid(self):
        return self._source_guid

    @source_guid.setter
    def source_guid(self, source_guid):
        if (
            self.local_vars_configuration.client_side_validation
            and source_guid is not None
            and len(source_guid) > 255
        ):
            raise ValueError(
                "Invalid value for `source_guid`, length must be less than or equal to `255`"
            )
        self._source_guid = source_guid

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, currency):
        self._currency = currency

    @property
    def aux_reference(self):
        return self._aux_reference

    @aux_reference.setter
    def aux_reference(self, aux_reference):
        if (
            self.local_vars_configuration.client_side_validation
            and aux_reference is not None
            and len(aux_reference) > 4
        ):
            raise ValueError(
                "Invalid value for `aux_reference`, length must be less than or equal to `4`"
            )
        self._aux_reference = aux_reference

    @property
    def registered_number(self):
        return self._registered_number

    @registered_number.setter
    def registered_number(self, registered_number):
        if (
            self.local_vars_configuration.client_side_validation
            and registered_number is not None
            and len(registered_number) > 25
        ):
            raise ValueError(
                "Invalid value for `registered_number`, length must be less than or equal to `25`"
            )
        self._registered_number = registered_number

    @property
    def deletable(self):
        return self._deletable

    @deletable.setter
    def deletable(self, deletable):
        self._deletable = deletable

    @property
    def tax_treatment(self):
        return self._tax_treatment

    @tax_treatment.setter
    def tax_treatment(self, tax_treatment):
        self._tax_treatment = tax_treatment

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if (
            self.local_vars_configuration.client_side_validation
            and email is not None
            and len(email) > 100
        ):
            raise ValueError(
                "Invalid value for `email`, length must be less than or equal to `100`"
            )
        self._email = email

    @property
    def tax_calculation(self):
        return self._tax_calculation

    @tax_calculation.setter
    def tax_calculation(self, tax_calculation):
        self._tax_calculation = tax_calculation

    @property
    def auxiliary_account(self):
        return self._auxiliary_account

    @auxiliary_account.setter
    def auxiliary_account(self, auxiliary_account):
        if (
            self.local_vars_configuration.client_side_validation
            and auxiliary_account is not None
            and len(auxiliary_account) > 25
        ):
            raise ValueError(
                "Invalid value for `auxiliary_account`, length must be less than or equal to `25`"
            )
        self._auxiliary_account = auxiliary_account

    @property
    def gdpr_obfuscated(self):
        return self._gdpr_obfuscated

    @gdpr_obfuscated.setter
    def gdpr_obfuscated(self, gdpr_obfuscated):
        self._gdpr_obfuscated = gdpr_obfuscated

    @property
    def system(self):
        return self._system

    @system.setter
    def system(self, system):
        self._system = system

    @property
    def has_unfinished_recurring_invoices(self):
        return self._has_unfinished_recurring_invoices

    @has_unfinished_recurring_invoices.setter
    def has_unfinished_recurring_invoices(self, has_unfinished_recurring_invoices):
        self._has_unfinished_recurring_invoices = has_unfinished_recurring_invoices

    @property
    def cis_registered(self):
        return self._cis_registered

    @cis_registered.setter
    def cis_registered(self, cis_registered):
        self._cis_registered = cis_registered

    @property
    def ni_based(self):
        return self._ni_based

    @ni_based.setter
    def ni_based(self, ni_based):
        self._ni_based = ni_based

    @property
    def cis_settings(self):
        return self._cis_settings

    @cis_settings.setter
    def cis_settings(self, cis_settings):
        self._cis_settings = cis_settings

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
        if not isinstance(other, Contact):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, Contact):
            return True
        return self.to_dict() != other.to_dict()
