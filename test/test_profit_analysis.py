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
from sage.models.profit_analysis import ProfitAnalysis  # noqa: E501
from sage.rest import ApiException

class TestProfitAnalysis(unittest.TestCase):
    """ProfitAnalysis unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ProfitAnalysis
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = sage.models.profit_analysis.ProfitAnalysis()  # noqa: E501
        if include_optional :
            return ProfitAnalysis(
                total = sage.models.profit_breakdown.ProfitBreakdown(
                    description = '0', 
                    total_cost = 1.337, 
                    total_sale = 1.337, 
                    profit = 1.337, 
                    profit_percentage = 1.337, ), 
                line_breakdown = [
                    sage.models.profit_breakdown.ProfitBreakdown(
                        description = '0', 
                        total_cost = 1.337, 
                        total_sale = 1.337, 
                        profit = 1.337, 
                        profit_percentage = 1.337, )
                    ]
            )
        else :
            return ProfitAnalysis(
        )

    def testProfitAnalysis(self):
        """Test ProfitAnalysis"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
