import pprint
import six
from sage.configuration import Configuration


class BankAccountContact(object):
    openapi_types = {
        "name": "str",
        "job_title": "str",
        "telephone": "str",
        "mobile": "str",
        "email": "str",
        "fax": "str",
    }
    attribute_map = {
        "name": "name",
        "job_title": "job_title",
        "telephone": "telephone",
        "mobile": "mobile",
        "email": "email",
        "fax": "fax",
    }

    def __init__(
        self,
        name=None,
        job_title=None,
        telephone=None,
        mobile=None,
        email=None,
        fax=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._name = None
        self._job_title = None
        self._telephone = None
        self._mobile = None
        self._email = None
        self._fax = None
        self.discriminator = None
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

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

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
        if not isinstance(other, BankAccountContact):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, BankAccountContact):
            return True
        return self.to_dict() != other.to_dict()
