import pprint
import six
from sage.configuration import Configuration


class GBBoxData(object):
    openapi_types = {
        "box_1": "float",
        "box_2": "float",
        "box_3": "float",
        "box_4": "float",
        "box_5": "float",
        "box_6": "float",
        "box_7": "float",
        "box_8": "float",
        "box_9": "float",
    }
    attribute_map = {
        "box_1": "box_1",
        "box_2": "box_2",
        "box_3": "box_3",
        "box_4": "box_4",
        "box_5": "box_5",
        "box_6": "box_6",
        "box_7": "box_7",
        "box_8": "box_8",
        "box_9": "box_9",
    }

    def __init__(
        self,
        box_1=None,
        box_2=None,
        box_3=None,
        box_4=None,
        box_5=None,
        box_6=None,
        box_7=None,
        box_8=None,
        box_9=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._box_1 = None
        self._box_2 = None
        self._box_3 = None
        self._box_4 = None
        self._box_5 = None
        self._box_6 = None
        self._box_7 = None
        self._box_8 = None
        self._box_9 = None
        self.discriminator = None
        if box_1 is not None:
            self.box_1 = box_1
        if box_2 is not None:
            self.box_2 = box_2
        if box_3 is not None:
            self.box_3 = box_3
        if box_4 is not None:
            self.box_4 = box_4
        if box_5 is not None:
            self.box_5 = box_5
        if box_6 is not None:
            self.box_6 = box_6
        if box_7 is not None:
            self.box_7 = box_7
        if box_8 is not None:
            self.box_8 = box_8
        if box_9 is not None:
            self.box_9 = box_9

    @property
    def box_1(self):
        return self._box_1

    @box_1.setter
    def box_1(self, box_1):
        self._box_1 = box_1

    @property
    def box_2(self):
        return self._box_2

    @box_2.setter
    def box_2(self, box_2):
        self._box_2 = box_2

    @property
    def box_3(self):
        return self._box_3

    @box_3.setter
    def box_3(self, box_3):
        self._box_3 = box_3

    @property
    def box_4(self):
        return self._box_4

    @box_4.setter
    def box_4(self, box_4):
        self._box_4 = box_4

    @property
    def box_5(self):
        return self._box_5

    @box_5.setter
    def box_5(self, box_5):
        self._box_5 = box_5

    @property
    def box_6(self):
        return self._box_6

    @box_6.setter
    def box_6(self, box_6):
        self._box_6 = box_6

    @property
    def box_7(self):
        return self._box_7

    @box_7.setter
    def box_7(self, box_7):
        self._box_7 = box_7

    @property
    def box_8(self):
        return self._box_8

    @box_8.setter
    def box_8(self, box_8):
        self._box_8 = box_8

    @property
    def box_9(self):
        return self._box_9

    @box_9.setter
    def box_9(self, box_9):
        self._box_9 = box_9

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
        if not isinstance(other, GBBoxData):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, GBBoxData):
            return True
        return self.to_dict() != other.to_dict()
