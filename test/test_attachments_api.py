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
from sage.api.attachments_api import AttachmentsApi  # noqa: E501
from sage.rest import ApiException


class TestAttachmentsApi(unittest.TestCase):
    """AttachmentsApi unit test stubs"""

    def setUp(self):
        self.api = sage.api.attachments_api.AttachmentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_attachments_key(self):
        """Test case for delete_attachments_key

        Deletes a Attachment  # noqa: E501
        """
        pass

    def test_get_attachments(self):
        """Test case for get_attachments

        Returns all Attachments  # noqa: E501
        """
        pass

    def test_get_attachments_key(self):
        """Test case for get_attachments_key

        Returns a Attachment  # noqa: E501
        """
        pass

    def test_get_attachments_key_file(self):
        """Test case for get_attachments_key_file

        Returns an Attachment File  # noqa: E501
        """
        pass

    def test_post_attachments(self):
        """Test case for post_attachments

        Creates a Attachment  # noqa: E501
        """
        pass

    def test_put_attachments_key(self):
        """Test case for put_attachments_key

        Updates a Attachment  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()