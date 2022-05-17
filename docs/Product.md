# Product

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Products & Services`: Restricted Access, Full Access
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the item | [optional] 
**displayed_as** | **str** | The name of the resource | [optional] 
**path** | **str** | The API path for the resource | [optional] 
**created_at** | **datetime** | The datetime when the item was created | [optional] 
**updated_at** | **datetime** | The datetime when the item was last updated | [optional] 
**deleted_at** | **datetime** | The datetime when the item was deleted | [optional] 
**deletable** | **bool** | Indicates whether the product can be deleted | [optional] 
**deactivatable** | **bool** | Indicates whether the product can be deactivated | [optional] 
**used_on_recurring_invoice** | **bool** | Indicates whether the product has been used on a recurring invoice | [optional] 
**item_code** | **str** | The item code for the product | [optional] 
**description** | **str** | The product description | [optional] 
**notes** | **str** | The notes for the product | [optional] 
**sales_ledger_account** | [**Base**](Base.md) |  | [optional] 
**sales_tax_rate** | [**Base**](Base.md) |  | [optional] 
**purchase_ledger_account** | [**Base**](Base.md) |  | [optional] 
**usual_supplier** | [**Contact**](Contact.md) |  | [optional] 
**purchase_tax_rate** | [**Base**](Base.md) |  | [optional] 
**cost_price** | **float** | The cost price of the product | [optional] 
**sales_prices** | [**list[SalesPrice]**](SalesPrice.md) | The sales prices for the product | [optional] 
**source_guid** | **str** | Used when importing products from external sources | [optional] 
**purchase_description** | **str** | The product purchase description | [optional] 
**active** | **bool** | Indicates whether the product is active | [optional] 
**catalog_item_type** | [**Base**](Base.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


