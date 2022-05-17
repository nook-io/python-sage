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
from sage.models.opening_balance_journal import OpeningBalanceJournal  # noqa: E501
from sage.rest import ApiException

class TestOpeningBalanceJournal(unittest.TestCase):
    """OpeningBalanceJournal unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OpeningBalanceJournal
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = sage.models.opening_balance_journal.OpeningBalanceJournal()  # noqa: E501
        if include_optional :
            return OpeningBalanceJournal(
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
                date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                reference = '0', 
                journal_lines = [
                    sage.models.base_journal_line.BaseJournalLine(
                        id = '0', 
                        ledger_account = sage.models.ledger_account.LedgerAccount(
                            id = '0', 
                            displayed_as = '0', 
                            __path = '0', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            ledger_account_group = sage.models.coa_group_type.CoaGroupType(
                                id = '0', 
                                displayed_as = '0', ), 
                            name = '0', 
                            display_name = '0', 
                            visible_scopes = [
                                '0'
                                ], 
                            included_in_chart = True, 
                            nominal_code = 56, 
                            ledger_account_type = sage.models.base.Base(
                                id = '0', 
                                displayed_as = '0', 
                                __path = '0', ), 
                            ledger_account_classification = sage.models.base.Base(
                                id = '0', 
                                displayed_as = '0', 
                                __path = '0', ), 
                            tax_rate = sage.models.base.Base(
                                id = '0', 
                                displayed_as = '0', 
                                __path = '0', ), 
                            fixed_tax_rate = True, 
                            visible_in_banking = True, 
                            visible_in_expenses = True, 
                            visible_in_journals = True, 
                            visible_in_other_payments = True, 
                            visible_in_other_receipts = True, 
                            visible_in_reporting = True, 
                            visible_in_sales = True, 
                            balance_details = sage.models.ledger_account_balance_details.LedgerAccountBalanceDetails(
                                balance = 1.337, 
                                credit_or_debit = '0', 
                                credits = 1.337, 
                                debits = 1.337, 
                                from_date = '0', 
                                to_date = '0', ), 
                            is_control_account = True, 
                            control_name = '0', 
                            display_formatted = '0', 
                            tax_recoverable = True, 
                            recoverable_percentage = 1.337, 
                            non_recoverable_ledger_account = sage.models.ledger_account.LedgerAccount(
                                id = '0', 
                                displayed_as = '0', 
                                __path = '0', 
                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                name = '0', 
                                display_name = '0', 
                                included_in_chart = True, 
                                nominal_code = 56, 
                                fixed_tax_rate = True, 
                                visible_in_banking = True, 
                                visible_in_expenses = True, 
                                visible_in_journals = True, 
                                visible_in_other_payments = True, 
                                visible_in_other_receipts = True, 
                                visible_in_reporting = True, 
                                visible_in_sales = True, 
                                is_control_account = True, 
                                control_name = '0', 
                                display_formatted = '0', 
                                tax_recoverable = True, 
                                recoverable_percentage = 1.337, 
                                cis_materials = True, 
                                tax_instalment = True, 
                                cis_labour = True, 
                                gifi_code = 56, ), 
                            cis_materials = True, 
                            tax_instalment = True, 
                            cis_labour = True, 
                            gifi_code = 56, ), 
                        details = '0', 
                        debit = 1.337, 
                        credit = 1.337, )
                    ]
            )
        else :
            return OpeningBalanceJournal(
        )

    def testOpeningBalanceJournal(self):
        """Test OpeningBalanceJournal"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
