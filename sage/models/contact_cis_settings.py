import pprint
import six
from sage.configuration import Configuration


class ContactCisSettings(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        "registered_cis_name": "str",
        "subcontractor_verification_number": "str",
        "deduction_rate": "ContactCisDeductionRate",
    }
    attribute_map = {
        "registered_cis_name": "registered_cis_name",
        "subcontractor_verification_number": "subcontractor_verification_number",
        "deduction_rate": "deduction_rate",
    }

    def __init__(
        self,
        registered_cis_name=None,
        subcontractor_verification_number=None,
        deduction_rate=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._registered_cis_name = None
        self._subcontractor_verification_number = None
        self._deduction_rate = None
        self.discriminator = None
        if registered_cis_name is not None:
            self.registered_cis_name = registered_cis_name
        if subcontractor_verification_number is not None:
            self.subcontractor_verification_number = subcontractor_verification_number
        if deduction_rate is not None:
            self.deduction_rate = deduction_rate

    @property
    def registered_cis_name(self):
        return self._registered_cis_name

    @registered_cis_name.setter
    def registered_cis_name(self, registered_cis_name):
        self._registered_cis_name = registered_cis_name

    @property
    def subcontractor_verification_number(self):
        return self._subcontractor_verification_number

    @subcontractor_verification_number.setter
    def subcontractor_verification_number(self, subcontractor_verification_number):
        self._subcontractor_verification_number = subcontractor_verification_number

    @property
    def deduction_rate(self):
        return self._deduction_rate

    @deduction_rate.setter
    def deduction_rate(self, deduction_rate):
        self._deduction_rate = deduction_rate

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
        if not isinstance(other, ContactCisSettings):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, ContactCisSettings):
            return True
        return self.to_dict() != other.to_dict()
