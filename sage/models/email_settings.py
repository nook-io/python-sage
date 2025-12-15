import pprint
import six
from sage.configuration import Configuration


class EmailSettings(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        "default_messages": "list[DefaultMessages]",
        "pdf_attached": "bool",
        "send_bcc": "bool",
        "updated_at": "datetime",
    }
    attribute_map = {
        "default_messages": "default_messages",
        "pdf_attached": "pdf_attached",
        "send_bcc": "send_bcc",
        "updated_at": "updated_at",
    }

    def __init__(
        self,
        default_messages=None,
        pdf_attached=None,
        send_bcc=None,
        updated_at=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._default_messages = None
        self._pdf_attached = None
        self._send_bcc = None
        self._updated_at = None
        self.discriminator = None
        if default_messages is not None:
            self.default_messages = default_messages
        if pdf_attached is not None:
            self.pdf_attached = pdf_attached
        if send_bcc is not None:
            self.send_bcc = send_bcc
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def default_messages(self):
        return self._default_messages

    @default_messages.setter
    def default_messages(self, default_messages):
        self._default_messages = default_messages

    @property
    def pdf_attached(self):
        return self._pdf_attached

    @pdf_attached.setter
    def pdf_attached(self, pdf_attached):
        self._pdf_attached = pdf_attached

    @property
    def send_bcc(self):
        return self._send_bcc

    @send_bcc.setter
    def send_bcc(self, send_bcc):
        self._send_bcc = send_bcc

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
        if not isinstance(other, EmailSettings):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, EmailSettings):
            return True
        return self.to_dict() != other.to_dict()
