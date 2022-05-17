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
from sage.models.post_bank_reconciliations_bank_reconciliation import PostBankReconciliationsBankReconciliation  # noqa: E501
from sage.rest import ApiException

class TestPostBankReconciliationsBankReconciliation(unittest.TestCase):
    """PostBankReconciliationsBankReconciliation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PostBankReconciliationsBankReconciliation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = sage.models.post_bank_reconciliations_bank_reconciliation.PostBankReconciliationsBankReconciliation()  # noqa: E501
        if include_optional :
            return PostBankReconciliationsBankReconciliation(
                bank_account_id = '0', 
                statement_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                statement_end_balance = 1.337, 
                reference = '0', 
                total_received = 1.337, 
                total_paid = 1.337, 
                starting_balance = 1.337, 
                closing_balance = 1.337, 
                reconciled_balance = 1.337, 
                balance_difference = 1.337, 
                status_id = '0'
            )
        else :
            return PostBankReconciliationsBankReconciliation(
                bank_account_id = '0',
        )

    def testPostBankReconciliationsBankReconciliation(self):
        """Test PostBankReconciliationsBankReconciliation"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
