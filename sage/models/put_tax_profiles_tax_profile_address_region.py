import pprint
import six
from sage.configuration import Configuration


class PutTaxProfilesTaxProfileAddressRegion(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {"name": "str", "code": "str"}
    attribute_map = {"name": "name", "code": "code"}

    def __init__(self, name=None, code=None, local_vars_configuration=None):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._name = None
        self._code = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if code is not None:
            self.code = code

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        self._code = code

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
        if not isinstance(other, PutTaxProfilesTaxProfileAddressRegion):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PutTaxProfilesTaxProfileAddressRegion):
            return True
        return self.to_dict() != other.to_dict()
