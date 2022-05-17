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
from sage.api.contact_people_api import ContactPeopleApi  # noqa: E501
from sage.rest import ApiException


class TestContactPeopleApi(unittest.TestCase):
    """ContactPeopleApi unit test stubs"""

    def setUp(self):
        self.api = sage.api.contact_people_api.ContactPeopleApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_contact_persons_key(self):
        """Test case for delete_contact_persons_key

        Deletes a Contact Person  # noqa: E501
        """
        pass

    def test_get_contact_persons(self):
        """Test case for get_contact_persons

        Returns all Contact People  # noqa: E501
        """
        pass

    def test_get_contact_persons_key(self):
        """Test case for get_contact_persons_key

        Returns a Contact Person  # noqa: E501
        """
        pass

    def test_post_contact_persons(self):
        """Test case for post_contact_persons

        Creates a Contact Person  # noqa: E501
        """
        pass

    def test_put_contact_persons_key(self):
        """Test case for put_contact_persons_key

        Updates a Contact Person  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
