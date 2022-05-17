# coding: utf-8

"""
    Sage Business Cloud Accounting - Accounts

    Documentation of the Sage Business Cloud Accounting API.  # noqa: E501

    The version of the OpenAPI document: 3.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from sage.configuration import Configuration


class PutJournalCodesJournalCode(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'name': 'str',
        'code': 'str',
        'journal_code_type_id': 'str',
        'control_name': 'str',
        'reserved': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'code': 'code',
        'journal_code_type_id': 'journal_code_type_id',
        'control_name': 'control_name',
        'reserved': 'reserved'
    }

    def __init__(self, name=None, code=None, journal_code_type_id=None, control_name=None, reserved=None, local_vars_configuration=None):  # noqa: E501
        """PutJournalCodesJournalCode - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._code = None
        self._journal_code_type_id = None
        self._control_name = None
        self._reserved = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if code is not None:
            self.code = code
        if journal_code_type_id is not None:
            self.journal_code_type_id = journal_code_type_id
        if control_name is not None:
            self.control_name = control_name
        if reserved is not None:
            self.reserved = reserved

    @property
    def name(self):
        """Gets the name of this PutJournalCodesJournalCode.  # noqa: E501

        The name of the journal code  # noqa: E501

        :return: The name of this PutJournalCodesJournalCode.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PutJournalCodesJournalCode.

        The name of the journal code  # noqa: E501

        :param name: The name of this PutJournalCodesJournalCode.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def code(self):
        """Gets the code of this PutJournalCodesJournalCode.  # noqa: E501

        The code of the journal code  # noqa: E501

        :return: The code of this PutJournalCodesJournalCode.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this PutJournalCodesJournalCode.

        The code of the journal code  # noqa: E501

        :param code: The code of this PutJournalCodesJournalCode.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def journal_code_type_id(self):
        """Gets the journal_code_type_id of this PutJournalCodesJournalCode.  # noqa: E501

        The journal code type of the journal code  # noqa: E501

        :return: The journal_code_type_id of this PutJournalCodesJournalCode.  # noqa: E501
        :rtype: str
        """
        return self._journal_code_type_id

    @journal_code_type_id.setter
    def journal_code_type_id(self, journal_code_type_id):
        """Sets the journal_code_type_id of this PutJournalCodesJournalCode.

        The journal code type of the journal code  # noqa: E501

        :param journal_code_type_id: The journal_code_type_id of this PutJournalCodesJournalCode.  # noqa: E501
        :type: str
        """

        self._journal_code_type_id = journal_code_type_id

    @property
    def control_name(self):
        """Gets the control_name of this PutJournalCodesJournalCode.  # noqa: E501

        The control name of the journal code  Control names are identifiers for a journal codes with a specific meaning. Some examples are `AC` for purchases, `VE` for sales, `OD` for other transactions and `REPBAL` for opening balances.   # noqa: E501

        :return: The control_name of this PutJournalCodesJournalCode.  # noqa: E501
        :rtype: str
        """
        return self._control_name

    @control_name.setter
    def control_name(self, control_name):
        """Sets the control_name of this PutJournalCodesJournalCode.

        The control name of the journal code  Control names are identifiers for a journal codes with a specific meaning. Some examples are `AC` for purchases, `VE` for sales, `OD` for other transactions and `REPBAL` for opening balances.   # noqa: E501

        :param control_name: The control_name of this PutJournalCodesJournalCode.  # noqa: E501
        :type: str
        """

        self._control_name = control_name

    @property
    def reserved(self):
        """Gets the reserved of this PutJournalCodesJournalCode.  # noqa: E501

        Indicates whether the journal code is reserved.  Reserved journal codes cannot be deleted. A journal code is reserved when it has a control name. Please note that journal codes can also not be deleted when there is any journal that is using the code.   # noqa: E501

        :return: The reserved of this PutJournalCodesJournalCode.  # noqa: E501
        :rtype: bool
        """
        return self._reserved

    @reserved.setter
    def reserved(self, reserved):
        """Sets the reserved of this PutJournalCodesJournalCode.

        Indicates whether the journal code is reserved.  Reserved journal codes cannot be deleted. A journal code is reserved when it has a control name. Please note that journal codes can also not be deleted when there is any journal that is using the code.   # noqa: E501

        :param reserved: The reserved of this PutJournalCodesJournalCode.  # noqa: E501
        :type: bool
        """

        self._reserved = reserved

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PutJournalCodesJournalCode):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PutJournalCodesJournalCode):
            return True

        return self.to_dict() != other.to_dict()
