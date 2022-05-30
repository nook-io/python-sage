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
from sage.api.journal_codes_api import JournalCodesApi  # noqa: E501
from sage.rest import ApiException


class TestJournalCodesApi(unittest.TestCase):
    """JournalCodesApi unit test stubs"""

    def setUp(self):
        self.api = sage.api.journal_codes_api.JournalCodesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_journal_codes_key(self):
        """Test case for delete_journal_codes_key

        Deletes a Journal Code  # noqa: E501
        """
        pass

    def test_get_journal_codes(self):
        """Test case for get_journal_codes

        Returns all Journal Codes  # noqa: E501
        """
        pass

    def test_get_journal_codes_key(self):
        """Test case for get_journal_codes_key

        Returns a Journal Code  # noqa: E501
        """
        pass

    def test_post_journal_codes(self):
        """Test case for post_journal_codes

        Creates a Journal Code  # noqa: E501
        """
        pass

    def test_put_journal_codes_key(self):
        """Test case for put_journal_codes_key

        Updates a Journal Code  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()