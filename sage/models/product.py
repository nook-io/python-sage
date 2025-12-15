import pprint
import six
from sage.configuration import Configuration


class Product(object):
    openapi_types = {
        "id": "str",
        "displayed_as": "str",
        "path": "str",
        "created_at": "datetime",
        "updated_at": "datetime",
        "deleted_at": "datetime",
        "deletable": "bool",
        "deactivatable": "bool",
        "used_on_recurring_invoice": "bool",
        "item_code": "str",
        "description": "str",
        "notes": "str",
        "sales_ledger_account": "Base",
        "sales_tax_rate": "Base",
        "purchase_ledger_account": "Base",
        "usual_supplier": "Contact",
        "purchase_tax_rate": "Base",
        "cost_price": "float",
        "sales_prices": "list[SalesPrice]",
        "source_guid": "str",
        "purchase_description": "str",
        "active": "bool",
        "catalog_item_type": "Base",
    }
    attribute_map = {
        "id": "id",
        "displayed_as": "displayed_as",
        "path": "$path",
        "created_at": "created_at",
        "updated_at": "updated_at",
        "deleted_at": "deleted_at",
        "deletable": "deletable",
        "deactivatable": "deactivatable",
        "used_on_recurring_invoice": "used_on_recurring_invoice",
        "item_code": "item_code",
        "description": "description",
        "notes": "notes",
        "sales_ledger_account": "sales_ledger_account",
        "sales_tax_rate": "sales_tax_rate",
        "purchase_ledger_account": "purchase_ledger_account",
        "usual_supplier": "usual_supplier",
        "purchase_tax_rate": "purchase_tax_rate",
        "cost_price": "cost_price",
        "sales_prices": "sales_prices",
        "source_guid": "source_guid",
        "purchase_description": "purchase_description",
        "active": "active",
        "catalog_item_type": "catalog_item_type",
    }

    def __init__(
        self,
        id=None,
        displayed_as=None,
        path=None,
        created_at=None,
        updated_at=None,
        deleted_at=None,
        deletable=None,
        deactivatable=None,
        used_on_recurring_invoice=None,
        item_code=None,
        description=None,
        notes=None,
        sales_ledger_account=None,
        sales_tax_rate=None,
        purchase_ledger_account=None,
        usual_supplier=None,
        purchase_tax_rate=None,
        cost_price=None,
        sales_prices=None,
        source_guid=None,
        purchase_description=None,
        active=None,
        catalog_item_type=None,
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
        self._deleted_at = None
        self._deletable = None
        self._deactivatable = None
        self._used_on_recurring_invoice = None
        self._item_code = None
        self._description = None
        self._notes = None
        self._sales_ledger_account = None
        self._sales_tax_rate = None
        self._purchase_ledger_account = None
        self._usual_supplier = None
        self._purchase_tax_rate = None
        self._cost_price = None
        self._sales_prices = None
        self._source_guid = None
        self._purchase_description = None
        self._active = None
        self._catalog_item_type = None
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
        if deleted_at is not None:
            self.deleted_at = deleted_at
        if deletable is not None:
            self.deletable = deletable
        if deactivatable is not None:
            self.deactivatable = deactivatable
        if used_on_recurring_invoice is not None:
            self.used_on_recurring_invoice = used_on_recurring_invoice
        if item_code is not None:
            self.item_code = item_code
        if description is not None:
            self.description = description
        if notes is not None:
            self.notes = notes
        if sales_ledger_account is not None:
            self.sales_ledger_account = sales_ledger_account
        if sales_tax_rate is not None:
            self.sales_tax_rate = sales_tax_rate
        if purchase_ledger_account is not None:
            self.purchase_ledger_account = purchase_ledger_account
        if usual_supplier is not None:
            self.usual_supplier = usual_supplier
        if purchase_tax_rate is not None:
            self.purchase_tax_rate = purchase_tax_rate
        if cost_price is not None:
            self.cost_price = cost_price
        if sales_prices is not None:
            self.sales_prices = sales_prices
        if source_guid is not None:
            self.source_guid = source_guid
        if purchase_description is not None:
            self.purchase_description = purchase_description
        if active is not None:
            self.active = active
        if catalog_item_type is not None:
            self.catalog_item_type = catalog_item_type

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
    def deleted_at(self):
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        self._deleted_at = deleted_at

    @property
    def deletable(self):
        return self._deletable

    @deletable.setter
    def deletable(self, deletable):
        self._deletable = deletable

    @property
    def deactivatable(self):
        return self._deactivatable

    @deactivatable.setter
    def deactivatable(self, deactivatable):
        self._deactivatable = deactivatable

    @property
    def used_on_recurring_invoice(self):
        return self._used_on_recurring_invoice

    @used_on_recurring_invoice.setter
    def used_on_recurring_invoice(self, used_on_recurring_invoice):
        self._used_on_recurring_invoice = used_on_recurring_invoice

    @property
    def item_code(self):
        return self._item_code

    @item_code.setter
    def item_code(self, item_code):
        if (
            self.local_vars_configuration.client_side_validation
            and item_code is not None
            and len(item_code) > 255
        ):
            raise ValueError(
                "Invalid value for `item_code`, length must be less than or equal to `255`"
            )
        self._item_code = item_code

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if (
            self.local_vars_configuration.client_side_validation
            and description is not None
            and len(description) > 255
        ):
            raise ValueError(
                "Invalid value for `description`, length must be less than or equal to `255`"
            )
        self._description = description

    @property
    def notes(self):
        return self._notes

    @notes.setter
    def notes(self, notes):
        if (
            self.local_vars_configuration.client_side_validation
            and notes is not None
            and len(notes) > 500
        ):
            raise ValueError(
                "Invalid value for `notes`, length must be less than or equal to `500`"
            )
        self._notes = notes

    @property
    def sales_ledger_account(self):
        return self._sales_ledger_account

    @sales_ledger_account.setter
    def sales_ledger_account(self, sales_ledger_account):
        self._sales_ledger_account = sales_ledger_account

    @property
    def sales_tax_rate(self):
        return self._sales_tax_rate

    @sales_tax_rate.setter
    def sales_tax_rate(self, sales_tax_rate):
        self._sales_tax_rate = sales_tax_rate

    @property
    def purchase_ledger_account(self):
        return self._purchase_ledger_account

    @purchase_ledger_account.setter
    def purchase_ledger_account(self, purchase_ledger_account):
        self._purchase_ledger_account = purchase_ledger_account

    @property
    def usual_supplier(self):
        return self._usual_supplier

    @usual_supplier.setter
    def usual_supplier(self, usual_supplier):
        self._usual_supplier = usual_supplier

    @property
    def purchase_tax_rate(self):
        return self._purchase_tax_rate

    @purchase_tax_rate.setter
    def purchase_tax_rate(self, purchase_tax_rate):
        self._purchase_tax_rate = purchase_tax_rate

    @property
    def cost_price(self):
        return self._cost_price

    @cost_price.setter
    def cost_price(self, cost_price):
        self._cost_price = cost_price

    @property
    def sales_prices(self):
        return self._sales_prices

    @sales_prices.setter
    def sales_prices(self, sales_prices):
        self._sales_prices = sales_prices

    @property
    def source_guid(self):
        return self._source_guid

    @source_guid.setter
    def source_guid(self, source_guid):
        if (
            self.local_vars_configuration.client_side_validation
            and source_guid is not None
            and len(source_guid) > 255
        ):
            raise ValueError(
                "Invalid value for `source_guid`, length must be less than or equal to `255`"
            )
        self._source_guid = source_guid

    @property
    def purchase_description(self):
        return self._purchase_description

    @purchase_description.setter
    def purchase_description(self, purchase_description):
        if (
            self.local_vars_configuration.client_side_validation
            and purchase_description is not None
            and len(purchase_description) > 250
        ):
            raise ValueError(
                "Invalid value for `purchase_description`, length must be less than or equal to `250`"
            )
        self._purchase_description = purchase_description

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, active):
        self._active = active

    @property
    def catalog_item_type(self):
        return self._catalog_item_type

    @catalog_item_type.setter
    def catalog_item_type(self, catalog_item_type):
        self._catalog_item_type = catalog_item_type

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
        if not isinstance(other, Product):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, Product):
            return True
        return self.to_dict() != other.to_dict()
