# StockMovement

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Products & Services`: Full Access
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the item | [optional] 
**displayed_as** | **str** | Display text for the stock movement | [optional] 
**path** | **str** | The API path for the resource | [optional] 
**links** | [**list[Link]**](Link.md) | Links for the resource | [optional] 
**created_at** | **datetime** | The datetime when the item was created | [optional] 
**updated_at** | **datetime** | The datetime when the item was last updated | [optional] 
**movement_number** | **str** | The movement number of the stock movement | [optional] 
**date** | **date** | The date the stock movement occurred | [optional] 
**cost_price** | **float** | The cost per unit of stock purchased | [optional] 
**quantity** | **float** | The quantity of the goods adjusted | [optional] 
**details** | **str** | The transaction details of the stock movement | [optional] 
**reference** | **str** | The reference of the stock movement | [optional] 
**stock_item** | [**StockItem**](StockItem.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


