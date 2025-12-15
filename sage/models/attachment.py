import pprint
import six
from sage.configuration import Configuration


class Attachment(object):
    openapi_types = {
        "id": "str",
        "displayed_as": "str",
        "path": "str",
        "deleted_at": "datetime",
        "file": "str",
        "mime_type": "str",
        "description": "str",
        "file_extension": "str",
        "transaction": "Base",
        "file_size": "int",
        "file_name": "str",
        "file_path": "str",
        "attachment_context_type": "Base",
        "attachment_context": "Base",
        "is_public": "bool",
        "created_at": "datetime",
        "updated_at": "datetime",
    }
    attribute_map = {
        "id": "id",
        "displayed_as": "displayed_as",
        "path": "$path",
        "deleted_at": "deleted_at",
        "file": "file",
        "mime_type": "mime_type",
        "description": "description",
        "file_extension": "file_extension",
        "transaction": "transaction",
        "file_size": "file_size",
        "file_name": "file_name",
        "file_path": "$file_path",
        "attachment_context_type": "attachment_context_type",
        "attachment_context": "attachment_context",
        "is_public": "is_public",
        "created_at": "created_at",
        "updated_at": "updated_at",
    }

    def __init__(
        self,
        id=None,
        displayed_as=None,
        path=None,
        deleted_at=None,
        file=None,
        mime_type=None,
        description=None,
        file_extension=None,
        transaction=None,
        file_size=None,
        file_name=None,
        file_path=None,
        attachment_context_type=None,
        attachment_context=None,
        is_public=None,
        created_at=None,
        updated_at=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._id = None
        self._displayed_as = None
        self._path = None
        self._deleted_at = None
        self._file = None
        self._mime_type = None
        self._description = None
        self._file_extension = None
        self._transaction = None
        self._file_size = None
        self._file_name = None
        self._file_path = None
        self._attachment_context_type = None
        self._attachment_context = None
        self._is_public = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if displayed_as is not None:
            self.displayed_as = displayed_as
        if path is not None:
            self.path = path
        if deleted_at is not None:
            self.deleted_at = deleted_at
        if file is not None:
            self.file = file
        if mime_type is not None:
            self.mime_type = mime_type
        if description is not None:
            self.description = description
        if file_extension is not None:
            self.file_extension = file_extension
        if transaction is not None:
            self.transaction = transaction
        if file_size is not None:
            self.file_size = file_size
        if file_name is not None:
            self.file_name = file_name
        if file_path is not None:
            self.file_path = file_path
        if attachment_context_type is not None:
            self.attachment_context_type = attachment_context_type
        if attachment_context is not None:
            self.attachment_context = attachment_context
        if is_public is not None:
            self.is_public = is_public
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

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
    def deleted_at(self):
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        self._deleted_at = deleted_at

    @property
    def file(self):
        return self._file

    @file.setter
    def file(self, file):
        self._file = file

    @property
    def mime_type(self):
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
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
    def transaction(self):
        return self._transaction

    @transaction.setter
    def transaction(self, transaction):
        self._transaction = transaction

    @property
    def file_size(self):
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        self._file_size = file_size

    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        self._file_name = file_name

    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        self._file_path = file_path

    @property
    def attachment_context_type(self):
        return self._attachment_context_type

    @attachment_context_type.setter
    def attachment_context_type(self, attachment_context_type):
        self._attachment_context_type = attachment_context_type

    @property
    def attachment_context(self):
        return self._attachment_context

    @attachment_context.setter
    def attachment_context(self, attachment_context):
        self._attachment_context = attachment_context

    @property
    def is_public(self):
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        self._is_public = is_public

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
        if not isinstance(other, Attachment):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, Attachment):
            return True
        return self.to_dict() != other.to_dict()
