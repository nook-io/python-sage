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
from sage.models.post_sales_quick_entries import PostSalesQuickEntries  # noqa: E501
from sage.rest import ApiException

class TestPostSalesQuickEntries(unittest.TestCase):
    """PostSalesQuickEntries unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PostSalesQuickEntries
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = sage.models.post_sales_quick_entries.PostSalesQuickEntries()  # noqa: E501
        if include_optional :
            return PostSalesQuickEntries(
                sales_quick_entry = sage.models.post_sales_quick_entries_sales_quick_entry.postSalesQuickEntries_sales_quick_entry(
                    quick_entry_type_id = '0', 
                    date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    contact_id = '0', 
                    reference = '0', 
                    ledger_account_id = '0', 
                    contact_name = '0', 
                    contact_reference = '0', 
                    details = '0', 
                    net_amount = 1.337, 
                    tax_rate_id = '0', 
                    tax_amount = 1.337, 
                    total_amount = 1.337, 
                    currency_id = '0', 
                    exchange_rate = 1.337, 
                    inverse_exchange_rate = 1.337, 
                    base_currency_net_amount = 1.337, 
                    base_currency_tax_amount = 1.337, 
                    base_currency_total_amount = 1.337, 
                    status_id = '0', 
                    tax_address_region_id = '0', 
                    trade_of_asset = True, )
            )
        else :
            return PostSalesQuickEntries(
                sales_quick_entry = sage.models.post_sales_quick_entries_sales_quick_entry.postSalesQuickEntries_sales_quick_entry(
                    quick_entry_type_id = '0', 
                    date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    contact_id = '0', 
                    reference = '0', 
                    ledger_account_id = '0', 
                    contact_name = '0', 
                    contact_reference = '0', 
                    details = '0', 
                    net_amount = 1.337, 
                    tax_rate_id = '0', 
                    tax_amount = 1.337, 
                    total_amount = 1.337, 
                    currency_id = '0', 
                    exchange_rate = 1.337, 
                    inverse_exchange_rate = 1.337, 
                    base_currency_net_amount = 1.337, 
                    base_currency_tax_amount = 1.337, 
                    base_currency_total_amount = 1.337, 
                    status_id = '0', 
                    tax_address_region_id = '0', 
                    trade_of_asset = True, ),
        )

    def testPostSalesQuickEntries(self):
        """Test PostSalesQuickEntries"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()