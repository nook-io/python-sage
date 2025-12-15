import pprint
import six
from sage.configuration import Configuration


class PutBusinessSettingsBusinessSettings(object):
    openapi_types = {
        "siret": "str",
        "management_centre_member": "bool",
        "rcs_number": "str",
        "share_capital": "float",
        "business_activity_type_id": "str",
        "legal_form_type_id": "str",
        "auxiliary_accounts_visible": "bool",
        "business_type_id": "str",
        "country_of_registration_id": "str",
        "default_ledger_accounts": "PutBusinessSettingsBusinessSettingsDefaultLedgerAccounts",
    }
    attribute_map = {
        "siret": "siret",
        "management_centre_member": "management_centre_member",
        "rcs_number": "rcs_number",
        "share_capital": "share_capital",
        "business_activity_type_id": "business_activity_type_id",
        "legal_form_type_id": "legal_form_type_id",
        "auxiliary_accounts_visible": "auxiliary_accounts_visible",
        "business_type_id": "business_type_id",
        "country_of_registration_id": "country_of_registration_id",
        "default_ledger_accounts": "default_ledger_accounts",
    }

    def __init__(
        self,
        siret=None,
        management_centre_member=None,
        rcs_number=None,
        share_capital=None,
        business_activity_type_id=None,
        legal_form_type_id=None,
        auxiliary_accounts_visible=None,
        business_type_id=None,
        country_of_registration_id=None,
        default_ledger_accounts=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._siret = None
        self._management_centre_member = None
        self._rcs_number = None
        self._share_capital = None
        self._business_activity_type_id = None
        self._legal_form_type_id = None
        self._auxiliary_accounts_visible = None
        self._business_type_id = None
        self._country_of_registration_id = None
        self._default_ledger_accounts = None
        self.discriminator = None
        if siret is not None:
            self.siret = siret
        if management_centre_member is not None:
            self.management_centre_member = management_centre_member
        if rcs_number is not None:
            self.rcs_number = rcs_number
        if share_capital is not None:
            self.share_capital = share_capital
        if business_activity_type_id is not None:
            self.business_activity_type_id = business_activity_type_id
        if legal_form_type_id is not None:
            self.legal_form_type_id = legal_form_type_id
        if auxiliary_accounts_visible is not None:
            self.auxiliary_accounts_visible = auxiliary_accounts_visible
        if business_type_id is not None:
            self.business_type_id = business_type_id
        if country_of_registration_id is not None:
            self.country_of_registration_id = country_of_registration_id
        if default_ledger_accounts is not None:
            self.default_ledger_accounts = default_ledger_accounts

    @property
    def siret(self):
        return self._siret

    @siret.setter
    def siret(self, siret):
        self._siret = siret

    @property
    def management_centre_member(self):
        return self._management_centre_member

    @management_centre_member.setter
    def management_centre_member(self, management_centre_member):
        self._management_centre_member = management_centre_member

    @property
    def rcs_number(self):
        return self._rcs_number

    @rcs_number.setter
    def rcs_number(self, rcs_number):
        self._rcs_number = rcs_number

    @property
    def share_capital(self):
        return self._share_capital

    @share_capital.setter
    def share_capital(self, share_capital):
        self._share_capital = share_capital

    @property
    def business_activity_type_id(self):
        return self._business_activity_type_id

    @business_activity_type_id.setter
    def business_activity_type_id(self, business_activity_type_id):
        self._business_activity_type_id = business_activity_type_id

    @property
    def legal_form_type_id(self):
        return self._legal_form_type_id

    @legal_form_type_id.setter
    def legal_form_type_id(self, legal_form_type_id):
        self._legal_form_type_id = legal_form_type_id

    @property
    def auxiliary_accounts_visible(self):
        return self._auxiliary_accounts_visible

    @auxiliary_accounts_visible.setter
    def auxiliary_accounts_visible(self, auxiliary_accounts_visible):
        self._auxiliary_accounts_visible = auxiliary_accounts_visible

    @property
    def business_type_id(self):
        return self._business_type_id

    @business_type_id.setter
    def business_type_id(self, business_type_id):
        self._business_type_id = business_type_id

    @property
    def country_of_registration_id(self):
        return self._country_of_registration_id

    @country_of_registration_id.setter
    def country_of_registration_id(self, country_of_registration_id):
        self._country_of_registration_id = country_of_registration_id

    @property
    def default_ledger_accounts(self):
        return self._default_ledger_accounts

    @default_ledger_accounts.setter
    def default_ledger_accounts(self, default_ledger_accounts):
        self._default_ledger_accounts = default_ledger_accounts

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
        if not isinstance(other, PutBusinessSettingsBusinessSettings):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PutBusinessSettingsBusinessSettings):
            return True
        return self.to_dict() != other.to_dict()
