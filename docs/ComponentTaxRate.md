# ComponentTaxRate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the item | [optional] 
**displayed_as** | **str** | The name of the resource | [optional] 
**path** | **str** | The API path for the resource | [optional] 
**created_at** | **datetime** | The datetime when the item was created | [optional] 
**updated_at** | **datetime** | The datetime when the item was last updated | [optional] 
**name** | **str** | The name of the tax rate | [optional] 
**agency** | **str** | The agency name (US Only) | [optional] 
**percentage** | **float** | The current tax rate percentage | [optional] 
**percentages** | [**list[TaxRatePercentage]**](TaxRatePercentage.md) | The tax rate percentage and date ranges they apply to | [optional] 
**is_visible** | **bool** | Indicates whether the tax rate is displayed in the application | [optional] 
**retailer** | **bool** | Indicates if tax rate is a retailer rate or not | [optional] 
**editable** | **bool** | Indicates whether a tax rate can be edited | [optional] 
**deletable** | **bool** | Indicates whether a tax rate can be deleted | [optional] 
**is_combined_rate** | **bool** | Indicates whether the tax rate is made up of component tax rates | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


