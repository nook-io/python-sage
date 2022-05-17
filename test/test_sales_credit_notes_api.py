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
from sage.api.sales_credit_notes_api import SalesCreditNotesApi  # noqa: E501
from sage.rest import ApiException


class TestSalesCreditNotesApi(unittest.TestCase):
    """SalesCreditNotesApi unit test stubs"""

    def setUp(self):
        self.api = sage.api.sales_credit_notes_api.SalesCreditNotesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_sales_credit_notes_key(self):
        """Test case for delete_sales_credit_notes_key

        Voids a Sales Credit Note  # noqa: E501
        """
        pass

    def test_get_sales_credit_notes(self):
        """Test case for get_sales_credit_notes

        Returns all Sales Credit Notes  # noqa: E501
        """
        pass

    def test_get_sales_credit_notes_key(self):
        """Test case for get_sales_credit_notes_key

        Returns a Sales Credit Note  # noqa: E501
        """
        pass

    def test_post_sales_credit_notes(self):
        """Test case for post_sales_credit_notes

        Creates a Sales Credit Note  # noqa: E501
        """
        pass

    def test_post_sales_credit_notes_key_release(self):
        """Test case for post_sales_credit_notes_key_release

        Releases a Sales Credit Note  # noqa: E501
        """
        pass

    def test_put_sales_credit_notes_key(self):
        """Test case for put_sales_credit_notes_key

        Updates a Sales Credit Note  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
