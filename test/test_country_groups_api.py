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
from sage.api.country_groups_api import CountryGroupsApi  # noqa: E501
from sage.rest import ApiException


class TestCountryGroupsApi(unittest.TestCase):
    """CountryGroupsApi unit test stubs"""

    def setUp(self):
        self.api = sage.api.country_groups_api.CountryGroupsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_country_groups(self):
        """Test case for get_country_groups

        Returns all Country Groups  # noqa: E501
        """
        pass

    def test_get_country_groups_key(self):
        """Test case for get_country_groups_key

        Returns a Country Group  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
