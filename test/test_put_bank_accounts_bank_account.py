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
from sage.models.put_bank_accounts_bank_account import PutBankAccountsBankAccount  # noqa: E501
from sage.rest import ApiException

class TestPutBankAccountsBankAccount(unittest.TestCase):
    """PutBankAccountsBankAccount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PutBankAccountsBankAccount
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = sage.models.put_bank_accounts_bank_account.PutBankAccountsBankAccount()  # noqa: E501
        if include_optional :
            return PutBankAccountsBankAccount(
                bank_account_type_id = '0', 
                ledger_account_id = '0', 
                nominal_code = 1, 
                default_payment_method_id = '0', 
                gifi_code = 1E+3, 
                bank_account_details = sage.models.put_bank_accounts_bank_account_bank_account_details.putBankAccounts_bank_account_bank_account_details(
                    account_name = '0', 
                    account_number = '0', 
                    sort_code = '0', 
                    bic = '0', 
                    iban = '0', ), 
                main_address = sage.models.post_bank_accounts_bank_account_main_address.postBankAccounts_bank_account_main_address(
                    address_line_1 = '0', 
                    address_line_2 = '0', 
                    city = '0', 
                    postal_code = '0', 
                    country_id = '0', 
                    bank_account_id = '0', 
                    contact_id = '0', 
                    address_type_id = '0', 
                    name = '0', 
                    region = '0', 
                    country_group_id = '0', 
                    is_main_address = True, ), 
                main_contact_person = sage.models.post_bank_accounts_bank_account_main_contact_person.postBankAccounts_bank_account_main_contact_person(
                    name = '0', 
                    job_title = '0', 
                    telephone = '0', 
                    mobile = '0', 
                    email = '0', 
                    fax = '0', ), 
                journal_code = sage.models.post_journals_journal_journal_code.postJournals_journal_journal_code(
                    name = '0', 
                    code = '0', 
                    journal_code_type_id = '0', 
                    control_name = '0', 
                    reserved = True, )
            )
        else :
            return PutBankAccountsBankAccount(
        )

    def testPutBankAccountsBankAccount(self):
        """Test PutBankAccountsBankAccount"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
