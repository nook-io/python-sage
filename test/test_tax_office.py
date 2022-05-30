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
from sage.models.tax_office import TaxOffice  # noqa: E501
from sage.rest import ApiException

class TestTaxOffice(unittest.TestCase):
    """TaxOffice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TaxOffice
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = sage.models.tax_office.TaxOffice()  # noqa: E501
        if include_optional :
            return TaxOffice(
                id = '0', 
                displayed_as = '0', 
                path = '0', 
                office_number = '0', 
                name = '0'
            )
        else :
            return TaxOffice(
        )

    def testTaxOffice(self):
        """Test TaxOffice"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()