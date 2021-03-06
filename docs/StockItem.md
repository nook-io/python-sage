# StockItem

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Products & Services`: Restricted Access, Full Access
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the item | [optional] 
**displayed_as** | **str** | The name of the resource | [optional] 
**path** | **str** | The API path for the resource | [optional] 
**created_at** | **datetime** | The datetime when the item was created | [optional] 
**updated_at** | **datetime** | The datetime when the item was last updated | [optional] 
**deleted_at** | **datetime** | The datetime when the item was deleted | [optional] 
**deletable** | **bool** | Indicates whether the stock item can be deleted | [optional] 
**deactivatable** | **bool** | Indicates whether the stock item can be deactivated | [optional] 
**used_on_recurring_invoice** | **bool** | Indicates whether the stock item has been used on a recurring invoice | [optional] 
**item_code** | **str** | The item code for the stock item | [optional] 
**description** | **str** | The stock item description | [optional] 
**notes** | **str** | The notes for the stock item | [optional] 
**sales_ledger_account** | [**Base**](Base.md) |  | [optional] 
**sales_tax_rate** | [**Base**](Base.md) |  | [optional] 
**purchase_ledger_account** | [**Base**](Base.md) |  | [optional] 
**usual_supplier** | [**Contact**](Contact.md) |  | [optional] 
**purchase_tax_rate** | [**Base**](Base.md) |  | [optional] 
**cost_price** | **float** | The cost price of the stock item | [optional] 
**sales_prices** | [**list[SalesPrice]**](SalesPrice.md) | The sales prices for the stock item | [optional] 
**source_guid** | **str** | Used when importing stock items from external sources | [optional] 
**purchase_description** | **str** | The stock item purchase description | [optional] 
**reorder_level** | **float** | The reorder level for the stock item | [optional] 
**reorder_quantity** | **float** | The reorder quantity for the stock item | [optional] 
**location** | **str** | The location for the stock item | [optional] 
**barcode** | **str** | The barcode for the stock item | [optional] 
**supplier_part_number** | **str** | The supplier part number for stock item | [optional] 
**weight** | **float** | The weight of stock item | [optional] 
**measurement_unit** | **str** | The unit of measure of weight for stock item | [optional] 
**weight_converted** | **float** | The weight of stock item converted to the lowest unit of measurement | [optional] 
**active** | **bool** | Indicates whether the stock item is active | [optional] 
**quantity_in_stock** | **float** | The current quantity of the stock item held by the business | [optional] 
**last_cost_price** | **float** | The most recent &#39;purchase invoice&#39; or &#39;adjustment in&#39; price | [optional] 
**last_cost_price_stock_value** | **float** | The value of the current stock in terms of the last cost price | [optional] 
**average_cost_price** | **float** | The average price across all purchases of this stock item | [optional] 
**average_cost_price_stock_value** | **float** | The value of the current stock in terms of the average cost price | [optional] 
**cost_price_last_updated** | **date** | The date on which the last cost price was last updated | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


