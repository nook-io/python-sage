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
from sage.models.contact_opening_balance import ContactOpeningBalance  # noqa: E501
from sage.rest import ApiException

class TestContactOpeningBalance(unittest.TestCase):
    """ContactOpeningBalance unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ContactOpeningBalance
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = sage.models.contact_opening_balance.ContactOpeningBalance()  # noqa: E501
        if include_optional :
            return ContactOpeningBalance(
                id = '0', 
                displayed_as = '0', 
                path = '0', 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                transaction = sage.models.base.Base(
                    id = '0', 
                    displayed_as = '0', 
                    __path = '0', ), 
                transaction_type = sage.models.base.Base(
                    id = '0', 
                    displayed_as = '0', 
                    __path = '0', ), 
                deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                contact_opening_balance_type = sage.models.base.Base(
                    id = '0', 
                    displayed_as = '0', 
                    __path = '0', ), 
                contact = sage.models.base.Base(
                    id = '0', 
                    displayed_as = '0', 
                    __path = '0', ), 
                date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                reference = '0', 
                details = '0', 
                net_amount = 1.337, 
                tax_rate = sage.models.base.Base(
                    id = '0', 
                    displayed_as = '0', 
                    __path = '0', ), 
                tax_amount = 1.337, 
                tax_breakdown = [
                    sage.models.tax_breakdown.TaxBreakdown(
                        tax_rate = sage.models.base.Base(
                            id = '0', 
                            displayed_as = '0', 
                            __path = '0', ), 
                        percentage = 1.337, 
                        amount = 1.337, )
                    ], 
                total_amount = 1.337, 
                currency = sage.models.base.Base(
                    id = '0', 
                    displayed_as = '0', 
                    __path = '0', ), 
                exchange_rate = 1.337, 
                base_currency_net_amount = 1.337, 
                base_currency_tax_amount = 1.337, 
                base_currency_tax_breakdown = [
                    sage.models.tax_breakdown.TaxBreakdown(
                        tax_rate = sage.models.base.Base(
                            id = '0', 
                            displayed_as = '0', 
                            __path = '0', ), 
                        percentage = 1.337, 
                        amount = 1.337, )
                    ], 
                base_currency_total_amount = 1.337
            )
        else :
            return ContactOpeningBalance(
        )

    def testContactOpeningBalance(self):
        """Test ContactOpeningBalance"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()