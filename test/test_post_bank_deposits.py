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
from sage.models.post_bank_deposits import PostBankDeposits  # noqa: E501
from sage.rest import ApiException

class TestPostBankDeposits(unittest.TestCase):
    """PostBankDeposits unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PostBankDeposits
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = sage.models.post_bank_deposits.PostBankDeposits()  # noqa: E501
        if include_optional :
            return PostBankDeposits(
                bank_deposit = sage.models.post_bank_deposits_bank_deposit.postBankDeposits_bank_deposit(
                    from_bank_account_id = '0', 
                    to_bank_account_id = '0', 
                    date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    reference = '0', 
                    cash_amount = 1.337, 
                    cheque_amount = 1.337, 
                    total_amount = 1.337, )
            )
        else :
            return PostBankDeposits(
                bank_deposit = sage.models.post_bank_deposits_bank_deposit.postBankDeposits_bank_deposit(
                    from_bank_account_id = '0', 
                    to_bank_account_id = '0', 
                    date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    reference = '0', 
                    cash_amount = 1.337, 
                    cheque_amount = 1.337, 
                    total_amount = 1.337, ),
        )

    def testPostBankDeposits(self):
        """Test PostBankDeposits"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
