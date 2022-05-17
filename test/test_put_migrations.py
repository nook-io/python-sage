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
from sage.models.put_migrations import PutMigrations  # noqa: E501
from sage.rest import ApiException

class TestPutMigrations(unittest.TestCase):
    """PutMigrations unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PutMigrations
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = sage.models.put_migrations.PutMigrations()  # noqa: E501
        if include_optional :
            return PutMigrations(
                migrations = sage.models.put_migrations_migrations.putMigrations_migrations(
                    status_id = '0', 
                    started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    completed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    source_product = '0', 
                    source_product_version = '0', 
                    source_license = '0', 
                    source_tool = '0', 
                    source_tool_version = '0', 
                    schema_id = '0', )
            )
        else :
            return PutMigrations(
                migrations = sage.models.put_migrations_migrations.putMigrations_migrations(
                    status_id = '0', 
                    started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    completed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    source_product = '0', 
                    source_product_version = '0', 
                    source_license = '0', 
                    source_tool = '0', 
                    source_tool_version = '0', 
                    schema_id = '0', ),
        )

    def testPutMigrations(self):
        """Test PutMigrations"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
