import pprint

import six

from sage.configuration import Configuration


class ContactPaymentPush(object):
    openapi_types = {
        "id": "str",
        "displayed_as": "str",
        "path": "str",
        "created_at": "datetime",
        "updated_at": "datetime",
        "links": "list[Link]",
        "transaction": "Base",
        "transaction_type_id": "str",
        "deleted_at": "datetime",
        "payment_method_id": "str",
        "contact_id": "str",
        "bank_account_id": "str",
        "date": "date",
        "net_amount": "float",
        "tax_amount": "float",
        "total_amount": "float",
        "currency_id": "str",
        "exchange_rate": "float",
        "base_currency_net_amount": "float",
        "base_currency_tax_amount": "float",
        "base_currency_total_amount": "float",
        "base_currency_currency_charge": "float",
        "reference": "str",
        "allocated_artefacts": "list[AllocatedPaymentArtefact]",
        "tax_rate_id": "str",
        "payment_on_account": "PaymentOnAccount",
        "editable": "bool",
    }
    attribute_map = {
        "id": "id",
        "displayed_as": "displayed_as",
        "path": "$path",
        "created_at": "created_at",
        "updated_at": "updated_at",
        "links": "links",
        "transaction": "transaction",
        "transaction_type_id": "transaction_type_id",
        "deleted_at": "deleted_at",
        "payment_method_id": "payment_method_id",
        "contact_id": "contact_id",
        "bank_account_id": "bank_account_id",
        "date": "date",
        "net_amount": "net_amount",
        "tax_amount": "tax_amount",
        "total_amount": "total_amount",
        "currency_id": "currency_id",
        "exchange_rate": "exchange_rate",
        "base_currency_net_amount": "base_currency_net_amount",
        "base_currency_tax_amount": "base_currency_tax_amount",
        "base_currency_total_amount": "base_currency_total_amount",
        "base_currency_currency_charge": "base_currency_currency_charge",
        "reference": "reference",
        "allocated_artefacts": "allocated_artefacts",
        "tax_rate_id": "tax_rate_id",
        "payment_on_account": "payment_on_account",
        "editable": "editable",
    }

    def __init__(
        self,
        id=None,
        displayed_as=None,
        path=None,
        created_at=None,
        updated_at=None,
        links=None,
        transaction=None,
        transaction_type_id=None,
        deleted_at=None,
        payment_method_id=None,
        contact_id=None,
        bank_account_id=None,
        date=None,
        net_amount=None,
        tax_amount=None,
        total_amount=None,
        currency_id=None,
        exchange_rate=None,
        base_currency_net_amount=None,
        base_currency_tax_amount=None,
        base_currency_total_amount=None,
        base_currency_currency_charge=None,
        reference=None,
        allocated_artefacts=None,
        tax_rate_id=None,
        payment_on_account=None,
        editable=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._id = None
        self._displayed_as = None
        self._path = None
        self._created_at = None
        self._updated_at = None
        self._links = None
        self._transaction = None
        self._transaction_type_id = None
        self._deleted_at = None
        self._payment_method_id = None
        self._contact_id = None
        self._bank_account_id = None
        self._date = None
        self._net_amount = None
        self._tax_amount = None
        self._total_amount = None
        self._currency_id = None
        self._exchange_rate = None
        self._base_currency_net_amount = None
        self._base_currency_tax_amount = None
        self._base_currency_total_amount = None
        self._base_currency_currency_charge = None
        self._reference = None
        self._allocated_artefacts = None
        self._tax_rate_id = None
        self._payment_on_account = None
        self._editable = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if displayed_as is not None:
            self.displayed_as = displayed_as
        if path is not None:
            self.path = path
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if links is not None:
            self.links = links
        if transaction is not None:
            self.transaction = transaction
        if transaction_type_id is not None:
            self.transaction_type_id = transaction_type_id
        if deleted_at is not None:
            self.deleted_at = deleted_at
        if payment_method_id is not None:
            self.payment_method_id = payment_method_id
        if contact_id is not None:
            self.contact_id = contact_id
        if bank_account_id is not None:
            self.bank_account_id = bank_account_id
        if date is not None:
            self.date = date
        if net_amount is not None:
            self.net_amount = net_amount
        if tax_amount is not None:
            self.tax_amount = tax_amount
        if total_amount is not None:
            self.total_amount = total_amount
        if currency_id is not None:
            self.currency_id = currency_id
        if exchange_rate is not None:
            self.exchange_rate = exchange_rate
        if base_currency_net_amount is not None:
            self.base_currency_net_amount = base_currency_net_amount
        if base_currency_tax_amount is not None:
            self.base_currency_tax_amount = base_currency_tax_amount
        if base_currency_total_amount is not None:
            self.base_currency_total_amount = base_currency_total_amount
        if base_currency_currency_charge is not None:
            self.base_currency_currency_charge = base_currency_currency_charge
        if reference is not None:
            self.reference = reference
        if allocated_artefacts is not None:
            self.allocated_artefacts = allocated_artefacts
        if tax_rate_id is not None:
            self.tax_rate_id = tax_rate_id
        if payment_on_account is not None:
            self.payment_on_account = payment_on_account
        if editable is not None:
            self.editable = editable

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def displayed_as(self):
        return self._displayed_as

    @displayed_as.setter
    def displayed_as(self, displayed_as):
        self._displayed_as = displayed_as

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path):
        self._path = path

    @property
    def created_at(self):
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        self._created_at = created_at

    @property
    def updated_at(self):
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        self._updated_at = updated_at

    @property
    def links(self):
        return self._links

    @links.setter
    def links(self, links):
        self._links = links

    @property
    def transaction(self):
        return self._transaction

    @transaction.setter
    def transaction(self, transaction):
        self._transaction = transaction

    @property
    def transaction_type_id(self):
        return self._transaction_type_id

    @transaction_type_id.setter
    def transaction_type_id(self, transaction_type_id):
        self._transaction_type_id = transaction_type_id

    @property
    def deleted_at(self):
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        self._deleted_at = deleted_at

    @property
    def payment_method_id(self):
        return self._payment_method_id

    @payment_method_id.setter
    def payment_method_id(self, payment_method_id):
        self._payment_method_id = payment_method_id

    @property
    def contact_id(self):
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        self._contact_id = contact_id

    @property
    def bank_account_id(self):
        return self._bank_account_id

    @bank_account_id.setter
    def bank_account_id(self, bank_account_id):
        self._bank_account_id = bank_account_id

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

    @property
    def net_amount(self):
        return self._net_amount

    @net_amount.setter
    def net_amount(self, net_amount):
        self._net_amount = net_amount

    @property
    def tax_amount(self):
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        self._tax_amount = tax_amount

    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        self._total_amount = total_amount

    @property
    def currency_id(self):
        return self._currency_id

    @currency_id.setter
    def currency_id(self, currency_id):
        self._currency_id = currency_id

    @property
    def exchange_rate(self):
        return self._exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, exchange_rate):
        self._exchange_rate = exchange_rate

    @property
    def base_currency_net_amount(self):
        return self._base_currency_net_amount

    @base_currency_net_amount.setter
    def base_currency_net_amount(self, base_currency_net_amount):
        self._base_currency_net_amount = base_currency_net_amount

    @property
    def base_currency_tax_amount(self):
        return self._base_currency_tax_amount

    @base_currency_tax_amount.setter
    def base_currency_tax_amount(self, base_currency_tax_amount):
        self._base_currency_tax_amount = base_currency_tax_amount

    @property
    def base_currency_total_amount(self):
        return self._base_currency_total_amount

    @base_currency_total_amount.setter
    def base_currency_total_amount(self, base_currency_total_amount):
        self._base_currency_total_amount = base_currency_total_amount

    @property
    def base_currency_currency_charge(self):
        return self._base_currency_currency_charge

    @base_currency_currency_charge.setter
    def base_currency_currency_charge(self, base_currency_currency_charge):
        self._base_currency_currency_charge = base_currency_currency_charge

    @property
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, reference):
        self._reference = reference

    @property
    def allocated_artefacts(self):
        return self._allocated_artefacts

    @allocated_artefacts.setter
    def allocated_artefacts(self, allocated_artefacts):
        self._allocated_artefacts = allocated_artefacts

    @property
    def tax_rate_id(self):
        return self._tax_rate_id

    @tax_rate_id.setter
    def tax_rate_id(self, tax_rate_id):
        self._tax_rate_id = tax_rate_id

    @property
    def payment_on_account(self):
        return self._payment_on_account

    @payment_on_account.setter
    def payment_on_account(self, payment_on_account):
        self._payment_on_account = payment_on_account

    @property
    def editable(self):
        return self._editable

    @editable.setter
    def editable(self, editable):
        self._editable = editable

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
        if not isinstance(other, ContactPayment):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, ContactPayment):
            return True
        return self.to_dict() != other.to_dict()
