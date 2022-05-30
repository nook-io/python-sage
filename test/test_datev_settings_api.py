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
from sage.api.datev_settings_api import DatevSettingsApi  # noqa: E501
from sage.rest import ApiException


class TestDatevSettingsApi(unittest.TestCase):
    """DatevSettingsApi unit test stubs"""

    def setUp(self):
        self.api = sage.api.datev_settings_api.DatevSettingsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_datev_settings(self):
        """Test case for get_datev_settings

        Returns all Datev Settings  # noqa: E501
        """
        pass

    def test_put_datev_settings(self):
        """Test case for put_datev_settings

        Updates a Datev Settings  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()