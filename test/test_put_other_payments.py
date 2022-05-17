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
from sage.models.put_other_payments import PutOtherPayments  # noqa: E501
from sage.rest import ApiException

class TestPutOtherPayments(unittest.TestCase):
    """PutOtherPayments unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PutOtherPayments
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = sage.models.put_other_payments.PutOtherPayments()  # noqa: E501
        if include_optional :
            return PutOtherPayments(
                other_payment = sage.models.put_other_payments_other_payment.putOtherPayments_other_payment(
                    transaction_type_id = '0', 
                    date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    total_amount = 1.337, 
                    base_currency_total_itc_amount = 1.337, 
                    total_itc_amount = 1.337, 
                    base_currency_total_itr_amount = 1.337, 
                    total_itr_amount = 1.337, 
                    part_recoverable = True, 
                    payment_method_id = '0', 
                    contact_id = '0', 
                    bank_account_id = '0', 
                    tax_address_region_id = '0', 
                    net_amount = 1.337, 
                    tax_amount = 1.337, 
                    reference = '0', 
                    withholding_tax_rate = 1.337, 
                    withholding_tax_amount = 1.337, 
                    payment_lines = [
                        sage.models.put_other_payments_other_payment_payment_lines.putOtherPayments_other_payment_payment_lines(
                            ledger_account_id = '0', 
                            total_amount = 1.337, 
                            details = '0', 
                            tax_rate_id = '0', 
                            net_amount = 1.337, 
                            tax_amount = 1.337, 
                            is_purchase_for_resale = True, 
                            trade_of_asset = True, 
                            gst_amount = 1.337, 
                            pst_amount = 1.337, 
                            tax_recoverable = True, )
                        ], )
            )
        else :
            return PutOtherPayments(
                other_payment = sage.models.put_other_payments_other_payment.putOtherPayments_other_payment(
                    transaction_type_id = '0', 
                    date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    total_amount = 1.337, 
                    base_currency_total_itc_amount = 1.337, 
                    total_itc_amount = 1.337, 
                    base_currency_total_itr_amount = 1.337, 
                    total_itr_amount = 1.337, 
                    part_recoverable = True, 
                    payment_method_id = '0', 
                    contact_id = '0', 
                    bank_account_id = '0', 
                    tax_address_region_id = '0', 
                    net_amount = 1.337, 
                    tax_amount = 1.337, 
                    reference = '0', 
                    withholding_tax_rate = 1.337, 
                    withholding_tax_amount = 1.337, 
                    payment_lines = [
                        sage.models.put_other_payments_other_payment_payment_lines.putOtherPayments_other_payment_payment_lines(
                            ledger_account_id = '0', 
                            total_amount = 1.337, 
                            details = '0', 
                            tax_rate_id = '0', 
                            net_amount = 1.337, 
                            tax_amount = 1.337, 
                            is_purchase_for_resale = True, 
                            trade_of_asset = True, 
                            gst_amount = 1.337, 
                            pst_amount = 1.337, 
                            tax_recoverable = True, )
                        ], ),
        )

    def testPutOtherPayments(self):
        """Test PutOtherPayments"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
