import pprint
import six
from sage.configuration import Configuration


class DefaultMessages(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {"message_type": "str", "locale": "str", "message": "str"}
    attribute_map = {
        "message_type": "message_type",
        "locale": "locale",
        "message": "message",
    }

    def __init__(
        self,
        message_type=None,
        locale=None,
        message=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._message_type = None
        self._locale = None
        self._message = None
        self.discriminator = None
        if message_type is not None:
            self.message_type = message_type
        if locale is not None:
            self.locale = locale
        if message is not None:
            self.message = message

    @property
    def message_type(self):
        return self._message_type

    @message_type.setter
    def message_type(self, message_type):
        self._message_type = message_type

    @property
    def locale(self):
        return self._locale

    @locale.setter
    def locale(self, locale):
        self._locale = locale

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, message):
        self._message = message

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
        if not isinstance(other, DefaultMessages):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, DefaultMessages):
            return True
        return self.to_dict() != other.to_dict()
