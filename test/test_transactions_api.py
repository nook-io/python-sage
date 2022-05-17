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
from sage.api.transactions_api import TransactionsApi  # noqa: E501
from sage.rest import ApiException


class TestTransactionsApi(unittest.TestCase):
    """TransactionsApi unit test stubs"""

    def setUp(self):
        self.api = sage.api.transactions_api.TransactionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_transactions(self):
        """Test case for get_transactions

        Returns all Transactions  # noqa: E501
        """
        pass

    def test_get_transactions_key(self):
        """Test case for get_transactions_key

        Returns a Transaction  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
