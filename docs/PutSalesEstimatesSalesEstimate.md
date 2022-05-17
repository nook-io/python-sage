# PutSalesEstimatesSalesEstimate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_id** | **str** | The contact the estimate relates to | [optional] 
**date** | **date** | The date of the estimate | [optional] 
**expiry_date** | **date** | The expiry date of the estimate | [optional] 
**estimate_number_prefix** | **str** | The estimate number prefix | [optional] 
**estimate_number** | **str** | The generated estimate number | [optional] 
**contact_name** | **str** | The name of the contact when the estimate was created | [optional] 
**contact_reference** | **str** | The reference of the contact when the estimate was created | [optional] 
**reference** | **str** | The reference for the estimate | [optional] 
**notes** | **str** | Estimate notes | [optional] 
**terms_and_conditions** | **str** | Estimate terms and conditions | [optional] 
**shipping_net_amount** | **float** | The net shipping amount | [optional] 
**shipping_tax_rate_id** | **str** | The ID of the Shipping Tax Rate. | [optional] 
**shipping_tax_amount** | **float** | The tax shipping amount. NOTE: This is not required for POST/PUT requests as the shipping tax is calculated based on the shipping_net_amount and the shipping_tax_rate. | [optional] 
**shipping_total_amount** | **float** | The total shipping amount | [optional] 
**net_amount** | **float** | The net amount of the estimate | [optional] 
**tax_amount** | **float** | The tax amount of the estimate | [optional] 
**total_amount** | **float** | The total amount of the estimate | [optional] 
**currency_id** | **str** | The ID of the Currency. | [optional] 
**exchange_rate** | **float** | The exchange rate for the estimate | [optional] 
**inverse_exchange_rate** | **float** | The inverse exchange rate for the estimate | [optional] 
**base_currency_shipping_net_amount** | **float** | The net shipping amount in base currency | [optional] 
**base_currency_shipping_tax_amount** | **float** | The tax shipping amount in base currency | [optional] 
**base_currency_shipping_total_amount** | **float** | The total shipping amount in base currency | [optional] 
**total_quantity** | **float** | The total quantity of the estimate | [optional] 
**total_discount_amount** | **float** | The discount amount on the  estimate | [optional] 
**base_currency_total_discount_amount** | **float** | The discount amount on the  estimate in base currency | [optional] 
**base_currency_net_amount** | **float** | The net amount of the estimate in base currency | [optional] 
**base_currency_tax_amount** | **float** | The tax amount of the estimate in base currency | [optional] 
**base_currency_total_amount** | **float** | The total amount of the estimate in base currency | [optional] 
**status_id** | **str** | The ID of the Status. | [optional] 
**sent** | **bool** | Indicates whether the estimate has been sent | [optional] 
**tax_address_region_id** | **str** | The ID of the Tax Address Region. (Canada only) | [optional] 
**withholding_tax_rate** | **float** | IRPF withheld Tax Rate (Spain only) | [optional] 
**withholding_tax_amount** | **float** | IRPF withheld Tax Amount (Spain only) | [optional] 
**base_currency_withholding_tax_amount** | **float** | IRPF withheld Tax Amount (Spain only) in the base currency | [optional] 
**invoice_id** | **str** | The ID of the Invoice. | [optional] 
**main_address** | [**PostSalesCorrectiveInvoicesSalesCorrectiveInvoiceMainAddress**](PostSalesCorrectiveInvoicesSalesCorrectiveInvoiceMainAddress.md) |  | [optional] 
**delivery_address** | [**PostSalesCorrectiveInvoicesSalesCorrectiveInvoiceMainAddress**](PostSalesCorrectiveInvoicesSalesCorrectiveInvoiceMainAddress.md) |  | [optional] 
**estimate_lines** | [**list[PutSalesEstimatesSalesEstimateEstimateLines]**](PutSalesEstimatesSalesEstimateEstimateLines.md) |  | [optional] 
**tax_analysis** | [**list[PostPurchaseCorrectiveInvoicesPurchaseCorrectiveInvoiceTaxAnalysis]**](PostPurchaseCorrectiveInvoicesPurchaseCorrectiveInvoiceTaxAnalysis.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


