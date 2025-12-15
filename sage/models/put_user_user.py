import pprint
import six
from sage.configuration import Configuration


class PutUserUser(object):
    openapi_types = {
        "first_name": "str",
        "last_name": "str",
        "initials": "str",
        "locale": "str",
    }
    attribute_map = {
        "first_name": "first_name",
        "last_name": "last_name",
        "initials": "initials",
        "locale": "locale",
    }

    def __init__(
        self,
        first_name=None,
        last_name=None,
        initials=None,
        locale=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._first_name = None
        self._last_name = None
        self._initials = None
        self._locale = None
        self.discriminator = None
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if initials is not None:
            self.initials = initials
        if locale is not None:
            self.locale = locale

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def initials(self):
        return self._initials

    @initials.setter
    def initials(self, initials):
        self._initials = initials

    @property
    def locale(self):
        return self._locale

    @locale.setter
    def locale(self, locale):
        allowed_values = [
            "en-GB",
            "en-IE",
            "en-US",
            "es-US",
            "en-CA",
            "fr-CA",
            "fr-FR",
            "de-DE",
            "es-ES",
        ]
        if (
            self.local_vars_configuration.client_side_validation
            and locale not in allowed_values
        ):
            raise ValueError(
                "Invalid value for `locale` ({0}), must be one of {1}".format(
                    locale, allowed_values
                )
            )
        self._locale = locale

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
        if not isinstance(other, PutUserUser):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PutUserUser):
            return True
        return self.to_dict() != other.to_dict()
