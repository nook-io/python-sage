import pprint
import six
from sage.configuration import Configuration


class PostMigrationTaxReturns(object):
    openapi_types = {
        "migration_tax_return": "PostMigrationTaxReturnsMigrationTaxReturn"
    }
    attribute_map = {"migration_tax_return": "migration_tax_return"}

    def __init__(self, migration_tax_return=None, local_vars_configuration=None):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._migration_tax_return = None
        self.discriminator = None
        self.migration_tax_return = migration_tax_return

    @property
    def migration_tax_return(self):
        return self._migration_tax_return

    @migration_tax_return.setter
    def migration_tax_return(self, migration_tax_return):
        if (
            self.local_vars_configuration.client_side_validation
            and migration_tax_return is None
        ):
            raise ValueError(
                "Invalid value for `migration_tax_return`, must not be `None`"
            )
        self._migration_tax_return = migration_tax_return

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
        if not isinstance(other, PostMigrationTaxReturns):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PostMigrationTaxReturns):
            return True
        return self.to_dict() != other.to_dict()
