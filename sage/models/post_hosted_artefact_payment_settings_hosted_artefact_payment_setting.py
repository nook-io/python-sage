import pprint
import six
from sage.configuration import Configuration


class PostHostedArtefactPaymentSettingsHostedArtefactPaymentSetting(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {"object_guid": "str", "disable_payment": "bool"}
    attribute_map = {"object_guid": "object_guid", "disable_payment": "disable_payment"}

    def __init__(
        self, object_guid=None, disable_payment=None, local_vars_configuration=None
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._object_guid = None
        self._disable_payment = None
        self.discriminator = None
        if object_guid is not None:
            self.object_guid = object_guid
        if disable_payment is not None:
            self.disable_payment = disable_payment

    @property
    def object_guid(self):
        return self._object_guid

    @object_guid.setter
    def object_guid(self, object_guid):
        self._object_guid = object_guid

    @property
    def disable_payment(self):
        return self._disable_payment

    @disable_payment.setter
    def disable_payment(self, disable_payment):
        self._disable_payment = disable_payment

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
        if not isinstance(
            other, PostHostedArtefactPaymentSettingsHostedArtefactPaymentSetting
        ):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(
            other, PostHostedArtefactPaymentSettingsHostedArtefactPaymentSetting
        ):
            return True
        return self.to_dict() != other.to_dict()
