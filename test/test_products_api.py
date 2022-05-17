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
from sage.api.products_api import ProductsApi  # noqa: E501
from sage.rest import ApiException


class TestProductsApi(unittest.TestCase):
    """ProductsApi unit test stubs"""

    def setUp(self):
        self.api = sage.api.products_api.ProductsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_products_key(self):
        """Test case for delete_products_key

        Deletes a Product  # noqa: E501
        """
        pass

    def test_get_products(self):
        """Test case for get_products

        Returns all Products  # noqa: E501
        """
        pass

    def test_get_products_key(self):
        """Test case for get_products_key

        Returns a Product  # noqa: E501
        """
        pass

    def test_post_products(self):
        """Test case for post_products

        Creates a Product  # noqa: E501
        """
        pass

    def test_put_products_key(self):
        """Test case for put_products_key

        Updates a Product  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
