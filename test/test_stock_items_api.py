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
from sage.api.stock_items_api import StockItemsApi  # noqa: E501
from sage.rest import ApiException


class TestStockItemsApi(unittest.TestCase):
    """StockItemsApi unit test stubs"""

    def setUp(self):
        self.api = sage.api.stock_items_api.StockItemsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_stock_items_key(self):
        """Test case for delete_stock_items_key

        Deletes a Stock Item  # noqa: E501
        """
        pass

    def test_get_stock_items(self):
        """Test case for get_stock_items

        Returns all Stock Items  # noqa: E501
        """
        pass

    def test_get_stock_items_key(self):
        """Test case for get_stock_items_key

        Returns a Stock Item  # noqa: E501
        """
        pass

    def test_post_stock_items(self):
        """Test case for post_stock_items

        Creates a Stock Item  # noqa: E501
        """
        pass

    def test_put_stock_items_key(self):
        """Test case for put_stock_items_key

        Updates a Stock Item  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
