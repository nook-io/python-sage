# TaxType

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The tax type id | [optional] 
**displayed_as** | **str** | Display text for the item | [optional] 
**path** | **str** | The API path for the resource | [optional] 
**federal_tax** | **bool** | Indicates whether this is a federal tax type | [optional] 
**country** | [**Base**](Base.md) |  | [optional] 
**address_regions** | [**list[Base]**](Base.md) | The address regions the tax type relates to | [optional] 
**tax_rates** | [**list[Base]**](Base.md) | The tax rates related to the tax type | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


