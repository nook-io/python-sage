# TaxProfile

### Endpoint Availability  * Accounting Plus: 🇨🇦 * Accounting Standard: 🇨🇦 * Accounting Start: 🇨🇦  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Settings`: Full Access
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the item | [optional] 
**displayed_as** | **str** | The name of the resource | [optional] 
**path** | **str** | The API path for the resource | [optional] 
**created_at** | **datetime** | The datetime when the item was created | [optional] 
**updated_at** | **datetime** | The datetime when the item was last updated | [optional] 
**tax_type** | [**Base**](Base.md) |  | [optional] 
**tax_number** | **str** | The tax number | [optional] 
**tax_number_suffix** | **str** | The tax number suffix | [optional] 
**collect_tax** | **bool** | Indicates whether tax is collected for this tax type | [optional] 
**tax_return_frequency** | [**Base**](Base.md) |  | [optional] 
**address_region** | [**AddressRegion**](AddressRegion.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


