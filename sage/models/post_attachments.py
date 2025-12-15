import pprint
import six
from sage.configuration import Configuration


class PostAttachments(object):
    openapi_types = {"attachment": "PostAttachmentsAttachment"}
    attribute_map = {"attachment": "attachment"}

    def __init__(self, attachment=None, local_vars_configuration=None):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._attachment = None
        self.discriminator = None
        self.attachment = attachment

    @property
    def attachment(self):
        return self._attachment

    @attachment.setter
    def attachment(self, attachment):
        if self.local_vars_configuration.client_side_validation and attachment is None:
            raise ValueError("Invalid value for `attachment`, must not be `None`")
        self._attachment = attachment

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
        if not isinstance(other, PostAttachments):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PostAttachments):
            return True
        return self.to_dict() != other.to_dict()
