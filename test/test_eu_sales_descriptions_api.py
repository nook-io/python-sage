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
from sage.api.eu_sales_descriptions_api import EUSalesDescriptionsApi  # noqa: E501
from sage.rest import ApiException


class TestEUSalesDescriptionsApi(unittest.TestCase):
    """EUSalesDescriptionsApi unit test stubs"""

    def setUp(self):
        self.api = sage.api.eu_sales_descriptions_api.EUSalesDescriptionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_eu_sales_descriptions(self):
        """Test case for get_eu_sales_descriptions

        Returns all EU Sales Descriptions  # noqa: E501
        """
        pass

    def test_get_eu_sales_descriptions_key(self):
        """Test case for get_eu_sales_descriptions_key

        Returns a EU Sales Description  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
