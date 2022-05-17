# OtherPaymentLineItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the item | [optional] 
**displayed_as** | **str** | The name of the resource | [optional] 
**ledger_account** | [**Base**](Base.md) |  | [optional] 
**details** | **str** | The details of the payment line | [optional] 
**tax_rate** | [**Base**](Base.md) |  | [optional] 
**net_amount** | **float** | The net amount of the payment line | [optional] 
**tax_amount** | **float** | The tax amount of the payment line | [optional] 
**total_amount** | **float** | The total amount of the payment line | [optional] 
**tax_breakdown** | [**list[TaxBreakdown]**](TaxBreakdown.md) | The tax breakdown for the payment line | [optional] 
**is_purchase_for_resale** | **bool** | Identifies whether the line item is for resale. (Ireland only) | [optional] 
**trade_of_asset** | **bool** | Whether the line item is marked as trade of asset. | [optional] 
**gst_amount** | **float** | The gst or hst tax amount for the other payment | [optional] 
**pst_amount** | **float** | The pst or qst tax amount for the other payment | [optional] 
**tax_recoverable** | **bool** | Indicates if the other payment is tax recoverable or not | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


