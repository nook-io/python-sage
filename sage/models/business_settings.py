import pprint
import six
from sage.configuration import Configuration


class BusinessSettings(object):
    openapi_types = {
        "path": "str",
        "siret": "str",
        "management_centre_member": "bool",
        "rcs_number": "str",
        "share_capital": "float",
        "business_activity_type": "BusinessActivityType",
        "legal_form_type": "LegalFormType",
        "auxiliary_accounts_visible": "bool",
        "default_ledger_accounts": "DefaultLedgerAccounts",
        "business_type": "BusinessType",
        "country_of_registration": "Base",
        "business_created_at": "datetime",
        "updated_at": "datetime",
    }
    attribute_map = {
        "path": "$path",
        "siret": "siret",
        "management_centre_member": "management_centre_member",
        "rcs_number": "rcs_number",
        "share_capital": "share_capital",
        "business_activity_type": "business_activity_type",
        "legal_form_type": "legal_form_type",
        "auxiliary_accounts_visible": "auxiliary_accounts_visible",
        "default_ledger_accounts": "default_ledger_accounts",
        "business_type": "business_type",
        "country_of_registration": "country_of_registration",
        "business_created_at": "business_created_at",
        "updated_at": "updated_at",
    }

    def __init__(
        self,
        path=None,
        siret=None,
        management_centre_member=None,
        rcs_number=None,
        share_capital=None,
        business_activity_type=None,
        legal_form_type=None,
        auxiliary_accounts_visible=None,
        default_ledger_accounts=None,
        business_type=None,
        country_of_registration=None,
        business_created_at=None,
        updated_at=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._path = None
        self._siret = None
        self._management_centre_member = None
        self._rcs_number = None
        self._share_capital = None
        self._business_activity_type = None
        self._legal_form_type = None
        self._auxiliary_accounts_visible = None
        self._default_ledger_accounts = None
        self._business_type = None
        self._country_of_registration = None
        self._business_created_at = None
        self._updated_at = None
        self.discriminator = None
        if path is not None:
            self.path = path
        if siret is not None:
            self.siret = siret
        if management_centre_member is not None:
            self.management_centre_member = management_centre_member
        if rcs_number is not None:
            self.rcs_number = rcs_number
        if share_capital is not None:
            self.share_capital = share_capital
        if business_activity_type is not None:
            self.business_activity_type = business_activity_type
        if legal_form_type is not None:
            self.legal_form_type = legal_form_type
        if auxiliary_accounts_visible is not None:
            self.auxiliary_accounts_visible = auxiliary_accounts_visible
        if default_ledger_accounts is not None:
            self.default_ledger_accounts = default_ledger_accounts
        if business_type is not None:
            self.business_type = business_type
        if country_of_registration is not None:
            self.country_of_registration = country_of_registration
        if business_created_at is not None:
            self.business_created_at = business_created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path):
        self._path = path

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
    def business_activity_type(self):
        return self._business_activity_type

    @business_activity_type.setter
    def business_activity_type(self, business_activity_type):
        self._business_activity_type = business_activity_type

    @property
    def legal_form_type(self):
        return self._legal_form_type

    @legal_form_type.setter
    def legal_form_type(self, legal_form_type):
        self._legal_form_type = legal_form_type

    @property
    def auxiliary_accounts_visible(self):
        return self._auxiliary_accounts_visible

    @auxiliary_accounts_visible.setter
    def auxiliary_accounts_visible(self, auxiliary_accounts_visible):
        self._auxiliary_accounts_visible = auxiliary_accounts_visible

    @property
    def default_ledger_accounts(self):
        return self._default_ledger_accounts

    @default_ledger_accounts.setter
    def default_ledger_accounts(self, default_ledger_accounts):
        self._default_ledger_accounts = default_ledger_accounts

    @property
    def business_type(self):
        return self._business_type

    @business_type.setter
    def business_type(self, business_type):
        self._business_type = business_type

    @property
    def country_of_registration(self):
        return self._country_of_registration

    @country_of_registration.setter
    def country_of_registration(self, country_of_registration):
        self._country_of_registration = country_of_registration

    @property
    def business_created_at(self):
        return self._business_created_at

    @business_created_at.setter
    def business_created_at(self, business_created_at):
        self._business_created_at = business_created_at

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
        if not isinstance(other, BusinessSettings):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, BusinessSettings):
            return True
        return self.to_dict() != other.to_dict()
