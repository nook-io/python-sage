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
from sage.models.post_migration_tax_returns import PostMigrationTaxReturns  # noqa: E501
from sage.rest import ApiException

class TestPostMigrationTaxReturns(unittest.TestCase):
    """PostMigrationTaxReturns unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PostMigrationTaxReturns
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = sage.models.post_migration_tax_returns.PostMigrationTaxReturns()  # noqa: E501
        if include_optional :
            return PostMigrationTaxReturns(
                migration_tax_return = sage.models.post_migration_tax_returns_migration_tax_return.postMigrationTaxReturns_migration_tax_return(
                    from_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    to_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    total_amount = 1.337, 
                    tax_return_frequency_id = '0', 
                    gb = sage.models.post_migration_tax_returns_migration_tax_return_gb.postMigrationTaxReturns_migration_tax_return_gb(
                        box_1 = 1.337, 
                        box_2 = 1.337, 
                        box_3 = 1.337, 
                        box_4 = 1.337, 
                        box_5 = 1.337, 
                        box_6 = 1.337, 
                        box_7 = 1.337, 
                        box_8 = 1.337, 
                        box_9 = 1.337, ), 
                    ie = sage.models.post_migration_tax_returns_migration_tax_return_ie.postMigrationTaxReturns_migration_tax_return_ie(
                        box_t1 = 1.337, 
                        box_t2 = 1.337, 
                        box_t3 = 1.337, 
                        box_t4 = 1.337, 
                        box_e1 = 1.337, 
                        box_e2 = 1.337, 
                        box_es1 = 1.337, 
                        box_es2 = 1.337, ), )
            )
        else :
            return PostMigrationTaxReturns(
                migration_tax_return = sage.models.post_migration_tax_returns_migration_tax_return.postMigrationTaxReturns_migration_tax_return(
                    from_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    to_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    total_amount = 1.337, 
                    tax_return_frequency_id = '0', 
                    gb = sage.models.post_migration_tax_returns_migration_tax_return_gb.postMigrationTaxReturns_migration_tax_return_gb(
                        box_1 = 1.337, 
                        box_2 = 1.337, 
                        box_3 = 1.337, 
                        box_4 = 1.337, 
                        box_5 = 1.337, 
                        box_6 = 1.337, 
                        box_7 = 1.337, 
                        box_8 = 1.337, 
                        box_9 = 1.337, ), 
                    ie = sage.models.post_migration_tax_returns_migration_tax_return_ie.postMigrationTaxReturns_migration_tax_return_ie(
                        box_t1 = 1.337, 
                        box_t2 = 1.337, 
                        box_t3 = 1.337, 
                        box_t4 = 1.337, 
                        box_e1 = 1.337, 
                        box_e2 = 1.337, 
                        box_es1 = 1.337, 
                        box_es2 = 1.337, ), ),
        )

    def testPostMigrationTaxReturns(self):
        """Test PostMigrationTaxReturns"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
