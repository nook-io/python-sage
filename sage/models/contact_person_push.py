import pprint
import six
from sage.configuration import Configuration


class ContactPersonPush(object):
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
        "deleted_at": "datetime",
        "contact_person_type_ids": "list[str]",
        "name": "str",
        "job_title": "str",
        "telephone": "str",
        "mobile": "str",
        "email": "str",
        "fax": "str",
        "is_main_contact": "bool",
        "address": "Base",
        "is_preferred_contact": "bool",
    }
    attribute_map = {
        "id": "id",
        "displayed_as": "displayed_as",
        "path": "$path",
        "created_at": "created_at",
        "updated_at": "updated_at",
        "deleted_at": "deleted_at",
        "contact_person_type_ids": "contact_person_type_ids",
        "name": "name",
        "job_title": "job_title",
        "telephone": "telephone",
        "mobile": "mobile",
        "email": "email",
        "fax": "fax",
        "is_main_contact": "is_main_contact",
        "address": "address",
        "is_preferred_contact": "is_preferred_contact",
    }

    def __init__(
        self,
        id=None,
        displayed_as=None,
        path=None,
        created_at=None,
        updated_at=None,
        deleted_at=None,
        contact_person_type_ids=None,
        name=None,
        job_title=None,
        telephone=None,
        mobile=None,
        email=None,
        fax=None,
        is_main_contact=None,
        address=None,
        is_preferred_contact=None,
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
        self._deleted_at = None
        self._contact_person_type_ids = None
        self._name = None
        self._job_title = None
        self._telephone = None
        self._mobile = None
        self._email = None
        self._fax = None
        self._is_main_contact = None
        self._address = None
        self._is_preferred_contact = None
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
        if deleted_at is not None:
            self.deleted_at = deleted_at
        if contact_person_type_ids is not None:
            self.contact_person_type_ids = contact_person_type_ids
        if name is not None:
            self.name = name
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
        if address is not None:
            self.address = address
        if is_preferred_contact is not None:
            self.is_preferred_contact = is_preferred_contact

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
    def deleted_at(self):
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        self._deleted_at = deleted_at

    @property
    def contact_person_type_ids(self):
        return self._contact_person_type_ids

    @contact_person_type_ids.setter
    def contact_person_type_ids(self, contact_person_type_ids):
        self._contact_person_type_ids = contact_person_type_ids

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if (
            self.local_vars_configuration.client_side_validation
            and name is not None
            and len(name) > 50
        ):
            raise ValueError(
                "Invalid value for `name`, length must be less than or equal to `50`"
            )
        self._name = name

    @property
    def job_title(self):
        return self._job_title

    @job_title.setter
    def job_title(self, job_title):
        if (
            self.local_vars_configuration.client_side_validation
            and job_title is not None
            and len(job_title) > 50
        ):
            raise ValueError(
                "Invalid value for `job_title`, length must be less than or equal to `50`"
            )
        self._job_title = job_title

    @property
    def telephone(self):
        return self._telephone

    @telephone.setter
    def telephone(self, telephone):
        if (
            self.local_vars_configuration.client_side_validation
            and telephone is not None
            and len(telephone) > 50
        ):
            raise ValueError(
                "Invalid value for `telephone`, length must be less than or equal to `50`"
            )
        self._telephone = telephone

    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        if (
            self.local_vars_configuration.client_side_validation
            and mobile is not None
            and len(mobile) > 50
        ):
            raise ValueError(
                "Invalid value for `mobile`, length must be less than or equal to `50`"
            )
        self._mobile = mobile

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
    def fax(self):
        return self._fax

    @fax.setter
    def fax(self, fax):
        if (
            self.local_vars_configuration.client_side_validation
            and fax is not None
            and len(fax) > 50
        ):
            raise ValueError(
                "Invalid value for `fax`, length must be less than or equal to `50`"
            )
        self._fax = fax

    @property
    def is_main_contact(self):
        return self._is_main_contact

    @is_main_contact.setter
    def is_main_contact(self, is_main_contact):
        self._is_main_contact = is_main_contact

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

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
        if not isinstance(other, ContactPerson):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, ContactPerson):
            return True
        return self.to_dict() != other.to_dict()
