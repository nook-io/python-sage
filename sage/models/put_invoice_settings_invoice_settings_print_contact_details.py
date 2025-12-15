import pprint
import six
from sage.configuration import Configuration


class PutInvoiceSettingsInvoiceSettingsPrintContactDetails(object):
    openapi_types = {
        "business_name": "bool",
        "website": "bool",
        "telephone": "bool",
        "mobile": "bool",
        "email_address": "bool",
        "due_date": "bool",
        "default_delivery_address": "str",
    }
    attribute_map = {
        "business_name": "business_name",
        "website": "website",
        "telephone": "telephone",
        "mobile": "mobile",
        "email_address": "email_address",
        "due_date": "due_date",
        "default_delivery_address": "default_delivery_address",
    }

    def __init__(
        self,
        business_name=None,
        website=None,
        telephone=None,
        mobile=None,
        email_address=None,
        due_date=None,
        default_delivery_address=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._business_name = None
        self._website = None
        self._telephone = None
        self._mobile = None
        self._email_address = None
        self._due_date = None
        self._default_delivery_address = None
        self.discriminator = None
        if business_name is not None:
            self.business_name = business_name
        if website is not None:
            self.website = website
        if telephone is not None:
            self.telephone = telephone
        if mobile is not None:
            self.mobile = mobile
        if email_address is not None:
            self.email_address = email_address
        if due_date is not None:
            self.due_date = due_date
        if default_delivery_address is not None:
            self.default_delivery_address = default_delivery_address

    @property
    def business_name(self):
        return self._business_name

    @business_name.setter
    def business_name(self, business_name):
        self._business_name = business_name

    @property
    def website(self):
        return self._website

    @website.setter
    def website(self, website):
        self._website = website

    @property
    def telephone(self):
        return self._telephone

    @telephone.setter
    def telephone(self, telephone):
        self._telephone = telephone

    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        self._mobile = mobile

    @property
    def email_address(self):
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        self._email_address = email_address

    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        self._due_date = due_date

    @property
    def default_delivery_address(self):
        return self._default_delivery_address

    @default_delivery_address.setter
    def default_delivery_address(self, default_delivery_address):
        self._default_delivery_address = default_delivery_address

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
        if not isinstance(other, PutInvoiceSettingsInvoiceSettingsPrintContactDetails):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PutInvoiceSettingsInvoiceSettingsPrintContactDetails):
            return True
        return self.to_dict() != other.to_dict()
