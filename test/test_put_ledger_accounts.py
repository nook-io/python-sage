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
from sage.models.put_ledger_accounts import PutLedgerAccounts  # noqa: E501
from sage.rest import ApiException

class TestPutLedgerAccounts(unittest.TestCase):
    """PutLedgerAccounts unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PutLedgerAccounts
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = sage.models.put_ledger_accounts.PutLedgerAccounts()  # noqa: E501
        if include_optional :
            return PutLedgerAccounts(
                ledger_account = sage.models.put_ledger_accounts_ledger_account.putLedgerAccounts_ledger_account(
                    ledger_account_type_id = '0', 
                    included_in_chart = True, 
                    name = '0', 
                    display_name = '0', 
                    nominal_code = 1, 
                    ledger_account_classification_id = '0', 
                    tax_rate_id = '0', 
                    fixed_tax_rate = True, 
                    visible_in_banking = True, 
                    visible_in_expenses = True, 
                    visible_in_journals = True, 
                    visible_in_other_payments = True, 
                    visible_in_other_receipts = True, 
                    visible_in_reporting = True, 
                    visible_in_sales = True, 
                    control_name = '0', 
                    tax_recoverable = True, 
                    recoverable_percentage = 1.337, 
                    non_recoverable_ledger_account_id = '0', 
                    cis_materials = True, 
                    cis_labour = True, 
                    gifi_code = 1E+3, )
            )
        else :
            return PutLedgerAccounts(
                ledger_account = sage.models.put_ledger_accounts_ledger_account.putLedgerAccounts_ledger_account(
                    ledger_account_type_id = '0', 
                    included_in_chart = True, 
                    name = '0', 
                    display_name = '0', 
                    nominal_code = 1, 
                    ledger_account_classification_id = '0', 
                    tax_rate_id = '0', 
                    fixed_tax_rate = True, 
                    visible_in_banking = True, 
                    visible_in_expenses = True, 
                    visible_in_journals = True, 
                    visible_in_other_payments = True, 
                    visible_in_other_receipts = True, 
                    visible_in_reporting = True, 
                    visible_in_sales = True, 
                    control_name = '0', 
                    tax_recoverable = True, 
                    recoverable_percentage = 1.337, 
                    non_recoverable_ledger_account_id = '0', 
                    cis_materials = True, 
                    cis_labour = True, 
                    gifi_code = 1E+3, ),
        )

    def testPutLedgerAccounts(self):
        """Test PutLedgerAccounts"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
