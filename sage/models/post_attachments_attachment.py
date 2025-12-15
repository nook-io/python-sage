import pprint
import six
from sage.configuration import Configuration


class PostAttachmentsAttachment(object):
    openapi_types = {
        "file": "str",
        "file_name": "str",
        "mime_type": "str",
        "description": "str",
        "file_extension": "str",
        "transaction_id": "str",
        "file_size": "int",
        "attachment_context_type_id": "str",
        "attachment_context_id": "str",
        "is_public": "bool",
    }
    attribute_map = {
        "file": "file",
        "file_name": "file_name",
        "mime_type": "mime_type",
        "description": "description",
        "file_extension": "file_extension",
        "transaction_id": "transaction_id",
        "file_size": "file_size",
        "attachment_context_type_id": "attachment_context_type_id",
        "attachment_context_id": "attachment_context_id",
        "is_public": "is_public",
    }

    def __init__(
        self,
        file=None,
        file_name=None,
        mime_type=None,
        description=None,
        file_extension=None,
        transaction_id=None,
        file_size=None,
        attachment_context_type_id=None,
        attachment_context_id=None,
        is_public=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._file = None
        self._file_name = None
        self._mime_type = None
        self._description = None
        self._file_extension = None
        self._transaction_id = None
        self._file_size = None
        self._attachment_context_type_id = None
        self._attachment_context_id = None
        self._is_public = None
        self.discriminator = None
        self.file = file
        self.file_name = file_name
        self.mime_type = mime_type
        if description is not None:
            self.description = description
        if file_extension is not None:
            self.file_extension = file_extension
        if transaction_id is not None:
            self.transaction_id = transaction_id
        if file_size is not None:
            self.file_size = file_size
        if attachment_context_type_id is not None:
            self.attachment_context_type_id = attachment_context_type_id
        if attachment_context_id is not None:
            self.attachment_context_id = attachment_context_id
        if is_public is not None:
            self.is_public = is_public

    @property
    def file(self):
        return self._file

    @file.setter
    def file(self, file):
        if self.local_vars_configuration.client_side_validation and file is None:
            raise ValueError("Invalid value for `file`, must not be `None`")
        self._file = file

    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        if self.local_vars_configuration.client_side_validation and file_name is None:
            raise ValueError("Invalid value for `file_name`, must not be `None`")
        self._file_name = file_name

    @property
    def mime_type(self):
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        if self.local_vars_configuration.client_side_validation and mime_type is None:
            raise ValueError("Invalid value for `mime_type`, must not be `None`")
        self._mime_type = mime_type

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def file_extension(self):
        return self._file_extension

    @file_extension.setter
    def file_extension(self, file_extension):
        self._file_extension = file_extension

    @property
    def transaction_id(self):
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        self._transaction_id = transaction_id

    @property
    def file_size(self):
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        if (
            self.local_vars_configuration.client_side_validation
            and file_size is not None
            and file_size > 2621440
        ):
            raise ValueError(
                "Invalid value for `file_size`, must be a value less than or equal to `2621440`"
            )
        if (
            self.local_vars_configuration.client_side_validation
            and file_size is not None
            and file_size < 0
        ):
            raise ValueError(
                "Invalid value for `file_size`, must be a value greater than or equal to `0`"
            )
        self._file_size = file_size

    @property
    def attachment_context_type_id(self):
        return self._attachment_context_type_id

    @attachment_context_type_id.setter
    def attachment_context_type_id(self, attachment_context_type_id):
        self._attachment_context_type_id = attachment_context_type_id

    @property
    def attachment_context_id(self):
        return self._attachment_context_id

    @attachment_context_id.setter
    def attachment_context_id(self, attachment_context_id):
        self._attachment_context_id = attachment_context_id

    @property
    def is_public(self):
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        self._is_public = is_public

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
        if not isinstance(other, PostAttachmentsAttachment):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PostAttachmentsAttachment):
            return True
        return self.to_dict() != other.to_dict()
