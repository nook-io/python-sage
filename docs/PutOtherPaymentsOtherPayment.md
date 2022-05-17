# PutOtherPaymentsOtherPayment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_type_id** | **str** | The transaction type of the payment | [optional] 
**date** | **date** | The date of the payment | [optional] 
**total_amount** | **float** | The total amount of the payment | [optional] 
**base_currency_total_itc_amount** | **float** | The total amount of input tax credit in base currency for the                      Other Payment (Canada only) | [optional] 
**total_itc_amount** | **float** | The total amount of input tax credit for the Other Payment (Canada only) | [optional] 
**base_currency_total_itr_amount** | **float** | The total amount of input tax refund in base currency for the                      Other Payment (Canada only) | [optional] 
**total_itr_amount** | **float** | The total amount of input tax refund for the Other Payment (Canada only) | [optional] 
**part_recoverable** | **bool** | Indicates if the Other Payment is part recoverable or not (Canada only) | [optional] 
**payment_method_id** | **str** | The ID of the Payment Method. | [optional] 
**contact_id** | **str** | The ID of the Contact. | [optional] 
**bank_account_id** | **str** | The ID of the Bank Account. | [optional] 
**tax_address_region_id** | **str** | The ID of the Tax Address Region. (Canada only) | [optional] 
**net_amount** | **float** | The net amount of the payment | [optional] 
**tax_amount** | **float** | The tax amount of the payment | [optional] 
**reference** | **str** | A reference of the payment | [optional] 
**withholding_tax_rate** | **float** | IRPF withheld tax rate | [optional] 
**withholding_tax_amount** | **float** | IRPF withheld tax amount | [optional] 
**payment_lines** | [**list[PutOtherPaymentsOtherPaymentPaymentLines]**](PutOtherPaymentsOtherPaymentPaymentLines.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


