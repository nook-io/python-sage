import pprint
import six
from sage.configuration import Configuration


class PostJournalsJournal(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        "date": "date",
        "reference": "str",
        "description": "str",
        "total": "float",
        "journal_code": "PostJournalsJournalJournalCode",
        "journal_lines": "list[PostJournalsJournalJournalLines]",
    }
    attribute_map = {
        "date": "date",
        "reference": "reference",
        "description": "description",
        "total": "total",
        "journal_code": "journal_code",
        "journal_lines": "journal_lines",
    }

    def __init__(
        self,
        date=None,
        reference=None,
        description=None,
        total=None,
        journal_code=None,
        journal_lines=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._date = None
        self._reference = None
        self._description = None
        self._total = None
        self._journal_code = None
        self._journal_lines = None
        self.discriminator = None
        self.date = date
        self.reference = reference
        if description is not None:
            self.description = description
        if total is not None:
            self.total = total
        if journal_code is not None:
            self.journal_code = journal_code
        self.journal_lines = journal_lines

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if self.local_vars_configuration.client_side_validation and date is None:
            raise ValueError("Invalid value for `date`, must not be `None`")
        self._date = date

    @property
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, reference):
        if self.local_vars_configuration.client_side_validation and reference is None:
            raise ValueError("Invalid value for `reference`, must not be `None`")
        self._reference = reference

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, total):
        self._total = total

    @property
    def journal_code(self):
        return self._journal_code

    @journal_code.setter
    def journal_code(self, journal_code):
        self._journal_code = journal_code

    @property
    def journal_lines(self):
        return self._journal_lines

    @journal_lines.setter
    def journal_lines(self, journal_lines):
        if (
            self.local_vars_configuration.client_side_validation
            and journal_lines is None
        ):
            raise ValueError("Invalid value for `journal_lines`, must not be `None`")
        self._journal_lines = journal_lines

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
        if not isinstance(other, PostJournalsJournal):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PostJournalsJournal):
            return True
        return self.to_dict() != other.to_dict()
