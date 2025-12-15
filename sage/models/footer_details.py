import pprint
import six
from sage.configuration import Configuration


class FooterDetails(object):
    openapi_types = {"column_1": "str", "column_2": "str", "column_3": "str"}
    attribute_map = {
        "column_1": "column_1",
        "column_2": "column_2",
        "column_3": "column_3",
    }

    def __init__(
        self, column_1=None, column_2=None, column_3=None, local_vars_configuration=None
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._column_1 = None
        self._column_2 = None
        self._column_3 = None
        self.discriminator = None
        if column_1 is not None:
            self.column_1 = column_1
        if column_2 is not None:
            self.column_2 = column_2
        if column_3 is not None:
            self.column_3 = column_3

    @property
    def column_1(self):
        return self._column_1

    @column_1.setter
    def column_1(self, column_1):
        self._column_1 = column_1

    @property
    def column_2(self):
        return self._column_2

    @column_2.setter
    def column_2(self, column_2):
        self._column_2 = column_2

    @property
    def column_3(self):
        return self._column_3

    @column_3.setter
    def column_3(self, column_3):
        self._column_3 = column_3

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
        if not isinstance(other, FooterDetails):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, FooterDetails):
            return True
        return self.to_dict() != other.to_dict()
