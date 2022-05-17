# coding: utf-8

"""
    Sage Business Cloud Accounting - Accounts

    Documentation of the Sage Business Cloud Accounting API.  # noqa: E501

    The version of the OpenAPI document: 3.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import sage
from sage.api.business_exchange_rates_api import BusinessExchangeRatesApi  # noqa: E501
from sage.rest import ApiException


class TestBusinessExchangeRatesApi(unittest.TestCase):
    """BusinessExchangeRatesApi unit test stubs"""

    def setUp(self):
        self.api = sage.api.business_exchange_rates_api.BusinessExchangeRatesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_business_exchange_rates_key(self):
        """Test case for delete_business_exchange_rates_key

        Deletes a Business Exchange Rate  # noqa: E501
        """
        pass

    def test_get_business_exchange_rates(self):
        """Test case for get_business_exchange_rates

        Returns all Business Exchange Rates  # noqa: E501
        """
        pass

    def test_get_business_exchange_rates_key(self):
        """Test case for get_business_exchange_rates_key

        Returns a Business Exchange Rate  # noqa: E501
        """
        pass

    def test_post_business_exchange_rates(self):
        """Test case for post_business_exchange_rates

        Creates a Business Exchange Rate  # noqa: E501
        """
        pass

    def test_put_business_exchange_rates_key(self):
        """Test case for put_business_exchange_rates_key

        Updates a Business Exchange Rate  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
