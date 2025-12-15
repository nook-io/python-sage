import pprint
import six
from sage.configuration import Configuration


class PutContactsContact(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        "name": "str",
        "contact_type_ids": "list[str]",
        "reference": "str",
        "default_sales_ledger_account_id": "str",
        "default_sales_tax_rate_id": "str",
        "default_purchase_ledger_account_id": "str",
        "tax_number": "str",
        "notes": "str",
        "locale": "str",
        "credit_limit": "float",
        "credit_days": "int",
        "credit_terms_and_conditions": "str",
        "product_sales_price_type_id": "str",
        "source_guid": "str",
        "currency_id": "str",
        "aux_reference": "str",
        "registered_number": "str",
        "tax_calculation": "str",
        "auxiliary_account": "str",
        "main_address": "PostBankAccountsBankAccountMainAddress",
        "delivery_address": "PostBankAccountsBankAccountMainAddress",
        "main_contact_person": "PostContactsContactMainContactPerson",
        "bank_account_details": "PutBankAccountsBankAccountBankAccountDetails",
        "tax_treatment": "PostContactsContactTaxTreatment",
    }
    attribute_map = {
        "name": "name",
        "contact_type_ids": "contact_type_ids",
        "reference": "reference",
        "default_sales_ledger_account_id": "default_sales_ledger_account_id",
        "default_sales_tax_rate_id": "default_sales_tax_rate_id",
        "default_purchase_ledger_account_id": "default_purchase_ledger_account_id",
        "tax_number": "tax_number",
        "notes": "notes",
        "locale": "locale",
        "credit_limit": "credit_limit",
        "credit_days": "credit_days",
        "credit_terms_and_conditions": "credit_terms_and_conditions",
        "product_sales_price_type_id": "product_sales_price_type_id",
        "source_guid": "source_guid",
        "currency_id": "currency_id",
        "aux_reference": "aux_reference",
        "registered_number": "registered_number",
        "tax_calculation": "tax_calculation",
        "auxiliary_account": "auxiliary_account",
        "main_address": "main_address",
        "delivery_address": "delivery_address",
        "main_contact_person": "main_contact_person",
        "bank_account_details": "bank_account_details",
        "tax_treatment": "tax_treatment",
    }

    def __init__(
        self,
        name=None,
        contact_type_ids=None,
        reference=None,
        default_sales_ledger_account_id=None,
        default_sales_tax_rate_id=None,
        default_purchase_ledger_account_id=None,
        tax_number=None,
        notes=None,
        locale=None,
        credit_limit=None,
        credit_days=None,
        credit_terms_and_conditions=None,
        product_sales_price_type_id=None,
        source_guid=None,
        currency_id=None,
        aux_reference=None,
        registered_number=None,
        tax_calculation=None,
        auxiliary_account=None,
        main_address=None,
        delivery_address=None,
        main_contact_person=None,
        bank_account_details=None,
        tax_treatment=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._name = None
        self._contact_type_ids = None
        self._reference = None
        self._default_sales_ledger_account_id = None
        self._default_sales_tax_rate_id = None
        self._default_purchase_ledger_account_id = None
        self._tax_number = None
        self._notes = None
        self._locale = None
        self._credit_limit = None
        self._credit_days = None
        self._credit_terms_and_conditions = None
        self._product_sales_price_type_id = None
        self._source_guid = None
        self._currency_id = None
        self._aux_reference = None
        self._registered_number = None
        self._tax_calculation = None
        self._auxiliary_account = None
        self._main_address = None
        self._delivery_address = None
        self._main_contact_person = None
        self._bank_account_details = None
        self._tax_treatment = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if contact_type_ids is not None:
            self.contact_type_ids = contact_type_ids
        if reference is not None:
            self.reference = reference
        if default_sales_ledger_account_id is not None:
            self.default_sales_ledger_account_id = default_sales_ledger_account_id
        if default_sales_tax_rate_id is not None:
            self.default_sales_tax_rate_id = default_sales_tax_rate_id
        if default_purchase_ledger_account_id is not None:
            self.default_purchase_ledger_account_id = default_purchase_ledger_account_id
        if tax_number is not None:
            self.tax_number = tax_number
        if notes is not None:
            self.notes = notes
        if locale is not None:
            self.locale = locale
        if credit_limit is not None:
            self.credit_limit = credit_limit
        if credit_days is not None:
            self.credit_days = credit_days
        if credit_terms_and_conditions is not None:
            self.credit_terms_and_conditions = credit_terms_and_conditions
        if product_sales_price_type_id is not None:
            self.product_sales_price_type_id = product_sales_price_type_id
        if source_guid is not None:
            self.source_guid = source_guid
        if currency_id is not None:
            self.currency_id = currency_id
        if aux_reference is not None:
            self.aux_reference = aux_reference
        if registered_number is not None:
            self.registered_number = registered_number
        if tax_calculation is not None:
            self.tax_calculation = tax_calculation
        if auxiliary_account is not None:
            self.auxiliary_account = auxiliary_account
        if main_address is not None:
            self.main_address = main_address
        if delivery_address is not None:
            self.delivery_address = delivery_address
        if main_contact_person is not None:
            self.main_contact_person = main_contact_person
        if bank_account_details is not None:
            self.bank_account_details = bank_account_details
        if tax_treatment is not None:
            self.tax_treatment = tax_treatment

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def contact_type_ids(self):
        return self._contact_type_ids

    @contact_type_ids.setter
    def contact_type_ids(self, contact_type_ids):
        self._contact_type_ids = contact_type_ids

    @property
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, reference):
        self._reference = reference

    @property
    def default_sales_ledger_account_id(self):
        return self._default_sales_ledger_account_id

    @default_sales_ledger_account_id.setter
    def default_sales_ledger_account_id(self, default_sales_ledger_account_id):
        self._default_sales_ledger_account_id = default_sales_ledger_account_id

    @property
    def default_sales_tax_rate_id(self):
        return self._default_sales_tax_rate_id

    @default_sales_tax_rate_id.setter
    def default_sales_tax_rate_id(self, default_sales_tax_rate_id):
        self._default_sales_tax_rate_id = default_sales_tax_rate_id

    @property
    def default_purchase_ledger_account_id(self):
        return self._default_purchase_ledger_account_id

    @default_purchase_ledger_account_id.setter
    def default_purchase_ledger_account_id(self, default_purchase_ledger_account_id):
        self._default_purchase_ledger_account_id = default_purchase_ledger_account_id

    @property
    def tax_number(self):
        return self._tax_number

    @tax_number.setter
    def tax_number(self, tax_number):
        self._tax_number = tax_number

    @property
    def notes(self):
        return self._notes

    @notes.setter
    def notes(self, notes):
        self._notes = notes

    @property
    def locale(self):
        return self._locale

    @locale.setter
    def locale(self, locale):
        self._locale = locale

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
        if (
            self.local_vars_configuration.client_side_validation
            and credit_days is not None
            and credit_days > 365
        ):
            raise ValueError(
                "Invalid value for `credit_days`, must be a value less than or equal to `365`"
            )
        if (
            self.local_vars_configuration.client_side_validation
            and credit_days is not None
            and credit_days < 0
        ):
            raise ValueError(
                "Invalid value for `credit_days`, must be a value greater than or equal to `0`"
            )
        self._credit_days = credit_days

    @property
    def credit_terms_and_conditions(self):
        return self._credit_terms_and_conditions

    @credit_terms_and_conditions.setter
    def credit_terms_and_conditions(self, credit_terms_and_conditions):
        self._credit_terms_and_conditions = credit_terms_and_conditions

    @property
    def product_sales_price_type_id(self):
        return self._product_sales_price_type_id

    @product_sales_price_type_id.setter
    def product_sales_price_type_id(self, product_sales_price_type_id):
        self._product_sales_price_type_id = product_sales_price_type_id

    @property
    def source_guid(self):
        return self._source_guid

    @source_guid.setter
    def source_guid(self, source_guid):
        self._source_guid = source_guid

    @property
    def currency_id(self):
        return self._currency_id

    @currency_id.setter
    def currency_id(self, currency_id):
        self._currency_id = currency_id

    @property
    def aux_reference(self):
        return self._aux_reference

    @aux_reference.setter
    def aux_reference(self, aux_reference):
        self._aux_reference = aux_reference

    @property
    def registered_number(self):
        return self._registered_number

    @registered_number.setter
    def registered_number(self, registered_number):
        self._registered_number = registered_number

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
        self._auxiliary_account = auxiliary_account

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
    def tax_treatment(self):
        return self._tax_treatment

    @tax_treatment.setter
    def tax_treatment(self, tax_treatment):
        self._tax_treatment = tax_treatment

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
        if not isinstance(other, PutContactsContact):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PutContactsContact):
            return True
        return self.to_dict() != other.to_dict()
