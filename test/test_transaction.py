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
from sage.models.transaction import Transaction  # noqa: E501
from sage.rest import ApiException

class TestTransaction(unittest.TestCase):
    """Transaction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Transaction
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = sage.models.transaction.Transaction()  # noqa: E501
        if include_optional :
            return Transaction(
                id = '0', 
                displayed_as = '0', 
                path = '0', 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                deleted = True, 
                reference = '0', 
                total = 1.337, 
                total_in_transaction_currency = 1.337, 
                contact = sage.models.base.Base(
                    id = '0', 
                    displayed_as = '0', 
                    __path = '0', ), 
                transaction_type = sage.models.base.Base(
                    id = '0', 
                    displayed_as = '0', 
                    __path = '0', ), 
                origin = sage.models.transaction_origin.TransactionOrigin(
                    id = '0', 
                    displayed_as = '0', 
                    __path = '0', 
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
                    sent = True, ), 
                audit_trail_id = '0', 
                number_of_attachments = '0'
            )
        else :
            return Transaction(
        )

    def testTransaction(self):
        """Test Transaction"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()