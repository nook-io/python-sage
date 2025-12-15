import pprint
import six
from sage.configuration import Configuration


class PostContactPersonsContactPerson(object):
    openapi_types = {
        "address_id": "str",
        "name": "str",
        "contact_person_type_ids": "list[str]",
        "job_title": "str",
        "telephone": "str",
        "mobile": "str",
        "email": "str",
        "fax": "str",
        "is_main_contact": "bool",
        "is_preferred_contact": "bool",
    }
    attribute_map = {
        "address_id": "address_id",
        "name": "name",
        "contact_person_type_ids": "contact_person_type_ids",
        "job_title": "job_title",
        "telephone": "telephone",
        "mobile": "mobile",
        "email": "email",
        "fax": "fax",
        "is_main_contact": "is_main_contact",
        "is_preferred_contact": "is_preferred_contact",
    }

    def __init__(
        self,
        address_id=None,
        name=None,
        contact_person_type_ids=None,
        job_title=None,
        telephone=None,
        mobile=None,
        email=None,
        fax=None,
        is_main_contact=None,
        is_preferred_contact=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._address_id = None
        self._name = None
        self._contact_person_type_ids = None
        self._job_title = None
        self._telephone = None
        self._mobile = None
        self._email = None
        self._fax = None
        self._is_main_contact = None
        self._is_preferred_contact = None
        self.discriminator = None
        self.address_id = address_id
        self.name = name
        self.contact_person_type_ids = contact_person_type_ids
        if job_title is not None:
            self.job_title = job_title
        if telephone is not None:
            self.telephone = telephone
        if mobile is not None:
            self.mobile = mobile
        if email is not None:
            self.email = email
        if fax is not None:
            self.fax = fax
        if is_main_contact is not None:
            self.is_main_contact = is_main_contact
        if is_preferred_contact is not None:
            self.is_preferred_contact = is_preferred_contact

    @property
    def address_id(self):
        return self._address_id

    @address_id.setter
    def address_id(self, address_id):
        if self.local_vars_configuration.client_side_validation and address_id is None:
            raise ValueError("Invalid value for `address_id`, must not be `None`")
        self._address_id = address_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if self.local_vars_configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        self._name = name

    @property
    def contact_person_type_ids(self):
        return self._contact_person_type_ids

    @contact_person_type_ids.setter
    def contact_person_type_ids(self, contact_person_type_ids):
        if (
            self.local_vars_configuration.client_side_validation
            and contact_person_type_ids is None
        ):
            raise ValueError(
                "Invalid value for `contact_person_type_ids`, must not be `None`"
            )
        self._contact_person_type_ids = contact_person_type_ids

    @property
    def job_title(self):
        return self._job_title

    @job_title.setter
    def job_title(self, job_title):
        self._job_title = job_title

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
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def fax(self):
        return self._fax

    @fax.setter
    def fax(self, fax):
        self._fax = fax

    @property
    def is_main_contact(self):
        return self._is_main_contact

    @is_main_contact.setter
    def is_main_contact(self, is_main_contact):
        self._is_main_contact = is_main_contact

    @property
    def is_preferred_contact(self):
        return self._is_preferred_contact

    @is_preferred_contact.setter
    def is_preferred_contact(self, is_preferred_contact):
        self._is_preferred_contact = is_preferred_contact

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
        if not isinstance(other, PostContactPersonsContactPerson):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PostContactPersonsContactPerson):
            return True
        return self.to_dict() != other.to_dict()
