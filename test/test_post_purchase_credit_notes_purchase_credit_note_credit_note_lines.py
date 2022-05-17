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
from sage.models.post_purchase_credit_notes_purchase_credit_note_credit_note_lines import PostPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines  # noqa: E501
from sage.rest import ApiException

class TestPostPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines(unittest.TestCase):
    """PostPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PostPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = sage.models.post_purchase_credit_notes_purchase_credit_note_credit_note_lines.PostPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines()  # noqa: E501
        if include_optional :
            return PostPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines(
                description = '0', 
                ledger_account_id = '0', 
                quantity = 1.337, 
                unit_price = 1.337, 
                is_purchase_for_resale = True, 
                product_id = '0', 
                service_id = '0', 
                trade_of_asset = True, 
                net_amount = 1.337, 
                tax_rate_id = '0', 
                tax_amount = 1.337, 
                total_amount = 1.337, 
                base_currency_unit_price = 1.337, 
                unit_price_includes_tax = True, 
                base_currency_net_amount = 1.337, 
                base_currency_tax_amount = 1.337, 
                base_currency_total_amount = 1.337, 
                eu_goods_services_type_id = '0', 
                gst_amount = 1.337, 
                pst_amount = 1.337, 
                tax_recoverable = True
            )
        else :
            return PostPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines(
                description = '0',
                ledger_account_id = '0',
                quantity = 1.337,
                unit_price = 1.337,
        )

    def testPostPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines(self):
        """Test PostPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
