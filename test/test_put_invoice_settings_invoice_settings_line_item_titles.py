# coding: utf-8

"""
    Sage Business Cloud Accounting - Accounts

    Documentation of the Sage Business Cloud Accounting API.  # noqa: E501

    The version of the OpenAPI document: 3.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import sage
from sage.models.put_invoice_settings_invoice_settings_line_item_titles import PutInvoiceSettingsInvoiceSettingsLineItemTitles  # noqa: E501
from sage.rest import ApiException

class TestPutInvoiceSettingsInvoiceSettingsLineItemTitles(unittest.TestCase):
    """PutInvoiceSettingsInvoiceSettingsLineItemTitles unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PutInvoiceSettingsInvoiceSettingsLineItemTitles
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = sage.models.put_invoice_settings_invoice_settings_line_item_titles.PutInvoiceSettingsInvoiceSettingsLineItemTitles()  # noqa: E501
        if include_optional :
            return PutInvoiceSettingsInvoiceSettingsLineItemTitles(
                description = '0', 
                unit_price = '0', 
                quantity = '0', 
                discount = '0'
            )
        else :
            return PutInvoiceSettingsInvoiceSettingsLineItemTitles(
        )

    def testPutInvoiceSettingsInvoiceSettingsLineItemTitles(self):
        """Test PutInvoiceSettingsInvoiceSettingsLineItemTitles"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
