# MigrationTaxReturn

### Endpoint Availability  * Accounting Plus: 🇬🇧, 🇮🇪 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇬🇧, 🇮🇪  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Statutory Reporting`: Full Access
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the item | [optional] 
**displayed_as** | **str** | The name of the resource | [optional] 
**path** | **str** | The API path for the resource | [optional] 
**created_at** | **datetime** | The datetime when the item was created | [optional] 
**updated_at** | **datetime** | The datetime when the item was last updated | [optional] 
**from_date** | **date** | The start date of the tax return | [optional] 
**to_date** | **date** | The end date of the tax return | [optional] 
**tax_return_frequency** | [**Base**](Base.md) |  | [optional] 
**total_amount** | **float** | The total of the tax return | [optional] 
**gb** | [**GBBoxData**](GBBoxData.md) |  | [optional] 
**ie** | [**IEBoxData**](IEBoxData.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


