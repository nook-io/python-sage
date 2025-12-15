import pprint
import six
from sage.configuration import Configuration


class PostContactPaymentsContactPaymentAllocatedArtefacts(object):
    openapi_types = {"artefact_id": "str", "amount": "float", "discount": "float"}
    attribute_map = {
        "artefact_id": "artefact_id",
        "amount": "amount",
        "discount": "discount",
    }

    def __init__(
        self,
        artefact_id=None,
        amount=None,
        discount=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._artefact_id = None
        self._amount = None
        self._discount = None
        self.discriminator = None
        if artefact_id is not None:
            self.artefact_id = artefact_id
        if amount is not None:
            self.amount = amount
        if discount is not None:
            self.discount = discount

    @property
    def artefact_id(self):
        return self._artefact_id

    @artefact_id.setter
    def artefact_id(self, artefact_id):
        self._artefact_id = artefact_id

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount):
        self._discount = discount

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
        if not isinstance(other, PostContactPaymentsContactPaymentAllocatedArtefacts):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PostContactPaymentsContactPaymentAllocatedArtefacts):
            return True
        return self.to_dict() != other.to_dict()
