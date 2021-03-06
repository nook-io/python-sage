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
from sage.api.sales_invoices_api import SalesInvoicesApi  # noqa: E501
from sage.rest import ApiException


class TestSalesInvoicesApi(unittest.TestCase):
    """SalesInvoicesApi unit test stubs"""

    def setUp(self):
        self.api = sage.api.sales_invoices_api.SalesInvoicesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_sales_invoices_key(self):
        """Test case for delete_sales_invoices_key

        Voids a Sales Invoice  # noqa: E501
        """
        pass

    def test_get_sales_invoices(self):
        """Test case for get_sales_invoices

        Returns all Sales Invoices  # noqa: E501
        """
        pass

    def test_get_sales_invoices_key(self):
        """Test case for get_sales_invoices_key

        Returns a Sales Invoice  # noqa: E501
        """
        pass

    def test_post_sales_invoices(self):
        """Test case for post_sales_invoices

        Creates a Sales Invoice  # noqa: E501
        """
        pass

    def test_post_sales_invoices_key_release(self):
        """Test case for post_sales_invoices_key_release

        Releases a Sales Invoice  # noqa: E501
        """
        pass

    def test_put_sales_invoices_key(self):
        """Test case for put_sales_invoices_key

        Updates a Sales Invoice  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
