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
from sage.models.transaction_origin import TransactionOrigin  # noqa: E501
from sage.rest import ApiException

class TestTransactionOrigin(unittest.TestCase):
    """TransactionOrigin unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TransactionOrigin
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = sage.models.transaction_origin.TransactionOrigin()  # noqa: E501
        if include_optional :
            return TransactionOrigin(
                id = '0', 
                displayed_as = '0', 
                path = '0', 
                links = [
                    sage.models.link.Link(
                        href = '0', 
                        rel = '0', 
                        type = '0', )
                    ], 
                due_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                outstanding_amount = 1.337, 
                currency = sage.models.base.Base(
                    id = '0', 
                    displayed_as = '0', 
                    __path = '0', ), 
                status = sage.models.base.Base(
                    id = '0', 
                    displayed_as = '0', 
                    __path = '0', ), 
                sent = True
            )
        else :
            return TransactionOrigin(
        )

    def testTransactionOrigin(self):
        """Test TransactionOrigin"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
