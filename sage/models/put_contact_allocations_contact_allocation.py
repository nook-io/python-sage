import pprint
import six
from sage.configuration import Configuration


class PutContactAllocationsContactAllocation(object):
    openapi_types = {
        "transaction_type_id": "str",
        "contact_id": "str",
        "date": "date",
        "allocated_artefacts": "list[PostContactAllocationsContactAllocationAllocatedArtefacts]",
    }
    attribute_map = {
        "transaction_type_id": "transaction_type_id",
        "contact_id": "contact_id",
        "date": "date",
        "allocated_artefacts": "allocated_artefacts",
    }

    def __init__(
        self,
        transaction_type_id=None,
        contact_id=None,
        date=None,
        allocated_artefacts=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._transaction_type_id = None
        self._contact_id = None
        self._date = None
        self._allocated_artefacts = None
        self.discriminator = None
        if transaction_type_id is not None:
            self.transaction_type_id = transaction_type_id
        if contact_id is not None:
            self.contact_id = contact_id
        if date is not None:
            self.date = date
        if allocated_artefacts is not None:
            self.allocated_artefacts = allocated_artefacts

    @property
    def transaction_type_id(self):
        return self._transaction_type_id

    @transaction_type_id.setter
    def transaction_type_id(self, transaction_type_id):
        self._transaction_type_id = transaction_type_id

    @property
    def contact_id(self):
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        self._contact_id = contact_id

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

    @property
    def allocated_artefacts(self):
        return self._allocated_artefacts

    @allocated_artefacts.setter
    def allocated_artefacts(self, allocated_artefacts):
        self._allocated_artefacts = allocated_artefacts

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
        if not isinstance(other, PutContactAllocationsContactAllocation):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PutContactAllocationsContactAllocation):
            return True
        return self.to_dict() != other.to_dict()
