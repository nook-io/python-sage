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
from sage.models.post_contacts_contact_main_contact_person import PostContactsContactMainContactPerson  # noqa: E501
from sage.rest import ApiException

class TestPostContactsContactMainContactPerson(unittest.TestCase):
    """PostContactsContactMainContactPerson unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PostContactsContactMainContactPerson
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = sage.models.post_contacts_contact_main_contact_person.PostContactsContactMainContactPerson()  # noqa: E501
        if include_optional :
            return PostContactsContactMainContactPerson(
                contact_person_type_ids = [
                    '0'
                    ], 
                name = '0', 
                job_title = '0', 
                telephone = '0', 
                mobile = '0', 
                email = '0', 
                fax = '0', 
                is_main_contact = True, 
                address_id = '0', 
                is_preferred_contact = True
            )
        else :
            return PostContactsContactMainContactPerson(
        )

    def testPostContactsContactMainContactPerson(self):
        """Test PostContactsContactMainContactPerson"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
