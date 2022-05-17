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
from sage.models.financial_settings import FinancialSettings  # noqa: E501
from sage.rest import ApiException

class TestFinancialSettings(unittest.TestCase):
    """FinancialSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FinancialSettings
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = sage.models.financial_settings.FinancialSettings()  # noqa: E501
        if include_optional :
            return FinancialSettings(
                path = '0', 
                year_end_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                year_end_lockdown_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                accounting_type = '0', 
                accounts_start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                base_currency = sage.models.base.Base(
                    id = '0', 
                    displayed_as = '0', 
                    __path = '0', ), 
                multi_currency_enabled = True, 
                use_live_exchange_rates = True, 
                mtd_activation_status = '0', 
                mtd_connected = True, 
                mtd_authenticated_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                tax_scheme = sage.models.tax_scheme.TaxScheme(
                    id = '0', 
                    displayed_as = '0', 
                    __path = '0', ), 
                tax_return_frequency = sage.models.base.Base(
                    id = '0', 
                    displayed_as = '0', 
                    __path = '0', ), 
                tax_number = '0', 
                general_tax_number = '0', 
                tax_office = sage.models.base.Base(
                    id = '0', 
                    displayed_as = '0', 
                    __path = '0', ), 
                default_irpf_rate = 1.337, 
                flat_rate_tax_percentage = 1.337, 
                recoverable_percentage = 1.337, 
                sales_tax_calculation = '0', 
                purchase_tax_calculation = '0', 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return FinancialSettings(
        )

    def testFinancialSettings(self):
        """Test FinancialSettings"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
