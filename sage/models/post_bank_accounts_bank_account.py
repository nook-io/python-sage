import pprint
import six
from sage.configuration import Configuration


class PostBankAccountsBankAccount(object):
    openapi_types = {
        "bank_account_type_id": "str",
        "ledger_account_id": "str",
        "nominal_code": "int",
        "default_payment_method_id": "str",
        "gifi_code": "int",
        "bank_account_details": "PostBankAccountsBankAccountBankAccountDetails",
        "main_address": "PostBankAccountsBankAccountMainAddress",
        "main_contact_person": "PostBankAccountsBankAccountMainContactPerson",
        "journal_code": "PostJournalsJournalJournalCode",
    }
    attribute_map = {
        "bank_account_type_id": "bank_account_type_id",
        "ledger_account_id": "ledger_account_id",
        "nominal_code": "nominal_code",
        "default_payment_method_id": "default_payment_method_id",
        "gifi_code": "gifi_code",
        "bank_account_details": "bank_account_details",
        "main_address": "main_address",
        "main_contact_person": "main_contact_person",
        "journal_code": "journal_code",
    }

    def __init__(
        self,
        bank_account_type_id=None,
        ledger_account_id=None,
        nominal_code=None,
        default_payment_method_id=None,
        gifi_code=None,
        bank_account_details=None,
        main_address=None,
        main_contact_person=None,
        journal_code=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._bank_account_type_id = None
        self._ledger_account_id = None
        self._nominal_code = None
        self._default_payment_method_id = None
        self._gifi_code = None
        self._bank_account_details = None
        self._main_address = None
        self._main_contact_person = None
        self._journal_code = None
        self.discriminator = None
        self.bank_account_type_id = bank_account_type_id
        if ledger_account_id is not None:
            self.ledger_account_id = ledger_account_id
        if nominal_code is not None:
            self.nominal_code = nominal_code
        if default_payment_method_id is not None:
            self.default_payment_method_id = default_payment_method_id
        if gifi_code is not None:
            self.gifi_code = gifi_code
        if bank_account_details is not None:
            self.bank_account_details = bank_account_details
        if main_address is not None:
            self.main_address = main_address
        if main_contact_person is not None:
            self.main_contact_person = main_contact_person
        if journal_code is not None:
            self.journal_code = journal_code

    @property
    def bank_account_type_id(self):
        return self._bank_account_type_id

    @bank_account_type_id.setter
    def bank_account_type_id(self, bank_account_type_id):
        if (
            self.local_vars_configuration.client_side_validation
            and bank_account_type_id is None
        ):
            raise ValueError(
                "Invalid value for `bank_account_type_id`, must not be `None`"
            )
        self._bank_account_type_id = bank_account_type_id

    @property
    def ledger_account_id(self):
        return self._ledger_account_id

    @ledger_account_id.setter
    def ledger_account_id(self, ledger_account_id):
        self._ledger_account_id = ledger_account_id

    @property
    def nominal_code(self):
        return self._nominal_code

    @nominal_code.setter
    def nominal_code(self, nominal_code):
        if (
            self.local_vars_configuration.client_side_validation
            and nominal_code is not None
            and nominal_code > 99999999
        ):
            raise ValueError(
                "Invalid value for `nominal_code`, must be a value less than or equal to `99999999`"
            )
        if (
            self.local_vars_configuration.client_side_validation
            and nominal_code is not None
            and nominal_code < 1
        ):
            raise ValueError(
                "Invalid value for `nominal_code`, must be a value greater than or equal to `1`"
            )
        self._nominal_code = nominal_code

    @property
    def default_payment_method_id(self):
        return self._default_payment_method_id

    @default_payment_method_id.setter
    def default_payment_method_id(self, default_payment_method_id):
        self._default_payment_method_id = default_payment_method_id

    @property
    def gifi_code(self):
        return self._gifi_code

    @gifi_code.setter
    def gifi_code(self, gifi_code):
        if (
            self.local_vars_configuration.client_side_validation
            and gifi_code is not None
            and gifi_code > 9999
        ):
            raise ValueError(
                "Invalid value for `gifi_code`, must be a value less than or equal to `9999`"
            )
        if (
            self.local_vars_configuration.client_side_validation
            and gifi_code is not None
            and gifi_code < 1000
        ):
            raise ValueError(
                "Invalid value for `gifi_code`, must be a value greater than or equal to `1000`"
            )
        self._gifi_code = gifi_code

    @property
    def bank_account_details(self):
        return self._bank_account_details

    @bank_account_details.setter
    def bank_account_details(self, bank_account_details):
        self._bank_account_details = bank_account_details

    @property
    def main_address(self):
        return self._main_address

    @main_address.setter
    def main_address(self, main_address):
        self._main_address = main_address

    @property
    def main_contact_person(self):
        return self._main_contact_person

    @main_contact_person.setter
    def main_contact_person(self, main_contact_person):
        self._main_contact_person = main_contact_person

    @property
    def journal_code(self):
        return self._journal_code

    @journal_code.setter
    def journal_code(self, journal_code):
        self._journal_code = journal_code

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
        if not isinstance(other, PostBankAccountsBankAccount):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PostBankAccountsBankAccount):
            return True
        return self.to_dict() != other.to_dict()
