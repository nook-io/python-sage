# PostPurchaseCorrectiveInvoicesPurchaseCorrectiveInvoice

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_id** | **str** | The ID of the Contact. | [optional] 
**contact_name** | **str** | The name of the contact when the invoice was created | [optional] 
**contact_reference** | **str** | The reference of the contact when the invoice was created | [optional] 
**date** | **date** | The date of the invoice | [optional] 
**due_date** | **date** | The due date of the invoice | [optional] 
**reference** | **str** | The reference for the invoice | [optional] 
**vendor_reference** | **str** | The vendor reference for the invoice | [optional] 
**notes** | **str** | Invoice notes | [optional] 
**total_quantity** | **float** | The total quantity of the invoice | [optional] 
**net_amount** | **float** | The net amount of the invoice | [optional] 
**tax_amount** | **float** | The tax amount of the invoice | [optional] 
**total_amount** | **float** | The total amount of the invoice | [optional] 
**currency_id** | **str** | The ID of the Currency. | [optional] 
**exchange_rate** | **float** | The exchange rate for the invoice | [optional] 
**inverse_exchange_rate** | **str** | The inverse exchange rate for the credit note | [optional] 
**base_currency_net_amount** | **float** | The net amount of the invoice in base currency | [optional] 
**base_currency_tax_amount** | **float** | The tax amount of the invoice in base currency | [optional] 
**base_currency_total_amount** | **float** | The total amount of the invoice in base currency | [optional] 
**status_id** | **str** | The ID of the Status. | [optional] 
**withholding_tax_rate** | **float** | IRPF withheld Tax Rate (Spain only) | [optional] 
**withholding_tax_amount** | **float** | IRPF withheld Tax Amount (Spain only) | [optional] 
**base_currency_withholding_tax_amount** | **float** | IRPF withheld Tax Amount (Spain only) in the base currency | [optional] 
**original_invoice_id** | **str** | The ID of the Original Invoice. (Spain only) | [optional] 
**original_invoice_number** | **str** | The number relating to the original invoice (Spain only) | [optional] 
**original_invoice_date** | **str** | The Invoice date relating to the original invoice (Spain only) | [optional] 
**invoice_lines** | [**list[PostPurchaseCorrectiveInvoicesPurchaseCorrectiveInvoiceInvoiceLines]**](PostPurchaseCorrectiveInvoicesPurchaseCorrectiveInvoiceInvoiceLines.md) |  | [optional] 
**tax_analysis** | [**list[PostPurchaseCorrectiveInvoicesPurchaseCorrectiveInvoiceTaxAnalysis]**](PostPurchaseCorrectiveInvoicesPurchaseCorrectiveInvoiceTaxAnalysis.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


