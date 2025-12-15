import pprint
import six
from sage.configuration import Configuration


class PutMigrationsMigrations(object):
    openapi_types = {
        "status_id": "str",
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
        "status_id": "status_id",
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
        status_id=None,
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
        self._status_id = None
        self._started_at = None
        self._completed_at = None
        self._source_product = None
        self._source_product_version = None
        self._source_license = None
        self._source_tool = None
        self._source_tool_version = None
        self._schema_id = None
        self.discriminator = None
        if status_id is not None:
            self.status_id = status_id
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
    def status_id(self):
        return self._status_id

    @status_id.setter
    def status_id(self, status_id):
        self._status_id = status_id

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
        self._source_product = source_product

    @property
    def source_product_version(self):
        return self._source_product_version

    @source_product_version.setter
    def source_product_version(self, source_product_version):
        self._source_product_version = source_product_version

    @property
    def source_license(self):
        return self._source_license

    @source_license.setter
    def source_license(self, source_license):
        self._source_license = source_license

    @property
    def source_tool(self):
        return self._source_tool

    @source_tool.setter
    def source_tool(self, source_tool):
        self._source_tool = source_tool

    @property
    def source_tool_version(self):
        return self._source_tool_version

    @source_tool_version.setter
    def source_tool_version(self, source_tool_version):
        self._source_tool_version = source_tool_version

    @property
    def schema_id(self):
        return self._schema_id

    @schema_id.setter
    def schema_id(self, schema_id):
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
        if not isinstance(other, PutMigrationsMigrations):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PutMigrationsMigrations):
            return True
        return self.to_dict() != other.to_dict()
