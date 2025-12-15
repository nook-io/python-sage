import pprint
import six
from sage.configuration import Configuration


class HostedArtefactPaymentSetting(object):
    openapi_types = {
        "id": "str",
        "displayed_as": "str",
        "path": "str",
        "object_guid": "str",
        "disable_payment": "bool",
    }
    attribute_map = {
        "id": "id",
        "displayed_as": "displayed_as",
        "path": "$path",
        "object_guid": "object_guid",
        "disable_payment": "disable_payment",
    }

    def __init__(
        self,
        id=None,
        displayed_as=None,
        path=None,
        object_guid=None,
        disable_payment=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._id = None
        self._displayed_as = None
        self._path = None
        self._object_guid = None
        self._disable_payment = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if displayed_as is not None:
            self.displayed_as = displayed_as
        if path is not None:
            self.path = path
        if object_guid is not None:
            self.object_guid = object_guid
        if disable_payment is not None:
            self.disable_payment = disable_payment

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
    def object_guid(self):
        return self._object_guid

    @object_guid.setter
    def object_guid(self, object_guid):
        if (
            self.local_vars_configuration.client_side_validation
            and object_guid is not None
            and len(object_guid) > 32
        ):
            raise ValueError(
                "Invalid value for `object_guid`, length must be less than or equal to `32`"
            )
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
        if not isinstance(other, HostedArtefactPaymentSetting):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, HostedArtefactPaymentSetting):
            return True
        return self.to_dict() != other.to_dict()
