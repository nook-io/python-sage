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
from sage.api.stock_movements_api import StockMovementsApi  # noqa: E501
from sage.rest import ApiException


class TestStockMovementsApi(unittest.TestCase):
    """StockMovementsApi unit test stubs"""

    def setUp(self):
        self.api = sage.api.stock_movements_api.StockMovementsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_stock_movements_key(self):
        """Test case for delete_stock_movements_key

        Deletes a Stock Movement  # noqa: E501
        """
        pass

    def test_get_stock_movements(self):
        """Test case for get_stock_movements

        Returns all Stock Movements  # noqa: E501
        """
        pass

    def test_get_stock_movements_key(self):
        """Test case for get_stock_movements_key

        Returns a Stock Movement  # noqa: E501
        """
        pass

    def test_post_stock_movements(self):
        """Test case for post_stock_movements

        Creates a Stock Movement  # noqa: E501
        """
        pass

    def test_put_stock_movements_key(self):
        """Test case for put_stock_movements_key

        Updates a Stock Movement  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
