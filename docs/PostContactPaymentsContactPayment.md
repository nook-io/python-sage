# PostContactPaymentsContactPayment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_type_id** | **str** | The transaction type of the payment | 
**contact_id** | **str** | The contact of the payment | 
**bank_account_id** | **str** | The bank account of the payment | 
**date** | **date** | The date the payment was made | 
**total_amount** | **float** | The total amount of the payment | 
**payment_method_id** | **str** | The ID of the Payment Method. | [optional] 
**net_amount** | **float** | The net amount of the payment | [optional] 
**tax_amount** | **float** | The tax amount of the payment | [optional] 
**currency_id** | **str** | The ID of the Currency. | [optional] 
**exchange_rate** | **float** | The exchange rate of the payment | [optional] 
**base_currency_net_amount** | **float** | The net amount of the payment in base currency | [optional] 
**base_currency_tax_amount** | **float** | The tax amount of the payment in base currency | [optional] 
**base_currency_total_amount** | **float** | The total amount of the payment in base currency | [optional] 
**base_currency_currency_charge** | **float** | The currency conversion charges in base currency | [optional] 
**reference** | **str** | A reference for the payment | [optional] 
**tax_rate_id** | **str** | The ID of the Tax Rate. | [optional] 
**allocated_artefacts** | [**list[PostContactPaymentsContactPaymentAllocatedArtefacts]**](PostContactPaymentsContactPaymentAllocatedArtefacts.md) |  | [optional] 
**payment_on_account** | [**PostContactPaymentsContactPaymentPaymentOnAccount**](PostContactPaymentsContactPaymentPaymentOnAccount.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


