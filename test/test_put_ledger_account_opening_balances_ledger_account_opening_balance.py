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
from sage.models.put_ledger_account_opening_balances_ledger_account_opening_balance import PutLedgerAccountOpeningBalancesLedgerAccountOpeningBalance  # noqa: E501
from sage.rest import ApiException

class TestPutLedgerAccountOpeningBalancesLedgerAccountOpeningBalance(unittest.TestCase):
    """PutLedgerAccountOpeningBalancesLedgerAccountOpeningBalance unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PutLedgerAccountOpeningBalancesLedgerAccountOpeningBalance
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = sage.models.put_ledger_account_opening_balances_ledger_account_opening_balance.PutLedgerAccountOpeningBalancesLedgerAccountOpeningBalance()  # noqa: E501
        if include_optional :
            return PutLedgerAccountOpeningBalancesLedgerAccountOpeningBalance(
                ledger_account_id = '0', 
                debit = 1.337, 
                credit = 1.337, 
                details = '0'
            )
        else :
            return PutLedgerAccountOpeningBalancesLedgerAccountOpeningBalance(
        )

    def testPutLedgerAccountOpeningBalancesLedgerAccountOpeningBalance(self):
        """Test PutLedgerAccountOpeningBalancesLedgerAccountOpeningBalance"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
