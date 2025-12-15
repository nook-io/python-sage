import pprint
import six
from sage.configuration import Configuration


class PostOtherPayments(object):
    openapi_types = {"other_payment": "PostOtherPaymentsOtherPayment"}
    attribute_map = {"other_payment": "other_payment"}

    def __init__(self, other_payment=None, local_vars_configuration=None):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._other_payment = None
        self.discriminator = None
        self.other_payment = other_payment

    @property
    def other_payment(self):
        return self._other_payment

    @other_payment.setter
    def other_payment(self, other_payment):
        if (
            self.local_vars_configuration.client_side_validation
            and other_payment is None
        ):
            raise ValueError("Invalid value for `other_payment`, must not be `None`")
        self._other_payment = other_payment

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
        if not isinstance(other, PostOtherPayments):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PostOtherPayments):
            return True
        return self.to_dict() != other.to_dict()
