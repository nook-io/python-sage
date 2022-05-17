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
from sage.models.put_contact_persons_contact_person import PutContactPersonsContactPerson  # noqa: E501
from sage.rest import ApiException

class TestPutContactPersonsContactPerson(unittest.TestCase):
    """PutContactPersonsContactPerson unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PutContactPersonsContactPerson
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = sage.models.put_contact_persons_contact_person.PutContactPersonsContactPerson()  # noqa: E501
        if include_optional :
            return PutContactPersonsContactPerson(
                address_id = '0', 
                name = '0', 
                contact_person_type_ids = [
                    '0'
                    ], 
                job_title = '0', 
                telephone = '0', 
                mobile = '0', 
                email = '0', 
                fax = '0', 
                is_main_contact = True, 
                is_preferred_contact = True
            )
        else :
            return PutContactPersonsContactPerson(
        )

    def testPutContactPersonsContactPerson(self):
        """Test PutContactPersonsContactPerson"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
