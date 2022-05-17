# coding: utf-8

"""
    Sage Business Cloud Accounting - Accounts

    Documentation of the Sage Business Cloud Accounting API.  # noqa: E501

    The version of the OpenAPI document: 3.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import sage
from sage.models.hosted_artefact_payment_setting import HostedArtefactPaymentSetting  # noqa: E501
from sage.rest import ApiException

class TestHostedArtefactPaymentSetting(unittest.TestCase):
    """HostedArtefactPaymentSetting unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test HostedArtefactPaymentSetting
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = sage.models.hosted_artefact_payment_setting.HostedArtefactPaymentSetting()  # noqa: E501
        if include_optional :
            return HostedArtefactPaymentSetting(
                id = '0', 
                displayed_as = '0', 
                path = '0', 
                object_guid = '0', 
                disable_payment = True
            )
        else :
            return HostedArtefactPaymentSetting(
        )

    def testHostedArtefactPaymentSetting(self):
        """Test HostedArtefactPaymentSetting"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
