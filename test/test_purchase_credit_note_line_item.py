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
from sage.models.purchase_credit_note_line_item import PurchaseCreditNoteLineItem  # noqa: E501
from sage.rest import ApiException

class TestPurchaseCreditNoteLineItem(unittest.TestCase):
    """PurchaseCreditNoteLineItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PurchaseCreditNoteLineItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = sage.models.purchase_credit_note_line_item.PurchaseCreditNoteLineItem()  # noqa: E501
        if include_optional :
            return PurchaseCreditNoteLineItem(
                id = '0', 
                displayed_as = '0', 
                is_purchase_for_resale = True, 
                description = '0', 
                product = sage.models.product.Product(
                    id = '0', 
                    displayed_as = '0', 
                    __path = '0', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    deletable = True, 
                    deactivatable = True, 
                    used_on_recurring_invoice = True, 
                    item_code = '0', 
                    description = '0', 
                    notes = '0', 
                    sales_ledger_account = sage.models.base.Base(
                        id = '0', 
                        displayed_as = '0', 
                        __path = '0', ), 
                    sales_tax_rate = sage.models.base.Base(
                        id = '0', 
                        displayed_as = '0', 
                        __path = '0', ), 
                    purchase_ledger_account = sage.models.base.Base(
                        id = '0', 
                        displayed_as = '0', 
                        __path = '0', ), 
                    usual_supplier = sage.models.contact.Contact(
                        id = '0', 
                        displayed_as = '0', 
                        __path = '0', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        links = [
                            sage.models.link.Link(
                                href = '0', 
                                rel = '0', 
                                type = '0', )
                            ], 
                        deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        balance = 1.337, 
                        contact_types = [
                            sage.models.base.Base(
                                id = '0', 
                                displayed_as = '0', 
                                __path = '0', )
                            ], 
                        name = '0', 
                        reference = '0', 
                        default_sales_ledger_account = sage.models.ledger_account.LedgerAccount(
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
                        default_sales_tax_rate = sage.models.base.Base(
                            id = '0', 
                            displayed_as = '0', 
                            __path = '0', ), 
                        default_purchase_ledger_account = sage.models.ledger_account.LedgerAccount(
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
                        tax_number = '0', 
                        notes = '0', 
                        locale = '0', 
                        main_address = sage.models.address.Address(
                            id = '0', 
                            displayed_as = '0', 
                            __path = '0', 
                            address_line_1 = '0', 
                            address_line_2 = '0', 
                            city = '0', 
                            postal_code = '0', 
                            country = sage.models.base.Base(
                                id = '0', 
                                displayed_as = '0', 
                                __path = '0', ), 
                            deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            bank_account = sage.models.base.Base(
                                id = '0', 
                                displayed_as = '0', 
                                __path = '0', ), 
                            contact = sage.models.base.Base(
                                id = '0', 
                                displayed_as = '0', 
                                __path = '0', ), 
                            address_type = sage.models.base.Base(
                                id = '0', 
                                displayed_as = '0', 
                                __path = '0', ), 
                            name = '0', 
                            region = '0', 
                            country_group = sage.models.base.Base(
                                id = '0', 
                                displayed_as = '0', 
                                __path = '0', ), 
                            is_main_address = True, ), 
                        delivery_address = sage.models.address.Address(
                            id = '0', 
                            displayed_as = '0', 
                            __path = '0', 
                            address_line_1 = '0', 
                            address_line_2 = '0', 
                            city = '0', 
                            postal_code = '0', 
                            deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            name = '0', 
                            region = '0', 
                            is_main_address = True, ), 
                        main_contact_person = sage.models.contact_person.ContactPerson(
                            id = '0', 
                            displayed_as = '0', 
                            __path = '0', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            contact_person_types = [
                                sage.models.contact_person_type.ContactPersonType(
                                    id = '0', 
                                    displayed_as = '0', 
                                    __path = '0', )
                                ], 
                            name = '0', 
                            job_title = '0', 
                            telephone = '0', 
                            mobile = '0', 
                            email = '0', 
                            fax = '0', 
                            is_main_contact = True, 
                            address = sage.models.base.Base(
                                id = '0', 
                                displayed_as = '0', 
                                __path = '0', ), 
                            is_preferred_contact = True, ), 
                        bank_account_details = sage.models.bank_account_details.BankAccountDetails(
                            account_name = '0', 
                            account_number = '0', 
                            sort_code = '0', 
                            bic = '0', 
                            iban = '0', ), 
                        credit_limit = 1.337, 
                        credit_days = 56, 
                        credit_terms_and_conditions = '0', 
                        product_sales_price_type = sage.models.base.Base(
                            id = '0', 
                            displayed_as = '0', 
                            __path = '0', ), 
                        source_guid = '0', 
                        currency = sage.models.base.Base(
                            id = '0', 
                            displayed_as = '0', 
                            __path = '0', ), 
                        aux_reference = '0', 
                        registered_number = '0', 
                        deletable = True, 
                        tax_treatment = sage.models.contact_tax_treatment.ContactTaxTreatment(
                            home_tax = True, 
                            eu_tax_registered = True, 
                            eu_not_tax_registered = True, 
                            rest_of_world_tax = True, 
                            is_importer = True, ), 
                        email = '0', 
                        tax_calculation = '0', 
                        auxiliary_account = '0', 
                        gdpr_obfuscated = True, 
                        system = True, 
                        has_unfinished_recurring_invoices = True, 
                        cis_registered = True, 
                        ni_based = True, 
                        cis_settings = sage.models.contact_cis_settings.ContactCisSettings(
                            registered_cis_name = '0', 
                            subcontractor_verification_number = '0', 
                            deduction_rate = sage.models.contact_cis_deduction_rate.ContactCisDeductionRate(
                                id = '0', 
                                displayed_as = '0', 
                                __path = '0', ), ), ), 
                    purchase_tax_rate = sage.models.base.Base(
                        id = '0', 
                        displayed_as = '0', 
                        __path = '0', ), 
                    cost_price = 1.337, 
                    sales_prices = [
                        sage.models.sales_price.SalesPrice(
                            id = '0', 
                            displayed_as = '0', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            price_name = '0', 
                            price = 1.337, 
                            price_includes_tax = True, )
                        ], 
                    source_guid = '0', 
                    purchase_description = '0', 
                    active = True, 
                    catalog_item_type = sage.models.base.Base(
                        id = '0', 
                        displayed_as = '0', 
                        __path = '0', ), ), 
                service = sage.models.service.Service(
                    id = '0', 
                    displayed_as = '0', 
                    __path = '0', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    deletable = True, 
                    deactivatable = True, 
                    used_on_recurring_invoice = True, 
                    item_code = '0', 
                    description = '0', 
                    notes = '0', 
                    sales_ledger_account = sage.models.base.Base(
                        id = '0', 
                        displayed_as = '0', 
                        __path = '0', ), 
                    purchase_ledger_account = sage.models.base.Base(
                        id = '0', 
                        displayed_as = '0', 
                        __path = '0', ), 
                    sales_tax_rate = sage.models.base.Base(
                        id = '0', 
                        displayed_as = '0', 
                        __path = '0', ), 
                    purchase_tax_rate = sage.models.base.Base(
                        id = '0', 
                        displayed_as = '0', 
                        __path = '0', ), 
                    sales_rates = [
                        sage.models.rate.Rate(
                            id = '0', 
                            displayed_as = '0', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            rate_name = '0', 
                            rate = 1.337, 
                            rate_includes_tax = True, 
                            service_rate_type = sage.models.base.Base(
                                id = '0', 
                                displayed_as = '0', 
                                __path = '0', ), )
                        ], 
                    source_guid = '0', 
                    purchase_description = '0', 
                    usual_supplier = sage.models.contact.Contact(
                        id = '0', 
                        displayed_as = '0', 
                        __path = '0', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        links = [
                            sage.models.link.Link(
                                href = '0', 
                                rel = '0', 
                                type = '0', )
                            ], 
                        deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        balance = 1.337, 
                        contact_types = [
                            sage.models.base.Base(
                                id = '0', 
                                displayed_as = '0', 
                                __path = '0', )
                            ], 
                        name = '0', 
                        reference = '0', 
                        default_sales_ledger_account = sage.models.ledger_account.LedgerAccount(
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
                        default_sales_tax_rate = sage.models.base.Base(
                            id = '0', 
                            displayed_as = '0', 
                            __path = '0', ), 
                        default_purchase_ledger_account = sage.models.ledger_account.LedgerAccount(
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
                        tax_number = '0', 
                        notes = '0', 
                        locale = '0', 
                        main_address = sage.models.address.Address(
                            id = '0', 
                            displayed_as = '0', 
                            __path = '0', 
                            address_line_1 = '0', 
                            address_line_2 = '0', 
                            city = '0', 
                            postal_code = '0', 
                            country = sage.models.base.Base(
                                id = '0', 
                                displayed_as = '0', 
                                __path = '0', ), 
                            deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            bank_account = sage.models.base.Base(
                                id = '0', 
                                displayed_as = '0', 
                                __path = '0', ), 
                            contact = sage.models.base.Base(
                                id = '0', 
                                displayed_as = '0', 
                                __path = '0', ), 
                            address_type = sage.models.base.Base(
                                id = '0', 
                                displayed_as = '0', 
                                __path = '0', ), 
                            name = '0', 
                            region = '0', 
                            country_group = sage.models.base.Base(
                                id = '0', 
                                displayed_as = '0', 
                                __path = '0', ), 
                            is_main_address = True, ), 
                        delivery_address = sage.models.address.Address(
                            id = '0', 
                            displayed_as = '0', 
                            __path = '0', 
                            address_line_1 = '0', 
                            address_line_2 = '0', 
                            city = '0', 
                            postal_code = '0', 
                            deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            name = '0', 
                            region = '0', 
                            is_main_address = True, ), 
                        main_contact_person = sage.models.contact_person.ContactPerson(
                            id = '0', 
                            displayed_as = '0', 
                            __path = '0', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            contact_person_types = [
                                sage.models.contact_person_type.ContactPersonType(
                                    id = '0', 
                                    displayed_as = '0', 
                                    __path = '0', )
                                ], 
                            name = '0', 
                            job_title = '0', 
                            telephone = '0', 
                            mobile = '0', 
                            email = '0', 
                            fax = '0', 
                            is_main_contact = True, 
                            address = sage.models.base.Base(
                                id = '0', 
                                displayed_as = '0', 
                                __path = '0', ), 
                            is_preferred_contact = True, ), 
                        bank_account_details = sage.models.bank_account_details.BankAccountDetails(
                            account_name = '0', 
                            account_number = '0', 
                            sort_code = '0', 
                            bic = '0', 
                            iban = '0', ), 
                        credit_limit = 1.337, 
                        credit_days = 56, 
                        credit_terms_and_conditions = '0', 
                        product_sales_price_type = sage.models.base.Base(
                            id = '0', 
                            displayed_as = '0', 
                            __path = '0', ), 
                        source_guid = '0', 
                        currency = sage.models.base.Base(
                            id = '0', 
                            displayed_as = '0', 
                            __path = '0', ), 
                        aux_reference = '0', 
                        registered_number = '0', 
                        deletable = True, 
                        tax_treatment = sage.models.contact_tax_treatment.ContactTaxTreatment(
                            home_tax = True, 
                            eu_tax_registered = True, 
                            eu_not_tax_registered = True, 
                            rest_of_world_tax = True, 
                            is_importer = True, ), 
                        email = '0', 
                        tax_calculation = '0', 
                        auxiliary_account = '0', 
                        gdpr_obfuscated = True, 
                        system = True, 
                        has_unfinished_recurring_invoices = True, 
                        cis_registered = True, 
                        ni_based = True, 
                        cis_settings = sage.models.contact_cis_settings.ContactCisSettings(
                            registered_cis_name = '0', 
                            subcontractor_verification_number = '0', 
                            deduction_rate = sage.models.contact_cis_deduction_rate.ContactCisDeductionRate(
                                id = '0', 
                                displayed_as = '0', 
                                __path = '0', ), ), ), 
                    active = True, 
                    cost_price = 1.337, ), 
                ledger_account = sage.models.base.Base(
                    id = '0', 
                    displayed_as = '0', 
                    __path = '0', ), 
                trade_of_asset = True, 
                quantity = 1.337, 
                unit_price = 1.337, 
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
                base_currency_unit_price = 1.337, 
                unit_price_includes_tax = True, 
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
                base_currency_total_amount = 1.337, 
                eu_goods_services_type = sage.models.base.Base(
                    id = '0', 
                    displayed_as = '0', 
                    __path = '0', ), 
                gst_amount = 1.337, 
                pst_amount = 1.337, 
                tax_recoverable = True
            )
        else :
            return PurchaseCreditNoteLineItem(
        )

    def testPurchaseCreditNoteLineItem(self):
        """Test PurchaseCreditNoteLineItem"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
