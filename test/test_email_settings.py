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
from sage.models.email_settings import EmailSettings  # noqa: E501
from sage.rest import ApiException

class TestEmailSettings(unittest.TestCase):
    """EmailSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EmailSettings
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = sage.models.email_settings.EmailSettings()  # noqa: E501
        if include_optional :
            return EmailSettings(
                default_messages = [
                    sage.models.default_messages.DefaultMessages(
                        message_type = '0', 
                        locale = '0', 
                        message = '0', )
                    ], 
                pdf_attached = True, 
                send_bcc = True, 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return EmailSettings(
        )

    def testEmailSettings(self):
        """Test EmailSettings"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
