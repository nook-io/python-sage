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
from sage.models.payment_on_account import PaymentOnAccount  # noqa: E501
from sage.rest import ApiException

class TestPaymentOnAccount(unittest.TestCase):
    """PaymentOnAccount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaymentOnAccount
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = sage.models.payment_on_account.PaymentOnAccount()  # noqa: E501
        if include_optional :
            return PaymentOnAccount(
                id = '0', 
                displayed_as = '0', 
                path = '0', 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                contact_name = '0', 
                contact_reference = '0', 
                contact = sage.models.base.Base(
                    id = '0', 
                    displayed_as = '0', 
                    __path = '0', ), 
                date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                reference = '0', 
                net_amount = 1.337, 
                tax_amount = 1.337, 
                total_amount = 1.337, 
                outstanding_amount = 1.337, 
                currency = sage.models.base.Base(
                    id = '0', 
                    displayed_as = '0', 
                    __path = '0', ), 
                exchange_rate = 1.337, 
                base_currency_net_amount = 1.337, 
                base_currency_tax_amount = 1.337, 
                base_currency_total_amount = 1.337, 
                base_currency_outstanding_amount = 1.337, 
                status = sage.models.base.Base(
                    id = '0', 
                    displayed_as = '0', 
                    __path = '0', )
            )
        else :
            return PaymentOnAccount(
        )

    def testPaymentOnAccount(self):
        """Test PaymentOnAccount"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
