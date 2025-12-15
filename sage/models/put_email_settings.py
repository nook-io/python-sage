import pprint
import six
from sage.configuration import Configuration


class PutEmailSettings(object):
    openapi_types = {"email_settings": "PutEmailSettingsEmailSettings"}
    attribute_map = {"email_settings": "email_settings"}

    def __init__(self, email_settings=None, local_vars_configuration=None):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._email_settings = None
        self.discriminator = None
        self.email_settings = email_settings

    @property
    def email_settings(self):
        return self._email_settings

    @email_settings.setter
    def email_settings(self, email_settings):
        if (
            self.local_vars_configuration.client_side_validation
            and email_settings is None
        ):
            raise ValueError("Invalid value for `email_settings`, must not be `None`")
        self._email_settings = email_settings

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
        if not isinstance(other, PutEmailSettings):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PutEmailSettings):
            return True
        return self.to_dict() != other.to_dict()
