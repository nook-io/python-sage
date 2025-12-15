import pprint
import six
from sage.configuration import Configuration


class AllocatedArtefact(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {"id": "str", "artefact": "Generic", "amount": "float"}
    attribute_map = {"id": "id", "artefact": "artefact", "amount": "amount"}

    def __init__(
        self, id=None, artefact=None, amount=None, local_vars_configuration=None
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._id = None
        self._artefact = None
        self._amount = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if artefact is not None:
            self.artefact = artefact
        if amount is not None:
            self.amount = amount

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def artefact(self):
        return self._artefact

    @artefact.setter
    def artefact(self, artefact):
        self._artefact = artefact

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

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
        if not isinstance(other, AllocatedArtefact):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, AllocatedArtefact):
            return True
        return self.to_dict() != other.to_dict()
