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
from sage.models.put_business_exchange_rates_business_exchange_rate import PutBusinessExchangeRatesBusinessExchangeRate  # noqa: E501
from sage.rest import ApiException

class TestPutBusinessExchangeRatesBusinessExchangeRate(unittest.TestCase):
    """PutBusinessExchangeRatesBusinessExchangeRate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PutBusinessExchangeRatesBusinessExchangeRate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = sage.models.put_business_exchange_rates_business_exchange_rate.PutBusinessExchangeRatesBusinessExchangeRate()  # noqa: E501
        if include_optional :
            return PutBusinessExchangeRatesBusinessExchangeRate(
                currency_id = '0', 
                rate = 1.337, 
                inverse_rate = 1.337, 
                base_currency_id = '0'
            )
        else :
            return PutBusinessExchangeRatesBusinessExchangeRate(
        )

    def testPutBusinessExchangeRatesBusinessExchangeRate(self):
        """Test PutBusinessExchangeRatesBusinessExchangeRate"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
