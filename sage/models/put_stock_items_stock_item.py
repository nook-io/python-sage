import pprint
import six
from sage.configuration import Configuration


class PutStockItemsStockItem(object):
    openapi_types = {
        "item_code": "str",
        "description": "str",
        "sales_ledger_account_id": "str",
        "purchase_ledger_account_id": "str",
        "notes": "str",
        "sales_tax_rate_id": "str",
        "usual_supplier_id": "str",
        "purchase_tax_rate_id": "str",
        "cost_price": "float",
        "source_guid": "str",
        "purchase_description": "str",
        "reorder_level": "float",
        "reorder_quantity": "float",
        "location": "str",
        "barcode": "str",
        "supplier_part_number": "str",
        "weight": "float",
        "measurement_unit": "str",
        "weight_converted": "float",
        "active": "bool",
        "quantity_in_stock": "float",
        "last_cost_price": "float",
        "last_cost_price_stock_value": "float",
        "average_cost_price": "float",
        "average_cost_price_stock_value": "float",
        "cost_price_last_updated": "date",
        "sales_prices": "list[PostProductsProductSalesPrices]",
    }
    attribute_map = {
        "item_code": "item_code",
        "description": "description",
        "sales_ledger_account_id": "sales_ledger_account_id",
        "purchase_ledger_account_id": "purchase_ledger_account_id",
        "notes": "notes",
        "sales_tax_rate_id": "sales_tax_rate_id",
        "usual_supplier_id": "usual_supplier_id",
        "purchase_tax_rate_id": "purchase_tax_rate_id",
        "cost_price": "cost_price",
        "source_guid": "source_guid",
        "purchase_description": "purchase_description",
        "reorder_level": "reorder_level",
        "reorder_quantity": "reorder_quantity",
        "location": "location",
        "barcode": "barcode",
        "supplier_part_number": "supplier_part_number",
        "weight": "weight",
        "measurement_unit": "measurement_unit",
        "weight_converted": "weight_converted",
        "active": "active",
        "quantity_in_stock": "quantity_in_stock",
        "last_cost_price": "last_cost_price",
        "last_cost_price_stock_value": "last_cost_price_stock_value",
        "average_cost_price": "average_cost_price",
        "average_cost_price_stock_value": "average_cost_price_stock_value",
        "cost_price_last_updated": "cost_price_last_updated",
        "sales_prices": "sales_prices",
    }

    def __init__(
        self,
        item_code=None,
        description=None,
        sales_ledger_account_id=None,
        purchase_ledger_account_id=None,
        notes=None,
        sales_tax_rate_id=None,
        usual_supplier_id=None,
        purchase_tax_rate_id=None,
        cost_price=None,
        source_guid=None,
        purchase_description=None,
        reorder_level=None,
        reorder_quantity=None,
        location=None,
        barcode=None,
        supplier_part_number=None,
        weight=None,
        measurement_unit=None,
        weight_converted=None,
        active=None,
        quantity_in_stock=None,
        last_cost_price=None,
        last_cost_price_stock_value=None,
        average_cost_price=None,
        average_cost_price_stock_value=None,
        cost_price_last_updated=None,
        sales_prices=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._item_code = None
        self._description = None
        self._sales_ledger_account_id = None
        self._purchase_ledger_account_id = None
        self._notes = None
        self._sales_tax_rate_id = None
        self._usual_supplier_id = None
        self._purchase_tax_rate_id = None
        self._cost_price = None
        self._source_guid = None
        self._purchase_description = None
        self._reorder_level = None
        self._reorder_quantity = None
        self._location = None
        self._barcode = None
        self._supplier_part_number = None
        self._weight = None
        self._measurement_unit = None
        self._weight_converted = None
        self._active = None
        self._quantity_in_stock = None
        self._last_cost_price = None
        self._last_cost_price_stock_value = None
        self._average_cost_price = None
        self._average_cost_price_stock_value = None
        self._cost_price_last_updated = None
        self._sales_prices = None
        self.discriminator = None
        if item_code is not None:
            self.item_code = item_code
        if description is not None:
            self.description = description
        if sales_ledger_account_id is not None:
            self.sales_ledger_account_id = sales_ledger_account_id
        if purchase_ledger_account_id is not None:
            self.purchase_ledger_account_id = purchase_ledger_account_id
        if notes is not None:
            self.notes = notes
        if sales_tax_rate_id is not None:
            self.sales_tax_rate_id = sales_tax_rate_id
        if usual_supplier_id is not None:
            self.usual_supplier_id = usual_supplier_id
        if purchase_tax_rate_id is not None:
            self.purchase_tax_rate_id = purchase_tax_rate_id
        if cost_price is not None:
            self.cost_price = cost_price
        if source_guid is not None:
            self.source_guid = source_guid
        if purchase_description is not None:
            self.purchase_description = purchase_description
        if reorder_level is not None:
            self.reorder_level = reorder_level
        if reorder_quantity is not None:
            self.reorder_quantity = reorder_quantity
        if location is not None:
            self.location = location
        if barcode is not None:
            self.barcode = barcode
        if supplier_part_number is not None:
            self.supplier_part_number = supplier_part_number
        if weight is not None:
            self.weight = weight
        if measurement_unit is not None:
            self.measurement_unit = measurement_unit
        if weight_converted is not None:
            self.weight_converted = weight_converted
        if active is not None:
            self.active = active
        if quantity_in_stock is not None:
            self.quantity_in_stock = quantity_in_stock
        if last_cost_price is not None:
            self.last_cost_price = last_cost_price
        if last_cost_price_stock_value is not None:
            self.last_cost_price_stock_value = last_cost_price_stock_value
        if average_cost_price is not None:
            self.average_cost_price = average_cost_price
        if average_cost_price_stock_value is not None:
            self.average_cost_price_stock_value = average_cost_price_stock_value
        if cost_price_last_updated is not None:
            self.cost_price_last_updated = cost_price_last_updated
        if sales_prices is not None:
            self.sales_prices = sales_prices

    @property
    def item_code(self):
        return self._item_code

    @item_code.setter
    def item_code(self, item_code):
        self._item_code = item_code

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def sales_ledger_account_id(self):
        return self._sales_ledger_account_id

    @sales_ledger_account_id.setter
    def sales_ledger_account_id(self, sales_ledger_account_id):
        self._sales_ledger_account_id = sales_ledger_account_id

    @property
    def purchase_ledger_account_id(self):
        return self._purchase_ledger_account_id

    @purchase_ledger_account_id.setter
    def purchase_ledger_account_id(self, purchase_ledger_account_id):
        self._purchase_ledger_account_id = purchase_ledger_account_id

    @property
    def notes(self):
        return self._notes

    @notes.setter
    def notes(self, notes):
        self._notes = notes

    @property
    def sales_tax_rate_id(self):
        return self._sales_tax_rate_id

    @sales_tax_rate_id.setter
    def sales_tax_rate_id(self, sales_tax_rate_id):
        self._sales_tax_rate_id = sales_tax_rate_id

    @property
    def usual_supplier_id(self):
        return self._usual_supplier_id

    @usual_supplier_id.setter
    def usual_supplier_id(self, usual_supplier_id):
        self._usual_supplier_id = usual_supplier_id

    @property
    def purchase_tax_rate_id(self):
        return self._purchase_tax_rate_id

    @purchase_tax_rate_id.setter
    def purchase_tax_rate_id(self, purchase_tax_rate_id):
        self._purchase_tax_rate_id = purchase_tax_rate_id

    @property
    def cost_price(self):
        return self._cost_price

    @cost_price.setter
    def cost_price(self, cost_price):
        self._cost_price = cost_price

    @property
    def source_guid(self):
        return self._source_guid

    @source_guid.setter
    def source_guid(self, source_guid):
        self._source_guid = source_guid

    @property
    def purchase_description(self):
        return self._purchase_description

    @purchase_description.setter
    def purchase_description(self, purchase_description):
        self._purchase_description = purchase_description

    @property
    def reorder_level(self):
        return self._reorder_level

    @reorder_level.setter
    def reorder_level(self, reorder_level):
        self._reorder_level = reorder_level

    @property
    def reorder_quantity(self):
        return self._reorder_quantity

    @reorder_quantity.setter
    def reorder_quantity(self, reorder_quantity):
        self._reorder_quantity = reorder_quantity

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        self._location = location

    @property
    def barcode(self):
        return self._barcode

    @barcode.setter
    def barcode(self, barcode):
        self._barcode = barcode

    @property
    def supplier_part_number(self):
        return self._supplier_part_number

    @supplier_part_number.setter
    def supplier_part_number(self, supplier_part_number):
        self._supplier_part_number = supplier_part_number

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        self._weight = weight

    @property
    def measurement_unit(self):
        return self._measurement_unit

    @measurement_unit.setter
    def measurement_unit(self, measurement_unit):
        self._measurement_unit = measurement_unit

    @property
    def weight_converted(self):
        return self._weight_converted

    @weight_converted.setter
    def weight_converted(self, weight_converted):
        self._weight_converted = weight_converted

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, active):
        self._active = active

    @property
    def quantity_in_stock(self):
        return self._quantity_in_stock

    @quantity_in_stock.setter
    def quantity_in_stock(self, quantity_in_stock):
        self._quantity_in_stock = quantity_in_stock

    @property
    def last_cost_price(self):
        return self._last_cost_price

    @last_cost_price.setter
    def last_cost_price(self, last_cost_price):
        self._last_cost_price = last_cost_price

    @property
    def last_cost_price_stock_value(self):
        return self._last_cost_price_stock_value

    @last_cost_price_stock_value.setter
    def last_cost_price_stock_value(self, last_cost_price_stock_value):
        self._last_cost_price_stock_value = last_cost_price_stock_value

    @property
    def average_cost_price(self):
        return self._average_cost_price

    @average_cost_price.setter
    def average_cost_price(self, average_cost_price):
        self._average_cost_price = average_cost_price

    @property
    def average_cost_price_stock_value(self):
        return self._average_cost_price_stock_value

    @average_cost_price_stock_value.setter
    def average_cost_price_stock_value(self, average_cost_price_stock_value):
        self._average_cost_price_stock_value = average_cost_price_stock_value

    @property
    def cost_price_last_updated(self):
        return self._cost_price_last_updated

    @cost_price_last_updated.setter
    def cost_price_last_updated(self, cost_price_last_updated):
        self._cost_price_last_updated = cost_price_last_updated

    @property
    def sales_prices(self):
        return self._sales_prices

    @sales_prices.setter
    def sales_prices(self, sales_prices):
        self._sales_prices = sales_prices

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
        if not isinstance(other, PutStockItemsStockItem):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PutStockItemsStockItem):
            return True
        return self.to_dict() != other.to_dict()
