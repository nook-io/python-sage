import pprint
import six
from sage.configuration import Configuration


class CoaAccount(object):
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
        "ledger_account_group": "CoaGroupType",
        "name": "str",
        "control_name": "str",
        "nominal_code": "int",
        "ledger_account_type": "Base",
        "ledger_account_classification": "Base",
        "tax_rate": "Base",
        "fixed_tax_rate": "bool",
        "cis_materials": "bool",
        "cis_labour": "bool",
    }
    attribute_map = {
        "id": "id",
        "displayed_as": "displayed_as",
        "path": "$path",
        "created_at": "created_at",
        "updated_at": "updated_at",
        "ledger_account_group": "ledger_account_group",
        "name": "name",
        "control_name": "control_name",
        "nominal_code": "nominal_code",
        "ledger_account_type": "ledger_account_type",
        "ledger_account_classification": "ledger_account_classification",
        "tax_rate": "tax_rate",
        "fixed_tax_rate": "fixed_tax_rate",
        "cis_materials": "cis_materials",
        "cis_labour": "cis_labour",
    }

    def __init__(
        self,
        id=None,
        displayed_as=None,
        path=None,
        created_at=None,
        updated_at=None,
        ledger_account_group=None,
        name=None,
        control_name=None,
        nominal_code=None,
        ledger_account_type=None,
        ledger_account_classification=None,
        tax_rate=None,
        fixed_tax_rate=None,
        cis_materials=None,
        cis_labour=None,
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
        self._ledger_account_group = None
        self._name = None
        self._control_name = None
        self._nominal_code = None
        self._ledger_account_type = None
        self._ledger_account_classification = None
        self._tax_rate = None
        self._fixed_tax_rate = None
        self._cis_materials = None
        self._cis_labour = None
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
        if ledger_account_group is not None:
            self.ledger_account_group = ledger_account_group
        if name is not None:
            self.name = name
        if control_name is not None:
            self.control_name = control_name
        if nominal_code is not None:
            self.nominal_code = nominal_code
        if ledger_account_type is not None:
            self.ledger_account_type = ledger_account_type
        if ledger_account_classification is not None:
            self.ledger_account_classification = ledger_account_classification
        if tax_rate is not None:
            self.tax_rate = tax_rate
        if fixed_tax_rate is not None:
            self.fixed_tax_rate = fixed_tax_rate
        if cis_materials is not None:
            self.cis_materials = cis_materials
        if cis_labour is not None:
            self.cis_labour = cis_labour

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
    def ledger_account_group(self):
        return self._ledger_account_group

    @ledger_account_group.setter
    def ledger_account_group(self, ledger_account_group):
        self._ledger_account_group = ledger_account_group

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if (
            self.local_vars_configuration.client_side_validation
            and name is not None
            and len(name) > 200
        ):
            raise ValueError(
                "Invalid value for `name`, length must be less than or equal to `200`"
            )
        self._name = name

    @property
    def control_name(self):
        return self._control_name

    @control_name.setter
    def control_name(self, control_name):
        if (
            self.local_vars_configuration.client_side_validation
            and control_name is not None
            and len(control_name) > 50
        ):
            raise ValueError(
                "Invalid value for `control_name`, length must be less than or equal to `50`"
            )
        self._control_name = control_name

    @property
    def nominal_code(self):
        return self._nominal_code

    @nominal_code.setter
    def nominal_code(self, nominal_code):
        self._nominal_code = nominal_code

    @property
    def ledger_account_type(self):
        return self._ledger_account_type

    @ledger_account_type.setter
    def ledger_account_type(self, ledger_account_type):
        self._ledger_account_type = ledger_account_type

    @property
    def ledger_account_classification(self):
        return self._ledger_account_classification

    @ledger_account_classification.setter
    def ledger_account_classification(self, ledger_account_classification):
        self._ledger_account_classification = ledger_account_classification

    @property
    def tax_rate(self):
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, tax_rate):
        self._tax_rate = tax_rate

    @property
    def fixed_tax_rate(self):
        return self._fixed_tax_rate

    @fixed_tax_rate.setter
    def fixed_tax_rate(self, fixed_tax_rate):
        self._fixed_tax_rate = fixed_tax_rate

    @property
    def cis_materials(self):
        return self._cis_materials

    @cis_materials.setter
    def cis_materials(self, cis_materials):
        self._cis_materials = cis_materials

    @property
    def cis_labour(self):
        return self._cis_labour

    @cis_labour.setter
    def cis_labour(self, cis_labour):
        self._cis_labour = cis_labour

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
        if not isinstance(other, CoaAccount):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, CoaAccount):
            return True
        return self.to_dict() != other.to_dict()
