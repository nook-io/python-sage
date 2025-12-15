import pprint
import six
from sage.configuration import Configuration


class PaymentAllocation(object):
    openapi_types = {
        "links": "list[Link]",
        "date": "date",
        "type": "str",
        "reference": "str",
        "amount": "float",
        "discount": "float",
        "stripe_transaction_id": "str",
        "contact_allocation": "ContactAllocation",
        "artefact": "Generic",
        "contact_payment": "ContactPayment",
        "displayed_as": "str",
        "negative_payment": "bool",
    }
    attribute_map = {
        "links": "links",
        "date": "date",
        "type": "type",
        "reference": "reference",
        "amount": "amount",
        "discount": "discount",
        "stripe_transaction_id": "stripe_transaction_id",
        "contact_allocation": "contact_allocation",
        "artefact": "artefact",
        "contact_payment": "contact_payment",
        "displayed_as": "displayed_as",
        "negative_payment": "negative_payment",
    }

    def __init__(
        self,
        links=None,
        date=None,
        type=None,
        reference=None,
        amount=None,
        discount=None,
        stripe_transaction_id=None,
        contact_allocation=None,
        artefact=None,
        contact_payment=None,
        displayed_as=None,
        negative_payment=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._links = None
        self._date = None
        self._type = None
        self._reference = None
        self._amount = None
        self._discount = None
        self._stripe_transaction_id = None
        self._contact_allocation = None
        self._artefact = None
        self._contact_payment = None
        self._displayed_as = None
        self._negative_payment = None
        self.discriminator = None
        if links is not None:
            self.links = links
        if date is not None:
            self.date = date
        if type is not None:
            self.type = type
        if reference is not None:
            self.reference = reference
        if amount is not None:
            self.amount = amount
        if discount is not None:
            self.discount = discount
        if stripe_transaction_id is not None:
            self.stripe_transaction_id = stripe_transaction_id
        if contact_allocation is not None:
            self.contact_allocation = contact_allocation
        if artefact is not None:
            self.artefact = artefact
        if contact_payment is not None:
            self.contact_payment = contact_payment
        if displayed_as is not None:
            self.displayed_as = displayed_as
        if negative_payment is not None:
            self.negative_payment = negative_payment

    @property
    def links(self):
        return self._links

    @links.setter
    def links(self, links):
        self._links = links

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type

    @property
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, reference):
        self._reference = reference

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount):
        self._discount = discount

    @property
    def stripe_transaction_id(self):
        return self._stripe_transaction_id

    @stripe_transaction_id.setter
    def stripe_transaction_id(self, stripe_transaction_id):
        self._stripe_transaction_id = stripe_transaction_id

    @property
    def contact_allocation(self):
        return self._contact_allocation

    @contact_allocation.setter
    def contact_allocation(self, contact_allocation):
        self._contact_allocation = contact_allocation

    @property
    def artefact(self):
        return self._artefact

    @artefact.setter
    def artefact(self, artefact):
        self._artefact = artefact

    @property
    def contact_payment(self):
        return self._contact_payment

    @contact_payment.setter
    def contact_payment(self, contact_payment):
        self._contact_payment = contact_payment

    @property
    def displayed_as(self):
        return self._displayed_as

    @displayed_as.setter
    def displayed_as(self, displayed_as):
        self._displayed_as = displayed_as

    @property
    def negative_payment(self):
        return self._negative_payment

    @negative_payment.setter
    def negative_payment(self, negative_payment):
        self._negative_payment = negative_payment

    def to_dict(self):
        result = {}
        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, PaymentAllocation):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PaymentAllocation):
            return True
        return self.to_dict() != other.to_dict()
