# PostOtherPaymentsOtherPaymentPaymentLines

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ledger_account_id** | **str** | The ID of the Ledger Account. | 
**total_amount** | **float** | The total amount of the payment line | 
**details** | **str** | The details of the payment line | [optional] 
**tax_rate_id** | **str** | The ID of the Tax Rate. | [optional] 
**net_amount** | **float** | The net amount of the payment line | [optional] 
**tax_amount** | **float** | The tax amount of the payment line | [optional] 
**is_purchase_for_resale** | **bool** | Identifies whether the line item is for resale. (Ireland only) | [optional] 
**trade_of_asset** | **bool** | Whether the line item is marked as trade of asset. | [optional] 
**gst_amount** | **float** | The gst or hst tax amount for the other payment | [optional] 
**pst_amount** | **float** | The pst or qst tax amount for the other payment | [optional] 
**tax_recoverable** | **bool** | Indicates if the other payment is tax recoverable or not | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


