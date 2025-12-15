import pprint
import six
from sage.configuration import Configuration


class PostJournalCodesJournalCode(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        "name": "str",
        "code": "str",
        "journal_code_type_id": "str",
        "control_name": "str",
        "reserved": "bool",
    }
    attribute_map = {
        "name": "name",
        "code": "code",
        "journal_code_type_id": "journal_code_type_id",
        "control_name": "control_name",
        "reserved": "reserved",
    }

    def __init__(
        self,
        name=None,
        code=None,
        journal_code_type_id=None,
        control_name=None,
        reserved=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._name = None
        self._code = None
        self._journal_code_type_id = None
        self._control_name = None
        self._reserved = None
        self.discriminator = None
        self.name = name
        self.code = code
        self.journal_code_type_id = journal_code_type_id
        if control_name is not None:
            self.control_name = control_name
        if reserved is not None:
            self.reserved = reserved

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if self.local_vars_configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        self._name = name

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        if self.local_vars_configuration.client_side_validation and code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")
        self._code = code

    @property
    def journal_code_type_id(self):
        return self._journal_code_type_id

    @journal_code_type_id.setter
    def journal_code_type_id(self, journal_code_type_id):
        if (
            self.local_vars_configuration.client_side_validation
            and journal_code_type_id is None
        ):
            raise ValueError(
                "Invalid value for `journal_code_type_id`, must not be `None`"
            )
        self._journal_code_type_id = journal_code_type_id

    @property
    def control_name(self):
        return self._control_name

    @control_name.setter
    def control_name(self, control_name):
        self._control_name = control_name

    @property
    def reserved(self):
        return self._reserved

    @reserved.setter
    def reserved(self, reserved):
        self._reserved = reserved

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
        if not isinstance(other, PostJournalCodesJournalCode):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PostJournalCodesJournalCode):
            return True
        return self.to_dict() != other.to_dict()
