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
from sage.models.payment_allocation import PaymentAllocation  # noqa: E501
from sage.rest import ApiException

class TestPaymentAllocation(unittest.TestCase):
    """PaymentAllocation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaymentAllocation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = sage.models.payment_allocation.PaymentAllocation()  # noqa: E501
        if include_optional :
            return PaymentAllocation(
                links = [
                    sage.models.link.Link(
                        href = '0', 
                        rel = '0', 
                        type = '0', )
                    ], 
                date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                type = '0', 
                reference = '0', 
                amount = 1.337, 
                discount = 1.337, 
                stripe_transaction_id = '0', 
                contact_allocation = sage.models.contact_allocation.ContactAllocation(
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
                    contact = sage.models.base.Base(
                        id = '0', 
                        displayed_as = '0', 
                        __path = '0', ), 
                    allocated_artefacts = [
                        sage.models.allocated_artefact.AllocatedArtefact(
                            id = '0', 
                            artefact = sage.models.generic.Generic(
                                id = '0', 
                                displayed_as = '0', 
                                __path = '0', ), 
                            amount = 1.337, )
                        ], ), 
                artefact = sage.models.generic.Generic(
                    id = '0', 
                    displayed_as = '0', 
                    __path = '0', 
                    links = [
                        sage.models.link.Link(
                            href = '0', 
                            rel = '0', 
                            type = '0', )
                        ], ), 
                contact_payment = sage.models.contact_payment.ContactPayment(
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
                    transaction = sage.models.base.Base(
                        id = '0', 
                        displayed_as = '0', 
                        __path = '0', ), 
                    transaction_type = sage.models.base.Base(
                        id = '0', 
                        displayed_as = '0', 
                        __path = '0', ), 
                    deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    payment_method = sage.models.base.Base(
                        id = '0', 
                        displayed_as = '0', 
                        __path = '0', ), 
                    contact = sage.models.base.Base(
                        id = '0', 
                        displayed_as = '0', 
                        __path = '0', ), 
                    bank_account = sage.models.base.Base(
                        id = '0', 
                        displayed_as = '0', 
                        __path = '0', ), 
                    date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    net_amount = 1.337, 
                    tax_amount = 1.337, 
                    total_amount = 1.337, 
                    currency = sage.models.base.Base(
                        id = '0', 
                        displayed_as = '0', 
                        __path = '0', ), 
                    exchange_rate = 1.337, 
                    base_currency_net_amount = 1.337, 
                    base_currency_tax_amount = 1.337, 
                    base_currency_total_amount = 1.337, 
                    base_currency_currency_charge = 1.337, 
                    reference = '0', 
                    allocated_artefacts = [
                        sage.models.allocated_payment_artefact.AllocatedPaymentArtefact(
                            id = '0', 
                            artefact = sage.models.generic.Generic(
                                id = '0', 
                                displayed_as = '0', 
                                __path = '0', ), 
                            amount = 1.337, 
                            discount = 1.337, )
                        ], 
                    tax_rate = sage.models.base.Base(
                        id = '0', 
                        displayed_as = '0', 
                        __path = '0', ), 
                    payment_on_account = sage.models.payment_on_account.PaymentOnAccount(
                        id = '0', 
                        displayed_as = '0', 
                        __path = '0', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        contact_name = '0', 
                        contact_reference = '0', 
                        date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        reference = '0', 
                        net_amount = 1.337, 
                        tax_amount = 1.337, 
                        total_amount = 1.337, 
                        outstanding_amount = 1.337, 
                        exchange_rate = 1.337, 
                        base_currency_net_amount = 1.337, 
                        base_currency_tax_amount = 1.337, 
                        base_currency_total_amount = 1.337, 
                        base_currency_outstanding_amount = 1.337, 
                        status = sage.models.base.Base(
                            id = '0', 
                            displayed_as = '0', 
                            __path = '0', ), ), 
                    editable = True, ), 
                displayed_as = '0', 
                negative_payment = True
            )
        else :
            return PaymentAllocation(
        )

    def testPaymentAllocation(self):
        """Test PaymentAllocation"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
