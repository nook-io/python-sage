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
from sage.models.post_sales_estimates_sales_estimate_estimate_lines import PostSalesEstimatesSalesEstimateEstimateLines  # noqa: E501
from sage.rest import ApiException

class TestPostSalesEstimatesSalesEstimateEstimateLines(unittest.TestCase):
    """PostSalesEstimatesSalesEstimateEstimateLines unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PostSalesEstimatesSalesEstimateEstimateLines
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = sage.models.post_sales_estimates_sales_estimate_estimate_lines.PostSalesEstimatesSalesEstimateEstimateLines()  # noqa: E501
        if include_optional :
            return PostSalesEstimatesSalesEstimateEstimateLines(
                description = '0', 
                ledger_account_id = '0', 
                quantity = 1.337, 
                unit_price = 1.337, 
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
                discount_amount = 1.337, 
                base_currency_discount_amount = 1.337, 
                discount_percentage = 1.337, 
                eu_sales_description_id = '0'
            )
        else :
            return PostSalesEstimatesSalesEstimateEstimateLines(
                description = '0',
                ledger_account_id = '0',
                quantity = 1.337,
                unit_price = 1.337,
        )

    def testPostSalesEstimatesSalesEstimateEstimateLines(self):
        """Test PostSalesEstimatesSalesEstimateEstimateLines"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
