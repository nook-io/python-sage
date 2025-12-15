import pprint
import six
from sage.configuration import Configuration


class ComponentTaxRate(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        "id": "str",
        "displayed_as": "str",
        "path": "str",
        "created_at": "datetime",
        "updated_at": "datetime",
        "name": "str",
        "agency": "str",
        "percentage": "float",
        "percentages": "list[TaxRatePercentage]",
        "is_visible": "bool",
        "retailer": "bool",
        "editable": "bool",
        "deletable": "bool",
        "is_combined_rate": "bool",
    }
    attribute_map = {
        "id": "id",
        "displayed_as": "displayed_as",
        "path": "$path",
        "created_at": "created_at",
        "updated_at": "updated_at",
        "name": "name",
        "agency": "agency",
        "percentage": "percentage",
        "percentages": "percentages",
        "is_visible": "is_visible",
        "retailer": "retailer",
        "editable": "editable",
        "deletable": "deletable",
        "is_combined_rate": "is_combined_rate",
    }

    def __init__(
        self,
        id=None,
        displayed_as=None,
        path=None,
        created_at=None,
        updated_at=None,
        name=None,
        agency=None,
        percentage=None,
        percentages=None,
        is_visible=None,
        retailer=None,
        editable=None,
        deletable=None,
        is_combined_rate=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._id = None
        self._displayed_as = None
        self._path = None
        self._created_at = None
        self._updated_at = None
        self._name = None
        self._agency = None
        self._percentage = None
        self._percentages = None
        self._is_visible = None
        self._retailer = None
        self._editable = None
        self._deletable = None
        self._is_combined_rate = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if displayed_as is not None:
            self.displayed_as = displayed_as
        if path is not None:
            self.path = path
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if name is not None:
            self.name = name
        if agency is not None:
            self.agency = agency
        if percentage is not None:
            self.percentage = percentage
        if percentages is not None:
            self.percentages = percentages
        if is_visible is not None:
            self.is_visible = is_visible
        if retailer is not None:
            self.retailer = retailer
        if editable is not None:
            self.editable = editable
        if deletable is not None:
            self.deletable = deletable
        if is_combined_rate is not None:
            self.is_combined_rate = is_combined_rate

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
    def created_at(self):
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        self._created_at = created_at

    @property
    def updated_at(self):
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        self._updated_at = updated_at

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def agency(self):
        return self._agency

    @agency.setter
    def agency(self, agency):
        self._agency = agency

    @property
    def percentage(self):
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        self._percentage = percentage

    @property
    def percentages(self):
        return self._percentages

    @percentages.setter
    def percentages(self, percentages):
        self._percentages = percentages

    @property
    def is_visible(self):
        return self._is_visible

    @is_visible.setter
    def is_visible(self, is_visible):
        self._is_visible = is_visible

    @property
    def retailer(self):
        return self._retailer

    @retailer.setter
    def retailer(self, retailer):
        self._retailer = retailer

    @property
    def editable(self):
        return self._editable

    @editable.setter
    def editable(self, editable):
        self._editable = editable

    @property
    def deletable(self):
        return self._deletable

    @deletable.setter
    def deletable(self, deletable):
        self._deletable = deletable

    @property
    def is_combined_rate(self):
        return self._is_combined_rate

    @is_combined_rate.setter
    def is_combined_rate(self, is_combined_rate):
        self._is_combined_rate = is_combined_rate

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
        if not isinstance(other, ComponentTaxRate):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, ComponentTaxRate):
            return True
        return self.to_dict() != other.to_dict()
