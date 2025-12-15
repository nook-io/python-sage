import pprint
import six
from sage.configuration import Configuration


class Migration(object):
    openapi_types = {
        "id": "str",
        "path": "str",
        "status": "MigrationStatus",
        "started_at": "datetime",
        "completed_at": "datetime",
        "source_product": "str",
        "source_product_version": "str",
        "source_license": "str",
        "source_tool": "str",
        "source_tool_version": "str",
        "schema_id": "str",
    }
    attribute_map = {
        "id": "id",
        "path": "$path",
        "status": "status",
        "started_at": "started_at",
        "completed_at": "completed_at",
        "source_product": "source_product",
        "source_product_version": "source_product_version",
        "source_license": "source_license",
        "source_tool": "source_tool",
        "source_tool_version": "source_tool_version",
        "schema_id": "schema_id",
    }

    def __init__(
        self,
        id=None,
        path=None,
        status=None,
        started_at=None,
        completed_at=None,
        source_product=None,
        source_product_version=None,
        source_license=None,
        source_tool=None,
        source_tool_version=None,
        schema_id=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._id = None
        self._path = None
        self._status = None
        self._started_at = None
        self._completed_at = None
        self._source_product = None
        self._source_product_version = None
        self._source_license = None
        self._source_tool = None
        self._source_tool_version = None
        self._schema_id = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if path is not None:
            self.path = path
        if status is not None:
            self.status = status
        if started_at is not None:
            self.started_at = started_at
        if completed_at is not None:
            self.completed_at = completed_at
        if source_product is not None:
            self.source_product = source_product
        if source_product_version is not None:
            self.source_product_version = source_product_version
        if source_license is not None:
            self.source_license = source_license
        if source_tool is not None:
            self.source_tool = source_tool
        if source_tool_version is not None:
            self.source_tool_version = source_tool_version
        if schema_id is not None:
            self.schema_id = schema_id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        if (
            self.local_vars_configuration.client_side_validation
            and id is not None
            and len(id) > 32
        ):
            raise ValueError(
                "Invalid value for `id`, length must be less than or equal to `32`"
            )
        self._id = id

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path):
        self._path = path

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def started_at(self):
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        self._started_at = started_at

    @property
    def completed_at(self):
        return self._completed_at

    @completed_at.setter
    def completed_at(self, completed_at):
        self._completed_at = completed_at

    @property
    def source_product(self):
        return self._source_product

    @source_product.setter
    def source_product(self, source_product):
        if (
            self.local_vars_configuration.client_side_validation
            and source_product is not None
            and len(source_product) > 50
        ):
            raise ValueError(
                "Invalid value for `source_product`, length must be less than or equal to `50`"
            )
        self._source_product = source_product

    @property
    def source_product_version(self):
        return self._source_product_version

    @source_product_version.setter
    def source_product_version(self, source_product_version):
        if (
            self.local_vars_configuration.client_side_validation
            and source_product_version is not None
            and len(source_product_version) > 50
        ):
            raise ValueError(
                "Invalid value for `source_product_version`, length must be less than or equal to `50`"
            )
        self._source_product_version = source_product_version

    @property
    def source_license(self):
        return self._source_license

    @source_license.setter
    def source_license(self, source_license):
        if (
            self.local_vars_configuration.client_side_validation
            and source_license is not None
            and len(source_license) > 50
        ):
            raise ValueError(
                "Invalid value for `source_license`, length must be less than or equal to `50`"
            )
        self._source_license = source_license

    @property
    def source_tool(self):
        return self._source_tool

    @source_tool.setter
    def source_tool(self, source_tool):
        if (
            self.local_vars_configuration.client_side_validation
            and source_tool is not None
            and len(source_tool) > 50
        ):
            raise ValueError(
                "Invalid value for `source_tool`, length must be less than or equal to `50`"
            )
        self._source_tool = source_tool

    @property
    def source_tool_version(self):
        return self._source_tool_version

    @source_tool_version.setter
    def source_tool_version(self, source_tool_version):
        if (
            self.local_vars_configuration.client_side_validation
            and source_tool_version is not None
            and len(source_tool_version) > 50
        ):
            raise ValueError(
                "Invalid value for `source_tool_version`, length must be less than or equal to `50`"
            )
        self._source_tool_version = source_tool_version

    @property
    def schema_id(self):
        return self._schema_id

    @schema_id.setter
    def schema_id(self, schema_id):
        if (
            self.local_vars_configuration.client_side_validation
            and schema_id is not None
            and len(schema_id) > 100
        ):
            raise ValueError(
                "Invalid value for `schema_id`, length must be less than or equal to `100`"
            )
        self._schema_id = schema_id

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
        if not isinstance(other, Migration):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, Migration):
            return True
        return self.to_dict() != other.to_dict()
