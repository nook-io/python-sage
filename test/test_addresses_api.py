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
from sage.api.addresses_api import AddressesApi  # noqa: E501
from sage.rest import ApiException


class TestAddressesApi(unittest.TestCase):
    """AddressesApi unit test stubs"""

    def setUp(self):
        self.api = sage.api.addresses_api.AddressesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_addresses_key(self):
        """Test case for delete_addresses_key

        Deletes a Address  # noqa: E501
        """
        pass

    def test_get_addresses(self):
        """Test case for get_addresses

        Returns all Addresses  # noqa: E501
        """
        pass

    def test_get_addresses_key(self):
        """Test case for get_addresses_key

        Returns a Address  # noqa: E501
        """
        pass

    def test_post_addresses(self):
        """Test case for post_addresses

        Creates a Address  # noqa: E501
        """
        pass

    def test_put_addresses_key(self):
        """Test case for put_addresses_key

        Updates a Address  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
